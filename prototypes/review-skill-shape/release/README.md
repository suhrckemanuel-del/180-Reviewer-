# Lead review skill: release

The release candidate handed out is `1026-cb4758f`, built from commit cb4758f.

**Rebuild on any machine**, from `prototypes/review-skill-shape/`:

    python release/build_zips.py 180dc-review-lead release <MMDD-shortsha>

Use today's date and the short hash of the commit you build from (`git rev-parse --short=7 HEAD`). The zips
land in `release/` and are git-ignored. Hand out **`180dc-review-lead.zip` only**: owner decision 2026-10-26,
the lead skill ships ungated. The script also writes a gated zip, which is not handed out.

Test runs go in `release/free-run/`, which is git-ignored too: decks never go in the repo.

## Tested (2026-10-24, Claude Code, real 28-page PDF)

- Written review: 5 findings, 796 words, quote check clean (11 of 12 on the slide, 1 check by eye
  and confirmed against the page).
- review.json: all 53 strings word for word from the review, only the listed keys.
- Deck walk: 28 slide pictures, one box per quote on the quoted words, evidence and "change these
  words" drawn differently, gap labels on the four gap findings, longer next step under
  "More on this step". About 5k tokens against about 45k for the review.
- Fixed after that run: a quote with straight quotes where the slide has curly ones was boxed only
  in part and still counted as located.

## Free run 1 (2026-10-26, stamp 1026-83417a8, a real 23-page PDF)

- Review: passed every release check. 751 words, quote check 10 of 13 on the slide plus 3 read
  from a table image, all numbers re-checked against the slides, review.json word for word.
- Deck walk: the file came back and all 23 slides showed as pictures, but Fix mode had **no boxes**:
  Free has poppler and no PyMuPDF. Fixed in 1040799 (poppler word boxes), checked here against the
  PyMuPDF path; needs one more Free run to confirm.

## Changes for Free run 2 (1026-cb4758f)

- Fix mode boxes on Free (poppler fallback), and the extract survives split emoji.
- The Framework line now gives its reason in the deck's own terms, only when one of the four principles
  genuinely explains the finding, each principle once at most.
- Fix mode shows every slide a finding quotes; "fix" marks only words to change; labelled figures are
  named as such; boxes stay visible on dark slides.

## Still open

- Free run 2 with `1026-cb4758f` (`FREE-TEST.md`): do the Fix-mode boxes appear on Free now?
- A .pptx deck walk with pictures needs LibreOffice in the sandbox; until then a PDF export gives the
  better view.
