# First-principles review: consulting AI research teaching

Review date: 7 October 2026. Independent qualitative review of Consulting_AI_Research_Findings.md and its eight stress-test statements. No consultant experiment, productivity benchmark, or historical investment backtest was performed. This review did not consult the other reviewer’s conclusions.

## Verdict

Proceed with a workshop on evidence assessment and AI-assisted research, with the changes below. The design is applicable to consulting because it connects retrieval to an actual decision and makes the fact-to-implication bridge visible. Its value is conditional on whether consultants can verify decisive evidence, identify missing evidence, and explain their reasoning unaided. Three contexts are a useful teaching option, not an established productivity requirement. The documents correctly distinguish firm accounts, experimental evidence, and proposed pedagogy; retain that distinction.

A supported fact can still be irrelevant to the client. A source check can establish what a document says without establishing that its measurement is valid. A correct recommendation can arise from weak reasoning. Accordingly, grade source fidelity, evidence quality, transfer to the client, and decision reasoning separately.

## Primary-source checks and candidate classifications

Classification rule: supported means the wording is warranted by inspected evidence; qualified means useful but requires narrowed wording; contradicted means the claim conflicts with inspected evidence or its stated logical premise; unsupported means the evidence cannot establish it. Unsupported does not imply the opposite is proven.

