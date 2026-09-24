#!/usr/bin/env python3
"""PROTOTYPE -- throwaway. Ticket 12.
Codex sometimes writes the reply to stderr instead of stdout (ticket 04 hit the
same thing). For any empty run file, recover the reply from the .err.txt: it
sits between a bare `codex` line and the `tokens used` footer."""
import pathlib, re
for md in sorted(pathlib.Path("runs").glob("codex--*.md")):
    if md.stat().st_size: continue
    err = md.with_suffix(".err.txt")
    if not err.exists(): continue
    t = err.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"\ncodex\n(.*?)\ntokens used\n", t, re.S)
    if not m:
        print(f"{md.name}: no reply found in stderr"); continue
    md.write_text(m.group(1).strip() + "\n", encoding="utf-8")
    print(f"{md.name}: recovered {len(m.group(1))} chars from stderr")
