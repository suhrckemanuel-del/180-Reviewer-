#!/usr/bin/env node
'use strict';
// Render the completed review. No model call, second analysis or client data in this file.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { execFileSync } = require('node:child_process');
const hash = text => crypto.createHash('sha256').update(text).digest('hex');
const normalize = text => text.replace(/\s+/gu, ' ').trim();
const HEADINGS = new Set(['BEFORE YOU USE THIS', 'WHAT WORKS', 'FINDINGS, IN ORDER',
  'WHAT TO FIX, IN ORDER', 'WHAT THIS REVIEW COULD NOT JUDGE', 'QUESTIONS WORTH ASKING THE TEAM',
  'HOW TO CHECK THIS FEEDBACK', 'AFTER THE FULL REVIEW', 'PASTE-BACK RECORD']);

function findingFields(text) {
  const labels = { Evidence: 'Evidence', Where: 'Evidence', Quote: 'Evidence',
    'The problem': 'Issue', 'Why it matters': 'Why it matters', 'Why it costs the client': 'Why it matters',
    'Do this': 'Next step', 'What to do': 'Next step', 'Next step': 'Next step',
    'Answer first': 'Question', Question: 'Question' };
  const fields = [];
  let current = { label: 'Evidence', text: '' };
  for (const line of text.slice(text.indexOf('\n') + 1).split('\n')) {
    const match = line.match(/^\s*(Evidence|Where|Quote|The problem|Why it matters|Why it costs the client|Do this|What to do|Next step|Answer first|Question):\s*(.*)$/);
    if (match) {
      if (current.text.trim()) fields.push(current);
      current = { label: labels[match[1]], sourceLabel: match[1], text: match[2] + '\n' };
    } else current.text += line + '\n';
  }
  if (current.text.trim()) fields.push(current);
  return fields;
}

function references(text) {
  const pages = new Set();
  for (const m of text.matchAll(/\b(?:PDF\s+)?p(?:p|age)?\.?\s*(\d+)(?:\s*[-–]\s*(\d+))?/gi)) {
    const first = Number(m[1]), last = Number(m[2] || first);
    if (last < first || last - first > 500) throw new Error('Invalid page reference range');
    for (let n = first; n <= last; n++) pages.add(n);
  }
  return [...pages];
}

