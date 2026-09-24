# Paste-ready build prompt: the three-paste path and the calibration context file

**Run on Opus at high effort.** Two of the three constraints below are safety constraints on an
artifact that will be pasted into other companies' AI tools by people this project will never
meet. A fast model will produce a nice-looking context file that leaks a client and strips every
control. Do not use one.

Paste everything below the line into a fresh chat. It is self-contained.

---

Working in `c:\Users\User\Desktop\180dc-ai`, branch `wip/case-study-gallery-private-content`.
Everything lives under `tools/quality-reviewer/v2/`. **Build the two artifacts and prove the
constraints hold. Write no new strategy documents.**

## What you are building and why

180 Degrees Consulting branches are student teams working for non-profits with no budget. The
reviewer currently reaches a team through a Claude Project plus a hosted renderer at
180dc-reviewer.pages.dev — the JSON goes into a Triage Desk that enforces a quote check, strips
readiness out of student payloads, and produces an override record. That path is good and it
stays.

**It also excludes everyone without that setup, and that is the problem you are solving.**

Read this before anything else, because it overrides any instinct to scope the work down. **The
three-paste path is not a free tier of a paid product. It is the product.** 180DC consultants are
students; many have no chargeable budget and no paid AI account, and the tool has to reach all of
them or it is not a tool for this organisation. The renderer path is the exception for people who
happen to have the setup, not the main road.

Two consequences that are not negotiable in this sprint. **You may not solve a hard constraint by
restricting who gets the tool** — narrowing to leads, to paid accounts, or to supervised use is
out of bounds as a solution, and if you find yourself proposing it you have mis-solved the
problem. And the tool has not yet produced the results that would justify asking anyone to pay
for it or absorb its cost, so nothing you design may assume budget.

The owner's requirement is a path that works with three pastes into any chat window, free tier,
no Project, no login, no renderer:

1. **The prompt** — `04-prompt-templates.md` section A.
2. **A calibration context file** — new, and the main thing you are writing. Distilled from the
   evidence this project has collected so the reviewer judges like an experienced lead rather
   than from the instruction text alone.
3. **The project brief and the deliverable** — the section B team input template, filled in.

Output has to land as readable chat prose that carries the same value a lead gets from the
renderer, because these users will never see the renderer.

## Read first, in this order

- `04-prompt-templates.md` sections A, B and E. E is the current calibration knowledge and is one
  synthetic worked case — you are replacing a pointer with a document.
- `eval-cases-real/labeling/worksheet-template.md`, the gold worksheet structure. **Sections
  "Acceptable AI feedback", "Unacceptable AI feedback", "False positives to avoid", "False
  negatives to catch" and "Honest uncertainty" are your raw material.** The owner's standing
  correction, 2026-08-02: the golds are not an answer key to optimise against, they show how a
  human team lead reasons, and those five sections are the valuable part, not the readiness level.
- `20-running-it-free.md`, all of it, section 4 especially.
- `22-trust-boundary.md` sections 1 and 2, the controls you are about to step outside of.
- `18-evidence-base.md` sections A and C.
- `01-rubric-v1.md`, and `25-comparator-gate.md` plus `24-ambiguity-pass-c.md` for what the last
  two sprints established about how the prompt actually behaves.

## Constraint 1: this is the most widely distributed artifact this project will ever produce

The context file gets pasted into ChatGPT, Gemini, Copilot and whatever else, by students, at
other branches, forever. Assume it ends up public.

The gold worksheets it is distilled from are **gitignored because they name findings on real
client deliverables.** So:

**The context file contains no client-identifying content of any kind.** No client names, no
sector-plus-geography combinations that identify one, no verbatim quotes from any real
deliverable, no case IDs, no paraphrase close enough to recover the original. You are extracting
**patterns** — "a savings percentage presented with no comparison to current spend" — not
instances.

Write it so it can be committed to a public repo, then verify that: re-read your own draft
adversarially and ask whether a person holding the 14 real decks could match any passage to one
of them. If yes, abstract further. State in the document itself that it is deliberately free of
client material and why.

## Constraint 2: chat mode escapes every control, so the controls must move into the output

This is the part most likely to be got wrong, and it is the one that matters.

In the renderer, three things are enforced by code: nothing leaves the tab until every quote is
machine-checked against the deck; readiness and blocking-issue ceilings are stripped out of any
student-facing payload, not just hidden; and a kill switch can withdraw the tool. **In a chat
window, none of that exists.** No quote check, no redaction, no kill switch, no record.

You cannot enforce. You can only construct. So the chat-native output format must achieve by
construction what the renderer achieves by enforcement:

