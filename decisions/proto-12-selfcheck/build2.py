#!/usr/bin/env python3
"""
PROTOTYPE -- throwaway. Ticket 12, second build.

B put the KEYS rule at the tail of paste 2A, and the tail arms cut it off, so
refusal was never tested on a tail cut. B2 moves the rule to sit WITH the
output template (~88% depth) and states it a second time in paste 1, beside
the key -- the quote-or-abstain precedent ticket 04 identified.
"""
import json, pathlib, tiktoken

SRC = pathlib.Path(r"C:\Users\User\Desktop\180dc-ai\.scratch\deliverable-reviewer\ticket-11")
OUT = pathlib.Path(__file__).parent / "bundles"
ENC = tiktoken.get_encoding("cl100k_base"); toks = lambda s: len(ENC.encode(s))

P1  = (SRC / "PASTE-1-system-prompt.txt").read_text(encoding="utf-8")
P2A = (SRC / "PASTE-2A-chat-path.md").read_text(encoding="utf-8")
P3  = (SRC / "PASTE-3-deck-A.md").read_text(encoding="utf-8")
KEY1, KEY2 = "SIGMA-7K", "DELTA-3Q"

RULE = """**The KEYS field is not optional and is not yours to invent.** Part 1 is the string given
as `BUNDLE KEY (part 1)` at the top of your system prompt. Part 2 is the string on the last
line of this document. Copy each character for character. If you do not have one of them,
write `MISSING` in its place. Never guess a key and never leave the field off. **If either
key is MISSING, do not produce the review at all: write the first line, say which part is
missing, say that your instructions arrived incomplete, and stop.**
"""

# paste 1: key at the very top, rule stated beside it
P1_B2 = f"BUNDLE KEY (part 1): {KEY1}\n\n{RULE}\n" + P1

# paste 2A: header demands both keys, rule restated with the template (~88%)
OLD_HDR = "REVIEW OF: <artifact type, one line> | MODE: <short | deep | lead>"
NEW_HDR = OLD_HDR + " | KEYS: <part 1>/<part 2>"
P2A_B2 = P2A.replace(OLD_HDR, NEW_HDR, 1)
ANCHOR = "## The template"
assert ANCHOR in P2A_B2
P2A_B2 = P2A_B2.replace(ANCHOR, RULE + "\n" + ANCHOR, 1)
P2A_B2 = P2A_B2.rstrip("\n") + f"\n\nBUNDLE KEY (part 2): {KEY2}\n"

def tail(t, f):
    ids = ENC.encode(t); return ENC.decode(ids[: int(len(ids) * f)])
def bundle(*p): return "\n\n".join(p)
GO = "\nReview this deliverable now, in your specified format.\n"

ARMS = {
  "B2-full":     bundle(P1_B2, P2A_B2, P3) + GO,
  "B2-tail97":   bundle(P1_B2, tail(P2A_B2, 0.97), P3) + GO,
  "B2-tail92":   bundle(P1_B2, tail(P2A_B2, 0.92), P3) + GO,
  "B2-headdrop": bundle(P2A_B2, P3) + GO,
}
m = json.loads(pathlib.Path("manifest.json").read_text())
for n, t in ARMS.items():
    (OUT / f"{n}.txt").write_text(t, encoding="utf-8")
    m["arms"][n] = {"chars": len(t), "tokens": toks(t), "has_key1": KEY1 in t,
                    "has_key2": KEY2 in t, "has_demand": "KEYS: <part 1>/<part 2>" in t,
                    "has_rule": "do not produce the review at all" in t}
    print(f"{n:<14}{len(t):>8,}  key1={KEY1 in t!s:<5} key2={KEY2 in t!s:<5} "
          f"rule={'do not produce the review at all' in t!s:<5} demand={'KEYS: <part 1>' in t}")
pathlib.Path("manifest.json").write_text(json.dumps(m, indent=2))
print(f"\nB2 token cost: {toks(P1_B2)+toks(P2A_B2)-toks(P1)-toks(P2A)} tokens")
