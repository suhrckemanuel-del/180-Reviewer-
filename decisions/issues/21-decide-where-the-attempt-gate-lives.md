# Decide where the attempt gate lives, given that losing paste 1 is silent

Type: grilling
Status: resolved
Blocked by: —

## Question

Surfaced by [ticket 10](10-design-the-consultant-feedback-loop.md) on 2026-09-20, which made the
student's typed attempt the **entire** student-side instrument for the pilot. That promotion is
what turns a placement detail into a decision.

Two established facts collide.

**One.** The map settled *"Attempt first, always"* while charting, and ticket 10 found it is **not
implemented on the product path** — it exists only in the HTML renderer (`PASTE-2B:154`) and as an
instruction to testers (`TEST-KIT/README.md:20`). Paste 1 and paste 2A, the path that calls itself
"this is the product", have no gate at all. So it has to be added.

**Two.** Ticket 04 measured that **losing paste 1 is silent**. The `headdrop` arm, with the entire
system prompt missing, returned 12/12 sections on both model families, every quote verbatim, a
valid paste-back record — indistinguishable from a good run by every check available, including the
quote gate. The mechanism it established: *truncation announces itself only when the truncated
thing has a closure property the model checks*, and prose has none.

Therefore: **put the gate in paste 1 and it disappears silently on exactly the small free-tier
windows the pilot most needs to hear from, and the review proceeds with no attempt.** The student
sees a normal-looking review. Ticket 10 pre-registered an 80% floor on attempt capture below which
the student instrument is declared failed — this is the mechanism most likely to breach it, and it
breaches it invisibly.

Settle:

1. **Which paste carries the gate**, or whether it is stated in both the way quote-or-abstain is.
   Quote-or-abstain is the one rule that survived every truncation arm, and the reason ticket 04
   gives is that it is stated three times across the two pastes. Nothing else is. That is a
   worked precedent, at a token cost that ticket 08 owns.
2. **What the gate actually does when no attempt has been given.** Refuse and ask, or review with a
   caveat. Ticket 12 faces the same fork on truncation and reached for refusal because it is the
   behaviour already observed; a caveat is likelier to be ignored.
3. **What counts as an attempt.** Ticket 10 set a working rule — under about 20 words is a bypass,
   excluded from the overlap measure, and the bypass rate is reported next to the capture rate. Is
   that the rule, and does the model enforce it or do we only measure it afterwards? A model that
   judges attempt quality is a model that can be argued with by a student in a hurry.
4. **Whether the gate is detectable from the output.** If a review can be produced with no attempt,
   nothing downstream can tell that run from a gated one. A one-line marker in the output — the
   same shape as ticket 04's `REVIEW OF:` detector — may be cheaper than making the gate robust.

**Anything proposed here must be tested against the ticket 04 truncation arms**, not reasoned
about, for the reason that ticket gives: the failure mode being defended against is a model
helpfully confabulating compliance.

**Overlaps ticket 12 deliberately.** 12 asks whether the bundle carries an integrity check at all
and what it is; this asks where one specific rule must survive and why it cannot be left to a
general check that does not exist yet. Whoever takes the second of the two should read the first
and say plainly if they have become one decision.

Answer records: the placement, the failure behaviour, the attempt threshold and who enforces it,
and any output-side marker. Edits go to [ticket 20](20-apply-the-accumulated-edit-lists-to-the-product.md).

---

## Answer (2026-09-20)

**The gate goes at the top of paste 3, the paste the student fills in, and that position was not
on this ticket's list.** Working record: [ticket-21/RESULTS.md](../ticket-21/RESULTS.md) —
**39 runs, two model families**, over ticket 04's truncation arms plus two new ones.

**The ticket was rewritten by today's withdrawal of the hosted page.** It says the gate exists in
the HTML renderer at `PASTE-2B:154`. That page is kill-switched, so the gate now exists nowhere a
user can reach. This is not a move. It is the first build.

### 0. The result that makes the rest small

**The gate is a pure function of whether its text is in the window.** Where the gate text survived
the cut, the model refused to review with nothing typed **16 of 16 times** — both families, every
truncation level, both wordings, and under a student arguing back. Where the gate text was cut, the
model reviewed **6 of 6 times** and **never once invented a marker claiming an attempt had been
given** (0 fabrications in 6).

That is the failure this ticket was built to fear — a model helpfully confabulating compliance —
and it did not appear. So there is no partial compliance to engineer around and no confabulation
to defend against. **There is only placement**, and placement is a fact about eviction order, not
about the model.

### 1. Placement: paste 3 first, paste 1 second, paste 2 not at all

Eviction drops the **oldest** turn. That orders every candidate and it **inverts the ticket's
framing**, which assumed the choice was paste 1 versus paste 2 and treated a copy in both as the
robust answer.

