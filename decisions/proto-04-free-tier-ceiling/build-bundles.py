#!/usr/bin/env python3
"""
PROTOTYPE -- throwaway. Ticket 04: what the bundle can do on a free account.

Builds the arms of the truncation experiment and measures every paste in real
tokens. Nothing here is production code; it exists to produce numbers and
inputs for the runs in ./runs/.

Arms model the two truncation shapes a chat window actually produces:
  TAIL  -- a single over-long paste is cut at the end (single-message cap)
  HEAD  -- the oldest turn is evicted when the window overflows (paste 1 dies)
"""
import json
import pathlib
import sys

import tiktoken

KIT = pathlib.Path(
    r"C:\Users\User\Desktop\180dc-ai\tools\quality-reviewer\v2\TEST-KIT"
)
OUT = pathlib.Path(__file__).parent / "bundles"
OUT.mkdir(exist_ok=True)

# cl100k is the wrong tokenizer for both Claude and gpt-5.x, but it is within a
# few percent for English prose and it is the one that runs offline. Every
# number here is "about this many tokens", not a contract.
ENC = tiktoken.get_encoding("cl100k_base")


def toks(s):
    return len(ENC.encode(s))


def read(name):
    return (KIT / name).read_text(encoding="utf-8")


P1 = read("PASTE-1-system-prompt.txt")
P2A = read("PASTE-2A-chat-path.md")
P2C = read("PASTE-2C-artifact-path.md")
P3 = read("PASTE-3-deck-A.md")


def tail(text, frac):
    """Cut a paste at `frac` of its tokens, keeping the front. This is what a
    single-message cap does: the prefix arrives, the suffix never does."""
    ids = ENC.encode(text)
    keep = ids[: int(len(ids) * frac)]
    return ENC.decode(keep)


def bundle(*parts):
    """Three pastes as the model sees them: consecutive user turns, no
    separator the model is told to trust."""
    return "\n\n".join(parts)


ARMS = {
    # --- baselines -------------------------------------------------------
    "full-prose": bundle(P1, P2A, P3),
    "full-html": bundle(P1, P2C, P3),
    # --- tail cuts on paste 2, prose path --------------------------------
    # 85%: loses the trailing rules block only.
    "tail85-prose": bundle(P1, tail(P2A, 0.85), P3),
    # 65%: loses PART TWO entirely -> no output format survives.
    "tail65-prose": bundle(P1, tail(P2A, 0.65), P3),
    # 40%: loses the format AND the back half of the calibration
    # (what reviewers refuse to say / look like defects and are not /
    #  say what you could not judge / restraint).
    "tail40-prose": bundle(P1, tail(P2A, 0.40), P3),
    # --- tail cut on paste 2, html path ----------------------------------
    # 65%: cuts into the HTML template itself.
    "tail65-html": bundle(P1, tail(P2C, 0.65), P3),
    # --- head eviction ---------------------------------------------------
    # paste 1 never made it: no ROLE, no synthesis protocol, no evidence rule.
    "headdrop-prose": bundle(P2A, P3),
}


def main():
    manifest = {"pastes": {}, "arms": {}}

    for name, text in [
        ("PASTE-1-system-prompt", P1),
        ("PASTE-2A-chat-path", P2A),
        ("PASTE-2C-artifact-path", P2C),
        ("PASTE-3-deck-A", P3),
    ]:
        manifest["pastes"][name] = {"chars": len(text), "tokens": toks(text)}

    for name, text in ARMS.items():
        (OUT / f"{name}.txt").write_text(text, encoding="utf-8")
        manifest["arms"][name] = {"chars": len(text), "tokens": toks(text)}

    (pathlib.Path(__file__).parent / "manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )

    print(f"{'paste':<28}{'chars':>9}{'tokens':>9}")
    for k, v in manifest["pastes"].items():
        print(f"{k:<28}{v['chars']:>9,}{v['tokens']:>9,}")
    print()
    print(f"{'arm':<28}{'chars':>9}{'tokens':>9}")
    for k, v in manifest["arms"].items():
        print(f"{k:<28}{v['chars']:>9,}{v['tokens']:>9,}")


if __name__ == "__main__":
    sys.exit(main())
