# A live deck with HyperFrames (Claude Code only)

Only when the consultant is in Claude Code with the HyperFrames skills installed and asks for a
deck to present live, with reveals. On claude.ai, the .pptx is the deck.

Build the slides as usual first: the checks, `numbers.json`, their titles. Then use the
`slideshow` skill, with these lessons from the 180DC prototype (HyperFrames 0.8.188):

- Put every slide inside one root composition (`data-composition-id="root"`) and register one
  timeline as `window.__timelines["root"]`. Separate top-level scenes did not resolve under
  `present`.
- Start the script with `window.__timelines = window.__timelines || {};`. It is undefined
  under `present`.
- Give each slide in the island an explicit `startTime` and `endTime`, and show or hide each
  slide with `tl.set(..., { autoAlpha })` at its boundaries.
- Entering a slide lands on its first fragment. Design the first reveal as the slide's opening
  state.
- `present` reads the island once: restart it after editing the island.
- The slideshow draws its own hotspot buttons. Don't add your own.
- Chart text at 1920×1080 needs 28 px or more.
- Never render a deck to MP4; it keeps only the first scene.
