# Which chart, and how to draw it

Pick the form from the comparison the title makes, not from the data's shape.

| The title compares | Chart (`type` in slides.json) |
| --- | --- |
| A change over time, or before and after an event | `line`, with an `event` marker on the date it changed |
| A few groups at two points (before/after, last year/this year) | `column`, clustered, the two points as series |
| Groups against each other on one measure | `bar` (horizontal), sorted largest first unless the order means something; "Other" always last. Survey answers: chart counts, shares in the numbers table |
| Parts of a whole, or shares in two populations | `stacked100` (horizontal), at most 4 parts |
| One number against a target | no chart: a large figure and its target in the caption, or a `bar` with two bars |

When two forms fit, pick the one that shows whether the claim holds across periods or groups
(two groups by season beats one pooled pair of bars), and keep the pooled figures in the
numbers table.

## Drawing rules

- **Highlight the subject.** The series the title is about is `"highlight": true`, or the one
  bar is `"highlight_category"` (180DC green). Everything else is grey. One highlight per
  chart, none before they have a title.
- **Few series.** Line: at most 4. More than that: fold the rest into "Other", or split slides.
- **Label directly.** Line ends carry the series name and last value; bars carry their values.
  The legend shows only when there are 2 or more series and direct labels can't do the job.
- **Bars start at zero.** Lines may start above zero when the change is small, but say so in
  the axis label.
- **Units on the axis or in the label**, never left to guess: %, €, people, parcels.
- **The source line** names the dataset, the period and the count of rows or records. If they
  haven't said where the data comes from, use `Source: [add source]` and tell them.
- **Text a reader needs** is 14 pt or more on the slide. If it doesn't fit, cut categories.
- No pie, donut, 3D, dual axis, gradient or shadow.
