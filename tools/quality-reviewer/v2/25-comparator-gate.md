# 25. The comparator gate, and whether the second axis fires

**Verdict: yes, the axis fires.** The gate suspended 11 of 11 decision-driving figures before the
patch and 0 of 11 after it, in both blind readers. The comparator test now runs on every figure in
a numeric deck instead of switching itself off, and the one comparator finding it produced is
legitimate: it rests on labels the extraction did not damage, not on values it did.

Ran 2026-08-08, same day as [24-ambiguity-pass-c.md](24-ambiguity-pass-c.md), against the open
defect that document left on the record. Result: **`frozen-2026-08-05e`**, sha `5a8d4ef2d651a064`.
One paragraph changed. One new defect found, one clause left open, neither patched.

## 1. The defect, confirmed on the current prompt

Section 6 of the ambiguity pass measured the collapse on revision `c`. None of the five `d` patches
touched this gate, so the first thing to establish was that the defect survived into the prompt
actually in force. It did.

One blind reviewer, `frozen-2026-08-05d`, real-13, under the blindness rules in
[05-eval-harness.md](05-eval-harness.md). It read one self-contained pack and nothing else on the
machine. Result: five findings, **zero comparator findings**, and this in `notAssessed`:

> "Whether the figures on slides 15 to 19 and 21 are measured against a stated comparator. The
> extraction notes flag those pages as having their percentage and kg figures detached from their
> scenario labels, so the comparator is unassessable for every figure the recommendation leans on
> and no finding was raised on it."

Three things in its gate log matter more than the count.

**It saw the comparator and the gate told it not to look.** Its own words: "Some of the figures do
carry a label reading '% of CO2 saved compared to traditional box', which on its face names a
comparator. I did not rely on that, because the mechanical test fired first and it is the test the
instruction told me to apply." The reviewer had already reached the right judgment and the
instruction overrode it.

**The suppression reached the rubric, not only the findings.** Dimension 5 carries a sub-check for
whether the argument's numbers are given something to be measured against. It could not be run, so
the reviewer scored that dimension over three sub-checks rather than four.

**It weakened an unrelated finding.** The critical slide 16 against slide 22 contradiction was built
on prose alone: "The ~90% on slide 21 would have made that finding sharper and I left it out."

So the axis was not merely quiet. It was disabled in three places at once.

## 2. The mechanical boundary

The distinction available is a property of the extraction note itself. The question is what the note
says was lost:

**TEXT**, meaning words are not in the input you were given. Or **PLACE**, meaning every word is in
front of you and only its position, order, pairing or formatting went.

Only lost TEXT suspends the comparator, and only for figures on the pages that note names or in a
table or exhibit those pages refer to. Lost PLACE suspends nothing.

**Why this boundary and not another.** The comparator test asks whether the deliverable names a
comparator anywhere. That is a question about the presence of words. Reordering does not remove
words, so a comparator the team wrote is still on the page to be read however badly ordered.
Deletion does remove them, and there the reviewer genuinely cannot establish absence. The boundary
tracks the one thing that actually decides whether absence is establishable.

**Why two readers land on the same side.** The test is a read of the note's own wording against two
closed lists, not a judgment about the figure, not a counterfactual about what a damaged exhibit
might have held, and not an opinion about severity of damage. The lists are not invented for this
deck. They are the vocabulary the intake convention already uses across the corpus:

| Lost TEXT, as written in the real cases | Lost PLACE, as written in the real cases |
|---|---|
| "no extractable text" (real-02) | "loose floating numbers" (real-01) |
| "not recoverable as text in the extraction" (real-02) | "lost their visual layout ... in scrambled order" (real-03) |
| "image-only and not extracted" (real-02) | "one word per line" (real-04) |
| "extracted with no text" (real-03) | "lost its two-column layout ... a single scrambled block" (real-05) |
| "no extracted numeric values at all" (real-01) | "interleaved and out of alignment" (real-08) |
| "extracted as empty" (real-10) | "flattened into a loose list; kept as extracted" (real-09, real-10, real-13) |

