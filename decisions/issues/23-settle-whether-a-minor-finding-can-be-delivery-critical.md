# Settle whether a minor finding can be delivery-critical

Type: grilling
Status: parked
Blocked by: —

## Question

Surfaced by the ticket 17 verification run on 2026-09-19, which it made contract-invalid on
two of nine cases. This is a live defect on the shipped prompt, not a cleanup item.

Ungating the severity demotion floor (ticket 16, decision 2) made minor findings common for
the first time: 1 in 45 before, 4 in 42 after. That immediately surfaced a conflict with an
invariant that has been in `check-review-v2.js` since the beginning and had almost never had
the chance to fire.

**Rule 8b:** a finding graded minor may not be marked `deliveryCritical: true`.

Two of the four new minors break it, two do not, same prompt, same run:

    real-01 f5  minor, deliveryCritical=true   "Placeholder Latin remains"
    real-05 f5  minor, deliveryCritical=true   "Internal notes retained"
    real-08 f4  minor, deliveryCritical=false  "Conclusion repeats opening"
    real-12 f5  minor, deliveryCritical=false  "Unresolved internal comments"

Both offenders are QA artifacts: placeholder text and leftover internal notes in a deck about
to go to a real client. **The reviewer's position is coherent and the prompt does not refute
it.** Closing the finding does not change what the client decides, which is exactly the
ungated floor's definition of minor. And the deck must not leave the building in that state,
which is exactly what delivery-critical means. Severity and delivery-criticality were
measuring two different things all along, and nothing noticed while minors did not exist.

The prompt's own deliveryCritical clause is written only for the no-blocker case: "If no
blocking rule fired and readiness is Needs targeted revision or better, deliveryCritical may
be true only for the single finding that is itself the reason readiness is not Nearly ready."
The severity floor no longer carries that gate. **The two rules no longer meet in the middle**,
and the space between them is where these two findings sit.

Settle which gives way:

1. **Rule 8b is wrong and goes.** Severity answers "does the client decide differently", and
   deliveryCritical answers "can this go out of the door". A QA artifact is honestly low on
   the first and absolute on the second. Cost: the invariant exists to stop a reviewer
   marking everything urgent, and this removes that floor entirely.
2. **The prompt is wrong and QA artifacts are not minor.** Keep 8b, teach the prompt that a
   professionalism or confidentiality defect is graded on exposure rather than on decision
   change. Cost: reintroduces a severity inflation path on exactly the axis the ungated floor
   was deflating, and it is the axis where "critical" is cheapest to reach for.
3. **Neither, and deliveryCritical is the field that should not exist.** It has a precedent
   this quarter: confidence retired in ticket 16 for carrying no variance, and readiness in
   ticket 05 for being untrustworthy. Nobody has asked what deliveryCritical is worth on real
   decks. Cost: it is load-bearing for the triage desk and the student pack.

Worth checking before deciding: how often the field has varied on real decks at all, and
whether the gold worksheets carry anything equivalent. If it is another constant, option 3
stops being the outside possibility.

Whichever wins, note that the ungated floor is the change that exposed this, and that a
contract invariant nobody can trip is not a verified invariant. That is the same shape as the
dead severity floor ticket 16 found: rules that have never engaged are not known to work.

Answer records: which rule changes, the edit, and whether the two invalid reviews become
valid under it without being rewritten.


---

**Parked 2026-09-20 by the owner, on the scope audit ([AUDIT-2026-09-20.md](../AUDIT-2026-09-20.md)).** Not cancelled and not out of scope: deferred until the pilot has run, at which point it is reconsidered against what the pilot actually showed.

Reason: **a live defect, parked knowingly** - the minor/delivery-critical conflict invalidates reviews against the JSON contract. The pilot ships the prose path, which has no such field. Carried on the accepted-gaps list.
