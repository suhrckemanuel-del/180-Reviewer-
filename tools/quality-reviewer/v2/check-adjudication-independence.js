#!/usr/bin/env node
/*
 * check-adjudication-independence.js — is a double-adjudication actually double?
 *
 * The 178-pair label set under eval-runs/real-baseline/threshold-refit/ is the target every
 * matcher in this project is fitted and validated against. Its authority rests on one claim,
 * made in 21-scorer-refit-sprint.md section 5.1 and repeated in 18-evidence-base.md A8:
 *
 *   two agents, fresh context each, blind to each other, agreed at kappa 0.971
 *
 * Cohen's kappa cannot detect a copy. Two files that are the same file agree perfectly, and
 * perfect agreement reads as the strongest possible evidence. So kappa was measured and
 * independence was assumed. This script measures independence.
 *
 * The test is the free-text reasoning, not the verdicts. Verdicts are drawn from three labels
 * and will coincide often by chance. The `why` field is a sentence of open prose. Two agents
 * writing independently produce different sentences even when they reach the same verdict, so
 * byte-identical prose across many pairs has one explanation: the files share an origin.
 *
 * Usage:
 *   node check-adjudication-independence.js [--json]
 *
 * Exit 0 if the adjudications look independent, 1 if they do not, 2 on usage failure.
 * Exit 1 is a finding, not a crash: it means the label set is one opinion, not two.
 */
'use strict';
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const DIR = path.join(__dirname, 'eval-runs', 'real-baseline', 'threshold-refit');

/* Independent prose agreeing to the byte is the signal. One or two coincidences are possible
 * on very short sentences; a quarter of the set is not. The bar is deliberately generous so
 * that tripping it is unarguable rather than a judgement call. */
const IDENTICAL_PROSE_LIMIT = 0.25;

function load(f) {
  const p = path.join(DIR, f);
  if (!fs.existsSync(p)) { console.error('missing ' + f); process.exit(2); }
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

function norm(s) { return String(s || '').replace(/\s+/g, ' ').trim().toLowerCase(); }

function analyse(A, B) {
  const a = A.adjudications, b = B.adjudications;
  const bm = new Map(b.map(x => [x.id, x]));
  const ids = a.map(x => x.id).filter(id => bm.has(id));

  let sameVerdict = 0, identicalProse = 0, bothPresent = 0;
  const divergences = [];
  for (const row of a) {
    const other = bm.get(row.id);
    if (!other) continue;
    bothPresent++;
    if (row.verdict === other.verdict) sameVerdict++;
    const same = norm(row.why) === norm(other.why) && norm(row.why) !== '';
    if (same) identicalProse++;
    else divergences.push({ id: row.id, A: { verdict: row.verdict, why: row.why }, B: { verdict: other.verdict, why: other.why } });
  }

  /* Order is the second tell. Independent agents given the same input file may well answer in
   * file order, so this is corroborating rather than decisive. */
  const orderIdentical = JSON.stringify(a.map(x => x.id)) === JSON.stringify(b.map(x => x.id));

  return {
    pairsInBoth: bothPresent,
    sameVerdict,
    sameVerdictRate: bothPresent ? sameVerdict / bothPresent : 0,
    identicalProse,
    identicalProseRate: bothPresent ? identicalProse / bothPresent : 0,
    orderIdentical,
    divergences,
    /* Content hash ignoring whitespace: catches a straight copy that was only reformatted. */
    proseDigestA: crypto.createHash('sha256').update(a.map(x => norm(x.why)).join('\n')).digest('hex').slice(0, 16),
    proseDigestB: crypto.createHash('sha256').update(b.map(x => norm(x.why)).join('\n')).digest('hex').slice(0, 16),
  };
}

function main(argv) {
  const asJson = argv.includes('--json');
  const A = load('adjudication-A.json');
  const B = load('adjudication-B.json');
  const r = analyse(A, B);
  r.independent = r.identicalProseRate < IDENTICAL_PROSE_LIMIT;

  if (asJson) { console.log(JSON.stringify(r, null, 2)); return r.independent ? 0 : 1; }

  console.log('ADJUDICATION INDEPENDENCE CHECK');
  console.log('  adjudicator A     ' + A.adjudicator + '   (' + A.adjudications.length + ' rows)');
  console.log('  adjudicator B     ' + B.adjudicator + '   (' + B.adjudications.length + ' rows)');
  console.log('  pairs in both     ' + r.pairsInBoth);
  console.log('');
  console.log('  same verdict            ' + r.sameVerdict + '/' + r.pairsInBoth + '   ' + (r.sameVerdictRate * 100).toFixed(1) + '%');
  console.log('  BYTE-IDENTICAL prose    ' + r.identicalProse + '/' + r.pairsInBoth + '   ' + (r.identicalProseRate * 100).toFixed(1) + '%   <-- the test');
  console.log('  pair order identical    ' + r.orderIdentical);
  console.log('  prose digest A / B      ' + r.proseDigestA + ' / ' + r.proseDigestB);
  console.log('');
  if (r.independent) {
    console.log('  VERDICT: consistent with independent adjudication.');
    console.log('  Identical prose is below the ' + (IDENTICAL_PROSE_LIMIT * 100) + '% limit, so agreement statistics can be read as agreement.');
    return 0;
  }
  console.log('  VERDICT: NOT INDEPENDENT.');
  console.log('  ' + r.identicalProse + ' of ' + r.pairsInBoth + ' free-text rationales are identical to the byte. Two agents writing');
  console.log('  separately do not produce the same sentence that many times. These files share an origin.');
  console.log('');
  console.log('  Consequence: kappa between them measures nothing. The label set is ONE opinion');
  console.log('  recorded twice, not two opinions that agreed. Anything fitted or validated against');
  console.log('  it inherits that, including T_HIT/T_NEAR and any matcher scored on these 178 pairs.');
  console.log('');
  console.log('  The ' + r.divergences.length + ' rows that do differ:');
  for (const d of r.divergences) console.log('    ' + d.id + '   A=' + d.A.verdict + '  B=' + d.B.verdict);
  return 1;
}

module.exports = { analyse };
if (require.main === module) process.exit(main(process.argv.slice(2)));
