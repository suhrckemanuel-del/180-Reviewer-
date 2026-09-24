#!/usr/bin/env node
/*
 * mc-match-3.js — an LLM judge for "does this AI finding catch this gold issue?", and the
 * harness that validates it against the 178-pair set.
 *
 * WHY THIS EXISTS
 *
 * mc-match-2 scores vocabulary overlap. The judgement that matters is whether two texts
 * describe the same underlying problem. 21-scorer-refit-sprint.md section 5 measured the
 * price of that substitution: AUC 0.718, and 88% accuracy at the best possible cut point
 * against 85% for a constant that ignores the input entirely. Three points of discriminative
 * power. No threshold fixes that, because the threshold was never the problem.
 *
 * DETERMINISM
 *
 * A scorer that returns different numbers on the same input is not a measurement instrument.
 * An LLM judge is not deterministic, so determinism is manufactured and then measured:
 *
 *   - one frozen prompt, hashed, its digest recorded on every verdict
 *   - N draws per pair, majority vote, ties resolved DOWN (conservative)
 *   - every draw cached by a hash of (prompt digest, role, draw index, pair text), so a
 *     re-score never re-calls a model and needs no API key
 *   - the rate at which the N draws disagreed is reported, always. That number is the honest
 *     confidence interval on every score this project publishes afterwards.
 *
 * THE TARGET IS NOT GROUND TRUTH
 *
 * The labels are LLM adjudications. Validating an LLM judge against them measures agreement
 * between two LLM passes, not correctness. Worse, `check-adjudication-independence.js` shows
 * A and B share an origin, so the label set is one opinion recorded twice. Role
 * `adjudicator-C` re-runs the original adjudication question under enforced isolation to
 * establish what the inter-rater number actually is.
 *
 * USAGE
 *
 *   node mc-match-3.js --split                          show the dev/holdout split
 *   node mc-match-3.js --emit <role> <draw> [--half H]  write subagent packs
 *   node mc-match-3.js --ingest                         load returned verdicts into the cache
 *   node mc-match-3.js --status                         what is cached, what is missing
 *   node mc-match-3.js --validate [--half H] [--labels L]
 *
 *   role   judge | adjudicator-C
 *   half   dev | holdout | all        (default all; --validate reports dev and holdout apart)
 *   labels A | C | consensus          (default A, the historical target)
 *
 * Exit 0 on success, 2 on usage failure. A judge that fails its bar still exits 0: a recorded
 * negative result is a successful measurement.
 */
'use strict';
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const V2 = __dirname;
const REFIT = path.join(V2, 'eval-runs', 'real-baseline', 'threshold-refit');
const HOME = path.join(V2, 'eval-runs', 'real-baseline', 'mc-match-3');
const PACKS = path.join(HOME, 'packs');
const VERDICTS = path.join(HOME, 'verdicts');
const CACHE = path.join(HOME, 'cache');

const BATCH_SIZE = 45;
const DRAWS = 3;

/* ========================================================================== *
 * THE JUDGE PROMPT. Frozen. Changing a character changes JUDGE_SHA, which
 * invalidates every cache entry, which is the point: cached verdicts belong to
 * the prompt that produced them.
 *
 * The two named traps are priors taken from 21-scorer-refit-sprint.md section
 * 5.5, where both adjudicators independently reported the same two failure
 * shapes. They are aggregate observations from a published document, not
 * per-pair knowledge of the answer key. Recorded here so the write-up can say
 * exactly what the judge was told before it was measured.
 * ========================================================================== */
const JUDGE_PROMPT = `You are judging pairs of texts about student consulting deliverables.

Each pair has two halves:

  GOLD ISSUE   a problem a human reviewer recorded about the deliverable
  AI FINDING   one finding an AI reviewer produced about the same deliverable

One question per pair: DOES THE AI FINDING CATCH THE GOLD ISSUE?

The test is counterfactual. Imagine a project lead who reads only the AI finding and never
sees the gold issue. Would the problem the gold issue names actually get dealt with?

  yes       the lead would deal with the problem the gold issue names
  partial   the lead would be looking in the right area, but would still have to identify the
            gold issue's problem for themselves
  no        these are different problems

Two traps. Both were measured in this exact data and both are common here.

TRAP 1, SAME PROBLEM IN DIFFERENT WORDS. The gold issue says there is no executive summary;
the AI finding says the deck never states a decision anywhere. Different vocabulary, one
problem. That is "yes". Judge the problem, never the wording. Two texts can share almost no
words and be about the same thing.

TRAP 2, SAME PLACE IN THE DECK, DIFFERENT PROBLEM. The AI finding and the gold issue cite the
same slides, or share consulting vocabulary such as evidence, recommendation, storyline, and
diagnose unrelated things. Shared location is not evidence. Shared jargon is not evidence.
That is "no".

Four more rules, in priority order when they conflict:

1. DIRECTION. A finding arguing for the opposite change from the gold issue does not catch it,
   however much vocabulary they share. "Add more interpretation" does not catch "cut the
   volume down".
2. SPECIFICITY. A broad finding does not catch a specific gold issue just by containing it as
   a possible instance. Ask whether the lead would arrive at the gold issue's actual problem,
   not whether the gold issue is technically consistent with the finding.
3. SYMPTOM VERSUS CAUSE. A finding that names one symptom of the gold issue's problem, without
   naming the problem, is "partial".
4. SEVERITY IS IRRELEVANT. The two halves may grade the same problem differently. That does
   not affect whether it was caught.

You are NOT told any matcher score and must not try to infer or reconstruct one. Do not reason
about word overlap. Reason about whether it is the same problem.

For each pair also give catchConfidence, an integer 0 to 100: how confident you are that a
lead reading only the AI finding would deal with the gold issue's problem. 0 means certainly
not, 100 means certainly yes. Use the full range. It must be consistent with your verdict
(low for "no", middling for "partial", high for "yes") but it carries your confidence within
that band, so two "no" verdicts you feel differently about should get different numbers.

Answer every pair in the pack. Do not skip any. Output exactly this JSON and nothing else:

{ "verdicts": [ { "id": "...", "verdict": "yes|partial|no", "catchConfidence": 0, "why": "one sentence" } ] }`;

