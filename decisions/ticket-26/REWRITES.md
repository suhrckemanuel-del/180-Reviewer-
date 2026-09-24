# Ticket 26 — three findings rewritten by hand

Written 2026-09-20. **Nothing here has touched the prompt.** These are hand-written objects for the
owner to react to, per the ticket's method (prototype, HITL).

Source material, and it is thin: **two reviews on disk, one model family, one synthetic deck.**
Five findings existed to choose from —
[haiku--student-attempt.md](../ticket-20/runs/haiku--student-attempt.md) (2) and
[haiku--lead-nothing.md](../ticket-20/runs/haiku--lead-nothing.md) (3). Three are rewritten below.

**Severities are left exactly as the runs produced them.** The tool over-calls high impact about
threefold, and rewriting the register and re-triaging at the same time would make it impossible to
say which change did what. A is High impact because the run said so, not because this session
agrees.

---

## A. The 8% comparator — the anchor, unchanged

From `haiku--student-attempt.md`, finding 1. This is the object the owner already approved
(*"I really do like this approach to teaching them"*), reproduced without edits so it stays the
fixed point the other two are measured against.

> **1. Nobody can tell if 8% is good.** [High impact]
> Slide 8 — *"The 8% assumption is conservative against the 32% attendance rate and is the main
> thing to test."*
>
> **The problem:** you compared 8% to your own event attendance, not to what membership conversion
> looks like anywhere else.
>
> **Why it matters:** going to an event is free and costs an evening. Paying £45 a year is a
> different decision by a different person. So "conservative against 32%" tells the board nothing
> about 8%. A board member who has run a membership scheme already has a number in their head, and
> yours has nothing to meet it with.
>
> **Do this:** find membership conversion for 3-5 comparable non-profits. Put 8% next to them.
>
> **Aim for a line like:** *"Comparable arts non-profits convert 5-12% of their mailing list. We
> assumed 8%, mid-range, and the soft launch tests it."* — that's the shape, not your words. Your
> numbers will be different.
>
> **Answer first:** what do comparable organisations actually convert?

The original, for the contrast:

> 1. The 8% conversion rate needs a peer benchmark to mean anything to the board. [High impact]
>    Where: Slide 8
>    Quote: "The 8% assumption is conservative against the 32% attendance rate and is the main thing to test."
>    Why it costs the client: The board cannot assess whether the recommendation is realistic without knowing how 8% compares to actual membership conversion in similar non-profits. Event attendance and membership commitment are different behaviors, so "conservative against 32%" does not tell the board whether to expect 8% or a fraction of it. The board could green-light the recommendation thinking 8% is defensible and later abandon it when soft launch falls short, or walk away from a sound bet.
>    What to do: Research what membership conversion looks like in 3-5 comparable non-profits in your region before soft launch. Find the range and where 8% sits in it. If 8% is typical, say so. If it is thin, name what you are betting on instead—what drives conversion in Client E's case. The team's hypothesis about engaged contacts and clear benefits is worth making explicit as your basis.
>    Answer first: What do comparable organisations see as membership conversion rates?

---

## B. The staffing assumption — a number that does not exist anywhere yet

From `haiku--student-attempt.md`, finding 2. Chosen because the missing figure is not out on the
internet to be researched — it comes out of a conversation with one person. If the rule only works
when the student can go and look something up, it breaks here.

> **2. You say the events won't strain staff, and nobody has counted the hours.** [High impact]
> Slide 9 — *"We assume the mailing list is accurate and that members-only events do not strain
> staff. A soft launch to the most engaged 200 contacts tests both before the full launch."*
>
> **The problem:** you listed staff strain as an assumption and then left it as one. There is not a
> single hour anywhere in the deck.
>
> **Why it matters:** Client E has one part-time coordinator and no money for a second. The board is
> not deciding whether members-only events are a nice idea; it is deciding whether one person can run
> them on top of the job they already have. "We assume it does not strain staff" reads as: nobody
> asked them.
>
> **Do this:** sit down with the coordinator and put hours against each piece — the mailing, the
> sign-ups, the two events. Then say whether it fits.
>
> **Aim for a line like:** *"The two members-only events cost about 18 coordinator hours each. There
> are roughly 30 spare hours across the autumn, so one event runs this year and the second waits."*
> — that's the shape, not your numbers.
>
> **Answer first:** how many hours do the two events actually take, and does the coordinator have
> them?

---

## C. The 5% gate — the hard case, and the one closest to the line

From `haiku--lead-nothing.md`, finding 2. Chosen deliberately because it is the case the
target/draft rule is most likely to fail on: the team probably *has* a basis for 5% and simply did
not write it down, so the "missing fact" is a sentence rather than a figure, and the example ends up
built mostly out of the student's own numbers.

> **2. Nothing says why 5% is the number that decides month three.** [Moderate]
> Slide 10 — *"Month two: review conversion against the 8% target. Month three: full launch if the
> soft launch clears 5%."*
>
> **The problem:** you set 5% as the go/no-go gate and never say where 5% came from.
>
> **Why it matters:** the board has to live with this gate in eight weeks. If the soft launch comes
> in at 6%, nobody in the room can say whether that is a pass with room to spare or a fail dressed up
> as one, so the decision goes to whoever argues hardest.
>
> **Do this:** say in one line what 5% is — break-even, the floor you would accept, or a judgement
> call. If it is a judgement call, say that.
>
> **Aim for a line like:** *"At £45, 5% of 200 contacts covers the £400 the soft launch costs to
> run, so 5% is break-even and below it we stop."* — that's the shape, not your numbers.
>
> **Answer first:** what is 5% — break-even, a floor you would accept, or a guess?

