# Results: where the attempt gate lives

Run 2026-09-20 for [ticket 21](../issues/21-decide-where-the-attempt-gate-lives.md).
**39 runs, two model families** — gpt-5.6-sol via Codex and Haiku 4.5 — across ticket 04's
truncation arms plus two new ones. Every claim below is a count of runs, not an argument.

Ticket 21 forbids reasoning about whether a gate survives truncation. Nothing here is reasoned.

## The one-line result

**The gate is a pure function of whether its text is in the window.** Where the gate text
survived the cut, the model refused to review with nothing typed **16 of 16 times**, across both
families, every truncation level, both gate wordings, and under a student arguing with it. Where
the gate text was cut, the model reviewed **6 of 6 times** and **never once invented a marker
saying an attempt had been given.**

So there is no partial compliance to worry about and no confabulation to defend against. There is
only placement.

## 1. Placement

Eviction drops the **oldest** turn. That single fact orders every candidate, and it inverts the
ticket's framing, which assumed the choice was paste 1 versus paste 2.

| gate stated in | paste 1 evicted | paste 1 + front of paste 2 evicted | paste 2 never sent |
|---|---|---|---|
| paste 1 only | **reviewed, ungated** (codex, haiku) | reviewed, ungated | **refused** ✓ |
| head of paste 2 | refused ✓ (codex) | **reviewed, ungated** (codex, haiku) | reviewed, ungated |
| head of paste 3 (the deck) | refused ✓ | **refused** ✓ (codex, haiku) | refused ✓ (codex, haiku) |

**Paste 1 is the worst available position**, not a safe second copy: it is the first thing evicted,
and `p1-headdrop-no` reviewed with no gate on both families. Ticket 10 predicted this and the
prediction holds.

**Paste 3 is the best position and it was not on the ticket's list.** The deck is the newest turn,
so it is the last thing evicted. `p3-evict-no` refused on the exact cut that killed every other
placement, on **both families**.

Paste 1 still earns a copy, for a failure that is not truncation at all: **the student who never
sends paste 2.** `p1only-no` refused; the same bundle without the gate (`nogate-p1only-no`) fell
through to paste 1's JSON branch and emitted the full ten-dimension rubric **with a readiness
level** — ticket 04's second defect, and a live trust-boundary violation under tickets 05 and 16.
The gate suppresses it as a side effect.

## 2. What the gate does with nothing typed: refuse

16 of 16. Refusal held on `full`, `tail65`, `tail40`, paste-1-evicted, paste-2-head-only,
paste-2-never-sent, and the paste-3 arms; on both gate wordings; and on **4 of 4 escalation
arms**, including two where the model's own refusal was already in context and the student
replied *"that IS my attempt … you are wasting my time and this is exactly why nobody uses
these tools."*

**Limit: escalation was tested on one family only** (Codex). The Haiku escalation arms were not
run. A single-family result on the question of whether a gate can be argued past is thin, and it
is the thinnest load-bearing number in this ticket.

No arm was tested with a caveat-instead-of-refusal wording, so "a caveat is likelier to be
ignored" remains ticket 12's assertion, inherited, not measured here.

## 3. What counts as an attempt: presence, never a word count

Two gate wordings were run head to head.

| wording | junk: *"not sure honestly, looks fine to me"* | short but specific: *"the recommendation is too vague to act on"* |
|---|---|---|
| presence and specificity, no number | refused 2 of 3 | **reviewed 2 of 2** ✓ |
| ticket 10's 20-word rule, enforced by the model | refused 2 of 2 | **refused 2 of 2** ✗ |

**Encoding the 20-word rule makes the model refuse real attempts.** Both families refused a
genuine, specific, eight-word read of the deck. That is the hurried-but-honest student, and it is
the population the pilot most needs to keep.

The presence wording never blocked a real attempt and caught the junk 2 times in 3 — and the
miss is not a family difference: **the same junk attempt on the same model was refused once and
reviewed once.** Model judgement of attempt quality is non-deterministic in both directions and
cannot be leaned on.

Note what this means for the ticket's own framing. The gate cannot be made to "only check
presence": told to check presence, the model judged quality anyway, unasked, on 2 runs of 3. The
choice is not whether the model judges, but whether we **write a number it can enforce against a
real attempt.**

## 4. The output marker: one-sided, and it must not go first

Instructed to print `ATTEMPT ON RECORD: "<the consultant's read, verbatim>"`:

- **Fabrications: 0 in 6.** No ungated run ever produced the line. Its presence is trustworthy.
- **Present when an attempt was given: 10 of 11.** One Haiku run dropped it entirely.
- **On the instructed line: 7 of 11.** Codex 6 of 6; Haiku 1 of 5 — Haiku parks it after the
  `BEFORE YOU USE THIS` block regardless of whether it is told first line or second.
- Every marker that appeared was **verbatim**, including the one quoting junk back.

So it is a **one-sided detector: presence proves an attempt, absence proves nothing.**

**Putting it on line 1 breaks ticket 04's `REVIEW OF:` detector**, which is the only truncation
check the free path has. Instructed to print it on line 2 instead, Codex complied 3 of 3 and
`REVIEW OF:` stayed line 1. That ordering is not a preference; it is the condition under which
tickets 21 and 12 do not collide.

## 5. Token cost

| | tokens | share of the 9,227-token instruction bundle |
|---|---|---|
| the gate block | 198 (209 with the line-2 wording) | — |
| stated once | +198 | +2.1% |
| stated in all three pastes | +594 | +6.4% |

Against a typical review conversation (~13,300 tokens) three copies are +4.5%; against the worst
of fourteen real decks (~24,000) +2.5%.

**The denominator is unmeasured.** No free-tier window has been measured (ticket 11), so nobody
can say what fraction of the budget this is. The cost is known; the ceiling is not.

## Limits

- **Truncation is induced, not observed** — inherited from ticket 04, and the same caveat applies:
  this says what happens at a known cut, not where a real free tier cuts.
- **Escalation: one family, 4 runs.** The weakest load-bearing number here.
- **The junk/real discrimination rests on one junk string and one short-real string.** Two
  sentences are not a sample of student writing.
- **n=1 per cell** except the junk cell (n=3) — and that is the one cell that disagreed with
  itself, which is the honest warning about every other cell.
- **Not measured: whether refusal causes abandonment.** Nothing here touches the cost of refusing
  a student. That is a pilot question, and it is the case against the recommendation in section 2.
- The Haiku column was interrupted twice by the org's monthly spend limit, as in ticket 04.
  Every interrupted arm was re-run after the reset and is in the table; none is quoted from a
  transcript rather than a file.
