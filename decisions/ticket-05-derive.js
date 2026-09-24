#!/usr/bin/env node
/* Ticket 05: can the readiness level be derived from the blocking issues a review
 * already reports, instead of being emitted by the model?
 *
 * PASTE-1-system-prompt.txt:167 — "Readiness is the lowest ceiling among the blocking
 * issues that fired." If the model follows its own rule, the level is redundant output.
 *
 * Run from tools/quality-reviewer/v2/eval-runs/real-baseline/.
 */
const fs = require('fs');
const path = require('path');

// blocking rule -> ceiling, as an index into LEVELS. PASTE-1-system-prompt.txt:151-166.
const CEILING = { 1: 0, 2: 1, 3: 1, 4: 2, 5: 1 };
const LEVELS = {
  'Not ready for client review': 0,
  'Needs substantial revision': 1,
  'Needs targeted revision': 2,
  'Nearly ready with minor edits': 3,
};
// :169 — "If no blocking rule fired, readiness is Nearly ready with minor edits by default",
// with a discretionary demote to Needs targeted revision the harness cannot reproduce.
const NO_BLOCKER_DEFAULT = 3;

function derive(review) {
  const rules = (review.blockingIssues || []).map(b => b.rule).filter(n => typeof n === 'number');
  if (!rules.length) return { idx: NO_BLOCKER_DEFAULT, discretionary: true };
  return { idx: Math.min(...rules.map(n => CEILING[n])), discretionary: false };
}

const runs = process.argv.slice(2);
if (!runs.length) { console.error('usage: ticket-05-derive.js <run-dir>...'); process.exit(1); }

let gOk = 0, gTot = 0;
for (const dir of runs) {
  if (!fs.existsSync(dir)) { console.log(dir + '  (missing)'); continue; }
  let ok = 0, tot = 0, noBlocker = 0;
  const misses = [];
  for (const f of fs.readdirSync(dir).filter(x => /\.review\.json$/.test(x)).sort()) {
    let r;
    try { r = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8')); } catch (e) { continue; }
    const emitted = LEVELS[r.readiness && r.readiness.level];
    if (emitted === undefined) continue;
    const d = derive(r);
    tot++;
    if (d.discretionary) noBlocker++;
    if (d.idx === emitted) ok++;
    else misses.push(f.split('.')[0] + ': derived R' + d.idx + ', emitted R' + emitted +
      (d.discretionary ? ' (no blocking rule fired — discretionary branch)' : ''));
  }
  gOk += ok; gTot += tot;
  console.log(path.basename(dir).slice(0, 19).padEnd(21) + ok + '/' + tot +
    '   no-blocker cases: ' + noBlocker + (misses.length ? '\n    ' + misses.join('\n    ') : ''));
}
console.log('\ntotal ' + gOk + '/' + gTot);
