#!/usr/bin/env node
/*
 * check-docs.js  documentation drift checker
 *
 * Why this exists. The prompt has a hash discipline, so a prompt that changes is visible.
 * The documents had nothing. An audit on 2026-08-05 found STATUS.md describing a sprint
 * that had already run as not yet started (D1), and reporting a decision as taken at the
 * top and open at the bottom (D2). Around thirty documents cross-reference each other and
 * nothing checked that they still agree.
 *
 * What it checks, and only this:
 *   1. Version drift. The prompt version, the prompt sha, the matcher version, the two
 *      matcher thresholds and the override-record version the renderer emits are all read
 *      out of the code, then every tracked document is checked for a PRESENT-TENSE
 *      assertion of a different value.
 *   2. Dead references. Every relative markdown link is resolved on disk, and every
 *      in-document anchor is resolved against the target's headings.
 *
 * What it deliberately does not check. Claims of state ("labeling has not started"). No
 * mechanical rule distinguishes a stale claim from a true one, and a checker that guesses
 * is a checker people learn to ignore. D1 and D2 were both state claims, so this catches
 * the class of thing they belong to rather than the two instances themselves.
 *
 * Tense. Historical statements are correct and must not be flagged. Tense is decided by
 * looking for a historical marker in the sentence around the token. This is a heuristic
 * and it is tuned to UNDER-flag: a stale present-tense claim sitting in a sentence that
 * happens to contain the word "was" will be missed. That is the intended trade.
 *
 * Opting a document out. A document that is a dated record of a past moment can carry
 *   <!-- check-docs: historical -->
 * in its first 40 lines. Version drift is then skipped for the whole file. Link checking
 * still runs, because a dead link is dead whatever the document's tense.
 *
 * No network. No API. Run it before a commit.
 *   node check-docs.js            report and exit non-zero on any finding
 *   node check-docs.js --quiet    findings only, no clean-file list
 */

'use strict';

const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const V2 = __dirname;

// ---- ground truth, read from the code ------------------------------------
/* Priority 1 in the doc-integrity ordering: a number a script prints beats a number a
 * document remembers. Nothing below is hardcoded. */
function groundTruth() {
  const { loadFrozenPrompt, CONFIG } = require('./run-reviews.js');
  const scorer = require('./score-review.js');
  const prompt = loadFrozenPrompt();
  /* The renderer is code too, and the override record it writes is a versioned contract that
   * documents quote. Added after STATUS.md and index.html disagreed about it within an hour
   * of each other. */
  const renderer = fs.readFileSync(path.join(V2, 'index.html'), 'utf8');
  const rec = /recordVersion:\s*'(override-log-\d+)'/.exec(renderer);
  return {
    promptVersion: CONFIG.promptVersion,
    promptHash: prompt.hash,
    matcherVersion: scorer.MATCHER_VERSION,
    /* mc-match-3 has no cut points. `_thresholds` is gone from score-review.js on purpose, so
     * the ground truth about thresholds is now "there aren't any" and the drift rule below
     * enforces that rather than checking two numbers. */
    hasThresholds: Object.prototype.hasOwnProperty.call(scorer, '_thresholds'),
    recordVersion: rec ? rec[1] : null,
  };
}

// ---- which files ----------------------------------------------------------
/* Tracked markdown only, and not the real-case trees. eval-cases-real/ and eval-runs/
 * carry client material and are out of scope for documentation integrity. */
function trackedDocs() {
  const out = execFileSync('git', ['ls-files', '--', '*.md'], { cwd: V2, encoding: 'utf8' });
  return out.split('\n')
    .map(s => s.trim())
    .filter(Boolean)
    .filter(f => !f.startsWith('eval-cases-real/'))
    .filter(f => !f.startsWith('eval-runs/'))
    .filter(f => !f.startsWith('eval-cases/'))
    .filter(f => !f.startsWith('node_modules/'));
}

