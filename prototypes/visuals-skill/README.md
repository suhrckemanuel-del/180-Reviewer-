# PROTOTYPE: what `180dc-visuals` hands the consultant (ticket 24)

Throwaway. It answers one question for the map's ticket "What the visuals skill does in version
one": **which output should a consultant leave with, and how does the skill handle their slide
titles?** Invented organisation and data; no client material.

Open `index.html` (serve the folder: `python -m http.server`) to see the four outputs side by side.

## What's here

| File | What it is |
| --- | --- |
| `data/pantry-bookings.csv` | The invented dataset: 12 months of bookings and missed pickups, online and phone |
| `content/consultant.json` | Stands in for the consultant's own words: titles, lines, notes. The skill lays these out verbatim |
| `scripts/recompute.py` | Every number a chart or title uses, recomputed from the data (stdlib, so it runs on Free) |
| `scripts/build_chart.py` | Two SVG charts from the recomputed numbers, with the source line on the image |
| `01-chart.html` | The skill's chat check (three rounds on one title) beside the finished chart |
| `02-deck.html` | The Free-path deck: one HTML artifact, 4 slides, arrow keys, notes (N), PDF via print |
| `04-deck.pptx` | The same 4 slides with native, editable charts and speaker notes (python-pptx) |
| `03-hyperframes/` | The same 4 slides as a HyperFrames slideshow: reveals, presenter notes, a branch slide |
| `screens/` | Stills: the .pptx rendered by PowerPoint, the HyperFrames slides at each hold |

Rebuild everything from the prototype folder:

```
python scripts/recompute.py data/pantry-bookings.csv data/recomputed.json
python scripts/build_chart.py data/recomputed.json charts
python scripts/build_pages.py
python scripts/build_pptx.py
python scripts/build_hf.py
npx hyperframes@0.8.188 present 03-hyperframes
```

## What it showed

1. **The check is the product.** Round 2's title ("Text reminders cut missed pickups by 63%") is a
   real so-what with the wrong base: 63% is the online drop, the all-bookings drop is 43%. Only
   recomputing from the data catches that, and it works the same in every format.
2. **Hand-typed numbers drift.** Building this, a booking total typed by hand into the source line
   (3,690) was wrong; the data says 3,657. Rule for the skill: no number on a slide that the script
   didn't print.
3. **Native .pptx charts lose annotations.** The July event line and the average bands moved to a
   caption. The SVG chart keeps them, but as a picture.
4. **HyperFrames needed four fixes to run** (scenes as clips, an undefined timeline registry under
   `present`, a server restart after island edits, a duplicate hotspot button). Fine for a Claude
   Code user, too fragile to hand a consultant.
5. **Projector type.** Chart labels sized for a pasted laptop slide were below HyperFrames' 28 px
   floor at 1920×1080. All formats now use 30 px.

The verdict and the decisions it settles go on the ticket, not here.