- **Readiness: the chat path emits no AI readiness level at all.** Do not build a lead-only
  block, a delimiter or a "do not forward" instruction — every one of those assumes a lead
  standing between the model and the student, and on this path there is nobody in between. The
  student is the operator. So the control cannot be redaction; it has to be non-production.

  This is the project's own conclusion applied rather than a concession. A4: readiness returns
  R0 and R2 on byte-identical input. A1 and A2: the findings have never missed a problem a human
  rated blocking, and no fabricated quote has ever survived. `STATUS.md` already instructs every
  lead to work from the findings and never pass on the grade. The unreliable output is therefore
  simply not produced here, and nothing is left to leak. The human still makes a readiness call —
  their own, prompted for in the paste-back block, which is the only readiness the record was
  ever meant to carry as judgement.

  Say plainly in the output why no grade is given: the findings are checkable and the grade is
  not repeatable. A user who feels the absence should understand it as honesty, not a missing
  feature. If you conclude some ceiling-shaped signal is genuinely needed, it must be one that
  survives being read by anyone, and you must say what makes it repeatable.
- **Quotes must be self-checkable.** Every finding carries its verbatim quote and location so a
  lead can confirm it against the deck by eye in seconds. Say plainly, in the output, that a
  quote that cannot be found in the deliverable means the finding is discarded — the human is
  now the quote check.
- **The grade is not the product.** `STATUS.md` is unambiguous: work from the findings, never
  pass on the AI's grade — the findings have never missed a blocking problem, the readiness
  level has returned two different answers on identical input. That warning is currently a
  document nobody in chat mode will read. It belongs in the output.
- **The client prohibition is absolute** and survives into this path unchanged: no deliverable
  goes to a client on this review alone, at any level of measured performance.

Update `22-trust-boundary.md` with a row for this audience and an honest "today" cell. The
existing second row's bar — "no readiness level in the payload a student receives" — is met on
this path by construction rather than by enforcement, since no level is produced at all. Say that
in the cell, and say what remains unenforceable: nobody can stop a user pasting the prompt into a
weak model, and nobody can verify a quote on their behalf. Write those as limits of the path, not
as reasons to withhold it.

## Constraint 3: a review nobody records is invisible to the evidence base

The pilot answers one question — whether communication findings are the ones leads actually keep
— and it answers it from override records: `decisions[]` joined to `ai.findings[].issueType`.
Chat mode produces prose and therefore produces nothing.

If most teams end up on the three-paste path, the evidence base stops growing exactly when it
starts mattering. So the chat output must end with **a short structured block a lead can paste
back** — findings with their `issueType`, what was kept, cut or turned into a question, the
lead's own readiness call, and whether it was faster than doing it by hand. Small enough that a
busy lead actually returns it. Match the field names in `buildRecord()` in `index.html` around
line 1754 so both paths feed one dataset.

## Constraint 4: be honest about the model

`20-running-it-free.md` section 4: every number this project has — including 0% blocking rules
missed and no fabricated quote surviving — was measured on Claude Opus 5. Run the same prompt on
a small free model and none of those numbers describe what the student is holding. Nobody has
looked.

The context file states this plainly, near the top, in the user's own interest. It does not
discourage free use — affordable access is the point of the project — it tells them which
properties are established and which are hopes. Do not soften this into marketing, and do not
turn it into a reason to prefer the paid path. The honest framing is that a consultant on a free
model gets a reviewer whose behaviour nobody has measured, which is still better than the
no-review baseline every one of them has today, and that measuring it is a thing this project
wants to do rather than a warning to walk away.

If a cheap check is available — naming which free models have been tried, or a self-test the
reviewer can run on itself — propose it in the handover. Do not build it in this sprint.

## What "the same value" means concretely

The renderer gives a lead: a verdict with score, effort and confidence; the worst criteria named;
findings with quote and location; keep/question/cut triage; their own readiness call; and a note
back to the team that writes itself. The chat output should carry the equivalent as prose in a
form a lead can act on in one read, and can forward the team-facing part of directly.

Restraint is a product value, not a limitation — the deep noise budget is five findings and lens
I prunes. A chat output that lists everything it noticed has failed even if every item is true.

## Definition of done

- The calibration context file, as a single pasteable document, at a path a non-technical lead
  can be pointed to.
- `04-prompt-templates.md` section E updated to point at it; a chat-native output section added
  **without touching section A's synthesis protocol, blocking rules, ceilings, severity
  definitions or noise budget.** If the output format cannot be added without touching those,
  stop and report why.
- Prompt version bumped, prior archived under `eval-runs/prompt-archive/`, re-hashing confirmed.
- `26-chat-native.md`: the design, the three constraints and how each is met, the
  confidentiality self-audit, and anything you could not solve.
- `22-trust-boundary.md` carries the new audience row.
- **Demonstrate it once, end to end**, on a synthetic case — not a real one, since the output of
  this test is going in a document. Show the actual chat output. Confirm the lead-only block is
  separable, the quotes are checkable, and the paste-back block parses.
- `node check-docs.js` clean.

## What would make this a failure

A context file with a recoverable client in it. Emitting an AI readiness level anywhere on this
path. Solving any constraint by narrowing who may use the tool. Quietly dropping the client
prohibition or the work-from-the-findings warning because they read as friction. Expanding
section A's protocol while adding an output format. Or a "free tier" story that implies the
evidence transfers to models it was never measured on.

The test to hold yourself to: **a consultant with no budget, no paid AI account and no lead
supervising them can open a free chat window, paste three things, and get a review they can act
on and check.** If your design does not deliver that, it has not met the brief.
