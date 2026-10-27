# build_deck_walk.py test (issue 23)

Tests `180dc-review-lead/scripts/build_deck_walk.py`, which builds the deck-line page (draft 05) as a file, so
slide pictures never pass through Claude. Everything here is invented: the deck is the food bank volunteer-app
deck the issue 23 drafts review. There is no client material.

```
python make_test_deck.py                                   # writes test-deck.pdf and test-deck.pptx (18 slides)
python ../180dc-review-lead/scripts/extract_deck.py test-deck.pdf -o deck-pdf.json
python ../180dc-review-lead/scripts/build_deck_walk.py review.json deck-pdf.json test-deck.pdf -o built-from-pdf.html
```

`test-deck.pptx` is not committed, because the repo ignores every `.pptx` to keep client decks out.
`make_test_deck.py` writes it again.

`review.json` is the REVIEW object from draft 05, word for word: what Claude would write. The script adds the
slide text from `deck.json` and, when it can render the deck, one JPEG per slide. It fills
`assets/deck-line.html` and writes one self-contained page.

## Results on 2026-10-23 (Windows, Python 3.14, PyMuPDF installed, no LibreOffice, no poppler)

| Run | Result |
|---|---|
| PDF | 18 pictures via PyMuPDF at quality 70, page 0.4 MB, all 11 quotes on their cited slides |
| PPTX | No LibreOffice here, so no pictures; page still builds with each slide's text (34 KB) |
| No deck file | Text only, same as the PPTX run |
| Finding cites slide 27 of 18 | Builds, prints `warning: finding 3 cites slide 27, but the deck has 18` |
| Quote boxes (added later the same day) | 10 of 10 quotes located on their slide with PyMuPDF; fix mode draws numbered boxes over them. The PPTX build has no boxes (no pictures) and highlights the quote in the slide text instead |

The fallback order is PyMuPDF, then `pdftoppm`; a .pptx goes through LibreOffice to PDF first. If the rendered
page count doesn't match `deck.json` (hidden slides, a different file), the script drops the pictures rather
than show the wrong slide. It steps JPEG quality down (70, 55, 40) to stay under a 12 MB page.

## Not tested yet

- **Claude Free's sandbox:** whether it has PyMuPDF or poppler for PDFs and LibreOffice for PPTX. That decides
  whether leads get pictures or text.
- **Getting the page to the lead on Free:** offered as a file to download, not shown inline.
- **SKILL.md:** not wired up yet. The "Deck walk" section still tells Claude to fill `assets/deck-walk.html` as
  an artifact.
- **Wrapped PDF titles:** a long PDF title that wraps onto two lines extracts as two lines, so a quote of the
  whole title is missed. The first fixture hit this on slide 12; it's the same failure as issue 20.
