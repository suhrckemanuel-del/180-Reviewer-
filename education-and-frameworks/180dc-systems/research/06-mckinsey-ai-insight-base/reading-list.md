# Research Angle 6: The McKinsey AI Insight Base

Curated from McKinsey / QuantumBlack, September 2026. Purpose is twofold: (a) raise our own working
knowledge of where AI actually is, (b) give the 180DC tools a defensible insight spine so the guide
and the reviewer teach something a student cannot get from a prompt box.

Every article below is public. No McKinsey account is required to read any of them.

---

## The through-line

One finding organises the rest. In the August 2026 State of AI survey, **80% of respondents say AI
improved their individual productivity, and 50% say it helps them make better decisions — but the
share of organisations attributing any EBIT impact to AI has not moved in a year (37%), and the
"high performer" group is flat at 6% of respondents.**

The gap between personal gain and institutional gain is the whole game. McKinsey's own read of what
separates the 6%: they **redesign the workflow rather than inserting AI into the existing one**
(73% of high performers report fundamental workflow redesign, vs 25% of everyone else).

For us this is the argument for the reviewer's shape. A tool that bolts feedback onto the existing
"student makes deck, team lead reads it the night before" workflow will reproduce the same 80/37
split: individual students feel faster, chapter output does not improve. The tool has to change the
sequence of the review, not just speed up a step in it.

---

## Read these three first (about 70 min total)

### 1. The state of AI in 2026: On the road to ROI
Tinkoff, Van der Veken, Chui — 25 Aug 2026 | Survey, 31pp | ~25 min
https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai

The baseline numbers, and the most citeable single source on this list.

What to take:
- 80% individual productivity / 37% EBIT / 6% high performers, flat year on year.
- 44% of organisations now scaling AI enterprise-wide, up from 38%.
- Large orgs scaling agents 40% (up from 27%); smaller orgs flat at 22%. The gap is widening —
  relevant to the affordable-tooling positioning.
- **32% have decided against buying a software product because they could build it in-house with
  coding agents.** That is us. It is also the strongest external validation of the whole 180DC AI
  build programme, and worth quoting in the pitch.
- About 20% report AI operating cost (tokens) now constrains usage. Cost discipline is a real
  design constraint, not premature optimisation.
- Workforce: last year 32% expected AI-driven headcount decline; 14% actually saw one. Useful
  calibration whenever someone in a chapter claims AI is about to eliminate junior consulting.

Use it in: the guide's opening, the pitch deck, and anywhere we need a defensible "where AI actually
is" slide.

### 2. Seizing the agentic AI advantage
Sukharevsky, Kerr, Hjartar et al — 12 Jun 2025 | Report | ~25 min
https://www.mckinsey.com/capabilities/quantumblack/our-insights/seizing-the-agentic-ai-advantage

The conceptual frame behind finding 1: the **gen AI paradox**. Horizontal use cases (copilots,
chatbots) scale fast but spread their benefit too thin to show up in earnings; vertical,
function-specific use cases carry the real impact but die in pilot.

What to take:
- The horizontal/vertical split is the cleanest way to explain why "everyone uses ChatGPT" and
  "nothing measurably improved" are both true at once.
- Their prescription: scattered initiatives to programmes, use cases to whole processes, siloed AI
  teams to cross-functional squads, experiments to industrialised delivery.
- The "agentic mesh" architecture argument is enterprise-scale — skim it.

Use it in: the education track. This is the best available frame for teaching a student why their
personal AI productivity does not translate into a better chapter.

### 3. One year of agentic AI: six lessons from the people doing the work
Yee, Chui, Roberts — 11 Sep 2025 | Article | ~20 min
https://www.mckinsey.com/capabilities/quantumblack/our-insights/one-year-of-agentic-ai-six-lessons-from-the-people-doing-the-work

The most directly useful build document here. The six lessons:

1. **It is not about the agent, it is about the workflow.** Map the process and the pain points first.
2. **Agents are not always the answer.** Low-variance, high-standardisation work is better served by
   rules or a single prompt. Reserve agents for high-variance, low-standardisation work.
3. **Stop "AI slop": invest in evals and build trust.** Onboard an agent like an employee — codify
   what good looks like, then test it. They cite task success rate, F1, retrieval accuracy. One bank
   reran tests whenever agent and human judgment diverged, and asked the agent "why" in succession.
