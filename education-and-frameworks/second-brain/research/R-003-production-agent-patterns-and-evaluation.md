---
type: research
id: R-003
date: 2026-08-19
updated: 2026-08-19
tags: [research, 180dc, agents, evaluation, mcp, ai-engineering]
ai-first: true
sensitivity: internal
confidence: high
status: partial
---

# R-003 — Production patterns for AI agent systems, and why they fail

## For future Claude
Practitioner brief on what actually works when building AI agent systems for analytical work, as of August 2026. Three findings drive everything downstream: workflows beat agents, evaluation is the real work, and reliability compounds multiplicatively so short chains beat long ones. The most important conclusion for 180DC is in Section 7 — a small organisation should build **context and evals**, not agents. Companion to [[ideas/180dc/research/R-002-consulting-ai-business-model-and-trust]]; feeds [[ideas/180dc/workshops/index]].

## Coverage note
One of four research lanes commissioned 2026-08-19. Two of four completed. See coverage gaps in [[ideas/180dc/research/R-002-consulting-ai-business-model-and-trust]].

---

## Headline judgments

1. **The field converged on "workflows first, agents last."** Anthropic and OpenAI both lead their official guidance with the same message: most production value comes from a single well-prompted call with good retrieval, not from an agent. Anthropic is explicit — start simple, evaluate comprehensively, add agentic systems only when simpler solutions fall short.
2. **Evaluation is the product work, not QA.** The most credible shipped-system writeup breaks effort down as 80% ordinary software engineering / 20% AI-specific — and of that 20%, 80% was evals. Roughly 16% of total effort on evaluation.
3. **The demo-to-production gap is arithmetic, not model capability.** Per-step reliability compounds multiplicatively.
4. **Retrieval orthodoxy flipped.** Vector RAG is no longer the default for agentic systems; tool-driven search is.

## 1 — The compounding reliability problem (confidence: high, this is arithmetic)

If each step succeeds independently with probability p, an n-step task succeeds at p^n:

| Per-step reliability | 10-step task |
|---|---|
| 95% | **59%** |
| 90% | **35%** |
| 85% | **20%** |

A three-step demo hides this completely; a twenty-step production workflow cannot. This single fact explains most of the demo-production gap, and argues for shorter chains, verification between steps, and hard guardrails far more than for better models.

**Related metric — pass^k, not pass@1.** Sierra's τ-bench introduced pass^k: the fraction of k independent attempts where *all* succeed. Claude 3.5 Sonnet scored **69.2% pass@1 → 46.2% pass^4** on retail; **46.0% → 22.5%** on airline. GPT-4o dropped from under 50% pass@1 to roughly **25% at pass^8**. Headline benchmarks describe best-case single attempts; users experience pass^k.

Source: https://sierra.ai/blog/benchmarking-ai-agents

## 2 — Agent patterns and when each applies (confidence: high, primary source)

From Anthropic's *Building Effective Agents*:

| Pattern | Use when | Failure mode |
|---|---|---|
| **Prompt chaining** | Fixed subtasks; trade latency for accuracy | Errors propagate silently down the chain |
| **Routing** | Distinct input categories need different handling | Router misclassification silently degrades everything downstream |
| **Parallelization** | Independent subtasks, or multiple perspectives wanted | Cost multiplies; voting hides disagreement rather than surfacing it |
| **Orchestrator-workers** | Subtasks unpredictable in advance | Workers make conflicting implicit decisions |
| **Evaluator-optimizer** | Clear criteria exist *and* model can articulate feedback | Degenerates into self-congratulatory loops when criteria are fuzzy — exactly the analytical-output case |

**Practical rule:** if you can predict when control should return to deterministic code, encode that in code. Do not let the model decide what to do next when you already know.

Source: https://www.anthropic.com/engineering/building-effective-agents

## 3 — Subagents: the teachable rule (confidence: high, both sides of a genuine disagreement)

**For:** Anthropic's multi-agent research system (Opus lead + Sonnet subagents) beat single-agent Opus by **90.2%** on internal research evals. Token usage alone explained **80% of performance variance**.

**Against:** Cognition's *Don't Build Multi-Agents* — actions carry implicit decisions, and parallel subagents that cannot see each other's decisions produce work that does not fit together. Claude Code deliberately avoids parallel subagents doing independent work; subagents answer questions, they do not build things.

