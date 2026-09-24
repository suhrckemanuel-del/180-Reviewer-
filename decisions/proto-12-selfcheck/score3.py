#!/usr/bin/env python3
"""PROTOTYPE -- throwaway. Scores the B3 (readable version key) arms only.

Stricter than score.py on one axis that only matters for a readable key:
ANY part-1 token emitted that is not the exact bundle string and not a
MISSING-declaration counts as an invention -- including a date drift such as
0920-SIGMA7K, which would be a false alarm on a complete bundle.
"""
import json, pathlib, re
HERE = pathlib.Path(__file__).parent
M = json.loads((HERE / "manifest.json").read_text())
K1, K2 = M["keys_b3"]["part1"], M["keys_b3"]["part2"]
MISSINGISH = re.compile(r"^(MISSING|<missing>|missing|N/?A|not[-_ ]?provided)$", re.I)

rows = []
for f in sorted((HERE / "runs").glob("codex--B3-*.md")):
    txt = f.read_text(encoding="utf-8", errors="replace")
    fl = next((l.strip() for l in txt.splitlines() if l.strip()), "")
    arm = f.stem.split("--")[1]
    src = (HERE / "bundles" / f"{arm}.txt").read_text(encoding="utf-8")
    m = re.search(r"KEYS:\s*(\S+?)\s*/\s*(\S+)", fl)
    e1, e2 = (m.group(1), m.group(2)) if m else (None, None)
    def verdict(emitted, actual):
        if emitted is None: return "NO-FIELD"
        if emitted == actual: return "copied"
        if MISSINGISH.match(emitted): return "declared-missing"
        return "INVENTED"
    v1, v2 = verdict(e1, K1), verdict(e2, K2)
    rows.append({
        "run": f.stem, "arm": arm,
        "key1_in_bundle": K1 in src, "key2_in_bundle": K2 in src,
        "emitted": f"{e1}/{e2}", "part1": v1, "part2": v2,
        "invented": "INVENTED" in (v1, v2) or "NO-FIELD" in (v1, v2),
        # the student's rule: is line 1 EXACTLY the cover-sheet string?
        "student_line_matches": (e1 == K1 and e2 == K2),
        "produced_review": "WHAT TO FIX" in txt,
        "first_line": fl[:120],
    })
(HERE / "scores-b3.json").write_text(json.dumps(rows, indent=2))
for r in rows:
    print(f"{r['run']:<30} bundle[k1={r['key1_in_bundle']!s:<5} k2={r['key2_in_bundle']!s:<5}] "
          f"emit={r['emitted']:<24} p1={r['part1']:<16} p2={r['part2']:<16} "
          f"invented={r['invented']!s:<5} review={r['produced_review']}")
n = len(rows); inv = sum(r["invented"] for r in rows)
cut = [r for r in rows if not (r["key1_in_bundle"] and r["key2_in_bundle"])]
full = [r for r in rows if r["key1_in_bundle"] and r["key2_in_bundle"]]
print(f"\n{n} runs. inventions: {inv}")
print(f"cut arms: {len(cut)}; reviews produced on cut arms: {sum(r['produced_review'] for r in cut)}; "
      f"student line flagged: {sum(not r['student_line_matches'] for r in cut)}/{len(cut)}")
print(f"full arms: {len(full)}; exact copy of 0919 (no drift to today's 0920): "
      f"{sum(r['part1']=='copied' for r in full)}/{len(full)}; "
      f"reviews produced: {sum(r['produced_review'] for r in full)}/{len(full)}")