/* Role adjudicator-C reproduces the ORIGINAL adjudication question verbatim, exactly as it
 * was posed to A and B in adjudication-set.json. It is deliberately not improved: its job is
 * to answer the same question a second time, genuinely independently, so that the inter-rater
 * number the project believed it had can actually be measured. */
const ADJUDICATOR_C_PREAMBLE = `You are adjudicating pairs of texts about student consulting deliverables.

Each pair has a GOLD ISSUE, a problem a human reviewer recorded about the deliverable, and an
AI FINDING, one finding an AI reviewer produced about the same deliverable.

`;
const ADJUDICATOR_C_TAIL = `

For each pair also give catchConfidence, an integer 0 to 100: how confident you are that a lead
reading only the AI finding would consider the gold issue raised.

Answer every pair in the pack. Do not skip any. Output exactly this JSON and nothing else:

{ "verdicts": [ { "id": "...", "verdict": "yes|partial|no", "catchConfidence": 0, "why": "one sentence" } ] }`;

const ROLES = { judge: null, 'adjudicator-C': null };

function sha(s) { return crypto.createHash('sha256').update(s).digest('hex'); }

function loadSet() {
  const p = path.join(REFIT, 'adjudication-set.json');
  if (!fs.existsSync(p)) { console.error('missing adjudication-set.json'); process.exit(2); }
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

function rolePrompt(role) {
  if (role === 'judge') return JUDGE_PROMPT;
  if (role === 'adjudicator-C') return ADJUDICATOR_C_PREAMBLE + loadSet().question + ADJUDICATOR_C_TAIL;
  console.error('unknown role "' + role + '". Roles: ' + Object.keys(ROLES).join(', '));
  process.exit(2);
}

/* Canonical pair text. The cache key must change when the pair text changes and must not
 * change when the file is reformatted, so it is built from the fields the model is shown, in
 * a fixed order, rather than from the JSON bytes. */
function pairCanonical(p) {
  const g = p.goldIssue, f = p.reviewFinding;
  return [
    'GOLD', g.anchor, g.detail, g.severity, g.dimension, g.type, g.location,
    'FINDING', f.short, f.title, f.diagnosis, f.why, f.fix, f.severity, f.issueType,
    (f.evidence || []).map(e => e.slide + ':' + e.quote).join('|'),
  ].map(x => String(x == null ? '' : x)).join('␟');
}

/* Build the pair shape the judge is shown, from a parsed gold issue and a review finding.
 *
 * This MUST reproduce build-refit-set.js byte for byte. The 178 cached verdicts were taken
 * against text clipped exactly this way, and the cache is keyed on that text: one character of
 * drift and every lookup misses silently, which would degrade the matcher to "unscored" across
 * the board rather than fail loudly. `assertPairShapeMatches()` below is the standing check.
 *
 * Note what the judge does NOT see: the finding's `fix` field, which findingText() in
 * score-review.js does include. The judge is scoring slightly less text than the old overlap
 * matcher did. That was build-refit-set.js's choice in the previous sprint, it applied equally
 * to adjudicators A and C, and changing it now would invalidate every cached verdict. */
function clip(s, n) {
  s = String(s == null ? '' : s).replace(/\s+/g, ' ').trim();
  return s.length > n ? s.slice(0, n) + '...' : s;
}

function toPair(goldIssue, finding, id) {
  return {
    id: id || null,
    goldIssue: {
      anchor: goldIssue.anchor,
      detail: clip(goldIssue.text, 700),
      severity: goldIssue.severity,
      dimension: goldIssue.dimension,
      type: goldIssue.type,
      mustCatch: !!goldIssue.mustCatch,
      location: (goldIssue.at && goldIssue.at.raw) || 'not stated',
    },
    reviewFinding: {
      short: finding.short,
      title: finding.title,
      diagnosis: clip(finding.diagnosis, 700),
      why: clip(finding.why, 400),
      severity: finding.severity,
      issueType: finding.issueType,
      evidence: (finding.evidence || []).slice(0, 2).map(e => ({ slide: e.slide, quote: clip(e.quote, 260) })),
    },
  };
}

function cacheKey(role, draw, p) {
  return sha([sha(rolePrompt(role)).slice(0, 16), role, String(draw), sha(pairCanonical(p))].join('|')).slice(0, 32);
}

/* ---- the split ----------------------------------------------------------- *
 * 178 pairs is small. Iterating a prompt against all 178 and then reporting accuracy on all
 * 178 is the fiction-fitted-thresholds mistake in a new coat. So: develop on dev, touch
 * holdout once.
 *
 * Stratified on three things at once, so both halves carry the hard pairs:
 *   case          all four cases appear in both halves in proportion
 *   label         yes / partial / no split evenly, and yes is only 25 pairs
 *   score band    the 0.24-0.39 ambiguous band, where mc-match-2 coin-flips, splits evenly
 *
 * NOT stratified on adjudicator agreement, which the method note asked for: there are only 2
 * disagreements in the whole set, and check-adjudication-independence.js shows the two
 * adjudications share an origin, so that axis carries no information to stratify on.
 *
 * Assignment is a pure function of the pair id, so the split is reproducible from this file
 * alone with nothing stored.
 * -------------------------------------------------------------------------- */
function bandOf(textScore) {
  if (textScore == null) return 'unknown';
  if (textScore < 0.24) return 'low';
  if (textScore < 0.39) return 'ambiguous';
  return 'high';
}

function buildSplit() {
  const pairs = loadSet().pairs;
  const labels = loadLabels('A');
  const key = new Map(JSON.parse(fs.readFileSync(path.join(REFIT, 'answer-key.json'), 'utf8')).key.map(k => [k.id, k]));

  const strata = new Map();
  for (const p of pairs) {
    const caseId = p.id.match(/^(real-\d+)/)[1];
    const k = key.get(p.id);
    const s = [caseId, labels.get(p.id) || '?', bandOf(k && k.textScore)].join('/');
    if (!strata.has(s)) strata.set(s, []);
    strata.get(s).push(p.id);
  }

  const split = new Map();
  for (const [name, ids] of [...strata.entries()].sort((a, b) => a[0].localeCompare(b[0]))) {
    /* Order inside a stratum by a hash of the id: stable, and unrelated to anything the
     * judge sees, so it cannot correlate with difficulty. */
    ids.sort((x, y) => sha(x + '|mc-match-3-split').localeCompare(sha(y + '|mc-match-3-split')));
    /* Odd strata leave a remainder. Always giving it to dev starves the held-out half of the
     * 25-pair positive class, so the parity flips per stratum on a hash of the stratum name. */
    const flip = parseInt(sha(name + '|parity').slice(0, 8), 16) % 2;
    ids.forEach((id, i) => split.set(id, (i + flip) % 2 === 0 ? 'dev' : 'holdout'));
  }
  return { split, strata };
}

function halfFilter(half) {
  const { split } = buildSplit();
  if (half === 'all' || !half) return () => true;
  if (half !== 'dev' && half !== 'holdout') { console.error('--half must be dev, holdout or all'); process.exit(2); }
  return id => split.get(id) === half;
}

/* ---- labels -------------------------------------------------------------- *
 * A and B are the 2026-08-05 files. C is this sprint's re-adjudication and lives in the cache
 * with everything else, deliberately NOT written into threshold-refit/adjudication-C.json:
 * refit-thresholds.js reserves that filename for a two-pair tie-break, and a full 178-pair
 * label set sitting under a name that means something else is how the next person gets misled.
 * -------------------------------------------------------------------------- */
function loadLabels(which) {
  if (which === 'C') {
    const rows = readCache().filter(r => r.role === 'adjudicator-C' && r.promptSha256 === sha(rolePrompt('adjudicator-C')).slice(0, 16));
    return new Map(rows.map(r => [r.id, r.verdict]));
  }
  const file = { A: 'adjudication-A.json', B: 'adjudication-B.json' }[which];
  if (!file) { console.error('labels must be A, B, C or consensus'); process.exit(2); }
  const p = path.join(REFIT, file);
  if (!fs.existsSync(p)) return new Map();
  return new Map(JSON.parse(fs.readFileSync(p, 'utf8')).adjudications.map(x => [x.id, x.verdict]));
}

const ORDER = ['no', 'partial', 'yes'];

/* Consensus across whichever independent label sources exist, resolved DOWN on a split.
 * A pair one source called yes and another called no is not evidence anything was caught. */
function consensusLabels(sources) {
  const maps = sources.map(loadLabels).filter(m => m.size);
  if (!maps.length) return new Map();
  const out = new Map();
  for (const id of maps[0].keys()) {
    const vs = maps.map(m => m.get(id)).filter(Boolean);
    out.set(id, ORDER[Math.min(...vs.map(v => ORDER.indexOf(v)))]);
  }
  return out;
}

function labelsFor(which) {
  if (which === 'consensus') return consensusLabels(['A', 'C']);
  return loadLabels(which);
}

/* ---- pack emission ------------------------------------------------------- */
function emit(role, draw, half) {
  rolePrompt(role);   // validates the role before writing anything
  const keep = halfFilter(half);
  const pairs = loadSet().pairs.filter(p => keep(p.id));
  fs.mkdirSync(PACKS, { recursive: true });
  fs.mkdirSync(VERDICTS, { recursive: true });

  const batches = [];
  for (let i = 0; i < pairs.length; i += BATCH_SIZE) batches.push(pairs.slice(i, i + BATCH_SIZE));

  const written = [];
  batches.forEach((batch, i) => {
    const name = role + '-draw' + draw + '-' + (half || 'all') + '-batch-' + String(i + 1).padStart(2, '0');
    const file = path.join(PACKS, name + '.json');
    fs.writeFileSync(file, JSON.stringify({
      pack: name,
      role,
      draw,
      promptSha256: sha(rolePrompt(role)).slice(0, 16),
      instructions: rolePrompt(role),
      isolation: 'Answer only from this file. Do not read any other file in this repository, ' +
        'and in particular do not look for any file containing verdicts, adjudications, scores ' +
        'or an answer key. Anything you find that looks like an answer to these pairs is either ' +
        'a different question or a contamination of this measurement.',
      writeTo: path.join('eval-runs', 'real-baseline', 'mc-match-3', 'verdicts', name + '.json'),
      pairCount: batch.length,
      pairs: batch,
    }, null, 1));
    written.push({ name, file, n: batch.length });
  });

  console.log('role ' + role + ', draw ' + draw + ', half ' + (half || 'all') + ', prompt ' + sha(rolePrompt(role)).slice(0, 16));
  console.log(pairs.length + ' pairs in ' + written.length + ' packs of up to ' + BATCH_SIZE);
  for (const w of written) console.log('  ' + w.name + '   ' + w.n + ' pairs');
  console.log('\nEach pack goes to one fresh subagent. It writes ' + path.relative(V2, VERDICTS) + '/<pack>.json');
  console.log('Then: node mc-match-3.js --ingest');
  return 0;
}

/* ---- ingest -------------------------------------------------------------- */
function ingest() {
  if (!fs.existsSync(VERDICTS)) { console.error('no verdicts directory yet'); process.exit(2); }
  fs.mkdirSync(CACHE, { recursive: true });
  const byId = new Map(loadSet().pairs.map(p => [p.id, p]));
  const files = fs.readdirSync(VERDICTS).filter(f => f.endsWith('.json')).sort();
  if (!files.length) { console.error('no verdict files in ' + VERDICTS); process.exit(2); }

  let added = 0, already = 0, unknown = 0, malformed = 0;
  for (const f of files) {
    const m = f.match(/^(judge|adjudicator-C)-draw(\d+)-/);
    if (!m) { console.log('  skip ' + f + '  (filename does not name a role and draw)'); continue; }
    const [, role, drawStr] = m;
    const draw = Number(drawStr);
    let doc;
    try { doc = JSON.parse(fs.readFileSync(path.join(VERDICTS, f), 'utf8')); }
    catch (e) { console.log('  BAD  ' + f + '  ' + e.message); malformed++; continue; }
    const rows = doc.verdicts || doc.adjudications || [];
    let n = 0;
    for (const r of rows) {
      const p = byId.get(r.id);
      if (!p) { unknown++; continue; }
      if (!ORDER.includes(r.verdict)) { malformed++; continue; }
      const k = cacheKey(role, draw, p);
      const out = path.join(CACHE, k + '.json');
      if (fs.existsSync(out)) { already++; continue; }
      fs.writeFileSync(out, JSON.stringify({
        id: r.id, role, draw,
        promptSha256: sha(rolePrompt(role)).slice(0, 16),
        pairSha256: sha(pairCanonical(p)).slice(0, 16),
        verdict: r.verdict,
        catchConfidence: typeof r.catchConfidence === 'number' ? r.catchConfidence : null,
        why: r.why || '',
        source: f,
        ingestedAt: new Date().toISOString(),
      }, null, 1));
      added++; n++;
    }
    console.log('  ' + f.padEnd(48) + n + ' new');
  }
  console.log('\n' + added + ' cached, ' + already + ' already present, ' + unknown + ' unknown ids, ' + malformed + ' malformed');
  return 0;
}

function readCache() {
  if (!fs.existsSync(CACHE)) return [];
  return fs.readdirSync(CACHE).filter(f => f.endsWith('.json'))
    .map(f => JSON.parse(fs.readFileSync(path.join(CACHE, f), 'utf8')));
}

function status() {
  const pairs = loadSet().pairs;
  const { split } = buildSplit();
  const rows = readCache();
  const seen = new Map();
  for (const r of rows) seen.set(r.role + '|' + r.draw + '|' + r.id, r);

  console.log('cache ' + path.relative(V2, CACHE) + '   ' + rows.length + ' verdicts');
  console.log('');
  for (const role of Object.keys(ROLES)) {
    const sha16 = sha(rolePrompt(role)).slice(0, 16);
    const draws = [...new Set(rows.filter(r => r.role === role).map(r => r.draw))].sort();
    const stale = rows.filter(r => r.role === role && r.promptSha256 !== sha16).length;
    console.log(role + '   prompt ' + sha16 + (stale ? '   (' + stale + ' cached under an older prompt, ignored)' : ''));
    if (!draws.length) { console.log('   nothing cached'); continue; }
    for (const d of draws) {
      const have = pairs.filter(p => seen.has(role + '|' + d + '|' + p.id));
      const dev = have.filter(p => split.get(p.id) === 'dev').length;
      console.log('   draw ' + d + '   ' + have.length + '/' + pairs.length + ' pairs   (dev ' + dev + ', holdout ' + (have.length - dev) + ')');
    }
  }
  return 0;
}

/* ---- the judge, as a matcher --------------------------------------------- *
 * Reads the cache only. No network, no key, no model call. A pair with fewer than one cached
 * draw returns null rather than a guess: an instrument that invents a number when it has no
 * measurement is the failure this whole sprint exists to correct.
 * -------------------------------------------------------------------------- */
function judgePair(pair, opts) {
  const role = (opts && opts.role) || 'judge';
  const sha16 = sha(rolePrompt(role)).slice(0, 16);
  const draws = [];
  for (let d = 1; d <= DRAWS; d++) {
    const f = path.join(CACHE, cacheKey(role, d, pair) + '.json');
    if (!fs.existsSync(f)) continue;
    const r = JSON.parse(fs.readFileSync(f, 'utf8'));
    if (r.promptSha256 !== sha16) continue;
    draws.push(r);
  }
  if (!draws.length) return null;

  const counts = { no: 0, partial: 0, yes: 0 };
  for (const d of draws) counts[d.verdict]++;
  const top = Math.max(...ORDER.map(v => counts[v]));
  /* Ties resolve DOWN. Two draws split between yes and no is not evidence of a catch. */
  const verdict = ORDER.find(v => counts[v] === top);
  const conf = draws.map(d => (d.catchConfidence == null ? { no: 10, partial: 50, yes: 90 }[d.verdict] : d.catchConfidence));

  return {
    verdict,
    unanimous: top === draws.length,
    draws: draws.length,
    counts,
    score: conf.reduce((s, x) => s + x, 0) / conf.length,
    spread: Math.max(...conf) - Math.min(...conf),
    why: draws[0].why,
  };
}

/* ---- self-check ---------------------------------------------------------- *
 * Rebuild every pair in the adjudication set from its source gold and review through toPair(),
 * and check the canonical text is identical. If this fails, score-review.js will look up cache
 * keys that do not exist and quietly report everything as unscored. Loud is the only acceptable
 * failure mode for a cache miss, so this is a command rather than a comment.
 * -------------------------------------------------------------------------- */
function selfcheck() {
  const S = require('./score-review.js');
  const STAB = path.join(V2, 'eval-runs', 'real-baseline', 'stability');
  const GOLD_DIR = path.join(V2, 'eval-cases-real', 'labeling');
  const byId = new Map(loadSet().pairs.map(p => [p.id, p]));

  if (!fs.existsSync(STAB)) { console.error('no stability runs on disk, cannot self-check'); return 2; }
  let checked = 0, mismatched = 0, notFound = 0;
  const bad = [];

  for (const run of fs.readdirSync(STAB)) {
    const dir = path.join(STAB, run);
    if (!fs.statSync(dir).isDirectory()) continue;
    for (const f of fs.readdirSync(dir).filter(x => x.endsWith('.review.json'))) {
      const caseId = f.replace('.review.json', '');
      const goldFile = path.join(GOLD_DIR, caseId + '.gold.md');
      if (!fs.existsSync(goldFile)) continue;
      const review = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));
      const gold = S.parseGold(goldFile);
      for (const gi of gold.issues || []) {
        (review.findings || []).forEach((fd, idx) => {
          const id = caseId + '-' + run.replace('_collect-', '') + '-g' + gi.rank + '-f' + idx;
          const want = byId.get(id);
          if (!want) { notFound++; return; }
          checked++;
          if (pairCanonical(toPair(gi, fd, id)) !== pairCanonical(want)) { mismatched++; bad.push(id); }
        });
      }
    }
  }

  console.log('PAIR SHAPE SELF-CHECK');
  console.log('  rebuilt and compared    ' + checked + ' of ' + byId.size + ' pairs in the adjudication set');
  console.log('  not in the set          ' + notFound + '   (expected: 282 pairs exist, 178 were selected)');
  console.log('  MISMATCHED              ' + mismatched);
  if (mismatched) {
    console.log('\n  toPair() has drifted from build-refit-set.js. Every cached verdict is unreachable.');
    for (const id of bad.slice(0, 10)) console.log('    ' + id);
    return 1;
  }
  console.log('\n  toPair() reproduces the judged text exactly. Cache lookups from score-review.js will hit.');
  return 0;
}

