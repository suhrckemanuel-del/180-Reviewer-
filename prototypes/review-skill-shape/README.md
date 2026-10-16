# Prototype: the review skill's shape

Throwaway. Answers [The review skill's shape](https://github.com/suhrckemanuel-del/180-Reviewer-/issues/13).
Lives on branch `prototype/review-skill-shape`, never on `main`.

## What is here

| File | What it is |
|---|---|
| `180dc-review-lead/SKILL.md` | Release `1006-NCEECNQ`'s lead setup cut from 7,800 words to 926. Both gate variants are in step 2 |
| `180dc-review-lead/references/` | The depth, read at named workflow steps: the five review questions, severity, false positives, case patches (1,540 words) |
| `180dc-review-lead/scripts/extract_deck.py` | Per-slide text to `deck.json`. Standard library only for .pptx and .docx |
| `180dc-review-lead/scripts/check_quotes.py` | Checks each quote against the slide it cites, item by item |
| `output-shape.html` | One **invented** review shown three ways (`?variant=A/B/C`), gated or ungated (`?gate=on`), phone width (`?phone=1`) |

Open the page: `python -m http.server 8713` in this folder, then
`http://127.0.0.1:8713/output-shape.html`. Arrow keys switch between variants.

## What the cut removed

The JSON contract and its field names, the nine lenses, the ten dimensions, the issue types, the
bundle keys, the history of the withdrawn readiness level, the duplicated blocks, and the lead
record and `lead-review.html`, which the setup referred to but never gave a schema for. The
lenses became five review questions. The blocking rules became the five ways a finding reaches
High impact. The case patches moved to `case-patches.md`.

**Also dropped, and worth a second look:** the "Could change if" line (folded into Couldn't
judge), the cross-cutting "questions worth asking the team" block, and the header notice
(it is now one line in the footer).

## Quote check, tested on an invented two-slide deck

The check passed both exact quotes and collapsed extra whitespace. It flagged a correct quote cited
to the wrong slide ("found on slide 1 instead") and a quote that joined two bullets ("not found").
It has not been run on Claude Free yet. Only `check_env.py` has.
