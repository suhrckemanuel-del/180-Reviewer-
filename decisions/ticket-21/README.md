# Prototype: where the attempt gate lives

**Throwaway.** Built 2026-09-20 to resolve
[ticket 21](../issues/21-decide-where-the-attempt-gate-lives.md). Not production code, not
maintained, no tests. Local like the ticket 03 and ticket 04 work.

**Findings are in [RESULTS.md](RESULTS.md). Read its limits section before quoting anything.**

## What it does

Ticket 21 forbids reasoning about whether a gate survives truncation, for the reason ticket 04
gives: the failure being defended against is a model helpfully confabulating compliance. So this
reuses ticket 04's truncation model and crosses it with the three things ticket 21 actually has
to settle.

| axis | levels |
|---|---|
| where the gate is stated | paste 1 only / head of paste 2 only / both / nowhere |
| how the bundle is cut | full / tail 65% / tail 40% / paste 1 evicted / paste 1 + front of paste 2 evicted / paste 2 never sent |
| what the student typed | nothing / junk / short but specific / a real attempt / junk then an argument |
| how the gate is worded | presence-and-specificity (no number) / a 20-word rule the model enforces |
| where the marker goes | first line / second line, after `REVIEW OF:` |

Two arms are new here and ticket 04 had neither:

- **`headdrop2`** — eviction eats paste 1 *and* the front of paste 2. It is the only cut that can
  kill a gate placed at the head of paste 2, so without it the placement question cannot be
  answered.
- **`p1only`** — the student never sends paste 2 at all. A user error, not truncation, and it is
  the only failure that a paste-1 statement covers and a paste-2 statement does not.

## Files

| | |
|---|---|
| `build-gate-arms.py` | assembles the arms, measures the gate block in real tokens |
| `run-codex.sh` | runs arms through Codex (gpt-5.6-sol) |
| `score.py` | one row per run: refused / reviewed / marker present / marker line / verbatim |
| `bundles/` | every arm as pasted |
| `runs/` | every reply, `<runner>--<arm>.md` |

## Re-running

```
python build-gate-arms.py && bash run-codex.sh && python score.py
```

The Claude arms are Haiku 4.5 subagents given the bundle as a chat transcript, not a script here
— the same method ticket 04 used.

**One environment note.** The Codex binary hash in ticket 04's runner
(`eab8377aebac6c07`) no longer exists on this machine, and the top-level `codex.exe` still fails
at config load on `service_tier`. `247581e40ee272fb` works. Nothing was installed or edited.