/* ---- metrics ------------------------------------------------------------- */
function auc(pos, neg) {
  if (!pos.length || !neg.length) return NaN;
  let wins = 0;
  for (const p of pos) for (const n of neg) {
    if (p > n) wins++; else if (p === n) wins += 0.5;
  }
  return wins / (pos.length * neg.length);
}

function prf(pred, truth) {
  let tp = 0, fp = 0, fn = 0, tn = 0;
  for (let i = 0; i < pred.length; i++) {
    if (pred[i] && truth[i]) tp++;
    else if (pred[i] && !truth[i]) fp++;
    else if (!pred[i] && truth[i]) fn++;
    else tn++;
  }
  const p = tp + fp ? tp / (tp + fp) : 0;
  const r = tp + fn ? tp / (tp + fn) : 0;
  return { p, r, f1: p + r ? 2 * p * r / (p + r) : 0, tp, fp, fn, tn, acc: (tp + tn) / pred.length };
}

function pct(x) { return (x * 100).toFixed(1) + '%'; }

/* The headline task, defined to match 21-scorer-refit-sprint.md section 5.2 exactly so the
 * numbers are comparable: binary yes vs no, `partial` excluded, n=162 under the A labels.
 * The constant is "call everything not-caught", which needs no model at all. */
function headline(rows) {
  const bin = rows.filter(r => r.label === 'yes' || r.label === 'no');
  const truth = bin.map(r => r.label === 'yes');
  const pred = bin.map(r => r.pred === 'yes');
  const s = prf(pred, truth);
  const constant = truth.filter(t => !t).length / (bin.length || 1);
  return { n: bin.length, ...s, constant, lift: s.acc - constant };
}

