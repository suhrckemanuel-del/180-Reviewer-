# Define the student trajectory metric and what gets stored

Type: grilling
Status: parked
Blocked by: —

## Question

One of the two evals that earn their keep. The other is the release gate (ticket 07); this is the
one that measures what 180DC exists to do.

The mechanism comes from McKinsey Quarterly's answer-key model (July 2026): the junior attempts the
work, AI grades it, the gap between the two narrows as judgment forms. Today the attempt gate makes
a student type their own read before findings unlock — **and then throws it away**. Nothing about a
student's development is recoverable.

Settle:

1. **What is a "gap".** The student writes prose; the reviewer emits structured findings. Comparing
   them is not obvious. Candidates: did the student name the same issue, at the same severity, on
   the same slide? Coverage of the reviewer's findings? Something coarser and hand-scored?
2. **Who computes it.** A model comparing attempt to findings is a model grading a student, which
   collides with principle 3 (rank, do not reject; no pass/fail verdicts on humans).
3. **Where the attempt is stored.** It is the student's own words about a real client deliverable,
   so it is confidential and it is personal. Chapter-local, never the shared corpus.
4. **What the student sees.** Their own trajectory only. Never a ranking against peers, and never
   "the AI was right N% of the time" — per Lee et al. (CHI 2025), confidence in the AI is the
   strongest predictor of *less* critical thinking, so an accuracy figure pointed at a student
   attacks the variable the tool exists to protect.
5. **Whether a flat trajectory means anything.** A student who does not converge may be improving,
   disengaged, or right where the reviewer is wrong. Decide what the metric is not allowed to claim.

Answer records: the metric definition, the storage location, who computes it, and what is shown.


---

**Parked 2026-09-20 by the owner, on the scope audit ([AUDIT-2026-09-20.md](../AUDIT-2026-09-20.md)).** Not cancelled and not out of scope: deferred until the pilot has run, at which point it is reconsidered against what the pilot actually showed.

Reason: the student-trajectory eval needs the attempt stored, which ticket 21 has not decided yet
