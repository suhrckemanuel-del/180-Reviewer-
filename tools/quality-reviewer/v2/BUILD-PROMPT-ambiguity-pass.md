# Paste-ready build prompt: the blind ambiguity pass on `frozen-2026-08-05c` (Track A)

**Run on Opus.** The work is judging whether an instruction can be executed the same way twice
by two competent readers. A fast model will agree with whatever it is shown, which is the one
failure mode that makes this sprint worthless.

**Runs in parallel with Track B** (`BUILD-PROMPT-mc-match-3.md`). File ownership is at the
bottom. **You do not own `STATUS.md`.**

Paste everything below the line into a fresh chat. It is self-contained.

---

Working in `c:\Users\User\Desktop\180dc-ai`, branch `idea/reviewer-v2`. Everything lives under
`tools/quality-reviewer/v2/`. **Run the method and report. Write no new strategy documents.**

## Why this can run now, when nothing else can

Every other improvement to the reviewer is blocked on `mc-match-3`, because the scorer that
would detect an improvement is 3 points better than ignoring its input. This sprint is the
exception, and the reason is worth understanding before you start.

It does not measure whether the prompt produces **better** reviews. It measures whether the
prompt can be **executed the same way twice**. That needs no gold labels, no matcher and no
scorer — it needs two competent readers and a disagreement count. A frozen prompt that two
readers execute differently is not frozen in any sense that matters, and it produces run-to-run
variance that the project would otherwise spend months attributing to the model.

This method has already worked once here. `19-prompt-change-2026-08-05.md` section 2.5: the
prompt was handed to two blind reviewers on a real case and they were asked which instructions
were ambiguous **to execute**. They independently named the same four. All four were patched
into revision `b`. `STATUS.md` calls it "the cheapest quality check available" and says it
"should be routine after every prompt edit." It has not been run since. Revision `c` exists
precisely because a later critic showed three of the four `b` patches replaced a coarse
ambiguity with a finer one — so `c` has never been tested by the method that produced `b`.

## Read first, in this order

- `19-prompt-change-2026-08-05.md` sections 2.5 and 2.6. **2.6 is the important one:** it is the
  record of the `b` patches narrowing ambiguity rather than closing it, and it tells you what
  a real finding looks like versus a cosmetic one.
- `04-prompt-templates.md` section A, the prompt itself
- `STATUS.md` lines 96-106, the method and the open design tension

## The method, and the one rule that makes it valid

Two independent reviewers, each in a **fresh context**, each given the prompt and one real case,
each asked to produce a review and then to name every instruction that was ambiguous to execute
and say how they resolved it. Then compare.

**The rule: neither reviewer may be shown the suspected defects.** There is a standing critique
naming four candidate ambiguities in revision `c` — the reader test having no operational
procedure, the fold rule hinging on an undefined "insight present or absent" call, the
extraction-damage counterfactual with no criterion for "could have", and one finding covering
figures at different failure depths with no rule for which severity wins.

**Do not put that list in front of either reviewer.** Do not paraphrase it, do not use it to
frame the question, do not check their output against it while they are still running. A
reviewer shown the answer will find the answer. The critique is a **prediction**, and the point
of the sprint is to test it — including the possibility that all four are theoretical and the
real divergences are somewhere nobody looked. Open the prediction only after both reviewers have
finished, and report the hit rate honestly. **"Two of the four predicted defects did not
materialise, and two unpredicted ones did"** is a better result than four confirmations, because
it is the one that could only have come from actually running the test.

Use a real case that has a gold label so a genuine execution difference can be told apart from
two reviewers both being wrong. Blindness rules from `05-eval-harness.md` apply in full: a
reviewing agent must never see `eval-cases-real/labeling/`, any `*.gold.md`, any worksheet, or
the other reviewer's output.

## What counts as a finding, and what does not

A finding is: **two competent readers executed this instruction differently, and here is the
divergence.** Quote both resolutions.

Not a finding: an instruction one reviewer found awkward, wordy or improvable. The prompt is
not being edited for style. If both reviewers resolved something the same way, it is not
ambiguous, however ugly it reads — say so and move on. Expect to clear some of the four
predictions this way.

## Then patch, but only what you measured

For each confirmed divergence, write the patch that closes it, and apply the lesson of section
2.6: **check that the patch does not just relocate the ambiguity one level finer.** State, for
each patch, what the new decision boundary is and why two readers would land on the same side
of it. If you cannot state that, the patch is not ready — record the divergence and leave the
instruction alone. An honest open defect beats a fourth round of narrowing.

Bump to `frozen-2026-08-05d`, archive the prior verbatim under `eval-runs/prompt-archive/`,
confirm it re-hashes.

## The hard constraint

**Touch no blocking rule, no ceiling, no severity definition and no noise budget.** Those move
readiness, readiness is already known not to repeat (A4), and the instrument that would detect
the difference is the one Track B is rebuilding. This sprint changes only how instructions are
executed, never what they decide. The two items that *do* need those levers — the missing
blocking rule for communication findings, and the 2-of-5 finding cap against a 60% thesis — are
deliberately out of scope and stay queued.

## Definition of done

- `24-ambiguity-pass-c.md`: the two reviewers' named ambiguities, which overlapped, the
  divergences with both resolutions quoted, the prediction hit rate stated plainly, each patch
  with its new decision boundary, and anything left open and why.
- `04-prompt-templates.md` patched, version and sha bumped, prior archived and re-hashing.
- A five-line block at the end of `24-*.md` headed **"For STATUS.md"**, ready to paste. Track B
  owns `STATUS.md` this week and will merge it. Do not edit that file.
- `node check-docs.js` clean.

## What would make this sprint a failure

Showing either reviewer the predicted defect list. Reporting four confirmations without saying
how the reviewers were kept blind. Editing the prompt for style under cover of the method.
Touching a blocking rule. Or producing a fifth round of narrowing and calling the ambiguity
closed — if a patch cannot state where two readers would now agree, it has not closed anything.

## File ownership, because Track B is running at the same time

**Yours:** `04-prompt-templates.md`, `24-ambiguity-pass-c.md`, `eval-runs/prompt-archive/`.
**Not yours, do not edit:** `STATUS.md`, `score-review.js`, `rescore.js`, `scorecard.js`,
`01-rubric-v1.md`, `23-*.md`. Track B owns those.
