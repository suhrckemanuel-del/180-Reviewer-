# How to ask Manuel a question

**Read revision 2 at the bottom first. It supersedes the shape in the middle of this file.**

Written 2026-09-19, after ticket 14's first grilling round. Manuel agreed with three
recommendations in a row and then said he could not actually follow them well enough to
disagree. **An answer given because the question was too dense to argue with is not an answer.**
This project already legislates against numbers that measure themselves; a decision that only
rubber-stamps the agent is the same error wearing a different hat.

Every session working this map follows this when putting a question to Manuel.

## The rule

**A question he cannot disagree with has failed, however correct the recommendation is.**

So each question must hand him the ammunition to say no. Not just less text — the *right* text.

## The shape (revision 1 — superseded, see revision 2 at the bottom)

```
### Q<n>: <the question in plain words, one line>

**Matters because:** <what breaks if we get this wrong — one line, concrete>

**The options:**
- **A** — <one line, no jargon>
- **B** — <one line, no jargon>

**I'd pick:** <A or B>, because <one line>.

**The best case against me:** <the strongest honest reason to pick the other one>

**If you're not sure:** <what he could say to punt it — "just pick", "explain X", "park it">
```

## Rules for the writing

1. **No code identifiers in the question.** Not `cacheKey()`, not `--half dev/holdout`, not
   `renderShareable()`. If a filename is genuinely the subject, name it once in plain words.
2. **No unexplained statistics.** "AUC 0.979" means nothing at a glance. Say "the matcher agrees
   with human judgement 98% of the time on the cases it was tested on."
3. **Two options, not three,** unless the third is genuinely live. A third option is usually the
   agent thinking out loud.
4. **Numbers get a unit he cares about**: minutes, tokens, dollars, or "one case in nine". Never
   a raw percentage with no denominator.
5. **Say how much it matters.** Tag each question `[big]`, `[medium]` or `[housekeeping]` so he
   knows where to spend attention. A `[housekeeping]` question should usually be a statement
   instead — decide it, say so, move on.
6. **Three questions maximum per round.** More than that and the later ones get waved through.
7. **The best-case-against is mandatory and must be real.** A strawman here is worse than
   omitting it: it manufactures the appearance of a choice.

## What does not go in a question

Findings, measurements, evidence and reasoning go **above** the questions, or in the ticket's
answer — not inside the question. The question is the decision only. If he wants the working, he
will ask, and the ticket records it permanently either way.

---

# Revision 2, 2026-09-20 — lead with the scene

Written after ticket 12's first round. The questions followed the shape below correctly and Manuel
still could not use them: *"Can you give me full context of the situation where this could happen?
Can you give context where things happen, and where outcomes matter?"*

**Revision 1 fixed the wrong thing.** It made questions short enough to read. Short is not the same
as concrete. A one-line option like *"Refuse outright"* is perfectly clear as English and still
tells you nothing about who it happens to, when, on what device, or what they do next. You cannot
disagree with an abstraction, so the rule from revision 1 — a question he cannot disagree with has
failed — was still being broken by questions that obeyed revision 1's format.

**So the rule gains a second half:** a question must name **a moment it happens to somebody**, and
**where the cost lands** when the answer is wrong. Brevity is now subordinate to that. A longer
question that puts him in the room beats a short one that does not.

## The shape, revised

```
## Q<n>: <the question in plain words, one line>  `[big | medium | housekeeping]`

### The scene

<A concrete moment. Who, when, on what device, what they were trying to do. Present tense.
Show the actual thing they would see on screen if it is short enough to show.>

### What each option does to that person

- **A — <name it>:** <what they see, and what they do next>
- **B — <name it>:** <same>

### Where the cost actually lands

<Who pays under each option, and in what. Not "risk" — minutes, re-pastes, students lost,
a bad review reaching a client board. Name the population, not the probability.>

### What we know, and how well

<The measured numbers, in units he cares about, each with its honest limit attached.>

### The decision

**I'd pick:** <A or B>, because <one line>.

**The best case against me:** <the strongest honest reason to pick the other one>

**If you're not sure:** <what he could say to punt it>
```

## What carries over unchanged from revision 1

Rules 1, 2, 4, 6 and 7 above still hold: no code identifiers, no unexplained statistics, numbers
get a unit he cares about, three questions maximum per round, and the best-case-against is
mandatory and must be real.

**Rule 3 is relaxed.** Two options is still the default, but the scene often makes a third genuinely
live, and if it does, show it.

**Rule 5 is strengthened.** Tag every question, and add a closing line naming **which single
question to answer if he only answers one**, and why the others can wait. Ticket 12's round had one
question that could not be deferred and two that could; saying so is more useful than three equal
asks.

**Where findings go is unchanged and matters more now**, because the scene makes it tempting to
smuggle evidence in. Findings and reasoning go in the ticket. What goes in the question is the
situation, the options, the cost, and the numbers he needs to weigh them — nothing that is there to
show the work.

## The test to apply before sending

Read the question back and ask: **could he picture one specific person having a bad day because of
this decision?** If not, it is still an abstraction, however short it is.