The corpus separates cleanly. Every "known gaps" bullet in the fourteen real cases falls on one side
or the other, and the two vocabularies do not overlap.

**A human drew the same line independently.** real-13's gold worksheet, written 2026-07-25 by a
labeler who had never seen this instruction, lists under false positives to avoid: "Do not penalise
the divider slides carrying DATE and TITLE and SUBTITLE placeholder labels, or the chart and
infographic slides whose figures float loose in the extract, as empty. **That is extraction
flattening, not a real gap.**" That is the patch's distinction, in a human's words, before the patch
existed.

**The patch, in full.** Section A step 5, the damaged-input paragraph only. Diffed
mechanically, and the change is a **single contiguous block**: 84 identical lines above it, 151
identical lines below it, four lines out and fifteen lines in. 235 of `d`'s 239 lines survive
byte-identical and in place. The line immediately below the block is the comparator severity
sentence, unchanged. No blocking rule, no ceiling, no severity definition and no noise budget was
touched, and that is asserted in code rather than by eye.

## 3. Before and after, as counts

Two blind readers on the patched prompt, fresh contexts, byte-identical packs, neither able to reach
the other's directory or anything under `eval-cases-real/labeling/`.

| | before, `d` | after, `e`, reader A | after, `e`, reader B |
|---|---|---|---|
| **Figures suspended by the gate** | **11 of 11** | **0 of 11** | **0 of 11** |
| Comparator findings | 0 | 0 | **1** |
| Findings total | 5 | 5 | 5 |
| Readiness | Not ready | Needs targeted revision | Not ready |

**The mechanical result is the first row and it is unambiguous.** The gate went from suspending
every figure the recommendation leans on to suspending none, in both readers, on the same input.
That is the defect closed.

**The finding count is 0, 0 and 1, and the honest reading is in section 5.** Reader A ran the test
on all eleven figures and concluded the deliverable passes it. Reader B ran the test on the same
eleven figures and concluded it fails at the second question. That is a real divergence and it is
not in the gate.

**Readiness moved and it means nothing.** A4 says readiness returns different levels on identical
bytes, and no blocking rule, ceiling, severity definition or noise budget was touched here, so the
move from R0 to R2 in one reader is noise by construction. It is recorded because it happened, not
because it is evidence. Reader A matching the gold's R2 exactly is one draw and is not a result.

**Interruption, disclosed.** Both patched-prompt readers hit a monthly spend limit at the moment of
composing their final summary message, after both had written their review and their gate log. The
artifacts are complete and both pass `check-review-v2.js`, quotes verbatim against the deck. Every
count in this document was read out of the JSON directly rather than taken from a reviewer's
self-report, which is how it should have been done regardless. The same thing happened to reviewer B
in the ambiguity pass and is recorded there for the same reason.

## 4. The determinism re-check, which is what protects Track A

Both readers were asked to classify every extraction note and say which words decided it. Five note
units, classified independently:

| Note | reader A | reader B | |
|---|---|---|---|
| Source and provenance line | reports no loss, suspends nothing | not a loss report, suspends nothing | same |
| Divider slides 1, 5, 9, 13, 14, 20, 25 | lost PLACE | lost PLACE | same |
| **Numeric slides 15-19, 21-24** | **lost PLACE** | **lost PLACE** | **same** |
| Anonymisation, client name replaced | lost PLACE | lost PLACE | same |
| Anonymisation, slide 3 replaced in full | lost PLACE | lost TEXT | **diverged** |

**The note that caused the collapse was classified identically, and for identical stated reasons.**
Both quoted the same deciding words out of note 3: "floating", "disconnected from their
box-size/scenario labels", "flattened", "loose list", "kept as extracted", "ligature artifacts".
Both stated that not one lost-TEXT marker appears in it. Reader B went further and verified the
values are physically present in the input before classifying. Neither reader reasoned about what
the damaged infographic might have held, which is the behaviour the instruction is built to prevent.

