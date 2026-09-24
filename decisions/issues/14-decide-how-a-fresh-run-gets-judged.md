# Decide how a fresh run's pairs get judged, now that mc-match-3 scores nothing outside its calibration set

Type: grilling
Status: resolved
Blocked by: —

## Question

Surfaced by ticket 01 on 2026-09-19. The baseline ran clean — 9 of 9 valid reviews — and came back
with `must-catch recall 0%` and `gold issue coverage 0%`, because **nothing was judged**, not because
anything was missed.

mc-match-2 computed a verdict from text overlap for any pair, badly (AUC 0.718). mc-match-3 replaced
it with a cache of LLM judge verdicts keyed on pair text: 712 verdicts over exactly the 178-pair
calibration set. `score-review.js` correctly returns `unscored` on a cache miss rather than inventing
`miss`. `--selfcheck` passes, 178 of 178, 0 mismatched — the matcher is intact and unapplied.

The consequence nobody costed when mc-match-3 shipped: **the harness can no longer score any run it
has not already judged.** This run needed 185 pair judgments (37 gold issues × 5 findings) and
`mc-match-3.js --emit` cannot produce them — `emit()` reads the fixed `adjudication-set.json` and has
no path to a run directory. Every future run has the same problem, and the per-pair error message
points at a command that cannot serve it.

So the project traded a matcher that scored everything badly for one that scores nothing at all, and
the accuracy win (held-out AUC 0.979) is real but currently unreachable outside its own test set.

The decision, not the build:

1. Does judging a run stay an LLM adjudication pass, or does mc-match-3 get a cheap deterministic
   pre-filter so only the ambiguous band costs judgments? 185 pairs per 9-case run is roughly the
   whole mc-match-3 calibration sprint, repeated every time the prompt changes.
2. If it stays a judging pass, how many draws, and does a single draw license a release decision when
   the calibration used three?
3. What does the scorecard print for an unjudged run? Printing `0%` for "not measured" is the
   flattering-direction failure this project keeps legislating against, and it did it here.
4. Is per-run judging affordable at all under the release cadence ticket 07 wants — and if not, does
   the gate drop the matcher-dependent metrics rather than pretend to have them?

Answer records: the judging path, its cost per run, and what the scorecard is allowed to report when
pairs are unjudged.

## Answer (2026-09-19)

**The judging pass is not built, and the release gate drops the matcher-dependent metrics rather
than pretend to have them.** That is question 4 of this ticket resolving in the negative, and it is
the owner's call: the eval loop comes off the critical path in favour of getting the tool into
usable shape. The cost work below is not wasted — it is the price tag for when the gate is wanted,
and several of the measurements invalidate claims the project was already carrying.

Measurement scratch: `.scratch/deliverable-reviewer/` (local only). One real 45-pair judge pack was
run end to end as a subagent and **not** ingested, so the cache is untouched at 712 verdicts.

### 1. The judging path, and what it costs

Measured, not estimated. One pack of 45 pairs (`judge-draw2-all-batch-01`, re-run fresh):
**100,202 tokens, 155 seconds, one subagent** — **2,227 tokens and 3.4 s per pair**, which is
**3.5x what the per-pair JSON size predicts**. The pair text is a small fraction of what a judging
subagent actually burns.

| judging depth | judgments | packs | tokens | wall clock @3 concurrent |
|---|---|---|---|---|
| 1 draw, 185 pairs | 185 | 5 | **~412K** | ~5 min |
| 3 draws, 185 pairs | 555 | 15 | **~1.24M** | ~13 min |
| the mc-match-3 calibration sprint, for scale | 712 | 16 | ~1.59M | ~15 min |

So the ticket's "roughly the whole calibration sprint, every time" is right at three draws, and
wrong by 3x at one. **Per gated prompt change: ~412K tokens and five minutes**, plus a one-off
~412K to judge the incumbent so there is anything to compare against. For scale, seven frozen
prompt versions shipped between 2026-07-26 and 2026-08-09, one every ~2 days.

### 2. A deterministic pre-filter cannot cut this materially — the option is dead

Sweeping mc-match-2's `textScore` against the 178 adjudicated labels (42 catches, 136 not):

- largest **zero-false-negative** low cut is `textScore < 0.132` -> excludes **17 of 178 = 9.6%**;
- adding a zero-error high cut at `>= 0.79` gets **22 of 178 = 12.4%** total;
- pushing to 25% exclusion throws away **4 of 42 real catches**.

12.4% is fitted **in-sample on the very set it is scored on**, so it is an optimistic ceiling. On
185 pairs it saves ~23 judgments — 412K to ~360K — and it changes pack composition, which section 4
shows is worth ~10% of verdicts on its own. **The choice was never "LLM pass vs pre-filter". It was
"pay, or drop the metrics."**

### 3. Draws 2 and 3 bought nothing, and "determinism" was measured against a copy of itself

From the existing cache, at zero cost:

| | draw1 | draw2 | draw3 | 3-draw majority |
|---|---|---|---|---|
| gold coverage (n=56) | 42.9% | 39.3% | 39.3% | **39.3%** |
| must-catch recall (n=12) | 75.0% | 66.7% | 75.0% | **66.7%** |

Draws 2 and 3 each reproduce the 3-draw majority on coverage **exactly**. Then the finding that
matters: **a fresh 4th draw taken today agrees with the 3-draw majority on only 86.7% (39/45) of
pairs — and 5 of the 6 disagreements are against a *unanimous* 3-draw verdict.**

