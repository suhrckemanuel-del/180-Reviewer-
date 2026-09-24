# Establish what the bundle can do on a free account and in Codex

Type: prototype
Status: resolved
Blocked by: —

## Question

The tool is a prompt plus a methodology context bundle plus the deliverable. It has to run for a
student with no paid plan, and for whatever coding agent they have — Claude Code, Codex, a plain
chat window. It was tested once on a free account and "worked to an extent", which is not a finding
anyone can build on.

`26-chat-native.md` established that the three-paste path holds on Opus, Sonnet and Haiku 4.5 —
zero fabricated quotes across 40 quotes and four models. What is unknown is everything above that
floor once a methodology bundle and an HTML output are added.

Find out, concretely:

1. **The context ceiling.** How much methodology context can ride along before a free-tier window
   truncates it, and what gets dropped first when it does.
2. **Whether truncation is silent.** A bundle that half-loads and reviews anyway is the dangerous
   failure. Is there a detectable signal?
3. **HTML output.** Does a free-tier model reliably emit the HTML, and what does it do when it
   cannot — degrade to prose, or produce broken markup?
4. **Codex and other agents.** Does the prompt survive a non-Claude model at all, and does
   quote-or-abstain hold there?

Prototype the smallest bundle that answers these. Link the artifact from this ticket.

Answer records: the ceiling, the failure modes, and which of them are detectable from the output
alone.

---

## Resolution (2026-09-19)

Prototype: [`proto-04-free-tier-ceiling/`](../proto-04-free-tier-ceiling/), findings in
[RESULTS.md](../proto-04-free-tier-ceiling/RESULTS.md). Seven arms, two model families
(**gpt-5.6-sol** via Codex and **Haiku 4.5**), eleven runs. Truncation was **induced** at known
token offsets rather than observed, which is what made question 2 answerable at all. Local only,
like the ticket 03 analysis.

**1. The ceiling — arithmetic established, ceiling NOT measured.** The bundle costs **9,227
tokens of instructions** before any deck (paste 1 4,065 + paste 2A 5,162). A typical real review
is **~13,300 tokens** and the worst of fourteen real decks **~24,000**. Where any free tier
actually cuts is unknown: no free account was driven and the research pass on published window
sizes died on a spend limit. **What drops first depends on the direction.** A tail cut kills
paste 2A's output format first — it is the last third of the file, gone between 85% and 65%. A
head eviction kills paste 1 whole. The quote rule survives both because it is stated three times
across the two pastes, and that redundancy is why the floor held everywhere.

**2. Truncation is silent in exactly one direction, and that is the finding.** Losing paste 2 is
**loud**: every arm that lost the format changed output *shape* — JSON, or an invented layout —
never a degraded version of the right one. That yields a one-line detector needing no judgement:
**does the reply open with `REVIEW OF:`?** Losing paste 1 is **silent**: `headdrop`, with the
entire system prompt missing, returned **12/12 sections on both models**, every quote verbatim,
valid paste-back record — indistinguishable from a good run by every check including the quote
gate. What degrades is restraint (Codex 6 findings without the system prompt vs 4 with; n=1).
The mechanism: **truncation announces itself only when the truncated thing has a closure property
the model checks.** The one arm that refused was `tail65-html`, which named the exact byte the
template died on. Prose has no closure property, so the model just proceeds.

**3. HTML: both models emitted it complete, first try, and both render** with two working modes
and the attempt gate intact. 2/2 — an existence proof, not a reliability estimate. **But the HTML
path requires a readiness level by design**: `PASTE-2C` makes `aiLevel` mandatory and the template
renders it as an "AI guess" pill. On identical input the two models returned "Needs targeted
revision" and "Nearly ready with minor edits" — reproducing the instability the level was retired
for. Routed to ticket 05.

**4. The prompt survives Codex fully and quote-or-abstain holds there.** Across all eleven runs,
both families, every truncation level: **55 evidence quotes, 54 verbatim from the deck, 1 verbatim
from the brief, 0 fabricated.** The `26-chat-native.md` floor extends to a second model family,
to a methodology bundle, to HTML output, and to a mostly-missing bundle.

**Two defects found while building the bundle.**

- **The noise budget is never stated to the model.** Paste 1 says "Cut to the noise budget for the
  mode (below)" and there is no below; "deep" does not appear in paste 1 at all. Paste 2A defers
  to "the noise budget in the prompt". It is in neither, and nor is the scope matrix paste 1 also
  cites. Both live in the harness pack. The restraint ceiling is therefore unenforced on the chat
  path, truncated or not. Routed to ticket 08.
- **The JSON fallback is a different product, not a degraded review.** Losing paste 2's format
  drops the model onto paste 1's JSON branch, which emits the full ten-dimension rubric with
  scores, a `diagnosticMean` and a readiness level — everything the chat-native path withholds,
  delivered authoritatively to a student with no lead in between. The kit's README also presents
  JSON as a legitimate route, so "I got JSON" does not read as an error.

**Surfaced:** tickets 11 (measure the four free tiers by hand), 12 (decide the bundle's truncation
self-check), 13 (decide the default output path). Input notes added to 05 and 08.

**Does not unblock cleanly.** Ticket 08 asks for bundle cost "against the ceiling found in ticket
04". The cost is established; the ceiling is not. 08 is left unblocked deliberately rather than
made to wait on ticket 11 — it should answer in the form of a token budget, not a fixed list.