**Gate outcome: identical.** Zero figures suspended, both readers, and the same eleven-figure list
tested normally: slide 15 (30%, 0.07, 78%, 0.56), slide 17 (71%, 78%), slide 18 (40%, 30%), slide 19
(+2-5%, +2.2 kg, 0.5 kg), slide 21 (~90%).

**The one divergence, and why it does not reject the patch.** The slide 3 clause says the
team-introduction slide "was replaced in full ... per policy". Reader A called it lost PLACE because
the instruction names anonymisation replacement explicitly. Reader B called it lost TEXT because
eight names with their affiliations are genuinely not in the input. Both readers **independently
identified this as the judgment call**, and both **independently proved it inert**: slide 3 carries
no figure and refers to no table or exhibit, so the set of figures it suspends is empty under either
reading. Reader A: "If a figure had sat on slide 3 I would have flagged this as a live ambiguity for
the lead."

So the determinism claim is precise, and weaker than "no divergence". **The gate's decision is
deterministic on this input. One clause's label is not, and the divergence is provably inert here
because a team-introduction slide never carries a decision figure.** That inertness holds across the
corpus, since the full-replacement convention is applied only to team slides. It is left open in
section 6 rather than patched, because patching it would ship an edit no two readers have tested and
its measured effect on this case is zero.

Track A bought determinism on the mechanical test and the patch did not spend it.

## 5. Are the findings legitimate, or is the gate firing by going blind

One comparator finding exists across both patched runs. Checked against the three ways it could be
wrong.

**Reader B, "Savings lack yardstick", major.** "The savings figures are measured only against the
deck's own conventional box, so the client cannot tell whether the advantage is worth building a
campaign on."

**Does the figure genuinely lack a comparator?** No, and the finding does not claim it does. This is
the second limb, "compares but never says what the comparison implies", not the first. The finding
opens by granting that the deck answers compared to what. A first-limb "no comparator" finding on
this deck would have been false, because "% of CO2 saved compared to traditional box" is printed on
slides 15, 17 and 18. Neither reader raised one. **This was the specific failure the sprint was told
to watch for and it did not occur.**

**Is the absence it claims establishable from undamaged material?** Yes, and verified independently
of both readers. A search across all 26 slides for target, benchmark, industry, competitor, average,
baseline, goal and market returns nothing but the phrase "an average of multiple datasets" inside a
methodology note. There is no external reference point anywhere in the deliverable.

**Does the finding depend on material the extraction damaged?** No, and this is the part that
matters most. Its three evidence quotes are "% of CO2 saved compared to traditional box" (slide 15),
"Kg of CO2 saved per box" (slide 15) and "Total Kg of CO2 saved through Client R13 per year" (slide
7). Labels and an output name. Not one value paired to a scenario, which is exactly what note 3 says
was flattened. Reader B stated the constraint before writing the finding: "The finding would stand
unchanged whichever percentage belongs to whichever box size."

**And the finding is sharper than the gold.** Slide 6 takes "Number of parcels per year" as a model
input. Slide 7 promises "Total Kg of CO2 saved through Client R13 per year" as a model output. The
results section reports per-box figures only and never once reports an annual number. Verified in
the deck. The team built a model that answers the client's real question and then presented the
answer it could not size. No labeler caught that, and it came out of the axis this sprint switched
back on.

**Verdict: legitimate.** The gate is not firing by going blind to damaged input. It is firing on
material the damage never touched, and the reviewer that raised it said so unprompted.

## 6. Read as a lead, and the new defect

**It does not flood.** One comparator finding covering five slides as a group, inside a five-finding
budget, in the reader that raised one. The other raised none. The "raise this ONCE for the
deliverable" cap held without being tested, and no reviewer returned a finding per number.