function evaluate(rows, title) {
  const L = [];
  const scored = rows.filter(r => r.judged);
  L.push(title);
  L.push('-'.repeat(title.length));
  if (!scored.length) { L.push('  nothing judged in this slice'); return L.join('\n'); }
  if (scored.length !== rows.length) L.push('  WARNING: ' + (rows.length - scored.length) + ' of ' + rows.length + ' pairs have no cached verdict and are excluded');

  const h = headline(scored);
  const a1 = auc(scored.filter(r => r.label === 'yes').map(r => r.score), scored.filter(r => r.label !== 'yes').map(r => r.score));
  const a2 = auc(scored.filter(r => r.label !== 'no').map(r => r.score), scored.filter(r => r.label === 'no').map(r => r.score));

  L.push('  n judged                  ' + scored.length);
  L.push('  AUC yes vs (partial+no)   ' + (isNaN(a1) ? 'n/a' : a1.toFixed(3)) + '        bar 0.850   ' + (a1 >= 0.85 ? 'PASS' : 'FAIL'));
  L.push('  AUC (yes+partial) vs no   ' + (isNaN(a2) ? 'n/a' : a2.toFixed(3)));
  L.push('  accuracy, yes vs no       ' + pct(h.acc) + ' on n=' + h.n + '   against ' + pct(h.constant) +
    ' for a constant that ignores its input   bar 92.0%   ' + (h.acc >= 0.92 ? 'PASS' : 'FAIL'));
  L.push('  lift over the constant    ' + (h.lift * 100).toFixed(1) + ' points');
  L.push('  precision / recall / F1   ' + pct(h.p) + ' / ' + pct(h.r) + ' / ' + h.f1.toFixed(3) + '   (tp ' + h.tp + ' fp ' + h.fp + ' fn ' + h.fn + ' tn ' + h.tn + ')');

  const conf = {};
  for (const v of ORDER) for (const w of ORDER) conf[v + '|' + w] = 0;
  for (const r of scored) conf[r.label + '|' + r.pred]++;
  L.push('');
  L.push('  3-class confusion (rows label, cols judge):');
  L.push('            ' + ORDER.map(v => v.padStart(9)).join(''));
  for (const v of ORDER) L.push('  ' + v.padEnd(10) + ORDER.map(w => String(conf[v + '|' + w]).padStart(9)).join(''));
  const exact = scored.filter(r => r.label === r.pred).length;
  L.push('  3-class exact agreement   ' + pct(exact / scored.length));

  return L.join('\n');
}

