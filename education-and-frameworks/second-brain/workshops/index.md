---
type: reference
date: 2026-08-19
updated: 2026-08-19
tags: [180dc, workshops, ai-training, head-of-ai, education]
ai-first: true
sensitivity: internal
status: design
---

# 180DC AI Workshop Programme

## For future Claude
Design hub for Manuel's 180DC AI workshop programme, shaped in conversation on 2026-08-19. Two tracks: a **board track** (delivered first, by Manuel and his AI-team partner, as pilot and credibility-builder) and a **member track** (post-selection, raising the floor across the cohort). The pedagogical spine is *earn judgement unaided first, then amplify it with AI*. Nothing here is board-approved yet. Evidence base: [[ideas/180dc/research/R-002-consulting-ai-business-model-and-trust]] and [[ideas/180dc/research/R-003-production-agent-patterns-and-evaluation]].

Status: **design, pre-approval.** This supersedes nothing; it gives substance to priority 3 in [[projects/180dc]] ("start workshop design").

---

## The problem being solved (stated by Manuel, 2026-08-19)

Members are already using AI, but with basic prompting, and are getting maybe **10–20% of the available value**. The goal is not adoption — adoption already happened. The goal is **quality of output**.

This sits against [[ideas/180dc/problems/P-004-member-value]] and [[ideas/180dc/problems/P-008-consulting-training]].

## The pedagogical spine (the core idea)

> **The way to get good AI output is human taste and critical thinking. You cannot amplify judgement you do not have.**

This is Manuel's own formulation and it resolves the hardest open question in the industry. Per [[ideas/180dc/research/R-002-consulting-ai-business-model-and-trust]] Finding 4, the consulting pyramid was simultaneously a margin mechanism and a training mechanism; AI attacked the margin function and **nobody has solved the training function**. Firms cut junior intake on a forecast without replacing the way judgement gets built.

180DC's existing structure already contains the answer:

| Stage | What it does |
|---|---|
| **Beginner case workshops** | Fundamentals |
| **Advanced case workshops — deliberately without AI** | Builds the unaided taste. This is the load-bearing step. |
| **AI workshops (post-selection)** | Teaches people to amplify judgement they now actually have |

**Keep the advanced track AI-free and make it deliberate rather than incidental.** Earn the judgement, then amplify it. No large firm can copy this, because they cut their junior pyramid before solving it.

## Design principle for everything built

> **Build AI that checks, challenges and teaches. Not AI that produces.**

The existing AI Quality Reviewer ([[projects/180dc]]) already has this shape — it critiques member work and teaches the principle behind each finding rather than doing the work. That instinct should govern the whole programme. It sidesteps the client-trust problem, compounds skill instead of eroding it, and matches the verification-first positioning below.

## The 10–20% problem — what actually closes the gap

Not clever prompting. Three things:

1. **Context** — giving it the real case material, the client's actual constraints, prior work
2. **Iteration** — critiquing and redirecting rather than accepting the first output
3. **Knowing what good looks like** — the taste, which is why the unaided workshops come first

**Teaching method: show, don't explain.** Live-rebuild a real weak output into a genuinely good one in front of the room. The gap between the two *is* the lesson.

## Track structure

| | **Board track** | **Member track** |
|---|---|---|
| **Who** | Board members with Pro plans | Members, post-selection |
| **Delivered by** | Manuel + AI-team partner | TBD |
| **When** | **First** — pilot and credibility | After board buy-in |
| **Core** | Context, iteration, taste | Same |
| **Extension** | Agentic workflows, subagents, personal career leverage | Amplifiers by plan tier |
| **Purpose** | Genuine value to board; they understand what they are approving | Raise the floor across the cohort |

### Why board-first (reasoning, 2026-08-19)
Same core material at a higher ceiling. It tests whether the teaching lands on a small friendly audience, builds credibility, and — the part that matters — board members who have personally felt the difference between 20% and 80% of an AI output will evaluate the AI-projects proposal with a reference experience rather than an abstraction.

**Caution, stated at design time:** this works because the training is genuinely valuable and given freely. It stops working the moment it reads as a trade. **Do not pitch the AI projects in the same session.** Let the goodwill sit; ask separately.

