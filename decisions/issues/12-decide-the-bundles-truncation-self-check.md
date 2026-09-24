# Decide the bundle's truncation self-check

Type: grilling
Status: resolved
Blocked by: —

## Question

Ticket 04 established the mechanism: **truncation announces itself only when the truncated thing
has a closure property the model checks.** The one arm that refused to review was the HTML arm —
a cut template is syntactically broken, and the model named the exact byte it died on and asked
for the rest. Every prose arm that lost paste 2 reviewed anyway, in some other shape. Worse, the
arm that lost paste 1 entirely returned a **perfect** 12/12 output with verbatim quotes, which no
check available to a student distinguishes from a good run.

So the free path has one detector today — *does the reply open with `REVIEW OF:`?* — and it covers
losing paste 2 only. Losing paste 1 is undetectable from the output.

Settle:

1. **Does the bundle carry an integrity check at all**, or is the `REVIEW OF:` detector plus a
   line in the instructions enough? A check that students skip is worse than none, because it
   reads as assurance.
2. **If yes, what is it?** Candidates: a terminator token at the end of each paste the model is
   told to confirm it saw; a word count or checksum the model restates; a required first line
   naming which pastes arrived. All of them cost tokens and all of them can be confabulated by a
   model that wants to be helpful — which is exactly the failure mode being defended against, so
   any candidate has to be tested against a truncated bundle, not reasoned about.
3. **What does the model do when the check fails?** Refuse outright, as the HTML arm did, or
   review with a stated caveat? Refusal is safer and is the behaviour already observed; a caveat
   is likelier to be ignored.
4. **Does paste 1 need the same redundancy the quote rule has?** Quote-or-abstain survived every
   cut because it is stated three times across both pastes. Nothing else is. Restating the
   synthesis protocol and the noise budget in paste 2 would make head-eviction survivable rather
   than merely detectable — at a token cost, and ticket 08 owns that budget.

Answer records: whether a check ships, its exact form, the failure behaviour, and any redundancy
added to paste 2. Any candidate must be verified against the ticket 04 truncation arms before it
is adopted.

---

## Resolution (2026-09-20)

Prototype: [`proto-12-selfcheck/`](../proto-12-selfcheck/), findings in
[RESULTS.md](../proto-12-selfcheck/RESULTS.md) — **read its limits section before quoting any
number here.** Two model families (gpt-5.6-sol via Codex, Haiku 4.5), nine arms, **34 scored
interlock runs plus 8 recall-probe runs**, truncation induced at known offsets as in ticket 04.
Local only.

**A check ships, and it is not the three markers.** The tester-facing and the student-facing check
are **two different mechanisms**. That is the decision this ticket turns on, and it is the question
the ticket could not ask because it predates ticket 11's marker design.

### The findings that made the call

**Ticket 04's silent failure is no longer silent.** With the entire system prompt missing, every
run on both families announced the loss and refused — against ticket 04's measurement of the same
cut returning 12/12 sections, verbatim quotes and a valid paste-back record, indistinguishable from
a good run by every check this project had.

**No model invented a key, in any run, on any arm.** The failure mode this ticket exists to defend
against — a model confabulating compliance because it is trying to be helpful — did not occur once
in 34 runs.

**The premise I was handed is wrong in one place, and it is worth recording because the brief rests
on it.** Ticket 11's sheet warns that the probe measures the model's recall rather than the text's
presence, so a model holding the whole bundle can still fail it, and that is why the control run is
mandatory. **It did not fail once in 6 complete-bundle runs, and it did not confabulate a lens label
in either cut run.** The three markers are a sound instrument. **The case against shipping them to
students is not that they false-alarm**, and any version of this answer leaning on that is leaning
on something unmeasured.

### 1. Does the bundle carry an integrity check at all? Yes — one, and the recall probe is not it

The three markers stay exactly where ticket 11 put them: **the tester's run sheet, with its
mandatory positive control.** They are not shipped to students. Three reasons, none of which is that
the probe is unreliable:

