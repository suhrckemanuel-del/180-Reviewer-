# Ticket 13 — resolution, 2026-09-20

**The artifact path is reached, and it stops being an output path.** It becomes a re-print of the
review the prose path already produced. Retire was live and was not taken; so was "second reviewer,
prettier", which is what the file currently is, and that one is rejected.

Three owner answers, over three rounds.

## 1. What the page is

**An optional extra, for both audiences, reached by pasting one more thing after the review has
already arrived.** The owner, round 1: *"something you get once you put in the prompt, the deck
context, the methodology, and it outputs it. Just visually nice way for team leads and students to
learn. This experience should effectively be the same if you're using the chat, but the other one is
just visually nice."*

That settles three of the ticket's four questions at once:

- **Question 1** (default, and how the other is reached): prose stays the default — it is what the
  pilot ships and nothing here delays it. The page is reached by an extra paste, after the review.
- **Question 3** (different defaults for leads and students): **no.** Same page, both audiences.
  The learning purpose is named for both.
- **Question 4** (fallback when a model cannot render it): **answered by construction.** The review
  already exists in the chat above the page. A failed render costs the reader nothing they did not
  already have. This was a real question under the old design, where the page *was* the output, and
  it stops being one here.

## 2. The page re-prints the review; it does not produce one

Round 3, question put as *where do the words on the page come from* — **A, the re-print**: same
findings, same quotes, same words, laid out, and the reader can scroll up and check.

**This contradicts the file as it stands and the rewrite is the substance of ticket 27.**
`PASTE-2C-artifact-path.md:3` opens *"It replaces the JSON output that prompt asks for"*, and the
file then restates every content rule for itself — at most three findings, one main issue, what a
fix may say, how quotes work. It is a second reviewer. Under this decision it becomes a layout plus
an instruction to draw a review that already exists, and it carries **no content rules of its own**.

What that buys, and it is most of the ticket's value:

- **The six-feature gap mostly closes for free.** The attempt marker on line 2 and the bundle key on
  line 1 are already in the review being re-printed. They do not have to be re-implemented on this
  path; they have to be *carried through*. Ticket 27 items 2 and 5 shrink from build to transcribe.
- **A lead who gets two different reviews is no longer possible by design.** Under the old design
  she had two, on one screen, with no way to know which to believe, and she was the only person who
  would ever see both.

## 3. The verdict row is deleted

Round 2: *"delete, we don't need verdict, we already just have list of errors."*

- The box row comes off the page. No grade box, no confidence box, and **no "Your call — Not set"
  box** — the lead's own verdict slot goes with it. That was the named cost of this option and it is
  accepted.
- The instructions stop calling anything **"the verdict pills"** (`PASTE-2C-artifact-path.md:15`).
  That phrase is the label on the hole.
- **This is what answers stop condition 3 on this path, and it answers it by construction rather
  than by guard.** The prose path produces no level because the instruction asking for one was
  deleted; the page now has no slot shaped like one. The guard that ticket 27 called *the item with
  no precedent* — a no-level check that works without a renderer — **shrinks to an absence check**:
  does the emitted page contain the box row. That is a string comparison, not a new instrument.

**It does not shrink to zero, and the answer must not be read as saying it does.** The model can
still write a grade into a heading or a sentence. Deleting the row removes the shape most likely to
invite one; it does not remove the possibility. Ticket 27 keeps item 6, at much lower cost and with
a defined test.

## 4. Question 2 — maintained, and what stops the drift

The owner said drift *"is not really important"* (round 1, Q3). **The ticket still has to answer it,
because "maintained" is the answer to question 2 and the failure mode is on record twice.** So it is
answered here as spec rather than left as his call:

**The re-print decision is itself most of the drift defence.** Drift happened twice because a
hand-maintained file carried a copy of rules that lived somewhere else. Under this decision the page
carries **no content rules**, so there is no copy to go stale — a prompt change lands in the prose
path, and the page re-prints whatever the prose path now produces.

**What is left to drift is the layout file itself**, and the mechanism that exists is
`build-bundle.js --check`. Today `PASTE-2C-artifact-path.md` is **not** one of the generator's three
sources (section A of `04-prompt-templates.md`, `CHAT-CONTEXT.md`, section B), and neither
`build-bundle.js` nor `check-docs.js` mentions it anywhere — the exact state the two stale
derivatives were in. **Ticket 27 item 7 stands unchanged and is not optional**, and its scope is now
smaller and more checkable: the page joins the generator, and `--check` asserts that the re-print
instruction still names the fields the prose output actually emits.

Recorded plainly: this is a session's judgement on a question the owner declined to weigh, filed as
a build requirement on ticket 27 rather than as a decision he made.

## 5. What ticket 27 becomes

Not resolved and not started here. Appended to 27 as an input. In summary: item 1 unchanged and
still blocked on ticket 26; items 2 and 5 shrink to carrying fields through a re-print; item 3
(the count line) unchanged; item 4 unchanged; **item 6 shrinks from an unbuilt instrument to an
absence check**; item 7 unchanged and mandatory. Plus one item 27 does not have: **the rewrite of
2C from a second reviewer into a re-print**, which is the largest single piece of work and the
thing the other items now depend on.

## Limits on this answer, stated

- **The re-print has never been run.** Zero measurements. Both rendered pages on file
  (`proto-04-free-tier-ceiling/render/`) are the *second-reviewer* design on a *pre-retirement*
  template, showing an `aiLevel` pill and a confidence label. **Ticket 04's "both model families
  rendered it first try" does not transfer to this decision** — it measured the design being
  replaced. Carrying that number across would be this map's standing caution in its own words.
- **A new failure mode appears that the old design did not have: the model rewriting the review
  while presenting it as a re-print.** Nothing checks that today. It is the thing ticket 27 must
  test first, and it is the best case against this decision, made at the time.
- **2C has still never been read against the current paste 1.** Unchanged from the ticket's own
  note, and the rewrite does not remove the need — it makes it the first step of the rewrite.
