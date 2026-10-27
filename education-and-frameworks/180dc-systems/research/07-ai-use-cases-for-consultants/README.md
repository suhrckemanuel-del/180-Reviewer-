# Research angle 7: what AI is actually good for, for consultants

Compiled 2026-10-06 from web research, three passes in parallel. A thinking database, not a plan:
about 110 use cases, each with what it does, value, how it fails, and a source. Rows marked
"synthesis" are reasoning, not sourced. Vendor quotas and prices move monthly, so re-check before
quoting them.

| File | What's in it | Rows |
|---|---|---|
| [01-what-firms-and-studies-show.md](01-what-firms-and-studies-show.md) | How McKinsey, BCG, Bain, Deloitte, PwC, EY and others use LLMs, plus the controlled studies, plus 10 key findings | 35 |
| [02-free-chat-use-cases.md](02-free-chat-use-cases.md) | Use cases on free ChatGPT, Claude, Gemini, Copilot and NotebookLM across the whole engagement, each with a principle-driven example prompt, the free-tier reality, and a top 10 | 45 |
| [03-pro-and-agentic-tools.md](03-pro-and-agentic-tools.md) | Paid and agentic: Claude Code, Cowork, Claude for Excel/PowerPoint, deep research, NotebookLM, Copilot, slide tools, HyperFrames. Best 10 and "not worth it" | 33 |

## The five things that matter most

1. **AI helps on drafting, ideation and critique, and hurts on "find the real answer in messy
   numbers".** In the BCG/Harvard study of 758 consultants, AI users were 25% faster and 40% better
   on tasks inside the frontier, and 19 points *less* likely to be right on a task just outside it.
2. **Answers vs hints decides whether people learn.** Students who practised with an AI that gave
   answers did 17% worse once it was removed; hints did no harm (Bastani et al., PNAS 2025). This
   is the evidence behind attempt-first and no-drafting.
3. **The main documented failure in consulting is fabricated sources.** Deloitte had two 2025
   government reports with citations that do not exist; one ended in a partial refund. Checking
   that every quote and source exists is the minimum.
4. **The firms' most-used tools are knowledge retrieval and slide critique** (Lilli, Deckster's
   "review this"). Their published numbers are usage counts, not quality measures, and nothing
   shows they check the logic or the numbers behind a slide.
5. **People can't tell whether AI is helping them.** Developers were 19% slower while believing
   they were 20% faster. Discount self-reported time savings, including our own.

## The highest-leverage moves, free tier

1. Red-team the recommendation before the client does.
2. The "so what?" ladder: the AI asks, the consultant answers.
3. MECE audit of an issue tree the consultant built first.
4. NotebookLM interview synthesis with quotes, plus a search for disconfirming evidence.
5. Action-title critique and a titles-only read of the deck.

Free-tier rule of thumb: NotebookLM for anything grounded in your own documents, Claude Free for
long single documents and critique, one deep-research run per project rather than per person, and
anonymise before pasting. Free ChatGPT trains on chats by default.

## The highest-leverage moves, paid

1. A reusable 180DC-methodology skill or plugin: encode the standard once, everyone inherits it.
2. Claude for Excel and PowerPoint: native, auditable models and the real template.
3. One deep-research tool, not several.
4. Artifacts for clickable calculators or dashboards that make a recommendation tangible.
5. Claude Code for one technical member, not the whole team.

**Not worth it for 180DC:** custom agent builds with no technical owner, Gamma or Beautiful.ai for
client decks, stacked research subscriptions, and HyperFrames as a default deliverable.

## Links to the rest of the repo

- The workshop built on this: [education/workshops/2026-10-deliverables-and-ai.md](../../education/workshops/2026-10-deliverables-and-ai.md)
- Earlier training research: [research/05](../05-training-and-knowledge-transfer/findings.md)