- **Paste 1 is the worst available position, not a safe second copy.** It is evicted first.
  `p1-headdrop-no` reviewed with no gate on both families. Ticket 10 predicted exactly this.
- **Head of paste 2 survives paste 1's eviction but dies when eviction reaches into paste 2**
  (`both-headdrop2-no`, both families, reviewed ungated). Ticket 04 had no arm for that cut, so
  this is new.
- **Head of paste 3 — the deck the student pastes last — survived the cut that killed every other
  placement**, on both families. It is the newest turn, so it is the last thing evicted.

So the redundancy question this ticket inherited from ticket 08 is **not a redundancy question.**
Three copies are three different failures, and only two are worth paying for:

| copy | the failure it alone covers | evidence |
|---|---|---|
| **paste 3, head** | eviction of everything older | `p3-evict-no` refused, both families |
| **paste 1, head** | the student never sends paste 2 | `p1only-no` refused; without the gate the same bundle fell through to the JSON branch and emitted the ten-dimension rubric **with a readiness level** |
| paste 2 | nothing the other two do not already cover | — |

**Ship the gate in paste 3 and paste 1. Not paste 2.** The paste-1 copy also suppresses ticket
04's JSON-fallback defect — a live stop-condition-3 violation under tickets 05 and 16 — as a side
effect, which is the strongest argument for paying for it.

**Cost, decided on its merits because ticket 08 is parked and owns nothing:** the gate block is
**198 tokens**. Two copies are **+396 on the 9,227-token instruction bundle, +4.3%**; +3.0% of a
typical review conversation, +1.7% of the worst of fourteen real decks. **The denominator is
unmeasured** — no free-tier window has been measured (ticket 11) — so this is a known cost against
an unknown ceiling, and that is the honest statement of it. 4.3% is cheap enough that the decision
does not turn on it; what it turns on is that the two copies are not copies.

### 2. Failure behaviour: refuse, and it cannot be argued past

**Refuse and ask.** 16 of 16, including **4 of 4 escalation arms** — two of them with the model's
own refusal already in context and the student replying *"that IS my attempt … you are wasting my
time and this is exactly why nobody uses these tools."*

**The thinnest load-bearing number in this ticket: escalation is one family, four runs.** A
single-family result on "can this be argued past" is thin and is recorded as thin. No caveat
wording was run, so ticket 12's "a caveat is likelier to be ignored" is inherited, not measured.

### 3. What counts as an attempt: never write a number the model can enforce

Ticket 10's working rule — under about 20 words is a bypass — was run **as a rule the model
enforces**, head to head against a wording that names presence and specificity with no number.

| wording | junk: *"not sure honestly, looks fine to me"* | short but real: *"the recommendation is too vague to act on"* |
|---|---|---|
| presence and specificity, no number | refused 2 of 3 | **reviewed 2 of 2** |
| the 20-word rule, model-enforced | refused 2 of 2 | **refused 2 of 2** |

**Encoding the threshold makes the model refuse real attempts.** Both families turned away a
genuine, specific, eight-word read of the deck. That is the hurried-but-honest student — the
population ticket 10's 80% capture floor is about — and the enforced rule is the mechanism most
likely to breach it.

The ticket asked whether the model enforces the threshold or we only measure it afterwards. **We
only measure it afterwards.** Ticket 10's 20-word rule survives unchanged as a *measurement-side*
rule: attempts under about 20 words are counted as bypasses, excluded from overlap, and the bypass
rate is reported beside the capture rate.

And one correction to the ticket's own framing, which asked for a gate that does not judge quality:
**there is no such gate.** Told to check presence, the model judged quality anyway, unasked, on 2
runs of 3. The choice is not whether it judges — it is whether we hand it a number to enforce
against a real attempt. **The same junk string on the same model was refused once and reviewed
once**, so model judgement of attempt quality is non-deterministic in both directions and nothing
downstream may lean on it.

### 4. The output marker: one-sided, and it goes on line 2

Ship `ATTEMPT ON RECORD: "<the consultant's read, verbatim>"` **as the line immediately after
`REVIEW OF:`**, never before it.

- **0 fabrications in 6** ungated runs. Presence of the line is trustworthy.
- **Present 10 of 11** times when an attempt was given; **verbatim 10 of 10**, including the one
  that quoted junk straight back.
- **On the instructed line 7 of 11.** Codex 6 of 6; Haiku 1 of 5 — Haiku parks it after the
  `BEFORE YOU USE THIS` block wherever it is told to put it.

So it is a **one-sided detector: presence proves an attempt, absence proves nothing.** It must be
described that way wherever it is written down, or it becomes the thing ticket 12 warns about — a
check that reads as assurance.

