# Ticket 10 working findings — the consultant feedback loop

Written 2026-09-20 while the ticket was claimed. Evidence only; the decisions are the three
questions put to the owner, and the resolution goes in the ticket.

## 1. The state of the two sides, checked rather than assumed

**Zero override records exist.** Both the lead side and the student side are prospective. Nothing
in this ticket may assume records already flow.

**The lead instrument is already specified and already has a capture surface on the product path.**
`TEST-KIT/PASTE-2A-chat-path.md:348` emits a `=== PASTE-BACK RECORD ===` block —
`override-log-2-chat`, every field `null`, filled by hand and sent back. It claims "Two minutes".
That is the whole of the live loop today.

**The UI the record spec was written against is out of scope.** `17-override-log.md` §3 and §4
are written against the Triage Desk in `index.html` — six fields free from the interface, and
§4.1's fix for manufactured agreement (`triage[i] = 'keep'` and the readiness picker pre-set to
the AI's call) is a *UI* fix. The map rules the hosted page out of scope. So:

- §3's "six of the record's fields need no new interface" is **void on the product path**. On the
  chat path every field is typed by a human.
- §4.1's failure mode is **not present** on the chat path, and for a good reason: the paste-back
  block ships all-`null`, so there is no default to mistake for an endorsement. The chat path is
  *better* on the anchoring-by-default axis and *worse* on the abandonment axis. Same bias, moved.
- §4.2 (`added[]`, what the AI missed) and §4.3 (`mustCatch`) are present in the paste-back block
  already. `added: []` ships empty, which is the field §4.2 itself names as most likely skipped.

## 2. The finding that decides the student side: the attempt gate is not on the product path

The map records **"Attempt first, always. Nothing unlocks until the consultant has committed their
own read"** as settled while charting. Checked against the artifacts:

| artifact | attempt gate |
|---|---|
| `PASTE-1-system-prompt.txt` | **absent** — no match for "attempt" in any relevant sense |
| `PASTE-2A-chat-path.md` — *"this is the product"* | **absent**. The only "attempt" is line 329, "the question the team answers before they attempt the fix", which is output content, not a gate |
| `PASTE-2B-json-contract.md:154` | present — "the student view shows the coaching-shaped findings with the typed-attempt gate" |
| `TEST-KIT/README.md:20` | present, as an instruction **to a tester**, with a box in `FEEDBACK.md` |

So the gate is a property of the **HTML renderer**, which is ticket 13's still-open default, and of
the test kit's protocol for testers. On the default chat path the review arrives in one reply and
there is nothing to unlock. **The settled decision is not implemented on the path the product
actually is.**

This is load-bearing for question 2. The attempt is the only thing a student produces that is not
a reaction to the tool — the same property `17-override-log.md` §5 and ticket 05 identify as what
makes `readinessCall.lead` worth keeping. It cannot be used as an instrument until it exists.

**And the record has no field for it.** The paste-back block is lead-shaped throughout (`lead.id`,
`lead.vsByHand`, `readinessCall.lead`). There is no student, no attempt, and no student-side record
of any kind anywhere in the system.

## 3. Selection bias: the response rate is not the problem, the denominator is

The ticket names the trap correctly — a five-minute form is filled by the conscientious. But the
sharper statement is that **non-response has a known direction**. A consultant who skips is
disproportionately one who was rushed, did not engage, or found nothing useful. Every one of those
is a negative signal. Returned feedback is therefore a **systematic upper bound** on the tool's
value, not a noisy estimate of it.

That makes the usual mitigation — chase the response rate with reminders, or make it mandatory —
the wrong move twice over: it converts a known-direction absence into "looks fine" text of unknown
direction, and mandatory free text is exactly what the ticket's own cost constraint forbids.

The mitigation that survives is to **make non-response countable**, which requires a denominator:
how many deliverables existed, not how many forms came back. **Today the denominator is
unobtainable.** The chat path has no telemetry of any kind — a student can run the reviewer twenty
times and leave no trace, and the paste-back record is the only artifact, which means the record
count *is* the response count and the two can never be separated. A response rate cannot be stated
from inside the instrument that is being responded to.

This is the same family as the map's standing caution: a measurement taken through the thing being
measured. Stated in the caution's own terms — the two sides are "reviews that happened" and
"records returned", and today the second is the only observer of the first.

The only available second observer is the lead, who knows what their team produced and does not
need the tool to know it.

## 4. What the release gate can be, given there isn't one

Ticket 14 took the gating eval off the critical path, so "feedback routes through the release gate"
names a thing that does not exist. What *does* exist, demonstrated end-to-end by ticket 17: patch
the prompt to a new frozen sha, regenerate packs, run the nine cases blind, file the scorecard.

Its known weakness, which must be stated wherever it is used: the golds behind it have an
inter-rater agreement of 2 of 4 with a 95% interval of [7%, 93%] (ticket 03), over-flag is coarse
and counts membership not distance (ticket 17 §4), and the comparison ticket 17 ran was
**uncontrolled** because neither prior baseline recorded the reviewer model. It is a change-detector,
not a quality bar.

## 5. Cost accounting, stated against the ticket's two-minute constraint

| instrument | added cost | rides on work already happening |
|---|---|---|
| lead paste-back record | claimed 2 min, **never timed on a human** | yes — the triage |
| `readinessCall.lead` reason, now unconditionally required (ticket 05) | free text, always | no — added by ticket 05 against this ticket's stated constraint |
| a student feedback form, 4 questions | ~3-5 min | no |
| a typed attempt | ~2 min | **yes if the gate ships** — it is the pedagogy, not a form |
| attempt-vs-review overlap | 0 min to the student | computed afterwards |

The "two minutes" on the paste-back record is a claim in the template, not a measurement. Nobody
has filled one in.

## 6. A caution on the overlap measure, before it is proposed

If attempt-vs-review overlap is scored by a model, the two sides are the student's attempt (written
before the review) and the review (generated from the deck). **Neither saw the other**, so the
measure clears the standing caution on its input side. It does not clear it on its judge side:
ticket 14 measured a fresh draw of the pair judge agreeing with its own earlier majority on 86.7%,
with 5 of 6 disagreements against a unanimous verdict, and the cache storing no model id. Any
overlap number must record the judge model and must be reported as a band, not a figure.

Separately: convergence of attempts over a term is confounded by the student simply improving over
a term. Without a comparison group it evidences nothing about the tool. Designing that comparison is
pilot design, not this ticket.
