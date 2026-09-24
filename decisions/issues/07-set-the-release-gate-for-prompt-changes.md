# Set the release gate for prompt changes

Type: grilling
Status: parked
Blocked by: 02

## Question

The other eval that earns its keep, and the only thing standing between this tool and silent
calibration drift across a three-year total turnover. A future member edits the prompt; something
has to tell them they broke it.

Blocked because a gate needs a number to sit at, and the current baseline is two prompt versions
and one matcher generation stale. Ticket 01 produces the number; ticket 02 takes the set from 9
cases to 11.

Settle:

1. **What must hold** for a prompt change to ship. Candidates: no regression on the 11 real cases,
   zero fabricated quotes, no blocking rule missed, findings within the noise budget, stability
   across repeated runs of the same bytes.
2. **How tight.** Too loose and it gates nothing; too tight and every legitimate improvement trips
   it, and the gate gets waived until it is ornamental.
3. **What the honest floor is.** Per `17-override-log.md` §5, the instruments here measure precision
   well and recall barely. A gate that claims to protect coverage would be claiming something the
   evidence cannot support.
4. **Who can waive it, and where the waiver is recorded.** `22-trust-boundary.md` already has the
   pattern: a quote check can be waived, in writing, findably.
5. **Whether the held-out slice exists.** Cases used to tune the prompt cannot also judge it.
   With 11 cases, splitting hurts. Decide whether to split anyway.

Answer records: the gate as a checklist a non-author can run, the waiver rule, and what the gate
explicitly does not protect.

---

**Input from [ticket 03](03-recover-an-inter-rater-number-from-the-double-labelled-cases.md) (closed 2026-09-19).** Bears on question 3, the honest floor. Readiness exact-match against gold is measured against a reference two humans reproduce at 2 of 4, 95% CI [7%, 93%]. A bar measured against that is not a bar. Either attach the stated noise floor or drop readiness exact-match from the gate.

---

**Input from [ticket 14](14-decide-how-a-fresh-run-gets-judged.md) (closed 2026-09-19), and a scope
change from the owner.** The eval loop is **off the critical path**: the pilot ships without a gate
and real usage produces the comparison. This ticket is no longer a blocker on anything.

Two hard constraints when it is picked up:

1. **The gate may not contain must-catch recall, gold issue coverage or severity alignment.** No
   judging pass exists, so nothing measures them. Per-run judging was costed at **~412K tokens and
   ~5 minutes at one draw** (measured, not estimated) and was judged not worth paying for yet.
   A deterministic pre-filter was ruled out: its zero-error ceiling is 12.4%, fitted in-sample.
2. **Bears on question 3, the honest floor.** With readiness exact-match already discounted by
   ticket 03, the gate's defensible contents are over-flag rate, blocking rules missed, restraint
   violations, contract validity and fabricated-quote count. If the gate ever regains a matcher
   metric it should be **must-catch recall and not coverage** — recall rides the `yes` axis, which
   measured 96.6% stable within a sitting and 45/45 across six weeks, while coverage rides the
   `partial`/`no` boundary where all the drift lives.

---

**Input from [ticket 05](05-retire-the-readiness-level-everywhere-it-appears.md) (closed 2026-09-19).** **Constraint 1 above is partly wrong and this corrects it.**

That constraint named over-flag rate as one of the gate's defensible survivors. Over-flag is a
*readiness* metric — `score-review.js:538` computes it as a negative readiness delta — so it does
not survive readiness retirement on its own terms. It survives for a different reason: the golds
keep their `## Expected readiness` field, and the harness now derives the predicted level from the
blocking rules the review reports rather than reading one the model emitted. Measured at **26 of 27
across three prompt versions**, void on any deck where no blocking rule fires.

So the gate's defensible contents are unchanged in count but not in kind: **contract validity,
fabricated-quote count, blocking rules missed, blocking false positives, restraint violations, and
the derived readiness metrics** (exact, within-one, over-flag, under-flag).

Two things this ticket must not do:

1. **Do not print over-flag rate and blocking false positives as two rows.** Ticket 16 established
   they are the same six cases; under the derived scorer they are computed from the same field. One
   metric, one row.
2. **Do not quote a derived readiness number without its limit.** It is void where no rule fires,
   and it gets blinder as the decks improve — which is the direction ticket 16 is pushing them.
   Re-measure the derivation error rate after ticket 17 before setting any bar on it.

Question 3, the honest floor, now has a second discount stacked on ticket 03's: the reference is
noisy *and* the prediction is arithmetic over a field the model may stop populating.

---

**Input from [ticket 15](15-decide-whether-to-keep-or-roll-back-frozen-2026-08-09.md) (closed 2026-09-20). A hold on question 1, and a candidate metric with a caveat.**

**Do not set a bar on over-flag rate until [ticket 22](22-decide-the-findings-based-severity-score.md) resolves.** Ticket 15 asked whether over-flag survives as a gate metric and the owner answered by reopening the axis instead, so the question is live rather than settled. Over-flag may still be *reported*; it may not carry a pass/fail threshold.

Four discounts on it are now established, each from a different ticket, so this is not one objection restated: it is one metric counted twice with blocking false positives (16); it counts membership and not distance, which is why it read 66.7% before and after ticket 17's patch while within-one moved 55.6% to 77.8% (17); its human reference was reproduced on 2 of 4, 95% CI [7%, 93%] (03); and post-retirement it is derived from a level that is void where no blocking rule fires and gets blinder as decks improve (05). A fifth from ticket 15: **it measures a quantity the product no longer produces on any path.**

**The candidate replacement, recommended and not adopted — ticket 22 inherits it.** Move the restraint bar to the **severity distribution**: matcher-free, so untouched by constraint 1 above; already computed as of ticket 17 (`score-review.js:313-317` parses gold severities, `:582-585` emits per-review counts); the only headline row that has ever moved under a deliberate change; and the axis the chat path actually displays. Current standing: gold 8% critical / 65% major / 27% minor against `frozen-2026-09-19` at 26% / 64% / 9.5%.

**Its two limits belong in the bar if it is set.** A distribution match is weaker than an alignment match — two reviews with identical distributions can disagree on the severity of every finding — so it is a restraint signal, not an accuracy one, and must be labelled that way. And **nobody has measured whether two humans agree on a finding's severity**; the cheap route is closed, because `_INTER-RATER-RECOVERY.md:163` records the four second-reader worksheets as thin, one issue each. That is the position readiness was in before ticket 03 measured it and it came back unusable. Do not assume the better case here because the old number was bad.


---

**Parked 2026-09-20 by the owner, on the scope audit ([AUDIT-2026-09-20.md](../AUDIT-2026-09-20.md)).** Not cancelled and not out of scope: deferred until the pilot has run, at which point it is reconsidered against what the pilot actually showed.

Reason: the release gate was taken off the critical path on 2026-09-19 and nothing since put it back
