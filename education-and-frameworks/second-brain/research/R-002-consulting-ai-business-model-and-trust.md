---
type: research
id: R-002
date: 2026-08-19
updated: 2026-08-19
tags: [research, 180dc, consulting-industry, ai-adoption, trust, pricing]
ai-first: true
sensitivity: internal
confidence: mixed
status: partial
---

# R-002 — How AI is changing the consulting business model, and the trust problem

## For future Claude
Evidence brief on what AI has actually done to consulting economics, hiring, and client trust as of August 2026. The single most useful finding: four Big Four firms published AI-fabricated reports in ten months and all four were caught by outsiders, while 70% of clients say they would not trust an AI-prepared consultancy report. This is the evidence base behind the verification-first positioning in [[ideas/180dc/workshops/index]]. Partial — this was one of four planned research lanes; two never completed (see Coverage gaps).

## Coverage gaps (read before relying on this)
Four research lanes were commissioned on 2026-08-19. Two completed (this note and [[ideas/180dc/research/R-003-production-agent-patterns-and-evaluation]]). Two were lost when the session ended and were never re-run:
- **What consulting firms actually deploy internally** (McKinsey Lilli, BCG tooling, Bain/OpenAI, Big Four) — unverified here.
- **Academic evidence on AI and knowledge-work quality** (Harvard/BCG jagged frontier study, deskilling, homogenization) — unverified here. This gap matters most for the training argument, since it is the lane that would have carried evidence on junior skill development.

Do not present this as complete industry research. Re-run those lanes before using it in a board setting.

## Source-quality warning (stated by researcher, 2026-08-19)
Much of what ranks on this topic is itself AI-generated SEO content. "AI consulting market size 2026" was found quoted as $8.96bn, $14.1bn, $30.24bn, $38.7bn and $65bn across sources all presenting as research. **Treat every market-size and average-rate figure in this space as unusable.** Claims below are graded: `strong` = FT, Source Global Research, primary company results, or primary forensic investigation; `medium` = secondary aggregation; `weak` = contested or thinly sourced.

---

## Finding 1 — Four Big Four AI fabrication incidents in ten months (confidence: strong)

All four were detected by outsiders using cheap tools, not by internal QC. In three of four, the document was *marketing* — thought leadership about AI, produced with unverified AI.

| Firm | Date | What happened |
|---|---|---|
| **Deloitte Australia** | Oct 2025 | ~AU$440,000 government report (Dept of Employment and Workplace Relations) contained fabricated academic citations and **a fabricated quote from a federal court judgment**. Found by Chris Rudge, Deputy Director of Health Law, University of Sydney. Deloitte refunded ~AU$97,000; revised version disclosed use of Azure OpenAI GPT-4o. |
| **EY** | 14 May 2026 | "Points of Attack: Uncovering Cyber Threats and Fraud in Loyalty Systems" (44pp). GPTZero found **16 of 27 sources fabricated, misattributed or dead (~70% of citations)**, including a cited McKinsey study on a "$200bn loyalty market" that has never existed. EY pulled the report the same day. |
| **KPMG** | surfaced Jun 2026 | "Total Experience: Redefining Excellence in the Age of Agentic AI." Of 45 citations, **only 5 accurate**; 16+ confirmed hallucinations. **UBS, the NHS, Swiss Federal Railways and Transport for London told the FT that claims about their AI usage were untrue or misleading.** Report pulled. |
| **PwC** | Aug 2026 | Four Middle East thought-leadership reports. GPTZero assessed the 2025 "Transforming Governance" as **84% likely wholly AI-generated**; it contained a fabricated government framework called "Citizen Pulse" that does not exist. **An FT investigation verified the findings.** |

Sources: https://oecd.ai/en/incidents/2025-10-05-be45 | https://incidentdatabase.ai/cite/1193/ | https://cybernews.com/ai-news/ernst-young-ai-slop-gptzero/ | https://gptzero.me/news/investigations-kpmg/ | https://oecd.ai/en/incidents/2026-06-12-b883 | https://gptzero.me/news/investigations-pwc/ | https://futurism.com/artificial-intelligence/top-consulting-group-pwc-ai-report-bizarre-hallucinations

## Finding 2 — Clients do not trust AI-made consulting work, and exposure makes it worse (confidence: strong)

Source Global Research, survey of **3,887 companies** (as of 2026-08):
- **70% would not trust a consultancy report prepared using AI.**
- Roughly **a third** said learning a firm had used AI in a published report would shake their confidence in it.
- **77% of clients who have actually used consultants' AI tools think the technology is a bubble about to burst, versus 55% of those who have not** (per CEO Fiona Czerniawska). Exposure *reduced* confidence.
- Meanwhile **more than 75% of UK consultancies use AI in delivery** (MCA).

Source Global's related observation: **"the market is currently pricing AI involvement as a discount rather than a premium,"** which makes disclosure of AI use a commercial decision rather than an ethical one for most firms.

Source: https://www.resultsense.com/news/2026-08-04-consultancy-clients-distrust-ai-reports/

## Finding 3 — Fee compression is demanded, but not yet visible in aggregate (confidence: strong both directions)

**Precedent for compression:** KPMG International pressed its own auditor, Grant Thornton UK, for a fee cut on the grounds that AI made audits faster, and threatened to switch. **The fee fell from $416,000 to $357,000, about 14%** (FT, 6 Feb 2026). First documented case of AI efficiency as an accepted basis for a discount — and the obvious inference is that KPMG's own clients run the same argument back at KPMG.

Grant Thornton's rebuttal is the canonical defence: *"High-quality audits rely heavily on expert human judgment, so our fees reflect both the cost of our people and the cost of the technology that supports them."*

