# Ticket 17 measurements: the verification run on `frozen-2026-09-19`

Run tree: `tools/quality-reviewer/v2/eval-runs/real-baseline/2026-09-19T20-24-40-subagent-packs`
(gitignored, local only, reviews quote client decks verbatim).

Prompt `frozen-2026-09-19`, sha `757a38ac6a14287b`. Previous `frozen-2026-08-09`, sha
`2371607aa850b674`. Nine cases, blind, one subagent per input, one draw each.

## 0. The confound, stated before the numbers

Neither prior baseline recorded the reviewer model. Both manifests say `model: undefined`,
because `--emit-packs` never wrote the field and only the API path did. **The "before" column
in everything below has an unrecorded variable in it.**

This run records `claude-opus-5`, effort high, thinking adaptive, mode deep. Those four are
now written by `--emit-packs`, marked in the manifest as **declared, not observed**: the
harness dispatches nothing on the subagent path, so the fields record what the operator was
asked to run, not what a dispatcher confirmed. The reviewing subagents for this run were
pinned to Opus explicitly at launch.

What this means for reading the comparison: it is **not controlled**. The 09-18 run may or
may not have been the same model at the same effort. A difference between the two columns is
consistent with the prompt change, with a model difference, or with both, and nothing in the
record can separate them. The comparison is still worth making, because the prediction was
pre-registered and specific, but no row below is a controlled before-and-after.

## 1. The prediction, scored

Recorded 2026-09-19 in ticket 16, before any run.

| metric | 08-09 | predicted | **actual** | held? |
|---|---|---|---|---|
| readiness exact | 11.1% | 33.3% | **11.1%** | **no** |
| readiness within one | 55.6% | 100% | **77.8%** | **no**, right direction |
| over-flag rate | 66.7% | 44.4% | **66.7%** | **no** |
| minor findings, of total | 1 of 45 | materially more | **4 of 42** | **yes** |

**Three of the four rows missed. Two of the three numeric rows did not move at all.**

## 2. Why, case by case. This is the useful part.

Format: `level [rules fired] findings, critical/major/minor`

| case | gold | before | after | ticket 16 predicted | verdict |
|---|---|---|---|---|---|
| real-01 | R2 | R1 [2] 5, 1/4/0 | R1 [2] 5, 1/3/1 | unchanged | held |
| real-02 | R2 | R0 [1,4] 5, 2/3/0 | **R0 [1,2]** 5, 2/3/0 | **R2 exact via rule 4** | **missed** |
| real-03 | R2 | R0 [1,2] 5, 2/3/0 | **R1 [2]** 4, 1/3/0 | **R1 via rule 2** | **held exactly** |
| real-04 | R0 | R1 [2,4] 5, 1/4/0 | R1 [2,4] 5, 2/3/0 | unchanged | held |
| real-05 | R2 | R1 [2] 5, 1/4/0 | R1 [2] 5, 1/3/1 | unchanged | held |
| real-08 | R0 | R1 [2] 5, 1/3/1 | R1 [2] 4, 1/2/1 | unchanged | held |
| real-12 | R1 | R1 [2] 5, 1/4/0 | R1 [2] 5, 1/3/1 | unchanged | held |
| real-13 | R2 | R0 [1,4] 5, 2/3/0 | **R0 [1,4]** 5, 1/4/0 | **R2 exact via rule 4** | **missed** |
| real-14 | R2 | R0 [1,2] 5, 2/3/0 | **R1 [2]** 4, 1/3/0 | **R1 via rule 2** | **held exactly** |

The pattern is clean and it is not noise:

- **The tightened gate filtered rule 1 on two of four decks, not four of four.** It stopped
  firing on real-03 and real-14. It still fires on real-02 and real-13, where the reviewer
  was able to write out two different client actions. That may be the gate working correctly
  rather than failing: on those two decks the contradiction may genuinely be decision-changing.
  Nothing here says which, and the golds say R2 on both.
- **The two cases the prediction got right are exactly the two whose fallback ceiling was
  rule 2. The two it got wrong are exactly the two whose fallback was rule 4.** Both predicted
  exact matches were rule-4 cases and both failed.
- **The model changed which rules it fired on a deck where rule 1 survived.** real-02 went
  from [1,4] to [1,2]: rule 4 stopped firing and rule 2 started. The prediction assumed the
  rest of the output holds still while one rule is tightened. **That assumption is now
  directly falsified, with a case that shows it.** Had rule 1 been suppressed on real-02, the
  remaining ceiling today is rule 2's R1, not the rule 4 R2 the counterfactual banked on. The
  arithmetic was applied to a rule set the run did not reproduce.
- **The displacement failure mode the ticket warned about did not happen.** Rule 3 fired zero
  times, as it has in all thirty-six reviews on record. Rule 1 was not re-homed.

