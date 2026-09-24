# Ticket 13, round 2 — Q2 broken down

## What you answered in round 1

- **Q1 — the page is an extra you get after pasting the prompt, the deck and the methodology. The
  same review, just laid out nicely, so leads and students can learn from it.** Not a second
  product. Recorded.
- **Q3 — not important.** Recorded, and it may disappear entirely depending on Q1 below.
- **Q2 — you asked what a readiness level is and for the question to be broken down.** That is this
  round.

---

## First: what a readiness level is, in plain words

Until September, every review ended with a one-line grade on the whole deck. Something like
*"Nearly ready — minor edits"* or *"Not ready — major rework"*. One verdict on the deck as a whole,
sitting at the top of the page where you see it before anything else.

We deleted it, for two reasons:

1. **It gave different answers to the same deck.** Run the identical deck, the identical words,
   twice, and it came back "nearly ready" once and "major rework" the other time. One team gets
   told to relax, another team with the same deck gets told to panic.
2. **People stop reading after a grade.** A student who sees "nearly ready" at the top does not
   read the three findings underneath with the same eyes.

So the rule now is: **the tool never grades the deck.** It says what is wrong, quotes the slide it
is wrong on, and the human decides whether it is ready. That rule is written down as one of the four
things that stop the project if it breaks.

**Why it comes up on the HTML page and not on the writing path.** The writing path cannot produce a
grade, because we deleted the instruction that asked for one — there is nothing to remove. The HTML
page is a layout with slots, and a row of boxes across the top is exactly the shape a grade wants to
sit in. Two things are true of the page today: the instructions still call that row **"the verdict
pills"**, and the first box in it is labelled **"Your call — Not set"**, waiting for a human. That is
a grade-shaped hole at the top of the page with a label on it.

---

## Q1: Is the page a second reviewer, or a re-print of the review you already got? `[big]`

### The scene

A team lead pastes the prompt, the methodology and her deck, and reads the review in the chat. It
names three problems and quotes the slides. She then pastes one more thing and gets the page.

Now: **where did the words on that page come from?**

- **A — A re-print.** The page shows the review she just read, laid out. Same three findings, same
  quotes, same words, in a nicer shape. She can scroll up and see they match.
- **B — A second review.** The page is produced by its own set of instructions that re-do the
  review in a different format. It can reach different findings, phrase them differently, or pick
  three different problems out of the deck.

**The file we have today is B.** Its first line says it replaces the output the main prompt asks
for, and it restates all the content rules itself — how many findings, what a fix may say, how
quotes work. It is a second reviewer that happens to be prettier.

What you described in round 1 is A.

### What each option does to her

Under **A**, she has two copies of the same thing and the page is the readable one. If the page ever
said something the review above it did not, she would see it immediately, because both are on her
screen.

Under **B**, she has two reviews. If they differ she has no way to know which one to believe, and
neither do we. She is also the only person who will ever see both.

### Where the cost actually lands

Under **A**, the cost lands on us, now: the file has to be rewritten from "here is how to review a
deck and draw it" into "here is how to draw a review that already exists". That is a real rewrite of
one file, and most of the six missing pieces stop being missing — the attempt line and the key line
are already in the review it is re-printing.

Under **B**, the cost lands on every future prompt change, and on the student who gets whichever of
the two reviews is wrong. This is also what makes your Q3 answer safe or unsafe: under A there is
almost nothing to drift, because the page carries no rules of its own. Under B there is a second set
of rules in a file no script reads, which is the thing that has already gone stale twice.

### What we know, and how well

- Both model families produced the full page first try — measured under B, once, on one deck. A has
  never been tried. It is a smaller ask of the model, not a bigger one.
- Under A the page has no opinion of its own to leak, which is most of what the next question is
  about.

### The decision

**I'd pick A**, because it is what you described, it shrinks the build substantially, and it makes
the next question much smaller.

**The best case against me:** B is what exists and what has been shown to work on two model
families. A is untested, and there is a real chance the model, asked to re-print a review, quietly
rewrites it anyway — in which case we have paid for a rewrite and still have two reviews, except now
we have told ourselves we do not. Under B at least the page is honestly a second thing.

**If you're not sure:** say so and I will try A on one deck before you decide — it is a single run.

---

