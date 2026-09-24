# Rewrite the finding for a student who has to act on it tonight

Type: prototype
Status: closed 2026-09-24
Blocked by: —

## Question

Opened 2026-09-20 by the owner, reacting to the first review off the shipped configuration
([ticket-20/runs/haiku--student-attempt.md](../ticket-20/runs/haiku--student-attempt.md)).

His words: the information is **valid and aligned with the philosophy, but it is not converting to
applicable.** It needs to be easier to digest, clear simple English, with examples explaining why
it matters — *"reducing resistance and maximizing effectiveness of the output"*.

**This is not a question about what the reviewer finds. It is a question about the register it
writes in.** The findings in that review are correct. A student with a deck due tomorrow would
struggle to act on them, and that is the whole value of the tool.

### What the run actually shows, traced to the prompt

Read finding 1 of that review as a twenty-year-old on a Sunday night:

1. **The titles are consultant register, not instructions.** *"Staffing assumptions merit explicit
   testing before the board decides."* A student cannot tell from that whether they have a problem
   or a suggestion. Nothing in the prompt governs the title's register; `LEAD WITH THE POINT`
   governs its *order* only.
2. **`Why it costs the client` ran about 90 words against the prompt's stated 40**
   (`04-prompt-templates.md`, `LEAD WITH THE POINT`), in one unbroken block. The budget is stated
   and is being overshot by 2x, which means stating it again will not fix it.
3. **There is no example of what good looks like.** *"Find the range and where 8% sits in it"*
   names the task and never shows the target. A student who did not already know what a good
   comparator sentence reads like cannot produce one from that.
4. **The single most useful line in the review is the last one.** In `THE HABIT TO BUILD`:
   *not "our assumption is conservative" but "conservative means X percentile in comparable
   groups."* That is the worked example, and it sits at the bottom, detached from the finding it
   would have made actionable.

Point 4 is the finding this ticket exists because of: **the device that makes the output convert
is already in the prompt, in the wrong place, once per review instead of once per finding.**

### The shape the owner reacted to and approved

Shown to him as a hand-rewrite of finding 1, and approved in principle
(*"I really do like this approach to teaching them"*):

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

Four devices are doing the work, and they should be named separately because they can be adopted
separately:

- **a plain-English title that states the problem**, not the remedy;
- **a one-line `The problem:` before the reasoning**, so the reasoning is optional on a first read;
- **a concrete contrast in `Why it matters`** (a free evening against £45) instead of abstract
  consequence;
- **`Aim for a line like:` — a worked example with invented numbers.**

### The boundary this moves, and it is the owner's to move

**`Aim for a line like` crosses the "no drafting" line the owner set while charting** — *the
reviewer surfaces findings and the consultant writes every word* — which is in
[parked-features.md](../parked-features.md) and in the map's Out of scope.

He has approved the direction knowing that. **This ticket has to state the new boundary precisely
enough that a later session can tell a worked example from a draft**, because "no drafting" was
load-bearing and the replacement must be too. The distinction on the table, not yet settled:

> An example built from **invented numbers** is a target. The student cannot paste it, because they
> still have to go and find the real figure. An example built from **their own numbers** is a
> draft.

That is a distinction this session proposed; it is not yet measured and not yet ruled on. **It is
the first thing this ticket must settle**, because every other device here is cosmetic and this one
is not.

### Settle

1. **The exact finding template**, field by field, replacing the five-field block in
   `CHAT-CONTEXT.md`'s `WHAT TO FIX, IN ORDER`.
2. **The worked-example rule**: what makes an example a target rather than a draft, stated so a
   model can apply it and a reader can audit it. Including what happens when the finding is about
   something with no number in it.
3. **Whether the register rules bind on lead mode too**, or only the student-facing modes. A lead
   triaging four decks on a Tuesday night may want the dense version.
4. **What happens to `THE HABIT TO BUILD`** now its best device is distributed into the findings.
   It may still earn its place; it may now be redundant.
5. **How the word budgets get enforced**, given the current one is stated and overshot 2x.

### Do not

- **Do not let the example carry the student's own numbers.** See the boundary above.
- **Do not build this into `PASTE-2C` yet.** The artifact path renders findings, so it must be
  built against the settled shape, not this one ([ticket 27](27-bring-the-artifact-path-level-with-the-prose-path.md)).
- **Do not ship it unverified.** It is a prompt change to the field that carries the entire product
  value. Every prompt change on this map that was not re-run moved something nobody predicted, and
  this one touches severity-adjacent text (`Why it matters`) in a tool that already over-calls high
  impact threefold.

### The method

Prototype, HITL. **Rewrite three findings by hand, in the target register, from reviews already on
disk** — the owner reacts to those rather than to a description. Then the template goes into the
prompt and the run measures whether the model can actually hold the register, which is the part
nobody can predict. Two candidate failure modes worth watching for specifically:

- **the model writes the example and then also writes the finding around it**, drifting into the
  draft it was told not to produce;
