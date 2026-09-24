# The truncation interlock false-alarmed on a complete bundle

Type: task
Status: open
Blocked by: —

## Question

Observed 2026-09-24 during [ticket 26](26-rewrite-the-finding-for-a-student-who-has-to-act-tonight.md)'s
verification run, on a mechanism that **ships**.

`codex--student-attempt-r2` refused to review:

> `KEYS: MISSING/OMEGA-9X`
> `Part 1 is missing. Your instructions arrived incomplete.`

**Both keys were in the bundle.** The bundle is **byte-identical** to `student-attempt-r1`, which
reviewed normally in the same batch. Re-run on the same bytes, it reviewed normally too.

So the interlock **false-alarmed, stochastically, on a complete bundle**.

### Why this is not a small thing

- [Ticket 12](12-decide-the-bundles-truncation-self-check.md) measured false alarms at **0 of 14
  complete-bundle runs** and set the honest upper bound near one in five. This is the first
  observed instance, and it moves that from "not seen" to "seen once".
- **It is the readiness level's defect in a different component**: two different answers on
  identical bytes. That property is what retired the readiness level and widened stop condition 3.
- The cost lands on a student: they are told their paste was cut and sent to re-paste from the
  Drive folder when nothing was wrong. It is the one refusal path in the product.

### What is not yet known, and must not be assumed

- **Whether it reproduces at any rate.** One refusal, one clean re-run, on one model family, on the
  **new** Codex binary (`80f78947ad880e6e`, codex-cli 0.155) -- not the binary ticket 12 measured
  on, which no longer exists.
- Whether the round of prompt edits ticket 26 made to paste 2 has any bearing. The interlock text
  was not edited, but paste 2 was, and no run isolates that.

### Settle

1. Reproduce or bound it: run the same bytes N times on both families and report a rate with its
   interval, not a verdict.
2. Whether ticket 12's "0 of 14" needs a correction note in
   [12-decide-the-bundles-truncation-self-check.md](12-decide-the-bundles-truncation-self-check.md)
   and in `22-trust-boundary.md`.
3. Whether the refusal should be softened for the case where one key is present and one is not --
   currently a missing part 1 refuses outright.

### Evidence

`ticket-26/runs/codex--student-attempt-r2--refusal1.md` is the preserved refusal; the bundle that
produced it is `ticket-26/bundles/student-attempt-r2.txt`. Local only.
