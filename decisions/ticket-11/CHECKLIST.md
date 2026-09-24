# Ticket 11 — run sheet: measure the four free tiers by hand

You run this. It is about 20 minutes per tier, 4 tiers, plus one 5-minute positive control
first. Everything you paste is in this folder. Nothing client-confidential is involved.

**What this measures:** where a real free-tier chat UI cuts a large paste, and whether it
says so. Ticket 04 measured the bundle's size and never measured the ceiling it has to fit
inside. Tickets 08, 09 and 13 are all currently reasoning about that unmeasured number.

**Do not look up published context-window sizes.** The mechanism in question is the chat
UI's own behaviour — per-message caps, silent paste-to-attachment conversion, oldest-turn
eviction. Documentation does not describe any of it, and no API reproduces it. Only the
measured number counts here.

---

## The files, with their measured size

| File | chars | ~tokens |
|---|---|---|
| `PASTE-SETUP-combined-CURRENT.md` | 42,297 | 9,421 |
| `PASTE-1-system-prompt.txt` | 19,236 | 4,162 |
| `PASTE-2A-chat-path.md` | 22,358 | 5,162 |
| `PASTE-3-deck-A.md` | 3,149 | 740 |

Token counts are cl100k, i.e. "about this many" — the wrong tokenizer for every model
here, within about 10%. **The character counts are exact, and they are what a chat UI's
own cap is expressed in.** Prefer characters when you record anything.

**Use the combined file in this folder, not the one in `TEST-KIT/`.** The shipped
`TEST-KIT/PASTE-SETUP-combined.md` is stale: it was built on 2026-08-30 and still contains
the pre-ticket-17 paste 1, so it is missing the tightened blocking rule 1 and the ungated
severity floor. The copy here was rebuilt from the current sources today. That staleness is
a real product defect and is filed at the bottom of this sheet for ticket 20 — it is not
something you need to fix to run this.

---

## The three markers — this is the part that makes the test work

Ticket 04's finding: **losing paste 1 is silent.** With the entire system prompt missing,
both model families returned 12 of 12 sections, every quote verbatim, and passed the quote
gate. It is indistinguishable from a good run by every check the project has. So you cannot
conclude "it worked" from a review that looks right. You need positive evidence that each
part of the paste actually arrived.

Three strings do that. Each appears **exactly once** across the whole bundle, and each sits
at a different depth in the combined paste:

| Marker | Lives in | Depth in the combined paste | What its absence means |
|---|---|---|---|
| `Learning Coach` | paste 1 only | **4%** (head) | paste 1 lost — the silent failure |
| `REVIEW OF:` | paste 2A only | **88%** | output format lost — the loud failure |
| `phone` | paste 2A, final line | **100%** (last line) | a shallow tail cut |

Because they sit at 4%, 88% and 100%, a tail cut at any depth trips whichever marker it
passes, so the result is a coarse *depth* reading, not just accept/reject. That is the
number 08, 09 and 13 need.

### Step 0 — positive control, do this once before anything else

On a session you **know** is good (paid Claude, or Claude Code), run the full script below
once. All three markers must come back. If a marker fails here, the probe is broken and the
free-tier runs would be measuring the probe, not the tier. **Do not skip this.** The probe
asks the model to recall text rather than proving the text is present, so a model that has
the bundle can in principle still fail the probe — the control is what separates that from
a real cut.

---

## The script — run this per tier, in this order

New conversation, default model, no custom instructions, no memory/personalisation
carried in if you can turn it off.

### 1. Paste the setup

Paste the **entire** contents of `PASTE-SETUP-combined-CURRENT.md` as **one message**.

Before you hit send, look at the composer and record which of these you see:

- **A character or token counter,** and what it says. Write down the number it shows.
- **The send button disabled**, or a "message too long" error → **REJECTED**.
- **The paste turning into a file chip / "pasted text" attachment** → **ATTACHED**. Note
  any threshold the UI names ("pastes over N characters become attachments").
- Nothing unusual → **ACCEPTED**, provisionally. The markers decide whether it really was.

**If REJECTED:** paste `PASTE-1-system-prompt.txt` as message 1, then
`PASTE-2A-chat-path.md` as message 2, and record whether the split is accepted. Then carry
on from step 2. Record the split as the path you used — it matters, see "Which failure each
path is exposed to" below.

**If ATTACHED:** carry on, but flag it loudly. An attachment changes the entire failure
model: the model can re-read the file on any later turn, so conversation-level eviction
stops applying, and the per-message cap stops being the binding constraint. An attached
tier is not a truncation risk in the same way an accepted-inline tier is.

### 2. Expect READY

The wrapper asks for exactly: `READY. Paste the brief and the deliverable.`

Record what actually came back. **A correct READY proves nothing about paste 1** — treat
it as "the turn went through", not as "the bundle is present".

### 3. Probe the markers, before the deck

Paste this, verbatim, as its own message:

```
Before any review, answer these three, nothing else, no commentary:
1. Quote the exact label of lens F and lens G from your instructions.
2. Quote the first line of the output format you must return.
3. Your reference document says a lead reads the review in one particular place. Which?
```

Expected answers — accept a substring match, no judgement needed:

