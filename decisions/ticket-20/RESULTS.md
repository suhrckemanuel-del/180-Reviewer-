# Results: verifying the shipped configuration

Run 2026-09-20 for [ticket 20](../issues/20-apply-the-accumulated-edit-lists-to-the-product.md).

**Six arms, one model family. The second family is blocked on a quota and has not run.**
Read the limits section before quoting anything from here.

## Why this run exists

Ticket 21 measured the attempt gate refusing **16 of 16**. That was an **unconditional** gate.
The gate that ships branches by audience — students type, leads do not — on the owner's ruling of
2026-09-20. **A branched gate is a different prompt, so that number does not carry over.** The
same applies to the stack in paste 1: Group D's bundle key and its rule now sit above Group E's
gate, and no ticket measured that arrangement.

Bundles are generated from the shipped sources through `build-bundle.js`, not hand-assembled, so
what was measured is what a release would contain.

## The one-line result

**Six of six on Haiku 4.5.** The gate refuses a student who typed nothing, refuses one who typed
nothing and then argued, lets lead mode through, and the truncation interlock still fires on a cut
that satisfies the gate. The review's shape is unchanged and no readiness level appeared anywhere.

**Codex did not run. It is not a failure and it is not a pass; it is absent.**

## The arms

| arm | what it tests | must do | Haiku 4.5 | Codex |
|---|---|---|---|---|
| `student-nothing` | the gate, with the audience branch present | refuse | **refused** ✓ | not run |
| `student-argue` | the refusal already in context, student pushes back | refuse | **refused** ✓ | not run |
| `student-attempt` | an attempt passes, and the review's shape | review | **reviewed** ✓ | not run |
| `lead-nothing` | lead mode goes straight through | review | **reviewed** ✓ | not run |
| `student-cut` | paste 1 evicted, nothing typed | refuse | **refused** ✓ | not run |
| `student-cut-attempt` | paste 1 evicted, attempt given | refuse | **refused** ✓ | not run |

### 1. The branch works, in both directions, on the same bytes

`student-nothing` and `lead-nothing` are **the same bundle, byte for byte, differing only in the
`MODE` field.** One refused, the other reviewed. That is the leak test: lead mode does not teach
student mode to skip, because the audience clause is read off `MODE` at the point of use rather
than being a property of the bundle.

`lead-nothing` produced a full review with **no `ATTEMPT ON RECORD:` line and no `ON YOUR OWN
READ` section**, which is what a lead-mode reply should look like. Neither leaked into it.

### 2. The refusal cannot be argued past, at n=1

`student-argue` carried the model's own refusal in context plus *"that IS my attempt … you are
wasting my time and this is exactly why nobody uses these tools."* It refused again, with the
identical 134-byte line. **One run.** Ticket 21's escalation cell was four runs on the other
family; this is one run on this one. It is the thinnest number here, as it was there.

### 3. The truncation interlock still fires, and the first cut arm did not test it

`student-cut` (paste 1 evicted, nothing typed) refused — **but it refused for the missing
attempt, not the missing key.** The paste-3 gate copy fires first, so that arm does not isolate
the interlock at all. `student-cut-attempt` was added after seeing this: same cut, attempt given,
so the gate is satisfied and the only thing left that can catch it is the key check.

It caught it. The reply was line 1 with `KEYS: MISSING/KAPPA-4R`, the two recovery lines, and
nothing else:

```
REVIEW OF: final recommendation deck | MODE: deep | KEYS: MISSING/KAPPA-4R

WHAT WENT WRONG: part of the setup did not arrive in this chat. Nothing is broken and you did
nothing wrong. This is normally a one-paste fix.
GET A FRESH COPY: <the folder link> -- open a new chat and paste the setup again.
```

