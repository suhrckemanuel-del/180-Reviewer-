# AI research for consulting: evidence, human judgment, and a teachable workflow

Research date: 7 October 2026. Prepared for a workshop that helps consultants do better research while retaining ownership of analysis and recommendations.

## Assessment

This is applicable to consulting. The strongest initial use case is producing a source-checkable evidence brief for an engagement team. AI can accelerate finding, extracting, organizing, and challenging information. The consultant still defines the client problem, evaluates whether evidence transfers to the client, develops commercial assumptions, obtains missing primary evidence, and decides what to recommend.

Our proposed three-context exercise reflects several publicly documented practices, but it is our teaching design. No source below establishes that MBB routinely uses exactly this three-agent arrangement, that it is superior to one well-run assistant, or that it protects jobs. Employment outcomes depend on management choices. A capacity-building workshop should explicitly reinvest saved effort in deeper analysis, client conversations, and junior development.

Evidence categories: **documented firm practice** means the organization describes an actual tool or workflow; **experiment** means a studied task under specific conditions; **our proposal** means a design recommendation requiring local validation. Firm pages are primary evidence of what organizations publicly describe, rather than independent proof of performance.

## What firms actually document

### McKinsey: find knowledge and the people behind it

**Documented practice.** Lilli searches curated knowledge, summarizes relevant material, links back to sources, and identifies experts. McKinsey describes content stewards who check quality and prepare material for reuse. Its implementation account reports colleague estimates of up to 30% time savings in knowledge search and synthesis; this is a firm-reported result, not a promised workshop outcome. [Lilli launch](https://www.mckinsey.com/about-us/new-at-mckinsey-blog/meet-lilli-our-generative-ai-tool); [implementation account](https://www.mckinsey.com/capabilities/tech-and-ai/how-we-help-clients/rewiring-the-way-mckinsey-works-with-lilli).

**Workshop implication, our inference.** Teach consultants to use an evidence search to locate the next expert and the next question. A useful output includes both documentary findings and a list of issues requiring client or specialist input. A public chatbot does not reproduce McKinsey's curated knowledge base, expert network, or access controls.

### Bain: automate specific research-adjacent tasks and spread employee-built tools

**Documented practice.** Bain's October 2024 account describes ChatGPT Enterprise pilots for generating Python for data analysis and automating Excel work, then an internal rollout, task-specific GPTs, employee innovation, training, and a deployment playbook. It also describes Answer Copilot accessing knowledge from nonconfidential partner email exchanges and a due-diligence bot assisting analysis of data-room documents. The stated benefit is more consultant capacity for analyzing and applying insights. [Bain deployment account](https://www.bain.com/insights/how-to-accelerate-progress-on-ai/).

**Workshop implication, our inference.** Start with a repeated bottleneck a consultant recognizes, such as extracting comparable metrics from annual reports. Have the person who understands the analysis specify acceptable output and check the result. Do not make autonomous strategy generation the initial exercise.

### BCG: task suitability and expertise matter

**Experiment, rather than a description of all current internal practice.** The preregistered study with 758 BCG consultants used GPT-4 and realistic consulting tasks. On tasks within the studied model's capabilities, AI users completed 12.2% more tasks and finished 25.1% faster on average. On a deliberately difficult managerial task, the combined AI conditions were about 19 percentage points less likely to give the correct recommendation. Incorrect AI-assisted recommendations could still be more coherent and persuasive. The study was first circulated in 2023 and published in Organization Science in 2026. It does not benchmark today's models or our proposed workflow. [Published paper](https://doi.org/10.1287/orsc.2025.21838); [accessible paper](https://www.hbs.edu/ris/Publication%20Files/dell-acqua-et-al-2026-navigating-the-jagged-technological-frontier_5c589c8c-fbb5-458f-b285-c944746cd717.pdf).

A separate 2024 BCG experiment studied coding, predictive modeling, and checking statistical outputs. It found immediate task-performance gains but did not establish equivalent unaided learning; domain familiarity helped participants know what correct output should look like. [BCG study account](https://www.bcg.com/publications/2024/gen-ai-increases-productivity-and-expands-capabilities).

**Workshop implication, our inference.** Grade correctness separately from persuasive writing. Preserve an unaided exercise in which learners explain a metric and critique an inference. AI-assisted completion is not the same outcome as acquiring consulting skill.

### Deloitte: research assistance in an approved environment

**Documented practice.** Deloitte describes PairD supporting research, content summarization, and coding in its own environment, with an explicit aim to support human insight and talent. [Deloitte account](https://www.deloitte.com/uk/en/about/story/impact/pairing-deloitte-human-insights-with-ai-technology.html).

**Workshop implication, our inference.** Use public or fictional information in the training demonstration. Real engagement material belongs in the firm's approved environment, subject to its actual policies.

### Gartner and Forrester: AI access to research, with routes to human expertise

**Documented products.** AskGartner draws on Gartner research and supplies citations and links to the underlying material. This is a client-facing access tool, not evidence of how every Gartner analyst creates research. [AskGartner FAQ](https://www.gartner.com/en/products/ask-gartner-faqs).

Forrester AI, previously Izola, provides source-linked access to proprietary research. AI Access Plus also offers analyst inquiry sessions for interpretation and validation. [Forrester AI Access](https://www.forrester.com/research/ai-access/).

**Workshop implication, our inference.** Separate getting an answer from assessing its fit. Teach learners to bring a sharper question to an expert after the AI has helped them understand the evidence and gaps.

### Kantar: a particularly clear account of human critical thinking

**Documented practice.** KAiA for Qual helps organize material, summarize transcripts, explore hypotheses, and develop narrative starting points. Kantar describes analysts adding context from first-hand respondent interactions, including nonverbal reactions absent from a transcript. Another account emphasizes human checks of qualitative output. [KAiA workflow](https://www.kantar.com/Inspiration/Agile-market-research/where-human-imagination-meets-AI-scale); [qualitative quality practices](https://www.kantar.com/north-america/Inspiration/Agile-market-research/AI-in-Qualitative-Research-5-essential-practices-for-quality-at-scale).

**Workshop implication, our inference.** AI can suggest a theme; the researcher assesses whether it fits what happened, whether a disconfirming case exists, and whether the sample supports its scope. Frequency of a theme in qualitative interviews is not automatically population prevalence.

### Ipsos: validate against people and measured reality

**Documented principles and methods.** Ipsos states that human experts verify AI-derived findings. Its March 2026 paper introduction warns that treating synthetic observations as ordinary independent human data can create misleading confidence. [Ipsos AI approach](https://www.ipsos.com/en/ai); [synthetic-confidence discussion](https://www.ipsos.com/en/calibrating-synthetic-confidence).

**Workshop implication, our inference.** Simulated customers can suggest interview questions or hypotheses. Do not present their generated responses as observed demand. Evidence quality depends on its origin and validation, rather than the apparent size of the generated dataset.

## How the consultant applies critical thinking

Our operational teaching standard is a chain from question to evidence to implication:

| Stage | AI assistance | Consultant action that must remain visible |
|---|---|---|
| Frame | Suggest subquestions and alternative explanations | Specify the decision, options, constraints, and what would change the decision |
| Find | Locate documents and candidate facts | Judge relevance, authority, coverage, and who is missing |
| Extract | Produce comparable claims and source locations | Check definitions, periods, units, denominators, and original context |
| Interpret | Suggest themes, explanations, and contradictions | Separate fact from inference; test causality and transfer to this client |
| Challenge | Identify counterevidence and missing information | Decide which objections matter and commission interviews or analysis |
| Recommend | Help organize an evidence-backed argument | Own assumptions, economics, trade-offs, recommendation, and communication |

For every material implication ask: What exactly does the source establish? What additional assumption connects it to the client decision? How could that assumption be tested? What would change our conclusion?

## The practical three-context exercise

Three participants can each use their own account, or one participant can use three separate fresh chats. The lesson requires three distinct briefs, rather than three registrations. Different accounts do not by themselves create independent expertise or independent evidence. Use public sources for live research, or a prepared source pack when search and usage limits would disrupt the class.

**Case:** fictional Northstar Grocers has £10m to invest over two years. Should it open convenience shops, improve its existing stores, or stage investment? Public research can inform market conditions and peer practices. It cannot determine Northstar's returns without store economics, local catchments, execution costs, and customer evidence.

Before researching, agree the decision criterion and owner. For this case, compare incremental cash flows, capital needs, risk, opportunity cost, and delivery capacity over an explicit horizon. Request client contribution margins, capex and operating costs, catchment demand, cannibalization, ramp-up, and capacity constraints. The teaching case can supply clearly fictional numbers for a break-even or sensitivity exercise. Permit an additional option or reframing if the initial three choices omit something important.

**Human setup, before any AI:** write the decision, three hypotheses, key assumptions, initial view, and disconfirming evidence to seek. Do not expose the initial preferred answer to the two discovery chats.

**Protect learning:** each learner manually checks one decisive source and derives one metric before seeing the AI extraction. After the exercise, they explain the business implication and one rejected inference without AI. A reviewer checks that explanation. The assignment includes both what the team would do with the released time and how junior consultants still practice research; human authorship of a final paragraph alone is insufficient.

**Context A — external evidence researcher.** Find market and customer evidence. Produce no recommendation. Record material facts with original sources and limitations.

**Context B — commercial researcher.** Independently investigate peer practices and economic mechanisms: price, basket size, footfall, productivity, capital intensity, and execution constraints. Examine competing explanations; do not give a predetermined option a persuasive advocate.

**Context C — evidence auditor.** Receives the two claim ledgers and original source material, not a polished recommendation. Reopens sources, checks material claims, identifies reused source origins, and records conflicts and gaps. This agent can flag issues, but the human verifies the decisive evidence.

Audit coverage as well as accuracy: map findings to the decision questions and note missing options, inaccessible material, and disconfirming evidence not found. A ledger can contain only correct facts and still omit the decisive evidence. Keep a short search-and-omissions log rather than claiming exhaustive search.

Use the ledger: claim ID; factual claim; source URL/document; exact page/section/table; brief relevant excerpt; publication date and measured period; metric/unit/population; source limitations; proposed client implication; additional assumption; audit status. Confidence should describe evidence quality and assumptions, not an invented calibrated probability.

**Start small:** use one structured assistant when the question is narrow and the source pack is small. Add the independent commercial brief when it brings a distinct investigation, and add the audit context when material claims need inspection. Cap the classroom output at eight claims and timebox each handoff. Three contexts earn their place only if coverage or checking improves enough to justify their coordination and review costs.

The final combined ledger should also contain at most eight decision-critical claims, each with a named human owner. Retain a separate gaps log. That owner opens the decisive source and explains its implication; the AI audit status is a checking aid, not certification. Include a later unfamiliar case if claiming retained learning, and keep manager coaching and junior exposure to client or expert conversations in the learning plan.

## Reusable prompts

### Shared research instructions

You are assisting a consultant researching [decision] for [client context]. The evidence cutoff is [date]. Use only accessible material you can inspect; if using a supplied pack, stay within it. Prefer original evidence. Record the actual period and definition of every metric. Produce the claim ledger specified above, with a maximum of eight material claims. Separate observed facts, forecasts, inference, and unknowns. Map coverage to the decision questions; list source families searched, inaccessible material, disconfirming evidence sought, and consequential gaps. Identify conflicting evidence and missing client data. If a source cannot be inspected, mark it unverified. Multiple articles repeating one release count as one evidence origin. A successful output makes the consultant's next analytical step clearer. Do not make the investment recommendation.

### Context A addition

Investigate market and customer conditions. Search for evidence that would discriminate among the three investment options. Explain coverage gaps. Give a short list of primary research questions for the consultant to ask next.

### Context B addition

Investigate peer practices and the commercial mechanisms behind them independently of Context A. Test alternative explanations for reported growth or improvement. Identify which economics the consultant must obtain from the client before assessing returns.

### Context C addition

Audit each material claim against its original source. Mark supported, supported with qualification, contradicted, or unverifiable, and explain the reason. Check number, period, metric, scope, forecast status, and earliest accessible evidence origin. Check omissions against the decision questions as well as fidelity of selected claims. Separate source fidelity, measurement limitations, and client applicability. Distinguish a supported fact from an unsupported implication. Retain valid claims and useful qualified evidence. Produce a prioritized list for human inspection, then unresolved evidence gaps. Do not treat agreement among agents as verification.

## What to measure before claiming time savings

Compare manual research, one structured AI chat, and the three-context workflow using matched source packs and comparable tasks. Rotate assignment across participants to reduce learning and order effects. Count human setup, source checking, handoff, repair, synthesis, and unaided explanation time; record total person-time and elapsed time separately, including failed attempts. Record AI usage separately. Have a reviewer who does not know the condition score factual support, inference quality, coverage, and decision usefulness. Include an open-search task if the intended application involves discovering sources; a prepared pack alone does not test discovery.

Predeclare what constitutes a material error and the minimum useful output. Prefer time to an acceptable verified brief over time to first answer. Set a quality gate of no unresolved material error in the submitted brief; report remaining gaps explicitly. This is an instructional acceptance standard, not a claim that the system can guarantee zero errors.

An AI-only stress test can expose weaknesses. It cannot establish consultant productivity, learning, employment effects, or superiority to a simpler workflow.

## Completed two-agent review

After the research draft was complete, two agents received fresh contexts and reviewed it independently: one from first principles of evidence and decision quality; the other from engagement management, client usefulness, knowledge work, and junior development. Each inspected original sources and assessed the same eight selected statements. They did not consult one another's review.

Both retained statements 1, 3, and 5; classified 2, 4, and 6 as contradicted; and classified 7 and 8 as unsupported. They recommended a bounded pilot. Their main improvements are now included: coverage checking, a stronger client-economics bridge, a combined ledger cap and human claim owners, total person-time measurement, optional rather than mandatory extra contexts, and explicit unaided learning and transfer checks.

This is an adversarial design and evidence review. The selected cases are not representative, the reviewers can share model blind spots, and agreement is not independent empirical validation. No measured speedup or workflow error rate was established.

Review files: [first-principles review](./Consulting_AI_First_Principles_Review.md), [overall consulting review](./Consulting_AI_Overall_Review.md), and [stress-test statements and results](./Consulting_AI_Research_Stress_Test.md).
