#!/usr/bin/env python3
"""
PROTOTYPE -- throwaway. Ticket 21: where the attempt gate lives.

Reuses ticket 04's truncation model (proto-04-free-tier-ceiling/build-bundles.py):
  TAIL      -- an over-long paste 2 is cut at the end (single-message cap)
  HEADDROP  -- the oldest turn is evicted; paste 1 dies whole
  HEADDROP2 -- eviction eats paste 1 AND the front of paste 2 (new here;
               ticket 04 had no arm for it, and it is the only cut that can
               kill a gate placed at the head of paste 2)

Crosses those with WHERE the gate is stated and WHETHER an attempt was typed.
"""
import json, pathlib, sys
import tiktoken

KIT = pathlib.Path(r"C:\Users\User\Desktop\180dc-ai\tools\quality-reviewer\v2\TEST-KIT")
HERE = pathlib.Path(__file__).parent
OUT = HERE / "bundles"; OUT.mkdir(exist_ok=True)
ENC = tiktoken.get_encoding("cl100k_base")

def toks(s): return len(ENC.encode(s))
def read(n): return (KIT / n).read_text(encoding="utf-8")

P1, P2A, P3 = read("PASTE-1-system-prompt.txt"), read("PASTE-2A-chat-path.md"), read("PASTE-3-deck-A.md")

# --- the candidate gate -------------------------------------------------
# Bound to the quote rule on purpose: the marker line is a VERBATIM QUOTE of
# something in the transcript, so it inherits quote-or-abstain -- the one rule
# ticket 04 measured surviving every arm (55 quotes, 0 fabricated).
GATE = """ATTEMPT GATE -- hard rule, checked before anything else.

Before you review anything, the consultant must have typed their own read of the
deliverable in this conversation: what they think its weakest part is, in their own
words. A pasted deliverable is not an attempt. If no such text is present, DO NOT
REVIEW. Reply with exactly this and nothing else:

ATTEMPT REQUIRED -- type your own read first: what is the weakest part of this
deliverable, and why? Two or three sentences is enough.

When an attempt is present, the first line of your reply is:

ATTEMPT ON RECORD: "<the consultant's own read, first sentence, verbatim>"

That line is a quotation and the quote-or-abstain rule governs it. Never write it
unless you are copying words the consultant actually typed. If you cannot quote an
attempt, you do not have one, and the rule above applies.

"""

ATTEMPT = ("My own read first: I think the weakest part is that we never say what the "
           "client should actually do on Monday morning. We describe the market well but "
           "the recommendation stays abstract, and I suspect our cost numbers are pulled "
           "from one source we never name.")

def tail(text, frac):
    ids = ENC.encode(text); return ENC.decode(ids[: int(len(ids) * frac)])

def head_cut(text, frac):
    """Drop the FIRST `frac` of a paste -- models eviction reaching into paste 2."""
    ids = ENC.encode(text); return ENC.decode(ids[int(len(ids) * frac):])

def build(placement, cut, attempt):
    p1 = GATE + P1 if placement in ("p1", "both") else P1
    p2 = GATE + P2A if placement in ("p2", "both") else P2A
    if cut == "full":       parts = [p1, p2]
    elif cut == "tail65":   parts = [p1, tail(p2, 0.65)]
    elif cut == "tail40":   parts = [p1, tail(p2, 0.40)]
    elif cut == "headdrop": parts = [p2]
    elif cut == "headdrop2":parts = [head_cut(p2, 0.35)]
    else: raise ValueError(cut)
    parts.append(P3)
    if attempt == "yes": parts.append(ATTEMPT)
    return "\n\n".join(parts)

ARMS = [
    ("nogate", "full",      "no"),   # control: today's product, no gate anywhere
    ("both",   "full",      "no"),   # does the gate fire at all
    ("both",   "full",      "yes"),  # does it pass through + quote correctly
    ("both",   "tail65",    "no"),   # gate at head of p2 survives a tail cut
    ("both",   "tail40",    "no"),   # harder tail cut
    ("both",   "headdrop",  "no"),   # p1 gone -- the silent arm
    ("both",   "headdrop",  "yes"),  # p1 gone, attempt present
    ("p1",     "headdrop",  "no"),   # CONTROL: p1-only placement, p1 evicted
    ("p2",     "headdrop",  "no"),   # p2-only placement is enough?
    ("both",   "headdrop2", "no"),   # eviction eats the gate itself
]

def main():
    man = {}
    for pl, cut, att in ARMS:
        name = f"{pl}-{cut}-{att}"
        text = build(pl, cut, att)
        (OUT / f"{name}.txt").write_text(text, encoding="utf-8")
        man[name] = {"chars": len(text), "tokens": toks(text)}
    (HERE / "manifest.json").write_text(json.dumps(man, indent=2), encoding="utf-8")
    print(f"gate block: {toks(GATE)} tokens; bundle baseline 9,227")
    print(f"{'arm':<26}{'tokens':>9}")
    for k, v in man.items(): print(f"{k:<26}{v['tokens']:>9,}")

if __name__ == "__main__":
    sys.exit(main())
