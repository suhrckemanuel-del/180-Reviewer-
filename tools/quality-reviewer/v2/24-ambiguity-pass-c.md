# 24. The blind ambiguity pass on `frozen-2026-08-05c`

Ran 2026-08-08. Method from [19-prompt-change-2026-08-05.md](19-prompt-change-2026-08-05.md)
section 2.5, the one that produced revision `b`. It had not been run since, so revision `c` had
never been tested by the method that produced it.

This pass does not measure whether the prompt produces better reviews. It measures whether the
prompt can be executed the same way twice. Result: **`frozen-2026-08-05d`**, sha
`fc39d6b6f928ed3a`, five patches against measured divergences, three defects left open on the
record.

## 1. What ran, and how the reviewers were kept blind

Two reviewers, each a fresh context with no history of this project, each given exactly one
file and told to read nothing else on the machine.

- **The case:** `real-13`, a packaging emissions calculator, final recommendation deck, 26
  slides, gold label R2. Chosen because its argument is entirely numeric (so the comparator
  test is exercised), its extraction notes flag figures across nine slides (so the damaged
  input path is exercised) and it carries a gold label, so a genuine execution difference can
  be told apart from two reviewers both being wrong.
- **The input:** `node run-reviews.js --emit-packs` produced the self-contained pack, which is
  section A plus the reference material the prompt refers to plus the case. Each reviewer got a
  byte-identical copy in its own directory. Neither could reach the other's.
- **The task:** produce the review, then name every instruction that was ambiguous to execute
  and say how it was resolved, what the alternative reading was and whether the two readings
  produce visibly different reviews.

