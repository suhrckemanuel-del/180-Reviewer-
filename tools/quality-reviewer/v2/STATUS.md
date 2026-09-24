# STATUS: reviewer v2

Updated 2026-08-08. Start here. [progress.md](progress.md) is the detailed log,
[18-evidence-base.md](18-evidence-base.md) is what is actually established,
[22-trust-boundary.md](22-trust-boundary.md) is what anyone is allowed to rely on.

An AI tool that reviews a team's draft consulting deliverables, says how close to client-ready
the work is and what to fix. A lead view for project leads, a coaching view for students.

## The state, in one table

| | where it is | what that means |
|---|---|---|
| **The product** | live at https://180dc-reviewer.pages.dev | a lead can do the whole loop from a link |
| **The prompt** | `frozen-2026-08-09`, sha `2371607aa850b674` | both axes fire. Quality still unmeasured |
| **The reach** | a three-paste chat path, no Project, no renderer, no paid account | [CHAT-CONTEXT.md](CHAT-CONTEXT.md). Open to any consultant. It produces **no readiness level or score at all**, so there is nothing to strip — see [22-trust-boundary.md](22-trust-boundary.md) section 1a. **Never run on a free model.** |
| **The findings** | trustworthy | 0% blocking rules missed, no fabricated quote ever (A1, A2) |
| **The readiness level** | **not trustworthy** | returns R0 and R2 on identical input (A4) |
| **The scorer** | **replaced and validated**, `mc-match-3` | LLM judge. Held-out AUC 0.979, accuracy 93.8% vs 84.0% for a constant (A8d) |
| **The validation set** | **weaker than claimed** | "two independent adjudicators, kappa 0.971" was one opinion copied. Real inter-rater kappa 0.562 (A8d) |
| **The next step** | **the pilot** | building stops here. Evidence comes from leads now, not the harness |

**One line:** the tool is live and useful, the prompt implements the two axes that matter, and
the measurement instrument underneath all of it was shown not to work on 2026-08-05 and was
replaced on 2026-08-08. The matcher no longer blocks anything. What it uncovered on the way out
does: the 178-pair label set everything is validated against was never double-adjudicated, so
the numbers are agreement between LLM passes and not correctness, and no human has checked a
single pair.

## When NOT to trust this tool

**Work from the findings. Do not pass on the AI's grade.** The findings carry checkable quotes
and have never missed a problem a human rated blocking; the grade has returned two different
answers on identical bytes. Never quote a recall or coverage number outside this project, and
never send a deliverable to a client on this review alone. The AI advises, a named human decides
([07-workflow.md](07-workflow.md)).

That is the summary. **The control is [22-trust-boundary.md](22-trust-boundary.md)**, and it is
where the detail now lives: who is allowed to have the tool and what has to be measurably true
before the next group gets it, what each of the four stop conditions actually trips, and the
kill switch. Two of the four are now enforced by the product rather than left for someone to
notice: nothing leaves the tab until every quote is machine-checked against the deck or the
check is waived on the record, and a readiness level cannot reach a student view, a printable or
a student pack without the view being replaced by a stop panel. The rollout was past its bar on
one count when that document was written, and section 5 says so.

## It is live

**https://180dc-reviewer.pages.dev**, deployed 2026-08-05. Redeploy steps in
[LIVE-URL.md](LIVE-URL.md). What a lead does, end to end:

1. **Opens the link** and picks a bundled review or loads their own JSON.
2. **Reads the status board**: verdict, score, effort and confidence across four tiles, the
   worst five of ten criteria in one row, and the deck timeline with callouts pinned above the
   pages they belong to.
3. **Triages every finding**: keep, turn into a question, or cut with a reason from a closed
   list of five. Keyboard throughout (`1` `2` `3` to decide, `j` `k` to move, `m` to mark the
   one it had to catch). Everything starts undecided.
4. **Pastes the deck text once**, and every quote in the review is checked as a verbatim
   substring of it. Nothing outbound unlocks until that passes or the lead waives it in writing.
5. **Sets their own readiness level.** The reviewer's answer sits beside its option labelled
   "AI guess" and is never preselected. Differing from it requires a written reason.
6. **Releases.** The note writes itself from the kept findings with quote and page attached,
   editable first. Two downloads: the note as markdown, the override record as
   `override-log-2` JSON. The student view flips to the kept set only, and the pack it travels
   in has readiness and every blocking ceiling stripped out of the payload, not just out of
   the view.

About four minutes on a five-finding deck. That is the design target being met, measured on the
synthetic cases. **It is not a saving**, because nobody has measured what this costs a lead
today, so there is no baseline to compare it against.