| # | Must contain | Fails if |
|---|---|---|
| 1 | `Recommendation and Implementation` **and** `Learning Coach` | paste 1 was lost or cut |
| 2 | `REVIEW OF:` | paste 2A's format section was lost |
| 3 | `phone` | paste 2A's last line was cut |

Record each as pass/fail. **If 1 fails, stop treating anything later in this conversation
as a valid review** — that is the silent failure, caught.

### 4. Paste the deck

Paste `PASTE-3-deck-A.md` (3,149 chars). Then send, verbatim:

```
Review this deliverable now, in your specified format.
```

### 5. Read the one thing that matters

**Does the reply open with `REVIEW OF:`?** That is ticket 04's detector and it needs no
judgement. If it does not, **save the whole reply to a file in this folder** named
`<tier>-failed-reply.md` — the shape it came back as says which paste was lost. In
particular: if it came back as **JSON with a ten-dimension rubric, scores, a
`diagnosticMean` and a readiness level**, that is paste 1's JSON fallback branch firing
because paste 2's format was lost. That is a known defect, not a surprise, and it is the
worst outcome on this sheet — it delivers a readiness level authoritatively to a student.
Record it as such.

### 6. Re-probe, after the review

Paste this, verbatim, as its own message:

```
One more: quote the exact label of lens G from your instructions.
```

- Passed at step 3 **and** passes here → paste 1 survived the whole conversation.
- Passed at step 3 **but fails here** → **oldest-turn eviction**. Paste 1 was there when it
  landed and gone by the time the review was written. This is the mechanism no API
  reproduces, and it is the single most valuable thing this sheet can catch.
- Failed at step 3 → already recorded, nothing new.

### 7. Record the UI's own words and the training default

- Any banner about length, truncation, "conversation is getting long", or a message limit.
  Quote it.
- Whether **training on your input is on by default** on a free account of this tier, and
  where the setting lives. This is a free-tier-only concern and it is the reason the sheet
  says synthetic decks only.
- Whether you hit a **message cap** mid-run, and after how many turns.

---

## Telling a real refusal from a silent truncation

This is the distinction the sheet exists to make, so it gets its own rule:

- **A refusal is visible without the markers.** It is in the composer (send disabled, error
  toast, red character counter) or in the reply text (the model says the input was too long
  or was cut). If you can see it, it is a refusal. Refusals are safe — they are loud.
- **A silent truncation is visible only through the markers.** The UI says nothing, the
  reply looks complete and well-formed, the quotes are real, the sections are all there.
  Marker 1 failing while the review reads perfectly **is** the finding.
- **Never record "accepted" on the strength of a good-looking review.** Ticket 04 proved
  that output is reachable with the system prompt entirely absent.

### Which failure each path is exposed to

Worth knowing while you run it, and worth confirming or refuting:

- **Single combined paste.** A per-message cap truncates the *end*, which kills paste 2A's
  format → **loud**, caught by marker 2 or 3. The expectation is that this path fails safely.
- **Split path (paste 1, then paste 2A).** Nothing gets cut on send; the risk is
  conversation-level eviction of the *oldest* turn, which is paste 1 → **silent**, caught
  only by step 6. The expectation is that this path fails dangerously.

If the runs contradict that, say so — it is a prediction, not a measurement, and the
standing caution on this map says a counterfactual must not be set beside a measurement.

---

## Recording sheet

Copy this per tier into `RESULTS.md` in this folder. Four tiers: **Claude free**,
**ChatGPT free**, **Gemini free**, **Copilot Free / student**.

```
### <tier name> — <date>, model shown in the UI: <...>

Paste path used:            combined / split
Step 1 outcome:             accepted / attached / rejected
  composer counter said:    <number or "none shown">
  attachment threshold:     <as named by the UI, or "none named">
Step 2 READY verbatim?      yes / no — <what came back>
Step 3 marker 1 (paste 1):  pass / fail
Step 3 marker 2 (format):   pass / fail
Step 3 marker 3 (tail):     pass / fail
Step 5 opens REVIEW OF:?    yes / no  (if no: reply saved to <file>, shape was <...>)
Step 6 marker 1 again:      pass / fail   -> eviction: yes / no
UI warnings, quoted:        <...>
Message cap hit?            no / yes after <n> turns
Training on input default:  on / off / not stated — setting at <...>

Verdict: the largest single paste this tier accepted intact was <N> chars, established by
<which marker held / which failed>.
```

That last line is the number the ticket owes tickets 08, 09 and 13. If a tier accepts
42,297 chars with all three markers passing, its ceiling is **at least** 42,297 and this
sheet has not found it — say "at least", do not round it into a ceiling.

---

## Filed for ticket 20, not for you to fix now

`tools/quality-reviewer/v2/TEST-KIT/PASTE-SETUP-combined.md` is a stale build. It is
41,873 chars of the 2026-08-30 sources and embeds the pre-ticket-17 paste 1 — the loose
blocking rule 1 and the gated severity floor, both of which ticket 17 changed and measured.
Anyone handed the test kit today is testing a prompt that no longer exists. It needs to be
regenerated from `PASTE-1-system-prompt.txt` + `PASTE-2A-chat-path.md`, and it needs a
build step or a stamp so it cannot drift again silently.