**Against compression:** European audit fees rose in all but one country (Ideagen Audit Analytics). MCA members booked £10.9bn in 2025 and forecast **+6% in 2026, +8% in 2027**. Elixirr (listed boutique) H1 2026: revenue £89m **+25%**, adjusted EBITDA £27.6m **+29%**, margin **31%**, AI-linked income up 260%+.

**Synthesis:** compression is demanded and forward-loaded; the compression *event* has not happened. What is visible is **mix shift** — Accenture Q1 FY26 consulting revenue grew 3% versus 7% for managed services. Clients are buying execution, not discretionary strategy.

Sources: https://www.irishtimes.com/business/2026/02/06/kpmg-pressed-its-auditor-to-pass-on-ai-cost-savings/ | https://www.oxfordeconomics.com/resource/mca-annual-industry-report-2026/

## Finding 4 — The junior pyramid is being cut on a forecast, not a measurement (confidence: strong)

FT, 1 Dec 2025: MBB and Big Four froze graduate starting salaries for a **third consecutive year**. Senior executives estimated **UK graduate recruitment could fall by about half** in the coming year. PwC abandoned its target of adding 100,000 employees globally by 2026.

The decisive line from that reporting: conservative hiring is *"in anticipation of productivity gains from AI, not because those gains are necessarily yet being realised."*

Nick Pye (Managing Partner, Mangrove Consulting, 19 Feb 2026) argues the model shifts to a **"diamond"** — thin base, fat middle — and that the training pathway inverts: firms hire **mid-career specialists rather than train generalists**, so you "specialize before consulting" instead of after.

**The structural point, and the most important idea in this note:** the pyramid was simultaneously a *margin* mechanism and a *training* mechanism. AI attacks the margin function first. **Nobody has solved the training function.** This is the industry's genuine unresolved problem, and the one place where the disruption story is under-stated rather than over-stated. Directly relevant to [[ideas/180dc/problems/P-008-consulting-training]].

Sources: https://tech.slashdot.org/story/25/12/01/1241232/ | https://www.consultancy.uk/news/43210/ai-may-up-end-the-consulting-pyramid

## Finding 5 — What clients now expect not to pay for (confidence: strong on direction, weak on magnitude)

Desk research and market scans; benchmarking; framework application; slide production; interview and meeting summarisation.

The structural change is not that these got cheaper — it is that **clients can now do the first 60% before they ever contact you**, which resets the negotiation before it starts. Corollary: any proposal whose value narrative rests on "we will research X and produce a report" now competes against free.

## Finding 6 — Where value migrated (confidence: medium, synthesised)

1. **Accountability you can transfer** — a named party that signs and carries liability. AI cannot hold a fiduciary duty.
2. **Judgement under ambiguity** — where the data does not determine the answer.
3. **Organisational politics and change execution.**
4. **Access and proprietary data** — what is not in the training corpus.
5. **Implementation depth** — the forward-deployed-engineer model.
6. **Verification as a service** — under-discussed, and given Finding 1, about to become a paid category.

## Finding 7 — The small-firm opening (confidence: medium — this is inference, not measurement)

The Big Four have a **verification problem at scale**: a firm that ships a 45-citation report with 5 accurate citations demonstrably cannot check its own output. A small team can — a partner can personally verify every claim in a 40-page report.

Given Finding 2 (the market prices AI involvement as a discount), the defensible position is **not** "we use AI." It is **"we use AI, here is the human verification layer, and that layer is what you are paying for."**

This is the evidence behind the verification-first decision in [[ideas/180dc/workshops/index]].

## Finding 8 — 180DC has already published its own AI methodology (confidence: strong)

180 Degrees Consulting published an AI methodology (David Cheesman, The Prompt Engineers; Navya Agarwal, ex-180DC Global Leadership Team). Three-layer model: **AI generates the foundations** (capability maps, maturity levels, rubrics, scoring) → **alumni/practitioner mentors refine** → **practice-testing on real engagements improves**. Their formulation: *"the book provides intellectual rigour; AI provides scale and speed; mentors provide judgement and nuance."*

**Gap worth noting:** it contains no risk or misuse warnings, which given Finding 1 is a material omission. Manuel's workshop programme can fill that gap rather than duplicate existing material.

Source: https://www.180dc.org/resources/amplifying-impact-by-using-a-tool-to-sell-more-to-win-more-projects

## What is hype (confidence: strong)

- **"Consulting fees are collapsing."** Not in the data. See Finding 3.
- **"AI-native firms are taking share from MBB."** No revenue evidence exists. OpenAI's Frontier Alliances structure (partnerships with Accenture, BCG, Capgemini, McKinsey, Feb 2026) suggests OpenAI itself concluded it needed incumbent distribution rather than being able to bypass it.
- **"The pyramid has already been replaced by AI."** See Finding 4 — cuts precede measured gains.
- **MIT Project NANDA "95% of GenAI pilots fail."** Universally cited, methodologically contested (52 interviews, 153 survey responses, not peer reviewed). **Do not build an argument on it.**

## Genuinely uncertain
- Whether 2025–26 junior hiring cuts are AI-driven, or a demand-cycle correction being *narrated* as AI. Both stories fit the data.
- Whether client AI-scepticism is a durable trust floor or a transient reaction to the 2025–26 scandals. Source's finding that exposure *increases* scepticism argues durable; two years is too short to know.

## Related
- [[ideas/180dc/workshops/index]] — the workshop programme this evidence supports
- [[ideas/180dc/research/R-003-production-agent-patterns-and-evaluation]] — the build-side companion
- [[ideas/180dc/problems/P-008-consulting-training]] · [[ideas/180dc/problems/P-007-deliverable-quality]] · [[ideas/180dc/problems/P-004-member-value]]
- [[projects/180dc]] — current truth and priorities
