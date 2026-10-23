"""PROTOTYPE. Fill the chart page and the HTML deck from three sources, each owned by one side:
  data/recomputed.json   numbers (script)
  content/consultant.json   titles, lines, notes (the consultant's words, used verbatim)
  charts/*.svg           marks (script)
Writes single-file pages (01-chart.html, 02-deck.html) at the prototype root, the way a
claude.ai artifact would be one file.

Usage: python scripts/build_pages.py   (run from the prototype folder)
"""
import base64, html, json, re

D = json.load(open("data/recomputed.json", encoding="utf-8"))
C = json.load(open("content/consultant.json", encoding="utf-8"))
SVG = {k: open(f"charts/{k}.svg", encoding="utf-8").read() for k in ("line", "bars")}
LOGO = "data:image/png;base64," + base64.b64encode(open("assets/180dc-logo.png", "rb").read()).decode()
S = {s["id"]: s for s in C["slides"]}
esc = html.escape

def fill(text, extra):
    def sub(m):
        k = m.group(1)
        if k in extra:
            return extra[k]
        return str(D[k])
    return re.sub(r"\{\{(\w+)\}\}", sub, text)

# 01: chart page
page = open("src/01-chart.html", encoding="utf-8").read()
open("01-chart.html", "w", encoding="utf-8").write(fill(page, {
    "title_line": esc(S["trend"]["title"]),
    "LINE_SVG": SVG["line"],
    "DATA": json.dumps(D),
}))

# 02: deck
def foot(n):
    return (f'<div class="foot"><img src="{LOGO}" alt="180 Degrees Consulting">'
            f'<span>{esc(C["org"])} · invented data · prototype</span><span>{n}</span></div>')

def slide(s, n, body):
    return (f'<section class="slide" data-notes="{esc(s["notes"])}">'
            f'<div class="tag">{esc(s["tag"])}</div><h1>{esc(s["title"])}</h1>'
            f'<div class="body">{body}</div>{foot(n)}</section>')

a = S["answer"]
reasons = "".join(f"<li><span>0{k + 2}</span>{esc(r)}</li>" for k, r in enumerate(a["reasons"]))
rows = "".join(f"<tr><th>{esc(k)}</th><td>{esc(v)}</td></tr>" for k, v in S["next"]["rows"])
slides = [
    slide(a, 1, f'<ol class="reasons">{reasons}</ol><p class="footnote">{esc(a["footnote"])}</p>'),
    slide(S["trend"], 2, f'<div class="chart" style="height:100%">{SVG["line"]}</div>'),
    slide(S["share"], 3, f'<div class="chart" style="height:100%">{SVG["bars"]}</div>'),
    slide(S["next"], 4, f'<table class="rows">{rows}</table>'),
]
deck = open("src/02-deck.html", encoding="utf-8").read()
open("02-deck.html", "w", encoding="utf-8").write(deck.replace("{{SLIDES}}", "\n".join(slides)))
print("wrote 01-chart.html, 02-deck.html")