**The reconciliation both sides accept:**

> **Fan out to gather. Stay single-threaded to synthesise.**

Multi-agent works for **breadth-first, read-only, decomposable** tasks — search, research, gathering evidence from many sources. It fails for **write-heavy, sequential, interdependent** tasks where coherence matters. Anthropic states the same: poor fit for tasks requiring shared context, many inter-agent dependencies, or sequential coordinated work.

**Consulting translation, teachable directly:** use subagents to research a market from ten angles at once; never use them to write three sections of the same deck.

**Cost:** agents use ~4x the tokens of a chat interaction; multi-agent ~15x. On a consumer plan that is a real constraint — knowing when *not* to fan out is part of the skill.

Sources: https://www.anthropic.com/engineering/multi-agent-research-system | https://cognition.com/blog/dont-build-multi-agents

## 4 — Context management determines quality (confidence: high)

- **Context rot is measured, not folklore.** Chroma tested 18 frontier models: reliability degrades as input length grows *even on trivial retrieval tasks*, well before the window is full. Counterintuitively, all 18 performed *better* on shuffled haystacks than on logically coherent documents.
- **Treat attention as a budget** — find the smallest set of high-signal tokens.
- **Three long-horizon techniques:** compaction (summarise before limits, preserving decisions and open questions); structured note-taking (persistent external memory across context resets); sub-agent isolation (clean window each, return 1–2k token summaries).
- **Failure mode:** teams stuff everything into context "just in case," then blame the model. The fix is subtractive.

Sources: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | https://www.trychroma.com/research/context-rot

## 5 — Evaluation methodology (confidence: high, strongest practitioner consensus)

Primary source: Hamel Husain's evals writing.

**The process:**
1. **Error analysis before infrastructure.** Most-skipped, most-important. Review 20–50 outputs after any significant change; **100+ traces** for a proper cycle.
2. **Open coding** — a domain expert writes free-form notes on each trace. No predefined categories; categories are the *output*.
3. **Axial coding** — group into failure categories, count occurrences. Now you know what to fix, ranked.
4. **Stop at saturation** — ~20 consecutive traces yielding no new category, after reviewing at least 100.
5. **Fix the top category** — usually a prompt change, not an architecture change.
6. **Only then automate** — write evaluators for failures you *found*, not ones you *imagined*.

**Design rules:**
- **Binary pass/fail, never 1–5 Likert.** Forces clear thinking, smaller samples for significance, stops people hiding uncertainty in "3". Pair each judgment with a written critique.
- **One "benevolent dictator" annotator** beats a committee.
- **Validate an LLM judge like a classifier** — 100+ hand labels, held-out test set, measure TPR and TNR. An unvalidated judge is a random number generator with good prose.
- **Reject prefab metrics** — "helpfulness score", BERTScore, ROUGE manufacture false confidence.
- **Build a custom data viewer** — repeatedly cited as ~10x faster iteration than off-the-shelf platforms.

**For fuzzy analytical output — the hardest case, and directly relevant to the Quality Reviewer:**
- **Decompose fuzzy into checkable.** "Is this a good market analysis" is unevaluable. "Does every numeric claim cite a retrieved source?" / "Are the comparables from the stated sector?" / "Does the conclusion follow from the stated evidence?" are binary and checkable.
- **Verification-first tool design.** Instead of asking the model to *explain* what was wrong, ask it to *fix it* in an isolated context — success/failure becomes an objective signal.
- **Citation and grounding checks are cheap and high-yield.**
- **Keep humans on source quality.** Anthropic's human testers caught agents systematically preferring SEO content farms over authoritative primary sources. No automated judge flagged it.
- **Start with ~20 real queries.** Anthropic's own starting point.

Sources: https://hamel.dev/blog/posts/evals-faq/ | https://hamel.dev/blog/posts/field-guide/

## 6 — Security: the lethal trifecta (confidence: high)

Simon Willison's model. An agent is exploitable when it simultaneously has:

1. **Access to private data**
2. **Exposure to untrusted content**
3. **An exfiltration vector** (any outward communication)

Remove any one leg and the attack fails. MCP is dangerous precisely because it makes mixing and matching tools trivial, so users assemble all three legs without noticing. Documented: Atlassian's MCP server allowed prompt injection via public issues to steal private data.

