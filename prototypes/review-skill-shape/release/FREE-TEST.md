# Free test: lead review skill 1026-cb4758f

One new deliverable, one Claude.ai Free account, about 20 minutes. This run settles #20 (does the
review work on Free) and #21 (does the deck walk work on Free). Private: the deck and everything
it produces stay in `free-run/`, which git ignores.

## Before you start

- [ ] Export the deliverable to **PDF** (that is what the rooms get). Put the PDF in `free-run/` here.
- [ ] claude.ai → Settings → Capabilities: **code execution and file creation** are on.
- [ ] Settings → Capabilities → Skills: **turn off every older review skill** (the test-20, test-23
      and student zips), so only one review skill can trigger.
- [ ] Upload **`180dc-review-lead.zip`** from this folder.
- [ ] Note how full your usage bar is (Settings → Usage), so you can see what the run costs.

## The run (one new chat)

1. Attach the PDF and type exactly:
   `Can you review this deck before it goes to the client?`
2. Read the reply as a lead would, on your phone if you can. Don't type anything yet. Fill in
   **A** below.
3. Type exactly:
   `Paste exactly what the scripts printed, and list every quote or finding you changed or dropped because the quote check failed.`
   Fill in **B**.
4. Type exactly: `deck walk`
5. Download the file it gives you, save it to `free-run/deck-walk.html`, open it in a browser,
   press **Fix mode** and click through every slide. Fill in **C**.
6. Check the usage bar again. Fill in **D**.

## A. The review (any "no" in bold stops the release)

- [ ] **The skill triggered**: the footer reads `180dc-review-lead · 1026-cb4758f`.
- [ ] **The first line is the quote-check line** (`Quotes checked by script: N of N ...`), not
      "Quotes not machine-checked".
- [ ] **The main issue comes next**, in two lines, and it is true of the deck.
- [ ] **Every quote you spot-check is really on the slide it cites** (check at least three, one per
      finding if you can).
- [ ] **No grade, score, readiness level or verdict on the deck.**
- [ ] **No sentence the team could paste into the deck**: next steps name a move, not wording.
- [ ] **At most 5 findings, and roughly one long phone screen.** (If it looks long, paste it into a
      word counter: over 800 words stops the release.)
- [ ] Each `Framework:` line names one principle and gives a reason that points at this deck (a
      slide, a figure, a claim). No principle appears twice; Minor findings have none.
- [ ] Would you send this to the team as it is? Yes / no, and why.

## B. What the scripts printed

- [ ] The extract line says how many slides it read, and the count matches the PDF.
- [ ] **Nothing correct was dropped or changed** to get past the quote check.
- [ ] Copy what it printed into `free-run/notes.md`. That shows which PDF reader Free has.

## C. The deck walk (a failure here cuts the deck walk from version one, not the review)

- [ ] A file came back to download. (No file means Free doesn't hand files back the way the skill
      says.)
- [ ] The chat reply is two lines, with no JSON or page code pasted in.
- [ ] Slides show as **pictures**, not text. (Text means Free has no PDF renderer.)
- [ ] The page's main issue, findings and quotes are the same as the chat review.
- [ ] In Fix mode, each box sits on the quoted words, one box per quote. Note any slide where it doesn't.
- [ ] Red solid boxes ("change these words") look different from dashed evidence boxes.
- [ ] Where a finding is about something missing, the slide shows "Add supporting analysis here".
- [ ] "More on this step" opens the longer next step.

## D. Cost

- [ ] Usage before and after the review, and after the deck walk (rough fractions of the bar are
      enough).

## When you're done

Tell Claude the run is in `free-run/`. It checks the page against the review locally, then posts
patterns only (no client content) to #20 and #21 and closes them if they pass.
