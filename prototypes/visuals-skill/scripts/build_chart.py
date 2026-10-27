"""PROTOTYPE. Draw the two charts as static SVG from recomputed.json, so every artifact
(chart page, HTML deck, HyperFrames deck) shows the same marks and the same numbers.

No title inside the SVG: the title is the consultant's, it lives on the slide.
The source line is inside, so a pasted image keeps it.

Usage: python build_chart.py <recomputed.json> <out_dir>
"""
import json, sys, os

d = json.load(open(sys.argv[1]))
out = sys.argv[2]
GREEN, PHONE, INK, MUTED, GRID = "#78B038", "#3A3F45", "#1D2124", "#6B7075", "#E4E6E1"
FONT = "'IBM Plex Sans', Inter, Arial, sans-serif"
SOURCE = (f"Source: pantry booking log, Jan–Dec, {d['online_booked_total']:,} online and "
          f"{d['phone_booked_total']:,} phone bookings. Invented data for a prototype.")

def line_chart():
    W, H = 1600, 760
    x0, x1, y0, y1 = 120, 1250, 50, 600  # plot box
    ymax = 25
    n = len(d["months"])
    X = lambda i: x0 + i * (x1 - x0) / (n - 1)
    Y = lambda v: y1 - v / ymax * (y1 - y0)
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{FONT}" role="img" '
         f'aria-label="Missed pickup rate by month, online and phone bookings">']
    for v in range(0, ymax + 1, 5):
        s.append(f'<line x1="{x0}" x2="{x1}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke="{GRID}" stroke-width="{2 if v == 0 else 1}"/>')
        s.append(f'<text x="{x0 - 16}" y="{Y(v) + 8:.1f}" text-anchor="end" font-size="30" fill="{MUTED}">{v}%</text>')
    for i, m in enumerate(d["months"]):
        s.append(f'<text x="{X(i):.1f}" y="{y1 + 42}" text-anchor="middle" font-size="30" fill="{MUTED}">{m}</text>')
    def lines(a, b, ends):
        for key, col, w in (("phone_rate", PHONE, 3), ("online_rate", GREEN, 4)):
            pts = " ".join(f"{X(i):.1f},{Y(d[key][i]):.1f}" for i in range(a, b + 1))
            s.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"/>')
            s.append(f'<circle cx="{X(ends):.1f}" cy="{Y(d[key][ends]):.1f}" r="7" fill="{col}" stroke="#fff" stroke-width="2"/>')
    def band(a, b, v):  # half-year average for online: the number the title quotes
        s.append(f'<line x1="{X(a):.1f}" x2="{X(b):.1f}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke="{GREEN}" stroke-width="10" stroke-opacity="0.22"/>')
    # groups let the HyperFrames deck reveal before, event, after; static charts show all three
    s.append('<g id="ln-before">')
    band(0, 5, d["online_before"])
    lines(0, 5, 0)
    s.append(f'<text x="{X(0):.1f}" y="{Y(d["online_before"]) - 22:.1f}" font-size="30" fill="{MUTED}">Jan–Jun avg, both channels: {d["online_before"]}%</text>')
    s.append('</g><g id="ln-event">')
    xm = (X(5) + X(6)) / 2
    s.append(f'<line x1="{xm:.1f}" x2="{xm:.1f}" y1="{y0 - 10}" y2="{y1}" stroke="{INK}" stroke-width="2" stroke-dasharray="6 6"/>')
    s.append(f'<text x="{xm + 14:.1f}" y="{y0 + 14}" font-size="30" fill="{INK}" font-weight="600">Text reminders start</text>')
    s.append(f'<text x="{xm + 14:.1f}" y="{y0 + 44}" font-size="30" fill="{MUTED}">online bookings only</text>')
    s.append('</g><g id="ln-after">')
    band(6, 11, d["online_after"])
    lines(5, 11, n - 1)
    # direct labels at the right end
    s.append(f'<text x="{x1 + 22}" y="{Y(d["phone_rate"][-1]) - 4:.1f}" font-size="32" font-weight="600" fill="{INK}">Phone</text>')
    s.append(f'<text x="{x1 + 22}" y="{Y(d["phone_rate"][-1]) + 34:.1f}" font-size="30" fill="{MUTED}">Jul–Dec avg {d["phone_after"]}%</text>')
    s.append(f'<text x="{x1 + 22}" y="{Y(d["online_rate"][-1]) - 4:.1f}" font-size="32" font-weight="600" fill="{INK}">Online</text>')
    s.append(f'<text x="{x1 + 22}" y="{Y(d["online_rate"][-1]) + 34:.1f}" font-size="30" fill="{MUTED}">Jul–Dec avg {d["online_after"]}%</text>')
    s.append('</g>')
    s.append(f'<text x="{x0 - 100}" y="{H - 30}" font-size="22" fill="{MUTED}">Missed pickups as a share of booked pickups. {SOURCE}</text>')
    s.append("</svg>")
    return "\n".join(s)

