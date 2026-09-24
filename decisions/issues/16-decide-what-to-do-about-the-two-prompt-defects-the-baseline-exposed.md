# Decide what to do about the two prompt defects the baseline exposed

Type: grilling
Status: resolved
Blocked by: —

## Question

Surfaced in review on 2026-09-19. Ticket 01 found both while running the baseline and neither has
a home. They are distinct from the bundle defects in ticket 08 — these fire on the **harness** path,
where the missing material is present.

### 1. Confidence is pinned Low on all nine cases by construction

`EVIDENCE AND SOURCE NOTES` is blank in every generated pack, and the prompt short-circuits
confidence to Low whenever it is. So the Medium test has never run on a real case, and the
confidence field has carried no information in any real-deck measurement ever taken.

Settle: does `--emit-packs` populate the field from the case, does the prompt stop short-circuiting,
or is confidence retired as a field that never earned its place? Note the third option has a
precedent this week — readiness is going for a similar reason. Whatever is chosen, every
confidence reading in the existing evidence base was produced under the short-circuit and should be
marked as such.

### 2. The noise budget saturates every time

Exactly 5 findings on all nine decks. The decks run 11 to 45 slides. A budget that is hit on every
input regardless of size is not a ceiling the model is choosing under — it is a target it is
filling, which is the opposite of the restraint the budget exists to create.

Settle: does the budget scale with deck length, does it stay flat and the prompt push harder on
"say nothing when there is nothing", or is saturation the expected and acceptable behaviour of a
deep-mode review? Worth testing against the restraint case (real-05, gold R2 almost R3) before
deciding — if the tool emits 5 findings on the best deck in the set, restraint is not working.

Both interact with ticket 15: over-flag at 66.7% is the metric that survives readiness retirement,
and saturation is the most likely mechanism behind it.

Answer records: the fix or the retirement for each, and which existing measurements are invalidated.

---

**Promoted 2026-09-19 (during ticket 14).** The owner took the eval loop off the critical path and
chose to ship `frozen-2026-08-09` **with these two defects fixed first** — see ticket 15. That makes
this ticket a **precondition of the pilot**, not a cleanup item.

The noise-budget half is now the more urgent of the two. With the matcher metrics gone from the
gate and readiness retiring, **over-flag rate is close to the only survivor**, and ticket 01 named
budget saturation as its most likely mechanism. Fixing saturation and fixing over-flag are probably
the same job.

## Answer (2026-09-19)

Three owner decisions, all taken knowingly against a stated case for the other side. Full
measurement record: [ticket-16/MEASUREMENTS.md](../ticket-16/MEASUREMENTS.md). Nothing was re-run;
every figure below is arithmetic on the ticket 01 baseline output and the eleven gold worksheets.

### The ticket's own hypothesis was wrong, and that is the main finding

The ticket said "fixing saturation and fixing over-flag are probably the same job". They are not
the same job and they do not share a mechanism.

Readiness is set by the blocking rules and by nothing else. The synthesis protocol's step 8 says
"Determine readiness from blocking issues, not from the score mean", and the readiness block says
"Readiness is the lowest ceiling among the blocking issues that fired". **There is no path from the
number of findings to the readiness level.** The noise budget cannot move over-flag no matter what
is done to it.

What does move it is visible in the scorecard's own blocking column: **the six over-flagged cases
and the six blocking false positives are the same six cases, exactly.** Over-flag 66.7% and
blocking false positives 66.7% were never two correlated metrics. They are one metric counted
twice, and the project has been reporting both as if they corroborated each other.

Rule firing across the nine decks: **rule 2 on 9 of 9**, rule 1 on 4 of 9, rule 4 on 3 of 9, rules
3 and 5 never. The four rule-1 cases are exactly the four gold-R2 decks predicted R0 that ticket 01
called the largest possible miss. **Rule 1 is the entire minus-two tail.** And rule 2, the clause
that fires on every single deck, is byte-identical across every commit that has ever touched the
prompt document: the one clause nobody has looked at.

### Decision 1. Blocking rule 1 is tightened

