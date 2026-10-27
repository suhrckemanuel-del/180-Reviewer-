---
type: reference
date: 2026-06-18
tags: [180dc, multi-agent, research, decisions]
ai-first: true
sensitivity: internal
---

# Multi-agent problem-solving method

## For future Claude
Use this method for consequential, ambiguous 180DC problems where independent research, competing mechanisms, and adversarial review justify the extra time and tokens. For simple or reversible questions, use one strong agent and a quick test instead.

## 1. Frame

Create one stable problem brief:

- Observable problem, not the preferred solution
- Decision to be made
- Stakeholders and incentives
- Desired outcome and success measures
- Known facts, assumptions, disputes, and unknowns
- Constraints and non-negotiables
- Evidence standard
- Decision criteria
- Abandonment condition

Do not proceed if the problem is still too vague to evaluate solutions.

## 2. Diverge independently

Give the same sanitized brief to three or four isolated agents. Do not show them one another's initial answers.

- **Strategist:** diagnosis, systems view, long-term value
- **Operator:** workflow, feasibility, ownership, adoption
- **Researcher:** external evidence, benchmarks, comparable cases
- **Contrarian:** alternative diagnosis, minimal intervention, reasons not to build

Each returns a diagnosis, causal mechanism, proposal, evidence, assumptions, risks, cheapest useful test, and confidence.

Require materially different mechanisms, not cosmetic variations.

AI can cheaply search a broad option space, but volume is not the objective. The useful pattern is [[learning/concepts/ai-divergence-human-convergence]]: stabilize the problem and criteria first, generate distinct mechanisms, then let evidence and human judgment eliminate most outputs. See the worked external example in [[videos/from-3k-to-10k-ai-money-and-life-advice]].

## 3. Audit evidence

A fresh reviewer labels material claims:

- `verified` - supported by direct or primary evidence
- `plausible` - indirect support
- `hypothesis` - not yet verified
- `contradicted` - evidence points elsewhere

Record the source, date, applicability, limitations, and conflicting evidence. Consensus between agents is not external evidence.

## 4. Converge blindly

Remove model or author identity and compare options against the original criteria:

- Expected impact
- Evidence strength
- Feasibility
- Stakeholder fit
- Cost and reversibility
- Risk
- Learning value

Keep the strongest options plus one credible dissenting option. Do not select by majority vote alone.

## 5. Red-team

Use a fresh critic to identify:

- Hidden assumptions and counterfactual explanations
- Failure scenarios and second-order effects
- Stakeholder resistance and perverse incentives
- Optimistic cost, adoption, or capability estimates
- Evidence that would reverse the recommendation

For AI systems also test representative, edge, and adversarial cases; false positives and negatives; traceability; reviewer disagreement; escalation; human override; and appeal paths.

## 6. Revise once

Let proponents revise once using the evidence audit and structured objections. Avoid endless open debate.

## 7. Decide and pilot

The human owner chooses: pilot, combine, gather specified evidence, reject, or escalate.

Prefer the smallest reversible test that can distinguish the leading hypotheses. Fix the baseline, success threshold, guardrails, owner, and stop/adapt/scale rules before the test.

## Stop when

- Two rounds produce no new evidence, mechanism, or material risk.
- Agents are paraphrasing existing positions.
- A reversible pilot is cheaper than more analysis.
- One option clearly wins with no unresolved critical risk.
- Required evidence is unavailable and human judgment is needed.

Default maximum: one independent generation round, one red-team round, and one revision round.
