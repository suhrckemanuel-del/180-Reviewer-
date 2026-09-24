# Ticket 13, round 1 — questions for Manuel

## Before the questions: what saying yes costs

You asked to see the HTML output and to run the tickets that finish it. Two different things, and
the gap between them is the whole of this ticket.

**Seeing it is nearly free.** Two rendered pages are already on disk from the free-tier work in
September. They look right. They also show a readiness pill reading "Nearly ready with minor edits"
and a confidence label — the two things we deleted on 20 September because the level gave two
different answers on identical input. Re-running one real deck through today's instructions and
sending you the page is one session and commits nothing.

**Shipping it is not.** The build behind this ticket is six missing pieces plus one item nothing in
this project has ever built: something that stops a readiness level appearing on that page. The
prose path meets that rule by accident of how it works — it produces no level, so there is none to
remove. The HTML page is different: the model writes the whole page, and the only thing between us
and a big "Ready to send" pill is a sentence in the instructions asking it not to.

And we have already measured what that kind of protection is worth here. A check that *tells the
reader* something went wrong got ignored every time we tried it, 5 tries out of 5. A check that
*withholds the review* until the reader does something held 16 out of 16. The HTML page cannot
withhold anything — it arrives whole, in one message, and the student opens it. The protection that
works is not available on this path, and the one that is available is the one we measured failing.

That is the price. Everything below assumes you have read it.

---

## Q1: Is the HTML page something we hand people, or something you look at once? `[big]`

### The scene

A team lead in a chapter we have never met opens the setup doc in February. She has a deck due to a
client board on Thursday. The doc offers her two ways to run the review: paste three things and get
writing back, or paste four things and get a page. She has ten minutes and no idea which is the one
we actually maintain, so she picks the one that sounds nicer.

### What each option does to her

- **A — You look at it once, we ship one path.** She is offered one way to run the review, the one
  that ships. I send you a freshly rendered page this week so you can see what the format gives us,
  and we decide about it again after the pilot, with real decks behind us. The HTML instructions
  stay in the test kit labelled as an experiment, not as something anyone is handed.
- **B — Leads can ask for it.** She sees both. The page becomes a fourth thing in the bundle and
  everything in Q2 and Q3 follows: the guard, the six missing pieces, joining the generator.
- **C — Retire it.** The HTML instructions are deleted and the follow-on build is cancelled. She
  sees one path and so does everyone after her, permanently.

### Where the cost actually lands

Under **A**, the cost is yours: you wait until after the pilot to decide whether the format is
worth having, and you get one page to look at in the meantime. Nobody downstream pays anything.

Under **B**, the cost lands on students. The page is the surface a level can appear on, and the
student is the reader nobody is watching — she is alone with it at 11pm on her phone. It also lands
on whoever inherits this project in five months, who now maintains two formats instead of one, and
who has no way to tell they have drifted apart.

Under **C**, the cost is that a format two model families rendered correctly first try, and which
you want, is thrown away on the strength of a pilot that has not run yet.

### What we know, and how well

- Both model families produced the full page first try, complete and rendering correctly. That was
  measured once, on one deck, on the version that still had the readiness pill in it.
- The page has never been read against the current instructions. The prose half was in that same
  state last week and turned out to contradict itself in two places, one of which put the wrong
  version stamp on every record we would have collected.
- The pilot ships the writing path whatever we decide here. Nothing in this question delays it.

### The decision

**I'd pick A**, because it gives you the thing you actually asked for — seeing it — this week,
without buying a protection problem nobody has solved, and it keeps C available after the pilot
instead of spending the decision now.

**The best case against me:** A is a decision not to decide, and this ticket was parked once
already on exactly that reasoning. The format is the one thing in this project that makes the
review look like a product rather than a wall of text, and if it is never the thing anyone is
handed, it will never be finished — "after the pilot" is where features go to stop existing. You
have seen the mockups; you know the page is the good version. Deferring it a second time is
choosing the plain version by default, three months running.

**If you're not sure:** say "send me the page first" and I will render one this week and bring this
question back with the real thing in front of you.

---

## Q2: If it ships, who catches a readiness level on that page? `[big]`

### The scene

A second-year student gets her page back at 11pm the night before the team's internal deadline. At
the top, where our instructions never put anything, is a pill reading **"Nearly ready — minor
edits"**, because the model filled in a shape it had seen before. She reads that, decides the deck
is broadly fine, fixes two of the three findings and goes to bed. Nobody else ever sees that page.
There is no server, no log, no lead looking over her shoulder.

