#!/usr/bin/env python3
"""
PROTOTYPE -- throwaway. Ticket 04.

The quote-or-abstain check on its own, over every run, looking ONLY at fields
the reply actually offers as evidence:

    "quote": "..."        JSON branch
    quote: "..."          the HTML data object
    Quote: "..."          the prose format

score.py has a loose fallback for replies that lost the template entirely; that
fallback catches ordinary prose in quotation marks and inflates the fabricated
count. This file does not guess. If a reply names no evidence field, it says so
rather than scoring it.
"""
import pathlib
import re

KIT = pathlib.Path(r"C:\Users\User\Desktop\180dc-ai\tools\quality-reviewer\v2\TEST-KIT")
RUNS = pathlib.Path(__file__).parent / "runs"

DQ = r'"((?:[^"' + "\\\\" + r']|' + "\\\\" + r'.)*)"'
PATTERNS = [
    r'"quote"\s*:\s*' + DQ,          # JSON branch
    r'\bquotes?\s*:\s*\[?\s*' + DQ,  # HTML data object
    r'Quote:\s*' + DQ,               # prose format
]


def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def main():
    deck = norm(
        KIT.joinpath("PASTE-3-deck-A.md")
        .read_text(encoding="utf-8")
        .split("DELIVERABLE TEXT", 1)[-1]
    )

    for f in sorted(RUNS.glob("*.md")):
        text = f.read_text(encoding="utf-8", errors="replace")
        qs = []
        for pat in PATTERNS:
            qs += [m.group(1) for m in re.finditer(pat, text)]
        qs = [q.replace('\\"', '"').replace("\\n", " ") for q in qs]
        qs = [q for q in qs if len(q) >= 8]

        if not qs:
            print(f"{f.stem:<26} -- no evidence field in this reply")
            continue

        bad = [q for q in qs if norm(q) not in deck]
        flag = "   <<< FABRICATED" if bad else ""
        print(f"{f.stem:<26} {len(qs) - len(bad)}/{len(qs)} verbatim{flag}")
        for b in bad[:3]:
            print(f"      {b[:110]}")


if __name__ == "__main__":
    main()
