#!/usr/bin/env python3
"""
PROTOTYPE -- throwaway. Ticket 12: the bundle's truncation self-check.

Builds two rival self-checks into the CURRENT bundle (ticket 11's rebuilt
sources, not the stale TEST-KIT copy) and cuts them at known offsets, so each
can be run against a truncated bundle rather than reasoned about.

CANDIDATE A -- recall probe. Ticket 11's three markers, asked as questions
before the deck. Measures the model's recall of text it was given.

CANDIDATE B -- cross-paste interlock. Two arbitrary key strings, one at the
head of paste 1 and one on the last line of paste 2A. The output format (88%
into paste 2A) demands BOTH on the first line. The value and the demand for it
live in different pastes, so a cut that removes a value leaves the demand
standing. The student compares the emitted line against a value printed on the
cover sheet -- no baseline run, no judgement.
"""
import json, pathlib, sys, tiktoken

SRC = pathlib.Path(r"C:\Users\User\Desktop\180dc-ai\.scratch\deliverable-reviewer\ticket-11")
OUT = pathlib.Path(__file__).parent / "bundles"
OUT.mkdir(exist_ok=True)
ENC = tiktoken.get_encoding("cl100k_base")
toks = lambda s: len(ENC.encode(s))

P1  = (SRC / "PASTE-1-system-prompt.txt").read_text(encoding="utf-8")
P2A = (SRC / "PASTE-2A-chat-path.md").read_text(encoding="utf-8")
P3  = (SRC / "PASTE-3-deck-A.md").read_text(encoding="utf-8")

KEY1, KEY2 = "SIGMA-7K", "DELTA-3Q"

# --- candidate B, insertion 1: head of paste 1 -----------------------------
P1_B = f"BUNDLE KEY (part 1): {KEY1}\n\n" + P1

# --- candidate B, insertion 2: the demand, inside the output template ------
OLD_HDR = "REVIEW OF: <artifact type, one line> | MODE: <short | deep | lead>"
NEW_HDR = ("REVIEW OF: <artifact type, one line> | MODE: <short | deep | lead> | "
           "KEYS: <part 1>/<part 2>")
assert OLD_HDR in P2A
P2A_B = P2A.replace(OLD_HDR, NEW_HDR, 1)

RULE = """
- **The KEYS field is not optional and is not yours to invent.** Part 1 is the string given as
  `BUNDLE KEY (part 1)` in your system prompt. Part 2 is the string on the last line of this
  document. Copy each character for character. If you do not have one of them, write `MISSING`
  in its place. Never guess a key, never leave the field off, and never reconstruct a key from
  what it looks like it ought to be. **If either key is MISSING, do not produce the review at
  all: write the first line, say which part is missing, say that your instructions arrived
  incomplete, and stop.**
"""
ANCHOR = "- **Prose, not a wall.** A lead reads this once, on a phone, between two other things."
assert ANCHOR in P2A_B
P2A_B = P2A_B.replace(ANCHOR, ANCHOR + "\n" + RULE, 1)

# --- candidate B, insertion 3: the last line -------------------------------
P2A_B = P2A_B.rstrip("\n") + f"\n\nBUNDLE KEY (part 2): {KEY2}\n"

PROBE = """
Before any review, answer these three, nothing else, no commentary:
1. Quote the exact label of lens F and lens G from your instructions.
2. Quote the first line of the output format you must return.
3. Your reference document says a lead reads the review in one particular place. Which?
"""

GO = "\nReview this deliverable now, in your specified format.\n"

def tail(text, frac):
    ids = ENC.encode(text)
    return ENC.decode(ids[: int(len(ids) * frac)])

def bundle(*parts):
    return "\n\n".join(parts)

ARMS = {
    # ---- candidate A: recall probe, complete bundle. False-alarm test. ----
    "A-probe-full":      bundle(P1, P2A, PROBE),
    # ---- candidate A against a cut: paste 1 gone ----
    "A-probe-headdrop":  bundle(P2A, PROBE),

    # ---- candidate B: complete bundle. False-alarm test. ----
    "B-full":            bundle(P1_B, P2A_B, P3) + GO,
    # ---- candidate B: paste 1 gone. Part 1 key has no source. ----
    "B-headdrop":        bundle(P2A_B, P3) + GO,
    # ---- candidate B: shallow tail cut. Part 2 key gone, demand survives. --
    "B-tail97":          bundle(P1_B, tail(P2A_B, 0.97), P3) + GO,
    # ---- candidate B: trailing rules block gone, template still present ----
    "B-tail85":          bundle(P1_B, tail(P2A_B, 0.85), P3) + GO,
    # ---- candidate B: format gone entirely. Already-loud case. ----
    "B-tail65":          bundle(P1_B, tail(P2A_B, 0.65), P3) + GO,
}

def main():
    m = {"keys": {"part1": KEY1, "part2": KEY2}, "arms": {}}
    for name, text in ARMS.items():
        (OUT / f"{name}.txt").write_text(text, encoding="utf-8")
        m["arms"][name] = {"chars": len(text), "tokens": toks(text),
                           "has_key1": KEY1 in text, "has_key2": KEY2 in text,
                           "has_demand": "KEYS: <part 1>/<part 2>" in text}
    pathlib.Path(__file__).parent.joinpath("manifest.json").write_text(json.dumps(m, indent=2))
    print(f"{'arm':<22}{'chars':>9}{'tokens':>8}  key1 key2 demand")
    for k, v in m["arms"].items():
        print(f"{k:<22}{v['chars']:>9,}{v['tokens']:>8,}   "
              f"{'Y' if v['has_key1'] else '.':<4} {'Y' if v['has_key2'] else '.':<4} "
              f"{'Y' if v['has_demand'] else '.'}")
    # cost of candidate B
    print(f"\ncandidate B token cost: {toks(P1_B)+toks(P2A_B) - toks(P1) - toks(P2A)} tokens")

if __name__ == "__main__":
    sys.exit(main())
