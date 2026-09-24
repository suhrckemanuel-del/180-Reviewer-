# Retire the readiness level everywhere it appears

Type: grilling
Status: resolved
Blocked by: —

## Question

Decided at charting: no readiness level, for anyone. It is not important enough to carry and it is
the one component measured as untrustworthy — it returns R0 and R2 on identical bytes (A4).

The decision is made. What is not decided is the blast radius, and it is wider than it looks. The
readiness level is load-bearing in at least five places:

- The **renderer** (`index.html`) draws it, and a stop panel enforces that it cannot reach a student
  view, a printable or a student pack.
- The **override record** carries `readinessCall.ai` and `readinessCall.lead`, and the lead's own
  call is the single most valuable field in it — a human judgment with a consequence.
- **`22-trust-boundary.md`** defines stop conditions in terms of it.
- The **eval harness** scores `readinessWithinOne` as a headline metric, visible in
  `scores-log.jsonl`.
- The **gold labels** record an expected readiness per case.

Settle:

1. Does `readinessCall.lead` survive? It is the lead's judgment, not the AI's, and it is the
   calibration signal the corpus would rest on. Strong case for keeping the human half and deleting
   only the AI half.
2. What replaces `readinessWithinOne` as a headline eval metric, or does the harness simply lose one?
3. Which stop conditions in `22-trust-boundary.md` need rewriting, and does removing the level
   weaken or strengthen the boundary?
4. Do the gold labels get re-cut, or does the expected-readiness field stay as labeler context that
   nothing scores against?

Answer records: what is deleted, what is kept, and the rewritten stop conditions.

---

**Input from [ticket 03](03-recover-an-inter-rater-number-from-the-double-labelled-cases.md) (closed 2026-09-19).** Questions 2 and 4 now have a number to work against: two humans reproduce the gold's readiness on 2 of 4 double-labelled cases, 95% CI [7%, 93%], quadratic-weighted kappa below chance. `readinessWithinOne` is scored against a reference with a human noise floor around half. That is an argument for retirement that does not depend on A4, so the decision survives someone later stabilising the model.

---

**Input from [ticket 04](04-establish-what-the-bundle-can-do-on-a-free-account.md) (closed 2026-09-19).**
The blast-radius list above is missing two places, both of which put a readiness level in front of
a student on the free path:

- **`TEST-KIT/PASTE-2C-artifact-path.md` requires it.** `aiLevel` is a mandatory field of the
  `REVIEW` object and the template renders it as an "AI guess" pill in lead mode. This is the
  shipped HTML path, not a defect. Student mode carries no pill, so the leak is lead-mode only.
  Measured directly: on the same deck with the same bundle, gpt-5.6-sol returned "Needs targeted
  revision" and Haiku 4.5 returned "Nearly ready with minor edits" — the A4 instability
  reproduced across models rather than across runs.
- **The JSON fallback emits it whenever paste 2 truncates.** Losing the chat format drops the
  model onto paste 1's JSON branch, which carries the ten-dimension rubric, `diagnosticMean` and a
  readiness level. Observed on both Haiku arms that lost the format.

So retirement has to reach the paste-2C contract and the paste-1 OUTPUT block, not only the
renderer, the record, the harness and the golds. Question 1 (`readinessCall.lead` survives?) is
unaffected.

Note the direct collision with the map's settled "**No readiness level, for anyone**": the prose
path (2A) suppresses it deliberately and argues the case at length, while the HTML path (2C)
requires it. Two artifacts in the same shipped kit contradict each other today.

---

**Input from [ticket 16](16-decide-what-to-do-about-the-two-prompt-defects-the-baseline-exposed.md)
(closed 2026-09-19). This ticket's scope grows: the confidence label retires alongside readiness.**

The owner retired the confidence label on the same call. It is the same edit surface as readiness -
the output contract, the validator, the renderer, the chat-native format, the usage guide - so it
rides with this sweep rather than getting its own.

What is deleted: the confidence field on the readiness block and on the scorecard. What survives
untouched: the "what could change it" sentence, which carries the whole signal and is richly
case-specific on all nine real cases.

