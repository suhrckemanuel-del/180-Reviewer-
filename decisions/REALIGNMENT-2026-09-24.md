# Realignment, 2026-09-24

Settled in a grilling session with the owner, four rounds. **This replaces the wayfinder map as the
working instrument.** The map is frozen, not abandoned — its destination was *"the decisions and
spec needed to put the reviewer in front of one pilot cohort"*, and by its own accounting every
decision it named is made.

## The goal, in the owner's words

> This is a reviewer, which then helps you and prompts you to think better. That's the goal. It's
> not doing the whole thing for you.

and, on what students should get out of it:

> It's not that there's a final truth. It's more that the things that they make, they have
> confidence in them, and they can have grounding evidence. Based on data they found.

**The same sentence is already on the project's own workshop slide**, written before any of this:
*"You will not find the right answer. You will pick one, and be able to say why."*
(`case-workshop-ai-training/Warmtewerk-Framework-Slide-v2.pptx`.)

## What triggered this

The owner's read: *"we've done a lot of work on logic, but it's not actually using anything, and
it's not helping much... we're doing so many checks and verifications."* Checked, and it holds:

- **The research reaches the shipped prompt in zero places.** A release is built from two files;
  neither cites, paraphrases or traces to anything in `research/`.
- **The rubric ships as ten bare names.** `01-rubric-v1.md` has anchors, four binary sub-checks per
  dimension, worked good/bad feedback pairs and per-dimension "abstain from" lists. None ship. The
  prompt orders the model to "score as binary sub-checks" and **never supplies them — the model
  invents forty of them, fresh, every run**, then computes a score off its own inventions.
- **v1 was closer to the goal than v2.** The old prompt carried a `RESEARCH FOUNDATION` block and
  required every finding to carry a principle tag from a named library. **v2 deleted both.** The
  research brief calls that tag *"the transfer mechanism — consultants carry a vocabulary of named
  standards."*
- **MECE: 0 occurrences across the 54 v2 documents. Issue tree: 0. 80/20: 0. Market sizing: 0.**
  The only real case framework in the repo is trapped in a PowerPoint.
- **The improvement loop is unbuilt.** `28-shared-corpus.md` says so in its own header. There is no
  `records/` directory and not one committed record. Across ~40 logged decisions, **none traces to
  a student's or a lead's feedback on a real review.**

## Decisions

| # | Decision | |
|---|---|---|
| 1 | The GitHub repo is **the improvement loop**, not just distribution | R1 |
| 2 | First real user is **the owner on a real deck, then the team** — not a pilot cohort | R1 |
| 3 | The reviewer **grounds in the research and applies frameworks critically**, Socratically | R1 |
| 4 | **Two-family verification only for failures a human cannot see** — the attempt gate, the key interlock, quote fidelity. Content and wording change freely | R2 |
| 5 | **Research/principle library now; frameworks built later** | R2 |
| 6 | Frameworks, when they exist, land in a **"how would you apply this"** field | R2 |
| 7 | **Principle library only (~270 tokens)**, not the full rubric (5,439) — the free-tier ceiling is still unmeasured | R3 |
| 8 | **Principle tag only where it genuinely applies**, not forced on every finding | R3 |
| 9 | The loop is **one append-only log file**, not a records folder | R3 |
| 10 | **GitHub for everyone now**, Drive only if someone actually struggles | R4 |
| 11 | **The map is frozen** | R4 |

## What ships, in order

**Batch 1 — make the prompt okay (a few hours, ~2 model runs).**

1. Add the **principle library** to paste 1, ~270 tokens, sourced to `10-source-register.md`:
   Pyramid Principle / Minto and the horizontal flow test, the student-consulting failure taxonomy,
   ERIP, deliberate practice.
2. **Principle tag on a finding where one genuinely applies**, omitted where none does. This is the
   teaching vocabulary a student carries into a conversation with a lead.
3. **Turn `Answer first:` into a thinking question**, never one answerable by looking something up.
4. **Distribution moves to GitHub.** `build-bundle.js` currently refuses to release without
   `DRIVE_FOLDER_URL`; that refusal and the student-facing message it prints both need rewriting for
   a repo link. **This is the only hard blocker in the 2026-09-24 audit and this removes it.**

**Batch 2 — get it out.** Cut a release, put it in the repo, use it on a real deck, append what was
wrong to the log. Then the team.

**Batch 3 — frameworks.** Transcribe `Warmtewerk-Framework-Slide-v2.pptx` into markdown
(MEASURE / COST / COVERAGE / RECOMMENDATION, twelve sub-questions, the NightOwl worked case), decide
when it is in scope, and wire it to the field from decision 6.

## What is dropped, explicitly

- **Ticket 27** (bring the artifact path level) — `PASTE-2C` is not in a release at all.
- **Ticket 28** (`Do this:` hands over pasteable text) — real, mild after today's hardening, one family.
- The **eight parked tickets** and the map's remaining machinery.

**Carried, as a watch item and not a blocker: [ticket 29](issues/29-the-interlock-false-alarmed-on-a-complete-bundle.md)** —
the truncation interlock refused a complete, byte-identical bundle once and reviewed it on re-run.
It sits on the one refusal path a user meets. *This is the session's assumption, not the owner's
instruction: he chose to freeze without commenting on it.*

## What we are knowingly accepting

- **The rubric stays fictional at runtime.** The model keeps inventing its own sub-checks until the
  free-tier ceiling is measured and the real ones can ship. This is decision 7's cost and it is the
  largest thing left on the table.
- **The bundle is ~12,000 tokens**, up from the 9,227 ticket 04 measured, against a ceiling nobody
  has measured. Ticket 11 would answer it and is not done.
- **The tool behaves measurably differently across model families** and the pilot cannot choose what
  students use.
- Everything on ticket 25's accepted-gaps list, unchanged.
