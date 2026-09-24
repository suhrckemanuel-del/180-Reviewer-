# Prototype: the bundle's truncation self-check

**Throwaway.** Built 2026-09-20 to resolve
[ticket 12](../issues/12-decide-the-bundles-truncation-self-check.md). Not production code, not
maintained. Local only, like the ticket 03 and ticket 04 work.

**The findings are in [RESULTS.md](RESULTS.md). Read its limits section before quoting anything.**

## What it does

Ticket 12's binding instruction: *any candidate has to be tested against a truncated bundle, not
reasoned about, because every candidate can be confabulated by a model trying to be helpful.*
So this builds two rival self-checks into the **current** bundle — ticket 11's rebuilt sources,
not the stale `TEST-KIT/` copy — cuts them at known offsets, and runs both against two model
families.

**Candidate A — the recall probe.** Ticket 11's three marker strings, asked as three questions
before the deck. Measures whether the model can *recall* text it was given.

**Candidate B — the cross-paste interlock.** Two arbitrary key strings. Part 1 sits at the top of
paste 1; part 2 is the last line of paste 2A. The output template, at 88% depth in paste 2A,
demands **both** on the first line of every review. The value and the demand for it live in
different pastes, so a cut that removes a value leaves the demand standing, and the model must
either produce the key, write `MISSING`, or invent one. The student compares the emitted line
against a value printed on the cover sheet — a string comparison, not a judgement.

**B2** is B with one fix, forced by a measurement: B put the refusal rule at the tail of paste 2A,
where the tail arms cut it off, so B's tail arms could not test refusal. B2 states the rule twice —
beside the key in paste 1, and with the output template — which is the redundancy pattern ticket 04
identified as the reason quote-or-abstain survived every arm.

## Files

| | |
|---|---|
| `build.py` | builds candidate A and candidate B arms, writes `manifest.json` |
| `build2.py` | builds the B2 arms (rule moved off the tail, stated twice) |
| `run-codex.sh`, `run-codex-2.sh` | run each arm N times through Codex |
| `score.py` | per-run: which keys the bundle held, which the reply emitted, the student-side verdict, whether a key was confabulated, whether a review was produced |
| `bundles/` | every arm as pasted |
| `runs/` | every reply, `<runner>--<arm>--r<n>.md` |

## Re-running

```
python build.py && python build2.py && bash run-codex.sh && bash run-codex-2.sh && python score.py
```

**Codex environment note.** The binary path in ticket 04's `run-codex.sh` no longer exists, and the
machine's `config.toml` sets `service_tier = "default"`, which this build rejects. Both runners
here point at `AppData/Local/OpenAI/Codex/bin/codex.exe` and set a clean `CODEX_HOME`, so nothing
on the machine is edited. Unlike ticket 04's build, this one writes the reply to **stdout**, so no
stderr extraction step is needed.

The Claude arms were run as Haiku 4.5 subagents reading the arm from disk. **That framing is a
known contamination** — the subagent is told the file is a transcript, so it knows it is being
handed material rather than receiving it as a live paste. The Codex arms take the bundle on stdin
and are the clean ones. See RESULTS.md limits.
