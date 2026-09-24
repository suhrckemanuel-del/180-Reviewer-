# Design the consultant feedback loop

Type: grilling
Status: resolved
Blocked by: —

## Question

Asked for at charting: the pilot should ask consultants for feedback, not just instrument them. This
is the qualitative half of the evidence, and it is the half that will explain *why* the numbers move.

The constraint that shapes it: per Lee et al. (CHI 2025), the named inhibitors of critical thinking
are lack of time, lack of incentive where thinking is not seen as part of the role, and lacking the
skill to inspect and steer output. A feedback form that costs five minutes is a form that gets
filled in by the conscientious and skipped by everyone the pilot most needs to hear from — and the
selection bias will flatter the tool.

Settle:

1. **Who is asked, and when.** Student after their review, lead after their triage, both at the end
   of a project cycle. These are three different instruments.
2. **What is actually worth asking.** Candidates: did it tell you something you did not know; did
   you disagree with anything and what; did you do something different because of it; would you use
   it again without being asked.
3. **The counterfactual.** `lead.vsByHand` exists because time-on-task was never interpretable
   without knowing what the same work costs unaided. The student side needs the equivalent, and
   "did it help" does not supply it.
4. **Cost.** Anything over about two minutes will not survive contact with a volunteer's week.
5. **What feedback is allowed to change.** Feedback that routes into the prompt without passing the
   release gate is how calibration drifts on vibes. Decide the path from a complaint to a change.

Answer records: the three instruments, their questions, and the route from feedback to a decision.

---

**Input from [ticket 05](05-retire-the-readiness-level-everywhere-it-appears.md) (closed 2026-09-19), and it is a decision this ticket should re-examine first.**

Ticket 05 kept `readinessCall.lead` — the lead's own four-level call — and made its one-line reason
**unconditionally required**. The old rule required a reason only when the lead differed from the
AI's call; the AI no longer makes one, so that trigger can never fire.

The owner took that decision against this ticket's stated constraint, which was put to him
explicitly: anything over about two minutes will not survive a volunteer's week, and mandatory free
text is the most reliable way to make a form get abandoned or filled with "looks fine" — which
would leave feedback from the conscientious only, flattering the tool.

**If pilot record volume disappoints, unwind this before anything else.** It is one field and one
rule, and it is the newest thing in the form.

Also relevant to question 2: `readinessCall.lead` is now the **only field in the record that is not
a reaction to what the tool said**. Everything else — keep, ask, cut, `cutReason` — exists because
the tool spoke first. Whatever instruments this ticket designs, that asymmetry is the one already in
the record and worth not duplicating.

---

## Answer (2026-09-20)

**Three instruments, and only one of them is a feedback form — the other two are a census and a
gate.** Working record: [ticket-10/FINDINGS.md](../ticket-10/FINDINGS.md).

Reprioritised onto the critical path the same day, on the owner's words: *we have to be sure it is
actually providing value.* That framing is what this answer is built to serve, and it forces one
thing the ticket did not ask for — **a pre-registered way for the pilot to come back negative.**
A design that can only return "yes" answers nothing.

### 0. The signal behind these decisions, stated plainly

The owner answered **A, A, A**. That is three recommendations accepted in a row, which is the exact
pattern [asking-rule.md](../asking-rule.md) was written after. Each question carried a real case
against, so this is not the ticket 14 failure repeating — but it is thin evidence and is recorded
as thin. **The one with an unpriced cost is Q2**, and it is flagged in section 3: choosing it
changes the product's default path, so the pilot will run a product that differs from everything
measured to date. If that lands badly, this is the decision to revisit, and the trigger is in
section 5.

### 1. The finding that reshaped the ticket: the attempt gate is not in the product

The map records *"Attempt first, always. Nothing unlocks until the consultant has committed their
own read"* as settled at charting. It is not implemented on the path the product is.

| artifact | attempt gate |
|---|---|
| `TEST-KIT/PASTE-1-system-prompt.txt` | **absent** |
| `TEST-KIT/PASTE-2A-chat-path.md` — *"this is the product"* | **absent**. Line 329's "attempt" is output content, not a gate |
| `TEST-KIT/PASTE-2B-json-contract.md:154` | present — a property of the **HTML renderer**, which is ticket 13's still-open default |
| `TEST-KIT/README.md:20` | present, as an instruction **to a tester**, with a box in `FEEDBACK.md` |

On the chat path the review arrives in one reply; there is nothing to unlock. And the paste-back
record is lead-shaped throughout — `lead.id`, `lead.vsByHand`, `readinessCall.lead`. **There is no
student, no attempt field, and no student-side record anywhere in the system.**