function parseReview(raw, pageDocument) {
  if (typeof raw !== 'string' || !raw.trim()) throw new Error('The completed review is empty');
  const keys = raw.match(/\bKEYS:\s*([A-Za-z0-9-]+\/[A-Za-z0-9-]+)/);
  if (!keys || /MISSING/.test(keys[1])) throw new Error('Missing or incomplete setup keys');
  const header = raw.match(/REVIEW OF:\s*(.*?)\s*\|\s*MODE:\s*(short|deep|lead)\b/);
  if (!header) throw new Error('Missing REVIEW OF / MODE header');
  // Reject affirmative retired output fields, not explanations such as "There is no grade".
  if (/^\s*(?:\*\*)?(?:overall (?:score|grade|rating)|readiness(?: level)?|confidence(?: level)?|grade|score)\s*:/im.test(raw)
      || /"(?:overallScore|readinessLevel|confidence|readinessCall\.ai)"\s*:/i.test(raw)) {
    throw new Error('Retired grade, score, confidence or readiness field in review');
  }
  if (!pageDocument || !Array.isArray(pageDocument.pages) || !pageDocument.pages.length) {
    throw new Error('Page-marked evidence JSON is required');
  }
  const pageMap = new Map();
  for (const p of pageDocument.pages) {
    if (!Number.isInteger(p.pdf_page) || p.pdf_page < 1 || typeof p.text !== 'string' || pageMap.has(p.pdf_page)) {
      throw new Error('Invalid or duplicate evidence page');
    }
    pageMap.set(p.pdf_page, normalize(p.text));
  }
  const pageCount = pageDocument.pageCount || Math.max(...pageMap.keys());
  if (!Number.isInteger(pageCount) || pageCount < Math.max(...pageMap.keys()) || pageCount > 10000) throw new Error('Invalid page count');
  const audienceHeader = raw.match(/^AUDIENCE: (student|lead) \| VERSION: (\S+)/m);
  if (audienceHeader && ((audienceHeader[1] === 'lead') !== (header[2] === 'lead'))) throw new Error('Audience and MODE disagree');
  const sections = [];
  const seenHeadings = new Set();
  let current = { title: 'Review context', text: '' };
  for (const line of raw.replace(/\r\n/g, '\n').split('\n')) {
    const heading = line.replace(/^#{1,6}\s+/, '').replace(/^\*\*|\*\*$/g, '').trim();
    if (HEADINGS.has(heading)) {
      if (seenHeadings.has(heading)) throw new Error('Duplicate review section: ' + heading);
      seenHeadings.add(heading); sections.push(current); current = { title: heading, text: '' };
    }
    else current.text += line + '\n';
  }
  sections.push(current);
  const strengths = sections.find(s => s.title === 'WHAT WORKS');
  const findingSections = sections.filter(s => ['FINDINGS, IN ORDER', 'WHAT TO FIX, IN ORDER'].includes(s.title));
  if (!strengths || findingSections.length !== 1 || !sections.some(s => s.title === 'WHAT THIS REVIEW COULD NOT JUDGE')) {
    throw new Error('Review must contain strengths, findings and assessment limitations');
  }
  const findingSection = findingSections[0];
  const starts = [...findingSection.text.matchAll(/^\s*(\d+)\.\s+(.+?)\s*\[(High impact|Moderate|Minor)\]\s*$/gm)];
  if ([...findingSection.text.matchAll(/^\s*\d+\.\s+.*\[[^\]]+\]\s*$/gm)].length !== starts.length) {
    throw new Error('Unrecognized finding severity');
  }
  const findings = starts.map((m, i) => ({
    id: 'f' + (i + 1), number: Number(m[1]), title: m[2], severity: m[3],
    text: findingSection.text.slice(m.index, starts[i + 1]?.index ?? findingSection.text.length).trim(),
  }));
  if (findings.some((f, i) => f.number !== i + 1)) throw new Error('Finding numbering must be consecutive');
  if (findings.length > (header[2] === 'short' ? 3 : 5)) throw new Error('Finding budget exceeded');
  const count = findingSection.text.match(/COUNT:\s*(\d+) high impact,\s*(\d+) moderate,\s*(\d+) minor/i);
  if (!count || ['High impact', 'Moderate', 'Minor'].some((s, i) => Number(count[i + 1]) !== findings.filter(f => f.severity === s).length)) {
    throw new Error('COUNT does not match finding severities');
  }
  findingSection.intro = findingSection.text.slice(0, starts[0]?.index ?? findingSection.text.length).trim();
  const quoteChecks = [];
  function checkQuotes(text, owner) {
    // Paragraph scope supports inline strengths and multiple separately quoted table cells.
    for (const paragraph of text.split(/\n\s*\n/)) {
      const paragraphsPages = references(paragraph);
      const quotes = [...paragraph.matchAll(/“([^”]+)”|"([^"\n]+)"/g)];
      for (const q of quotes) {
        const quote = q[1] || q[2];
        const line = paragraph.slice(paragraph.lastIndexOf('\n', q.index) + 1,
          paragraph.indexOf('\n', q.index) === -1 ? undefined : paragraph.indexOf('\n', q.index));
        const linePages = references(line);
        const locations = linePages.length ? linePages : paragraphsPages;
        if (!locations.length) throw new Error(owner + ': quote lacks a page reference');
        const matched = locations.find(p => pageMap.get(p)?.includes(normalize(quote)));
        if (!matched) throw new Error(owner + ': quote ' + (quoteChecks.length + 1) + ' not found on cited pages ' + locations.join(', '));
        quoteChecks.push({ owner, page: matched, text: quote });
      }
    }
  }
  checkQuotes(strengths.text, 'strengths');
  for (const f of findings) {
    f.fields = findingFields(f.text);
    f.pages = references(f.text);
    if (!f.pages.length || f.pages.some(p => !pageMap.has(p))) throw new Error(f.id + ': unavailable evidence page');
    const before = quoteChecks.length;
    checkQuotes(f.text, f.id);
    if (before === quoteChecks.length) throw new Error(f.id + ': finding has no verifiable quote');
  }
  for (const p of references(raw)) if (!pageMap.has(p)) throw new Error('Review references an excluded or unavailable page: ' + p);
  return { schemaVersion: 'review-view-1', title: header[1], mode: header[2], keys: keys[1],
    promptVersion: audienceHeader?.[2] || null,
    sourceHash: hash(raw), documentHash: pageDocument.sha256 || null, rawReview: raw, pageCount, includedPages: [...pageMap.keys()],
    sections, findings, quoteChecks,
    evidenceStatus: 'Quotes matched page-marked text. Visual meaning and findings still require human checking.' };
}