That is not hypothetical wording — it is the exact string sitting in the rendered page on disk from
September, in the pill position, in both model families.

### What each option does to her

- **A — Accept it as a known gap, in writing, and give the page only to leads.** She never sees the
  page; her lead might. If a level appears on the lead's copy, a lead is a reader who has been told
  the tool states no level and can disregard it. The gap is written on the accepted-gaps list with
  today's date, not quietly carried.
- **B — Build a protection first and do not ship the page until it works.** She never sees the page
  until somebody has solved a problem nobody has solved, and I cannot tell you today what that
  solution is or how long it takes. That is the honest shape of B: open-ended.

### Where the cost actually lands

Under **A**, the cost lands on the rule itself. We wrote down in September that the tool produces
no level for anyone, and we would be shipping a surface where that holds by request rather than by
construction. Two rows of the trust document are already red; this would be a third thing carried
on trust, and the person who inherits this in five months reads a rule that is true of one path and
aspirational on the other.

Under **B**, the cost lands on the calendar and on you: the format you asked for does not exist
until an unbounded piece of work finishes, and the follow-on build stalls behind it.

### What we know, and how well

- The thing that *reports* a problem to the reader was ignored 5 times out of 5 in our own testing.
  The thing that *withholds the review* until the reader acts held 16 out of 16. The page cannot
  withhold — it arrives whole.
- The instructions do already say, in plain words, that the page states no level and no confidence
  label. That is a request to the model, and it has never been tested. The pages we have on disk
  predate it.
- The page is not free-form: the instructions say fill in a data object and paste a fixed template
  underneath. There is no level field to fill, so a level would have to come from the model editing
  the template or inventing a row. Narrower than "anything could happen" — still nothing watching.

### The decision

**I'd pick A** if the page ships at all, because B is an open commitment in exchange for a
protection the shape of this path cannot really provide, and A at least puts the exposure on the
reader best equipped to shrug it off.

**The best case against me:** A ships a page to leads that violates, in principle, the one stop
condition this project enforced hardest — and leads are precisely the population we said we would
*not* trust with a level, because trusting them with it was the readiness feature's whole pitch and
it failed. "Accepted gap" has done real work on this map, but it has been used six times now, and a
seventh on the rule we most recently tightened is how a rule becomes decoration.

**If you're not sure:** this question disappears entirely if Q1 is A or C. Answer Q1 first.

---

## Q3: If it ships, what stops the two formats drifting apart? `[medium]`

### The scene

March. Someone tightens a rule in the prompt because a review flagged something it should not have.
The writing path picks the change up, because that path is generated from one source by a script
and the script refuses to build when anything disagrees. The HTML instructions sit in a folder that
no script reads. In April a student pastes them and gets a page asking her to supply a confidence
label that was deleted in September.

That is not a prediction. It has happened twice already this year, to the two hand-maintained copies
we had, and both times nobody noticed until somebody went looking for something else.

### What each option does

- **A — The HTML file joins the generator and the drift check.** The command that already exists
  (`build-bundle.js --check`) is extended to cover it, so a change to the prompt that the HTML
  instructions do not reflect fails the build instead of reaching a student. This is real work and
  it is the only thing that has ever stopped this happening.
- **B — It stays an experiment, clearly labelled, and nobody is handed it.** Drift is then harmless,
  because a stale experiment is a stale experiment.

### Where the cost actually lands

Under **A**, on whoever does the build, and on every future prompt change, which now has to be made
in two places or the build stops. That is the point of it and it is also a permanent tax.

Under **B**, on nobody — but B is only available if Q1 is A or C.

### What we know, and how well

- The HTML file is not one of the three sources the generator reads, and neither script mentions it
  anywhere. It is in exactly the state the two files that went stale were in.
- It is already behind: the September build put six things into the writing path and none into it.
  So this is not "keep them level" — it is "catch up, then keep level".

### The decision

**I'd pick A** if the answer to Q1 is B, and note that there is no third answer. "We will maintain
both" without the check is not a plan — it is the exact sentence that was true both times a file
went stale.

**The best case against me:** putting the HTML into the generator means every future prompt edit
costs more, forever, to protect a format that may turn out to be the one nobody uses. If the pilot
shows students only ever want the writing, we will have bought a tax on the path that matters to
insure the path that does not.

**If you're not sure:** this only matters under Q1 = B.

---

**If you answer only one: answer Q1.** Q2 and Q3 exist only if Q1 is "leads can ask for it". If Q1
is "look at it once" or "retire it", both of them go away and the follow-on build is cancelled or
deferred with it.
