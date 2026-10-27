"""PROTOTYPE. The same four slides as a HyperFrames slideshow: fragment reveals, presenter
notes, and one branch slide ("How we computed this") behind a hotspot. Writes
03-hyperframes/index.html from the same three sources as the other artifacts.

Usage: python scripts/build_hf.py   (run from the prototype folder)
"""
import html, json

D = json.load(open("data/recomputed.json", encoding="utf-8"))
C = json.load(open("content/consultant.json", encoding="utf-8"))
SVG = {k: open(f"charts/{k}.svg", encoding="utf-8").read() for k in ("line", "bars")}
S = {s["id"]: s for s in C["slides"]}
esc = html.escape

# absolute timeline: (scene id, start, duration, fragments as absolute times)
PLAN = [("answer", 0, 6, [1.5, 2.5, 3.5]),
        ("trend", 6, 7, [7.5, 9.5, 11.5]),
        ("share", 13, 5, [14.5, 16.0]),
        ("next", 18, 4, []),
        ("method", 22, 3, [])]  # branch slide, reached only from the hotspot

def foot(n):
    return (f'<div class="foot"><img src="assets/180dc-logo.png" alt="180 Degrees Consulting">'
            f'<span>{esc(C["org"])} · invented data · prototype</span><span>{n}</span></div>')

def scene(sid, start, dur, tag, title, body, n, label):
    # not a clip: the one root timeline shows and hides each slide, so a seek from the
    # slideshow lands on the right slide whether or not a scene runtime is loaded
    return (f'    <div id="{sid}" class="scene" data-start="{start}" data-duration="{dur}" data-label="{esc(label)}">\n'
            f'      <div class="tag">{esc(tag)}</div><h1>{esc(title)}</h1>\n'
            f'      <div class="body">{body}</div>{foot(n)}\n    </div>')

a, t, sh, nx = S["answer"], S["trend"], S["share"], S["next"]
reasons = "".join(f'<li id="answer-r{k}"><span>0{k + 2}</span>{esc(r)}</li>' for k, r in enumerate(a["reasons"]))
rows = "".join(f"<tr><th>{esc(k)}</th><td>{esc(v)}</td></tr>" for k, v in nx["rows"])
table = "".join(f"<tr><td>{m}</td><td>{D['online_rate'][i]}%</td><td>{D['phone_rate'][i]}%</td></tr>"
                for i, m in enumerate(D["months"]))
method_body = (
    '<div class="method"><div>'
    '<p>Missed pickup: a booked parcel nobody collected by closing time.</p>'
    '<p>Rate: missed pickups divided by booked pickups, per month and channel.</p>'
    f'<p>Jul–Dec totals: {D["missed_after_total"]} missed, {D["phone_missed_after"]} of them phone bookings.</p>'
    '<p>Every number on these slides comes from recompute.py run on the booking log.</p>'
    '</div><div><table class="data"><tr><th>Month</th><th>Online</th><th>Phone</th></tr>'
    f'{table}</table></div></div>')

timings = {p[0]: p for p in PLAN}
span = lambda sid: {"startTime": timings[sid][1], "endTime": timings[sid][1] + timings[sid][2]}
scenes = [
    scene("answer", 0, 6, a["tag"], a["title"],
          f'<ol class="reasons">{reasons}</ol><p class="footnote" id="answer-fn">{esc(a["footnote"])}</p>', 1, "Answer"),
    scene("trend", 6, 7, t["tag"], t["title"],
          f'<div class="chart" style="height:100%">{SVG["line"]}</div>', 2, "What changed in July"),
    scene("share", 13, 5, sh["tag"], sh["title"], f'<div class="chart" style="height:100%">{SVG["bars"]}</div>', 3, "Where missed pickups come from"),
    scene("next", 18, 4, nx["tag"], nx["title"], f'<table class="rows">{rows}</table>', 4, "Next step"),
    scene("method", 22, 3, "Missed pickups · method", "How the numbers on these slides were computed", method_body, "A", "Method (branch)"),
]

# one root timeline on absolute time; each reveal finishes before its fragment's hold time
scene_sets = "\n".join(
    f'      tl.set("#{sid}", {{ autoAlpha: 1 }}, {start}); tl.set("#{sid}", {{ autoAlpha: 0 }}, {start + dur - 0.001});'
    for sid, start, dur, _ in PLAN)
JS = """      window.__timelines = window.__timelines || {};
      const tl = gsap.timeline({ paused: true });
      const show = (sel, at) => tl.fromTo(sel, { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.4, ease: "power2.out" }, at);
""" + scene_sets + """
      show("#answer-r0", 1.0); show("#answer-r1", 2.0); show("#answer-r2", 3.0); show("#answer-fn", 3.0);
      show("#ln-before", 7.0); show("#ln-event", 9.0); show("#ln-after", 11.0);
      show("#bar-0", 14.0); show("#bar-1", 15.5);
      tl.set({}, {}, 25);
      window.__timelines["root"] = tl;
      tl.seek(0);"""

island = {
    "slides": [
        {"sceneId": "answer", **span("answer"), "notes": a["notes"], "fragments": timings["answer"][3]},
        {"sceneId": "trend", **span("trend"), "notes": t["notes"], "fragments": timings["trend"][3],
         "hotspots": [{"id": "how", "label": "How we computed this", "target": "method-seq",
                       "region": {"x": 75, "y": 26, "w": 20, "h": 6}}]},
        {"sceneId": "share", **span("share"), "notes": sh["notes"], "fragments": timings["share"][3]},
        {"sceneId": "next", **span("next"), "notes": nx["notes"]},
    ],
    "slideSequences": [{"id": "method-seq", "label": "Method", "slides": [
        {"sceneId": "method", **span("method"), "notes": "Only if asked. Every figure traces back to one script run on the booking log."}]}],
}

page = open("src/03-hf.html", encoding="utf-8").read()
page = (page.replace("{{ISLAND}}", json.dumps(island, indent=2, ensure_ascii=False))
            .replace("{{SCENES}}", '    <div id="root" data-composition-id="root" data-start="0" data-duration="25" '
                     'data-width="1920" data-height="1080">\n' + "\n".join(scenes) + "\n    </div>")
            .replace("{{TIMELINES}}", JS))
open("03-hyperframes/index.html", "w", encoding="utf-8").write(page)
print("wrote 03-hyperframes/index.html")
