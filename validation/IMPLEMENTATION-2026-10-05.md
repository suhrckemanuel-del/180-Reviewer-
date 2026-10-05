# Calibration and product implementation — 2026-10-05

Initial local candidate: `candidate-2026-10-05-calibrated`. The owner requested implementation
using the existing archived reviews. No new reviewer run, human approval, published
release or measured learning improvement is claimed.

| Ticket | Implemented | Evidence and remaining scope |
|---|---|---|
| #2 Prompt/calibration | Whole-deliverable and appendix checks, counterevidence, strengths first, decision-bearing severity, no default effort estimate, zero findings, full-review-then-coach. | Source and generated-kit consistency pass. The new wording has not been tested in another model run; existing runs retain their original status. |
| #3 HTML | Deterministic saved-review renderer, quote/page validation, product theme, student/lead controls, separate keep/ask/cut notes, local PDF identity check, note export/restore and print. | Software regression checks pass. Browser desktop/narrow/dark/print checks completed against an existing saved review. Owner theme approval and human usefulness judgment remain. |
| #4 Intake | Original page/slide selection, included/excluded records, local PDF page preview, page-marked evidence JSON, ignored-output enforcement. Tables retain cells without guessed headers; chart missing values retain their positions. Speaker notes excluded by default. | Actual archived PDF/PPTX/DOCX extraction exercised. PDF selected-page preview and exclusion records verified. PPTX/DOCX visuals and DOCX pagination require original-file inspection; they are not rendered by this helper. Extraction does not anonymize. |
| #5 Release path | Combined setup/input/cover sheet generated; exact first-line keys aligned; GitHub entry point; immutable release file checks; updated first-use/publishing docs. | `build-bundle.js --check` passes with zero versioned releases. Consultant access, free-tier limits, fresh-account flow and human pilot observations remain unmeasured. Nothing published. |

## Checks completed

- `review-view.test.js` with an existing private review/evidence pair: exact raw text/hash
  and embedded payload, escaping including script terminators and replacement tokens,
  missing keys, retired fields, duplicate headings, unknown severities, count mismatch,
  altered quotes, unavailable pages, zero findings, private output and generated manifests.
- Browser: both modes retain all findings; notes exported and restored with an unsaved-note
  confirmation; original review export matches the rendered input byte for byte; source
  PDF identity matches its recorded hash; no horizontal overflow at 390px; no page errors.
- Desktop and phone screenshots, dark appearance and printable PDF inspected locally.
  Print includes expanded source context, all findings and current human notes.
- Browser network observations contained only the local file/loopback preview. No external
  assets, analytics or client upload are used. Downloads were verified with the browser's
  destination explicitly set to ignored private storage; the automation download helper
  initially cancelled downloads and was not treated as a product pass.
- Selected PDF pages retained original numbering and exclusions. Preview images came
  directly from the original pages. Actual PowerPoint and Word files extracted locally.
- Generated-kit consistency, JavaScript syntax and `git diff --check` passed.

The combined setup is 51,472 characters. A model-specific token count and free-tier capacity
were not measured. Character counts are not evidence that a particular chat will accept it.

The renderer rejected punctuation discrepancies in an earlier saved review. For interface
testing only, a separately labelled display copy contains two punctuation-only quote
corrections verified visually against the original PDF. The original output was preserved;
its finding wording and severity were not recalibrated or represented as a new run.

Detailed client records, outputs, corrections, extracts and screenshots remain under
ignored `_client-private`. This public record contains implementation facts only.

## Concision follow-up

At the owner's request, current sources are now `candidate-2026-10-05-concise`.
All modes use Evidence, Why it matters, Next step and Question, with a short issue title.
The redundant problem paragraph, repeated quote/sign-off notice and duplicate team questions
are removed from future reviews. Commentary targets 80–110 words per finding, excluding
quoted evidence; necessary qualifications must remain. Strengths and limits use short bullets.

HTML uses consistent section/field labels and collapsible optional discussion controls.
Older saved reviews retain all source text, including legacy problem paragraphs. Regression
checks reconstruct each source body from the structured fields to verify no content was lost.
The standardized private preview uses the same saved review, not a new reviewer run.
The regenerated combined setup contains 50,395 characters; no token/capacity claim is made.

## Owner design approval

On 2026-10-05 the owner said the standardized interface was good for now and requested it
be stored. This approves the current visual/format direction. It does not constitute human
adjudication of reviewer findings, a consultant workflow observation or client approval.
The approved local HTML and implementation source fingerprints are preserved in ignored
private storage. [CURRENT-MAP.md](../CURRENT-MAP.md) records the current ticket position.
