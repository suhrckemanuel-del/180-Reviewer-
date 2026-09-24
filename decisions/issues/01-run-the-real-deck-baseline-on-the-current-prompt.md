# Run the real-deck baseline on the current frozen prompt

Type: task
Status: resolved
Blocked by: —

## Question

Nothing to decide. Every measurement decision below is blocked on numbers that do not exist, and
the machinery to produce them is already on disk.

State found in the audit of 2026-09-18:

- 9 of 11 golds have reviews, all produced under `frozen-2026-08-03` or earlier.
- The last scored run is 2026-08-05, matcher `mc-match-2`.
- The current prompt is `frozen-2026-08-09`, sha `2371607aa850b674`. The current matcher is
  `mc-match-3` (held-out AUC 0.979), which landed 2026-08-08 and **has never been run over the real
  set**.
- `eval-runs/real-baseline/2026-08-07T18-08-56-subagent-packs/` holds a complete, self-contained
  9-case input pack with a manifest. The packs were generated and the reviews were never collected.

`progress.md` said re-run all nine cases once the matcher landed. It landed three days later and
nobody went back. **The measured baseline is two prompt versions and one matcher generation stale.**

Do:

1. Regenerate the input packs on `frozen-2026-08-09` — do not run the 2026-08-07 packs, they encode
   an older prompt and would measure the wrong thing.
2. Run each case blind per the manifest protocol: one subagent per `*.input.md`, reading nothing
   else from the project — no gold, no worksheet, no other case's review, no harness source.
3. `node run-reviews.js --collect <pack-dir>`.
4. Rescore with `mc-match-3` and append to `scores-log.jsonl`.

Answer records: the scorecard, which cases moved, and anything the run exposed about the prompt.

Note the whole tree is gitignored and local-only — reviews quote client decks verbatim.

## Answer

Ran 2026-09-19. Packs regenerated on `frozen-2026-08-09`, sha verified `2371607aa850b674` read out
of section A at run time. Nine cases run blind, one subagent per `*.input.md`, three at a time.
Collected, scored, appended to `scores-log.jsonl` under key `frozen-2026-08-09|||mc-match-3`.
Pack: `eval-runs/real-baseline/2026-09-18T22-00-30-subagent-packs/` (gitignored, local only).

**9 of 9 reviews validated against the v2 contract, 0 invalid.** The self-contained pack works and
the free subagent path reproduces it.

### Scorecard

| metric | 08-03 / mc-match-2 | 08-09 / mc-match-3 | |
|---|---|---|---|
| readiness within one level | 77.8% | **55.6%** | −22.2 |
| readiness exact | 33.3% | **11.1%** | −22.2 |
| over-flag rate | 55.6% | **66.7%** | +11.1 |
| under-flag rate | 11.1% | **22.2%** | +11.1 |
| blocking false positives | 55.6% | **66.7%** | +11.1 |
| blocking rules missed | 0% | **0%** | — |
| restraint violations | 1 of 1 | **1 of 1** | — |
| mean findings per review | 4.9 | **5.0** | — |
| must-catch recall | 44.4% | **unmeasured** | not comparable |
| gold issue coverage | 37.8% | **unmeasured** | not comparable |
| severity exact | 75% (n=4) | **n/a** (n=0) | not comparable |

Holdout (real-05, real-08, real-13): within-one 66.7%, exact 0%.

The comparison is legitimate only for the rows above the line: readiness, over-flag, blocking and
restraint do not route through the matcher, so the matcher generation change does not touch them.

**On every metric that is actually measured, `frozen-2026-08-09` is worse than `frozen-2026-08-03`.**

### Which cases moved

Six of nine are unchanged. The whole 22-point regression sits in three cases, and all three moved
the wrong way:

| case | gold | 08-03 | 08-09 | |
|---|---|---|---|---|
| real-04 | R0 | R0 **exact** | R1 | exact match broken, now soft by one |
| real-13 | R2 | R2 **exact** | R0 | exact match broken, now over by two — and it is a holdout case |
| real-14 | R2 | R1 (over by one) | R0 | over by two |

`frozen-2026-08-09` broke two of the three exact readiness matches the previous prompt had. The
escalation is systematic, not scattered: four cases (real-02, real-03, real-13, real-14) all carry
gold R2 "Needs targeted revision" and all four are now predicted R0 "Not ready for client review",
the largest possible miss.

### The blocker this run exposed: mc-match-3 cannot score a new run

**`must-catch recall 0%` and `gold issue coverage 0%` are not results. Nothing was measured, and the
scorecard prints unmeasured as zero.** All 37 gold issues came back `unscored`.

The cause is structural, not a bug. mc-match-2 computed a verdict from text overlap for any pair it
was handed — badly (AUC 0.718), which is why it was replaced. mc-match-3 is not a function over
pairs; it is a **cache of LLM judge verdicts**, keyed on a hash of the pair text, holding 712
verdicts over exactly the 178-pair calibration set. `score-review.js` looks a pair up and correctly
returns `unscored` on a miss rather than inventing `miss`, which is the right call and is documented
as deliberate at `score-review.js:422`.

This run's 185 new pairs (37 gold issues × 5 findings) have never been judged, so every lookup
misses. The per-pair basis says `no cached verdict for this pair. Run: node mc-match-3.js --emit
judge <draw>` — **and that command cannot serve this run.** `emit()` sources from `loadSet()`, which
reads the fixed `threshold-refit/adjudication-set.json`. There is no path from `--emit` to a run
directory.

`node mc-match-3.js --selfcheck` passes clean: 178 of 178 pairs rebuild, 0 mismatched. The matcher is
intact. It is simply unapplied, and nothing in the harness can apply it.

So mc-match-3 was never a drop-in replacement for mc-match-2, and shipping it silently took the
harness from "scores every run badly" to "cannot score any new run at all". Judging this run means
an adjudication pass over 185 pairs — roughly the size of the entire mc-match-3 calibration sprint.
**That work is not in this map and needs a ticket.**

### What else the run exposed about the prompt

1. **Confidence is pinned Low on all 9 cases by construction, and carries no signal.** The prompt
   says if `EVIDENCE AND SOURCE NOTES` is blank, confidence is Low and you are done. That field is
   blank in all nine packs, so the Medium test never runs on any real case. Several subagents
   flagged it independently. This is the same class of defect as the 2026-08-05 discovery that the
   noise budget and scope matrix were missing from packs: an uncontrolled input sitting underneath
   every measurement.

2. **The noise budget is behaving as a target, not a ceiling.** Every one of the nine reviews
   produced exactly 5 findings — zero variance — and 7 or 8 total items against a cap of 8. A budget
   that saturates every time on decks ranging from 11 to 45 slides is being filled to quota rather
   than reporting what was found. Over-flagging at 66.7% is the same phenomenon seen from the
   severity side.

3. **The measurable half of this scorecard measures the feature ticket 05 retires.** With the matcher
   unapplied, every non-vacuous number here — readiness exact, readiness within one, over-flag,
   blocking false positives — is about the readiness level. A release gate built on today's
   scorecard would gate prompt changes on a retired component. Ticket 07 should not assume this
   instrument is available.

### Follow-up runs owed

**real-10 and real-11 were not run.** Both are still gated by `check-gold.js` on the contradictions
ticket 02 resolves, and the emitter skipped them. When ticket 02 lands, regenerate packs on the
then-current prompt and run those two to take the set from 9 to 11.
