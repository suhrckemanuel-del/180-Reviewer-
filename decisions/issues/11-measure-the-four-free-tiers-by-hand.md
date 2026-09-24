# Measure the four free tiers by hand

Type: task
Status: claimed
Blocked by: —

## Question

Nothing to decide. This is the twenty minutes of manual work that closes the one gap ticket 04
could not: **where a real free tier actually cuts the paste, and whether it says so.**

Ticket 04 measured the bundle (9,227 tokens of instructions, ~13,300 for a typical whole review,
~24,000 worst case) and established what breaks at each cut depth on two model families. It could
not establish the ceiling, because no free account was driven and the research pass on published
window sizes died on a spend limit. Model proxies cannot substitute: a chat UI's own behaviour —
per-message caps, silent paste-to-attachment conversion, oldest-turn eviction — is the mechanism
in question, and no API or agent harness reproduces it.

**Needs a human with four free accounts.** AFK is not possible: creating accounts and signing in
is out of scope for the agent.

For each of **Claude free**, **ChatGPT free**, **Gemini free** and **Copilot Free / student**:

1. Paste `TEST-KIT/PASTE-SETUP-combined.md` (41,873 characters) as one message. Record which
   happened: **rejected** ("too long"), **converted to an attachment** (note any character
   threshold shown), or **accepted**.
2. If it was rejected, split into `PASTE-1-system-prompt.txt` then `PASTE-2A-chat-path.md` and
   record whether the split is accepted.
3. Paste `PASTE-3-deck-A.md`.
4. Record the single thing that matters: **does the reply open with `REVIEW OF:`?** That is
   ticket 04's detector and it needs no judgement. If it does not, save the reply — the shape it
   came back as says which paste was lost.
5. Note any warning the UI showed about length, truncation or conversation limits, and whether
   training-on-input is on by default.

Use the synthetic decks only. Nothing client-confidential goes into this.

Answer records: per tier — accepted / attached / rejected, the detector's verdict, the UI's own
warning if any, and the training default. Feeds tickets 08, 12 and 13.

---

## Prepared 2026-09-20 — run sheet handed over, awaiting the human's runs

Not resolved. A task ticket closes when the work is done, and the work is four free accounts
being driven by hand. What exists now is the sheet to drive them with:
[`ticket-11/CHECKLIST.md`](../ticket-11/CHECKLIST.md), with every file to paste beside it.

**Three changes to the ticket's own step list, all forced by ticket 04's silent-truncation
finding.**

1. **Step 1 pastes a different file than the ticket names.** The shipped
   `TEST-KIT/PASTE-SETUP-combined.md` (41,873 chars) is a **stale build** — 2026-08-30, embedding
   the pre-ticket-17 paste 1, so it carries the loose blocking rule 1 and the gated severity floor
   that ticket 17 replaced and measured. Rebuilt from current sources as
   `ticket-11/PASTE-SETUP-combined-CURRENT.md`, **42,297 chars / ~9,421 cl100k tokens**. That is
   also a fresh instructions figure against ticket 04's 9,227 — the ticket 17 patch cost ~194
   tokens. The staleness is appended to [ticket 20](20-apply-the-accumulated-edit-lists-to-the-product.md)
   as item 10, in Group B because it derives from paste 1.

2. **The ticket's step 4 detector is necessary and not sufficient, so the sheet adds a
   marker probe.** `does the reply open with REVIEW OF:?` only catches the *loud* failure. Ticket
   04 established that losing paste 1 returns 12/12 sections with verbatim quotes and passes the
   quote gate — so running the ticket as written would record "accepted" on a conversation whose
   system prompt was never there. Three strings fix that, each occurring **exactly once** in the
   bundle and each at a different depth of the combined paste: **`Learning Coach`** (paste 1 only,
   **4%**), **`REVIEW OF:`** (paste 2A only, **88%**), **`phone`** (paste 2A's last line, **100%**).
   Verified unique by count. Because the depths are spread, a tail cut trips whichever marker it
   passes, so each tier yields a coarse *depth* reading rather than accept/reject — which is the
   form tickets 08, 09 and 13 actually need.

3. **The probe runs twice, before the deck and after the review.** Pass-then-fail isolates
   **oldest-turn eviction** from an on-arrival cut. That is the one mechanism the ticket says no
   API or agent harness reproduces, and it is invisible to a single probe.

**Refusal versus silent truncation, the rule the sheet states:** a refusal is visible without the
markers (disabled send, error toast, or the model saying the input was cut); a silent truncation is
visible *only* through the markers. So "accepted" may never be recorded off a good-looking review.

**The honest weakness, and the control that covers it.** The probe measures *recall*, not
presence: a model holding the whole bundle could still fail it, which would read as a cut that
never happened. Step 0 is therefore a positive control on a known-good session, and it is marked
do-not-skip. If the control fails, the probe is what is being measured, not the tier.

**One prediction is recorded, explicitly as a prediction and not a measurement**, per the map's
standing caution: the single combined paste should fail **loudly** (a per-message cap truncates the
tail, killing the output format), and the split path should fail **silently** (nothing is cut on
send; the risk is eviction of the oldest turn, which is paste 1). The sheet asks for it to be
contradicted if the runs contradict it.

Still owed on resolution: per tier — accepted/attached/rejected, the three marker verdicts before
and after, the UI's own warning quoted, the training-on-input default, and the largest single paste
accepted intact, stated as "at least N chars" when no marker failed.

---

## Note from ticket 12 (2026-09-20) — what this sheet is now for

Ticket 12 landed, and it changes what one tier would buy. Recorded here rather than acted on: this
sheet is claimed by another session and its run is the owner's call.

**What changed.** The ticket 04 gap this sheet exists to close was *"losing paste 1 is silent"*.
Ticket 12 closed it in the bundle itself: a cross-paste key interlock makes a lost paste announce
itself and refuse, measured 34 runs across two model families, 0 invented keys. So the danger this
sheet was chasing is no longer undetectable in the field, which is what the sheet could only ever
have measured on four tiers on one afternoon.

**What did not change, and it is the reason to still run one.** Ticket 12's truncation is
**induced at known offsets**. Nothing there touches what only a real chat UI does — the per-message
cap, silent paste-to-attachment conversion, oldest-turn eviction. Those are still unmeasured, and
they are the mechanisms the sheet's own preamble says no documentation describes and no API
reproduces.

**Recommendation: run one tier, reduced to a positive control.** Not a ceiling hunt — tickets 08
and 13, which needed the ceiling number, are parked, so the number has no consumer. What is worth
ten minutes is a single question: **does a real free tier take the bundle inline and come back with
the correct KEYS line on the review?** That is steps 1, 2, 4 and 5 only. Step 3's three-marker probe
and step 6's re-probe stay in the sheet and stay valuable **here**, because a tester has the control
run a student does not — that asymmetry is exactly why ticket 12 did not ship the markers to
students.

**One thing to add if it is run:** the bundle will by then carry the interlock, so record the
review's first line verbatim. It is a stronger reading than the markers, and it is taken at the
moment the review is written rather than before the deck.
