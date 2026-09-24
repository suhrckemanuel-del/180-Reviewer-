# Ticket 16: what the measurements say

Measured 2026-09-19 from `eval-runs/real-baseline/2026-09-18T22-00-30-subagent-packs`
(the ticket 01 baseline, `frozen-2026-08-09`, sha `2371607aa850b674`), against the eleven
gold worksheets in `eval-cases-real/labeling/`, plus the three earlier real-deck runs.
No new reviews were run. Everything below is arithmetic on recorded output.

## 1. The ticket's hypothesis is wrong: the noise budget does not cause the over-flag

The ticket says "fixing saturation and fixing over-flag are probably the same job."
They are not the same job, and the budget is not the mechanism.

Readiness is set by the blocking rules and by nothing else. The prompt's synthesis protocol
step 8 says "Determine readiness from blocking issues, not from the score mean", and the
readiness block says "Readiness is the lowest ceiling among the blocking issues that fired".
**The number of findings cannot move readiness.** So the noise budget cannot be the mechanism
behind over-flag, whatever else is wrong with it.

The actual mechanism is visible in the scorecard's own blocking column:

| case | gold blocking | review fired | gold | pred |
|---|---|---|---|---|
| real-01 | none | rule 2 | R2 | R1 |
| real-02 | none named | rules 1, 4 | R2 | R0 |
| real-03 | none | rules 1, 2 | R2 | R0 |
| real-04 | yes | rules 2, 4 | R0 | R1 |
| real-05 | none | rule 2 | R2 | R1 |
| real-08 | yes | rule 2 | R0 | R1 |
| real-12 | yes | rule 2 | R1 | R1 |
| real-13 | none | rules 1, 4 | R2 | R0 |
| real-14 | none | rules 1, 2 | R2 | R0 |

**The six over-flagged cases and the six blocking false positives are the same six cases,
exactly.** Over-flag rate 66.7% and blocking-false-positive rate 66.7% are not two
correlated metrics. They are one metric counted twice.

## 2. Rule 2 fires on 9 of 9. Rule 1 carries the whole regression.

Rule firing across the nine decks:

- **rule 2** (client decision unclear, or the deck does not answer the question, or the core
  recommendation is unsupported; ceiling R1): **9 of 9**
- **rule 1** (a contradiction the recommendation rests on; ceiling R0): **4 of 9** — real-02,
  real-03, real-13, real-14
- **rule 4** (ungrounded headline number; ceiling R2): 3 of 9
- rules 3 and 5: never

Those four rule-1 cases are exactly the four gold-R2 decks predicted R0 that ticket 01 called
"the largest possible miss". Rule 1 is the entire minus-two tail.

Rule 2 has never been edited. Across all five commits that touched the prompt document its
text is byte-identical, while rule 1 gained its guardrail on 2026-08-07 in the trust-boundary
commit. **The clause that fires on every deck is the one clause nobody has looked at.**

### Counterfactual: suppress rule 1, keep everything else

This is arithmetic on the recorded blocking issues, not a new run. Rule 1's guardrail already
says an inconsistency that does not change what the client does "is a major finding and fires
nothing", so suppression here means applying the rule as written, and the readiness level
falls to the next ceiling that actually fired.

| case | gold | now | rule 1 suppressed |
|---|---|---|---|
| real-02 | R2 | R0 | **R2 exact** (rule 4 ceiling) |
| real-13 | R2 | R0 | **R2 exact** (rule 4 ceiling) |
| real-03 | R2 | R0 | R1 (rule 2 ceiling) |
| real-14 | R2 | R0 | R1 (rule 2 ceiling) |
| the other five | — | — | unchanged |

| metric | 08-03 | 08-09 now | 08-09 minus rule 1 |
|---|---|---|---|
| readiness exact | 33.3% | 11.1% | **33.3%** |
| readiness within one | 77.8% | 55.6% | **100%** |
| over-flag rate | 55.6% | 66.7% | **44.4%** |

One rule restores the 08-03 exact rate, beats both prompts on over-flag, and takes
within-one to every case in the set.

**Asymmetry worth naming:** rule 1's suppression is simulable because another ceiling remains
on all four cases. Rule 2's is not. On real-01 and real-05 it is the only rule that fired, so
suppressing it leaves readiness unpinned and the level unpredictable without a re-run. Any
rule-2 change has to be measured, not calculated.

**Caveat on the whole section:** this counterfactual is scored against one labeler's golds,
and ticket 03 measured that labeler's agreement with a second reader at 2 of 4 with a 95%
interval of [7%, 93%]. What the counterfactual shows is the direction and the mechanism. The
decimal places are not load-bearing.

## 3. Saturation is chronic, predates every prompt change, and is the smallest of the three errors

Findings per review, mean across the nine real decks:

| run | prompt era | mean |
|---|---|---|
| 2026-07-29 | the original baseline | 4.89 |
| 2026-08-02 | — | 4.89 |
| 2026-09-18 | `frozen-2026-08-09` | 5.00 |

Saturation is not something 08-09 introduced. It has been the behaviour since the first
real-deck run, through every prompt version, across decks of 11 to 45 slides.

Against the gold, volume is the least wrong thing about the output:

