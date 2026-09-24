# Test kit: run the reviewer yourself, on a free account

Everything you need is in this folder. Nothing here needs Claude Code, a paid account, an
API key or this repository. You could email this folder to someone and they could run it.

**Three decks, none of them reviewed in front of you.** They are synthetic and anonymised, so
nothing here is client-confidential and you can paste them into any service. Each one is built
around a different failure, and one of them is a genuinely good deck. **You are not told which
is which.** The answers are sealed in `answers/`.

---

## Before you start: the one rule that makes this worth doing

**Write down your own top three issues for a deck BEFORE you read the review of it.**

There is a box for this in `FEEDBACK.md`. Do it first, in two minutes, as the team lead you
would be. If you read the review first you will find yourself agreeing with it, and the test
will tell you nothing. This is the same discipline the project applies to itself: state the
answer before you see the result, or the result cannot surprise you.

---

## Route 1: the chat path (this is the product)

What a consultant with no budget and no paid account does.

**Fastest version, two pastes:**

1. **Paste `PASTE-SETUP-combined.md`** (42k characters). It ends by telling the model to reply
   `READY. Paste the brief and the deliverable.` and to review nothing yet. Wait for that.
2. **Paste one of `PASTE-3-deck-A.md` / `-B` / `-C`** — the brief and the deck.

**If that gets rejected as too long**, some free tiers cap a single message. Split it:

1. **Paste `PASTE-1-system-prompt.txt`** (19k) — the reviewer's instructions.
2. **Paste `PASTE-2A-chat-path.md`** (22k) — the calibration context and the output format.
3. **Paste a deck.**

You get a readable review back. No JSON, no renderer, no grade.

> If the service lets you, put pastes 1 and 2 in a Project, a Custom GPT or a system prompt, and
> then each deck is a single message. Not required.

**Turn off model training first.** Most consumer free tiers train on what you paste unless you
say otherwise. These decks are synthetic so it does not matter here, but build the habit before
you ever do this with real client work.

## Route 2: the visual path (same reviewer, adds the desk)

Same idea, but you get the full Triage Desk instead of prose. Also free.

1. **Paste `PASTE-1-system-prompt.txt`**
2. **Paste `PASTE-2B-json-contract.md`** — the output contract, instead of the chat format
3. **Paste a deck** — same files as above
4. You get JSON. Copy all of it.
5. Open **https://180dc-reviewer.pages.dev** and paste it into "OR BRING YOUR OWN"

That is the same desk a Claude Code user sees: quote gate, blocking issues, triage cards,
rubric, the note that writes itself. It runs entirely in your browser.

**Known issue you will hit if you skip paste 2B:** the system prompt tells the model to match
"the v2 output contract" but does not contain it. Without `PASTE-2B` the JSON comes back in an
invented shape and the renderer refuses to draw it. That is a real packaging defect, not you
doing it wrong.

---

## Route 3: the two-mode page (test this one first)

The same reviewer, but the output is an interactive page instead of prose. **Artifacts work on a
free Claude account**, so this needs no paid plan.

1. **Paste `PASTE-1-system-prompt.txt`** &mdash; the reviewer's instructions.
2. **Paste `PASTE-2C-artifact-path.md`** &mdash; the two-mode output format and its template.
3. **Paste a deck** &mdash; `PASTE-3-deck-A.md`, `-B` or `-C`.

You should get a page with two tabs:

- **Lead mode.** Verdict pills, where the deck is weakest, a per-slide timeline with callouts,
  dashed arcs joining slides that contradict each other, one main issue, and the fixes.
- **Student mode.** Three findings. Each names the principle, quotes the deck as proof, and asks
  a question. **The suggested fix stays locked until the student types their own answer**, then
  shows both side by side.

### What to check on this route

- [ ] Both tabs render and switch
- [ ] The timeline has one tile per slide, and the coloured ones match the findings
- [ ] The arcs, if any, join two slides that genuinely contradict each other
- [ ] Student mode has **three findings or fewer**
- [ ] The fix button is disabled until you type, and your answer appears next to the suggestion
- [ ] No suggested fix is text you could paste straight onto a slide

The likely failure is the model rewriting the template instead of just filling in the `REVIEW`
object. If the page looks different from the description above, say so &mdash; that tells us the
instruction is not strong enough, which is worth more than a clean run.

---

## Testing it on a real PowerPoint

The three decks above are text, because they have to be pasteable by anyone. Your own
deliverables are `.pptx`, and getting from one to the other is a real step the product has to
support. There is a tool for it:

```
python ../deck-to-paste.py "your deck.pptx" -o deck.md
```

It also reads `.pdf` and `.docx`. It writes the `DELIVERABLE TEXT` block, slide by slide, plus
an extraction-notes block. Then fill in the template fields at the top of any of the
`PASTE-3-deck-*.md` files, drop your block in below them, and paste that as your third paste.

**Tables and charts are the reason this exists.** A table copied by hand loses which column
each number was in, and a chart pasted as text usually loses its values completely. Those are
exactly the numbers the reviewer's comparator test asks "compared to what" about. The tool
keeps a table's header row and binds each value to its column, and it reads chart values out of
the chart data rather than the slide surface:

```
[Table] Tier | Members | Cost per member
  Tier: Standard; Members: 820; Cost per member: 14.20

[Chart]
  Membership income -- 2023: 31000.0; 2024: 34500.0; 2025: 29800.0
```

**Do not reword the extraction notes it writes.** The reviewer reads them to tell a figure whose
comparator is genuinely missing from one the extraction destroyed, and it decides that on the
exact wording. A slide reported as "no extractable text" gets its comparator test suspended; a
slide reported as "kept as extracted" does not.

**This path is the least tested thing in the kit.** It works on the decks tried so far, but real
decks are messier than any test file: text boxes in odd orders, images of tables, charts linked
to spreadsheets. If it produces something garbled, that output is worth more to me than a clean
run. Send it.

**Confidentiality:** anonymise before you paste, per the usual rule. The tool reads one file and
writes one file and stores nothing, but the service you paste into is not ours.

---

## Which route to test

Do **Route 1 on all three decks** first. That is the product and it is what most consultants
will use. If you have time, do Route 2 on one deck to see the desk.

Try to use a genuinely free tier for at least one deck. Every number this project has was
measured on Claude Opus, and nobody has ever checked what a free model does with this prompt.
That gap is the single largest unknown left, and you are the only one who can close it.

---

## Then

Fill in `FEEDBACK.md` and send it back. Open `answers/` only after you have written your own
verdict for a deck. `WHAT-TO-LOOK-FOR.md` is the checklist.

## Files

| file | what it is |
|---|---|
| `PASTE-1-system-prompt.txt` | the reviewer, paste first, both routes |
| `PASTE-2A-chat-path.md` | route 1 second paste: calibration plus the prose format |
| `PASTE-2B-json-contract.md` | route 2 second paste: the JSON contract |
| `PASTE-3-deck-A/B/C.md` | three briefs with their decks, paste one at a time |
| `WHAT-TO-LOOK-FOR.md` | the checklist, ten minutes per deck |
| `FEEDBACK.md` | fill this in and send it back |
| `answers/` | sealed. Open after you have written your own verdict |
