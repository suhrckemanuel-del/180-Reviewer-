#!/usr/bin/env python3
"""PROTOTYPE -- throwaway. Ticket 12. Final tally across every arm."""
import pathlib, re, collections
K1, K2 = "SIGMA-7K", "DELTA-3Q"
GOOD = f"KEYS: {K1}/{K2}"
t = collections.OrderedDict()
for f in sorted(pathlib.Path("runs").glob("*.md")):
    if not f.stat().st_size or "A-probe" in f.stem: continue
    txt = f.read_text(encoding="utf-8", errors="replace")
    fl = next((l.strip() for l in txt.splitlines() if l.strip()), "")
    runner, arm, _ = f.stem.split("--")
    src = pathlib.Path("bundles", arm + ".txt").read_text(encoding="utf-8")
    intact = (K1 in src) and (K2 in src)
    # the student's check, exactly as a student would perform it:
    student_ok = GOOD in fl
    row = t.setdefault(arm, dict(n=0, intact=intact, agree=0, reviewed=0,
                                 invented=0, rule=("do not produce the review at all" in src)))
    row["n"] += 1
    row["agree"] += (student_ok == intact)
    row["reviewed"] += ("WHAT TO FIX" in txt or '"findings"' in txt)
    pair = re.findall(r"KEYS:\s*(\S+)\s*/\s*([^|\n]+)", fl)
    for a, b in pair:
        for x in (a.strip(), b.strip()):
            if x in (K1, K2): continue
            if re.fullmatch(r"(MISSING|<missing>|part 2 (missing|not provided)|missing)", x, re.I): continue
            row["invented"] += 1
print(f"{'arm':<14}{'bundle':<9}{'rule':<6}{'n':<4}{'student check right':<21}{'review produced':<17}{'invented keys'}")
for a, r in t.items():
    print(f"{a:<14}{'intact' if r['intact'] else 'CUT':<9}{'Y' if r['rule'] else 'cut':<6}{r['n']:<4}"
          f"{f'{r[chr(97)+chr(103)+chr(114)+chr(101)+chr(101)]}/{r[chr(110)]}':<21}{f'{r[chr(114)+chr(101)+chr(118)+chr(105)+chr(101)+chr(119)+chr(101)+chr(100)]}/{r[chr(110)]}':<17}{r['invented']}")