function drawStability(rows) {
  const L = [];
  const withDraws = rows.filter(r => r.judged && r.judged.draws > 1);
  L.push('DRAW DISAGREEMENT  (determinism, reported whether it flatters or not)');
  L.push('-'.repeat(69));
  if (!withDraws.length) { L.push('  only one draw cached, so determinism is UNMEASURED'); return L.join('\n'); }
  const split = withDraws.filter(r => !r.judged.unanimous);
  L.push('  pairs with ' + DRAWS + ' draws       ' + withDraws.length);
  L.push('  draws not unanimous     ' + split.length + '   ' + pct(split.length / withDraws.length));
  const meanSpread = withDraws.reduce((s, r) => s + r.judged.spread, 0) / withDraws.length;
  L.push('  mean confidence spread  ' + meanSpread.toFixed(1) + ' points of 100');
  const byLabel = {};
  for (const r of withDraws) {
    byLabel[r.label] = byLabel[r.label] || { n: 0, split: 0 };
    byLabel[r.label].n++;
    if (!r.judged.unanimous) byLabel[r.label].split++;
  }
  for (const v of ORDER) if (byLabel[v]) L.push('    label ' + v.padEnd(8) + byLabel[v].split + '/' + byLabel[v].n + ' split   ' + pct(byLabel[v].split / byLabel[v].n));
  L.push('');
  L.push('  This is the confidence interval on every score built on this matcher.');
  return L.join('\n');
}

