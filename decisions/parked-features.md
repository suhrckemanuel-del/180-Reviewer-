# Parked features

Ideas ruled out of the current route but worth reconsidering later. Nothing here is a commitment.

| feature | why it was parked | what would have to change to revive it |
|---|---|---|
| **AI-drafted fixes, communication axis only** (slide titles, wording, chart labels — never the governing insight or recommendation logic) | Decided 2026-09-18: no drafting at all. It breaks "teach, do not ghostwrite", and "the human must visibly edit" is unenforceable — a cosmetic edit is undetectable. | **Partly revived 2026-09-20 — see the amendment below.** For the rest: evidence that the attempt gate alone leaves the weakest consultants stuck, plus a mechanism that can actually detect whether a draft was engaged with rather than accepted. |
| **Readiness level / overall score** | Retired as not important enough to carry, and measured untrustworthy (R0 and R2 on identical input). | A calibration instrument that holds on repeated runs of the same bytes, and a decision that actually depends on the grade. |
| **Hosted page** | Not the product. The tool is a prompt plus context bundle. | A population that cannot run a prompt themselves and still needs the tool. |

---

## Amendment 2026-09-20: the worked example

**The owner moved the "no drafting" line, deliberately, and this records where it now sits.**

He read the first review off the shipped configuration and said the information was valid and
aligned with the philosophy but **was not converting to something applicable**. Shown a hand-rewrite
that ends each finding with a worked example — *"Aim for a line like: 'Comparable arts non-profits
convert 5-12% of their mailing list. We assumed 8%, mid-range, and the soft launch tests it.'"* —
he approved the direction: *"I really do like this approach to teaching them."*

**What is now in scope:** an example sentence showing the *shape* of a good answer, built from
**invented numbers**, attached to the finding it makes actionable.

**What is still parked:** everything in the row above. The reviewer does not write the student's
slide, their title, their wording or their chart labels.

**The distinction the amendment rests on, and it is not yet settled:** an example built from
invented numbers is a **target** — the student cannot paste it, because they still have to go and
find the real figure. An example built from their own numbers is a **draft**. That line was
proposed by the session that raised this, it has not been measured, and
[ticket 26](issues/26-rewrite-the-finding-for-a-student-who-has-to-act-tonight.md) has to settle it
precisely enough for a model to apply and a reader to audit. **Until it does, this amendment is a
direction, not a rule.**

**Why the original decision is not simply wrong.** It was made against a real failure: "the human
must visibly edit" is unenforceable, because a cosmetic edit is undetectable. The worked example
does not solve that — it sidesteps it, by giving the student something they *cannot* edit into
their deck without doing the work first. If ticket 26 cannot hold that distinction in the prompt,
the original objection applies again in full and this amendment should be withdrawn rather than
weakened.



---

## Amendment WITHDRAWN 2026-09-24, by measurement

**The worked example is out of the prompt.** The amendment above stood on a distinction it asked
[ticket 26](issues/26-rewrite-the-finding-for-a-student-who-has-to-act-tonight.md) to settle
precisely enough for a model to apply and a reader to audit. The distinction turned out to be
statable and auditable -- **a reader can run it in ten seconds** -- and **a model will not hold it
reliably.**

The settled rule, kept here because it is correct and a later attempt should start from it rather
than reinvent it: *an example is a target when the conclusion inside it is controlled by a figure
the deliverable does not yet contain.* Audit it two ways -- strike the invented values and what is
left must have a hole where the evidence goes; change an invented value and the conclusion must
change with it.

**Three templates, twenty-six runs, two model families.** The device works on one family and not
the other, and no wording tried moved that:

- round 1 (self-audit): Codex 6 of 10 findings, all passing both tests; Haiku 2 of 10, one of the
  two asserting *"making 8% conservative"* regardless of what the student finds.
- round 2 (trigger tied to `Answer first`, conditional form): Codex **0 of 9**; Haiku 10 of 11 but
  as a conditional shell with drafts inside it.
- round 3 (round-1 trigger plus conditional form, pre-registered bar of zero conclusion-asserting
  examples): **failed 3 of 10**, one of them the harmful kind.

**The deciding evidence was collateral.** `Do this:` -- a field with no exception and no licence --
produced finished pasteable sentences, including one built entirely from the team's own numbers.
The original objection to AI-drafted fixes was that *"the human must visibly edit"* is
unenforceable because a cosmetic edit is undetectable. A finished sentence in `Do this:` needs no
edit at all. **The objection returned in full, which is the condition the owner set for
withdrawing rather than weakening.**

**Honest limit on the withdrawal.** Removing the example did not remove the leak: Haiku still
produced pasteable parentheticals in `Do this:` with nothing licensing them, three across two
arms. The amendment **aggravated** that defect; it did not create it. So the withdrawal is not a
fix for drafting, and the remaining leak is tracked separately.

**What would have to change to revive it:** a way to make the audit hold on the weaker family, or
a pilot population known to be on a model that holds it. Evidence is in
[ticket-26/RESULTS.md](ticket-26/RESULTS.md); the three templates are recoverable from the run
directories.