| # | Classification | Correction and reason | Consulting consequence |
|---|---|---|---|
| 1 | Supported | McKinsey explicitly reports colleagues estimating up to 30% savings on searching and synthesizing knowledge. Keep the attribution, task scope, upper-bound wording, and workshop caveat. This is a firm report, not an independent measured effect for this exercise. [McKinsey, The Impact](https://www.mckinsey.com/capabilities/tech-and-ai/how-we-help-clients/rewiring-the-way-mckinsey-works-with-lilli). | Do not budget engagement savings from this number. |
| 2 | Contradicted | The experiment used GPT-4, 758 BCG consultants, and particular tasks. It reports 25.1% quicker completion on 18 tasks inside the studied capability frontier. For the separate managerial task, AI conditions were about 19 percentage points less likely to produce the correct answer. It cannot prove results for current tools across all work. [Original paper, abstract and section 4.2](https://www.hbs.edu/ris/Publication%20Files/dell-acqua-et-al-2026-navigating-the-jagged-technological-frontier_5c589c8c-fbb5-458f-b285-c944746cd717.pdf). | Task selection and correctness matter; impressive prose is insufficient. |
| 3 | Supported | Bain’s 2 October 2024 account documents pilots of ChatGPT Enterprise tools producing Python code for data analysis and automating complex Excel processes. It is evidence of described deployment, not a controlled performance comparison. [Bain, section 1](https://www.bain.com/insights/how-to-accelerate-progress-on-ai/). | Teach bounded workflows whose output a consultant can inspect. |
| 4 | Contradicted | Three accounts citing the same announcement reproduce one evidence origin. Independent searches may reveal omissions, but agreement does not create independent observations or validate the announcement. Different accounts also do not establish independent model errors. | Track source lineage; give one announcement one evidential weight. |
| 5 | Supported | Kantar explicitly describes the analyst adding contextual memory of first-hand respondent interactions, including nonverbal responses, to model interpretation. That documents a workflow, not universal proof that human interpretation is accurate. [Kantar, How Kantar Qual optimises AI-human collaboration, item 2](https://www.kantar.com/Inspiration/Agile-market-research/where-human-imagination-meets-AI-scale). | Preserve interviews and contextual interpretation, and test human interpretations against counterexamples. |
| 6 | Contradicted | The product is an access and synthesis service. Forrester explicitly states that experts produce its research using interviews, briefings and surveys, and offers analyst contact. This conflicts with the claim of entirely autonomous authorship. [Forrester, The Forrester AI Access Difference and Connect With The Humans Behind The Research](https://www.forrester.com/research/ai-access/). | Distinguish research creation from AI distribution and retrieval. |
| 7 | Unsupported | Market growth cannot establish Northstar’s marginal returns or the superiority of committing all £10m. Missing local demand, cannibalization, margins, capex, execution, and alternative-option economics prevent that conclusion. The fictional case supplies no investment evidence to close these gaps. | Record a research hypothesis and request client economics; do not convert a market trend into an allocation. |
| 8 | Unsupported | Human authorship at the last stage neither demonstrates practice in research judgment nor controls workforce decisions. The supplied sources do not establish either guarantee. A person could merely rewrite an AI conclusion. | Require observable reasoning practice and test learning; describe workforce protection as an organizational commitment if one exists. |

No statement falls in the qualified category under these exact wordings: the three legitimate statements already contain the needed scope, while the remaining statements make stronger propositions. This classification is not a model error rate: the candidates were deliberately selected and several are obvious overclaims.

## The three most material weaknesses

**1. Evidence auditing can miss the evidence that never enters the ledger.** Context C verifies A and B’s selected claims. It cannot infer all omitted counterevidence from those claims. An eight-claim cap helps verification effort but can hide a decisive omission. Add an audit of coverage against predeclared decision questions, options, and competing explanations. Distinguish verified quotation from independently validated observation. Firm pages are appropriate evidence of public descriptions, but remain interested sources for performance claims.

**2. Labor can move downstream without being saved.** Net human effort includes setup, retrieval, verification, deduplication, repair, handoffs, synthesis, and the required unaided explanation. More claims and more contexts can increase these costs; shorter waiting time is not necessarily lower total person-time. Three people working at once may improve elapsed time while increasing labor. Record both. Approve augmentation when an acceptable brief uses less total effort at comparable quality, or produces a material improvement in decision usefulness worth the additional effort. Do not require every useful exercise to be faster.

**3. Human sign-off is weaker than human capability.** The consultant retains formal ownership but may lose practice in finding evidence, making comparisons, calculating economics, and recognizing misleading framing. Reading a ledger and composing a conclusion do not demonstrate those abilities. Include unaided work on representative facts and inference before and after assistance, feedback, and a later unfamiliar transfer task. No immediate classroom check establishes durable learning or protects jobs.

## Three contexts versus one

The stages are necessary; the account count is not. One structured chat can research, maintain a ledger, and revisit its claims. A separate fresh audit context can reduce exposure to a persuasive draft and make challenge easier. Two discovery contexts may broaden coverage when tasks differ materially and run in parallel. However, they can share model tendencies, search rankings, source families, and blind spots. They are separate processes, not demonstrably independent experts.

Start the production workflow with one researcher and human source checking. Offer a fresh auditor for material uncertainty, then add the second discovery brief when it has a clear coverage job. For the classroom, retain three roles if the purpose is to teach provenance, division of research, and criticism. State that purpose. Compare the full arrangement with the simpler workflow before claiming a productivity advantage.

## Prompt design and concrete changes

The current prompts are substantially sound: the decision and cutoff are explicit; recommendation is deferred; accessible original sources, definitions, conflicts, assumptions, and unknowns are requested. Do not replace them with a persuasive advocate for a favored option. Keeping the initial human preference private from discovery is sensible, although framing and selected hypotheses can still bias the search.

Make five amendments:

1. Define the investment criterion and decision horizon before searching: incremental cash flows, implementation capacity, risk, and opportunity cost. Specify evidence that would distinguish each option and permit an additional option or reframing.
2. Add to A and B: “Map coverage to each decision question. List searched source families, material inaccessible sources, disconfirming evidence sought, and consequential gaps. Do not imply search exhaustiveness.”
3. Add to C: “Check omissions against the decision questions, not only fidelity of selected claims. Verify the earliest accessible evidence origin. Separate source fidelity, measurement limitations, and client applicability. A missing or unreadable source remains unverified.”
4. Cap the combined decision-critical ledger as well as each discovery output; preserve a short omissions log. Let the human choose which claims need exhaustive checking by decision materiality. An auditor’s pass is a queue-management signal, not certification.
5. Require the learner to reproduce one relevant calculation, explain one fact-to-client inference and its assumption, reject one tempting invalid inference, and propose one targeted client interview question without AI. Preserve the underlying source with the submission.

These are proposed controls derived from the failure mechanisms, not experimentally established optimal prompts.

## What a meaningful pilot can establish

The current qualitative review checks selected claims, exposes inference failures, and tests whether the teaching design has a coherent division of work. It does not show how often the workflow fails on ordinary engagements, how much it saves, whether trainees learn, or whether three contexts outperform one.

For a local pilot, compare manual research, one structured assistant, and the three-context design using comparable tasks and balanced assignment. Use distinct matched source packs or tasks to reduce carryover, not the identical case repeated in the same order. Include realistic ambiguities, inaccessible sources, duplicate announcements, and mixed forecast/actual measures. Keep model, tool access, participant experience and source access recorded. Include an open-search task if eventual use requires open search; a prepared pack alone does not test discovery.

Use blind human review of source accuracy, coverage of decisive evidence, assumptions, alternatives, and practical next steps. Record total person-minutes and elapsed time to a verified acceptable brief; include unsuccessful attempts and unresolved gaps. Treat the quality gate as an acceptance rule rather than proof that all errors were found. Measure immediate unaided understanding separately, then later transfer if claiming skill development. A small pilot supplies local directional evidence; broader productivity, learning, or staffing conclusions require broader observations.

Augmentation is credible when the saved effort is explicitly spent on activities that improve the engagement: testing a commercial assumption, obtaining customer evidence, interviewing an expert, exploring a competing option, or developing junior capability. Document that changed work. The workshop should promise a disciplined way to use AI in research, while leaving measured efficiency and learning outcomes to the pilot.