**Why this one is worth the owner's attention.** Everything in that example except `£400` is the
student's own number. It still passes both halves of the audit test below, but it passes narrowly,
and it is the shape a later session will point at when arguing the line has moved again.

---

## The rule: what makes an example a target rather than a draft

The working line in the ticket — *invented numbers are a target, their own numbers are a draft* —
**does not survive contact with the object the owner approved.** Example A contains "We assumed 8%",
which is the student's own number, taken from their own slide. Read strictly, the working line
forbids the thing that was approved.

The line that does hold, and that keeps A, B and C all legal:

### The rule, as a model would be given it

1. **A finding earns a worked example only if it names something that is not in the deliverable
   today** and that the student has to go and get — a figure, a source, a comparison, a number that
   only exists once someone is asked. A finding that is purely about wording, ordering or emphasis
   gets **no example**. That is the parked feature, and it stays parked.
2. **The example is built around the missing thing, and the missing thing is invented.** Numbers
   already in the deliverable may be reused to hold the sentence together; the number the finding
   sends them to go and find must be a stand-in.
3. **The example is written after the finding and may contain nothing the finding has not already
   said** — only the facts in `The problem:` and `Do this:`, plus the invented stand-in.
4. **It is introduced as a shape, never as text**: *"that's the shape, not your numbers."*

### The audit test, which a reader can run in about ten seconds

Both halves must pass.

- **Strike out every invented value.** What is left must have a hole in it where the evidence goes.
  If what is left is a sentence the student could put on a slide, it was a draft.
- **Change the invented value to something wild.** The sentence's conclusion must change with it.
  If the conclusion survives any value of the missing number, the example is not a target for their
  evidence — it is a draft of their argument.

Run against the three:

| | strike the invented values | flip the invented values |
|---|---|---|
| **A** (5-12%) | *"Comparable arts non-profits convert __ of their mailing list. We assumed 8%, mid-range…"* — hole. Passes. | at 20-40%, "mid-range" becomes "we are low". Conclusion flips. Passes. |
| **B** (18 hours, 30 hours) | *"The two events cost about __ hours each. There are roughly __ spare…"* — hole. Passes. | at 4 hours against 30 spare, both events run. Conclusion flips. Passes. |
| **C** (£400) | *"…covers the __ the soft launch costs to run, so 5% is break-even"* — hole. Passes, narrowly. | at £2,000, 5% is nowhere near break-even. Conclusion flips. Passes. |

### When the finding has no number in it

Clause 1 answers it: **no missing fact, no example.** A finding that says the title buries the point,
or that slide 6 should come before slide 4, gets the first five fields and stops. This is not a gap
in the rule — it is the rule refusing to become the thing that was parked, which was help with
titles, wording and chart labels.

---

## What this rewrite does not do, and it should be said plainly

**It is not shorter.** Finding 1 in the original runs about 163 words across its two prose fields;
the rewrite runs about 147 across four. The gain is not length, it is that a student can stop
reading after `The problem:` and still know what is wrong, and stop after `Do this:` and still know
what to do. If shorter is also wanted, that trades directly against the example, and it is a
separate decision.

**The 40-word budget is not merely unenforced, it is wrong.** `Why it matters` in these three hand
rewrites runs **58, 53 and 49 words** — written by hand, with no model in the loop and no incentive
to pad. The target register does not fit in 40. Restating 40 would have failed even if the model had
obeyed it, which is a second reason beyond the one already known.

So the proposed mechanism for the budget, decided rather than asked:

- replace the word count with **a sentence cap**, which a model can actually count: title one
  sentence, `The problem:` one sentence, `Why it matters:` at most four, `Do this:` at most two,
  `Aim for a line like:` one plus the disclaimer, `Answer first:` one question;
- give `Why it matters` a **shape obligation** that is self-limiting — it must name a contrast
  between two things and the person who is affected by it — rather than a length;
- keep a stated budget of **about 55 words** for `Why it matters`, which is where the register
  actually lands, not where we wish it landed.

Whether any of that holds is what the run measures. None of it is claimed to work yet.

---

## Guarding the two failure modes, in the template text itself

**`The problem:` and `Why it matters:` collapsing** is the regression risk. They are given
non-overlapping jobs that can be checked from outside:

- `The problem:` is about **the deliverable**. What is wrong with the work, addressed to the person
  who made it.
- `Why it matters:` is about **the reader of the deliverable**. What happens in the board room.
  Test: if `Why it matters` is still true with no board, no client and no decision in it, it has
  collapsed into a restatement of the problem.

**The model writing the example first and drafting the finding around it** is guarded by clause 3 —
the example may contain nothing the finding has not already said. That is checkable after the fact:
every claim in the example traces to `The problem:` or `Do this:`, or it is the invented stand-in.

---

## Limits to carry into the answer

- **One synthetic deck, one model family, two reviews.** The register problem may look different on
  a real deck with real slide text, and nothing here establishes that it does not.
- The deck is unusually number-dense. **A deck whose findings are mostly about structure and
  wording would get very few worked examples under clause 1**, and whether that is the right
  outcome or a failure of the rule cannot be told from this material.
- The three rewrites are one person's register. Whether a model can hold it is the open question,
  and it is the only question the run can answer.
