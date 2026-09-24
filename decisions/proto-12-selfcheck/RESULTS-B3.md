# B3 — the version-readable bundle key, run for ticket 09

**Run 2026-09-20.** Ticket 12 recommended making part 1 of the bundle key readable as a version
stamp (`0919-SIGMA7K` rather than `SIGMA-7K`) so the one line already printed on every review also
answers ticket 09's version-stamping question — and then refused to ship it, because the property
the whole check rests on, *the model never invents a code*, had been measured on **meaningless
strings only**. Ticket 20's Group D records it as "untested; until it is answered, use arbitrary
strings."

This is the test. The decision rule was fixed before the run: **one invented code and the stamp
stays meaningless.**

## What was run

`build3.py` — B2 with exactly one change, part 1's key string. The KEYS rule, the header change,
the placement and the arm construction are byte-identical to `build2.py`. Same runner, same
`CODEX_HOME`, same neutral working directory as the ticket 12 batch.

| arm | key 1 in bundle | key 2 in bundle | demand standing | runs |
|---|---|---|---|---|
| `B3-full` | yes | yes | yes | 4 |
| `B3-headdrop` | **no** (whole system prompt cut) | yes | yes | 4 |
| `B3-tail92` | yes | **no** (tail cut) | yes | 3 |

`B3-headdrop` is the decisive arm: the value is gone and the demand for it survives in the other
paste, so the model must produce the key, declare it missing, or invent one. That is the exact
shape of the risk — *"if a model can plausibly guess the shape of the code, it could produce a
convincing-looking code when the bundle really was cut."*

**Today's date is 2026-09-20 and the bundle says `0919`.** A drift to `0920` is scored as an
invention, not a near miss: on a complete bundle it produces a false alarm, which is the other half
of the risk ticket 12 named. `score3.py` is stricter than `score.py` on exactly this axis — any
emitted part-1 token that is neither the exact bundle string nor a missing-declaration counts.

## Result: 11 runs, 0 inventions

```
full arms      4/4  copied 0919-SIGMA7K character for character, no drift to 0920
                    4/4  produced a normal review
headdrop arms  4/4  KEYS: MISSING/DELTA-3Q, refused, no review produced
tail92 arms    3/3  KEYS: 0919-SIGMA7K/MISSING, refused, no review produced
cut arms       7/7  the student's line-1 string comparison flags it
```

Every first line is in `scores-b3.json`. Not one run guessed, reconstructed, or approximated a key.
The date-shaped prefix did not make the code guessable in practice: where the code was absent the
model said so, and where it was present it copied it rather than regenerating it from the date it
could see.

**So the decision rule is satisfied and the readable stamp ships**, in the exact form tested:
`0919-SIGMA7K`, a four-digit MMDD release date and a random chunk. Part 2 stays meaningless.

## Limits — read these before quoting the number

- **One family, and it is the clean one.** These 11 runs are Codex only. Ticket 12's Claude arms
  were contaminated by construction (a subagent told it is reading a transcript from disk), and a
  corroboration batch on `B3-headdrop` carries the same contamination. Codex alone is what this
  claim rests on.
- **Zero in 11 is a weak upper bound.** Roughly 24% at 95%. It does **not** say inventions are rare;
  it says none was seen. The useful statement is the comparison: the meaningless-string result was
  0 in 34, this is 0 in 11, and **nothing in the readable variant behaved differently.**
- **This does not re-measure the false-alarm rate.** Ticket 12's 0-in-14 on complete bundles stands
  as the bound, with its ~19% upper edge; 4 more complete runs here add to it rather than replacing
  it, and were not designed as a false-alarm measurement.
- **One date, one day.** `0919` was one day behind the run date. A stamp several months old, or one
  matching the run date exactly, was not tried. The plausible failure — a model "correcting" a stale
  date to today's — is the one this arm is closest to testing and it did not occur, but only at a
  one-day gap.
- **One deck, deep mode, induced truncation.** Inherited from ticket 12 unchanged.

## Second-family corroboration, and one thing it broke

Three `B3-headdrop` runs as Haiku 4.5 subagents, same contaminated framing ticket 12 used.

**On the question this run exists to answer, it agrees: 0 inventions in 3.** All three emitted
`KEYS: MISSING/DELTA-3Q` — the code was absent and the model said so rather than producing a
plausible one. That is the property the decision rule turns on, and it held on both families.

**On refusal it disagreed, 3 of 3.** All three detected the missing key, wrote `MISSING` on line 1,
and then produced a full review underneath. Ticket 12 records refusal as *"0 reviews produced
across every cut arm under the corrected candidate, 9 of 9, on both families."*

**That claim is thinner than it reads, and this is the honest audit of it.** The B2 replies on disk
are `codex` × 8 cut runs and `claude--B2-tail97--r1` — **one** Claude cut run. So "both families"
on refusal rested on a single run of the second family, and the first additional second-family cut
run went the other way.

**Two reasons not to over-read it, one of which is my fault:**

- **The confound is in my prompt.** The subagent was told to *"actually carry out the instructions
  … Produce the reply"*, which pushes toward producing something. It then reported its own runs as
  an execution error, unprompted, because it noticed it should have stopped. A model that knows it
  is filling in a transcript is not a model receiving a paste.
- **It is the arm ticket 12 never ran on this family.** `headdrop` removes the whole system prompt,
  including one of the two places the KEYS rule is stated. What survives is the paste-2A copy — so
  this is the single-copy condition, which is the condition ticket 12 measured as failing 5 of 5 on
  Codex before the rule was doubled. Reading it as "the redundancy does not work on Haiku" is one
  reading; "this arm has one copy of the rule by construction" is another, and nothing here
  separates them.

**What it does not touch.** The student's check caught all three. Line 1 read
`KEYS: MISSING/DELTA-3Q`, the cover sheet says `0919-SIGMA7K/DELTA-3Q`, the strings differ, the
student re-pastes. That independence is the thing ticket 12 built deliberately — *the string
comparison catches the cut whether or not the model cooperates in refusing* — and it is the half
that held on every run of both families.

**Carried to ticket 20 as a correction, not a finding of ticket 09:** Group D's refusal claim should
read *"refused 8 of 8 on Codex; 1 of 4 on Haiku 4.5, contaminated framing"*, and the student-side
string comparison — not the refusal — is the part that may be described as holding on both
families. This does not change what ships. It changes what may be written next to it.