Two deliberate refusals. The desk does not pre-agree with the reviewer, because one that starts
fully kept and pre-set to the AI's level manufactures the agreement it exists to measure
([17-override-log.md](17-override-log.md) section 4.1). And the readiness level never reaches a
student, because A4 says it does not repeat. Since 2026-08-07 that second refusal is asserted
rather than designed in: a level string reaching a student view, a printable or a student pack
replaces the whole view with a stop panel.

## The prompt, changed 2026-08-05 and still unmeasured for quality

`frozen-2026-08-09`, sha `2371607aa850b674`. Every prior version except `b` is archived under
`eval-runs/prompt-archive/` and re-hashes correctly, so reverting is one file copy. Full record in
[19-prompt-change-2026-08-05.md](19-prompt-change-2026-08-05.md).

**What 08-09 changed, and it is small.** Five lines inside the OUTPUT block, adding one
conditional: if the pasted material includes a context document defining a chat-native output
format, write that format instead of the JSON, with every lens, rule, ceiling, severity
definition and budget still binding. Nothing else in the prompt moved. The harness never pastes a
context document, so every scored run stays on the JSON branch and no measurement is affected.
That is what reaches a branch with no Project and no renderer: three pastes into any chat window.
Design and the end-to-end demonstration in [26-chat-native.md](26-chat-native.md).

Built on two axes an ex-McKinsey consultant named independently as where a consultant's return
sits, which for the first also confirmed A6 from outside the data:

- **Communication.** The rule that cut communication findings first is deleted, a reader test
  added, and readability given a slot in the priority order instead of sitting last as a QA
  artifact.
- **Interrogating numbers.** A comparator test: compared to what, so is that good, and if not
  what is it a symptom of.
- Plus a lead-with-the-point rule, so the reviewer stops burying its own conclusions.

No blocking rule, ceiling, severity definition or noise budget was touched, so any readiness
movement in a future run is noise rather than effect.

**The method worth keeping.** The prompt is handed to two blind reviewers on a real case, who are
then asked which instructions were ambiguous to *execute*. It produced revision `b`, and running it
again on `c` produced `d` plus one serious defect nobody had predicted
([24-ambiguity-pass-c.md](24-ambiguity-pass-c.md)). It is the cheapest quality check available and
it should be routine after every prompt edit.

**The second axis was disabled and now is not (`e`, 2026-08-08).** The comparator test suspended
itself on 11 of 11 figures on a numeric deck, because its damaged-input gate keyed on any extraction
note touching the page and a note about flattened layout read to it exactly like a note about
missing values. The gate now asks one question of the note's own words, whether TEXT was lost or
only the PLACE of text, and only lost TEXT suspends anything. Measured: **11 of 11 figures suspended
before, 0 of 11 after, in both blind readers**, who classified the deciding note identically. The
one comparator finding produced rests on labels the extraction never damaged. Full record in
[25-comparator-gate.md](25-comparator-gate.md).

**What that did not settle.** Two readers on the patched prompt split on the test's second question,
whether "so is that good or bad" can be answered by the deliverable's own prose. It decides whether
the axis produces a finding at all on a given deck. Newly measurable, deliberately not patched, and
first in the queue after the pilot.

**Open design tension, not yet resolved.** The thesis puts ~60% of the value on communication.
The reader test is hard-capped at one finding and the comparator test at one, against a deep
budget of five, so the two new axes can occupy at most 2 of 5 slots and communication alone at
most 1 of 5. The caps exist to protect restraint and they are right. But finding count may
simply be the wrong instrument for expressing where value sits, and the rubric still carries
only one communication dimension of ten. Recorded rather than papered over.

## The measurement, and why it is the bottleneck

**Headline, 07-26 to 08-03**, both runs re-scored under `mc-match-2` so they sit on one matcher:
readiness exact **22.2% to 33.3%**, within one **55.6% to 77.8%**, over-flag **66.7% to 55.6%**,
must-catch recall **22.2% to 44.4%**, gold issue coverage **35.1% to 37.8%**. Blocking rules
missed stayed at 0%. Regression guard held. The tool used R2 for the first time ever, on
real-13, exact.

**Two of those were previously misreported.** Under the old fiction-fitted thresholds they read
must-catch 22.2% to 33.3% and coverage 21.6% to 32.4%. So the must-catch gain was *understated*,
it is twice what was claimed, and the coverage gain was *largely an artifact*: a reported +10.8
points is really +2.7. Every direction survives re-scoring. One magnitude does not.

**Then the instrument itself was measured, and it failed.** 178 gold-issue/finding pairs. The
matcher agreed with the labels at AUC 0.718. At its best possible cut point it classified 88% of
pairs correctly against 85% for a constant that ignores the input entirely, and at the
thresholds actually shipped it managed **83.2% against an 84.5% constant, fractionally worse
than having no model at all**. Method in [21-scorer-refit-sprint.md](21-scorer-refit-sprint.md).