**Putting it on line 1 would have broken ticket 04's `REVIEW OF:` detector**, the only truncation
check the free path has. That is the concrete collision between this ticket and ticket 12, and it
is avoided by ordering rather than negotiated later.

### 5. Ticket 12: not one decision, but they share one line of output

Read as asked. **They are not one decision, and merging them would be wrong.**

Three of this ticket's four questions turned out not to depend on ticket 12 at all, because the
gate needs no integrity check to work — 16 of 16 says it works whenever its text is present, and
0 of 6 says it is absent whenever its text is not. Placement, failure behaviour and the attempt
threshold are settled here and none of them waits on anything.

What they **do** share is one artifact: **the first two lines of the output**. One of them must own
it, and it should be ticket 12, because a detector for "the attempt was missing" and a detector for
"paste 1 was evicted" are the same missing line. This ticket hands ticket 12 three measured
constraints rather than a second answer:

1. `REVIEW OF:` **stays line 1.** The attempt marker goes on line 2. Non-negotiable — it is what
   keeps ticket 04's detector alive.
2. **Marker compliance is 7 of 11 on line placement and 10 of 11 on presence**, so any check built
   on line *position* is weaker than one built on presence anywhere in the reply.
3. **A gate in paste 3 is the most eviction-resistant position in the bundle.** If ticket 12 ships
   a terminator or a paste-census line, the same ordering argument applies to it, and it should
   not be placed in paste 1.

One finding is ticket 12's outright, found here and handed over: **`both-headdrop2-no` reviewed
normally and opened with `REVIEW OF:` on both families** — ticket 04's detector passes a bundle
that lost the entire system prompt *and* the front of paste 2. That is the detector's blind spot,
measured.

**Checked against ticket 12 after it landed, rather than left to agree later.** Ticket 12 closed
the same day and its Group D **extends** line 1 to
`REVIEW OF: … | MODE: … | KEYS: <part 1>/<part 2>` rather than replacing it. So `REVIEW OF:`
survives, line 2 is free, and the two answers fit without either being renegotiated. The collision
this ticket was worried about did not happen, because both sessions kept the same line 1.

**And the two tickets disagree on one number in a way that is informative rather than a conflict.**
Ticket 12 measured that a key rule shipped without its template change fails **5 of 5** — the model
notices the missing key and writes the review anyway. This ticket measured refusal holding
**16 of 16**. These are not the same instrument and not a copy of each other: ticket 12's check
asks the model to *report* a defect, this one asks it to *withhold the product*, and they were run
in different sessions on different prototypes. The rule worth carrying out of both: **a check that
reports gets ignored; a check that withholds holds.** For one of these to move without the other,
someone would have to change what the model is asked to do on failure, not how loudly it is
told.

### 6. What this knowingly ships without

- **The hole, and it is smaller than this ticket thought before ticket 12 landed.** If eviction
  eats into paste 3's head the gate is gone and the review proceeds; nothing in the bundle can
  survive that, because the check's own text is what got cut. But Group D's key interlock fires
  first on the cut that matters: in `headdrop2` the paste-1 key is gone while the demand for it
  survives in paste 2, so the review is refused before the missing gate can matter. **The residual
  is the cut that takes the gate *and* the demand line** — everything up to 88% of paste 2 — and
  whether any real free tier cuts that deep is **unmeasured** (ticket 11, reduced rather than
  parked). This was written as unclosable and is corrected here; the two groups together are
  stronger than either, which is an argument for shipping them together and not for shipping
  either alone.
- **No measurement of what refusal costs.** Nothing here touches abandonment, which ticket 10 named
  as the bias the chat path already carries.
- Truncation is **induced, not observed** (inherited from ticket 04). One junk string and one
  short-real string are not a sample of student writing. Cells are n=1 except the junk cell at n=3,
  and that is the cell that disagreed with itself.

Edits appended to [ticket 20](20-apply-the-accumulated-edit-lists-to-the-product.md), Group E.


**Owner answers recorded 2026-09-20** in [DECISIONS-2026-09-20.md](../DECISIONS-2026-09-20.md) Part 4. Read it before acting on the questions in this ticket.


**Owner ruling 2026-09-20, and it overrides ticket 09's resolution of the same point.** **Leads do not type; students do; the audience branch is one named switch with one documented default.** Ticket 09 resolved this as unconditional by inference from a remark the owner had already withdrawn; he has now confirmed students-only a second time, knowing the escape-hatch objection. Build the switch, do not resolve this from ticket 09's write-up, and correct HANDOVER section 5.5. Full ruling and its two consequences - the bypass as an accepted gap, and the mandatory re-run of the branched gate - are in [DECISIONS-2026-09-20.md](../DECISIONS-2026-09-20.md), Q4 final ruling.
