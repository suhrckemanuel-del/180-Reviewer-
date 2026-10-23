# `numbers.json` and `slides.json`

## numbers.json (written by your `compute.py`)

A flat object. Values are numbers or lists of numbers (one per category), plus lists of labels.

```json
{
  "months": ["Jan", "Feb", "Mar"],
  "online_rate": [19.1, 18.5, 19.3],
  "online_rate_jan_jun": 19.0,
  "online_bookings_total": 3657,
  "given_pilot_weeks": 8
}
```

- Store percentages in percent units (19.1, not 0.191), and say so with `"unit": "%"` on the chart.
- Keys starting with `given_` are numbers the consultant stated themselves (a target, a pilot
  length), not computed. The checks accept them and report them as "given by you".
- A ratio the title states ("1.6 times", "a third") needs its own key: compute it, don't infer it.

## slides.json (written by you)

```json
{
  "slides": [
    {
      "title": "<their title, verbatim, or null for the placeholder>",
      "chart": {
        "type": "line",
        "categories": "months",
        "series": [
          {"name": "Online", "key": "online_rate", "highlight": true},
          {"name": "Phone", "key": "phone_rate"}
        ],
        "unit": "%",
        "decimals": 1,
        "y_label": "Missed pickups, % of booked",
        "y_max": 25,
        "event": {"at": "Jul", "label": "Text reminders start, 1 Jul"}
      },
      "caption": "Online bookings only got reminders.",
      "source": "Source: pantry booking log, Jan–Dec, 3,657 online and 1,833 phone bookings",
      "notes": "<their speaker notes, verbatim, or empty>"
    }
  ]
}
```

- `type`: `line`, `column`, `bar` or `stacked100` (see `charts.md`).
- `categories` and every series `key` name lists in numbers.json, all the same length.
  For `stacked100`, categories are the bars ("Bookings", "Missed pickups") and each series is
  one part, in percent, adding to 100 per bar.
- `event` (line and column only) marks a category where something changed. The PNG draws it as a
  dashed line. On the .pptx it's drawn as a dashed line over the editable chart, placed by
  category; if they move or resize the chart, they move the line too.
- `caption` is a label, not a claim: what the chart covers, never what it means. A projection's
  assumption ("Projection: phone bookings missing at the Jul–Dec online rate") is a label.
- `highlight_category` (bar only, optional): the one category to colour green, by name; the
  rest go grey. Use it when the title is about one bar, not one series.
- `y_label` names the value axis for every type (it sits under horizontal bars).
- Keep `y_label` under about 40 characters and `caption` plus `source` under about 120, or the
  PNG wraps and crowds.
- `y_max` and `decimals` are optional.