The reviewer must name the two different things the client would do under the two readings. If it
cannot name them, the contradiction is an ordinary finding and fires nothing. This is not new
policy, it is the rule's existing guardrail made checkable: the guardrail already says an
inconsistency where "the client's action is the same either way" fires nothing, and the model is
not applying it.

Predicted effect, by arithmetic on the recorded blocking issues:

| metric | 08-03 | 08-09 now | 08-09 with rule 1 tightened |
|---|---|---|---|
| readiness exact | 33.3% | 11.1% | **33.3%** |
| readiness within one | 77.8% | 55.6% | **100%** |
| over-flag rate | 55.6% | 66.7% | **44.4%** |

real-02 and real-13 land on gold exactly via rule 4's R2 ceiling; real-03 and real-14 move from two
levels over to one.

**The case against, accepted knowingly:** this breaks the change-isolation discipline. Every
prompt-change document since 2026-08-05 closes with a written promise that no blocking rule,
ceiling, severity definition or noise budget was touched, precisely so that readiness movement in a
later run is a real effect and not noise. That promise cannot be made about the next version. And
the evidence is nine decks from one labeler whose agreement with a second reader ticket 03 measured
at 2 of 4, 95% CI [7%, 93%].

**Therefore this prediction is a prediction, and it is recorded before the run.** 33.3% exact,
100% within one, 44.4% over-flag. If the verification run comes back materially different, the
counterfactual method is wrong and that matters more than the patch does.

### Decision 2. The severity demotion floor is ungated

A finding is minor whenever closing it would not change what the client actually does, whatever
else is wrong with the deck. The floor stops being conditional on the deck firing no blocking rule.

The floor was added on 2026-07-03 to fix exactly this failure. It is gated on the deck having no
blocking issues, and a blocking rule fired on 9 of 9 decks in this run, 9 of 9 in 2026-07-29 and
8 of 9 in 2026-08-02. **It has engaged on one real deck out of twenty-seven reviews.** On real
decks it is dead text, and it has been dead since the day it shipped.

What it was meant to prevent, measured against the golds:

| | gold (37 issues, 9 decks) | review (45 issues, 9 decks) | ratio |
|---|---|---|---|
| issues per deck | 4.1 | 5.0 | **1.2x** |
| critical | 3 (8%) | 13 (29%) | **4.3x** |
| major | 24 (65%) | 31 (69%) | 1.3x |
| minor | 10 (27%) | **1 (2%)** | **0.1x** |

One minor finding in forty-five.

**The case against, accepted knowingly:** criticals are what make a lead stop and read. Six of the
nine decks genuinely were not client-ready, and a tool that softens on those decks helps a team
send weak work to a real client. Turning the volume down is easy to overshoot and hard to notice.

### Decision 3. The confidence label is retired. The sentence under it stays.

The confidence fields on the readiness block and the scorecard are deleted. The
"what could change it" sentence survives unchanged and carries the whole signal: it is richly
case-specific on all nine cases, naming the missing excel on real-04, the four blank-extracted
slides on real-03, the six sub-models on real-13.

The evidence for retirement is not that the field lost its signal in August. It is that **it never
had any**, across forty-one real-deck reviews under two different rules:

| regime | reviews | readiness confidence |
|---|---|---|
| before the short-circuit (07-29, 08-02, stability collects) | 29 | **Medium, 29 of 29** |
| after (comparator gate 08-08, the 09-18 baseline) | 12 | **Low, 12 of 12** |

Never High, never mixed, zero variance inside either regime. Three structural reasons, and they
close off every repair:

1. **High is unreachable by rule** - "missing evidence notes never allow High", and the notes are
   always absent.
2. **Medium is guaranteed by construction** - the Medium test asks whether every finding that sets
   readiness rests on quotable text, and quote-or-abstain already drops any finding without a
   verbatim quote. The test is satisfied by the rule that produced the findings. That is why the
   pre-patch era is 29 of 29 Medium *with the same blank field*.
3. **Low is a form-completeness check** - it reports whether three template fields were filled in,
   which the person who filled the template already knows.