/* Untracked working documents in the v2 root are swept too. They are the newest ones and
 * they drift the same way. Nothing outside the root, so this cannot wander into a real
 * case folder. */
function untrackedRootDocs() {
  const out = execFileSync('git', ['ls-files', '--others', '--exclude-standard', '--', '*.md'],
    { cwd: V2, encoding: 'utf8' });
  return out.split('\n')
    .map(s => s.trim())
    .filter(Boolean)
    .filter(f => !f.includes('/'));
}

// ---- masking --------------------------------------------------------------
/* Fenced code blocks are commands, JSON and archived prompt text. A revert command that
 * names the old hash is correct by construction, so fences are masked out before any
 * version check. Line numbers are preserved so a finding still points at a real line. */
function maskFences(text) {
  const lines = text.split('\n');
  let inFence = false;
  return lines.map(l => {
    if (/^\s*```/.test(l)) { inFence = !inFence; return ''; }
    return inFence ? '' : l;
  });
}

// ---- tense ----------------------------------------------------------------
/* Two gates, and a finding has to pass both.
 *
 * The first is a CURRENCY CUE: the sentence has to actually claim the value is the one in
 * force. This is the gate that does the work. Most mentions of an old version in these
 * documents are narrative ("mc-match-1 scores vocabulary overlap", a before/after table
 * row, a revert instruction) and none of them assert currency, so none of them fire. It
 * is a deliberately short list. Growing it trades false positives for catches and the
 * trade is the wrong way round here.
 *
 * The second is a HISTORICAL marker, which vetoes: "the prompt is currently X" is a
 * currency claim, "the prompt was currently X on 08-02" is not. */
const CURRENCY = new RegExp([
  '\\bcurrent(ly)?\\b', '\\bnow\\b', '\\btoday\\b', '\\bat present\\b',
  '\\bpinned to\\b', '\\bfrozen at\\b', '\\bin use\\b', '\\bin force\\b',
  '\\bstands at\\b', '\\bwe run\\b', '\\bruns? at\\b',
  '\\b(the )?(frozen )?prompt is\\b', '\\bthe matcher is\\b', '\\bthe scorer is\\b',
  '\\bthresholds? (is|are)\\b', '\\bthe (prompt|matcher) version is\\b',
].join('|'), 'i');

const HISTORICAL = new RegExp([
  '\\bwas\\b', '\\bwere\\b', '\\bhad\\b', '\\bused\\b', '\\bran\\b', '\\bre-?ran\\b',
  '\\bproduced\\b', '\\bmeasured\\b', '\\bscored\\b', '\\bre-?scored\\b',
  '\\bre-?fitted\\b', '\\barchived?\\b', '\\barchive\\b', '\\bprevious(ly)?\\b',
  '\\bprior\\b', '\\bold\\b', '\\bformer\\b', '\\bbefore\\b', '\\buntil\\b',
  '\\bsupersede[ds]?\\b', '\\bhistoric(al)?\\b', '\\brevert\\b', '\\bback to\\b',
  '\\bchanged\\b', '\\bmoved\\b', '\\bbumped?\\b', '\\breplaced?\\b',
  '\\bas of\\b', '\\bat the time\\b', '\\bno longer\\b', '\\bstale\\b',
  '\\d{4}-\\d{2}-\\d{2}',           // an explicit date pins the claim to a moment
  '\\bto\\s+[`*]*\\d',              // a transition: "0.45 to 0.39"
].join('|'), 'i');

/* The sentence around a hit, so "The 08-02 run used X" is judged whole rather than by the
 * fragment the regex matched. Table rows are bounded by the cell, which is the right unit:
 * a before/after table row carries its own marker. */
function contextFor(line, index) {
  if (line.includes('|')) {
    const cells = line.split('|');
    let at = 0;
    for (const c of cells) {
      if (index >= at && index < at + c.length) return c;
      at += c.length + 1;
    }
  }
  /* Sentence boundaries have to survive markdown emphasis: "known.** `mc-match-1`" is two
   * sentences, and reading it as one is how "The cause is now known" lent its "now" to the
   * clause after it. */
  const BOUND = /[.;:!?][)"'*_`\]]*\s/g;
  let start = 0;
  let m;
  BOUND.lastIndex = 0;
  while ((m = BOUND.exec(line)) !== null && m.index < index) start = m.index + m[0].length;
  BOUND.lastIndex = index;
  const end = (m = BOUND.exec(line)) !== null ? m.index + 1 : line.length;
  return line.slice(start, end);
}

/* True when the offset sits inside a double-quoted span. Documents quote each other, and a
 * quoted example of a wrong claim is not a wrong claim. */
function insideQuotes(line, index) {
  let count = 0;
  for (let i = 0; i < index; i++) if (line[i] === '"') count++;
  return count % 2 === 1;
}

// ---- check 1: version drift ----------------------------------------------
function checkVersions(file, lines, gt, findings) {
  const rules = [
    {
      what: 'prompt version',
      re: /\bfrozen-\d{4}-\d{2}-\d{2}[a-z]?\b/g,
      ok: m => m === gt.promptVersion,
      current: gt.promptVersion,
    },
    {
      what: 'prompt sha',
      re: /\b[0-9a-f]{16}\b/g,
      ok: m => m === gt.promptHash,
      current: gt.promptHash,
    },
    {
      what: 'matcher version',
      re: /\bmc-match-(\d+)\b/g,
      /* A version above the current one is a plan, not drift. mc-match-3 is the next
       * build and every document that names it is right to. */
      ok: (m, cap) => m === gt.matcherVersion
        || Number(cap) > Number(/(\d+)$/.exec(gt.matcherVersion)[1]),
      current: gt.matcherVersion,
    },
    {
      what: 'override record version',
      re: /\boverride-log-(\d+)\b/g,
      /* Same rule as the matcher: a version above the current one is a plan, and a version
       * below it is real history that documents are right to describe. */
      ok: (m, cap) => !gt.recordVersion || m === gt.recordVersion
        || Number(cap) > Number(/(\d+)$/.exec(gt.recordVersion)[1]),
      current: gt.recordVersion,
    },
    {
      /* The matcher had cut points until 2026-08-08 and no longer does. A document that talks
       * about T_HIT or T_NEAR in the present tense is describing an instrument that does not
       * exist. Past-tense mentions are fine and are what 21-scorer-refit-sprint.md is full of;
       * the HISTORICAL and CURRENCY guards below sort them out. */
      what: 'threshold constant',
      re: /T_(?:HIT|NEAR)/g,
      ok: () => gt.hasThresholds,
      current: 'removed: ' + gt.matcherVersion + ' is an LLM judge and has no cut points',
    },
  ];

  lines.forEach((line, i) => {
    for (const rule of rules) {
      rule.re.lastIndex = 0;
      let m;
      while ((m = rule.re.exec(line)) !== null) {
        if (rule.ok(m[0], m[1])) continue;
        if (insideQuotes(line, m.index)) continue;
        /* Strip version tokens before judging tense. `frozen-2026-08-03` carries a date
         * inside it, and left in place that date reads as a historical marker and vetoes
         * the very claim it is part of. */
        const ctx = contextFor(line, m.index).replace(/frozen-\d{4}-\d{2}-\d{2}[a-z]?/g, '');
        if (!CURRENCY.test(ctx)) continue;
        if (HISTORICAL.test(ctx)) continue;
        findings.push({
          file, line: i + 1, kind: 'drift',
          msg: rule.what + ' reads ' + (rule.threshold ? m[1] : m[0]) + ', current is ' + rule.current,
          text: line.trim().slice(0, 110),
        });
      }
    }
  });
}

// ---- check 2: dead references --------------------------------------------
function slug(heading) {
  return heading.toLowerCase()
    .replace(/[`*_]/g, '')
    .replace(/[^\w\s-]/g, '')
    .trim()
    .replace(/\s+/g, '-');
}

const anchorCache = new Map();
function anchorsOf(absPath) {
  if (anchorCache.has(absPath)) return anchorCache.get(absPath);
  let set = new Set();
  try {
    for (const l of fs.readFileSync(absPath, 'utf8').split('\n')) {
      const m = /^#{1,6}\s+(.*)$/.exec(l);
      if (m) set.add(slug(m[1]));
    }
  } catch (_) { /* unreadable target is reported by the file check, not here */ }
  anchorCache.set(absPath, set);
  return set;
}

function checkLinks(file, lines, findings) {
  const abs = path.join(V2, file);
  const dir = path.dirname(abs);
  lines.forEach((line, i) => {
    const re = /\[[^\]]*\]\(([^)\s]+)\)/g;
    let m;
    while ((m = re.exec(line)) !== null) {
      const target = m[1];
      if (/^(https?:|mailto:|#)/.test(target) === true && target[0] !== '#') continue;
      if (target.startsWith('#')) {
        if (!anchorsOf(abs).has(target.slice(1).toLowerCase())) {
          findings.push({ file, line: i + 1, kind: 'link',
            msg: 'anchor ' + target + ' does not exist in this file', text: line.trim().slice(0, 110) });
        }
        continue;
      }
      const [rel, frag] = target.split('#');
      const resolved = path.resolve(dir, decodeURI(rel));
      if (!fs.existsSync(resolved)) {
        findings.push({ file, line: i + 1, kind: 'link',
          msg: 'link target ' + rel + ' does not exist', text: line.trim().slice(0, 110) });
        continue;
      }
      if (frag && fs.statSync(resolved).isFile() && !anchorsOf(resolved).has(frag.toLowerCase())) {
        findings.push({ file, line: i + 1, kind: 'link',
          msg: 'anchor #' + frag + ' does not exist in ' + rel, text: line.trim().slice(0, 110) });
      }
    }
  });
}

/* ---- provenance: the rubric and the source register must agree -------------------
 * 10-source-register.md says which rubric dimensions each source grounds, and the rubric
 * names its sources in each dimension heading. Nothing kept the two in step, and by
 * 2026-08-31 they had drifted three ways: a dimension with no registered source, a source
 * claiming a dimension whose heading never named it, and a heading naming a source the
 * register maps elsewhere. Names alone cannot be compared, so the headings now carry
 * S-numbers and this checks both directions. */
function checkProvenance(root) {
  const reg = fs.readFileSync(path.join(root, '10-source-register.md'), 'utf8');
  const rub = fs.readFileSync(path.join(root, '01-rubric-v1.md'), 'utf8');
  const problems = [];

  const claims = {};
  for (const b of reg.split('\n### ').slice(1)) {
    const sid = (b.match(/^(S\d+)\./) || [])[1];
    if (!sid) continue;
    const dl = b.match(/\*\*Dimensions\.\*\*[ \t]*([^\n]+)/);
    claims[sid] = dl ? (dl[1].match(/\d+/g) || []).map(Number) : [];
  }

  const heads = {};
  for (const m of rub.matchAll(/### Dimension (\d+)\.[^[\n]*\[([^\]]*)\]/g)) {
    heads[Number(m[1])] = {
      sids: m[2].match(/S\d+/g) || [],
      none: /NO REGISTERED SOURCE/.test(m[2]),
    };
  }

  for (const sid of Object.keys(claims)) {
    for (const d of claims[sid]) {
      if (heads[d] && !heads[d].sids.includes(sid)) {
        problems.push(sid + ' claims dimension ' + d + ', whose heading does not name it');
      }
    }
  }
  for (const d of Object.keys(heads)) {
    for (const sid of heads[d].sids) {
      if (claims[sid] && !claims[sid].includes(Number(d))) {
        problems.push('dimension ' + d + ' names ' + sid + ', which does not list dimension ' + d);
      }
    }
  }
  for (let d = 1; d <= 10; d++) {
    if (heads[d] && heads[d].sids.length === 0 && !heads[d].none) {
      problems.push('dimension ' + d + ' names no source and is not marked as having none');
    }
  }
  return problems;
}

// ---- main -----------------------------------------------------------------
function main(argv) {
  const quiet = argv.includes('--quiet');
  const gt = groundTruth();
  const files = [...new Set([...trackedDocs(), ...untrackedRootDocs()])].sort();

  console.log('check-docs  ground truth from the code');
  console.log('  prompt   ' + gt.promptVersion + '  sha256:' + gt.promptHash);
  console.log('  matcher  ' + gt.matcherVersion + (gt.hasThresholds ? '  (has cut points)' : '  (no cut points, LLM judge)'));
  console.log('  record   ' + (gt.recordVersion || 'not found in index.html'));
  console.log('  scope    ' + files.length + ' markdown documents\n');

  const findings = [];
  const historical = [];
  const clean = [];

  for (const file of files) {
    const abs = path.join(V2, file);
    let raw;
    try { raw = fs.readFileSync(abs, 'utf8'); } catch (_) { continue; }
    const masked = maskFences(raw);
    const isHistorical = /<!--\s*check-docs:\s*historical\s*-->/.test(raw.split('\n').slice(0, 40).join('\n'));

    const before = findings.length;
    if (!isHistorical) checkVersions(file, masked, gt, findings);
    checkLinks(file, masked, findings);
    if (isHistorical) historical.push(file);
    else if (findings.length === before) clean.push(file);
  }

  if (findings.length === 0) {
    console.log('clean. ' + files.length + ' documents, no version drift, no dead references.');
  } else {
    let last = null;
    for (const f of findings) {
      if (f.file !== last) { console.log(f.file); last = f.file; }
      console.log('  ' + String(f.line).padStart(5) + '  ' + f.kind.toUpperCase() + '  ' + f.msg);
      console.log('         ' + f.text);
    }
    console.log('\n' + findings.length + ' finding' + (findings.length === 1 ? '' : 's') + '.');
  }

  /* The bundle check, joined here 2026-09-20 (ticket 20 Group F). It is the drift check
   * for the artifacts a person actually pastes: the generated test-kit pastes against
   * their sources, every release against the sources it records, the register against the
   * release folders, and paste 2's record stamp against build-bundle.js's PROMPT_VERSION.
   * Two hand-maintained derivatives went stale undetected before this existed, which is
   * why the recommendation was a check rather than a pin: a check catches the class. */
  let bundleFailed = false;
  try {
    console.log('');
    bundleFailed = require('./build-bundle.js').cmdCheck() !== 0;
  } catch (e) {
    console.log('build-bundle --check could not run: ' + e.message);
    bundleFailed = true;
  }

  const prov = checkProvenance(V2);
  if (prov.length) {
    console.log('\nPROVENANCE, 01-rubric-v1.md against 10-source-register.md:');
    for (const x of prov) console.log('  ' + x);
  }

  if (!quiet) {
    if (historical.length) {
      console.log('\nversion checks skipped (marked historical): ' + historical.join(', '));
    }
    console.log('\nchecked and clean: ' + clean.length + ' of ' + files.length);
  }

  console.log('\nThis checks version strings and references only. It does not check claims of');
  console.log('state, and the tense heuristic is tuned to under-flag. A clean run is not a');
  console.log('guarantee that the documents agree with each other.');

  return findings.length === 0 && !bundleFailed ? 0 : 1;
}

if (require.main === module) process.exit(main(process.argv.slice(2)));
module.exports = { groundTruth, slug };
