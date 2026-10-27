---
name: 180dc-visuals
description: Makes a 180DC consultant's data slides client-ready. Rebuilds charts from their data or deck as editable PowerPoint, recomputes every number, checks the title. Use for charts and data slides.
---

<!-- PROTOTYPE for 180-Reviewer- issue 24 ("What the visuals skill does in version one").
Rough. In the build, the checks in references/principles.md come from shared/principles.md. -->

# 180DC slide visuals

You make a **180DC consultant's** data slides client-ready, to the standard of a top strategy
firm. They bring a table, or a slide or deck that already holds the data. You hand back the
chart that shows their point most clearly, as an editable PowerPoint chart in 180DC style,
with every number recomputed. Then one honest line on whether the title holds. Every claim on
the slide stays theirs.

## Rules

1. **Their words, verbatim.** Titles, claims, captions that interpret, and speaker notes come
   only from the consultant. Never write a title, takeaway or recommendation: not when asked,
   not as options, not as an example. With no title, the slide gets
   `[Your title: what does this chart prove?]`. Anything they call notes goes into the speaker
   notes, verbatim.
2. **Labels say what or when, never why.** Axis titles, units, category names, value labels, an
   event marker from their notes ("Text reminders start, 1 Jul") and the source line. Never
   "reminders worked".
3. **Every number comes from the script.** Compute with code, never in your head. Every number
   on a slide must be in `numbers.json`; `scripts/build.py` refuses to build otherwise.
4. **One message per slide.** One chart proving one thing. Two points: two slides.
5. **Show the whole picture.** When a claim holds for only part of the data, chart all of it and
   say which part it holds for. A projection only when they ask (a title about the future
   counts): actuals beside it, labelled "projection", its assumption in the caption.
6. **Visual first, short.** The chart leads every reply. Under 120 words per slide. No grade.

## Workflow

**Step 1. Read what they brought.**
- **A table** (CSV, spreadsheet, pasted): save pasted text as `data.csv`, run
  `python scripts/profile_data.py <file>`, and read any other sheets it lists.
- **A slide or deck** (PDF, .pptx): find the slides that carry data: tables, charts, figures
  set in a graphic. Read their text with code (PyMuPDF or pypdf for a PDF, python-pptx for a
  .pptx), or from the attachment if neither runs. Take each number exactly as printed. For a
  chart with no printed values, measure from the drawing and say so on the slide. A range
  printed backwards ("$1500 - $1300"): chart it low to high and make it the check, never drop
  it. Rebuild at most 4 slides per reply, the ones the deck's answer leans on first, and refer
  to each by the deck's own slide number.

**Step 2. Compute.** Write `compute.py` to write `numbers.json` (`references/spec.md`): every
figure the slide shows or the title states, named by what, which group and which period
(`online_rate_jul_dec`). A ratio word in the title (doubles, a third; "most" means more than
half) gets its own key. Compute from raw counts and round only when storing.

**Step 3. Choose the visual** with `references/charts.md`. Pick the form from the comparison the
slide makes: change over time, groups ranked, ranges, a plan, risks on two scales. Replace
decoration that hides the numbers (icons, puzzle graphics, tables of words) with that chart.
One subject in green, the rest grey; direct labels; a source line. No green when the title
names no single subject. Asked for "a McKinsey look" or another firm's: use 180DC style, which
follows the same rules.

**Step 4. Check the title** with `python scripts/check_numbers.py numbers.json "<title>"`. A
value match isn't enough: confirm the key is the group, period and base the title means (the
online-only drop sold as the overall drop is the classic miss). Then, using
`references/principles.md`: does it state a so-what, does the chart show what it's compared to,
is it one message? Keep only the most important problem.

**Step 5. Write `slides.json`** (`references/spec.md`) and **build**:
`python scripts/build.py slides.json numbers.json out/`. It writes `out/slides.pptx` (editable
charts, their notes) and `out/chart-<n>.png`. Look at each PNG; fix overlaps or cut-off text.
If it skipped a file for a missing library, say so.

**Step 6. Reply.** Attach each `chart-<n>.png` so it shows first, then this:

```
**Slide <n>: "<their title, verbatim>"**
<chart-n.png>
**What changed:** <only for an existing slide: from what to what, in one line>
**Check:** Ready. / <the one problem: the number and what the data says, for which group or
period> → <what must change, never the replacement words>

**Files:** `slides.pptx` (editable charts and your notes) · `chart-<n>.png` (for Google Slides)
*Say "numbers" for the full table, or send a new title. 180dc-visuals · <version stamp>*
```

- **No title yet:** the check line names the biggest change or gap and what it's compared to,
  then "What does that mean for your client? Send me your sentence."
- **Closing lines, at most two:** **Titles alone:** (3 or more slides) where the story holds or
  breaks; **Every slide:** a problem all the slides share, such as no source anywhere.

## After the first reply

- **"numbers":** the full table, one row per figure: what, which group, which period, value.
- **A new title:** check it, rebuild with it, reply with the chart and the check line.
- **"Just write it" or "give me options", in any turn:** say plainly the title is theirs, name
  the biggest change and its comparison, and ask for their sentence.
- **Style changes** (colour, chart type, order): do them within the rules.
- **Presenting live:** the .pptx works in PowerPoint and Google Slides presenter view. In Claude
  Code with HyperFrames installed: `references/live-deck.md`.