Rule firing across the set: r1 2 of 9 (was 4), r2 8 of 9 (was 9), r3 0, r4 2 of 9 (was 3), r5 0.

**Over-flag did not move because the same six decks over-flag: real-01, real-02, real-03,
real-05, real-13, real-14, an identical set before and after.** Three of them escalate by
less than they did, which within-one picks up and over-flag cannot see, because over-flag is
a membership count and not a distance.

## 3. What the counterfactual method got wrong, precisely

It had two parts and only one of them failed.

1. **The ceiling table applied to observed blocking rules.** Not at fault. Re-measured on
   this run in section 4: it reproduces the emitted level on 9 of 9.
2. **The assumption that the rule set itself is invariant under a prompt edit.** This is the
   part that failed, twice over: rule 1 kept firing where it was predicted to stop, and rule 4
   stopped firing where it was predicted to carry the ceiling.

So the method's error is not in the arithmetic. It is that **a counterfactual over a model's
output needs the model's output, and there is no substitute for running it.** Arithmetic on
recorded blocking issues can describe a run that happened. It cannot predict a run that has
not.

## 4. The derivation (ticket 05) re-measured, including this run

    2026-07-29  frozen-2026-07-26   9/9   no-blocker cases: 0
    2026-08-02  frozen-2026-08-03   8/9   no-blocker cases: 1
    2026-09-18  frozen-2026-08-09   9/9   no-blocker cases: 0
    2026-09-19  frozen-2026-09-19   9/9   no-blocker cases: 0
    total 35/36

**Zero no-blocker decks on this run**, so ticket 05's blind spot did not open. Tightening
rule 1 made fewer rules fire without making any deck fire none: rule 2 still catches 8 of 9,
and the one deck it misses (real-13) fires 1 and 4.

**This is the evidence that separates ticket 05's claim from ticket 16's.** They share the
ceiling table but not the input to it: ticket 05 feeds it rules the review actually reported,
ticket 16 fed it rules it assumed a future run would report. The shared half was tested again
here and passed on every case, on a prompt version it had never seen. The unshared half is
what broke. See section 3 of the ticket 17 resolution for the argument in full.

## 5. Severity, the third change

| | gold (37 over 9) | before (45) | **after (42)** |
|---|---|---|---|
| critical | 3 (8%) | 13 (29%) | **11 (26%)** |
| major | 24 (65%) | 31 (69%) | **27 (64%)** |
| minor | 10 (27%) | 1 (2%) | **4 (9.5%)** |
| findings per deck | 4.1 | 5.0 | **4.7** |

Minor findings went from 1 to 4, a 4x move on the ratio the ticket named, and the row holds
in the direction predicted. It is still a third of the gold's share. Criticals barely moved,
13 to 11, against a gold count of 3.

**The noise budget stopped saturating for the first time in the project's history.** Three
decks returned 4 findings (real-03, real-08, real-14). Every previous run on every previous
prompt returned a mean of 4.89 to 5.00 with the cap hit on nearly every deck. Nobody
predicted this and the budget was not touched: the cap stayed at 5 by decision 4 of ticket
16. The plausible mechanism is that the ungated floor lets a weak finding be graded minor and
then cut by lens I, where before it had to be graded major and kept. That is a mechanism, not
a measurement, and one run does not establish it.

## 6. Two contract failures, and they are caused by this patch

`real-01` and `real-05` are contract-invalid. Both fail the same check, `check-review-v2.js`
rule 8b: **a minor finding marked `deliveryCritical: true`.**

    real-01 f5  minor, deliveryCritical=true   "Placeholder Latin remains"
    real-05 f5  minor, deliveryCritical=true   "Internal notes retained"
    real-08 f4  minor, deliveryCritical=false  "Conclusion repeats opening"
    real-12 f5  minor, deliveryCritical=false  "Unresolved internal comments"

This is a real interaction the ticket did not anticipate, and it is a consequence of the
change rather than a bad run. Rule 8b has been in the validator all along and almost never
fired, because minor findings were almost never produced: 1 in 45. Make minors common and the
invariant starts biting. Two of the four new minors carry the flag and two do not, on the same
prompt, in the same run.

Both offending findings are QA artifacts, placeholder text and internal notes left in a deck,
and the reviewer's position is defensible in plain terms: it does not change what the client
decides, so it is minor, and it must not go out of the door, so it is delivery-critical. The
prompt does not settle it. Its deliveryCritical clause is written only for the no-blocker
case, and the severity floor now has no such gate, so the two rules no longer meet.

**Nothing was edited to make these pass.** They are scored exactly as they came back, and
both are included in every figure above, at n=9.

## 7. What is not measured here

`must-catch recall` and `gold issue coverage` read 0% and are **unmeasured, not zero**
(ticket 14). Every pair in this run is new to the judge cache, so mc-match-3 scored nothing.
Neither number may be quoted.