4. **Make every step trackable.** One provider caught an accuracy drop immediately because
   observability covered each step rather than only the output.
5. **The best use case is the reuse case.** Shared validated components, not a new stack per workflow.
6. **Humans remain essential, but roles change.** Oversight, edge cases, judgment, compliance.

What to take: lessons 2, 3 and 5 are where we are weakest. Lesson 2 is a direct challenge to any
instinct to make the reviewer more agentic than it needs to be — deck review is genuinely
high-variance, which argues for keeping it, but the question should be asked explicitly per feature
rather than assumed. Lesson 3 names a discipline our labelling and baseline work already implements;
adopting their vocabulary (evals, task success rate) makes that work legible to outsiders.

---

## The one that matters most for 180DC

### 4. Building expertise in the age of AI: Who trains the next generation?
Bryan Hancock — 13 Jul 2026 | McKinsey Quarterly | ~20 min
https://www.mckinsey.com/capabilities/people-and-organization/our-insights/building-expertise-in-the-age-of-ai-who-trains-the-next-generation

Read this one closely. It is about exactly our problem: AI automates the routine entry-level tasks
through which judgment was historically built, producing an **"AI drag" on early-career people**
while senior people get an AI boost.

Their answer is the **"answer key" model**: the junior attempts the work first, AI grades it, and the
manager discusses the difference. **That is the typed-attempt gate in our student mode**, published
by McKinsey Quarterly and arrived at independently. It corroborates research angle 05 (feedback
teaches only when the consultant attempts first — the generation effect) from a completely separate
direction, and it means the design decision can be defended to a chapter president with a Quarterly
citation rather than a psychology paper.

Two things in it we do not currently do, both worth building:

- **Measure judgment formation as the narrowing gap between the student's own attempt and the AI
  output over time.** We already capture the typed attempt and the model's findings. Storing both and
  scoring their convergence across a semester turns the reviewer from a feedback tool into a
  development-tracking instrument — and gives a chapter something to report that no prompt box can.
- **The preceptor model**: a senior member formally paired with a junior, who observes *how the junior
  interacts with the AI*, not just the output. Suggests a team-lead view showing the student's attempt
  next to the model's, which is a small change to the two-mode page.

Also in it: hire and develop for judgment, curiosity and adaptability over tool fluency; expand
sandboxed simulation. It cites Matt Beane, *The Skill Code*, as further reading.

---

## For building the tools

### 5. What McKinsey learned while creating its generative AI platform (Lilli)
Erik Roth with Lareina Yee — 25 Nov 2024 | Podcast transcript, 6pp | ~12 min
https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/what-mckinsey-learned-while-creating-its-generative-ai-platform

The closest published analogue to what we are doing: a professional-services firm building its own AI
layer on its own accumulated judgment. Short, concrete, unusually candid.

What to take:
- Started with **four people** and four durable domains, and stayed anchored to them. Now 150+.
- **Every single item in the development pipeline is tied to a specific user problem.** Nothing enters
  the backlog without one. A rule we could adopt verbatim.
- Launched to only **2,500 colleagues** deliberately: you can build faster than you can learn, because
  building is coding and learning is waiting for users. Argues for the pilot being small and real
  rather than broad — directly relevant to the pilot that is next after the comparator gate fix.
- Alpha / beta / LilliX experimental tiers.
- Their **most-used agent is "Tone of Voice"**, which turns messy prose into McKinsey-quality writing,
  and its biggest beneficiaries are non-native English speakers. Remarkably close to our reviewer's
  communication-clarity axis, and evidence that the clarity half of the two-axis thesis is where the
  adoption actually is.
- Not a plain RAG instance: an orchestration layer over a mix of large and small models.

Companion case study (5 min, skim):
https://www.mckinsey.com/capabilities/tech-and-ai/how-we-help-clients/rewiring-the-way-mckinsey-works-with-lilli

### 6. Is that AI agent worth it? Agentic economics and the modern operating model
QuantumBlack, 2026 | ~15 min
https://www.mckinsey.com/capabilities/quantumblack/our-insights/is-that-ai-agent-worth-it-agentic-economics-and-the-modern-operating-model

Token and unit economics: linking AI spend to business outcomes rather than counting tokens. Matters
because the free-tier chat-native path exists precisely to dodge a cost constraint that the State of
AI survey now confirms is real for one organisation in five. More technical companion:
https://www.mckinsey.com/capabilities/quantumblack/our-insights/cost-versus-value-managing-agentic-ai-system-performance

