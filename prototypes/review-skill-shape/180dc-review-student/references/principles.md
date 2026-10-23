# The four principles, as checks

<!-- PROTOTYPE. In the build these entries come from shared/principles.md, and the "not a break"
lists from shared/false-positives.md. -->

Each check gives: what a break looks like, what is **not** a break, what to tell them to do, and
a test they can run to know it's fixed. The move names the change and where; it never contains
the words.

## Before any check: know the title

The first line of a slide in `deck.json` is often not its title: a small section label can come
first in the file. Use the slide's `title` field, or the slide image when you can see it.
`largest_text` is the biggest text on the slide: usually the title, but sometimes a number or a
callout, so use it only when it reads as a heading. When none of these tells you which line is
the title, don't build a title or ghost-deck finding on that slide.

## Weak is not absent

Before saying a deck never states something, search every slide for it. If it is there in weak
form (hedged, buried in a list, one point among six), quote that and say what is wrong with it
("your summary says returning donors are 'very promising' in the middle of a paragraph, not as
the answer"). "Never" and "missing" are only for what is truly not in the deck. A consultant who
finds the line you said was missing stops trusting the rest.

## A deck inside the deck

A deliverable often contains something the team made *for* the client to use: a pitch deck for
investors, a template, a guide. Judge the pyramid and the ghost deck on the consultant's own
argument to the client (usually the opening and closing sections), not on the product they made,
which follows its own conventions (a pitch ends on its ask). A divider or contents slide usually
marks where the product starts. The so-what and compared-to-what checks still apply inside the
product: the client will use those slides too.

## 1. The pyramid (governing thought first)

The deck has one governing thought, its answer, and states it before the support. Every section
is a reason for it or evidence for a reason. In a final deliverable the answer is the
recommendation. In a problem analysis or interim deck it is the main finding, or the question
and scope plus what the team already thinks. That counts.

**A break:** the opening slides are agenda, team, context and method, and the answer first
appears late or only at the end; no slide states one answer, only topics; the deck has several
answers of equal weight and never says which one governs; sections that support nothing the
answer says.

**Not a break:** title, team and agenda before a summary that states the answer; a summary table
with its reason nearby.

**Gated:** compare their sentence with slides 1 to 3. If the slides say it, the pyramid holds:
say so under What works. If it appears late, quote where; if nowhere, that is the finding. If
the deck promises to compare options later but its opening already assumes the outcome, that is
a finding too: the reader can't tell whether the choice is made.

**Do this:** state the governing thought on one early slide (usually slide 2) as the answer, and
make each section's opening title one reason for it. **Check it:** read only that slide to
someone outside the project. Can they say what the client should do or believe, and why?

## 2. The title is the so-what

A title states what the slide proves, for this client. "Sign-ups by channel" is a label;
a full-sentence takeaway is a so-what.

**A break:** a title that names a topic ("Market overview", "Competitor analysis", "Survey
results") on a slide whose content carries a conclusion; a takeaway buried in a subtitle or a
body line while the title stays a label; a title so general it is true of any deck ("Competitors
differ in key features"). Pick the slide where it matters most, one the answer leans on.

**Not a break:** dividers, agenda, appendix and title slides; reference slides; a takeaway you
would phrase differently.

When most titles are labels, raise this once, naming the slides, and drop the ghost-deck check:
the fix is the same.

**Do this:** make the title the one thing the slide proves, and move the label into a small
section tag if they want to keep it. **Check it:** could someone disagree with the title? A label
can't be disagreed with. And does the slide still say it if the chart is deleted?

## 3. The ghost deck

Read the titles alone, in order: they should tell the story from the answer down to the next
step. This is how consultants plan a deck before building slides.

**A break:** a title that doesn't follow from the one before it (a jump with no bridge); two titles
saying the same thing; a section whose titles don't support the governing thought; the titles end
without the answer or a next step; the order of the argument differs from the order of slides.

**Not a break:** dividers and appendix; a deliberate recap.

**Do this:** write the titles out as a list on their own, fix the order and the missing links
there, then rebuild the slides to match. **Check it:** read the titles aloud in order. Does a
listener follow the argument without seeing a single slide?

## 4. Compared to what?

Only for figures the answer or a key slide leans on. A number alone doesn't say whether it is
good, bad, big or small. The reader needs where it comes from (source, date) and a comparison:
a benchmark, last year, a competitor, a target.

**A break:** a figure on a key slide with no comparison or no source, so the reader can't tell
what it means; a percentage with no base ("70% of what?"); a claimed gain with no baseline.

Get the wording right: if the deck already names a comparison, even a vague one ("compared to
traditional buildings"), say what is still missing (the source, the basis, the time span), not
that there is none.

**Not a break:** the client's own operating data; a figure whose source and comparison sit in a
footnote, exhibit or appendix (check there first); figures on background slides the answer
doesn't use; a qualitative claim with no figure; an assumption labelled as an assumption.

Raise this once, for the figure that matters most, and name others with the same gap. Name what is
missing; never supply the comparison or the number.

**Do this:** put the comparison the client would decide against right next to the figure, with
its source and date. **Check it:** cover everything but the number and its line. Can a reader
say whether it's good or bad?

## Extraction damage is not a break

The text came out of a file. Empty slides (images, diagrams), numbers detached from labels, text
out of order and placeholder dates on dividers come from the extract, not the consultant. Build
no finding on a chart or table you can't see.