**The numbers are interrogated now, in both reviews.** Reader B does it as a comparator finding: "A
saving that reads large per box may be small per year, and no competitor claim is given to beat."
Reader A does it under blocking rule 4 instead, making its critical finding the fact that the 78%
and ~90% cases rest on a breakage scenario the deck never measures the frequency of. Both are a lead
reading numbers and asking what they are worth. Before the patch the review's entire numeric content
was one unsourced-ratios finding, and the reviewer had recorded that the gate stopped it from doing
more.

**The new defect, and it is the successor to the one just fixed.** The two readers diverged on the
comparator test's second question, "so is that good or bad". Reader A took the deck's own prose to
answer it: "BROKEN ITEMS HAVE A HUGE IMPACT", "the emissions savings are dominated by broken items".
Reader B held that every comparator in the deck is internal to the deck's own model and that nothing
external says whether the result is good.

**Reader B has the better of it.** A deliverable asserting its own result is huge is not a yardstick,
and reading it as one makes the second question answerable by adjective. But the instruction does not
currently decide between them, and this is the first time it could possibly have been measured,
because until this patch the gate switched the test off before the second question was ever reached.
This is prediction 4 of the ambiguity pass moving from "never ran" to "runs and is underdetermined".

**Not patched.** The sprint's constraint is one fix, and a second edit to the same instruction, made
without a second measured pass, is how a pilot review ends up looking wrong for a reason nobody can
name. It is the first item in the handover.

## 7. Definition of done

- `04-prompt-templates.md` patched, one paragraph. **`frozen-2026-08-05e`, sha `5a8d4ef2d651a064`,
  18,304 bytes.**
- `d` archived verbatim at `eval-runs/prompt-archive/frozen-2026-08-05d.txt`, **re-hashes to
  `fc39d6b6f928ed3a`**, asserted in code not by eye. Archive chain now 07-26, 08-03, 08-05, 08-05c,
  08-05d. Revert is one file copy.
- Constraint check, machine-verified: the comparator severity sentences are byte-identical across
  `d` and `e`, and the diff touches nothing but the damaged-input paragraph. No blocking rule, no
  ceiling, no severity definition, no noise budget, no reader test.
- `node check-docs.js` clean, 50 documents.
- Both patched reviews pass `node check-review-v2.js` against the deck, quotes verbatim.

**Not done, and deliberately.** The reviews were not scored against gold. Scoring routes through
`mc-match-3`, which spends API on an LLM judge, and this sprint is judged on comparator counts and
legitimacy rather than on precision and recall. The nine-case set is unaffected and still sits where
[STATUS.md](STATUS.md) leaves it.

## 8. Handover: found, and deliberately not fixed

1. **The comparator test's second question is underdetermined.** Two blind readers on the patched
   prompt split on whether "so is that good or bad" is answered by the deliverable's own prose. It
   decides whether a comparator finding exists at all, so it decides whether the axis produces
   anything on a given deck. **This is the highest-value item in the queue** and it is newly
   measurable only because this sprint ran. Section 6.
2. **The TEXT/PLACE call on a wholly substituted page.** The two readers split on the slide 3
   anonymisation clause. Inert on every deck in the corpus, because full replacement is applied only
   to team-introduction slides, which carry no figures. It stops being inert the first time a page
   carrying a figure is replaced in full. Section 4.
3. **Prediction 4 of the ambiguity pass is still untested.** It concerns how a comparator finding
   covering figures at different failure depths is graded. Reader B's finding covers five slides at
   one depth, so it still did not run. It is closer than it was.
4. **`check-docs.js` under-flags version drift in tables.** STATUS.md carried
   `frozen-2026-08-05c` in three places for a day while the checker reported clean, because the
   currency cues do not match a markdown table cell. Fixed the strings by hand this sprint, did not
   touch the checker.
5. **Everything queued by the ambiguity pass stays queued**: rule 1's second limb, the missing
   blocking rule for communication findings, the 2-of-5 finding cap against a 60 percent thesis, and
   the forty sub-checks. All are blocking-rule or doctrine work and all were out of scope here for
   the same reason.
