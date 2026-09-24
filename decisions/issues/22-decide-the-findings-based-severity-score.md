# Decide whether a stacked summary score gets added to the findings list

Type: grilling
Status: resolved
Blocked by: —

## Question

---

**Scoped down 2026-09-20 by the owner, on the scope audit ([AUDIT-2026-09-20.md](../AUDIT-2026-09-20.md)).**

**Half of this already ships.** `CHAT-CONTEXT.md:324` grades every finding
`[High impact | Moderate | Minor]` and the output lists them in priority order, so *"why don't we
just list them"* describes what a pilot user already receives. The audit checked this rather than
assuming it.

**So this ticket is one question, not a redesign: does a single stacked summary number get added on
top of the list that already exists?** Everything below stands as the material for answering it -
in particular the collision with stop condition 3, which was widened on 2026-09-19 to *"the tool
produces a readiness level, for anyone"*, and the finding that the tool grades criticals at 3.3x
the human rate, so a stacked score inherits the inflation rather than escaping it.

The other questions below (the arithmetic, who sees it, the trust-boundary rows, the fate of
over-flag) only get asked if the answer to that one is yes.

---

Opened 2026-09-20 by the owner, during [ticket 15](15-decide-whether-to-keep-or-roll-back-frozen-2026-08-09.md),
in his own words:

> *"i feel we need to re think about readness level i feel it could just be based on perfect
> deliverables but more like its based on the errors it finds in the deck. so the cirtiqual ones
> are just stacked why dones we just list them i feel htats so much more simplare we just a need a
> simple scorring system for the errors we find"*

Read plainly: the retired readiness level asked *how far is this from a perfect deliverable*, which
is a judgement. The proposal is to ask *what did the review actually find*, and let the answer fall
out of the findings — criticals stack, and possibly nothing more than listing them is needed.

**This is not a resumption of the retired level and must not be worked as one.** The map's Out of
scope entry is amended, not deleted. The two objects:

| | retired level (ticket 05) | what is proposed here |
|---|---|---|
| what it is | the lowest ceiling among the blocking rules that fired | arithmetic over the findings the review already produced |
| who computes it | the model, as a judgement | the reader, or the harness, by counting |
| failure that killed it | identical bytes returned two different levels | **does not apply** — same findings give the same score |

So the specific defect that retired the level does not reach this. Three others do, and they are
what this ticket has to settle rather than assume.

### The hard part, and it is not the arithmetic

**1. Is this a readiness level by another name, and does stop condition 3 forbid it?**

Stop condition 3 was widened on 2026-09-19 to *"the tool produces a readiness level, for anyone"*,
and two rows of `22-trust-boundary.md` go red over it, knowingly. A stacked score over findings is
a single number summarising how bad the deck is. **That is what a readiness level is, and calling
it a score does not change what a student does with it.** Ticket 05's own argument for retirement
was not only that the level was unstable — it was that *"nothing fenced means nothing forwardable
past a fence"*, and that non-production beats redaction. A score reinstates the thing to fence.

The honest counter, which is why this is a real question rather than a refusal: ticket 05's stop
condition was written against a number the tool *invents*. A count of what it found is not invented,
and a student who reads "3 critical, 4 major, 2 minor" has been told something checkable — they can
go and look at the three. That is not the same act as being handed R1.

Settle this first. Everything else depends on it.

**2. The severity labels this rests on have never been checked against a second human.**

The score is only as good as the severity grade on each finding, and **nobody has measured whether
two people agree on one**. The cheap route is closed: `_INTER-RATER-RECOVERY.md:163` records that
the four second-reader worksheets are thin, one issue each and some fields empty.

This is exactly the position readiness was in before ticket 03 measured it — and when it was
measured it came back at 2 of 4, 95% CI [7%, 93%], quadratic kappa below chance. **Do not assume
the better case for severity because the old number was bad.** Decide whether this ships before or
after a severity inter-rater number exists, and if before, say what makes that acceptable.

**3. The tool's severity distribution is a long way off the human's, and it just moved.**

Measured on the nine real decks, `frozen-2026-09-19` against the golds:

| | gold (37 findings) | `frozen-2026-09-19` (42) |
|---|---|---|
| critical | 3 (8%) | 11 (26%) |
| major | 24 (65%) | 27 (64%) |
| minor | 10 (27%) | 4 (9.5%) |

Criticals run at **3.3x** the human rate. If criticals stack, they stack 3.3x too fast, and the
score inherits the inflation rather than escaping it. Ticket 16's ungated severity floor moved this
in the right direction (minors 1 in 45 to 4 in 42) and it has one run behind it.

### Settle

1. **Whether a summary score is produced at all, or only the list.** The owner's message contains
   both — *"the critical ones are just stacked"* and *"why don't we just list them"*. Listing
   findings by severity is something the chat template already does and needs no decision. A single
   stacked number is a new output and is the part that collides with stop condition 3.
2. **If a score: what the arithmetic is**, in one line a student can reproduce by hand, and what
   happens when the noise budget caps the findings at 5 — a capped list cannot distinguish a deck
   with 5 problems from one with 20.
3. **Who sees it** — student, lead, both, neither. The paths differ: the chat path shows severities
   already, the artifact path has no redaction and no stop panel at all (ticket 05).