The 97.2% draw2-vs-draw3 agreement measured the judge **against itself in one sitting, on one model
build, with one batching**. The honest cross-time figure six weeks later is 86.7%, and
within-sitting unanimity predicts nothing about it. **This is the map's standing caution for the
third time, by a third mechanism.** Compounding it: cache entries store `promptSha256` but **no
model identifier**, so it is not possible to tell whether two cached verdicts came from the same
judge at all.

**The saving grace, and the one thing that makes a future gate viable:** the instability is almost
entirely on the `partial`/`no` boundary. The `yes` axis — the only thing `must-catch recall` counts,
per `JUDGE_TO_VERDICT` (yes->hit, partial->near, no->miss) — was **96.6% stable within the sitting
and 45/45 across six weeks**. Recall is the robust metric; coverage-counting-nears is the fragile
one. If the gate ever returns, it should use recall and not coverage.

### 4. Priced and parked, for whenever the gate is built

Three questions were on the frontier when the ticket was reframed. They do not need answering now,
but they are real and should not be rediscovered:

- **Pack composition is the largest uncontrolled variable measured.** Draw1 differs from draws 2
  and 3 by 10.7% for no reason but being emitted `--half dev/holdout` instead of `--half all` —
  same prompt, same pairs, different neighbours in the pack. With a single draw there is no
  within-run averaging to absorb it. The fix is to batch **one pack per case** (9 packs of 5-30
  instead of 5 packs of 45, ~+10% cost), which makes composition a function of the case rather than
  of the run.
- **The judge is validated on 4 of the 9 cases.** The whole 178-pair set comes from real-01,
  real-03, real-04 and real-13 — 95 of the run's 185 pairs. **90 pairs (49%) sit on decks the judge
  has never been scored on**, and the held-out AUC 0.979 is held out *within* those four. Belongs
  on `18-evidence-base.md`'s not-known list.
- **The judge prompt is frozen by hash, not by policy.** `cacheKey()` includes the judge prompt
  sha, so one character discards every stored verdict. Under a gate that accumulates ~185 verdicts
  per release, a year of monthly releases is ~2,200 verdicts destroyed by one word. Freeze it in
  writing, name the price at the top of the file, and pin the judge model beside it — an unpinned
  model is an unversioned prompt by another route, which is exactly the 13.3% drift above.

### 5. What the scorecard may report when pairs are unjudged

The failure is worse than the ticket stated, and it is a **presentation-layer** failure over an
honest data layer. `score-review.js:466` ranks `unscored` above `miss` with a comment naming *"the
flattering direction"* by name, and the per-case table prints `unscored` for all nine cases
correctly. Then `scorecard.js:95` computes `pct(hits, withMustCatch.length)` — **`unscored` sits in
the denominator and can never reach the numerator, so it is arithmetically identical to `miss`.**

Three consequences, all live:

1. the headline prints *"(upper bound counting near misses 0%)"* — asserting even the **ceiling** is
   zero, i.e. certainty that nothing was caught;
2. *"READ THIS BEFORE QUOTING THE NUMBER"* says "recall is a floor" — true for `miss`, false for
   `unscored`;
3. `renderShareable()`, the aggregate-only export designed to leave the building, carries
   `must-catch recall 0%` **with no per-case table beside it**.

And it is already in the append-only log as though measured: `frozen-2026-08-09|||mc-match-3`
carries `mcRecall=0, mcCases=9`, where `mcCases=9` asserts the denominator was nine. `--trend` now
renders 22.2 -> 33.3 -> 44.4 -> **0** as a collapse. **The flattering direction here is not toward
the prompt — 0% looks bad for it — but toward whoever ships next**: restore the judging path,
recover 40%, and book a +40 pt improvement that never happened.

**Decided (and de-scoped to a build note, not a design question — the scorecard has no automated
consumer; `--trend` is its only reader and it prints to console):**

- a metric with no judged pairs prints `unmeasured (0 of 185 pairs judged)`, never a percentage;
- `pct()` returns `null`, not `0`, when the judged denominator is zero;
- `renderShareable()` omits a metric it cannot substantiate rather than exporting `0%`;
- the "recall is a floor" note says floor **over judged pairs**;
- the `frozen-2026-08-09|||mc-match-3` log line is corrected to `mcRecall=null, mcCases=0` with a
  note, so `--trend` stops rendering a collapse that did not occur.

This stays cheap **only while nothing reads the scorecard**. Ticket 07 specifies its answer as "a
checklist a non-author can run" — the day that lands, the scorecard becomes the gate's instrument
face and this stops being cosmetic.

### 6. Consequences for other tickets

- **Ticket 07** is unblocked by this but demoted: the gate it defines **may not contain must-catch
  recall, gold coverage or severity alignment**, because nothing measures them. Combined with
  ticket 03 (readiness exact-match is measured against a reference two humans reproduce at 2 of 4),
  the gate's honest contents are over-flag rate, blocking rules missed, restraint violations,
  contract validity and fabricated-quote count.
- **Ticket 01's `must-catch recall 0%` and `gold issue coverage 0%` must never be quoted.** They are
  `unmeasured`. The scorecard is wrong, not the run.
- **`18-evidence-base.md`** should carry the judge-drift figure (86.7% cross-time, unanimity
  predicts nothing) and the 4-of-9 validation gap on its not-known list.