- **It reads the wrong moment.** The probe runs before the deck. Ticket 11's own step 6 exists
  because eviction can happen between the probe and the review, so a probe can pass and the review
  still be written from an evicted bundle. A student-facing check has to ride on the review itself.
- **It is skippable, which is this ticket's own disqualifier.** Three extra messages a student
  chooses to send, before the thing they came for. Question 1 above says a check students skip is
  worse than none because it reads as assurance.
- **Its pass criterion is plausibility.** A student judges three free-text answers against nothing.
  A shipped check has to be a comparison against a value the student holds outside the model.

### 2. What is it? A two-part cross-paste key interlock in the mandatory first line

Three edits, and the placement is load-bearing — see section 3 for the measurement that forced it:

- **Top of paste 1:** `BUNDLE KEY (part 1): <key 1>`, with the KEYS rule stated immediately under it.
- **Last line of paste 2A:** `BUNDLE KEY (part 2): <key 2>`.
- **With the output template in paste 2A (~88% depth):** the header line becomes
  `REVIEW OF: ... | MODE: ... | KEYS: <part 1>/<part 2>`, and the KEYS rule is stated a **second**
  time here — copy each character, write `MISSING` if you do not have one, never guess, never omit
  the field, and if either is missing do not produce the review at all.

**Why this is not a recall probe wearing a hat.** The value and the demand for it live in
**different pastes**, so any cut that removes a value leaves the demand standing, and the model must
produce the key, declare it missing, or invent one. And the student's check is
**"does the first line read exactly `KEYS: <key 1>/<key 2>`"** — a string comparison against a value
printed on their cover sheet. No baseline run, no control, no judgement, and **it cannot be skipped,
because it is the first line of the review they asked for.**

**The student's rule is "exactly this string, or re-paste" — never "look for the word MISSING".**
Measured: where the rule itself had been cut off, the model wrote `<missing>`, `part 2 missing` and
`part 2 not provided` as well as `MISSING`. Any deviation from the expected line is the signal.

**Cost: 303 tokens, 3.2% of the ~9,400-token bundle.**

### 3. What does the model do when the check fails? Refuse — and detection does not depend on it

Refusal is the measured behaviour with the correct placement: **0 reviews produced across every cut
arm under the corrected candidate, 9 of 9.**

> **CORRECTED 2026-09-20 by [ticket 09](09-decide-how-the-bundle-is-distributed-and-version-stamped.md),
> applied by [ticket 20](20-apply-the-accumulated-edit-lists-to-the-product.md).** This originally
> read *"9 of 9, on both families"*. It is not both families. An audit of the run files found the
> nine are **eight Codex runs and one Claude run**, and three further Claude runs on the `headdrop`
> arm **detected the missing key and reviewed anyway, 3 of 3** (contaminated framing, and a prompt
> confound recorded in `proto-12-selfcheck/RESULTS-B3.md`). So the honest figures are **refusal 8 of
> 8 on Codex, 1 of 4 on Haiku 4.5, contaminated** — a single-family result with a second family
> pointing the other way.
>
> **Nothing that ships changes**, and the reason is the sentence below: the student's string
> comparison caught all three. What changes is what may be written beside it. **Refusal is the
> model's cooperation; the string comparison is the check.** Do not describe the interlock as
> resting on refusal.

But the two halves are deliberately
independent — the student's string comparison catches the cut whether or not the model cooperates in
refusing.

That independence is doing real work, because **the false-alarm rate is bounded only weakly: 0 in 14
complete-bundle runs, a 95% upper bound near 19%.** That does not license "it almost never
false-alarms". It licenses "none was seen, and one student in five is not yet ruled out". The
asymmetry is what settles it: a false alarm costs one re-paste, a missed silent truncation costs a
confident review built on a third of its instructions.

**The one thing that broke was my own first design, and only a truncated run could show it.** The
first candidate put the refusal rule at the tail of paste 2A, beside the key it protects. The tail
cuts removed the rule along with the key, and the model **detected the missing key and wrote the
review anyway, 5 of 5.** Detection held; refusal did not. Restating the rule in both pastes — the
redundancy ticket 04 credits for quote-or-abstain surviving every arm — took the cut arms to
**refused 9 of 9** (see the correction in section 3: eight of those nine are Codex).
**A rule is not safe where the thing it guards is.**