## Q2: Should the page be allowed to show any overall verdict box at all? `[big]`

### The scene

A student opens her page at 11pm. Across the top is a row of boxes. One of them reads
**"Nearly ready — minor edits"**. Nobody put it there on purpose: the row exists, it is labelled in
the instructions as the verdict row, and the model filled the empty box the way a model fills an
empty box. She reads it, decides the deck is broadly fine, fixes two of the three findings and goes
to bed. Nobody else ever sees that page — no server, no log, no lead looking over her shoulder.

That exact sentence is sitting in the rendered page we have on file from September, in that exact
position, from both model families. It was legitimate then. It is the thing we deleted now.

### What each option does to her

- **A — Delete the box row from the page.** The page opens with what is wrong and where, and there
  is no box at the top for anything to sit in. She sees three findings and a slide map. There is no
  grade because there is no slot shaped like one.
- **B — Keep the row and tell the model not to put a grade in it.** She sees the row, with "Effort:
  3–5 days" and "Your call: not set" in it. The rule against a grade is a sentence in the
  instructions asking the model to behave. If it does not, she is the one who finds out.

### Where the cost actually lands

Under **A**, the cost is visual and it is yours: the top-of-page summary row is part of what makes
the page look like a product rather than a document, and deleting it makes the page plainer. It also
removes the "Your call — not set" box, which is the one place a lead was meant to record their own
verdict.

Under **B**, the cost lands on a student, alone, once. We would not find out. There is no version of
this where we catch it afterwards, because nothing on this path is recorded anywhere.

### What we know, and how well

- We have measured, on this project, that a check which *tells the reader* something went wrong gets
  ignored: 5 times out of 5. A check that *withholds the review* until the reader does something
  held 16 out of 16. The page cannot withhold anything — it arrives whole in one message. So the
  protection that works is not available here, and B is the kind we measured failing.
- Under A there is nothing to protect, which is why this question is worth more than the guard was.
- If you picked A on the previous question, the risk here is already smaller: a re-print of a review
  that contains no grade has no grade to print. A still closes it properly; B leaves the hole open
  on both.

### The decision

**I'd pick A** — delete the row. It is the only option here that does not depend on the model
behaving, and it costs one visual element rather than an open-ended piece of work nobody has built.

**The best case against me:** the box row is the part of the page a lead actually uses — it is the
at-a-glance line that lets her decide in ten seconds whether to read further, which is the entire
reason a lead would open a page instead of reading the writing. Delete it and the page is a prettier
document rather than a faster one, and the "visually nice for people" thing you asked for is
precisely the part being cut. We would also be removing the lead's own verdict box because we are
worried about the model's, which punishes the wrong party.

**If you're not sure:** a middle answer exists and I will take it if you want it — keep the row but
allow only things that are facts rather than judgements (how long the fixes take, how many findings,
how many slides), and delete the empty "Your call" box so there is no unfilled slot inviting one.

---

**If you answer only one: answer Q1.** It is the one that decides how big this is, and it makes Q2
smaller either way. Q2 can be answered after you have seen a page.

---

# Answers, 2026-09-20

**Q2 — ANSWERED: delete the row.** The owner: *"delete, we don't need verdict, we already just
have list of errors."* Option A, taken whole. Consequences, to be written into the answer when
this ticket closes:

- The box row comes out of the page. No grade box, no confidence box, and **no "Your call — Not
  set" box** either — the lead's own verdict slot goes with it, which was the named cost of A and
  is accepted.
- The instructions stop calling anything "the verdict pills". That phrase is the label on the hole.
- This closes the stop-condition-3 exposure by construction rather than by guard: there is no slot
  shaped like a grade, so the unbuildable no-level guard from ticket 27 item 6 **shrinks to a
  check that the row is absent** rather than a watcher for a level that could appear anywhere.
  It does not vanish — the model can still write a sentence — but the shape most likely to invite
  one is gone.
- The middle answer (keep the row, facts only) was offered and **not** taken.

**Q1 — still open.** Not answered and not inferred from the Q2 answer. Round 3.

**Q1 — ANSWERED, round 3: A, the re-print.** The owner: *"a"*, to a question whose A was *the page
shows the review she just read, laid out — same findings, same quotes, same words*. The file's
current design, a second reviewer with its own content rules, is rejected.
