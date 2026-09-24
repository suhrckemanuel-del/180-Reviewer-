# Paste-ready build prompt: the comparator gate (Track C — the last build before the pilot)

**Run on Opus at high effort. Not max.** The trap in this sprint is subtle enough to need real
reasoning — the obvious fix destroys a property that was just measured and paid for — but the
characteristic failure mode here is *scope expansion*, and maximum effort on a bounded fix
reliably produces more surface area, not less. High is the right setting. A fast model will
rewrite the instruction, report that it reads better, and never check whether it fires.

Paste everything below the line into a fresh chat. It is self-contained.

---

Working in `c:\Users\User\Desktop\180dc-ai`, branch `wip/case-study-gallery-private-content`.
Everything lives under `tools/quality-reviewer/v2/`. **Fix one thing and prove it fires. Write
no new strategy documents.**

## Read this part first, because it changes how you should scope everything below

**This is the last build.** After it, the tool goes to real project leads on real deliverables
and the evidence comes from them, not from the eval harness. The project has spent three weeks
on measurement infrastructure — a re-fitted scorer, an LLM judge, an adjudication-independence
checker — and in that time zero project leads have used the tool and reported back. That was the
wrong ratio and it has been called. Nothing in this sprint should extend it.

So: if you find something else worth fixing, **write it down in the handover section and leave
it alone.** "While I was in there" is the specific behaviour this instruction exists to prevent.

## What the product is, so you can check your own work against it

An AI tool that reviews a team's draft consulting deliverable and tells a project lead how close
to client-ready it is and what to fix. It advises; a named human decides.

Its quality thesis comes from an ex-McKinsey consultant and is the reason the prompt looks the
way it does: **roughly 60% of a consultant's value is communication clarity — can a fast,
skimming reader get the point — and most of the rest is interrogating the numbers: compared to
what, so is that good, and if not what is it a symptom of.** Two axes. The prompt was rewritten
on 2026-08-05 to implement both.

**Right now it implements one.** That is what you are fixing, and the test of your work is not
whether the instruction reads better — it is whether a lead reading a review of a numeric deck
sees its numbers interrogated.

## The defect

From `24-ambiguity-pass-c.md`, the blind two-reviewer ambiguity pass:

> The comparator test silently switched itself off on every figure in the deck. Both reviewers
> executed the gate identically. The gate keys on any extraction note touching a page, and a
> note about layout damage reads to it exactly like a note about unreliable values.

Read that document's section on it in full before touching anything, then read the gate itself at
`04-prompt-templates.md` step 5, around line 97.

This is **not an ambiguity**. Two independent reviewers applied it the same way. It is an
instruction that is unambiguous and **inert** — it fires zero times on exactly the decks it
exists for, because a deck whose argument is numeric is a deck likely to carry extraction notes.

## The property you must not destroy

Track A predicted four defects in this prompt by reading it and scored **1 of 4**. One of the
three misses is directly relevant: the extraction-damage carve-out was predicted to cause
divergence between reviewers, and it was measured as **cleared — both reviewers applied the
mechanical test identically.**

That determinism is real, it was expensive to establish, and it is worth more than the gate's
current breadth. **The obvious fix destroys it.** Any patch of the form "suppress the comparator
finding when the extraction damage plausibly affects the values" or "use judgement about whether
the flagged material could have carried the comparator" restores the axis by making the gate a
judgement call, and two readers will then apply it differently. That is rejected in advance —
do not propose it.

**Your patch must be mechanical: a test two competent readers apply identically without
judgement.** The distinction you are drawing — a note about layout or formatting damage versus a
note about values being unreliable — is a property of the extraction note itself, not of the
figure, not of a counterfactual, and not of the reader's opinion. That is where a mechanical
boundary is available. Find it, state it, and state why two readers land on the same side.

If you conclude no mechanical boundary exists, **say so and stop.** Recording that honestly is a
better outcome than shipping a judgement call, and the project has twice been well served by a
sprint that returned a negative result.

## Hard constraints

**Touch no blocking rule, no ceiling, no severity definition and no noise budget.** Identical to
the constraint Track A worked under, for the same reason: those move readiness, readiness is
known not to repeat, and nothing downstream is currently measuring it. The comparator finding's
severity rules at `04-prompt-templates.md` lines 100-101 stay byte-identical.

Do not touch the reader test. Do not "improve" adjacent instructions.

## The verification, which is the actual deliverable

A wording change with no behavioural evidence is not a fix, and this sprint is judged on the
evidence, not the patch. Required, in this order:

**1. Establish the before number.** On the real case Track A used, under the current prompt, the
comparator test fires **zero** times. Confirm that rather than assuming it.

**2. Show it fires after.** Run the patched prompt on the same case, blind, under the blindness
rules in `05-eval-harness.md` — the reviewing agent never sees `eval-cases-real/labeling/`, any
`*.gold.md`, any worksheet, or another case's review. Count comparator findings. Report before
and after as a count.

**3. Show the findings are legitimate, not just numerous.** For each comparator finding the
patched prompt now raises, confirm the figure genuinely lacks a comparator in the deliverable
rather than having one that sat in extraction-damaged material. A gate that fires by going blind
to damaged input is worse than one that never fires, because it produces confident wrong
findings a lead will act on. If you cannot tell, that is a finding about the patch.

**4. Re-check determinism on the patched instruction specifically.** Two blind readers, fresh
context, asked how they applied the gate. If they diverge, **the patch traded determinism for
coverage and must be rejected** — report that and revert rather than shipping it. This is the
step most likely to be skipped and it is the one that protects what Track A bought.

**5. Sanity-check against the thesis.** Read the resulting review as a project lead would. Are
the numbers actually interrogated — compared to what, is that good, what is it a symptom of — or
did you produce five mechanical "no comparator" flags that no lead would act on? Restraint is a
product value here, not a limitation; the deep-mode noise budget is 5 findings total and lens I
prunes. A gate that fires correctly but floods is a different failure, and you should say so
plainly if that is what you see.

## Definition of done

- `04-prompt-templates.md` patched, bumped to `frozen-2026-08-05e`, `d` archived under
  `eval-runs/prompt-archive/` and re-hashing to `fc39d6b6f928ed3a`.
- `25-comparator-gate.md`: the mechanical boundary and why two readers land on the same side of
  it, before/after counts, the legitimacy check per finding, the determinism re-check, and the
  read-as-a-lead judgement. Verdict in the first three lines: **does the axis fire, yes or no.**
- `node check-docs.js` clean.
- `STATUS.md` updated — Track B has finished, so you own this file now. The prompt row, and
  "What happens next", which should end with the pilot, not with another build.
- A short handover block listing anything you found and deliberately did not fix.

## What would make this sprint a failure

Reporting a reworded instruction with no before/after count. Restoring the axis by making the
gate a judgement call. Skipping the determinism re-check because the patch "obviously" reads the
same to everyone. Touching a blocking rule. Or fixing something else you noticed on the way —
the next thing this project does is put the tool in front of real leads, and every extra change
is one more thing that could be the reason a pilot review looks wrong.