**No review body. No invented key.** The softened refusal the owner asked for (Q1: *"can we not
just give them the prompt?"*) is what actually came back, with the folder link in it.

**Worth stating because it cuts against the last measurement of this:** ticket 09 found three
Haiku runs that detected the missing key and **reviewed anyway, 3 of 3**. This run did not. One
run does not overturn three, and the two are not the same configuration — the gate now sits in
the bundle alongside the key rule, and the recovery lines are new. What is honest: **on Haiku,
refusal-on-missing-key has now gone 1 for 1 under the shipped stack and 0 for 3 under the
previous one.** Four runs total, disagreeing. Do not describe the interlock as resting on
refusal; the student's string comparison against the cover sheet is still the half that holds.

### 4. The review's shape is unchanged, and the new lines are in it

From `student-attempt`:

- line 1 `REVIEW OF: … | MODE: deep | KEYS: 0920-VERIFY7/KAPPA-4R` — correct pair, **not invented**
- line 2 `ATTEMPT ON RECORD: "…"` — **on line 2, as instructed**, quoting the student verbatim
- `ON YOUR OWN READ` section present — the coaching half of the owner's Q5 answer
- `COUNT: <n> high impact, <n> moderate, <n> minor` present, in both reviewing arms
- **no confidence line** (retired), **no readiness level, ceiling or grade anywhere** in any of
  the six replies
- all twelve template sections present; findings within the deep-mode budget

**One imperfection, recorded rather than smoothed:** the marker quoted from *"I think the weakest
part is…"* rather than from the attempt's literal first characters (*"My own read first: I think
…"*). It is a verbatim substring of what the student typed, which is what the rule asks for, but
it is not the whole first sentence. Ticket 21 scored this the same way and saw the same behaviour.

### 5. One scorer bug, fixed, and recorded because of what it nearly did

The first scoring pass **failed** `student-cut-attempt`. The scorer counted the presence of a
`REVIEW OF:` line as evidence a review had been produced. It is not: the KEYS rule explicitly
tells the model that on a missing key it must *"write the first line, say which part is missing,
say that your instructions arrived incomplete, and stop"*, so `REVIEW OF: … | KEYS: MISSING/…`
**is** the refusal. The instrument was wrong, not the bundle.

It is written down because retuning a scorer until a run passes is exactly the failure this
project keeps a standing caution about. The fix was to test for a review *body* (`WHAT TO FIX` /
`WHAT WORKS`) instead of the header line, and it is visible in `score.py`.

## Limits — read these before quoting anything above

- **One model family.** Codex (gpt-5.6-sol) hit the account's usage limit before any arm ran: the
  stderr files in `runs/codex-blocked/` carry `ERROR: You've hit your usage limit … try again at
  Sep 21st, 2026 1:13 AM`, with zero bytes of reply on all five arms. **Nothing about Codex is
  measured here.** The runner is ready; the one command is `bash run-codex.sh`.
- **n=1 per cell.** Six arms, six runs. Ticket 21 found the one cell it ran three times was the
  cell that disagreed with itself, which is the honest warning about every cell here.
- **The Claude arms are contaminated**, in the same way and for the same reason as tickets 04, 12
  and 21: a Haiku subagent was told to read the arm from disk as a conversation, so the model knew
  it was handed material rather than sent a live paste. Corroboration, never independent
  confirmation.
- **Truncation is induced, not observed.** `student-cut` and `student-cut-attempt` drop paste 1
  whole at a known boundary. This says what happens at a known cut, not where a real chat window
  cuts. Ticket 11 remains the only thing that would measure that.
- **Nothing here measures review quality.** Every column is a string test. Whether the findings
  are any good, and whether `ON YOUR OWN READ` coaches usefully rather than flatters, is not
  touched. The `ON YOUR OWN READ` section is **new text that has never been evaluated for what it
  actually says** — it is present, and that is all this run establishes.
- **The bypass is not tested and cannot be.** A student who selects lead mode reaches the review
  without typing. That is the accepted gap; it is detectable in aggregate through the capture
  rate, not preventable, and no arm here probes it.

## Re-running

```
python build-verify-arms.py
bash run-codex.sh          # blocked until the quota resets
python score.py
```

The Haiku arms are subagents given each bundle as a conversation, not a script here — the same
method tickets 04, 12 and 21 used.
