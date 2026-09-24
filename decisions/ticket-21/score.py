#!/usr/bin/env python3
"""PROTOTYPE -- throwaway. Ticket 21. One row per run: did the gate fire, did the
marker appear, was it verbatim, was it on the right line."""
import pathlib, re, json
ATT_LONG=("My own read first: I think the weakest part is that we never say what the "
 "client should actually do on Monday morning. We describe the market well but "
 "the recommendation stays abstract, and I suspect our cost numbers are pulled "
 "from one source we never name.")
ATT_SHORT="the recommendation is too vague to act on"
ATT_THIN="not sure honestly, looks fine to me"
POOL=[ATT_LONG,ATT_SHORT,ATT_THIN]
rows=[]
for f in sorted(pathlib.Path("runs").glob("*.md")):
    if f.name.endswith(".stderr.txt"): continue
    t=f.read_text(encoding="utf-8",errors="replace")
    lines=[l for l in t.splitlines() if l.strip()]
    refused="ATTEMPT REQUIRED" in t and len(t)<400
    m=re.search(r'ATTEMPT ON RECORD:\s*"(.*?)"',t)
    marker_line=None
    for i,l in enumerate(lines[:12]):
        if l.startswith("ATTEMPT ON RECORD:"): marker_line=i+1; break
    verb = any(m.group(1).strip() in a for a in POOL) if m else None
    runner,arm=f.stem.split("--",1)
    rows.append(dict(runner=runner,arm=arm,refused=refused,
        reviewed=not refused and len(t)>2000,
        marker=bool(m),marker_line=marker_line,marker_verbatim=verb,
        opens_review_of=bool(lines and lines[0].startswith("REVIEW OF:")),bytes=len(t)))
print(f"{'runner':<7}{'arm':<24}{'refused':>8}{'reviewed':>9}{'marker':>8}{'line':>6}{'verbatim':>9}{'REVIEWOF#1':>11}")
for r in rows:
    print(f"{r['runner']:<7}{r['arm']:<24}{str(r['refused']):>8}{str(r['reviewed']):>9}"
          f"{str(r['marker']):>8}{str(r['marker_line']):>6}{str(r['marker_verbatim']):>9}{str(r['opens_review_of']):>11}")
pathlib.Path("scores.json").write_text(json.dumps(rows,indent=2),encoding="utf-8")