### 2. Why the record spec's outstanding work is void, not pending

[17-override-log.md](../../../tools/quality-reviewer/v2/17-override-log.md) sections 3 and 4 are
written against the Triage Desk in `index.html`. The map rules the hosted page out of scope, so:

- **Section 3 is void on the product path.** "Six of the record's fields need no new interface" was
  true of the desk. On the chat path a human types every field.
- **Section 4.1 is void, and its failure mode is genuinely absent.** The desk defaulted every
  finding to `keep` and pre-set the lead's readiness to the AI's — manufactured agreement. The
  paste-back block ships all-`null`. The chat path is **better** on anchoring-by-default and
  **worse** on abandonment: same bias, moved, not removed.
- **Sections 4.2 and 4.3 are already done** — `added: []` and `mustCatch` are both in the
  paste-back block.

Nobody should build section 3 or section 4. That correction is an edit, filed in section 8.

### 3. The three instruments

**Instrument 1 — the review record. Lead, per triage. Exists; unchanged.**
`TEST-KIT/PASTE-2A-chat-path.md:348`, `override-log-2-chat` (becoming `-3-chat` under ticket 20).
Kept as hand-filled JSON in chat; **no UI is built**. Its "two minutes" is a claim in the template
that no human has ever tested.

`readinessCall.lead`'s required reason **stays required**, which is ticket 05's call taken against
this ticket's own cost constraint. What changes is that the unwind now has a number instead of a
feeling — see section 5. This ticket's earlier note said "if pilot record volume disappoints,
unwind this before anything else"; that is now a pre-committed trigger, not a judgement call made
after seeing the data.

**Instrument 2 — the cycle census. Lead, once per project cycle, about 5 minutes. New, and it is
the denominator.** Five questions:

1. List every deliverable your team produced this cycle — name, type, stage.
2. For each: was the reviewer run on it? *yes / no / don't know*.
3. For each "no": why not — *didn't know I could / no time / didn't think it would help /
   client-sensitive / forgot*.
4. Did the reviewer change anything your team actually sent to the client this cycle? *what, or no*.
5. Would you use it next cycle without being asked? *yes / no / only for what*.

Question 3 is the load-bearing one and it is the whole reason this instrument exists. It converts
silence from missing data into a **measured reason for silence**. Question 4 is the nearest
available proxy for the client-outcome measure that remains fog.

**Instrument 3 — the attempt, plus one question. Student, per review.**

- **Before** the deck: the student types their own top three problems with it. The reviewer does not
  review until it has them. This is the charting decision finally being implemented.
- **After**: one question, one line, optional — *did you change the deliverable because of this,
  and what?*
- **Computed by us, at zero student cost**: how much of the review was already in the attempt.

The attempt is the only thing a student produces that is not a reaction to the tool — structurally
the same property that made `readinessCall.lead` worth keeping in ticket 05, and the asymmetry this
ticket's own input note warned against duplicating.

**No end-of-cycle student instrument.** The ticket floated "both at the end of a project cycle";
that collapses into the census. A student end-of-cycle form rides on nothing and is pure added cost.

### 4. The overlap measure, with its limits stated before anyone quotes it

Two sides: the attempt (written before the review) and the review (generated from the deck).
**Neither saw the other**, so it clears the standing caution on the input side. It does **not**
clear it on the judge side. Ticket 14 measured a fresh draw of the pair judge agreeing with its own
earlier majority on **86.7%, with 5 of 6 disagreements against a unanimous verdict**, and the cache
storing no model id. So: **the judge model is recorded on every overlap score, and the number is
reported as a band, never as a figure.**

A second limit, and it is not small: **convergence over a term is confounded by students simply
getting better over a term.** Without a comparison group, a closing gap evidences nothing about the
tool. Designing that comparison is pilot design, and it is filed as fog, not resolved here.

### 5. Response rates: assumed now, with the consequence pre-committed

The ticket's trap is real but it is stated one level too shallow. **Non-response has a known
direction** — whoever skips was rushed, disengaged, or unimpressed — so returned feedback is a
*systematic upper bound* on the tool's value, not a noisy estimate of it. Chasing the rate with
reminders or mandates converts a known-direction absence into "looks fine" text of unknown
direction, which is worse.

So the rates below are pre-registered **with what happens if each is missed**, decided now:

