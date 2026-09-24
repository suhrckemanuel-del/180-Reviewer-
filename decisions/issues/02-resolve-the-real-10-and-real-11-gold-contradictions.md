# Resolve the real-10 and real-11 gold contradictions

Type: task
Status: parked
Blocked by: —

## Question

Both cases have gold labels on disk and neither has a review, because the golds contradict
themselves: an issue is marked at a severity that does not match the readiness the labeler recorded.
`progress.md` describes the fix as a human citing the rule that fires, lowering the issue to major,
or raising the readiness — minutes of work — and says it takes the set from 9 to 11.

HITL: a human has to make the call, and it must be recorded as a call rather than silently edited.

Do:

1. Open `eval-cases-real/labeling/real-10.gold.md` and `real-11.gold.md` alongside the rubric.
2. For each, state which blocking rule fires and resolve the contradiction in the direction the rule
   dictates. Record the reasoning in the gold file itself.
3. Fill the empty table in `eval-cases-real/labeling/agreement-log.md` — it has a header and **zero
   rows** for 11 golds, so no gold in this project currently has a provenance record.
4. Fold both cases into the ticket 01 run.

Answer records: the two resolutions with the rule cited, and confirmation the gold log is populated.


---

**Parked 2026-09-20 by the owner, on the scope audit ([AUDIT-2026-09-20.md](../AUDIT-2026-09-20.md)).** Not cancelled and not out of scope: deferred until the pilot has run, at which point it is reconsidered against what the pilot actually showed.

Reason: the gold set stays at 9 cases; taking it to 11 serves the eval, which is off the critical path