**Blindness, specifically.** Neither reviewer was shown the standing critique, and neither
brief named, paraphrased or gestured at any suspected defect. The prompt asking for the log
described the target in general terms only ("a place where the instruction did not by itself
determine what you should do"), and it carried two explicit exclusions in both directions:
exclude wording that was merely clumsy, exclude judgments about the deck rather than about the
instruction. Neither reviewer read `eval-cases-real/labeling/`, any `*.gold.md`, any worksheet,
`STATUS.md`, `19-*.md` or the other's output. The prediction was opened only after both had
finished, and the divergence list below was assembled before it was read.

Reviewer B was interrupted by an unrelated spend limit after writing its review but before
writing its log, and was resumed from its own transcript rather than restarted, so the log is
the record of the execution that actually produced that review. Its isolation instruction was
repeated on resume.

**Both reviews are contract-valid.** `check-review-v2.js` passes both, quotes verbatim against
the deck. That matters: every divergence below is between two admissible reviews, not between a
good one and a broken one.

## 2. What the two reviewers named

Reviewer A named 18 instructions, reviewer B named 26. **Twelve were named by both.** Of those
twelve, eight were resolved identically and four diverged. Two further divergences are visible
in the artifacts but were named by only one reviewer.

| Instruction | A | B | |
|---|---|---|---|
| Rule 1's two-part contradiction test | named | named | same resolution |
| Extraction flag scope, figures or whole slides | named | named | same resolution |
| The comparator test's mechanical exclusion | named | named | same resolution |
| Rule 4 firing when the numbers are flagged | named | named | same resolution |
| Sub-checks: what they are, how many | named | named | same resolution |
| deliveryCritical count when a blocker fired | named | named | same resolution |
| Strengths on a Not ready deck | named | named | same resolution |
| Findings sort key | named | named | same resolution |
| **The reader-test fold rule** | named | named | **DIVERGED** |
| **Confidence Medium or Low** | named | named | **DIVERGED** |
| **Verbatim quoting: whitespace and joins** | named | named | **DIVERGED** |
| Wholly undetermined output fields | named | named | **diverged, presentational** |
| Scorecard result label threshold | named | not named | **DIVERGED in output** |
| Rule 1's second limb, one rule firing twice | not named | named | **DIVERGED in output** |

The eight convergences are the useful negative result. Both reviewers independently flagged the
sub-check construction as wholly undetermined ("essentially unreproducible across readers", B),
then both independently built four sub-checks per dimension and both landed on `diagnosticMean`
2.9 with eight of ten dimensions identical. Both marked four of five findings delivery-critical
where the text gives no rule at all. Both included exactly three strengths. Both put `team` on
every finding's owner. Those instructions read badly and execute consistently, which is exactly
the case section 2.6 warns against patching.

The headline agreement is larger than the disagreement. Both returned five findings and two
comments, both reached **Not ready for client review**, both built the readiness on the same
slide 16 versus slide 22 contradiction, and both suppressed the comparator test entirely.

## 3. The divergences

### 3.1 The fold rule, and what counts as a governing insight

> "This is ONE finding, never two. If the deliverable has no governing insight at all, fold the
> reader test into the governing-insight finding rather than raising both ... Raise it on its
> own only when the insight is present and the reader still cannot reach it, which is the
> buried-insight case."

Both reviewers looked at the same sentence on slide 24 and reached opposite conclusions.

**A:** "Not an insight. It is an instruction to persuade, it names no lever and it does not
answer which action the client takes first, so I treated the deck as having no governing
insight and folded the reader test into finding 2 as a single finding, graded major."

**B:** "I judged the insight present but buried: slide 16 carries the analytical governing
thought and slide 24 carries the client-facing one ('Persuade your clients by showing what
their contribution can be if they choose Client R13'), both in the back third. That made it the
buried-insight case, so I raised the reader test as its own finding (finding 3, 'Insight
arrives too late')."

**Effect on the artifacts.** A's review carries one finding where B's carries two. A's finding
2 is typed `communication` and covers both altitudes. B's finding 3 is a standalone reader-test
finding. Against a five-slot budget the displacement is real: B's fifth slot holds something A
carries only as a comment.

### 3.2 Confidence, Medium or Low

> "Confidence with partial input: Medium when every finding that sets readiness rests on text
> you can quote, Low when the readiness level itself could change with the missing material."

against

> "If the input lacks the client question, the artifact type or the evidence notes, do not
> proceed on a guess. Ask up to three specific questions and set confidence to Low."

Both clauses fired at once on this input. The text never orders them.

**A:** "Medium, giving priority to the first clause because the contradictory sentences
themselves survived extraction intact and are prose, not figures."

**B:** "Low. The missing-context clause is the most specific and it fired plainly: the input's
EVIDENCE AND SOURCE NOTES field is empty and no single client question is stated."

**Effect on the artifacts.** `readiness.confidence` and `scorecard.confidence` read Medium in
one review and Low in the other, on byte-identical input. A lead reading Low weights the whole
review differently.

### 3.3 Verbatim, when the extraction damaged the whitespace

> "Verbatim means character for character, with one exception: a line wrap in the pasted input
> counts as a single space, so a quote may join wrapped lines. Change no other character."

This diverged in two separate ways.

**The doubled space.** The input carries `CO2 conversion ratios  are either derived ...` with
two spaces. Both reviewers quoted that line.

**A:** "preserved the doubled space in the slide 10 quote exactly" and noted that normalising it
"is also a character change".

**B:** "I also normalized a genuine double space in 'CO2 conversion ratios  are' to a single
space, which the contract's whitespace-normalized validator accepts but which the 'change no
other character' sentence does not obviously license."

Two reviewers, one source string, opposite treatment, both accepted by the validator. This is
the cleanest divergence in the run because there is no judgment about the deck anywhere in it.

**What counts as a joinable wrap.** A restricted joining to lines that are one wrapped sentence
and quoted only body text, treating the pack's slide headers as scaffolding. B "treated
consecutive lines as joinable regardless of whether they were one sentence in the original
layout", which produced a seven-item agenda quote: "Introduction Inputs and Outputs Model
Description User-Model Interaction Results Recommendations Q&A". That string is a sentence
nobody wrote, and the validator accepts it, because its check normalises whitespace and the
seven items are consecutive lines in the input.

### 3.4 The scorecard result label

Named by A, not by B, and visible in both artifacts. Nothing in the prompt or the contract maps
`checksPassed` onto `pass`, `partial` and `fail`. A set dimension 10 at 3 of 4 to `pass`; B set
the same 3 of 4 to `partial`. `check-review-v2.js` computes an expected label and warned on A's
review. So this one has a right answer already sitting in the checker, and the prompt never said
so.

### 3.5 Rule 1's second limb, and one rule firing twice

Named by B, not by A, and the widest divergence in the output. B fired rule 1 twice, once on
the contradiction and once on "a recommendation that could mislead the client", reading the
publication of unsourced claims as reaching that limb. A raised one blocking issue. B's review
therefore shows two blocking issues and two criticals against A's one and one.

**This is not patched.** It sits inside a blocking rule, and the hard constraint on this sprint
forbids touching one. Recorded in section 6 and queued.

### 3.6 The undetermined output fields

Both named it, neither could do anything but invent. A emitted two critical tiles, B four.
Effort estimates, callouts and tags are equally free. Presentational, no effect on findings,
severity or readiness. Not patched, for the reason in section 6.

## 4. The prediction, opened after the fact

The standing critique named four candidate ambiguities in revision `c`. Read only after both
logs were complete and the divergence list above was assembled.

| # | Predicted defect | Result |
|---|---|---|
| 1 | The reader test has no operational procedure | **Cleared** |
| 2 | The fold rule hinges on an undefined "insight present or absent" call | **Confirmed** |
| 3 | The extraction-damage counterfactual has no criterion for "could have" | **Cleared** |
| 4 | One finding covers figures at different failure depths, no rule for which severity wins | **Not exercised** |

**One of four confirmed, two cleared, one never ran.**

**Prediction 1 is cleared.** Neither reviewer named the skim procedure as ambiguous. Both ran it
mechanically, both recorded the same limitation in `notAssessed` in near-identical words ("the
reader test was run on the titles, the order and the flow only"). The `c` patch that replaced
the unrunnable simulation with a mechanical procedure did its job. What both reviewers named
instead was the *fold* rule sitting one sentence later, which is prediction 2.

**Prediction 3 is cleared, and something else is behind it.** The `c` patch replaced the
counterfactual with a mechanical page test, and both reviewers applied it identically with zero
divergence. But both then reported the same consequence, unprompted: applied literally to this
deck, the test switched the comparator off for every figure in the deliverable. A: "the escape
hatch covers all of them." B: "there is no comparator finding in a review of a deck whose entire
argument is numeric." That is not an ambiguity, because it reproduces perfectly. It is a scope
collapse, and it is a more serious problem than the one that was predicted. Section 6.

**Prediction 4 never ran.** It concerns how a comparator finding is graded, and neither reviewer
raised a comparator finding, for the reason above. Not disconfirmed. Untested, and it stays
untested until the scope collapse is dealt with.

**Four unpredicted divergences materialised**: the confidence precedence, the whitespace rule,
the join rule and the scorecard label. Three of the four are in instructions nobody had
questioned, and the whitespace one is the sharpest finding in the run precisely because it has
no judgment in it at all.

## 5. The patches, and where two readers now agree

Five patches, each against a measured divergence. For each, the test that section 2.6 demands:
state the new decision boundary and why two readers land on the same side of it.

### Patch 1. The fold rule (divergence 3.1)

The present-or-absent call is now one test against one quotable sentence. The insight is present
only if a single sentence, on its own, both names what the client should do or choose and gives
the reason. Both halves, same sentence. Assembling the halves from different slides means
absent.

**New boundary:** does one quoted sentence contain both halves. **Why two readers land the same
side:** it is checkable against a string rather than against a concept, and it forces the
reviewer to produce the sentence. Run against the case that diverged: A's slide 24 sentence
names an action with no reason, so absent. B's slide 16 sentence states a fact with no action,
so absent. B's own log says it needed two slides to assemble the halves, which the rule now
names as the absent case outright. Both reviewers land on absent and fold, which is what A did
and what B's reasoning produces once the halves cannot be assembled across slides.

**Not a relocation:** the previous patch replaced a vague concept with a vaguer one. This
replaces a concept with an artifact the reviewer has to quote, so a disagreement is now visible
as two different quoted sentences rather than two different intuitions.

### Patch 2. Confidence precedence (divergence 3.2)

The two tests are now ordered. Check the input fields first: if CLIENT QUESTION, ARTIFACT TYPE
or EVIDENCE AND SOURCE NOTES is blank, says none, or says not stated, confidence is Low and the
quote test never runs.

**New boundary:** is a named field of the pasted input blank. **Why two readers land the same
side:** it is a presence check on three named fields of a template, not a judgment about
evidence quality. On this case the field is empty, so both reviewers reach Low, which is B's
answer. A's reasoning cannot survive the ordering because the ordering is explicit.

### Patch 3. Whitespace in quotes (divergence 3.3, first half)

Any run of whitespace in the input counts as one space in the quote. A line wrap, a tab and two
or more consecutive spaces are all one space. Change no character that is not whitespace.

**New boundary:** is the character whitespace. **Why two readers land the same side:** it is a
character-class test with nothing to weigh, and it now matches what
`check-review-v2.js` already does (`s.replace(/\s+/g, ' ')`). The instruction was the only
thing disagreeing with the checker. Both reviewers' quotes remain valid; only B's was licensed
before, and now both are.

### Patch 4. What may be joined (divergence 3.3, second half)

Join lines only to reassemble one sentence the extraction wrapped. Titles, agenda entries,
bullets, list entries and table cells are never joined into a single quote, even when the
extraction left them on consecutive lines. A finding needing several of them gives each its own
evidence entry with its own slide number.

**New boundary:** is the material on the next line a continuation of the same sentence or a
separate item. **Why two readers land the same side:** the rule names the failure case in a
closed list rather than asking for a judgment, and the case that diverged is in the list. B's
seven-item agenda quote is an agenda entry join, now forbidden outright, and the reader test now
has a stated way to use several titles without concatenating them. **Partial close, stated as
such:** prose wrapping was never divergent (both reviewers joined wrapped sentences the same
way), so this patch closes the measured divergence and does not pretend to have closed every
question about what a wrap is.

### Patch 5. The scorecard result label (divergence 3.4)

The label follows from the counts and is not a second judgment: `pass` when `checksPassed`
equals `checksTotal`, `fail` at 1 or 0, `partial` otherwise.

**New boundary:** arithmetic. **Why two readers land the same side:** there is nothing left to
decide, and this is the mapping `check-review-v2.js` has been computing all along. A's `pass` at
3 of 4 raised a validator warning; under the patch it is `partial`, which is B's answer and the
checker's.

**Constraint check.** No patch touches any of the five blocking rules, any readiness ceiling,
any of the three severity definitions or the noise budget. The reader test's severity sentences
are byte-identical across the change. Every patch changes how an instruction is executed, never
what it decides.

**Version.** `frozen-2026-08-05d`, sha `fc39d6b6f928ed3a`, 17,248 bytes. Revision `c` archived
verbatim at `eval-runs/prompt-archive/frozen-2026-08-05c.txt` and re-hashes to
`80983d7179eb950f`. Revision `b` (`54a6c835299cabb3`) was never archived when it was current and
its text is not recoverable, so the archive chain runs 07-26, 08-03, 08-05, 08-05c. Recorded
rather than fabricated. `node check-docs.js` clean, 47 documents.

## 6. Left open, and why

**1. The comparator test silently switched itself off on 100 percent of this deck's figures.**
Not an ambiguity: both reviewers executed the extraction gate identically and both suppressed
every comparator finding, on a deck whose whole argument is numeric. The gate as written keys
on any extraction note touching the page, and a note about *layout* damage ("figures
disconnected from their box-size labels") reads the same to it as a note about unreliable
*values*. This is the newer axis of the two-axis thesis disabling itself on damaged input, which
is most real input. **Not patched here** because no divergence was measured, and patching an
instruction the method did not flag is exactly the failure mode this sprint exists to avoid. It
needs its own sprint, and it should get one before prediction 4 can be tested at all.

**2. Rule 1's second limb, and whether one rule may fire twice.** Measured, wide (one blocking
issue against two, one critical against two) and **forbidden by this sprint's hard constraint**,
which bars touching a blocking rule. Queued. It belongs with the two items already queued for
the same reason: the missing blocking rule for communication findings, and the 2-of-5 finding
cap against a 60 percent thesis.

**3. The sub-check construction, and the undetermined output fields.** Both reviewers named the
sub-checks as wholly undetermined and B called `diagnosticMean` "essentially unreproducible",
yet both built four checks per dimension and both landed on 2.9. **No divergence was measured,
so under the method it is not a finding**, and the honest reading is that they converged on a
convention rather than on the text. Closing it means authoring forty sub-checks, which is new
doctrine and belongs to `01-rubric-v1.md`. The same logic covers the tile states, effort and
tags: section A carries no instruction there, so there is nothing to disambiguate and writing
one would be doctrine rather than a patch. All recorded, none patched.

## 7. What this run says about the method

It cost two reviewer runs and no API spend, and it separated three real execution defects from
eight instructions that read badly and execute fine. The 8-to-4 ratio is the argument for
running it rather than reading the prompt critically: a critic reading `c` predicted four
defects and got one, cleared two and could not have known the fourth never runs. Three of the
four defects that did materialise were in instructions nobody had questioned.

It remains the cheapest quality check available and it should stay routine after every prompt
edit. One refinement worth carrying forward: **compare the two reviews as artifacts, not only
the two self-reports.** Two of the six divergences here were named by one reviewer only and
would have been missed if the logs alone had been intersected.

---

## For STATUS.md

- **The prompt** was bumped to `frozen-2026-08-05d`, sha `fc39d6b6f928ed3a`, by this pass on 2026-08-08, and superseded the same day by `frozen-2026-08-05e` ([25-comparator-gate.md](25-comparator-gate.md)). STATUS.md lines 15, 79 and 141 still said `frozen-2026-08-05c` / `80983d7179eb950f` at the time of writing and needed updating (check-docs under-flagged them; the checker was otherwise clean).
- **The blind ambiguity pass ran on `c` (2026-08-08, `24-ambiguity-pass-c.md`).** Two blind reviewers on real-13, both contract-valid, both Not ready. Twelve instructions named by both, eight resolved identically, four diverged.
- **The standing critique scored 1 of 4.** The fold rule confirmed, the reader-test procedure and the extraction counterfactual cleared, the fourth never exercised. Four unpredicted divergences found instead: confidence precedence, verbatim whitespace, quote joining, scorecard label.
- **Five patches applied**, each with a stated decision boundary. No blocking rule, ceiling, severity definition or noise budget touched, so readiness movement in a future run is still noise rather than effect.
- **New open defect, and it is serious:** the comparator test suppressed itself on every figure in the deck via the extraction gate, reproducibly. It disables the newer thesis axis on damaged input and it needs its own sprint. Rule 1's second limb (one blocking issue against two) is measured but out of scope here and joins the queue.
