# The four checks

<!-- PROTOTYPE. In the build these entries come from shared/principles.md, and the "not a break"
lists from shared/false-positives.md. -->

Run them in this order. Each has a **test** (does it break?), a **pick rule** (which slide you
report, so every run picks the same one), what is **not a break**, and the **do this / check it**
to give. The move names the change and where; it never contains the words.

## Before the checks

**Know the title.** The first line of a slide in `deck.json` is often not its title. Use the
slide's `title`, else its `largest_text` when it reads as a heading, else the slide image. If none
tells you, tag the slide D in the title table and leave it out of checks 2 and 3.

**Weak is not absent.** Before saying the deck never states something, search every slide for
it. If it is there in weak form (hedged, buried in a list, one point among six), quote that and
say what is wrong with it. "Never" and "missing" are only for what is truly not in the deck.

**A deck inside the deck.** A deliverable can contain a product the team made *for* the client: a
pitch deck for investors, a template, a guide. Checks 1 and 3 judge the consultant's own argument
to the client, not the product, which follows its own conventions (a pitch ends on its ask).
Checks 2 and 4 still apply inside the product.

**Extraction damage is not a break.** Empty slides, numbers detached from labels, text out of
order and placeholder dates on dividers come from the extract. Build nothing on a chart you can't
see.

## 1. Pyramid

**Test.** Find the **governing thought**: the one sentence the deck most wants the client to
believe or do. It breaks if any of these is true:
- it first appears after the first three non-D slides;
- it is generic, true of any client ("X needs a holistic strategy");
- it doesn't answer the deck's own question, when a slide states one (a problem statement,
  a research question, a brief);
- the opening gives several points of equal weight and never says which one governs.

In a problem analysis or interim deck, the main finding, or the question plus what the team
already thinks, counts as the answer. Gated: compare their sentence with the first slides.

**Pick.** The summary or first content slide. Quote its governing line, or its first line if it
has none, and the question slide when that is the proof.

**Do this:** state the answer to the deck's own question on that slide, first, and order what
follows so one point leads. **Check it:** read only that slide to someone outside the project.
Can they say what the client should do or believe, and why?

## 2. So-what titles

**Test.** It breaks if two or more content slides have an **L** title in the title table.

**Pick.** The first **L** slide in slide order, skipping the slide check 1 used. Quote its title,
and its takeaway line if the body has one. List every other **L** slide number in one line.

**Not a break:** D slides; a takeaway you would phrase differently; one **L** slide alone.

**Do this:** make the title the one thing the slide proves; keep the topic as a small tag if they
want it. **Check it:** could someone disagree with the title? A label can't be disagreed with.

## 3. Ghost deck

**Not judged** when check 2 breaks with half or more of the content titles **L**: there is no
story to read yet, and fixing check 2 comes first. Say that in one line.

**Test.** Read the **T** titles alone, in order. Two questions, in this order:
1. **Does every section say something?** A section (the slides between two dividers, or the
   whole deck if it has none) breaks if it has no **T** title.
2. **Does the story end on the answer?** The last **T** titles break if they end on options,
   findings or "could" statements without saying which one the client should take, or with no
   next step. In an interim deck, "what we will do next, and why" counts as the ending.

**Pick.** The first question that breaks. For 1, the first such section; quote its first title.
For 2, quote the last **T** titles (up to three).

**Do this:** write the titles as a list on their own, fix the order and the missing link there,
then rebuild the slides to match. **Check it:** read the titles aloud in order. Does a listener
follow the argument without seeing a slide?

## 4. Compared to what?

**Candidates.** Figures and size claims ("most", "low", "needs to be improved", "x% increase")
on **T** title slides only, in slide order. Not on the summary (it restates figures shown
later), and never on **L** or **D** slides.

**Test.** A candidate breaks if the slide gives no comparison (a benchmark, last year, a
competitor, a target) or no base for a percentage, so the reader can't tell whether it is good or
bad. Check footnotes and the appendix first. A missing source alone is a break only for a figure
the answer rests on.

**Pick.** The first candidate in slide order that breaks. Name up to two others in one line.
If the deck already names a comparison, even a vague one, say what is still missing.

**Not a break:** the client's own operating data shown as a trend; figures on background slides
the answer doesn't use; a labelled assumption.

**Do this:** put the comparison the client would decide against right next to the figure, with
its source and period. **Check it:** cover everything but the figure and its line. Can a reader
say whether it's good or bad?