### 4. Does paste 1 need the same redundancy the quote rule has? The rule does, the protocol does not, and the noise budget was never redundancy

The question bundles three things the run separates:

- **The KEYS rule: yes, and not optional.** Measured above. Already inside the 303 tokens.
- **The synthesis protocol: no, recommended against.** Restating it in paste 2A costs **1,377
  tokens, 15% of the bundle.** Its purpose was to make head-eviction *survivable* rather than merely
  detectable. With the interlock, head-eviction no longer produces a review at all — so what the
  redundancy now buys is **a degraded review instead of a refusal**, on exactly the windows most
  likely to cut. Worse trade, at 15%. Put to the owner as Q3 rather than decided here.
- **The noise budget: not redundancy at all — a missing rule, and decided here because ticket 08 is
  parked.** Ticket 04 found it is stated in **neither** paste while being cited by both, so the
  restraint ceiling is unenforced on the chat path whether or not anything is truncated.
  **Add it to paste 2A: 89 tokens.** The scope matrix, cited by paste 1 in the same breath, is
  **not** added — it feeds only the JSON/rubric branch, which is a defect path, so the dangling
  citation is deleted instead.

**Total token cost of this ticket: 392 tokens, 4.2% of the bundle.** Question 4 named ticket 08 as
the owner of that budget. 08 is parked, so the number is stated and owned here.

### What this does for ticket 21, which ran in parallel

**They have not become one decision, and 21 keeps all four of its questions.** But 12 removes 21's
hardest constraint. Ticket 21's problem is that *put the attempt gate in paste 1 and it vanishes
silently*. With the interlock, **paste 1 cannot vanish silently** — its loss is a refusal, measured
on both families with no review produced. So 21 can place the gate on its merits instead of around
an undetectable failure. Two caveats 21 must carry: the interlock's *demand* lives in paste 2A, so
it protects paste 1 and not itself; and all of this is induced truncation, not an observed tier.

### What this does for ticket 09

**The key can be the version stamp at no extra cost.** Ticket 09's question 2 lists "the output
carries the version" as an option, and this field already does, on every review, in a place a lead
reads. Give part 1 a version-readable prefix and one field answers both. **Untested as a variant** —
only arbitrary strings were run, and a meaningful key is by construction easier for a model to
confabulate, which is the one property measured at zero here. Put to the owner as Q2.

### Not claimed

- **No free tier was driven.** Truncation is induced at known offsets. Ticket 11's sheet remains the
  only thing that would measure where a real chat UI cuts.
- **The Claude arms are contaminated.** They were Haiku subagents told to read the arm from disk as
  a transcript, so the model knew it was handed material rather than sent a live paste. Every
  conclusion above holds on the **Codex arms alone**; the Claude arms are corroboration, not
  independent confirmation.
- **One deck, deep mode only.** Nothing here says the interlock behaves the same on a 70-slide deck
  or in short or lead mode.
- **Ticket 04's JSON-fallback readiness leak was not re-tested.** That defect was found on ticket
  04's Claude arms; the one format-loss arm here was Codex and carried no readiness level, but that
  is a different model on a different prompt version. Neither confirmed nor cleared.
- The interlock did not change the review's shape (2–4 findings, all sections, valid record), but
  the baseline for that comparison is a single ticket 04 run. It says "no shape change", not "no
  effect".

### Open questions to the owner

Three, written to the scene-first shape that `asking-rule.md` revision 2 introduced (the first
round of these was too abstract to argue with, which is what produced that revision):
[ticket-12/QUESTIONS.md](../ticket-12/QUESTIONS.md). Q1 — refuse or warn — is the one that cannot
be deferred.

### Edits

Appended to [ticket 20](20-apply-the-accumulated-edit-lists-to-the-product.md). **Nothing in the
product was changed by this session.**


**Owner answers recorded 2026-09-20** in [DECISIONS-2026-09-20.md](../DECISIONS-2026-09-20.md) Part 4. Read it before acting on the questions in this ticket.