- **`The problem:` and `Why it matters:` collapse into each other**, which would make the output
  longer rather than clearer and would be a straight regression.

Answer records: the template, the worked-example rule, what happened to the habit section, and what
the run showed about whether the register holds.


---

## Answer, 2026-09-24

**The register change ships. The worked example does not.**

### 1. The finding template

Short and deep mode replace the five-field block with: a full-sentence title and severity, the
location and verbatim quote on one line, then `The problem:` (the deliverable, addressed to whoever
wrote it), `Why it matters:` (the *reader* of the deliverable -- a contrast between two things and
the person the difference lands on, about 55 words), `Do this:` (the move, not the words),
`Answer first:`. **Lead mode is unchanged**, on the owner's ruling -- a lead triaging several decks
wants the compressed version -- plus one clause saying the student shape does not apply there.

### 2. The worked-example rule: settled, then WITHDRAWN

The rule the ticket demanded was produced and it is auditable: **an example is a target when the
conclusion inside it is controlled by a figure the deliverable does not yet contain.** Two reader
tests -- strike the invented values and a hole must remain where the evidence goes; change an
invented value and the conclusion must change with it. The blunt version on the ticket ("their own
numbers make it a draft") **forbade the object the owner approved**, which contains "We assumed
8%"; the version above keeps it and is checkable in ten seconds.

**A model will not hold it.** Three templates, twenty-six runs, two families -- self-audit,
trigger-plus-conditional-form, and both combined against a pre-registered bar of zero
conclusion-asserting examples. The bar failed 3 of 10. Codex swung from 6 of 10 to 0 of 9 to 7 of
10 on wording changes; Haiku never produced a reliable one. **No wording moved the family split**,
which is the evidence that wording was not the variable in control.

**The deciding evidence was collateral, not the examples.** `Do this:` -- a field with no exception
-- produced finished pasteable sentences, one built entirely from the team's own figures. The
original "no drafting" objection was that *"the human must visibly edit"* is unenforceable; text
that arrives finished needs no edit at all. That is the owner's stated condition for withdrawing
rather than weakening, and it is met. Recorded in [parked-features.md](../parked-features.md) with
the rule preserved so a later attempt starts from it.

**The owner's criterion, given 2026-09-24, is what made the call decidable**: the goal is not a
final truth but students having confidence in work they can ground in evidence they found. Under
it, absence of an example is neutral and an example that hands over a conclusion is the only
harmful outcome -- so the bar became "never hands over a conclusion" rather than "always fires",
and that bar is the one that failed.

### 3. Register rules on lead mode: no

Student modes only. Verified across three rounds: **no bleed on any lead arm** except one round-1
Codex arm that appended the example line, which the added clause addresses.

### 4. `THE HABIT TO BUILD`: deleted

The owner's call -- *"not that necessary, it's just an idea"* -- and his reasoning went further than
the question asked: the teaching belongs inside the findings, through how the argument is built,
not in a section at the bottom repeating it. Gone from 10 of 10 arms in both modes, both families,
with no model reinstating it.

### 5. Word budgets: not restated, re-mechanised

The stated 40 words was **not merely unenforced, it was wrong** -- three hand-written rewrites in
the target register landed at 58, 53 and 49. The field was split and given two different jobs
instead. `Why it matters` now runs about 31-55 words against the 90-word block that opened this
ticket. **Splitting the field moved it; the number never would have**, which is the one mechanism
finding clean across every round and both families.

A cross-paste contradiction was fixed on the way: paste 1 budgeted the same field at 40 words while
paste 2 said 55. Paste 1's budget is now scoped to the record fields it names.

### Cost

Paste 2 grows **+383 tokens, +6.2%** -- down from +808 with the example in.

### What this ticket found and did not fix

- **[Ticket 28](28-stop-do-this-handing-over-pasteable-text.md)**: `Do this:` hands over pasteable
  text, worse under the amendment and **still present after withdrawing it**, on Haiku only. The
  amendment aggravated the defect rather than causing it, so this document's first causal claim was
  corrected in [RESULTS.md](../ticket-26/RESULTS.md).
- **[Ticket 29](29-the-interlock-false-alarmed-on-a-complete-bundle.md)**: the truncation interlock
  refused a **complete, byte-identical** bundle once and reviewed it on re-run. Ticket 12 measured
  0 false alarms in 14; this is the first, and it is stochastic on identical input.

### Limits

One synthetic, number-dense deck. The Haiku arms are subagents reading a transcript while Codex is
piped to a fresh process, so **family and harness are confounded** and this run cannot separate
them -- inherited from tickets 04, 12, 20 and 21. Round 1's Codex ran on a binary that Codex has
since deleted; the round-1 template was re-run on the current binary to prove the round-2 collapse
was the template and not the instrument. Firing rates describe these runs and are not estimates.

Working record: [ticket-26/RESULTS.md](../ticket-26/RESULTS.md), hand-rewrites in
[ticket-26/REWRITES.md](../ticket-26/REWRITES.md).
