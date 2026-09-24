# Paste-ready build prompt: the paired mockups, one review shown two ways

**Run on Opus at high effort.** This writes into `website/`, which is a deployed Cloudflare
Pages tree. A mistake here publishes client material to the open web, and the correctness
constraint in section 3 is subtle enough that a fast model will get it wrong and produce
something that looks right.

Paste everything below the line into a fresh chat. It is self-contained.

---

Working in `c:\Users\User\Desktop\180dc-ai`, branch `wip/case-study-gallery-private-content`.
**Build two HTML pages and a page that shows them together. Write no new strategy documents.**

## What you are building, and the one idea it has to carry

180 Degrees Consulting branches are student teams. The AI Quality Reviewer reaches them through
two doors, and people keep assuming the free one is a cut-down version of the paid one. It is
not, and the mockups exist to make that legible in a glance:

- **The desk.** A lead with Claude Code produces JSON and opens it in a hosted Triage Desk:
  status board, blocking issues, triage cards, rubric, a note that writes itself, a student pack.
- **The chat path.** A consultant with no budget, no login and no paid account pastes three
  things into any free chat and gets a readable review back. **This is the product**, not the
  fallback. Most 180DC consultants are students with no chargeable budget.

**The single idea both pages must carry: the findings are identical, and the difference is the
container.** The desk shows a readiness level and a diagnostic score because a page can cage
them behind a quote gate, a warning strip and a redacted student pack. The chat path produces
**no** level and **no** score, because a chat window can cage nothing and the reader is the
operator with nobody in between. That is not a feature gap. It is the same review with the
unreliable half withheld where nothing can hold it.

Full reasoning in [26-chat-native.md](26-chat-native.md) section 3.4 and
[11-decision-log.md](11-decision-log.md), entry 2026-08-09.

## Read first

- `website/reviewer-mockups/build-desk.js` — the existing mockup generator, its header comment
  especially. It already splits fabricated from live and refuses to write a live build to a
  tracked path. Follow that pattern; do not invent a second one.
- `website/reviewer-mockups/data-fabricated.json` — the fabricated review. **Both new pages
  render this same object.** Client Z, five findings.
- `tools/quality-reviewer/v2/index.html` — the real desk. The mockup should look like the
  product, not like a redesign of it.
- `tools/quality-reviewer/v2/CHAT-CONTEXT.md` PART TWO — the exact chat output format. The chat
  mockup renders this, not an approximation of it.
- `tools/quality-reviewer/v2/26-chat-native.md` sections 3.1 to 3.5.

## Build three things

### 1. The desk view
A presentational mockup of the Triage Desk on the fabricated review. The working product already
exists; this is the version you can put in a deck or a board pack. Status board, the blocking
issues with their ceilings, the findings as triage cards, the rubric, the note. It **does** show
the readiness level and the diagnostic mean, and it shows them the way the product does: the
level labelled "AI guess", never preselected, sitting under the strip that says the same deck
has come back at two different grades.

### 2. The chat view
What a consultant on a free tier actually sees: a chat window, their three pastes collapsed to a
summary, and the review rendered as the prose it really is. Take the text from the chat format
in `CHAT-CONTEXT.md` PART TWO, populated from the same fabricated review.

**It must contain no readiness level, no ceiling, no blocking-rule number and no score.** Not
greyed out, not blurred, not behind a lock icon. Absent. The only place any level string may
appear is inside the paste-back record block, where the format prints the four options for the
human to choose from. If your page shows a locked or teased grade you have inverted the product:
the grade is not a premium feature, it is the part the evidence does not support.

### 3. The comparison
One page putting them side by side, with the findings visibly the same in both and the
difference visibly limited to the container. This is the page that will actually get shown to a
board or another branch, so it carries the one-line framing: **both doors give you the same
findings, and neither gives you a grade you should pass on.**

## Hard constraints

**Fabricated data only, everywhere.** `website/` is a deployed Pages tree. A real review quotes
a client deliverable verbatim, and committing one here publishes it. `build-desk.js --live`
already refuses to write unless its output path is gitignored; anything you add follows the same
rule. Before you finish, grep your own output for the real case identifiers (`real-01` through
`real-14`, `Client R`) and confirm zero hits.

**Do not touch** `tools/quality-reviewer/v2/index.html`. That is the live product, deployed, and
this sprint is presentational. If you find a bug in it, write it in the handover.

**No invented numbers.** Every figure on either page comes from `data-fabricated.json`. If the
comparison page wants a statistic about the project, take it from `18-evidence-base.md` or
`STATUS.md` and cite which. Do not write "90% faster" or anything like it; nobody has measured
what this costs a lead today and `STATUS.md` says so explicitly.

**Both pages render in a viewer's light or dark theme** and are readable on a phone.

## Definition of done

- Two mockup pages plus a comparison page, in `website/reviewer-mockups/`, tracked and safe to
  show anyone.
- Both driven from the same `data-fabricated.json`, so the findings are provably identical. Say
  in the handover how you guaranteed that rather than asserting it.
- A grep result, pasted in the handover, proving no real-case identifier appears in any new file.
- `node check-docs.js` clean.
- A short handover listing anything you found and deliberately did not fix.

## What would make this sprint a failure

A chat view that shows a locked, blurred or teased grade, which sells the free path as crippled
and misstates why the grade is missing. Any real client text reaching `website/`. Invented
performance numbers. Redesigning the desk instead of representing it. Or two pages built from
different data, which would quietly break the only claim the pair exists to make.
