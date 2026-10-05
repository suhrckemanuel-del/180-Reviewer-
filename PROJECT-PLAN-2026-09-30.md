# 180 Reviewer execution plan

Current build position, separate experiences and remaining acceptance work:
[CURRENT-MAP.md](CURRENT-MAP.md). Older dated progress below remains historical evidence.

**2026-10-06 steering:** separate student/lead prompts and HTML supersede the mode-switch
candidate. The earlier approved checkpoint remains historical and untouched; it does not
approve this split. Read [split checks](validation/SPLIT-EXPERIENCES-2026-10-06.md).
Owner requested a sanitized supervised candidate and PR, with no merge or deployment.
No new review campaign is part of this pass. Existing issue gates remain open.

Updated: 2026-10-05. This plan mirrors the live GitHub issues #1-#5. GitHub is the task list; this file is the local execution and acceptance map. Client-derived files, quotes, model outputs, and adjudications stay in ignored local storage and are not posted to GitHub.

## Product and finish line

The intended product is a supervised review flow for consultants and leads. The reviewer supports a person's own judgment; it does not approve client work, make the client's choice, or write paste-ready slide copy. Student flow: present the completed review, then continue in the same chat as a plain-language coach, explaining the decision behind a finding and asking the student to choose a response and support it with evidence. Work through one issue at a time without writing slide copy. An unaided first read is optional in normal use; it is collected before feedback only when measuring learning. Lead flow is separate: leads triage findings and sign off before client use. The paste-back record is evaluation/admin data, not a student-facing block to copy into GitHub. HTML under issue #3 is a faithful view of the same completed review, not a second review or the chat coach itself. Content selection and safe extraction remain in scope under issue #4.

The project is finished for a bounded pilot only when issues #1-#5 meet their evidence-based acceptance criteria, the release path and current hosted state are verified, the lead and owner have reviewed the pilot evidence, and README, release notes, and GitHub describe the same measured scope. Passing these tickets does not establish generalized learning gains or authorize unsupervised client use.

## Live issue map and order

