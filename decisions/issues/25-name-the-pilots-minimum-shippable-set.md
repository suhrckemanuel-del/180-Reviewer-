# Name the pilot's minimum shippable set

Type: grilling
Status: resolved
Blocked by: —

## Question

Graduated 2026-09-20 from the map's **Not yet specified** patch *"What 'usable' actually means, and
how we know we reached it"*, which said it would be sharp enough to ticket once someone picked up
one of the usability tickets. Three have now been picked up and the patch is sharp: it is a
sequencing question, and it is the question that tells this map when it is finished.

**The destination is a pilot. Nobody has said which open tickets block it.** There are ten open
tickets and one execution ticket, and they are currently a flat list with no precondition ordering:

| ticket | what it decides | blocks a pilot? |
|---|---|---|
| [20](20-apply-the-accumulated-edit-lists-to-the-product.md) | apply the accumulated edits (the only ticket that changes the product) | **almost certainly yes** |
| [21](21-decide-where-the-attempt-gate-lives.md) | where the attempt gate lives — ticket 10 found it is **not in the product** | ? |
| [24](24-decide-how-the-path-that-ships-gets-measured.md) | how the shipping path gets measured at all | ? |
| [08](08-decide-what-goes-in-the-methodology-context-bundle.md) | what goes in the bundle | ? |
| [09](09-decide-how-the-bundle-is-distributed-and-version-stamped.md) | how the bundle is distributed | ? |
| [11](11-measure-the-four-free-tiers-by-hand.md) | whether the bundle fits a free tier | ? |
| [12](12-decide-the-bundles-truncation-self-check.md) | the truncation self-check | ? |
| [13](13-decide-the-default-output-path.md) | HTML or prose by default | ? |
| [22](22-decide-the-findings-based-severity-score.md) | the findings-based score | ? |
| [23](23-settle-whether-a-minor-finding-can-be-delivery-critical.md) | a live contract conflict | ? |
| [02](02-resolve-the-real-10-and-real-11-gold-contradictions.md), [06](06-define-the-student-trajectory-metric.md), [07](07-set-the-release-gate-for-prompt-changes.md), [18](18-decide-whether-blocking-rule-2-needs-the-same-treatment.md) | eval and gold work | probably not — 14 took the gate off the critical path |

**Why this is worth a ticket rather than a judgement call in passing.** Every session so far has
picked the next ticket by what was unblocked, and the map has produced nine resolutions and zero
product changes. An unordered frontier is what allowed that: each ticket was takeable, so one was
taken, and none of them was the one that ships anything. Naming the minimum set converts the
frontier from "what can I do" to "what is left".

### Settle

1. **Which of the above are preconditions** of putting this in front of one cohort, and which are
   improvements that can land during or after. Two lists, not a ranking.
2. **What the pilot is allowed to ship without.** State it as a list of known gaps the cohort runs
   with, so they are accepted rather than forgotten. Candidates on today's evidence: no release
   gate, no must-catch measurement, no score on the path that ships, no comparison group.
3. **What "usable" means, concretely enough to fail.** The destination has carried the word since
   2026-09-19 with no definition. One or two sentences naming what a student must be able to do
   without help.
4. **Whether anything currently in scope should leave it.** With nine resolutions behind it, this
   is the natural moment to cut, and cutting is cheaper than sequencing.

### Two things that make this answerable now and did not before

- **Ticket 10 fixed the instruments and pre-registered their floors**, so "what the pilot records"
  is no longer an open variable in this decision.
- **Ticket 15 named the shipping version**, so the prompt is no longer a moving target.

### The one thing to be careful of

The honest answer may be that **the minimum set is larger than it looks**, because ticket 10 found
the attempt gate — settled at charting as *"Attempt first, always"* — is absent from the product,
and ticket 24 found the product path has never been measured. A short precondition list assembled
in a hurry would be the third instance of this map's recurring failure: a comfortable answer that
nothing checked. Per [asking-rule.md](../asking-rule.md), whoever puts this to the owner carries
the case for the *longer* list as well as the shorter one.

Answer records: the precondition list, the accepted-gaps list, a definition of usable, and anything
cut from scope.


## Answer (2026-09-20)

**Resolved by the scope audit rather than by its own session** — the owner asked the question this
ticket exists to ask, in conversation, the hour after it was created. Full working:
[AUDIT-2026-09-20.md](../AUDIT-2026-09-20.md).

**The precondition list is four tickets:** [20](20-apply-the-accumulated-edit-lists-to-the-product.md)
cut down to its four pilot items, [12](12-decide-the-bundles-truncation-self-check.md),
[21](21-decide-where-the-attempt-gate-lives.md) and
[09](09-decide-how-the-bundle-is-distributed-and-version-stamped.md).

**Eight tickets are parked** until the pilot has run: 02, 06, 07, 08, 13, 18, 23, 24, plus ticket 11
reduced. Parked is recorded on each ticket with its reason; it is a deferral, not a scope ruling.

**The accepted-gaps list**, so these are carried visibly rather than forgotten:

1. **No release gate.** Off the critical path since 2026-09-19; a future member can edit the prompt
   with nothing telling them they broke it.
2. **Must-catch recall and gold coverage are unmeasured**, not zero, and may not be quoted (ticket 14).
3. **The path that ships has never been scored, on any version.** All thirty-six reviews on record
   ran the harness path (ticket 24).
4. **Blocking rule 2 fires on 9 of 9 decks, unguarded** (ticket 18). Not visible on the pilot path,
   which emits no rule numbers.
5. **A minor finding marked delivery-critical fails the JSON contract** (ticket 23). Not reachable
   on the pilot path, which has no such field.
6. **No comparison group** for the attempt-overlap measure (ticket 10).

**"Usable", defined:** a student or lead can obtain the current bundle without the repo, paste it
into a free account, be told if it was cut, be made to commit their own read first, and receive
findings they can check against their own deliverable. Nothing in that sentence requires a score, a
readiness level, a hosted page or an eval.

**What this ticket got wrong about itself:** it argued the minimum set might be *larger* than it
looks. The audit found the opposite — four of twelve — because the test it applied (can the pilot
run without this?) is stricter than the test the map had been using (is this unblocked?).