4. **What happens to stop condition 3 and the two red trust-boundary rows**, whichever way 1 goes.
5. **Whether over-flag rate is now dead.** Ticket 15 left this deliberately open. The recommendation
   on the table, not adopted: report over-flag with no pass/fail bar, and move the gate's restraint
   bar to the severity distribution, which is matcher-free and already computed
   (`score-review.js:313-317` parses gold severities, `:582-585` emits per-review counts). The full
   argument and its two stated limits are in ticket 15 section 4.

### Constraints carried in

- **Ticket 20's Group B is not blocked on this and must not wait for it.** The emitted readiness
  level is deleted from the prompt as ticket 05 wrote it. This ticket starts from a tool that
  produces no level.
- **Ticket 07 must not set a bar on over-flag rate before this resolves.**
- Per [asking-rule.md](../asking-rule.md), question 1 above is the one to put to the owner, because
  it is the one where the agent's reflex (refuse, the map just retired this) and the owner's
  instinct (it is simpler and more honest than what we had) genuinely disagree.

Answer records: whether a score is produced, its arithmetic, who sees it, what happens to stop
condition 3, and the fate of over-flag rate.


**Owner answers recorded 2026-09-20** in [DECISIONS-2026-09-20.md](../DECISIONS-2026-09-20.md) Part 4. Read it before acting on the questions in this ticket.

---

## Answer (2026-09-20)

**A count line. No single score.** The owner's words: *"We could just do the count line, B, it's
pretty simple."* Recorded in [DECISIONS-2026-09-20.md](../DECISIONS-2026-09-20.md) Q6, and applied
by [ticket 20](20-apply-the-accumulated-edit-lists-to-the-product.md) in the same pass.

**This ticket decided nothing new and shipped something anyway**, which makes it the only ticket on
this map of which that is true. The decision was the owner's, made in one line; the work was
writing it into the output template in a form that cannot be read as a verdict.

### 1. Is a summary score produced at all? No. A count, and only a count.

`COUNT: <n> high impact, <n> moderate, <n> minor`, immediately under the `WHAT TO FIX, IN ORDER`
heading in `CHAT-CONTEXT.md`. Arithmetic over the list directly beneath it, which the reader can
check by counting.

**The fence around it is the part that matters, and it is in the template beside the line:**

> The count is arithmetic over the list below and nothing else. It is not a grade, a score, a
> readiness level or a verdict on the deliverable, and you never write it as one. Do not add a
> total, a percentage, a rating or a sentence interpreting it.

**Why that fence is load-bearing rather than decorative.** The tool calls findings high impact
about **three times as often as a human reviewer does** (criticals 26% against a gold 8%, measured
on the nine real decks under `frozen-2026-09-19`). So `3 high impact` is inflated in a known
direction, and it is inflated in exactly the direction that frightens a student — which is how the
retired grade did its damage. The owner's own case against his answer, put to him and accepted:
**a count is a grade in disguise if it is allowed to read like one.**

### 2. The arithmetic

One line a student can reproduce by hand: count the findings at each severity in the list below
the COUNT line. Nothing is weighted, summed, normalised or divided.

**The noise-budget interaction the ticket flagged is real and is not solved.** The budget caps
deep mode at five findings, so a capped list cannot distinguish a deliverable with five problems
from one with twenty. That is a limit of the count, it is inherent in capping the list at all, and
it is the second reason the count must never be read as a measure of how bad the work is. Stated,
not fixed.

### 3. Who sees it

Everyone, because it is part of the one output template both audiences receive. There is no
branch: the chat path already shows per-finding severities to both, and the count adds no
information that was not already on the screen. The artifact path (`PASTE-2C`) gets no count line
in this pass -- it is a separate template and the ticket named the chat output.

### 4. Stop condition 3 is untouched, and the two red rows stay red for their own reasons

**A count line is not a readiness level and does not reopen stop condition 3.** The condition
forbids the tool producing a level, ceiling, grade or overall score. A count of items in a visible
list is none of those: it is not invented, it has no scale, and it is checkable by the reader in
ten seconds. The validator's level-rejection check (`check-review-v2.js`) is unchanged by this
ticket and still rejects `readiness.level`, `blockingIssues[].ceiling`, `grade` and `rating`.

`22-trust-boundary.md` rows :21 and :22 went NOT MET in this pass for an unrelated reason -- the
hosted page they describe was withdrawn. Nothing in this ticket moved them.

### 5. Over-flag rate: still open, and deliberately not decided here

Ticket 15 left it open and this ticket does not close it. The recommendation on the table --
report over-flag with no pass/fail bar and move the restraint bar to the severity distribution --
belongs to whatever ticket 07 becomes. **Ticket 07 must still not set a bar on over-flag rate**;
that constraint survives unchanged.

### 6. What this ticket did NOT settle, and must not be read as settling

- **The severity labels the count rests on have never been checked against a second human.** The
  ticket asked whether a score ships before or after a severity inter-rater number exists. A count
  line ships before, and the reason it is acceptable is that a count makes no claim the underlying
  labels are right -- it says "the tool called three of these high impact", which is true whatever
  a second reader would have said. **A score would have needed that number. A count does not.**
  If anything downstream ever aggregates or compares these counts across deliverables, the
  inter-rater question is live again and must be answered first.
- **The 3.3x over-call is not corrected by this ticket**, only labelled. Ticket 16's ungated
  severity floor moved it in the right direction with one run behind it.

Edits applied by [ticket 20](20-apply-the-accumulated-edit-lists-to-the-product.md), not filed for
a later session.
