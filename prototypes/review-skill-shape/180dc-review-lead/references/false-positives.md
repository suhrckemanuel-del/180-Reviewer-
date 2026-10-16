# Things that look like defects and are not

Each item cost a 180DC lead time to write down. Drop any candidate finding that matches.

## Extraction damage (the file, not the team)

The text you read was pulled out of a deck and the pull is lossy. None of these is a finding:

- Slides that arrive empty: images, diagrams or section dividers. Their content exists.
- Table and chart figures that arrive flattened or detached from their labels.
- Loose numbers with no sentence around them: callouts, page numbers, footers.
- Text broken one word per line or out of order.
- A date or title placeholder on a divider page. (Placeholder text in the body of a finished
  deliverable **is** a real finding.)

`scripts/extract_deck.py` lists the slides it could not read. Build no finding on a figure, table
or series from those slides unless you can see the slide image. A contradiction whose only evidence
is a value the extraction may have broken is a question for the lead, not a finding.

## Not about extraction

- **The client's own operating data** needs no citation to a study.
- **A section the brief never asked for** is not a gap. Check the brief first.
- **A named person in an illustrative scenario** (a persona, a worked example) is not a breach.
- **A deliberately partial artifact** (interim deliverable, research plan, draft) is reviewed as
  what it is.
- **Something you did not understand** may be domain material, not unclear writing. Say which.
- **"Not disclosed" or "not found here"** is not "confirmed absent". A proposal to improve a
  process does not prove there is no process today.
- **A disclosed method is not a missing method,** even without a worked example.

More patterns from past reviews: `case-patches.md`.