### Free vs paid plan handling
Do **not** build two workshops split by plan tier — free users learn they are in the lesser session and disengage. Instead:
- **The method** (context, iteration, taste) is plan-agnostic and works on free. That is ~80% of the gain, at no cost.
- **The amplifiers** (subagents, long context, projects, custom instructions) are the Pro extension, taught second.

### The one high-level technique worth a slot
From [[ideas/180dc/research/R-003-production-agent-patterns-and-evaluation]] Section 3:

> **Fan out to gather. Stay single-threaded to synthesise.**

Consulting translation: use subagents to research a market from ten angles at once; **never** use them to write three sections of the same deck. Parallel agents cannot see each other's implicit decisions, so the sections do not fit together. Counterintuitive enough to be worth teaching, concrete enough to apply immediately. Note the cost: multi-agent runs ~15x the tokens of a chat, which is a real constraint on a consumer plan — knowing when *not* to fan out is part of the skill.

## Decisions settled (2026-08-19, by Manuel, not yet board-approved)

| # | Decision | Rationale |
|---|---|---|
| 1 | **Build the verification layer.** | Four Big Four fabrication scandals in ten months, all caught externally; 70% of clients distrust AI-prepared reports. A small team can verify what a large firm demonstrably cannot. See [[ideas/180dc/research/R-002-consulting-ai-business-model-and-trust]] Findings 1, 2, 7. |
| 2 | **Teach judgement, not tool tricks.** | The durable skill is knowing what to verify and when output is wrong. |
| 3 | **AI workshops come after selection**, for members who are in. | |
| 4 | **Board track runs first and separately from the member track.** | Pilot + credibility + informed approvers. |
| 5 | **Method taught plan-agnostic; amplifiers taught as tier extension.** | Avoids a two-class workshop. |

## Open decisions

| # | Question | Why it matters |
|---|---|---|
| A | **The board pitch itself.** | Gates everything. Strongest framing: *the industry cut its junior training pipeline on a forecast and has no replacement; we are a training organisation, so we can build what they cannot.* That is a vision, not a tooling request. |
| B | **Is the board track one session or a series?** | Affects scope and the ask. |
| C | **What counts as an "AI project"?** | Manuel floated members doing AI work beyond consulting deliverables. Genuinely different risk profile — **separate it from the workshop track in the proposal**, or the board evaluates both as one thing and the ambitious half drags down the safe half. |
| D | **Disclosure policy — do teams tell clients AI was used?** | 70% distrust argues conceal; but concealment is how the Big Four incidents became scandals rather than corrections. Only defensible version: disclose the use *and* the verification layer, and sell the layer. |
| E | **Where exactly is the line on AI use?** | Needs an explicit list. Fine for research and first drafts; never for an unverified client-facing claim. Vague guidance means everyone invents their own line. |
| F | **Does 180 build a shared context corpus, or only train people?** | [[ideas/180dc/research/R-003-production-agent-patterns-and-evaluation]] Section 7 is unambiguous: a small org should build **context and evals**, not agents. A shared corpus compounds across cohorts; training alone evaporates when members graduate. Highest-leverage choice on this list. |
| G | **Co-delivery alignment.** | Manuel and his partner must agree on the method before teaching it. |

## Next actions

1. Draft the **workshop spine** — session flow, what is taught, what is demonstrated live, the before/after rebuild.
2. Draft the **board pitch** (open decision A).
3. **Re-run the two lost research lanes** — internal firm deployment, and the academic evidence on AI and skill development. The second directly strengthens the training argument for the board.

## Related
- [[projects/180dc]] — role, current priorities, Quality Reviewer status
- [[ideas/180dc/index]] — problem studio hub
- [[ideas/180dc/hypotheses/H-002-tools-optimization-and-capability-system]] — the operating model this programme instantiates
- [[ideas/180dc/problems/P-004-member-value]] · [[ideas/180dc/problems/P-008-consulting-training]] · [[ideas/180dc/problems/P-007-deliverable-quality]]

## Session designs
- [[ideas/180dc/workshops/consultant-training-frameworks-and-agenda]] — consultant training (3 Nov 2026, TBC): five frameworks to review and the 2-hour live-case agenda (2026-10-09)