function renderReview(review, audience = review.mode === 'lead' ? 'lead' : 'student') {
  if (!['student','lead'].includes(audience)) throw new Error('Unknown audience');
  const template = fs.readFileSync(path.join(__dirname, audience + '-review.template.html'), 'utf8');
  const css = fs.readFileSync(path.join(__dirname, 'review-view.css'), 'utf8').replace(/^\uFEFF/, '');
  const client = fs.readFileSync(path.join(__dirname, 'review-view.client.js'), 'utf8');
  const data = JSON.stringify(review).replace(/</g, '\\u003c').replace(/\u2028/g, '\\u2028').replace(/\u2029/g, '\\u2029');
  return template.replace('/* VIEW_CSS */', () => css).replace('/* VIEW_CLIENT */', () => client).replace('"VIEW_DATA"', () => data);
}

function assertPrivateOutput(filename) {
  const repo = execFileSync('git', ['rev-parse', '--show-toplevel'], { cwd: __dirname, encoding: 'utf8', stdio: ['ignore','pipe','pipe'] }).trim();
  const privateRoot = path.join(repo, '_client-private');
  const target = path.resolve(filename);
  const relative = path.relative(privateRoot, target);
  if (!relative || relative.startsWith('..') || path.isAbsolute(relative)) throw new Error('Output must be inside repository _client-private');
  // Existing parents must not redirect through a junction outside the private area.
  let parent = path.dirname(target);
  while (!fs.existsSync(parent)) parent = path.dirname(parent);
  const real = path.relative(fs.realpathSync(privateRoot), fs.realpathSync(parent));
  if (real.startsWith('..') || path.isAbsolute(real)) throw new Error('Output parent resolves outside _client-private');
  if (fs.existsSync(target) && fs.lstatSync(target).isSymbolicLink()) throw new Error('Output may not be a symbolic link');
  execFileSync('git', ['-c', 'safe.directory=' + repo.replace(/\\/g, '/'), 'check-ignore', '--quiet', '--', target], { cwd: repo, stdio: 'pipe' });
  return target;
}

function main(argv) {
  const option = name => { const i = argv.indexOf(name); return i >= 0 ? argv[i + 1] : null; };
  if (argv.includes('--help') || !option('--review')) {
    console.log('node review-view.js --review completed-review.md --pages evidence.json --audience student|lead --out _client-private/run/student-review.html|lead-review.html');
    return;
  }
  if (!option('--pages') || !option('--out')) throw new Error('--pages and --out are required');
  const output = assertPrivateOutput(option('--out'));
  const raw = fs.readFileSync(option('--review'), 'utf8');
  const pages = JSON.parse(fs.readFileSync(option('--pages'), 'utf8'));
  const review = parseReview(raw, pages);
  const audience = option('--audience') || (review.mode === 'lead' ? 'lead' : 'student');
  if (!['student','lead'].includes(audience)) throw new Error('Use --audience student or lead');
  const savedAudience = raw.match(/^AUDIENCE: (student|lead) \| VERSION: (\S+)/m)?.[1] || (review.mode === 'lead' ? 'lead' : 'student');
  if (savedAudience !== audience && !argv.includes('--historical-preview')) throw new Error('Audience mismatch; use the matching view. Historical previews require --historical-preview and --provenance');
  if (argv.includes('--historical-preview') && !option('--provenance')) throw new Error('Historical preview requires accurate --provenance');
  review.audience = audience;
  review.provenance = option('--provenance') || 'Completed ' + audience + ' review. No new analysis performed.';
  const html = renderReview(review, audience);
  fs.mkdirSync(path.dirname(output), { recursive: true });
  fs.writeFileSync(output, html);
  console.log('Rendered ' + review.findings.length + ' unchanged findings; ' + review.quoteChecks.length + ' quotes matched.');
  console.log(output);
}
if (require.main === module) {
  try { main(process.argv.slice(2)); } catch (error) { console.error('Review view refused: ' + error.message); process.exitCode = 1; }
}
module.exports = { parseReview, renderReview, references, assertPrivateOutput };
