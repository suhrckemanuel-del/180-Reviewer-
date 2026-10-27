---
type: reference
date: 2026-10-09
updated: 2026-10-09
tags: [180dc, workshops, consultant-training, frameworks, ai-research, head-of-ai]
ai-first: true
sensitivity: internal
status: design
---

# Consultant training: frameworks and 2-hour agenda

## For future Claude
The working design for the 180DC consultant training (planned for Tue 3 Nov 2026, or Wed 4 Nov, TBC), agreed with Manuel in conversation on 2026-10-07 to 2026-10-09. It holds two things: the five frameworks to teach, and the 2-hour block structure built around a live case. Manuel wants to review the frameworks later. Nothing here is board-approved; date, time and format are still TBA. Parent hub: [[ideas/180dc/workshops/index]]. Project: [[projects/180dc]].

## Design intent (stated by Manuel)
- **Engaging first.** Short, quick, hands-on. Members should leave wanting more, and actually learn.
- **The live case is the key part.** Teaching exists to feed it.
- **Don't over-engineer.** Big point. The research behind this (see Sources) is far heavier than the session; take only what juniors can use in the room.
- AI research is taught as *research you can defend*: no fabrication, critical thinking kept, value over polish.
- The planted-error "fabrication brief" exercise was considered and **dropped** by Manuel (2026-10-07).

## The 2-hour block structure

| Time | Block | Min |
|---|---|---|
| 0:00–0:30 | Frameworks (the five below, taught as one chain) | 30 |
| 0:30–0:40 | How AI actually works, and the rules against making things up | 10 |
| 0:40–0:50 | Live case: frame the problem, no AI (issue tree + day-one hypothesis) | 10 |
| 0:50–1:00 | Research with one chat | 10 |
| 1:00–1:10 | Check it in a fresh, separate chat; open the decisive sources by hand | 10 |
| 1:10–1:20 | Consolidate: so-what each fact, agree the answer | 10 |
| 1:20–1:35 | Build the slide (ghost-deck title first) | 15 |
| 1:35–1:55 | Pitches, 3 minutes each | 20 |
| 1:55–2:00 | Debrief | 5 |

**Open constraint: pitch time depends on team count.** 20 minutes holds about 5 teams at 3 minutes with no Q&A; 8 teams need about 30. Recommended fix: every team builds a slide, 4 or 5 are drawn at random to pitch (keeps the session at 2 hours and keeps every team sharp). Alternatives: trim frameworks to 25 and consolidation to 5, or run pitches in two parallel rooms. **Expected headcount is still unknown.**

Cheap engagement add-ons (no extra time):
- After each pitch, one question: "Which number on your slide would you bet on, and where's the source?" It puts the no-fabrication rule on stage.
- End the debrief with a real near-miss from the session (a team that almost used an unchecked number) instead of a planted example.

### The 10-minute AI block: what goes in it
- One mental model: the model only reads its desk and writes text; a tool call is a note the app runs (from the AMSA AI Academy L3 deck).
- Four rules: open every source you cite; never invent a number, quote or source; mark anything you couldn't open as unverified; keep fact, forecast and your own inference separate.
- Walk the research prompt line by line, saying why each line exists. That is the useful part of "how prompts and agents work".
- The hook: in the BCG/HBS study of 758 consultants, AI made people faster on suitable tasks but made wrong answers on a hard task *more persuasive* (Dell'Acqua et al., Organization Science 2026, https://doi.org/10.1287/orsc.2025.21838).

### Live-case setup decisions
- **Two chats, not three agents.** One research chat, one fresh checker chat. The research files' own reviews found no evidence that three contexts beat one, and every handoff costs time. Splitting work between people in a team is fine; that is roles, not agent architecture.
- **Lightweight claim log, 4 columns:** claim | source and page | what it does NOT prove | checked by a human (y/n).
- **Case fit:** the tested case (fictional Northstar Grocers, £10m UK grocery capex) is corporate strategy. Recommended: swap to a fictional 180-shaped case (e.g. a social enterprise choosing between two revenue-growth options) and re-run the prompt test once. Not yet decided.
- **Must do before the session:** test the prompts on the free ChatGPT/Claude accounts juniors actually have (the pilot ran in Codex with subagents, not on a free account), and prepare a source-pack fallback for search or usage limits.
- **Pitch grading:** evidence and reasoning over polish; every number must have a source the presenter can open live; each team names one claim it rejected and why.

## The five frameworks (to review)
Taught in this order as one chain, from the question to the pitch. Suggested split of the 30 minutes: issue tree + hypothesis 12, so-what 6, ghost deck + pyramid 10, 2 to show how the chain runs through the case. Use the case itself as the running example so the framework block doubles as the case briefing.

| # | Framework | What it is | When a 180 consultant uses it | Live-case step |
|---|---|---|---|---|
| 1 | **Issue tree (MECE)** | Break the client question into sub-questions that don't overlap and together cover everything. | Week one of every project: scoping, splitting work across the team, spotting what the brief missed. | Frame |
| 2 | **Day-one hypothesis** | Write your best-guess answer before researching, then look for evidence that could prove it wrong. | Stops "boiling the ocean"; gives research a direction and makes AI prompts sharper. | Frame, research |
| 3 | **"So what?" test** | For every fact, ask what it means for this client until you reach an implication; facts with no so-what get cut. | Turning research into insight; the most common gap in junior decks. | Check, consolidate |
| 4 | **Ghost deck** | Write every slide title first as a full-sentence conclusion; read the titles alone to test the story. | Planning every deliverable; finds missing logic early. | Build the slide |
| 5 | **Pyramid Principle** | Answer first, then three supporting arguments, then evidence. The ghost deck is the pyramid applied to a whole deck. | Every slide, email and client call. | Pitch |

Mention in one sentence each, don't teach:
- **Driver tree:** an issue tree with numbers (e.g. donations = donors x gift size x retention). Useful for market sizing and fundraising projects.
- **Impact vs effort matrix:** for ranking final recommendations, since 180 clients have little capacity.

Why this set: it is one chain rather than five tools, and it feeds the AI deliverable reviewer. The reviewer's criteria (action titles, governing insight, recommendation specificity, evidence sourcing, actionability) are produced by the ghost deck, the so-what test and the pyramid. Team leads learn the reviewer on 27 Oct; consultants learn what it rewards on 3 Nov.

Core sources (standard consulting canon): Barbara Minto, *The Pyramid Principle*; Ethan Rasiel, *The McKinsey Way*.

## Sources
- Research and prompt pilot for the AI-research block (read-only, outside the vault): `C:\Users\User\Desktop\180 deliverables\Consulting_AI_Research_Findings.md`, `AI_Consulting_Research_Lab.md`, `AI_Consulting_Research_Test_Log.md`, plus the two reviews (`Consulting_AI_First_Principles_Review.md`, `Consulting_AI_Overall_Review.md`), all dated 2026-10-07.
- Trainings announcement slides: `deliverables/180dc-ai-team/180dc-ai-dev-team-intro.pptx`.
