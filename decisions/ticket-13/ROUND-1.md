# Ticket 13, round 1 — findings, then the questions

Claimed 2026-09-20. Question as amended: **does the artifact path get reached at all, and how.**
Not "which path wins" — prose ships and is the de facto default (ticket 15). *Retire it* is on the
table as a real option.

## What I checked

- Ticket 13 in full: original body, the ticket 05 input, the ticket 15 input, the park note and the
  unpark note. Four amendments; the live question is the unpark note's, not the title's.
- Ticket 27's gap table.
- `22-trust-boundary.md` section 2, stop condition 3.
- `PASTE-2C-artifact-path.md` (272 lines), `build-bundle.js`, `check-docs.js`.
- The two rendered HTML pages from ticket 04 in `proto-04-free-tier-ceiling/render/`.

## Five findings that price the yes

**1. The HTML page already exists and he can see one this week for nearly nothing.**
Ticket 04 produced two complete rendered pages, one per model family. They are on disk. But they
were rendered from the **pre-retirement** 2C: `claude-full.html:97,99,184,186` carry `aiLevel`
("Nearly ready with minor edits") and a Confidence pill — the two features retired on 2026-09-20.
So the artifact he would be looking at today is a demonstration of two deleted features. Re-running
one deck through the *current* 2C and rendering it is one session and commits nothing.

**2. The guard is the cost, and the guard type this project has measured to work is unavailable
here.** Ticket 21 measured it in plain terms: *a check that reports a defect gets ignored (5 of 5),
a check that withholds the product holds (16 of 16).* The shipped interlock works because the
student cannot get the review without reading the key line first. The artifact path cannot withhold
anything — the page arrives whole, in one message, and the reader opens it. Every guard available
on this path is the reporting kind. `check-review-v2.js`, which stop condition 3 names as the
enforcement, is not in the chat loop at all: nobody runs a script on a pasted page.

**3. 2C's design is better than "HTML the model writes freehand", and that is worth being precise
about.** 2C says: *do not design a page, fill in the data object and paste the template underneath,
unchanged.* The level cannot arrive through a field — there is no field — so it would have to
arrive by the model editing the template or inventing a pill. Narrower than freehand, still
unguarded, and still nothing watching.

**4. 2C is outside the generator and outside every check.** `build-bundle.js`'s sources are exactly
three: section A of `04-prompt-templates.md`, `CHAT-CONTEXT.md`, section B. Neither
`build-bundle.js` nor `check-docs.js` mentions 2C anywhere. So the artifact path is in exactly the
state the two prior derivatives were in when they went stale undetected. `--check` is the mechanism
that exists and 2C is not in it.

**5. The gap is not six features of transcription plus one hard item — it is one hard item plus a
worse-than-absent condition.** Ticket 27 records it: the gate lives in pastes 1 and 3, which the
artifact path also uses, so the student *does* meet the gate, but 2C has no line-2 slot for the
marker and no line-1 slot for the keys. The detectors run and their output has nowhere to land.
A check that appears to run is worse than one that is absent.

## Round 1 questions — see QUESTIONS.md