The evidence, which is stronger than the case against readiness: **confidence has never varied on a
real deck, under either of the two rules it has had.** Medium on 29 of 29 reviews before the
2026-08-08 short-circuit, Low on 12 of 12 after. Never High, never mixed, zero variance inside
either regime. It is structurally incapable of varying: High is forbidden by rule whenever evidence
notes are missing and they always are, Medium is guaranteed because quote-or-abstain already
requires what the Medium test checks for, and Low is a check on whether someone filled in a form.

Two consequences for the sweep beyond the obvious deletions:

- **The confidence readings in the evidence base are invalidated in both directions**, not just
  after August. The constant changed value on 2026-08-08 with nothing recording it, so any document
  comparing a reading from before that date with one from after is comparing two definitions. The
  full list of affected lines is in ticket 16's answer.
- **`11-decision-log.md:25` (2026-07-02) ends "Test: re-run both, expect Medium on both". That test
  was never run**, and the 2026-08-08 patch made it unrunnable. The decision log should say so.

Also found: three pre-patch reviews carry Medium on the readiness block and Low on the scorecard in
the same document. Two fields, one question, no rule saying they must agree. Neither survives, so
this resolves itself, but it is worth a line in the record.

## Answer (2026-09-19)

Five owner decisions, each taken against a stated case for the other side, plus two settled here.
The headline: **the readiness level is deleted as a thing the tool produces, and survives as a
thing the harness computes.** Those are different objects and the ticket was written as though
they were one.

Derivation evidence: [ticket-05-derive.md](../ticket-05-derive.md) (local only).

### The decisions

1. **`readinessCall.lead` survives.** The lead picks one of the four levels; the tool states none.
   Kept because it is the **only field in the record that is not a reaction to the tool's output** —
   `17-override-log.md` §5.1 names selection bias as the record's core weakness, and this is the one
   field that does not suffer it. *Case against, accepted:* it is also the one field ticket 03
   measured as weakly determined between humans (2 of 4, 95% CI [7%, 93%]), and **zero records exist
   today** — no `records/` directory, no filled instance anywhere in the repo, corroborated by
   `22-trust-boundary.md:23`. The decision is entirely prospective on both sides.

2. **`readinessCall.ai` and `readinessCall.delta` are deleted** from both record variants. `.ai` was
   already `null` on the shipped chat path (`CHAT-CONTEXT.md:391`); this makes the renderer agree.

3. **The harness keeps readiness, computed not emitted.** `readinessWithinOne`, `readinessExact`,
   over-flag and under-flag survive, scored against a **derived** predicted level: the lowest
   ceiling among the blocking rules the review reports. Never exported, never quoted standalone.

4. **Stop condition 3 widens** from "a student sees a readiness level" to "**the tool produces a
   readiness level, for anyone**". Two shipped artifacts become violations on the day this lands
   and two trust-boundary rows go red. *Case against, accepted:* a row that is red on purpose,
   waiting on a scheduled fix, teaches people to stop reading red rows, and this document's only
   value is that its rows mean something.

5. **The lead's reason line is unconditionally required.** The old trigger — required when the lead
   differs from the AI — cannot fire once the AI has no opinion, and on the chat path it never
   could. *Case against, accepted, and flagged to the owner as the answer most worth unwinding:*
   ticket 10's stated constraint is that anything over two minutes will not survive a volunteer's
   week, and mandatory free text is the most reliable way to make a form get abandoned or filled
   with "looks fine". If record volume disappoints in the pilot, **unwind this first.**

6. **Settled, not asked: the gold labels are not re-cut.** All eleven keep `## Expected readiness`.
   Under decision 3 the field is not vestigial — it is the reference the derived level is scored
   against, and it also feeds over-flag and under-flag, which need the gold label rather than the
   product feature (`score-review.js:288-293`).

7. **Settled, not asked: the corpus's gold-sampler trigger is re-specified.** `28-shared-corpus.md`
   :188-194 points expert labelling attention at "a record where the lead moved readiness two
   levels" — a delta that no longer exists. Replacement trigger: **`cutReason: wrong`, or an
   `added[]` entry at `severity: critical`.** Both are already collected, the first is what
   `17-override-log.md` calls the one field to build if only one gets built, and the second is stop
   condition 1's own detector.

### The derivation, measured

`PASTE-1-system-prompt.txt:167` already defines the level as arithmetic: the lowest ceiling among
the blocking rules that fired. That is testable against what the model actually emitted.

