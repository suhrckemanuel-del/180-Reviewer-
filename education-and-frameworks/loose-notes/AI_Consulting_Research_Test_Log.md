# Research prompt pilot and case walkthrough

Run date: 7 October 2026. Historical evidence cutoff: 30 April 2025.

Environment: this Codex desktop session, using two independently briefed research subagents followed by a third evidence auditor. Agents inherited the session model and reasoning configuration. This run was not conducted on a verified ChatGPT Free account, and no numeric usage allowance is inferred from it.

The copyable shared core, role assignments, and facilitator instructions are in [AI_Consulting_Research_Lab.md](AI_Consulting_Research_Lab.md). The two researcher invocations additionally instructed them to follow the prompt exactly, return an execution log, and avoid file edits. Market and peer researchers received no previous conversation context or each other's output.

## Initial hypothesis

An illustrative participant might write: "Convenience expansion is attractive because shoppers value proximity and large competitors are expanding."

This is a hypothesis to investigate. It is not supplied client evidence, and the research must be allowed to challenge it.

## Source pack and inspected facts

| ID | Inspected finding | Original source, publication date, locator | Boundary |
|---|---|---|---|
| M1 | Great Britain food-store sales volumes fell 1.3% in March 2025, after a 2.2% February decline; seasonally adjusted. | [ONS retail sales, March 2025](https://www.ons.gov.uk/businessindustryandtrade/retailindustry/bulletins/retailsales/march2025), 25 April 2025, section 3 | National quantity changes do not establish Northstar revenue or convenience-format performance. |
| M2 | Total retail volumes rose 1.6% quarter-on-quarter and 1.7% year-on-year in Q1 2025. | Same ONS release, section 2 | All retailing, not grocery alone; a counterweight to an overly broad decline narrative. |
| M3 | UK food and non-alcoholic beverage prices rose 3.0% year-on-year in March 2025, versus 3.3% in February; monthly prices were unchanged. | [ONS consumer price inflation, March 2025](https://www.ons.gov.uk/economy/inflationandpriceindices/bulletins/consumerpriceinflation/march2025), 16 April 2025, section 3 food discussion and section 5 Table 3 | Slower inflation does not mean prices fell year-on-year or establish client basket economics. |
| M4 | CMA described access-constrained shoppers depending on generally higher-priced convenience stores. | [CMA cost of living update](https://www.gov.uk/government/publications/cost-of-living-update/cma-cost-of-living-update), 26 July 2024, Groceries / Retailer profitability update, paragraph before Pricing issues | Regulator assessment, not a quantified price premium, willingness-to-pay estimate, or ROI. |
| C1 | Tesco reported opening 55 Express and seven One Stop UK stores; it refreshed 245 UK convenience stores and 100 UK large stores in FY2024/25. | [Tesco preliminary results](https://www.tescoplc.com/media/mxfjrk4x/tesco-plc-preliminary-results-2425-press-release.pdf), 10 April 2025, printed pages 3 and 12 | Both strategies were pursued; activity counts do not rank their returns. |
| C2 | Tesco reported approximately £510m Save to Invest savings across the Group. | Same Tesco release, printed pages 2-3 | Group savings are not profit attributable to UK convenience refurbishments. |
| C3 | Sainsbury's reported nearly 4% convenience sales growth; management said space and range changes helped. | [Sainsbury's original results PDF](https://corporate.sainsburys.co.uk/media/agjkfo41/prelim-results-announcement-24-25-report.pdf), 17 April 2025, printed pages 1 and 3-4; year ended 1 March 2025 | Company-reported sales performance and a management explanation, not measured causal uplift or project ROI. |
| C4 | Sainsbury's expected 25 new convenience stores in each of the following two years. | Same Sainsbury's PDF, printed page 3 | Forward plan, not achieved openings or evidence of a particular return. |

These six findings were independently inspected by the coordinating agent, checking the relevant original source text and locators. The audit agent also checked a selected subset below. Each researcher supplied brief source excerpts and claim-level limitations in its original chat output; the table above preserves the substantive findings without reproducing every quotation.

## Execution observations

Researcher A searched for ONS March 2025 retail sales, ONS March 2025 food inflation, and CMA convenience/value evidence. It opened three distinct primary sources, reported no inaccessible sources, and produced four findings. It did not mistake total retail growth for food-store growth or national data for local demand.

Researcher B searched for Tesco and Sainsbury April 2025 results. It opened Tesco's results webpage, Sainsbury's results webpage, and the Tesco PDF. Its three-source limit was reached before it could corroborate the Sainsbury webpage's publication date. It marked the Sainsbury convenience growth and future opening plans provisional and excluded them from cutoff-qualified findings. That is appropriate uncertainty handling, not a completed verification.

One pilot lesson: a rigid source cap can be consumed by a landing page and its PDF. For class, start from the direct source pack. For a wider investigation, explicitly allow one extra original source when publication metadata needs verification; do not silently relax the cutoff.

## Deliberately misleading audit inputs

The auditor received three real findings (M1, C1, and provisional C3) plus these three planted errors. The underlying source links were supplied, but it had to inspect them itself.

| Trap | Deliberately flawed assertion | Required detection |
|---|---|---|
| T1 | The ONS decline proves Northstar convenience revenues fell by the same percentage. | National quantity data cannot establish client revenue or a particular format. |
| T2 | Tesco's group savings were profit from UK convenience refurbishments and prove refurbishments beat openings. | Incorrect attribution and unsupported comparison. |
| T3 | Sainsbury's planned openings prove an 18% ROI and justify committing the entire client budget. | A plan is not a measured return; 18% was invented for this test. |

These traps were intentionally obvious enough for a teaching demonstration. Detection in this small test does not measure reliability on subtler errors or unfamiliar cases.

## Auditor results

The audit prompt was run once with M1, C1, provisional C3, and the three planted assertions. It opened four primary sources: the ONS release, Tesco PDF, Sainsbury webpage, and Sainsbury original PDF.

| Input | Result | Explanation |
|---|---|---|
| M1 | Supported | Correct national statistical estimate, period, unit, and release date. |
| C1 | Figures supported; date initially incompletely verified | Original PDF supports counts. Auditor's cap prevented opening the separate official date page. |
| C3 | Supported as company reporting | Original PDF dated 17 April 2025 resolved the earlier missing publication date; management attribution retained as such. |
| T1 | Unsupported; caught | National volumes were incorrectly substituted for client revenues. |
| T2 | Unsupported; caught | Group savings were incorrectly attributed to one format and investment type. |
| T3 | Unsupported; caught | Planned openings do not establish ROI; the 18% figure has no support in the cited disclosure. |

Result: all three deliberately planted errors were identified. The coordinating agent then opened [Tesco's official results page](https://www.tescoplc.com/preliminary-results-202425/), which displays 10 April 2025, closing the auditor's date-verification gap. It also opened the dated Sainsbury original PDF and inspected the relevant claims. Thus eight reported research claims have source support after coordination, while the company explanations and plans retain their appropriate labels.

The final verified record did not arise from one flawless first response. It required an auditor to resolve one missing date and the coordinator to resolve another. The prompts encouraged disclosure of gaps; the workflow completed the verification.

## What the consultant can do with the evidence

The two researchers agree that published evidence does not rank the client's investments. Their emphasis differs: market research raises questions about value and access; peer research shows expansion and existing-estate investment occurring together.

A useful additional option is a staged allocation: compare a limited existing-store improvement pilot with due diligence on a small set of candidate convenience catchments, retaining the remaining budget until the economics are clearer. This is a consultant-designed option, not a finding in the sources or a quantified investment recommendation.

Request three sets of client evidence:

1. Candidate-site capital cost, rent, staffing, sales ramp, delivery cost, and sales diverted from existing stores.
2. Existing-store stockouts, waste, labour, transaction counts, basket margin, and historical improvement results against comparable stores.
3. Investment hurdle, cash constraints, implementation capacity, and local customer research.

Then compare incremental cash flows over a common horizon, including an agreed residual value where appropriate. Check both scenarios under the same discount rate and demand assumptions. A pilot needs a credible comparison group and contribution-profit measures; an increase in sales alone does not establish an investment return.

## Test status and limits

This is one live case pilot of two research prompts and a targeted auditor stress test. It does not establish reproducibility across models, accounts, or tool configurations. The human synthesis prompt is a facilitator template, not a separately validated component. Formal workshop acceptance requires checking the actual participant accounts and repeating the exercise with another case.

The experiment supports teaching claim verification and decision framing. It does not show that multiple agents outperform a single researcher; no single-agent comparison was run.
