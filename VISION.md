# Vision

## The sentence everything else serves

**A consultant finishes with work they have confidence in, grounded in evidence they went and
found.**

Not a final truth. Not a grade. Not a better deck produced by a machine. A defensible choice, held
by the person who has to defend it.

The owner put it this way on 2026-09-24:

> It's not that there's a final truth. It's more that the things that they make, they have
> confidence in them, and they can have grounding evidence. Based on data they found.

and:

> This is a reviewer, which then helps you and prompts you to think better. That's the goal. It's
> not doing the whole thing for you.

The same idea was already written, months earlier, at the bottom of the chapter's own case-workshop
slide — before any of this software existed:

> **You will not find the right answer. You will pick one, and be able to say why.**

That the two were written independently is the strongest evidence available that this is the right
target. It is also a warning: the tool spent months drifting away from a goal that was already
articulated in the room.

## Why a reviewer and not an assistant

The obvious product is an assistant that improves the deck. It is the wrong product here, for a
reason specific to 180DC.

**The organisation's value to its members is that they learn to consult.** The client work is real
and it matters, but a chapter that ships better decks while producing worse consultants has
destroyed the thing it exists for. Total turnover inside three years means every cohort that learns
less is a permanent loss — there are no seniors to carry the knowledge forward.

An assistant that drafts produces a better deck this week and a weaker consultant every week.

The premise is **not** whether students use AI. They already do. It is whether they use it at a
level that builds them.

## The four commitments

### 1. Attempt first

Nothing unlocks until the consultant has committed their own read of their own work. The reviewer
**refuses** — and the refusal cannot be argued past; that was tested against a user pushing back.

This is the generation effect and the "answer key" model: the junior attempts the work, the AI
grades the attempt, and the difference is where the learning is. There is no difference to learn
from if you never formed a view.

It is also the only student-side instrument this system has. The gap between what the consultant
saw and what the reviewer saw, closing over a term, is the thing actually worth measuring.

### 2. No drafting

The reviewer surfaces findings. **The consultant writes every word.**

This was tested, hard, and the test is why the commitment survives in this form. A "worked example"
was added — one invented sentence showing the *shape* of a good answer — because the output was
correct and students could not act on it. Three different wordings were tried across 26 runs on two
model families. The device worked on one family and not the other, and no wording moved that.

Worse, licensing one finished sentence made the model start handing over finished sentences in the
*next field along*, including one built entirely from the team's own figures — pasteable, requiring
no evidence they did not already have.

The original objection to AI-drafted fixes was that *"the human must visibly edit"* is
unenforceable, because a cosmetic edit is undetectable. **Text that arrives finished needs no edit
at all.** The objection returned in full and the feature was withdrawn.

What replaces it is the Socratic turn: instead of showing the sentence, ask the question that makes
them derive it.

Full record: [decisions/parked-features.md](decisions/parked-features.md),
[decisions/ticket-26/RESULTS.md](decisions/ticket-26/RESULTS.md).

### 3. No grade

The tool produces no readiness level, no score and no overall verdict, for anyone.

Not because grading is philosophically wrong, but because **this one did not work**: the same
deliverable, byte-identical input, came back with two different readiness levels. A number that
unstable, attached to work going to a real board, is worse than no number.

A count of the findings in the visible list survives — `2 high impact, 1 moderate` — because it is
arithmetic over a list the reader can see, not a judgement. It is fenced against being written as a
verdict, because the tool calls findings high impact about **three times as often as a human does**
and a summary would inherit that inflation rather than escape it.

### 4. Every finding is checkable

Every finding carries a **verbatim quote** and a location. If the consultant cannot find the quote
in their own work, the finding is discarded — not softened.

This is the only defence a student has against a confident machine, and it is the one that has held
best under testing: 55 quotes, two model families, every truncation level, **zero fabrications**,
including with the system prompt entirely missing.

## What it costs to hold these

Each commitment gives something up, and the tradeoffs are accepted rather than hidden:

- **Attempt first** costs the consultant who is stuck at midnight and just wants help.
- **No drafting** costs the weakest consultants most — they are the ones who most need to see what
  good looks like, and this refuses to show them.
- **No grade** costs the lead who wants to know how much to trust a review at a glance.
- **Checkable findings** cost the reviewer the ability to say anything it cannot quote, including
  true things about what is *missing* from a deck.

If these are ever revisited, they should be revisited against these costs and not against a
re-argument of the principle.

## Where this is going

The repo is the system. Use it on real work, log what was wrong, change the prompt against the log.
No separate eval apparatus gating the loop — that was tried, and it produced decisions rather than
improvements.

Next, in order: ground the reviewer in the research it was built from but never actually cites;
give a consultant a **named vocabulary** they can carry into a conversation with a lead; then teach
the case frameworks — starting with the chapter's own, in [frameworks/](frameworks/).

The measure of whether any of it worked is not a scorecard. It is whether a consultant's own read
of their own work gets closer to the reviewer's, over a term, without the reviewer ever writing a
word of their deck.