| run | prompt | derived == emitted | cases with no rule fired |
|---|---|---|---|
| 2026-07-29 | `frozen-2026-07-26` | **9/9** | 0 |
| 2026-08-02 | `frozen-2026-08-03` | **8/9** | 1 |
| 2026-09-18 | `frozen-2026-08-09` | **9/9** | 0 |

**26 of 27.** The single miss is the entire limit of the method: real-13 under `frozen-2026-08-03`
was the one review in twenty-seven where no blocking rule fired, so the prompt's discretionary
demote applied — and it demoted correctly, to gold. **On the one case where arithmetic and judgment
disagreed, judgment won, on a holdout.** Record the limit plainly: *the derived level is void on any
deck where no blocking rule fires, and it gets blinder as the decks get better.*

This is not a new instrument. **Ticket 16's predicted table — exact 33.3%, within-one 100%,
over-flag 44.4% — was itself computed by this arithmetic on recorded blocking issues.** The project
has already staked a pre-registered falsifiable prediction on the derivation; this ticket only
names it and measures its error rate.

**A correction that rides along:** ticket 16 established that over-flag and blocking false positives
are the same six cases. Under decision 3 both are computed from blocking issues. **They are one
metric and must stop being printed as two corroborating rows.**

### What is deleted

| where | what | note |
|---|---|---|
| `TEST-KIT/PASTE-1-system-prompt.txt` | the level assignment at :167, the no-blocker default and discretionary demote at :169-181, `readiness` from the OUTPUT block | **the five blocking rules and `blockingIssues[].rule` stay** — A1 needs them and so does the derivation |
| `TEST-KIT/PASTE-2C-artifact-path.md` | the mandatory `aiLevel` field (:42), its derivation rule (:96), the "AI guess" pill (:216) | this path has **no redaction and no stop panel**, and the same template renders student mode |
| `03-output-contract.md`, `check-review-v2.js` | the `readiness` level field | lands with ticket 16's confidence deletion, same files |
| `index.html` and `site/index.html` | `aiLevel()` / `delta()` (:968-969), the "AI guess" option in the lead picker (:1679-1683), the AI-guess tile sub-line (:1282-1292), `readinessCall.ai` and `.delta` in `buildRecord()` (:1830) | the lead's own picker **stays** |
| both record variants | `readinessCall.ai`, `readinessCall.delta` | shape change, so `recordVersion` bumps to `override-log-3` / `override-log-3-chat` |
| `scorecard.js` | the readiness lines in `renderShareable()` (:223-234) | the export lock decision 3 depends on |

### What is kept

`readinessCall.lead` and its now-mandatory `reason`; all eleven gold `## Expected readiness`
sections; the five blocking rules and the reported `blockingIssues`; the outbound scan, student-pack
redaction and `MutationObserver` stop panel (`index.html:1100-1168`), widened per decision 4; and
readiness inside the harness, derived.

### The rewritten stop condition 3

> **3. The tool produces a readiness level, for anyone.**
>
> *How it is caught:* the contract validator rejects any review carrying a readiness level field at
> all — the check moves from "was the student pack redacted" to "was a level produced". The outbound
> scan runs on every view and every export, not only student-facing ones. The `MutationObserver`
> attaches to the lead view as well as the student and print views. **The artifact path has none of
> this today and does not ship until it does.**
>
> *Who acts:* the stop panel names this condition and says the fix is to re-run the review, never to
> edit it. Unchanged.

**Does removing the level weaken or strengthen the boundary? Strengthen, and the document already
knows why.** §1a argues that the chat path's control moved "from redaction to non-production", and
that nothing fenced means nothing forwardable past a fence. Decision 4 extends that from one route
to every route. The one genuine loss is §3's honest in-product hedge — the "AI guess / Unstable"
chip told leads the number could not be trusted — but deleting the number deletes both the warning
and the thing warned about, which is net stronger.

**Two rows go red on the day this lands**, and that was accepted knowingly:

- `22-trust-boundary.md:22` (whole project team) — **MET -> NOT MET** until the artifact path's
  `aiLevel` and the JSON fallback stop emitting a level.
