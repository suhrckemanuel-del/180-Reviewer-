'use strict';
// Software regression checks using an existing private review, never a model or invented deck.
// node review-view.test.js <private saved review> <private evidence JSON>
const fs = require('node:fs');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const { parseReview, renderReview, assertPrivateOutput } = require('./review-view');
const bundle = require('./build-bundle');
const [reviewPath, evidencePath] = process.argv.slice(2);
if (!reviewPath || !evidencePath) throw new Error('Provide a saved private review and its evidence JSON');
const raw = fs.readFileSync(reviewPath, 'utf8');
const evidence = JSON.parse(fs.readFileSync(evidencePath, 'utf8'));
const parsed = parseReview(raw, evidence);
assert.equal(parsed.rawReview, raw);
assert.equal(parsed.sourceHash, crypto.createHash('sha256').update(raw).digest('hex'));
assert(parsed.quoteChecks.length >= parsed.findings.length);
for (const finding of parsed.findings) {
  const body = finding.text.slice(finding.text.indexOf('\n') + 1).trim().replace(/\s+/g, ' ');
  const rebuilt = finding.fields.map(field => (field.sourceLabel ? field.sourceLabel + ': ' : '') + field.text.trim()).join(' ').replace(/\s+/g, ' ');
  assert.equal(rebuilt, body, 'Standard fields must retain every source field and quote');
  assert(finding.fields.every(field => ['Evidence', 'Issue', 'Why it matters', 'Next step', 'Question'].includes(field.label)));
}
const dataFromHtml = html => JSON.parse(html.match(/<script id="review-data" type="application\/json">([\s\S]*?)<\/script>/)[1]);
assert.deepEqual(dataFromHtml(renderReview(parsed)), parsed);
const escaped = { ...parsed, title: '</script><img src=x onerror=alert(1)> $&', rawReview: raw + '\n$& </script>' };
assert.deepEqual(dataFromHtml(renderReview(escaped)), escaped);
assert.throws(() => parseReview(raw.replace(/KEYS:\s*\S+/, 'KEYS: MISSING/MISSING'), evidence), /keys/i);
assert.throws(() => parseReview(raw + '\nScore: 4', evidence), /retired/i);
assert.throws(() => parseReview(raw + '\nWHAT WORKS\n', evidence), /duplicate/i);
if (parsed.findings.length) {
  assert.throws(() => parseReview(raw.replace(/COUNT:\s*\d+/, 'COUNT: 999'), evidence), /COUNT/);
  const quote = parsed.quoteChecks.find(q => q.owner !== 'strengths');
  assert.throws(() => parseReview(raw.replace(quote.text, 'QUOTE_MUTATION_FOR_SOFTWARE_TEST'), evidence), /quote/i);
  assert.throws(() => parseReview(raw.replace('[' + parsed.findings[0].severity + ']', '[Undefined]'), evidence), /severity/i);
  const excluded = structuredClone(evidence);
  excluded.pages = excluded.pages.filter(p => p.pdf_page !== quote.page);
  assert.throws(() => parseReview(raw, excluded), /page|quote/i);
}
const zeroSections = parsed.sections.map(s => ({ ...s, text: ['FINDINGS, IN ORDER', 'WHAT TO FIX, IN ORDER'].includes(s.title) ? 'COUNT: 0 high impact, 0 moderate, 0 minor\nNo findings recorded.\n' : s.text }));
const zeroRaw = zeroSections.map(s => (s.title === 'Review context' ? '' : s.title + '\n') + s.text).join('\n');
assert.equal(parseReview(zeroRaw, evidence).findings.length, 0);
assert.throws(() => assertPrivateOutput(require('node:path').join(__dirname, 'client-output.html')), /_client-private/);
const files = bundle.buildRelease({ k1: '1005-QATEST', k2: 'QATEST-22' }, 'https://example.invalid/local-test');
const manifest = JSON.parse(files['MANIFEST.json']);
for (const [name, meta] of Object.entries(manifest.files)) {
  assert.equal(meta.sha256, crypto.createHash('sha256').update(files[name]).digest('hex'));
}
assert(files['COVER-SHEET.md'].includes('KEYS: 1005-QATEST/QATEST-22'));
assert(!files['STUDENT-SETUP.txt'].match(/<<[A-Z_]+>>/));
for (const audience of ['student','lead']) {
  const setup = files[audience.toUpperCase() + '-SETUP.txt'];
  assert(setup.includes('AUDIENCE: ' + audience + ' | VERSION: ' + bundle.PROMPT_VERSION));
  assert(!setup.match(/<<[A-Z_]+>>/));
  assert(!setup.includes('=== PASTE-BACK RECORD ==='));
  assert.equal(setup.includes('AFTER THE FULL REVIEW ('),audience==='student');
  const html = renderReview(parsed,audience);
  assert.deepEqual(dataFromHtml(html),parsed);
  assert(!html.includes('class="mode-switch"'));
  assert.equal(html.includes('id="lead-summary"'),audience==='lead');
}
assert.throws(()=>parseReview(raw.replace('REVIEW OF:', 'AUDIENCE: lead | VERSION: test\nREVIEW OF:'),evidence),/Audience/);
console.log('Review preservation, escaping, quote/page rejection, zero findings, private output and bundle checks passed.');
