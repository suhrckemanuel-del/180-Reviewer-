#!/usr/bin/env python3
"""
PROTOTYPE -- throwaway. Ticket 04.

codex-cli 0.155 streams the prompt echo, the reasoning and the final message to
stderr and leaves stdout empty when stdin is piped. The reply sits between the
last bare `codex` line and the `tokens used` footer. Pull it out into the .md
the scorer reads.
"""
import pathlib
import re

RUNS = pathlib.Path(__file__).parent / "runs"


def extract(text):
    lines = text.replace("\r", "").split("\n")
    starts = [i for i, l in enumerate(lines) if l.strip() == "codex"]
    if not starts:
        return None, None
    body = lines[starts[-1] + 1:]
    ends = [i for i, l in enumerate(body) if l.strip() == "tokens used"]
    used = None
    if ends:
        tail = body[ends[0] + 1:]
        used = next((t.strip() for t in tail if t.strip()), None)
        body = body[: ends[0]]
    return "\n".join(body).strip(), used


def main():
    for err in sorted(RUNS.glob("codex--*.stderr.txt")):
        arm = err.name.replace("codex--", "").replace(".stderr.txt", "")
        out = RUNS / f"codex--{arm}.md"
        reply, used = extract(err.read_text(encoding="utf-8", errors="replace"))
        if not reply:
            print(f"{arm:<20} no reply found ({err.stat().st_size:,} bytes stderr)")
            continue
        out.write_text(reply, encoding="utf-8")
        print(f"{arm:<20} {len(reply):>7,} bytes   tokens used: {used}")


if __name__ == "__main__":
    main()
