# Ticket 04: what the bundle does above the chat-native floor

Prototype, 2026-09-19. Throwaway. Answers the four questions in
[issue 04](../issues/04-establish-what-the-bundle-can-do-on-a-free-account.md).

`26-chat-native.md` is the floor: zero fabricated quotes across 40 quotes on Opus, Sonnet and
Haiku 4.5, full bundle, prose output. This tests what happens **above** that floor once a
methodology bundle and an HTML output are added, and what happens when the bundle arrives
incomplete.

**Read the limits section before quoting any of this.** The headline result is real and the
mechanism is established. The free-tier ceiling itself is not measured.

---

## What was run

Seven arms, two model families, eleven completed runs. Bundles assembled from `TEST-KIT/`
by [build-bundles.py](build-bundles.py); replies in [runs/](runs/); scored by
[score.py](score.py) and [check-quotes.py](check-quotes.py).

Truncation is **induced, not observed**. That is the design choice that makes question 2
answerable at all: cutting at a known token offset turns "is a half-loaded bundle detectable"
into a controlled experiment, instead of waiting for a free tier to cut somewhere unknown.

| arm | what it models |
|---|---|
| `full-prose` / `full-html` | baseline, nothing missing |
| `tail85` / `tail65` / `tail40` | a single over-long paste cut at the end, i.e. a per-message cap |
| `headdrop` | paste 1 evicted by window overflow, i.e. the oldest turn dropped |

Models: **gpt-5.6-sol** via the Codex CLI (all seven arms) and **Haiku 4.5** via an agent
harness (four arms; the rest were lost to a spend limit, see limits).

## The bundle, in real tokens

Measured with `cl100k`, which is the wrong tokenizer for both families and within a few
percent for English prose.

| | tokens |
|---|---|
| Paste 1, system prompt | 4,065 |
| Paste 2A, chat-path context | 5,162 |
| Paste 2C, HTML-path context | 5,663 |
| **Instructions before any deck** | **9,227** (prose) / **9,728** (HTML) |
| Real decks, 14 cases | min 2,066 · median 4,052 · max 14,711 |
| **Typical whole review** | **~13,300** |
| **Worst whole review** | **~24,000** |

## Results

`branch` is which output shape came back. The chat path is only ever supposed to produce
`prose`.

| run | branch | sections | quotes verbatim | readiness leaked |
|---|---|---|---|---|
| codex / full-prose | **prose** | 12/12 | 4/4 | — |
| codex / tail85-prose | **prose** | 11/12 | 7/7 | — |
| codex / tail65-prose | ad-hoc | 0/12 | 9/9 | — |
| codex / tail40-prose | JSON fallback | 0/12 | 9/9 | — |
| codex / headdrop-prose | **prose** | 12/12 | 6/6 | — |
| codex / full-html | html | n/a | 7/7 | `Needs targeted revision` |
| codex / tail65-html | **REFUSED** | — | — | — |
| claude / headdrop-prose | **prose** | 12/12 | 3/3 | — |
| claude / tail65-prose | JSON fallback | 0/12 | 2/2 | `Nearly ready with minor edits` |
| claude / tail40-prose | JSON fallback | 0/12 | 3/4 (1 from brief) | `Needs targeted revision` |
| claude / full-html | html | n/a | 4/4 | `Nearly ready with minor edits` |

---

## 1. The ceiling, and what drops first

**The ceiling was not measured.** No free-tier account was driven, and the research pass on
published window sizes and overflow behaviour died on a spend limit before it reported. What
follows is the arithmetic and the failure ordering, which are established; where a given free
tier actually cuts is not.

**The arithmetic.** 9.2K tokens of instructions ride along before the deck. A typical real
review is ~13.3K and the worst of fourteen real decks is ~24K. That is comfortably inside a
200K window and it is **not** obviously inside whatever a free GPT tier allows, which is
exactly the number nobody has.

**What drops first depends on the direction of the cut, and the two directions have opposite
consequences.**

- **Tail cut** (one paste too long). Paste 2A is ordered preamble → calibration → output
  format, so **the output format dies first**. It occupies the last third of the file. At 85%
  the format survives nearly whole (11/12 sections). Between 85% and 65% it goes, and with it
  the whole chat-native design.
- **Head eviction** (window overflow across turns). Paste 1 dies whole, taking the synthesis
  protocol, the severity definitions and the blocking rules with it.

**The quote rule survives both**, because it is stated three times across two pastes: twice in
paste 1 (lines 39 and 183) and again in paste 2A's closing rules. Nothing else in the bundle is
redundant like that, and it is the reason the floor held under every cut.

## 2. Is truncation silent? Split, and the split is the actionable result

**Losing paste 2 is loud.** Every arm that lost the output format changed output *shape* —
JSON, or an invented "Strengths / Priority findings" layout. None produced the prose format
badly; they produced something else entirely. That gives a one-line check anyone can run:

> **Does the reply open with `REVIEW OF:`?** If not, paste 2 did not land whole. Nothing
> below that line is trustworthy as a chat-native review, whatever it looks like.

**Losing paste 1 is silent, and this is the dangerous case.** `headdrop` — the entire system
prompt missing — returned **12/12 sections on both models**, with every quote verbatim and a
valid paste-back record. It is indistinguishable from a good run by every structural check,
including the quote gate. A student would have no way to know.

