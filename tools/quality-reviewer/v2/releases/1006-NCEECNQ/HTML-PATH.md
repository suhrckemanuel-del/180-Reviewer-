# Optional local HTML: the same completed review

Use this only AFTER the complete chat review has been written and saved. Do not run another
analysis, fill a second review object or design custom HTML. The renderer reads the saved
review, validates the existing findings against page-marked source text and displays it.

The source of truth is the completed review, including strengths, count, order, severity,
quotes, questions, limitations and setup keys. A renderer cannot silently repair content.
If validation fails, report the mismatch. Keep the raw review unchanged and record any
human-approved correction in a separate copy before rendering that copy.

## With local repository access

1. Save the completed review under the ignored `_client-private` directory.
2. Obtain page-marked evidence with the local intake tool. Keep the original PDF as the
   authority; JSON/text is an indexing and quote-checking aid, not a visual substitute.
3. Run `node tools/quality-reviewer/v2/review-view.js --review <saved-review.md> --pages
   <evidence.json> --out <ignored-private-output.html>` (one command on one line).
4. Open that local HTML. Attach the original PDF using the page's file picker for source
   navigation. No file is uploaded. Check that it is the correct source PDF.
5. Verify the rendered page at desktop and narrow widths and check both modes and print.

Without local tools, return the complete chat review. Do not invent a replacement page or
claim that HTML has been generated. The local renderer is optional; chat coaching still works.

## Separate student and lead files

Choose `--audience student` and `student-review.html`, or `--audience lead` and
`lead-review.html`. Each has a dedicated template; there is no mode switch. Both retain
the supplied complete review. Student adds an optional reasoning field and
a discussion prompt for continuing in the same chat. It does not hide feedback, require a
minimum answer length, score a response or simulate learning. Lead mode adds keep/ask/cut
decisions and notes. Human notes are separate from the immutable review and can be explicitly
saved and restored locally. They are not auto-saved; restore checks audience, review hash and keys.
Lead displays unresolved decisions and missing reasons. For existing historical review
material, `--historical-preview --provenance <accurate-description>` explicitly permits an
audience mismatch for interface inspection only. The view labels that provenance and does
not relabel the saved review's original mode, keys or text as a new candidate output.

There are no grades, readiness scores, student rankings or page pass/fail labels. A page
marker means only that a finding cites it. Zero findings is valid. Do not manufacture a
main issue, contradictions, mandatory fixes or estimated work time to fill the interface.

## Fidelity and privacy

The renderer preserves the original review text in its payload and original-review download.
Text matching is not proof that a finding or its visual interpretation is correct. A human
still checks the original source. Never edit a reviewed quote to make the checker pass.

Use only the fixed renderer and its shared brand stylesheet. No external fonts, assets,
analytics, hosting or network requests. Client outputs and browser checks stay ignored in
`_client-private`. Do not copy them into a website deployment directory.