**The cause was known**: it scored vocabulary overlap, and the judgement that matters is whether
two texts describe the same problem.

**It was replaced on 2026-08-08 and the replacement was measured properly.** `mc-match-3` asks
an LLM judge that question directly, three draws per pair, majority vote, cached by pair hash so
a re-score is free and offline. Developed on one half of the set and tested once on the other:

| held-out half, 89 pairs | mc-match-2, as deployed | **mc-match-3** |
|---|---|---|
| AUC | 0.704 | **0.979** |
| accuracy | 84.0% | **93.8%** |
| a constant that ignores its input | 84.0% | 84.0% |
| precision | 50.0% | **83.3%** |

The bar was AUC 0.850 and accuracy 92%. It passes against all three available label sets, and
three of four stability cases now hold a stable must-catch verdict where two of four did before.
**The judge's three draws disagree with each other on 11.8% of pairs, rising to 20% on the pairs
labelled a catch.** That is the error bar on every recall number from here and it belongs beside
them.

**What the sprint found in the input data matters more than the win.**
`check-adjudication-independence.js` shows **176 of the 178 free-text rationales in the two
adjudication files are identical to the byte**. They are not two independent opinions; they
share an origin, and Cohen's kappa cannot detect a copy, which is why 0.971 was believed for
three days. An independent re-adjudication run this sprint puts the real figure at **kappa
0.562**. Almost all of the disagreement is where `partial` begins; on the yes-versus-no line the
matcher is actually fitted to, the two independent raters agree **126 of 127, 99.2%**, which is
why the result above survives. Full account in [23-mc-match-3.md](23-mc-match-3.md).

## What happens next: the pilot

**Building stops here.** Three weeks went into measurement infrastructure, a re-fitted scorer, an
LLM judge, an adjudication-independence checker and two prompt passes, and in that time zero project
leads used the tool on a real deliverable and reported back. Nothing below extends that ratio. The
prompt implements both axes and both are now measured to fire, the findings have never missed a
blocking issue a human rated blocking, and the trust boundary is enforced by the product rather than
by anyone remembering. That is enough to put it in front of leads.

1. **Pick the decks and the leads.** Real projects, real drafts, leads who will say what was wrong
   with the review. [22-trust-boundary.md](22-trust-boundary.md) governs who is allowed the tool and
   what stops the rollout.
2. **Run it, and collect what the harness cannot see.** Did the lead act on a finding. Did a finding
   waste their time. Did they disagree with the readiness level, which the desk already forces them
   to answer in writing. The override record is the instrument and it already ships.
3. **The pilot.** Its evidence outranks anything the eval harness can produce, and it is the only
   thing that can tell this project whether the tool is useful rather than merely correct.

**Waiting, and not gating the pilot.** A human adjudicating 40 pairs is still the only thing gating
an **external claim**, because every number here is validated against labels no human has checked
and the one independence check that was claimed turned out to be a copy. Re-running the nine cases,
resolving real-10 and real-11's contradictory golds, and an ex-consultant sanity-check of near
misses are all worth doing and none of them blocks a lead opening the link. Do them after, or in
parallel, and never in front.

Out of scope and staying that way: real-06, real-07 and real-09 have no gold.

**The ship, iterate or revert call was resolved on 2026-08-05: iterate.** The prompt was edited
on the two-axis thesis rather than on blocking rule 2, which was the option on the table before
that conversation. Rule 2 remains the binding constraint on readiness and is still the obvious
next prompt edit after the matcher lands. Revert is proven, not assumed: both archived prompts
re-hash correctly and the 07-29 run folder is untouched.

## How to reproduce a run

No API key needed. Packs exist for the 08-03 prompt
(`eval-runs/real-baseline/2026-08-02T20-40-19-subagent-packs/`) and the 07-26 baseline
(`.../2026-07-29T16-29-44-subagent-packs/`, do not overwrite, it is the comparison).

```
node run-reviews.js --emit-packs                     # packs are self-contained since 2026-08-05
# one Claude Code subagent per <case>.input.md, blind, writes <case>.review.json
node run-reviews.js --collect "<abs path to packs dir>"
node rescore.js "<abs path to packs dir>"            # only when MATCHER_VERSION has moved
node scorecard.js "<abs path to packs dir>"
```

Blindness is what makes the number honest: a reviewing agent must never see
`eval-cases-real/labeling/`, any `*.gold.md`, any worksheet, or another case's review.

`node check-docs.js` before a commit: reads the prompt version, prompt sha, matcher version and
the override-record version out of the code, then flags any document asserting
a different value in the present tense, plus every dead link and anchor. It catches version
drift only, not stale claims of state, and it is tuned to under-flag.
