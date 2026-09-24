# Decide the default output path, HTML or prose

Type: grilling
Status: closed
Blocked by: -

## Question

Charting settled that HTML rendering is "wanted but must stay optional". Ticket 04 removed the
technical doubt: **both output paths work on free-tier-class models.** gpt-5.6-sol and Haiku 4.5
each emitted the full two-mode HTML page first try, complete, rendering correctly with the
student-mode attempt gate intact. The prose path works too. Neither is blocked by capability, so
the choice is now about what a student should be handed by default.

What makes this a real decision rather than a preference:

- **The HTML path requires a readiness level today.** `PASTE-2C` makes `aiLevel` mandatory and
  renders it as an "AI guess" pill in lead mode. The two models disagreed on identical input.
  Blocked by ticket 05, because if retirement lands, 2C has to be rewritten or dropped — and a
  2C without `aiLevel` is an untested artifact.
- **The two paths disagree about the product.** 2A argues at length that the unreliable half
  should not be produced at all; 2C produces it. Whichever becomes the default is also a
  statement about which argument won.
- **Cost differs slightly** (paste 2C is 5,663 tokens against 2A's 5,162), and ticket 11 says
  whether either fits.

Settle:

1. Which path a student is handed by default, and how the other is reached.
2. Whether both are maintained, or one is retired. Two output contracts that drift is the
   failure mode already seen once in this project.
3. Whether leads and students get different defaults — lead mode is where the readiness pill
   lives, and leads are the population that could be trusted with it if anyone could.
4. What the fallback is when a model cannot render the artifact at all.

Answer records: the default, the opt-out, and what happens to the path that loses.

---

**Input from [ticket 05](05-retire-the-readiness-level-everywhere-it-appears.md) (closed 2026-09-19). This ticket is unblocked on the 05 side.**

Retirement landed, and it reaches further into the artifact path than this ticket's question
assumed. `aiLevel` is deleted from `PASTE-2C-artifact-path.md` — the mandatory field (:42), the
derivation rule (:96) and the "AI guess" pill (:216).

**The finding this ticket needs to act on:** the artifact path has **no outbound scan, no payload
redaction and no stop panel**. The renderer's guards at `index.html:1100-1168` protect the
renderer only. The same 2C template that requires `aiLevel` also renders student mode. Under the
widened stop condition 3 — *the tool produces a readiness level, for anyone* — **the artifact path
does not ship until it carries the same check.** That is a precondition of choosing it as the
default, not a follow-up.

A 2C without `aiLevel` is an untested artifact, as this ticket already says. It is now also an
artifact that needs a guard it has never had.

---

**Input from [ticket 15](15-decide-whether-to-keep-or-roll-back-frozen-2026-08-09.md) (closed 2026-09-20). Question 1 is partly pre-empted by facts on the ground, and this ticket should know it.**

**The prose path is the de facto default and has been since the chat-native build.** Ticket 15 established that the shipped pilot package is the three-paste chat path — paste 1 is section A of `04-prompt-templates.md`, paste 2 is `CHAT-CONTEXT.md`, paste 3 is the input template — and that it is what the pilot ships on `frozen-2026-09-19`. This ticket's question 1 is therefore no longer "which becomes the default" but **"does the artifact path get reached at all, and how"**. That is a smaller and more answerable question.

Two facts it inherits:

- **The artifact path is now two prompt versions stale and nobody has checked it.** Ticket 15 found paste 2 of the *prose* path still demanding a confidence label paste 1 has deleted, and still stamping records `frozen-2026-08-09`. `PASTE-2C-artifact-path.md` has had no more attention than paste 2 did and has had less. Before choosing it as a default or an opt-out, someone has to read it against the current paste 1, not against the version it was written for.
- **`check-docs.js` has no check that the paste files agree with each other.** Two independent drift instances surfaced on 2026-09-20 — paste 2, and the stale `PASTE-SETUP-combined.md` found by ticket 11. A third output path is a third thing to drift. That is an argument for question 2's "retire one" option that this ticket did not have when it was written.

**And a new dependency: [ticket 22](22-decide-the-findings-based-severity-score.md).** The owner reopened readiness on 2026-09-20 as a score computed from the findings. If a score ships, it has to render somewhere, and the artifact path is the only surface with a place to put one. Ticket 22's question 3 asks who sees it; this ticket answers where. Neither blocks the other, but they must not be resolved in ignorance of each other.


---

**Parked 2026-09-20 by the owner, on the scope audit ([AUDIT-2026-09-20.md](../AUDIT-2026-09-20.md)).** Not cancelled and not out of scope: deferred until the pilot has run, at which point it is reconsidered against what the pilot actually showed.

Reason: prose is the de facto default and ships today; the HTML question is not pilot-blocking


---

**UNPARKED 2026-09-20 by the owner**, who asked to see the HTML output and to run the tickets that
finish it. It was parked the same day on the scope audit, on the grounds that prose is the de facto
default and HTML is not pilot-blocking. Both of those remain true; the owner wants it anyway, which
is a scoping call and his to make.

**The blocker on ticket 11 is released.** It was there because 11 would say whether either path
fits a free-tier window. Two things retire that dependency: ticket 04 already showed both paths
render first try on free-tier-class models, and the owner deferred the free tier entirely on
2026-09-20 (*"once the product is finished for paid users, we can definitely work on the free
one"*). Size is not what this ticket turns on any more.

**The question is smaller than it was, and smaller is the point.** Ticket 15 established prose as
the shipped default, so this is no longer "which path wins". It is **"is the artifact path reached
at all, and how"**, and the cheapest honest answers include *retire it*.

**Answer this before [ticket 27](27-bring-the-artifact-path-level-with-the-prose-path.md), because
it can cancel it.** 27 is the build that brings the artifact path level with the prose path, and it
is a substantial build: six features absent, plus a no-level guard that has to work without a
renderer, which nothing in this project has built. If the answer here is "retired, or reached only
by a lead who asks for it", most of that work does not happen.

**One thing this ticket now inherits that it did not have when parked:** the gap it is deciding
about got wider on 2026-09-20. Ticket 20 shipped six things into the prose path and none into the
artifact path. Whatever is decided here, **two output paths that drift is the failure mode this
project has already seen twice**, and the second path now starts from six features behind.

---

## Answer, 2026-09-20

**The artifact path is reached, and it stops being an output path.** It becomes a **re-print of the
review the prose path already produced** — an optional extra, both audiences, reached by pasting one
more thing after the review has arrived. Prose stays the default. *Retire* was live and was not
taken; so was "second reviewer, prettier", which is what the file currently is, and **that one is
rejected**.

Three owner answers over three rounds, full working in
[ticket-13/ANSWER.md](../ticket-13/ANSWER.md), rounds in
[QUESTIONS.md](../ticket-13/QUESTIONS.md) and
[QUESTIONS-ROUND-2.md](../ticket-13/QUESTIONS-ROUND-2.md).

- **Questions 1, 3 and 4 fall out of the first answer.** Prose is the default and the page is an
  extra paste after it; **no**, leads and students get the same page, the learning purpose is named
  for both; and the render-failure fallback is **answered by construction** — the review is already
  in the chat above the page, so a failed render costs the reader nothing they did not have. That
  was a real question when the page *was* the output; it stops being one here.
- **The re-print decision contradicts the file.** `PASTE-2C-artifact-path.md:3` opens *"It replaces
  the JSON output that prompt asks for"* and then restates every content rule for itself. Under this
  decision it carries **no content rules at all**. That rewrite is the largest piece of work in
  ticket 27 and ticket 27 did not have it.
- **The six-feature gap mostly closes for free.** The attempt marker and the bundle key are already
  in the review being re-printed; they are carried through, not re-implemented.
- **The verdict row is deleted** — the owner's *"we don't need verdict, we already just have list of
  errors"*. No grade box, no confidence box, and **no "Your call — Not set" box**: the lead's own
  verdict slot goes with it, which was the named cost and is accepted. The instructions stop calling
  anything *"the verdict pills"* (:15).
- **That is what answers stop condition 3 here, and it answers it by construction rather than by
  guard.** Ticket 27's *item with no precedent* — a no-level check that works without a renderer —
  **shrinks to an absence check on the box row**, a string comparison rather than a new instrument.
  **It does not shrink to zero:** the model can still write a grade into a heading or a sentence.
  The slot is gone, not the possibility.
- **Question 2 is "maintained", and the drift answer is filed as spec, not as his call** — he said
  drift *"is not really important"*. The re-print is itself most of the defence: drift happened
  twice because a hand-maintained file held a copy of rules living elsewhere, and the page now holds
  none. What is left to drift is the layout file, and **`build-bundle.js --check` is the mechanism
  that exists**: 2C is not one of its three sources and neither it nor `check-docs.js` mentions 2C
  anywhere — the exact state the two stale derivatives were in. **Ticket 27 item 7 stands and is not
  optional.**

**Limits.** The re-print has **never been run — zero measurements**. Both pages on file are the
second-reviewer design on a pre-retirement template, so **ticket 04's "both families rendered it
first try" does not transfer to this decision**; carrying it across would be this map's standing
caution in its own words. And the design introduces a failure the old one did not have — **the model
rewriting the review while presenting it as a re-print** — which nothing checks today, is the best
case against this decision, and is the first thing ticket 27 must test. 2C is still unread against
the current paste 1.

**Ticket 27 is not resolved and not started.** Its rewritten scope is appended to it as an input.