| Issue | Live scope | Dependency | Completion evidence |
|---|---|---|---|
| [#1 Validate review logic and consultant learning on distinct cases](https://github.com/suhrckemanuel-del/180-Reviewer-/issues/1) | Replace synthetic acceptance cases with a small real-PDF sample from the deliverable folder, including the real deck with the owner's prior read; preregister expected catches; independently review and adjudicate every quote/finding. Keep all client material local and ignored. | Baseline for #2 and #3. | Case-level local records; must-catches, quotes, restraint, coaching, limitations and go/no-go. Earlier synthetic runs remain historical only and do not count. Real-deck baseline is exploratory, not a lead-signed pass. A human-authored revision is still needed to assess learning. |
| [#2 Ground the prompt in research and calibrate its coaching](https://github.com/suhrckemanuel-del/180-Reviewer-/issues/2) | Remove unsupported binary scoring; add source-traceable principles; implement full-review-then-coach; calibrate severity; run the new candidate with isolated local review agents on the selected real PDFs, then use separate local agents to audit findings against source pages. No synthetic deliverables. | #1 baseline. | Generated candidate bundle and token count; real-PDF reviews, independent quote/severity adjudication, no invented scoring or slide copy, tested post-review coaching, model limitations and explicit note that local agents do not establish external-service behavior. All client material stays ignored. |
| [#3 Rebuild HTML as a faithful view of the same review](https://github.com/suhrckemanuel-del/180-Reviewer-/issues/3) | Deterministic HTML from completed reviews of the selected real PDFs; lead adjudication controls; student receives the complete review then uses the same chat for conversational coaching; validate input/quotes; assess unreviewed pages honestly; test screen, keyboard, print and hosted state. HTML is the saved/printable review, not the chat coach. | #2. | Fresh real-PDF outputs compared field-by-field with HTML; no invented fields/findings; lead can record keep/ask/cut without raw JSON; student can choose what to discuss and reason toward a fix with evidence; rendered desktop, narrow, keyboard and print checks. Keep client artifacts local. |
| [#4 Let consultants select and inspect deliverable content before review](https://github.com/suhrckemanuel-del/180-Reviewer-/issues/4) | Select/preview pages from actual PDFs; preserve table/chart context; mark visual-only text as not assessed; anonymization check; exercise the extractor on actual local deliverables only. | Independent; can proceed alongside #2/#3. | Preview/paste correspondence; exclusions; safe intake; PDF/PPTX/DOCX checks on actual local deliverables; client content and detailed outputs remain ignored. |
| [#5 Publish one GitHub consultant release and pilot the whole flow](https://github.com/suhrckemanuel-del/180-Reviewer-/issues/5) | One consultant entry point; generated/versioned files and aligned keys; first-use guide; fresh-account workflow; lead and small-group pilot. | #1, #2, #4, and #3 if HTML ships. | `build-bundle.js --check`, correct three-file download and recovery path, key checks, first-use and free-tier tests, lead sign-off, and improvement log. |

## Execution order

**Current progress, 2026-10-03:** Candidate `candidate-2026-10-03-issue-2e` now implements
full-review-first, optional learning-measurement read, and same-chat student coaching; lead
triage remains separate. The TEST-KIT was regenerated and `build-bundle.js --check` passes
(0 releases; 2e; attempt-gate audience `none`). Three actual-PDF candidate reviews are complete
(28, 66, and 22 pages), with a separate AI-derived reference and another local agent's audit for
each output. The audits visually confirmed all 29 quoted passages and locations. They found
severity inflation across the sample and two missed preregistered decision questions in the third
case; see the ignored local case report at
`_client-private/issue-1/candidate-2e/VALIDATION-SUMMARY-2026-10-03.md`. These are AI-derived local
checks, not human gold or external model/service validation. No candidate-2e review has been run
on the owner-baselined real-12 deck, no human lead adjudication has been collected, and no case
author has completed the post-review reasoning/revision exercise. The decision remains NO-GO.
No synthetic input was used in these runs; earlier synthetic outputs and the old-prompt real-deck
review are historical only and do not count. Source/doc updates and candidate 2e are local and
unpushed.

**Student-flow clarification (2026-10-01):** The student sees the completed review first.
Then the same chat acts as a coach: explain a selected finding simply (what the deck says,
what that implies, and why it matters), invite the student to choose what to improve and
what evidence supports that choice, and help them test their reasoning without writing the
slide. The student can ask which finding to start with or select one themselves. A solo
first read is a learning-measurement step only, not a routine-use gate. Paste-back remains
an evaluation/lead record, not the student's next task. HTML stores/prints the same review;
the actual coaching happens in chat. This distinction is now part of the #2/#3 acceptance
criteria and does not count as completed validation.

1. Preserve #1's existing result as the baseline NO-GO record; do not relabel its same-chat observations as independent evidence.
2. Use candidate 2e on actual deliverable PDFs only: the first three local runs and cross-agent AI audits are complete. Next have a human lead adjudicate them, run candidate 2e on the owner-baselined actual deck from a clean reviewer context, and keep synthetic cases out of acceptance.
3. Implement #4 intake safeguards and #3 HTML fidelity. These can be developed in parallel after #2's output contract is stable, but each retains its own acceptance evidence.
4. Run the #5 end-to-end pilot only against the accepted prompt, intake path, and current HTML path if HTML is included.
5. Update each GitHub issue with accurate evidence and remaining blockers. Close only when its own acceptance criteria are met; issue closure is not a proxy for owner approval or rollout authorization.

## Current constraints and evidence rules

- The real-deck review showed useful coaching but has exact-quote and severity concerns. Client-derived source, quotes, screenshot, raw prompt, and output are in `_client-private/` and must remain ignored.
- The earlier real-deck baseline used a different prompt; it cannot validate candidate 2e. Recheck every quote against the visual source and have a human lead adjudicate findings before forwarding.
- The consultant who participated in the earlier conversation did not author the case. Their feedback can inform prompt design but does not satisfy issue #1's author-based learning observation.
- Issue #2's local candidate work is preliminary. Existing synthetic case runs are historical only; they do not count toward acceptance or prove real-PDF performance.
- The live prompt sources are `tools/quality-reviewer/v2/04-prompt-templates.md` and `CHAT-CONTEXT.md`; generated `TEST-KIT/PASTE-*` files must be rebuilt with `build-bundle.js`, not hand-edited.
- The earlier source register already marks arXiv 2605.17554 as withdrawn and says not to rely on it. Issue #2 must keep that correction explicit wherever the framework is used.
- Historical maps and sprint documents remain history. They do not override the live issue bodies or this execution map.

## Implementation steering, 2026-10-05

The owner requested implementation from the existing archived reviews and no further review rounds for this work. Candidate calibration, deterministic HTML, selected local intake and generated entry-point documentation are implemented. Their software checks and remaining pilot evidence are recorded in validation/IMPLEMENTATION-2026-10-05.md. Earlier instructions to commission additional reviewer agents are superseded for this implementation pass. Historical runs retain their original status; issue acceptance, human confirmation of the control and learning/pilot measurements are not inferred from source changes.