**The ticket's first option is struck.** Populating the evidence field from the case would break
gold comparability on every case in the set: `run-reviews.js:210` says so in a comment, and it is
right. The blank fields are deliberate because the human labeler had no extra context either.

**The case against, accepted knowingly:** the red-team document names this field as the designed
defence against false confidence, and removing a visible hedge from a tool aimed at students reads
badly in hindsight if the tool is later confidently wrong. The mitigation is that the hedge
survives as a sentence rather than a label, and the sentence says more.

### Decision 4, stated not asked. The noise budget cap stays at 5.

Saturation is real, chronic and the least wrong thing in the output. Mean findings per review:
4.89 on 2026-07-29, 4.89 on 2026-08-02, 5.00 on 2026-09-18 - unchanged by every prompt version
ever shipped, across decks of 11 to 45 slides. It is 22% over the gold's 4.1, against severity
errors of 4x in both directions.

The answer to the ticket's third framing, "is saturation the expected and acceptable behaviour of
a deep-mode review", is **effectively yes, once severity is honest.** A strong deck's five findings
graded one major and four minors reads as restraint whatever the count is. Five findings all graded
major or critical does not. The restraint failure was never about volume.

### The restraint case, tested as the ticket required

real-05, gold R2 and explicitly "almost Nearly ready", whose gold worksheet says *"manufacturing
criticals here to justify a lower readiness would be a calibration failure"*. The review returned 5
findings, 1 critical, 4 major, **0 minor**, fired rule 2, set R1. Gold: 3 major, 1 minor, no
blocking rule.

**Restraint is not working, and the ticket's test is met.** Two honest qualifications that cut the
other way and belong in the record: three of the five findings do match gold issues, and the
critical the tool raised, the deck asserting IFC eligibility without measuring the client against
any funder's criteria, sits exactly where the labeler wrote *"the labeler does not know what IFC is
and so could not judge whether the IFC funding route is the right recommendation"*. That finding
may be a real catch the gold cannot score. The severity and the ceiling are still wrong.

### Which existing measurements are invalidated

**Every confidence reading in the evidence base, all of them, in both directions.** Not just the
post-August ones. A constant is not a measurement, and the constant changed value on 2026-08-08
with nothing recording it, so any document comparing a confidence reading from before that date
with one from after is comparing two different definitions. Specifically:

- `18-evidence-base.md` - any claim resting on a confidence reading.
- `16-board-package.md:271` and `:287`, and the stress-test row at `16a-board-package-stress-test.md:112`.
  These say confidence "is not demonstrated to be reproducible". That was too generous. It is
  perfectly reproducible and perfectly uninformative.
- `11-decision-log.md:25` (2026-07-02) records the Medium-versus-Low rule and ends "Test: re-run
  both, expect Medium on both". **That test was never run**, and the 2026-08-08 short-circuit made
  it unrunnable.
- `13-usage-guide.md:282-283`, the troubleshooting rows telling a team to fill in the evidence
  notes and re-run to raise confidence. On the harness path that advice could never have worked.
- `08-red-team.md:50-51`, the detection and mitigation for false confidence.
- `03-output-contract.md:36,51`, `check-review-v2.js:28,71,102`, `CHAT-CONTEXT.md:313`.

**Found in passing, and it should not survive either:** three pre-patch reviews carry a Medium
confidence on the readiness block and a Low on the scorecard in the same document. Two fields, one
question, and no rule anywhere saying they must agree.

**Nothing about the noise budget or severity is invalidated** - those figures were measured
correctly and simply read wrong. The scorecard's over-flag and blocking-false-positive rows,
however, should stop being presented as independent corroboration. They are the same six cases.

### What this does not settle

**Rule 2 fires on 9 of 9 and nothing above touches it.** It was deliberately left alone: unlike
rule 1, its effect cannot be calculated. On real-01 and real-05 it is the only rule that fired, so
suppressing it leaves readiness unpinned and the level unpredictable without an actual run. It is
now ticket 18, blocked on the verification run in ticket 17.
