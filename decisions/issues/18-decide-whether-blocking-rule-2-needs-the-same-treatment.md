# Decide whether blocking rule 2 needs the same treatment as rule 1

Type: grilling
Status: parked
Blocked by: 17

## Question

Surfaced by [ticket 16](16-decide-what-to-do-about-the-two-prompt-defects-the-baseline-exposed.md)
on 2026-09-19 and deliberately left open there.

**Blocking rule 2 fired on 9 of 9 real decks.** Rule 1 fired on 4, rule 4 on 3, rules 3 and 5 never.
Rule 2 reads:

> The client decision is unclear, the deck does not answer the client's question, or the core
> recommendation is unsupported. Ceiling Needs substantial revision.

Three limbs joined by "or", no guardrail on any of them, and each is arguably true of almost every
student deck ever written. Rule 1 got a guardrail on 2026-08-07 and rule 4 has always carried one
("fires only when the number drives the decision"). **Rule 2's text is byte-identical across every
commit that has ever touched the prompt document.** It is the clause that fires on everything and
the one clause nobody has looked at.

Why this was not decided with rule 1: **its effect cannot be calculated.** Rule 1's suppression was
simulable because another ceiling had already fired on all four of its cases. On real-01 and
real-05, rule 2 is the only rule that fired, so suppressing it leaves readiness unpinned and the
resulting level unpredictable without an actual run.

Settle, once ticket 17's numbers exist:

1. **Does rule 2 firing on every deck mean it is broken, or that student decks genuinely do fail to
   name the client's decision?** This is the honest fork and it is not rhetorical. Ticket 01's
   labeler independently wrote "not phrased as a question anywhere in the deck" into 7 of the 9
   input packs' client-question field. The rule may be reporting a real and near-universal property
   of the corpus. If so, firing 9 of 9 is correct behaviour and the defect is that a universal
   finding is being used to set a *comparative* readiness level.
2. **If it is broken, which limb?** "Decision is unclear", "does not answer the question" and "core
   recommendation is unsupported" are three different failures wearing one ceiling. They should
   probably not share a rule.
3. **Does a rule that fires on everything belong in a readiness ladder at all**, or does it belong
   as a standing finding every deck gets, outside the blocking mechanism?
4. Ticket 17 will show what rule 2 does once rule 1 is tightened and minors are reachable. Check
   first whether it absorbed rule 1's displaced findings before concluding anything about its
   own rate.

Answer records: whether rule 2 changes, which limb, and what a rule that fires universally is for.


---

**Input from [ticket 17](17-apply-the-three-ticket-16-fixes-and-verify-them-on-the-nine-cases.md) (resolved 2026-09-19). This ticket is now unblocked, and two of its premises have changed.**

**Rule 2 no longer fires on 9 of 9. It fired on 8 of 9** under `frozen-2026-09-19`. The deck it
missed is **real-13**, which fired 1 and 4. So the clause is not quite the universal it was
described as, and there is now one real deck on which its absence can be observed.

**It is still not simulable, and the reason got sharper.** Ticket 16 left rule 2 alone because
suppressing it on real-01 and real-05 leaves readiness unpinned. Ticket 17 then showed why that
reasoning cannot be rescued by arithmetic: **the counterfactual method was refuted on the four
decks it was applied to, and it failed precisely where it assumed a rule set would hold still
under an edited prompt.** real-02 silently swapped rule 4 for rule 2 while rule 1 kept firing.
Do not compute a predicted table for rule 2. Run it, or decide without a number.

**And there is a cheaper question to ask first.** Rule 2's ceiling is R1, and R1 is where this
prompt now puts **seven of nine decks**. Whatever rule 2 is doing, it is doing the same thing
almost everywhere, which is the property that made it invisible in the first place. Ask what
distribution of levels the set should have before asking whether rule 2 produces it.


---

**Parked 2026-09-20 by the owner, on the scope audit ([AUDIT-2026-09-20.md](../AUDIT-2026-09-20.md)).** Not cancelled and not out of scope: deferred until the pilot has run, at which point it is reconsidered against what the pilot actually showed.

Reason: **a live defect, parked knowingly** - blocking rule 2 fires on 9 of 9 decks and is unguarded. On the pilot path no rule number is emitted, so a student never sees it; it distorts the eval, not the product. Carried on the accepted-gaps list.