**Tool poisoning:** malicious instructions embedded in MCP *tool descriptions* — invisible to the user, fully visible to the model.

**Controls:** treat every tool result as untrusted input; audit and pin tool definitions; never connect an agent directly to a production database; enumerate the trifecta for every deployed configuration and break a leg deliberately.

Sources: https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ | https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks

## 7 — Build vs buy for a small organisation (confidence: medium — vendor-dominated topic)

**Build only where all of these hold:**
1. The workflow is **core and differentiating**. If a vendor sells it, buy it.
2. You have **domain experts who will actually annotate traces**. Non-negotiable, and the constraint that kills most small-org builds — not engineering capacity. Someone must read 100 outputs weekly, forever.
3. The task has a **verifiable output**. If you cannot tell whether the answer was right, you cannot improve the system and should not automate it.
4. You can live with **maintenance in perpetuity**.

**The conclusion that matters most for 180DC:**

> Do not build agents — build **context and evals**. A well-organised corpus, good tool definitions, documented failure modes, and 50 labelled examples of good vs bad output are portable across every vendor and model generation. That asset compounds. A custom agent framework depreciates. Buy the harness, own the evaluation.

This directly supports the shared-corpus decision in [[ideas/180dc/workshops/index]] and validates the existing Quality Reviewer approach in [[projects/180dc]] — a critique tool with a golden set is exactly the "context and evals" asset, not an agent build.

## 8 — Why agent projects fail (confidence: high on mechanisms, low on the headline statistic)

**Discount the famous number.** MIT Project NANDA's "95% of GenAI pilots delivered no measurable P&L impact" rests on 52 executive interviews and 153 survey responses, not peer reviewed. Directional signal, not evidence.

**Failure modes that hold up:**
1. **Compounding error** — Section 1.
2. **Confident wrongness with no verification surface.** "The worst part about hallucinations is that the model is very confident about being right."
3. **The verification trap** — agents trust a tool's *reported* status rather than the actual outcome.
4. **Silent context corruption** — when a tool returns unexpected data, the model improvises around it and continues with corrupted state. It rarely stops.
5. **Poorly-specified tool schemas.** Anthropic's heuristic: if your engineers cannot decide which of two tools applies, the agent definitely cannot. They spend *more* time on tool definitions than on prompts.
6. **No traceability** — POCs stall because nobody can reconstruct why the agent did what it did.
7. **Unbounded scope** — agents that will attempt anything fail at everything.
8. **Tools-first mindset** — buying observability platforms before reading 100 of your own outputs.

Source: https://threedots.tech/post/ai-agent-that-lies/

## 9 — Sequenced recommendation (confidence: high, synthesised)

1. **Write down 20 real queries** — actual ones from actual work.
2. **Do them with a single well-prompted call plus manual context.** This is your baseline and it is often good enough.
3. **Read 100 outputs.** Open-code, axial-code, rank failure categories. They will not be what you expected.
4. **Fix the top category with a prompt or context change.** Re-measure. Repeat until prompts stop helping.
5. **Only now add tools** — one at a time, each with its own eval.
6. **Only now consider decomposition** — fan-out-for-gathering, single-thread-for-synthesis.
7. **Build the LLM judge last**, after 100+ human labels.
8. **Instrument tracing from day one** anyway.

The pattern across every credible source: success is determined by error analysis, scoping, tool clarity, context discipline, and data quality. The architecture is the easy part, and it is the part everyone writes about.

## Source quality
**Primary/high confidence:** Anthropic engineering blog, Hamel Husain, Sierra τ-bench, Chroma, Cognition, Three Dots Labs, OpenAI's practical guide, Simon Willison, Invariant Labs.
**Directional only:** MCP latency figures, build-vs-buy costs, most "why agents fail" listicles — vendor and SEO dominated.
**Notable gap:** very few honest, detailed postmortems from named teams exist. The genre is overwhelmingly success stories.

## Related
- [[ideas/180dc/workshops/index]] — the teaching programme
- [[ideas/180dc/research/R-002-consulting-ai-business-model-and-trust]] — the market-side companion
- [[ideas/agent-mcp-tool-watchlist]] — Manuel's MCP tool assessments
- [[projects/180dc]] — Quality Reviewer and current priorities