| instrument | assumed rate | floor | if the floor is missed |
|---|---|---|---|
| cycle census | **100% of leads** | 100% | that team is **excluded from every numerator and denominator** and reported as excluded. Never imputed. |
| per-triage record | **60% of reviews a lead ran** | 40% | lead-side precision figures are **not reported as rates at all** — raw counts only — and `readinessCall.lead`'s required reason is unwound first, per section 3 |
| student one-question follow-up | **40%** | 25% | student self-report is **dropped entirely**; only the overlap is reported, which needs no response |
| attempt captured | **95% of runs** | 80% | the student instrument has failed and the pilot reports no student-side finding |

Three things about that table.

**The census is the one that must not fail, and it has no fallback.** Everything else degrades; this
one is load-bearing, because without it there is no denominator and the record count *is* the
response count. It is also the only one worth chasing, and chasing a handful of leads is feasible in
a way chasing a cohort of students is not. That asymmetry is the actual argument for the census over
a response-rate caveat.

**"Attempt captured" is not the same as "attempt meant".** A gate in text can be satisfied by
pasting junk. Any attempt under about 20 words is counted as a bypass and excluded from overlap,
and the bypass rate is reported alongside the capture rate.

**The census's own honest weakness**, which was put to the owner and accepted: the lead's list is
the only record of what the list should have contained. A lead who omits three unreviewed
deliverables flatters the tool invisibly. Mitigation is thin — cross-check the list against the
team's own project plan where one exists — and it is stated rather than solved.

### 6. Pre-registered ways this comes back negative

Recorded before the pilot, so the result can refute rather than confirm. Any one of these is a
reportable negative finding:

1. **Revealed preference.** The census shows the reviewer was run on a minority of deliverables it
   was available for, with nobody having been told to stop.
2. **Nothing new.** The median student attempt already contains 2 of the 3 findings the review
   returns — the tool is telling students what they already knew.
3. **Wrong, not just noisy.** Cuts carrying `cutReason: wrong` outnumber cuts carrying `too-minor`.
4. **Net cost.** Leads report `vsByHand: slower` more often than `faster`.
5. **Not voluntary.** Census question 5 comes back majority "no".

### 7. Feedback's route to a change — nothing touches the prompt on its own

The gating eval is off the critical path, so "route it through the release gate" names something
that does not exist. What exists, demonstrated end-to-end by ticket 17: **new frozen version and
sha, packs regenerated, nine cases run blind, scorecard filed, change-isolation note written
honestly.** That is the gate, provisionally, until ticket 07 sets a real one.

- A complaint is **filed** and changes nothing by itself.
- A complaint implying a prompt change becomes a ticket on this map.
- **No prompt edit ships without the nine-deck run and a filed scorecard.** No exception for
  obviously-broken, which was the accepted cost of Q3's answer.
- Documentation, bundle contents and distribution are **not** gated this way.

Stated wherever this gate is invoked: the golds behind it agreed **2 of 4, 95% interval [7%, 93%]**
(ticket 03), over-flag counts membership not distance (ticket 17 section 4), and ticket 17's own
comparison was **uncontrolled** because neither prior baseline recorded the reviewer model. **It is
a change-detector, not a quality bar.**

### 8. Edits, appended to ticket 20

1. **Add the attempt gate to the chat path.** The reviewer refuses to review until the consultant
   has given their own top three. Exact wording and placement are **not settled here** — see the
   new ticket in section 9, and route back rather than inventing it.
2. **Add a student-side record.** The paste-back block is lead-shaped; it needs an `attempt` field
   and a student variant, or the student produces nothing recordable.
3. **Correct `17-override-log.md`.** Mark sections 3 and 4.1 **void** against the product path,
   with the reason (the desk is out of scope), and mark 4.2 and 4.3 **already present** in the
   paste-back block. As written they read as outstanding work, and building them would build the
   wrong thing.
4. **Write the census down** as a document alongside the record spec, with section 5's table in it.

### 9. What this surfaced

**New ticket 21 — where the attempt gate lives, given losing paste 1 is silent.** Ticket 04's
sharpest finding is that head-eviction is undetectable: the `headdrop` arm returned 12/12 sections
with verbatim quotes, indistinguishable from a good run. **If the gate lives in paste 1 and paste 1
is truncated, the gate disappears silently and the review proceeds with no attempt** — and the
attempt is now the student's entire instrument. The failure lands hardest on small free-tier
windows, which is exactly the population the pilot needs. That is a decision about placement and
redundancy, it is sharp now, and it sits directly against ticket 12.

**Unchanged as fog:** client-level deliverable improvement, and the comparison group the overlap
measure would need.