- `:21` (pilot lead) — its clause "Readiness never preselected, a written reason required to differ"
  is rewritten to "the tool states no level; the lead's own call is required, with a written
  reason", and it is **NOT MET** until the picker's AI option is removed.
- `:25` (chat path) stays **MET by construction** and is unaffected.
- `:24` (another branch) loses its "readiness exact-match reported with its spread" bar. That bar's
  replacement is ticket 07's, not this ticket's.

### Sequencing, and it is not optional

**Ticket 17 must run before the prompt-side deletion lands.** Ticket 17 verifies ticket 16's
pre-registered prediction, and that prediction is stated in readiness metrics. Ticket 17 says
explicitly that it is not blocked on this ticket and expects only the minimum confidence change.
So this ticket's edits split:

- **Land now:** the record changes, the renderer changes, the doc sweep, the widened stop condition,
  the derived scorer in `score-review.js`.
- **Land with or after ticket 17's verification run:** the deletion of the level from
  `PASTE-1-system-prompt.txt`, `03-output-contract.md` and `check-review-v2.js`.

Deleting the emitted level before ticket 17 runs would destroy the only pre-registered falsification
test this project has.

### Documents that assert something now false

- `26-chat-native.md:262` — says the pilot query joins `readinessCall.ai` against `readinessCall.lead`.
  Already false on the path it describes; now false everywhere.
- `17-override-log.md:209` — rates `readinessCall` a **full match** for the gold worksheet's
  "Expected readiness", the only row rated full match with no caveat. The record no longer carries
  the AI side, and ticket 03 measured the human side at 2 of 4. Downgrade it.
- `17-override-log.md:132-134` — the `delta != 0` trigger. Replaced by decision 5.
- `17-override-log.md:148-149` — the "already free in the UI" table lists `readinessCall.delta`.
- `28-shared-corpus.md:188-194` — "calibrating readiness" as a flywheel benefit, and the
  two-level-move sampler trigger. Replaced by decision 7.
- `22-trust-boundary.md` §3 — the in-product warning's dose, describing a chip that will not exist.

### What this does not settle

The artifact path's rewrite is **ticket 13**, which was blocked on this one and is now unblocked —
a `PASTE-2C` without `aiLevel` is an untested artifact and somebody has to run it. The gate's
replacement bar for row `:24` is **ticket 07**. Whether the two-minute form survives a mandatory
reason line is **ticket 10**, and decision 5 is the first thing it should re-examine.


---

**Correction from [ticket 17](17-apply-the-three-ticket-16-fixes-and-verify-them-on-the-nine-cases.md), 2026-09-19. The derivation survives. One sentence about it does not.**

The derivation was re-measured on `frozen-2026-09-19`, a prompt version it had never seen:
**9 of 9, zero no-blocker decks. Total now 35 of 36.** Decision 3 stands and the harness keeps
readiness.

**But ticket 16's prediction, computed by this same ceiling table, was refuted** - two of its
three numeric rows did not move at all. The answer above says "this is not a new instrument:
ticket 16's pre-registered prediction was computed by exactly this arithmetic", offered as
reassurance that the derivation was already load-bearing. **Read today it cuts the other way,
and it should be read as scoped rather than withdrawn.**

The two uses are not the same operation. They share the ceiling table and differ in what feeds
it. This ticket feeds it **the blocking rules a review actually reported**, which is a
consistency claim about output that exists. Ticket 16 fed it **rules it assumed a future run
would report**, which is a forecast. The forecast failed on the assumption, not on the table:
real-02 fired rules 1 and 4 before the edit and 1 and 2 after, so the ceiling the counterfactual
relied on was not there to be found.

**The rule going forward: this derivation scores runs that exist. It does not predict runs that
do not.** Nobody may compute a predicted scorecard from it again.

Also touched by ticket 17, as that ticket's step 1 permitted: the confidence label was deleted
from `03-output-contract.md`, `check-review-v2.js` and the `run-reviews.js` response schema.
**Readiness was not touched in any of the three**, per the sequencing constraint above, so the
prompt-side deletion this ticket owns is still entirely ahead of you. `04-prompt-templates.md`
section A and `TEST-KIT/PASTE-1-system-prompt.txt` are still byte-identical to each other and
both now sit at sha `757a38ac6a14287b`, which is the sha your edits start from.
