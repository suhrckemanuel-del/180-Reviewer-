# Decide what goes in the methodology context bundle

Type: grilling
Status: parked
Blocked by: 04

## Question

The tool is a prompt plus "our resources on our methodology" plus the deliverable. Today that middle
piece is `CHAT-CONTEXT.md` — calibration knowledge distilled from the human gold worksheets, plus
the output format. The question is whether it stays that, or becomes a wider methodology pack.

Blocked by ticket 04, because the answer is bounded by what a free-tier window can actually carry.

Candidates for inclusion, roughly in order of how much they would change the output:

- the calibration distillate (today's `CHAT-CONTEXT.md`)
- the 10-dimension rubric from `01-rubric-v1.md`
- the five criteria and the ERIP model from research angle 01
- the recurring student failure modes from research angle 02
- the horizontal flow test and MBB reviewer discipline from research angle 04
- worked examples of good and bad findings

Settle:

1. What earns its place, measured by whether it changes the review rather than whether it is true.
2. What the bundle costs in context, against the ceiling found in ticket 04.
3. Whether one bundle serves both students and leads, or they diverge.
4. **The line from Hansen, Nohria and Tierney (HBR 1999)**: the bundle is calibration for the
   evaluator, not a library of answers. If it starts carrying past deliverables a student could
   pattern-match against, it has become a codification strategy this org cannot staff — Ernst &
   Young ran 250 people to make that work. Keep it judgment, not exemplars.

Answer records: the bundle's contents, its size, and the rule for what may be added later.

---

**Input from [ticket 04](04-establish-what-the-bundle-can-do-on-a-free-account.md) (closed 2026-09-19).**

**Question 2 has half an answer.** The cost is measured: paste 1 is **4,065 tokens**, paste 2A is
**5,162**, so **9,227 tokens of instructions ride along before any deck**. Real decks run 2,066 to
14,711 tokens (median 4,052), making a typical whole review **~13,300** and the worst **~24,000**.
The *ceiling* those numbers should be measured against was **not** established — no free account
was driven. Ticket 11 closes that. This ticket was deliberately left unblocked rather than made to
wait: answer in the form of a **token budget with headroom**, not a fixed list, and ticket 11 later
tells you whether the budget was right.

**A defect that changes what "required contents" means.** Two things paste 1 explicitly defers to
are in neither paste:

- **The mode table / noise budget.** Paste 1 step 7 says "Cut to the noise budget for the mode
  (below)" — there is no below, and the word "deep" never appears in paste 1. Paste 2A defers the
  other way, to "the noise budget in the prompt".
- **The scope matrix.** Paste 1's rubric block says "see the scope matrix you were given".

Both are built by `run-reviews.js --emit-packs` for the harness and neither reaches the three-paste
kit. Consequence: **the restraint ceiling is unenforced on the chat path**, and observed finding
counts floated between 3 and 6 with nothing to cut to. These are not candidates for inclusion —
they are already cited as present. Treat them as required bundle contents before weighing anything
on the candidate list, and note the cost is small.

One more datum for question 1: **quote-or-abstain needs no help.** 55 quotes across two model
families and every truncation level, 0 fabricated, including with the system prompt entirely
absent. It is stated three times across the two pastes, and that redundancy is what survives.
Whatever else the bundle carries, do not spend budget re-teaching it.


---

**Parked 2026-09-20 by the owner, on the scope audit ([AUDIT-2026-09-20.md](../AUDIT-2026-09-20.md)).** Not cancelled and not out of scope: deferred until the pilot has run, at which point it is reconsidered against what the pilot actually showed.

Reason: the bundle exists and works; this asks whether to make it wider, which is an improvement