| | gold (n=37 over 9 decks) | review (n=45 over 9 decks) | ratio |
|---|---|---|---|
| issues per deck | 4.1 | 5.0 | **1.2x** |
| critical | 3 (8%) | 13 (29%) | **4.3x** |
| major | 24 (65%) | 31 (69%) | 1.3x |
| minor | 10 (27%) | **1 (2%)** | **0.1x** |

**The budget is 22% over. The severity grading is off by a factor of four in both
directions.** The reviewer wrote one minor finding in forty-five.

### Why minors never appear

The prompt's demotion floor reads: "When a deck fired no blocking rule, default a finding to
minor and promote it to major only when you can name the specific way the client's decision
changes without the fix."

It is gated on the deck firing no blocking rule. A blocking rule fired on **9 of 9** decks in
this run, 9 of 9 in 2026-07-29, and 8 of 9 in 2026-08-02. The floor added on 2026-07-03 to fix
exactly this failure has engaged on **one real deck out of twenty-seven reviews**. On real
decks it is dead text.

## 4. The restraint case, tested as the ticket asked

real-05, gold R2 and explicitly called "almost Nearly ready", the strongest deck in the set.
Its gold worksheet says in as many words: *"Restraint matters on this one, it is a strong deck
and manufacturing criticals here to justify a lower readiness would be a calibration failure."*

The review returned **5 findings: 1 critical, 4 major, 0 minor**, fired blocking rule 2, and
set R1. The gold's own list is 3 major and 1 minor with no blocking rule.

So yes: the tool emits 5 findings on the best deck in the set, and restraint is not working.
But the count is the least of it. The gold wanted four issues and got five, wanted zero
criticals and got one, wanted a minor and got none.

**The honest caveat, because this cuts the other way.** Three of the five findings match gold
issues (the thin way forward at slide 27, the missing pyramid executive summary, the roadmap
depth). And the critical the tool raised, the deck asserting IFC eligibility without measuring
the client against any funder's criteria, sits precisely where the gold labeler recorded their
own uncertainty: *"The labeler does not know what IFC is and so could not judge whether the IFC
funding route is the right recommendation."* That finding may be a real catch the gold cannot
score. The severity and the blocking ceiling are still wrong.

## 5. Confidence has never varied on a real deck, under either rule

The short-circuit landed on 2026-08-08 in the ambiguity pass, as Patch 2, and it was a
deliberate fix to a real defect: two blind readers returned Medium and Low on byte-identical
input, and the patch ordered the two tests so a presence check on three named fields runs
first. It worked. It also pinned the field.

Every real-deck review ever produced, by regime:

| regime | reviews | readiness.confidence |
|---|---|---|
| before the short-circuit (07-29, 08-02, the stability collects) | 29 | **Medium, 29 of 29** |
| after (comparator gate 08-08, the 09-18 baseline) | 12 | **Low, 12 of 12** |

**Never High. Never mixed. Zero variance inside either regime.** The field did not lose its
signal on 2026-08-08; it never had any. It was a constant that changed its constant value, and
every confidence reading in the evidence base silently changed meaning on that date with
nothing recording it.

Three reasons it cannot vary, and they are structural:

1. **High is unreachable by rule.** "Missing evidence notes never allow High", and the emitter
   leaves that field blank on every case by design.
2. **Medium is guaranteed by construction.** The Medium test is "every finding that sets
   readiness rests on text you can quote". Quote-or-abstain already requires a verbatim quote
   on every finding or the finding is dropped. The test is satisfied by the rule that produced
   the findings. That is why the pre-patch era is 29 of 29 Medium with the same blank field.
3. **Low is a form-completeness check.** Post-patch it reports whether three template fields
   were filled in, which is something the person who filled the template already knows.

### The emitter's blank fields are correct and must not be "fixed"

`run-reviews.js:210` carries the reason in a comment: *"the blank fields are deliberate: the
human labeler had no extra context either, so supplying any would make the run and the gold
answer different questions."* Populating EVIDENCE AND SOURCE NOTES from the case file would
break gold comparability on every case in the set. **That option, which the ticket lists first,
should be struck.**

### The signal the field was supposed to carry already exists elsewhere

`readiness.whatCouldChangeIt` is richly case-specific on all nine: it names the missing excel
on real-04, the four slides that extracted blank on real-03, the six sub-models on real-13.
Retiring the three-valued label costs nothing as long as that sentence stays.

### One inconsistency found in passing

Three reviews in the pre-patch era carry `readiness.confidence` Medium and
`scorecard.confidence` Low in the same document. Two fields, one question, no rule saying they
must agree. Whatever is decided, they should not both survive.

## 6. What this leaves to decide

1. Whether to touch blocking rule 1, which means breaking the change-isolation discipline that
   every prompt-change document since 2026-08-05 has promised to keep.
2. Whether to ungate the severity demotion floor so minor findings become reachable on decks
   that fired a blocking rule.
3. Whether the confidence label is retired or repaired.

The noise budget cap itself is not on that list. On the measurement it is 22% over and it
cannot move the metric the gate needs. Recommendation, stated rather than asked: **leave the
cap at 5 and let the severity fix do the restraint work.** If severity grades honestly, a
strong deck's five findings become one major and four minors, which reads as restraint to the
student whatever the count is. Overrule this if the cap should move anyway.
