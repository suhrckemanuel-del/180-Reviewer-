# Visual directions for the review output (issue 23)

Five drafts of the lead's deck-walk view, made on 2026-10-23 while working out the final look. Every draft is
filled from the same `REVIEW` object as `180dc-review-lead/assets/deck-walk.html`, so any one can drop in. The
deck and the review are invented (a food bank volunteer-app deck); there is no client material here.

Open `index.html` for the side-by-side gallery, or open each file directly in a browser.

| File | Idea | Verdict so far |
|---|---|---|
| `01-look-options.html` | Three recolours of the old layout (Steep, Vercel, Ramp), chat and deck walk side by side | Rejected: still looked made by Claude |
| `02-paper.html` | The deck as paper on a desk: each finding pinned to its slide, quote highlighted, printed-label metadata | Good direction, calm, read-only |
| `03-hand-back.html` | Built around the lead's job: swipe one finding per card, decide send / ask / leave out, copy a note to the team | Right idea, too loud |
| `04-review-sheet.html` | Between 02 and 03: one ruled sheet, findings on slide frames, a decision row on each, the note at the end | Front-runner |
| `05-route.html` | The deck as a transit line in slide order: quotes at their own slide, numbered red loops for one problem across slides, a slide bar and slide viewer, a ticket-stub note | Liked; loops and slide viewer added after first feedback |

## What made the early drafts look Claude-made

- Every block was its own floating card: 12–22px rounded corners, soft shadow, pastel tinted panel inside.
- The main issue sat in a tinted callout box with a coloured stripe down its left edge.
- Severity in red / amber / grey chips, which also reads as a grade of the deck.
- A bookish serif and plain system sans, close to Claude's own chat fonts.

## What we borrowed instead

- **Ruled cells, not cards** (Ramp's logo grid, Browserbase, Attio's tab bar): boxes share one 1px line, square
  corners, no soft shadow. In 04 this is one CSS rule: an ink grid with 1px gaps.
- **The slide as the object** (Ramp's invoice with an attached panel, Superhuman's in-text highlight): the quote
  sits on a 16:9 slide frame with a green highlighter.
- **Printed labels** (teenage engineering's device labels, Ramp's top line): counts and the check line on a spec
  plate; the slide strip as a port strip with solid / hatched / outline marks.
- **One loud surface** (Ramp's single accent): 180DC green fills the main-issue band and the lead's "send"
  choices, nothing else.
- **Fonts**: Schibsted Grotesk and Martian Mono in 04, Overpass and Overpass Mono in 05 (Google Fonts, free).
- **Slide order, not severity order** (05): the team works through the deck from slide 1, so 05 lays the review out
  that way and lists the fixes in the note in slide order too.

## Showing the real slide, and what it costs

05 opens any slide in a viewer. In the prototype the viewer shows the slide's text from an invented `DECK`
object, kept apart from `REVIEW`. The question is how a real slide gets into the page.

- **Through Claude:** not workable. The page is text Claude writes out, and one slide image as text is roughly
  30–60k tokens, so a single deck would blow a Free account's limits.
- **Through a build script:** costs no extra tokens. The skill already runs `extract_deck.py` in the sandbox.
  A sibling script (say `build_deck_walk.py review.json deck.json deck.pdf`) would put Claude's `REVIEW` together
  with the slide text from `deck.json` and, where the sandbox can render them, small slide pictures. It would
  write the finished page as a file. Claude writes only `REVIEW`, as it does now, and the slides never pass
  through the model.
- **Costs:** the page becomes a downloaded file, not an inline artifact. PDF pages render easily; PPTX needs
  LibreOffice in the sandbox, which is untested on Free. If rendering fails, the script still embeds the slide
  text, which is what the prototype shows.

## Open before any of these ships

- Whether Claude Free's artifact view loads Google Fonts. The fallback is the system font, which still works.
- Whether the Copy button works inside Claude's chat. If copying is blocked, it selects the text instead.
- Lead decisions live in memory and reset when the page reloads.
- The note to the team is assembled only from REVIEW sentences (main issue, next steps, ask-the-team questions,
  strengths). It adds headings, not new advice.

Screenshots of every draft at phone width, and the reference sites, are in `screenshots/`.
