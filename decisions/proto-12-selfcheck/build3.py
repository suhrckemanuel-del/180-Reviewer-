#!/usr/bin/env python3
"""
PROTOTYPE -- throwaway. Ticket 12, third build, run for ticket 09.

B2 with ONE change: part 1's key is made readable as a version stamp.
  B2:  BUNDLE KEY (part 1): SIGMA-7K
  B3:  BUNDLE KEY (part 1): 0919-SIGMA7K

Ticket 12's Q2 decision rule: the zero-invented-codes property was measured on
meaningless strings only. A date-shaped code is reconstructable from context --
the model can see today's date. Run it. If it invents even one code, the stamp
stays meaningless.

Today is 2026-09-20. The bundle says 0919. A drift to 0920 is an invention.
"""
import json, pathlib, tiktoken

SRC = pathlib.Path(r"C:\Users\User\Desktop\180dc-ai\.scratch\deliverable-reviewer\ticket-11")
OUT = pathlib.Path(__file__).parent / "bundles"
ENC = tiktoken.get_encoding("cl100k_base"); toks = lambda s: len(ENC.encode(s))

P1  = (SRC / "PASTE-1-system-prompt.txt").read_text(encoding="utf-8")
P2A = (SRC / "PASTE-2A-chat-path.md").read_text(encoding="utf-8")
P3  = (SRC / "PASTE-3-deck-A.md").read_text(encoding="utf-8")
KEY1, KEY2 = "0919-SIGMA7K", "DELTA-3Q"

# RULE is byte-identical to build2.py's except for the keys it names.
RULE = """**The KEYS field is not optional and is not yours to invent.** Part 1 is the string given
as `BUNDLE KEY (part 1)` at the top of your system prompt. Part 2 is the string on the last
line of this document. Copy each character for character. If you do not have one of them,
write `MISSING` in its place. Never guess a key and never leave the field off. **If either
key is MISSING, do not produce the review at all: write the first line, say which part is
missing, say that your instructions arrived incomplete, and stop.**
"""

P1_B3 = f"BUNDLE KEY (part 1): {KEY1}\n\n{RULE}\n" + P1

OLD_HDR = "REVIEW OF: <artifact type, one line> | MODE: <short | deep | lead>"
NEW_HDR = OLD_HDR + " | KEYS: <part 1>/<part 2>"
P2A_B3 = P2A.replace(OLD_HDR, NEW_HDR, 1)
ANCHOR = "## The template"
assert ANCHOR in P2A_B3
P2A_B3 = P2A_B3.replace(ANCHOR, RULE + "\n" + ANCHOR, 1)
P2A_B3 = P2A_B3.rstrip("\n") + f"\n\nBUNDLE KEY (part 2): {KEY2}\n"

def tail(t, f):
    ids = ENC.encode(t); return ENC.decode(ids[: int(len(ids) * f)])
def bundle(*p): return "\n\n".join(p)
GO = "\nReview this deliverable now, in your specified format.\n"

ARMS = {
  "B3-full":     bundle(P1_B3, P2A_B3, P3) + GO,          # control: is it copied, or drifted?
  "B3-headdrop": bundle(P2A_B3, P3) + GO,                 # decisive: key1 gone, demand standing
  "B3-tail92":   bundle(P1_B3, tail(P2A_B3, 0.92), P3) + GO,  # key2 gone, key1 present
}
m = json.loads(pathlib.Path("manifest.json").read_text())
m["keys_b3"] = {"part1": KEY1, "part2": KEY2}
for n, t in ARMS.items():
    (OUT / f"{n}.txt").write_text(t, encoding="utf-8")
    m["arms"][n] = {"chars": len(t), "tokens": toks(t), "has_key1": KEY1 in t,
                    "has_key2": KEY2 in t, "has_demand": "KEYS: <part 1>/<part 2>" in t,
                    "has_rule": "do not produce the review at all" in t}
    print(f"{n:<14}{len(t):>8,}  key1={KEY1 in t!s:<5} key2={KEY2 in t!s:<5} "
          f"rule={'do not produce the review at all' in t!s:<5} demand={'KEYS: <part 1>' in t}")
pathlib.Path("manifest.json").write_text(json.dumps(m, indent=2))
