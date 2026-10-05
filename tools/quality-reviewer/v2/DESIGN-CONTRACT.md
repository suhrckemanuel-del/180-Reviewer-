# Review view design contract

Separate student and lead HTML files render a supplied completed review without another
analysis. Student reads the complete review and optionally continues reasoning in the same
chat. Lead verifies evidence, decides keep/ask/cut with reasons and exports a human record.
No audience switch; no lead controls in student, no student exercises in lead.

Restore the supplied prototype references: v2/index.html and sibling
180dc-ai/website/reviewer-mockups/paired.css and templates. Use soft grey #EDEFF2,
white panels, near-black #111827, green #16A66A and accessible #0F8455, quiet borders,
14px corners, compact top bar, 16px panel spacing and a right-hand review desk. Keep readable
Evidence / Why it matters / Next step / Question fields. Older source fields remain intact;
a legacy problem paragraph appears as Issue. Saved text is never rewritten.

Strengths first, complete findings, expandable context. Page markers mean citations only.
No grades, rankings, readiness scores, page-pass labels, mandatory attempt gate or manufactured
findings. Zero findings is valid. A named human signs off before client use.

Native labelled inputs and visible keyboard focus. Explicit export/restore checks audience,
source mode/version, hash and keys; no automatic storage. Source PDF attachment verifies
recorded identity locally. No external fonts, assets, analytics or requests.

Check desktop, phone, keyboard, content/evidence, exports/restoration and readable print with
human notes. Captures stay client-private. Historical preview provenance must be explicit.
The old approved checkpoint remains untouched and does not approve this split design.