function contamination(role) {
  /* The A/B failure was a copy that perfect agreement made invisible. The draws of one role
   * are separately generated, so identical free-text across draws would mean the same leak.
   * Checked here so it cannot go unnoticed a second time. */
  const rows = readCache().filter(r => r.role === role && r.why);
  const byPair = new Map();
  for (const r of rows) {
    if (!byPair.has(r.id)) byPair.set(r.id, []);
    byPair.get(r.id).push(r.why.replace(/\s+/g, ' ').trim().toLowerCase());
  }
  let multi = 0, identical = 0;
  for (const [, whys] of byPair) {
    if (whys.length < 2) continue;
    multi++;
    if (new Set(whys).size === 1) identical++;
  }
  return { multi, identical, rate: multi ? identical / multi : 0 };
}

function validate(half, which) {
  const pairs = loadSet().pairs;
  const { split } = buildSplit();
  const labels = labelsFor(which);
  if (!labels.size) { console.error('label set "' + which + '" is not present'); process.exit(2); }
  const keep = halfFilter(half);

  const rows = pairs.filter(p => keep(p.id)).map(p => {
    const j = judgePair(p, { role: 'judge' });
    return {
      id: p.id, half: split.get(p.id), label: labels.get(p.id),
      judged: j, pred: j ? j.verdict : null, score: j ? j.score : null,
    };
  }).filter(r => r.label);

  console.log('MC-MATCH-3 VALIDATION');
  console.log('  judge prompt      ' + sha(JUDGE_PROMPT).slice(0, 16));
  console.log('  labels            ' + which + (which === 'consensus' ? '  (A and C, resolved down on a split)' : ''));
  console.log('  draws per pair    ' + DRAWS + ', majority vote, ties resolved down');
  console.log('  bar               AUC >= 0.850 and accuracy >= 92.0%, both against the constant baseline');
  console.log('');

  if (half && half !== 'all') {
    console.log(evaluate(rows, half.toUpperCase() + ' HALF'));
  } else {
    console.log(evaluate(rows.filter(r => r.half === 'dev'), 'DEV HALF  (the judge prompt was iterated against this)'));
    console.log('');
    console.log(evaluate(rows.filter(r => r.half === 'holdout'), 'HELD-OUT HALF  (touched once, this is the number that counts)'));
    console.log('');
    console.log(evaluate(rows, 'ALL 178  (reported for comparability with 21 section 5.2, not as the result)'));
  }

  console.log('');
  console.log(drawStability(rows));

  /* Behaviour on the pairs where the call is genuinely hard. */
  const dis = path.join(REFIT, 'disagreements.json');
  if (fs.existsSync(dis)) {
    const d = JSON.parse(fs.readFileSync(dis, 'utf8')).disagreements || [];
    console.log('');
    console.log('THE PAIRS WHERE THE ADJUDICATORS SPLIT');
    console.log('-'.repeat(69));
    console.log('  n = ' + d.length + '. Two pairs carry no statistical information; this is reported because');
    console.log('  the method note asked for it, and the honest reading is that it cannot settle anything.');
    for (const x of d) {
      const r = rows.find(y => y.id === x.id);
      console.log('    ' + x.id + '   A=' + x.A + ' B=' + x.B + '   judge=' +
        (r && r.judged ? r.pred + ' (' + JSON.stringify(r.judged.counts) + ', conf ' + r.judged.score.toFixed(0) + ')' : 'not judged'));
    }
  }

  const c = contamination('judge');
  console.log('');
  console.log('CONTAMINATION CHECK ACROSS DRAWS');
  console.log('-'.repeat(69));
  console.log('  pairs with 2+ draws     ' + c.multi);
  console.log('  byte-identical prose    ' + c.identical + '   ' + pct(c.rate) +
    (c.rate > 0.25 ? '   <-- draws are not independent, treat the vote as one draw' : '   (independent)'));

  /* Inter-rater, if a genuinely independent second adjudication exists. */
  const C = loadLabels('C');
  if (C.size) {
    const A = loadLabels('A');
    const ids = [...A.keys()].filter(id => C.has(id));
    const agree = ids.filter(id => A.get(id) === C.get(id)).length;
    const cnt = (m) => ORDER.reduce((o, v) => (o[v] = ids.filter(id => m.get(id) === v).length, o), {});
    const ca = cnt(A), cc = cnt(C);
    const pe = ORDER.reduce((s, v) => s + (ca[v] / ids.length) * (cc[v] / ids.length), 0);
    const raw = agree / ids.length;
    console.log('');
    console.log('INTER-RATER, A AGAINST AN INDEPENDENT C');
    console.log('-'.repeat(69));
    console.log('  pairs in both           ' + ids.length);
    console.log('  raw agreement           ' + pct(raw));
    console.log('  Cohen\'s kappa           ' + ((raw - pe) / (1 - pe)).toFixed(3));
    console.log('  A marginals             ' + JSON.stringify(ca));
    console.log('  C marginals             ' + JSON.stringify(cc));
    console.log('  (the 0.971 in 21 section 5.1 was A against a copy of A, and measures nothing)');

    /* The same test that caught A/B, applied to A against C. If this ever trips, C is worthless
     * for the same reason B was, and the number above must not be quoted. */
    const aWhy = new Map(JSON.parse(fs.readFileSync(path.join(REFIT, 'adjudication-A.json'), 'utf8'))
      .adjudications.map(x => [x.id, String(x.why || '').replace(/\s+/g, ' ').trim().toLowerCase()]));
    const cWhy = new Map(readCache().filter(r => r.role === 'adjudicator-C')
      .map(r => [r.id, String(r.why || '').replace(/\s+/g, ' ').trim().toLowerCase()]));
    const both = [...aWhy.keys()].filter(id => cWhy.has(id));
    const dup = both.filter(id => aWhy.get(id) === cWhy.get(id) && aWhy.get(id) !== '').length;
    console.log('  byte-identical prose    ' + dup + '/' + both.length + '   ' + pct(both.length ? dup / both.length : 0) +
      (dup / (both.length || 1) > 0.25 ? '   <-- C IS CONTAMINATED, discard the kappa above' : '   (C is genuinely independent)'));

    const confAC = {};
    for (const v of ORDER) for (const w of ORDER) confAC[v + '|' + w] = 0;
    for (const id of ids) confAC[A.get(id) + '|' + C.get(id)]++;
    console.log('');
    console.log('  confusion (rows A, cols C):');
    console.log('            ' + ORDER.map(v => v.padStart(9)).join(''));
    for (const v of ORDER) console.log('  ' + v.padEnd(10) + ORDER.map(w => String(confAC[v + '|' + w]).padStart(9)).join(''));

    /* The yes/no line is the one the matcher is actually fitted to. Agreement there can be far
     * better than the 3-class number if the raters differ mainly on where `partial` starts. */
    const hard = ids.filter(id => A.get(id) !== 'partial' && C.get(id) !== 'partial');
    const hardAgree = hard.filter(id => A.get(id) === C.get(id)).length;
    console.log('');
    console.log('  ignoring partial        ' + hardAgree + '/' + hard.length + ' agree   ' + pct(hard.length ? hardAgree / hard.length : 0));
  }

  console.log('');
  console.log('LIMITATION');
  console.log('-'.repeat(69));
  console.log('  These labels are LLM adjudications, not ground truth, so what is measured above is');
  console.log('  agreement between two LLM passes over the same question and not correctness.');
  return 0;
}

