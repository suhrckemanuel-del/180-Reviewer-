# Prototype: what the bundle does on a free account and in Codex

**Throwaway.** Built 2026-09-19 to resolve
[ticket 04](../issues/04-establish-what-the-bundle-can-do-on-a-free-account.md). Not production
code, not maintained, no tests. Kept local like the ticket 03 analysis — `.scratch/` is untracked
by convention in this repo.

**The findings are in [RESULTS.md](RESULTS.md). Read its limits section before quoting anything.**

## What it does

Assembles the three-paste bundle from `tools/quality-reviewer/v2/TEST-KIT/`, cuts it at known
token offsets to simulate the two ways a chat window loses a paste, runs every arm through two
model families, and checks each reply against the deck.

Truncation is **induced, not observed**. That is the point: cutting at a known offset turns "is a
half-loaded bundle detectable" into a controlled experiment instead of a wait for a free tier to
cut somewhere unknown. What it does *not* do is tell you where a real free tier cuts — see ticket
11.

## Files

| | |
|---|---|
| `build-bundles.py` | assembles the seven arms, measures every paste in real tokens, writes `manifest.json` |
| `run-codex.sh` | runs every arm through Codex |
| `extract-codex.py` | pulls the reply out of Codex's stderr stream |
| `score.py` | branch / sections / quotes / readiness-leak per run → `scores.json` |
| `check-quotes.py` | the strict quote-or-abstain check on its own |
| `quote-audit.txt` | the definitive quote table: 55 quotes, 54 deck, 1 brief, 0 fabricated |
| `bundles/` | the seven arms as pasted |
| `runs/` | every reply, `<runner>--<arm>.md` |
| `render/` | the two HTML replies as `.html`, to open in a browser |

## Re-running

```
python build-bundles.py && bash run-codex.sh && python extract-codex.py && python score.py
```

Two environment notes, both discovered the hard way:

- **Codex.** The npm-installed CLI on this machine (0.121.0) is too old for the account's model
  and fails at config load. `run-codex.sh` uses the binary the Codex desktop app ships
  (`AppData/Local/OpenAI/Codex/bin/eab8377aebac6c07/codex.exe`, 0.155) instead. Nothing was
  installed and no config was edited; the only override is `service_tier`, which the existing
  `config.toml` sets to a value that build rejects.
- **Codex writes the reply to stderr** when stdin is piped, between a bare `codex` line and a
  `tokens used` footer. Hence `extract-codex.py`.

The Claude arms were run as Haiku 4.5 subagents, not by a script here. Four of the seven were lost
to the org's monthly spend limit mid-run, which is why the Claude column in RESULTS.md is
incomplete.

## Scorer caveat

`score.py` has a loose fallback for replies that lost the template entirely: it treats any long
quoted run as a candidate quote, which catches ordinary prose in quotation marks and inflates the
`FABRICATED` column on the JSON arms. **Those numbers are scorer noise, not fabricated quotes.**
`check-quotes.py` and `quote-audit.txt` are the honest count — they look only at fields the reply
actually offers as evidence, and report "none found" rather than guessing.
