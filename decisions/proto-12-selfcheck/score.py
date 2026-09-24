#!/usr/bin/env python3
"""PROTOTYPE -- throwaway. Ticket 12. Scores every reply in ./runs."""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).parent
M = json.loads((HERE / "manifest.json").read_text())
K1, K2 = M["keys"]["part1"], M["keys"]["part2"]

def first_line(t):
    for l in t.splitlines():
        if l.strip():
            return l.strip()
    return ""

def score(name, txt):
    arm = name.split("--")[1]
    src = (HERE / "bundles" / f"{arm}.txt").read_text(encoding="utf-8")
    fl = first_line(txt)
    r = {"run": name, "arm": arm,
         "key1_in_bundle": K1 in src, "key2_in_bundle": K2 in src,
         "opens_REVIEW_OF": fl.startswith("REVIEW OF:"),
         "has_KEYS_field": "KEYS:" in txt[:400],
         "emits_K1": K1 in txt, "emits_K2": K2 in txt,
         "says_MISSING": bool(re.search(r"MISSING", txt[:1200])),
         "refused": bool(re.search(r"incomplete|did not (arrive|receive)|cannot produce|not produce the review|instructions arrived", txt[:2500], re.I)),
         "first_line": fl[:160]}
    # candidate A scoring: the three recall markers
    if arm.startswith("A-"):
        r["marker1_pasteA"] = ("Learning Coach" in txt) and ("Recommendation and Implementation" in txt)
        r["marker2_format"] = "REVIEW OF:" in txt
        r["marker3_tail"]   = "phone" in txt.lower()
    else:
        # verdict a student can reach with two string comparisons
        want1, want2 = r["key1_in_bundle"], r["key2_in_bundle"]
        got1, got2 = r["emits_K1"], r["emits_K2"]
        r["student_verdict"] = ("PASS" if (got1 and got2) else "FLAG")
        r["correct"] = (r["student_verdict"] == "PASS") == (want1 and want2)
        emitted = [x for pair in re.findall(r"KEYS:\s*(\S+)\s*/\s*(\S+)", fl) for x in pair]
        r["confabulated_key"] = any(x not in (K1, K2, "MISSING") for x in emitted)
        r["produced_review"] = "WHAT TO FIX" in txt
    return r

rows = []
for f in sorted((HERE / "runs").glob("*.md")):
    if f.stat().st_size == 0: continue
    rows.append(score(f.stem, f.read_text(encoding="utf-8", errors="replace")))

(HERE / "scores.json").write_text(json.dumps(rows, indent=2))
for r in rows:
    if r["arm"].startswith("A-"):
        print(f"{r['run']:<34} m1={r['marker1_pasteA']!s:<5} m2={r['marker2_format']!s:<5} m3={r['marker3_tail']!s:<5}")
    else:
        print(f"{r['run']:<34} bundle[k1={r['key1_in_bundle']!s:<5} k2={r['key2_in_bundle']!s:<5}] "
              f"emit[k1={r['emits_K1']!s:<5} k2={r['emits_K2']!s:<5}] "
              f"{r['student_verdict']:<5} correct={r['correct']!s:<5} refused={r['refused']!s:<5} confab={r['confabulated_key']}")
        print(f"{'':<34}  |{r['first_line']}")