---

## Optional, later

- **From adoption to impact: three horizons of AI transformation** (Quarterly) — staged model, useful
  if we write a chapter-level AI adoption roadmap.
  https://www.mckinsey.com/capabilities/people-and-organization/our-insights/from-adoption-to-impact-three-horizons-of-ai-transformation
- **State of AI trust in 2026: shifting to the agentic era** (blog) — pairs with the trust-boundary
  work in v2/22-trust-boundary.md.
  https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/tech-forward/state-of-ai-trust-in-2026-shifting-to-the-agentic-era
- **What is an AI agent?** (explainer) — the definition to hand a student who has never met the term.
  https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-an-ai-agent
- **An executive's guide to AI** (interactive) — foundations, if the basics feel shaky.
  https://www.mckinsey.com/capabilities/quantumblack/our-insights/an-executives-guide-to-ai

---

## Source discipline

All figures above are as published by McKinsey and are attributed inline with article and date. They
have NOT been through the process in verification-report.md. The State of AI figures are self-reported
survey data (n=1,719, 97 nations, fielded 4 May to 8 Jun 2026, weighted by each respondent nation's
contribution to global GDP) — describe them as "respondents report", never as measured outcomes.
Before any of these numbers enters a client-facing or pitch deliverable, run it through the same check
as the rest of the evidence base.

---

## Beyond McKinsey: two sources that constrain the design

Added 2026-09-18, while mapping the shared-corpus architecture
(tools/quality-reviewer/v2/28-shared-corpus.md). Neither is McKinsey and both are load-bearing.

### 7. What's your strategy for managing knowledge?
Morten Hansen, Nitin Nohria, Thomas Tierney — Harvard Business Review, March/April 1999 | ~20 min
https://www.library.hbs.edu/working-knowledge/whats-your-strategy-for-managing-knowledge

The foundational study of this exact question in this exact industry, and still the sharpest.
Two strategies: **codification** (people-to-documents; knowledge extracted from the person, made
independent of them, reused at scale — Ernst & Young, Andersen) and **personalization** (dialogue
and networks; documents tell you who to call, not what to copy — McKinsey, Bain, BCG).

The finding that matters: effective firms pick one and use the other in a supporting role.
Pursuing both equally "can quickly undermine a business." And codification is expensive — Ernst &
Young ran a 250-person Center for Business Knowledge plus a codifier in each of 40 practice areas.

Why it binds us: 180DC does bespoke work with people who are here to learn, which is the
personalization end twice over, and we have volunteers on three-year turnover rather than 250
librarians. So any deliverable corpus we build has to feed the evaluator, never the student. The
moment a student can browse past decks for a shape to copy, we have bought the codification
strategy we cannot staff and sold the teaching mandate that justifies the tool.

### 8. The Impact of Generative AI on Critical Thinking
Lee, Tankelevitch, Sarkar, Wilson et al. (Microsoft Research and Carnegie Mellon) — CHI 2025 | ~30 min
https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/
PDF: https://www.microsoft.com/en-us/research/wp-content/uploads/2025/01/lee_2025_ai_critical_thinking_survey.pdf

Survey of 319 knowledge workers, 936 first-hand task examples. The empirical backing for the
"without sacrificing critical thinking" half of everything we build.

What to take:
- **Higher confidence in the AI predicts less critical thinking; higher confidence in yourself
  predicts more.** Confidence in AI is the strongest coefficient in their model (-0.69, p<0.001).
  This is the single most design-relevant result in the paper: the target variable is the
  student's confidence in themselves, not their trust in the tool.
- GenAI shifts the effort rather than removing it — information gathering becomes verification,
  problem solving becomes response integration, execution becomes stewardship.
- 69 to 79 percent of examples report less effort across the Bloom categories.
- **Users with AI produce a less diverse set of outcomes for the same task.** Homogenisation is
  measurable and it is what a shared calibration corpus would accelerate.
- Named inhibitors: no time, no incentive where critical thinking is not seen as part of the role,
  and lacking the skill to inspect and steer output.

Note this is self-reported perception, not measured performance — describe it that way. Pair it
with Dell'Acqua et al. (jagged frontier) in research angle 05, which measures output instead.