/* ---- CLI ----------------------------------------------------------------- */
function main(argv) {
  const flag = n => { const i = argv.indexOf(n); return i === -1 ? null : argv[i + 1]; };
  const half = flag('--half');

  if (argv.includes('--split')) {
    const { split, strata } = buildSplit();
    const dev = [...split.values()].filter(v => v === 'dev').length;
    const labels = loadLabels('A');
    console.log('STRATIFIED SPLIT  (pure function of the pair id, nothing stored)');
    console.log('  dev ' + dev + ', holdout ' + (split.size - dev) + ', total ' + split.size);
    console.log('  strata: ' + strata.size + '  (case x label x mc-match-2 score band)');
    console.log('');
    const rollup = {};
    for (const [id, h] of split) {
      const k = id.match(/^(real-\d+)/)[1] + ' / ' + labels.get(id);
      rollup[k] = rollup[k] || { dev: 0, holdout: 0 };
      rollup[k][h]++;
    }
    console.log('  ' + 'case / label'.padEnd(24) + 'dev'.padStart(6) + 'holdout'.padStart(9));
    for (const k of Object.keys(rollup).sort()) console.log('  ' + k.padEnd(24) + String(rollup[k].dev).padStart(6) + String(rollup[k].holdout).padStart(9));
    return 0;
  }

  if (argv.includes('--emit')) {
    const i = argv.indexOf('--emit');
    const role = argv[i + 1];
    const draw = Number(argv[i + 2]);
    if (!role || !Number.isInteger(draw) || draw < 1) {
      console.error('usage: node mc-match-3.js --emit <role> <draw> [--half dev|holdout|all]');
      return 2;
    }
    return emit(role, draw, half);
  }

  if (argv.includes('--ingest')) return ingest();
  if (argv.includes('--status')) return status();
  if (argv.includes('--selfcheck')) return selfcheck();
  if (argv.includes('--validate')) return validate(half, flag('--labels') || 'A');

  console.error('usage: node mc-match-3.js --split | --emit <role> <draw> | --ingest | --status | --selfcheck | --validate');
  console.error('       optional: --half dev|holdout|all   --labels A|C|consensus');
  return 2;
}

module.exports = {
  judgePair, toPair, buildSplit, pairCanonical, DRAWS,
  JUDGE_PROMPT, JUDGE_SHA: sha(JUDGE_PROMPT).slice(0, 16),
};
if (require.main === module) process.exit(main(process.argv.slice(2)));
