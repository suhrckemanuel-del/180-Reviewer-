# The 180DC Deliverable Reviewer

> **Current scope and issue plan:** see [PROJECT-PLAN-2026-09-30.md](PROJECT-PLAN-2026-09-30.md).
> It supersedes the historical decision map and prior realignment as the working plan.
> **Current progress and split-design acceptance:** [CURRENT-MAP.md](CURRENT-MAP.md).

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

The review itself runs in a chat model. The intended student flow is to receive the complete
review first, then use the same chat as a plain-language coach to reason through what a finding
means and how they might address it with evidence. An unaided first read is optional in normal
use and is collected before feedback only when measuring learning. An optional HTML view is
implemented locally under issue #3 as a faithful rendering of the same review; coaching continues in chat.
The old hosted review desk is not the current release path.

**Start supervised testing:** [Start here](tools/quality-reviewer/v2/releases/1006-NCEECNQ/START-HERE.md).
The [candidate PR](https://github.com/suhrckemanuel-del/180-Reviewer-/pull/6) is open for owner review.
Choose STUDENT-SETUP.txt / STUDENT-INPUT-TEMPLATE.txt for complete feedback and optional
same-chat reasoning, or LEAD-SETUP.txt / LEAD-INPUT-TEMPLATE.txt for concise evidence checks
and human keep/ask/cut decisions. Optional HTML uses student-review.html or lead-review.html
with separate templates, local notes and exports. The candidate remains subject to owner review.

The old approved checkpoint is historical and does not approve this split. Software checks
use an existing private saved review with labelled provenance; no new prompt-performance,
learning-gain, account-capacity or pilot-acceptance claim follows. Consultant access and
human workflow checks remain. A named human signs off before client use.

## What it deliberately will not do

| It will not | Because |
|---|---|
| Give a grade, score or readiness level | The same deliverable was given **two different levels on byte-identical input**. That half is not produced at all. |
| Approve anything | A named human signs off on client work. That rule does not move. |
| Require a solo first read in routine use | It is a learning-measurement step, not an access gate. |

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
| `tools/quality-reviewer/v2/releases/` | Immutable versioned consultant bundles, once generated. Generation alone does not publish or approve a pilot. |
| [`tools/quality-reviewer/v2/TEST-KIT/`](tools/quality-reviewer/v2/TEST-KIT/) | Generated student/lead starting files and Start here guide with test keys. |
| [`tools/quality-reviewer/v2/`](tools/quality-reviewer/v2/) | Prompt/context sources, bundle generator, local intake and deterministic review view. |
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

**Historical measurements:** quote-or-abstain held across 55 quotes on two model families in
older tests. Those results do not validate the current candidate. The former attempt gate is
removed from ordinary use. The bundle-key interlock also has a recorded false alarm.

**Known broken or unmeasured, and carried deliberately:**

- **No accepted consultant release exists.** Registered split candidate `1006-NCEECNQ` is
  prepared for PR review and supervised testing. Generation and publication do not establish
  owner approval, learning gains or pilot acceptance.

- Candidate 2e removes unsupported binary sub-check scoring and uses the ten dimensions
  qualitatively. Three actual-PDF local reviews and cross-agent AI audits are complete. They found
  severity inflation and missed decision questions; no human lead adjudication or case-author
  learning observation was collected. The candidate remains NO-GO. Historical synthetic runs do not
  count.
- The historical attempt gate is absent from current ordinary use. Its older measurements do
  not validate the revised full-review-first flow.
- **Account capacity has not been measured.** No current token, free-tier or paste-limit claim
  is made. The actual consultant account must be tested.
- **The path that ships has never been scored.** Every measurement on record ran a different path.
- The bundle-key interlock **false-alarmed once on a complete bundle** — see
  [decisions/issues/29-the-interlock-false-alarmed-on-a-complete-bundle.md](decisions/issues/29-the-interlock-false-alarmed-on-a-complete-bundle.md).
- The tool behaves **measurably differently on different model families**, and a consultant brings
  their own.

The historical audit is in [decisions/AUDIT-2026-09-24.md](decisions/AUDIT-2026-09-24.md).
Current implementation status and checks are in
[validation/SPLIT-EXPERIENCES-2026-10-06.md](validation/SPLIT-EXPERIENCES-2026-10-06.md).

---

**Client confidentiality:** real deliverables, decks and extracted client text never enter this
repo. `.gitignore` enforces it. Anonymise before committing any example.
