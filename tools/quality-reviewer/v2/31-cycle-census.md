# 31. The cycle census

Written down 2026-09-20 by ticket 20 (historical external working record),
from ticket 10 (historical external working record)
sections 3 and 5. It sits alongside [17-override-log.md](17-override-log.md), which specifies the
per-triage record. That document is the numerator. **This one is the denominator.**

**The five questions and the response-rate table below are pre-registered.** They were decided
before any data existed, with the consequence of each floor being missed committed in advance.
Neither may be softened or re-derived when the pilot is designed. Re-deriving a pre-registered
floor after seeing the data is the thing pre-registration exists to stop.

## 1. What it is

**Lead, once per project cycle, about five minutes.** One of three instruments:

| | instrument | who | when |
|---|---|---|---|
| 1 | the per-triage override record | lead | per review |
| 2 | **the cycle census** | lead | per project cycle |
| 3 | the attempt, plus one question | student | per review |

## 2. The five questions

1. List every deliverable your team produced this cycle — name, type, stage.
2. For each: was the reviewer run on it? *yes / no / don't know*.
3. For each "no": why not — *didn't know I could / no time / didn't think it would help /
   client-sensitive / forgot*.
4. Did the reviewer change anything your team actually sent to the client this cycle? *what, or no*.
5. Would you use it next cycle without being asked? *yes / no / only for what*.

**Question 3 is the load-bearing one and it is the whole reason this instrument exists.** It
converts silence from missing data into a *measured reason for silence*. Every other instrument in
this project can only hear from people who chose to answer; this is the one that asks why the
others were not used.

**Question 4 is the nearest available proxy** for the client-outcome measure that is still fog.
Whether the client got a better deliverable is the defensible outcome and nobody has yet said how
it would be measured.

## 3. Response rates, and what happens when one is missed

Non-response has a **known direction**: whoever skips was rushed, disengaged or unimpressed. So
returned feedback is a *systematic upper bound* on the tool's value, not a noisy estimate of it.
Chasing the rate with reminders or mandates converts a known-direction absence into "looks fine"
text of unknown direction, which is worse.

| instrument | assumed rate | floor | if the floor is missed |
|---|---|---|---|
| cycle census | **100% of leads** | 100% | that team is **excluded from every numerator and denominator** and reported as excluded. Never imputed. |
| per-triage record | **60% of reviews a lead ran** | 40% | lead-side precision figures are **not reported as rates at all** — raw counts only — and `readinessCall.lead`'s required reason is the first thing unwound |
| student one-question follow-up | **40%** | 25% | student self-report is **dropped entirely**; only the overlap is reported, which needs no response |
| attempt captured | **95% of runs** | 80% | the student instrument has failed and the pilot reports no student-side finding |

**The census is the one that must not fail, and it has no fallback.** Everything else degrades;
this one is load-bearing, because without it there is no denominator and the record count *is* the
response count. It is also the only one worth chasing: chasing a handful of leads is feasible in a
way chasing a cohort of students is not. That asymmetry is the argument for a census rather than a
response-rate caveat.

**"Attempt captured" is not the same as "attempt meant."** A gate in text can be satisfied by
pasting junk. Any attempt under about twenty words is counted as a bypass and excluded from
overlap, and **the bypass rate is reported beside the capture rate.** The twenty-word threshold is
a measurement-side rule only and must never be written into the bundle: ticket 21 measured a
model-enforced twenty-word rule refusing a genuine eight-word attempt on both model families.

**A second, wider bypass the pilot must count.** The attempt gate branches by audience — students
type, leads do not — so anyone who selects lead mode reaches the review without typing. A student
who hears about that can claim to be a lead. It cannot be prevented from inside a prompt, because
there is no identity to check; it is detectable in aggregate and not per student, through this same
capture rate and the `ATTEMPT ON RECORD:` marker. See [29-handover.md](29-handover.md) section 5.5.

## 4. The census's own honest weakness

Put to the owner and accepted rather than solved: **the lead's list is the only record of what the
list should have contained.** A lead who omits three unreviewed deliverables flatters the tool
invisibly. The mitigation is thin — cross-check the list against the team's own project plan where
one exists — and it is stated rather than closed.

## 5. Pre-registered ways this comes back negative

Recorded before the pilot so the result can refute rather than confirm. Any one is a reportable
negative finding:

1. **Revealed preference.** The census shows the reviewer was run on a minority of the deliverables
   it was available for, with nobody having been told to stop.
2. **Nothing new.** The median student attempt already contains 2 of the 3 findings the review
   returns — the tool is telling students what they already knew.
3. **Wrong, not just noisy.** Cuts carrying `cutReason: wrong` outnumber cuts carrying `too-minor`.
4. **Net cost.** Leads report `vsByHand: slower` more often than `faster`.
5. **Not voluntary.** Census question 5 comes back majority "no".
