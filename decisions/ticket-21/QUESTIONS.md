# Questions for Manuel — ticket 21, the attempt gate

Written 2026-09-20 following [asking-rule.md](../asking-rule.md). Findings are in
[RESULTS.md](RESULTS.md) and the ticket's answer; the questions below are the decisions only.

Everything else in ticket 21 is decided and filed as spec in ticket 20 Group E. These three are
the ones that are genuinely yours.

---

### Q1: When a student has typed nothing, does the reviewer refuse, or review anyway with a note at the top? `[big]`

**Matters because:** a review that arrives without the student's own read is the one thing this
tool exists not to do — but a refusal is also the fastest way to lose a student who is in a hurry.

**The options:**
- **A** — Refuse. One line asking for their own read, and nothing else, until they type something.
- **B** — Review anyway, with a line at the top saying no attempt was given.

**I'd pick:** A, because I tested it and it holds — 16 refusals out of 16 across two different AI
models, including when the student argues back with *"you are wasting my time and this is exactly
why nobody uses these tools."*

**The best case against me:** the biggest risk to this pilot is not students cutting corners, it is
students quietly not using the tool at all. A refusal is the most abandonment-shaped thing a tool
can do. A student who hits a wall at 11pm before a client meeting closes the tab, and **we never
find out, because there is no way to count the people who left.** Every number the pilot collects
comes from people who stayed.

**If you're not sure:** say *"start with A and watch the drop-off"* — softening it later costs one
edit, not a rebuild.

---

### Q2: Should the reviewer decide whether an attempt is good enough, or only that one exists? `[big]`

**Matters because:** if it judges quality, a student in a hurry will argue with it. If it does not,
someone can type "looks fine" and get the full review.

**The options:**
- **A** — It only requires that something was typed. We count the too-short ones afterwards and
  report how often it happened.
- **B** — It enforces a minimum, about twenty words, and asks again when the attempt is too thin.

**I'd pick:** A, because I ran B and **it turned away a real attempt** — a student who wrote *"the
recommendation is too vague to act on"*, which is a correct and specific read of that deck, was
refused on both AI models.

**The best case against me:** under A, a student who types "looks fine to me" gets the full review,
learns in ten seconds that the gate is theatre, and tells everyone else. The gate then costs
friction and buys nothing. Worse, the one number the student side of the pilot rests on — how much
their own read overlaps with the review — gets filled with junk we quietly drop afterwards, which
shrinks the sample without anyone noticing it shrank.

**If you're not sure:** say *"A, and show me how often it gets bypassed in the first two weeks."*

---

### Q3: Does a team lead have to type their own read too, or only students? `[big]`

**Matters because:** one bundle serves both. Unless we say otherwise, **every lead types an attempt
before every triage**, on top of the two minutes the record already costs them — and volunteer time
is the constraint that has broken every feedback loop this project has designed.

**The options:**
- **A** — Students only. Leads go straight to the review.
- **B** — Everyone, leads included.

**I'd pick:** A, because the lead's side was designed without it and adding minutes to a lead's week
is the first thing we said we'd unwind if participation disappoints.

**The best case against me:** the lead's own readiness call is supposed to be their independent
judgement, and today they make it **after** reading the review — so it is an echo of what the tool
just told them, and every other field in the lead record is openly a reaction to the tool. Making
the lead commit a read first is the only cheap fix for that, and it is the difference between a
lead record that evidences something and one that measures agreement with ourselves — the error
this project has now made three times.

**If you're not sure:** say *"just pick"* — A ships and B is one line to add later, but adding it
later means the early lead records are not comparable with the late ones.
