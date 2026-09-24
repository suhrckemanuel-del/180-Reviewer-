# The 180DC Deliverable Reviewer

A reviewer that makes a consultant think harder about their own work. **It does not write the work,
and it does not grade it.**

> You will not find the right answer. You will pick one, and be able to say why.
>
> — 180 Degrees Consulting Delft-Rotterdam, the decision-case framework slide

---

## What this is for

180 Degrees Consulting is student-run. There are no seniors, turnover is total inside three years,
and the clients and boards are real. The realistic alternative to this tool is **no substantive
review at all** — not a better review.

So the bar is not "is the feedback correct". It is:

**A consultant finishes with work they have confidence in, grounded in evidence they went and
found.** Not a final truth. A defensible choice.

Everything in this repo is downstream of that sentence. When a decision here looks strange, it is
usually because it was made to protect that and not something else. [VISION.md](VISION.md) has the
long version and the evidence behind each choice.

## What it actually is

There is no app, no login and no website. It is **a prompt, a context pack and your deliverable**,
pasted into whatever chat model you already have.

**As a consultant:**

> **No release has been cut yet.** `build-bundle.js --release` refuses until a distribution URL is
> set, and that decision — a GitHub link rather than a Google Drive folder — was only taken on
> 2026-09-24 and is not built. Until it is, the usable copies live in
> [`tools/quality-reviewer/v2/TEST-KIT/`](tools/quality-reviewer/v2/TEST-KIT/) and carry test keys
> rather than release keys. The steps below are the real ones; only the folder changes.

1. Open `release/` and take the three files.
2. Read `COVER-SHEET.md`. One page.
3. Open a new chat. Paste **`REVIEWER-SETUP.txt` as one message**.
4. Fill in `TEAM-INPUT-TEMPLATE.txt` — the client question, the audience, your constraints, your
   sources, then your deck as text — and paste it.
5. **Type your own read first**: what you think the weakest part is, two or three sentences.
   *The reviewer refuses to review until you do.* That is deliberate — see
   [VISION.md](VISION.md#attempt-first).
6. **Check the first line reads exactly `KEYS: <part1>/<part2>`**, against the cover sheet. If it
   does not, your chat silently dropped part of the paste. Start a new chat and paste again.
7. Read the findings. Every one carries a verbatim quote from your own work and where it is. **If
   you cannot find a quote in your own deck, that finding is wrong — drop it.** Nothing is checking
   this but you.

**As a team lead:** the same, with `MODE: lead` — denser, no typed attempt required, no coaching.

## What it deliberately will not do

| It will not | Because |
|---|---|
| Give a grade, score or readiness level | The same deliverable was given **two different levels on byte-identical input**. That half is not produced at all. |
| Write your slide, your title or your wording | If the sentence arrives finished, no thinking happened. Tested three ways over 26 runs; see [decisions/parked-features.md](decisions/parked-features.md). |
| Approve anything | A named human signs off on client work. That rule does not move. |
| Review before you have tried | The generation effect. You learn from the gap between your read and its read, and there is no gap if you never read it. |

## How it gets better

This repo **is** the improvement loop. There is no separate system.

1. Use it on a real deliverable.
2. When something is wrong — a finding that is noise, a question that lands flat, a quote that is
   not in the deck — append it to **[IMPROVEMENT-LOG.md](IMPROVEMENT-LOG.md)**. One line is enough.
3. A change to the prompt references the log entry that prompted it.

That is the whole process, on purpose. An earlier version of this project produced seventeen
resolved decisions and, for a long stretch, **zero changes a user would notice**. The log exists so
that real use, not internal reasoning, is what moves the prompt.

**Verification, when you change something:** re-run on two model families **only** for failures a
human cannot see — the attempt gate, the bundle-key interlock, quote fidelity. Wording and content
you can simply read and judge. See [decisions/REALIGNMENT-2026-09-24.md](decisions/REALIGNMENT-2026-09-24.md),
decision 4.

## What is in here

| | |
|---|---|
| `release/` | What a consultant copies, once a release is cut. **Generated — never edit by hand.** Does not exist yet. |
| [`tools/quality-reviewer/v2/TEST-KIT/`](tools/quality-reviewer/v2/TEST-KIT/) | The same three files with test keys. What to use today. |
| [`tools/quality-reviewer/v2/`](tools/quality-reviewer/v2/) | The system. `04-prompt-templates.md` and `CHAT-CONTEXT.md` are the only two files that ship; `build-bundle.js` generates the release from them. |
| [`tools/quality-reviewer/v2/01-rubric-v1.md`](tools/quality-reviewer/v2/01-rubric-v1.md) | The ten dimensions, with anchors, sub-checks and worked good/bad feedback. |
| [`tools/quality-reviewer/v2/10-source-register.md`](tools/quality-reviewer/v2/10-source-register.md) | Every claim the rubric rests on, with its limitation and which dimension it grounds. |
| [`research/`](research/) | The evidence base: deliverable quality, student failure modes, professional-services QA, training and transfer, plus a McKinsey reading base. |
| [`frameworks/`](frameworks/) | Case frameworks the reviewer should be able to apply. |
| [`decisions/`](decisions/) | Why it is the way it is — the map, the tickets, the audits and the measurements. Read this before changing anything load-bearing. |

## Building a release

```bash
cd tools/quality-reviewer/v2 && node build-bundle.js --check
```

`--check` verifies the generated files still match their sources. `--release` cuts a new one with a
fresh key pair and registers it. Two hand-maintained copies of this prompt have already gone stale
undetected, which is why it is generated rather than copied.

## Honest status

**Works and is measured:** quote-or-abstain held across 55 quotes on two model families with zero
fabrications, even with the system prompt entirely absent. The attempt gate refuses and cannot be
argued past. The bundle-key interlock catches a silently truncated paste.

**Known broken or unmeasured, and carried deliberately:**

- **No release exists.** The one hard blocker, and it is a decision about where consultants get the
  files, not a bug.

- The prompt tells the model to score the ten dimensions "as binary sub-checks" and **never supplies
  the sub-checks** — so it invents them each run. The real ones are in `01-rubric-v1.md` and do not
  fit the token budget yet.
- **The free-tier ceiling has never been measured.** The bundle is ~12,000 tokens and nobody knows
  where the cliff is.
- **The path that ships has never been scored.** Every measurement on record ran a different path.
- The bundle-key interlock **false-alarmed once on a complete bundle** — see
  [decisions/issues/29-the-interlock-false-alarmed-on-a-complete-bundle.md](decisions/issues/29-the-interlock-false-alarmed-on-a-complete-bundle.md).
- The tool behaves **measurably differently on different model families**, and a consultant brings
  their own.

The full list is in [decisions/AUDIT-2026-09-24.md](decisions/AUDIT-2026-09-24.md).

---

**Client confidentiality:** real deliverables, decks and extracted client text never enter this
repo. `.gitignore` enforces it. Anonymise before committing any example.