def share_bars():
    W, H = 1600, 760
    x0, x1 = 330, 1500
    rows = (("Bookings", d["phone_share_of_bookings_after"]), ("Missed pickups", d["phone_share_of_missed_after"]))
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{FONT}" role="img" '
         f'aria-label="Phone bookings share of bookings and of missed pickups, July to December">']
    s.append(f'<text x="{x0}" y="70" font-size="32" font-weight="600" fill="{INK}">Phone</text>')
    s.append(f'<rect x="{x0 - 30}" y="50" width="20" height="20" fill="{PHONE}"/>')
    s.append(f'<text x="{x0 + 150}" y="70" font-size="32" font-weight="600" fill="{INK}">Online</text>')
    s.append(f'<rect x="{x0 + 120}" y="50" width="20" height="20" fill="{GREEN}"/>')
    s.append(f'<text x="{x1}" y="70" text-anchor="end" font-size="30" fill="{MUTED}">Share of Jul–Dec total</text>')
    for r, (label, p) in enumerate(rows):
        y = 150 + r * 230
        bw = x1 - x0
        pw = bw * p / 100
        s.append(f'<g id="bar-{r}">')
        s.append(f'<text x="{x0 - 30}" y="{y + 72}" text-anchor="end" font-size="30" font-weight="600" fill="{INK}">{label}</text>')
        s.append(f'<rect x="{x0}" y="{y}" width="{pw - 1:.1f}" height="110" fill="{PHONE}"/>')
        s.append(f'<rect x="{x0 + pw + 1:.1f}" y="{y}" width="{bw - pw - 1:.1f}" height="110" fill="{GREEN}"/>')
        s.append(f'<text x="{x0 + 24}" y="{y + 70}" font-size="40" font-weight="600" fill="#fff">{p}%</text>')
        s.append(f'<text x="{x1 - 24}" y="{y + 70}" text-anchor="end" font-size="34" fill="{INK}">{round(100 - p, 1)}%</text>')
        s.append('</g>')
    s.append(f'<line x1="{x0 + (x1 - x0) / 2:.1f}" x2="{x0 + (x1 - x0) / 2:.1f}" y1="130" y2="630" stroke="{INK}" stroke-width="1" stroke-dasharray="4 6"/>')
    s.append(f'<text x="{x0 + (x1 - x0) / 2 + 10:.1f}" y="655" font-size="22" fill="{MUTED}">50%</text>')
    s.append(f'<text x="20" y="{H - 30}" font-size="22" fill="{MUTED}">Jul–Dec: {d["phone_missed_after"]} of {d["missed_after_total"]} missed pickups were phone bookings. {SOURCE}</text>')
    s.append("</svg>")
    return "\n".join(s)

os.makedirs(out, exist_ok=True)
open(os.path.join(out, "line.svg"), "w", encoding="utf-8").write(line_chart())
open(os.path.join(out, "bars.svg"), "w", encoding="utf-8").write(share_bars())
print("wrote line.svg, bars.svg")