What is actually lost there is restraint: Codex returned **6 findings without the system prompt
against 4 with it**, Haiku 3. One sample per cell, so this is a direction and not a number.

**The one genuinely good failure was the HTML arm.** `tail65-html` did not review. It refused,
and named the cut:

> "The HTML template is incomplete. It ends after `<div id="stu" hidden></div>` with a lone
> `<`, so I cannot paste it unchanged."

That is the whole mechanism in one result. **Truncation announces itself when the truncated
thing has a closure property the model checks.** A half-delivered HTML template is
syntactically broken and gets refused. A half-delivered prose document is just a shorter prose
document, so the model proceeds. If truncation detection is wanted on the prose path, the
bundle has to carry something with a closure property — a terminator the model is told to
verify — because prose does not have one on its own.

## 3. HTML on a free-tier-class model

**Both models emitted it, complete, first try.** Both reproduced the full template and filled
the `REVIEW` object; both render; both modes work; the student-mode attempt gate is intact.
2/2, which is an existence proof and not a reliability estimate.

**But the HTML path re-introduces the readiness level, by design, not by truncation.**
`PASTE-2C` requires `aiLevel` as a mandatory field and the template renders it as an "AI guess"
pill in lead mode. On the same deck with the same bundle the two models returned **"Needs
targeted revision"** and **"Nearly ready with minor edits"** — reproducing, across models, the
instability the readiness level was retired for. Student mode carries no pill, so the leak is
lead-mode only.

This collides with the map's settled "**No readiness level, for anyone**" and belongs to
ticket 05. The prose path (2A) suppresses readiness deliberately and says so at length; the
HTML path (2C) requires it. **Two artifacts in the same shipped kit contradict each other.**

## 4. Codex and quote-or-abstain

**The prompt survives a non-Claude model intact.** gpt-5.6-sol produced the prose format at
12/12 sections with a valid paste-back record, and held the format at 11/12 even at an 85% cut.

**Quote-or-abstain held everywhere.** Across all eleven runs, both families and every
truncation level:

**55 evidence quotes. 54 verbatim from the deck. 1 verbatim from the brief. 0 fabricated.**

The single non-deck quote (Haiku, `tail40`) is a real if minor rule violation — it quoted the
input brief's source notes as though they were deliverable text. It is not an invention.

The floor in `26-chat-native.md` therefore extends: it holds on a second model family, it holds
with a methodology bundle attached, it holds in HTML, and it holds when most of the bundle is
missing. **Quote-or-abstain is the most robust property the tool has**, and the redundant
statement of it across both pastes is why.

---

## Two defects found while building the bundle

**1. The noise budget is never stated to the model.** Paste 1 says "Cut to the noise budget for
the mode (below)" and there is no below — the word "deep" does not appear in paste 1 at all.
Paste 2A refers to "the noise budget in the prompt". It is in neither. The same paste also says
"see the scope matrix you were given", which is also absent. Both live in the harness pack that
`run-reviews.js --emit-packs` builds, and the three-paste kit does not carry them. So the
restraint ceiling is not enforced on the chat path at all, truncated or not, and finding counts
floated between 3 and 6 with nothing to cut to. This is the same family as the packaging defect
the kit's README already documents for paste 2B. **Ticket 08 should treat the mode table and
the scope matrix as required bundle contents.**

**2. The JSON fallback is not a degraded review, it is a different product.** When paste 2's
format is lost, the model falls back to the JSON branch described in paste 1's OUTPUT block —
which emits the full ten-dimension rubric with scores, a `diagnosticMean`, and a readiness
level. Everything the chat-native path was built to withhold arrives at once, presented
authoritatively, to a student with no lead in between. The kit's README also tells testers that
JSON is a legitimate route (route 2), so "I got JSON" does not read as an error.

---

## Limits — read before quoting any of this

- **No free-tier account was tested.** gpt-5.6-sol and Haiku 4.5 are model proxies. Neither is
  claude.ai-free or chatgpt-free, and crucially **neither reproduces a chat UI's truncation
  behaviour**, which is the actual mechanism question 1 asks about. Chat UIs also convert long
  pastes to attachments, which this does not model at all.
- **Both models ran inside agent harnesses** (Codex CLI, a subagent), each with its own system
  prompt. That is faithful to "whatever coding agent they have" and is *not* faithful to a
  plain chat window.
- **n = 1 per arm.** No repeats, no seeds, one deck (`PASTE-3-deck-A`, synthetic, 740 tokens —
  well under the 4,052-token median). Every count here is a single observation.
- **Four Claude arms are missing** (`tail85`, `tail40`-rerun, `tail65`-rerun, `full-prose`),
  lost to the org monthly spend limit mid-run. The Claude column is four arms, not seven.
- **The published-ceiling research did not complete.** Window sizes, per-message caps and
  overflow behaviour for the four free tiers remain unestablished.
- Truncation was induced at clean token offsets. Real truncation may land mid-token, mid-word,
  or drop a middle chunk rather than a tail.

## What would close the gap

One human with a free account and twenty minutes, pasting `TEST-KIT/PASTE-SETUP-combined.md`
(41,873 characters) into each of the four free tiers and reporting only: did it reject the
paste, convert it to an attachment, or accept it — and **did the reply open with
`REVIEW OF:`**. That last question is the entire detector, and it needs no judgement.
