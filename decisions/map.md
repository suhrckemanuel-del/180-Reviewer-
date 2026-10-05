# Map: the deliverable reviewer as a real tool

> **Historical / superseded:** this 2026-09-18 map is retained as decision history. The
> 2026-09-30 [project plan](../PROJECT-PLAN-2026-09-30.md) is the current source of truth.
> For the current build, owner design approval and remaining release work, read
> [CURRENT-MAP.md](../CURRENT-MAP.md), updated 2026-10-05 against GitHub issues #1–#5.

Label: `wayfinder:map`
Charted: 2026-09-18

## Destination

**The decisions and spec needed to put the reviewer in front of one pilot cohort of 180DC
students and team leads, running on real engagements, in a usable state.**

The map is done when nothing is left to decide and a build session can execute.

**Redrawn 2026-09-19 by the owner, during ticket 14.** The destination previously also required
"an eval loop that gates prompt changes and shows each student their own trajectory". **The gating
eval comes off the critical path.** Manuel's reasoning: the comparisons built so far have not
changed a decision, the real comparison arrives when people use the tool and the output is read by
a human and by AI agents, and usability is the priority. Ticket 14 supports him from the other
side — with the matcher unusable, every number left on the scorecard measures the readiness level,
the component ticket 05 retires, so the gate would police a feature being deleted.

What this does **not** mean: the gate is not out of scope, it is later, and ticket 07 stays open
with its permitted contents now constrained. The student-trajectory eval (ticket 06) was not part
of this decision and is untouched.

**Where the map stands, 2026-09-20, end of day.**
[Ticket 25](issues/25-name-the-pilots-minimum-shippable-set.md) named four preconditions for the
pilot: **20, 12, 21 and 09. All four are now resolved**, and so is ticket 22, which was never a
precondition. **The map reached its destination for the pilot path** — and the owner extended it the same
evening, see below. Ticket 11 is claimed by another session and is not blocking.

**Extended 2026-09-20, after the build, by the owner.** He read the first review off the shipped
configuration and made two calls that put decisions back on the map:

- **The output does not convert.** The findings are right and a student could not act on them.
  That was [ticket 26](issues/26-rewrite-the-finding-for-a-student-who-has-to-act-tonight.md),
  **closed 2026-09-24. The register change ships; the worked example is withdrawn** and the "no
  drafting" line is back where it was at charting -- see
  [parked-features.md](parked-features.md). It surfaced two defects it did not fix,
  [ticket 28](issues/28-stop-do-this-handing-over-pasteable-text.md) and
  [ticket 29](issues/29-the-interlock-false-alarmed-on-a-complete-bundle.md).
- **He wants the HTML output.** [Ticket 13](issues/13-decide-the-default-output-path.md) was
  unparked — does the artifact path get reached at all, and how — and
  [ticket 27](issues/27-bring-the-artifact-path-level-with-the-prose-path.md) is the build behind
  it. **13 closed the same evening and did not cancel 27; it changed its shape.** The page becomes a
  **re-print** of the review the prose path already produces, carrying no content rules of its own,
  with the verdict row deleted. **27 is now blocked by 26 alone** and 26 is the frontier.

**Sequencing that is not a preference:** 26 before 27. Ticket 26 settles the shape of a finding and
the artifact path renders findings, so building 27 first means building it twice.

**Audited 2026-09-24** at the owner's request: [AUDIT-2026-09-24.md](AUDIT-2026-09-24.md). It finds
**one true hard stop** (the Drive folder, which `--release` refuses without), that **ticket 20's
verification is now stale** because ticket 26 changed paste 2 after it ran, and that the pilot's
start date is blocked on naming a cohort rather than on any software.

**What is left of the original destination is not a decision, it is two errands**, both recorded in
ticket 20's answer:

1. **Re-run the Codex arms.** The shipped gate branches by audience, so ticket 21's "16 of 16" did
   not carry over and had to be re-measured. It was, on Haiku 4.5, 6 of 6 — and Codex hit the
   account's usage limit before a single arm ran. One family is not two.
   `bash ticket-20/run-codex.sh`, then `python ticket-20/score.py`.
2. **Create the Google Drive folder and set `DRIVE_FOLDER_URL`.** Its link is printed inside every
   bundle, in the refusal a student sees when their paste was cut, so it cannot be added afterwards
   to copies already issued. `build-bundle.js --release` refuses until it is set.

**No release may be cut until both are done**, and until one is, nothing today's build changed is
in anybody's hands. That is structural rather than a promise: the prompt sources now carry
placeholders and are not pasteable, so the standing hazard this map carried all day — that editing
section A of `04-prompt-templates.md` ships to the pilot with no decision and no record — is closed.

## Notes

**Domain.** 180 Degrees Consulting: a global student-run pro bono consultancy. No seniors, total
turnover inside three years, real clients and real boards. The realistic alternative to this tool
is no substantive review at all. See [CONTEXT.md](../../CONTEXT.md) and
[tools/quality-reviewer/v2/STATUS.md](../../tools/quality-reviewer/v2/STATUS.md).

**Skills every session should consult.** `grilling` and `domain-modeling` by default. `research`
for anything outside the working directory. `prototype` where the question is "how should this
behave".

**How to ask Manuel a question — [asking-rule.md](asking-rule.md), added 2026-09-19 during ticket
14.** He agreed with three dense recommendations in a row and then said he could not follow them
well enough to disagree. A question he cannot argue with is not a decision, it is a rubber stamp,
and that is the same self-confirming error this map already guards against elsewhere. Every
question carries the best honest case *against* the recommendation, plain words, no code
identifiers, three per round.

**Plan, do not build** — with two exceptions, both carried deliberately. First, `task` tickets that
generate numbers other decisions are blocked on: tickets 01, 02, 03, 11 and 17. Second, and added
2026-09-20 on the owner's call, **[ticket 20](issues/20-apply-the-accumulated-edit-lists-to-the-product.md)
ships changes** — because the map had no way to reach its own destination. Every resolved ticket
produced a decision and none of them changed the product; tickets 05 and 16 closed into edit lists
filed as "executable spec for a build session" that no ticket owned. Ticket 19 owns them, decides
nothing, and routes anything underspecified back to its source ticket. **When 08, 09, 12, 13 or 21
closes, append its edits to ticket 20 rather than creating another execution ticket.** Ticket 10
closed that way on 2026-09-20, and it also shows the routing rule working: it named the attempt gate
as an edit, then pulled it back out because its placement was a live decision, and ticket 20 carries
an explicit instruction not to build it from ticket 10's description.

**Added 2026-09-20, and it reframes every metric on this map.** **Zero of the thirty-six reviews on
record ran the path the pilot ships.** All of them ran the harness path; the pilot runs the
three-paste chat path. And it is structural rather than an oversight: `CHAT-CONTEXT.md:400` forbids
the chat path from emitting a blocking rule number, while `score-review.js:535,587` needs exactly
that field, so **the derived readiness scorer cannot read the product at all** — nor can blocking
rules missed or blocking false positives. Four of the seven metrics ticket 07 was going to gate on
are unavailable on the product path. Severity, quote fidelity and findings count survive, which is
now the strongest argument for ticket 15's severity-distribution proposal. This is
[ticket 24](issues/24-decide-how-the-path-that-ships-gets-measured.md) and it does **not** invalidate
the nine-case work, which measured the shared system prompt and caught real defects.

**Standing caution, added 2026-09-19 after ticket 03.** This project has now produced the same
error twice by two different mechanisms, three days apart: **a number that measures something
against a copy of itself.** First the "kappa 0.971" that was one opinion duplicated; then
`_LABELING-RECORD.md` describing a straddle the owner resolved *while knowing* the second reader's
answer as an independent concordance. Before any agreement, accuracy or validation figure enters a
document, state explicitly what the two sides are and whether either saw the other. The pattern is
worth more attention than either instance.

**Extended again 2026-09-19 after ticket 17, and this one is about predictions rather than
figures.** Ticket 16 computed what a prompt change would do by arithmetic over recorded blocking
issues, assuming the model changes nothing else when one rule is tightened. **It changed other
things, on a case that shows it, and two of three numeric rows did not move at all.** The rule to
carry: **a counterfactual over a model's output is not a measurement and must not be entered in a
table beside one.** State what would have to be true for it to hold, then run the thing. And note
the honest limit on this caution itself, which ticket 17 also demonstrates: the reflex to treat two
numbers as one copy is right often enough to be a standing rule, and it was **wrong here** -
ticket 05's derivation and ticket 16's prediction share a ceiling table and nothing else that
matters, and the run separated them. Check before merging two things, in that direction too.

**Extended 2026-09-19 after ticket 16, and the family is wider than "agreement" figures.** The
scorecard's over-flag rate and blocking-false-positive rate are computed from **the same six
cases** and have been read as two metrics agreeing. Same error, no human involved and no
agreement figure in sight: **a number presented as corroboration that is a copy of the thing it
corroborates.** Add the second half of the check — before any two figures are set side by side as
mutually supporting, state what would have to happen for one to move without the other.

**Settled while charting** (destination-shaping, not ticket resolutions):

- Both students and team leads are users, asymmetrically. Leads contribute review records; students
  use the tool and never touch the repo. The premise is not whether students use AI — they already
  do — but whether they use it at a level that builds them.
- **No drafting.** The reviewer surfaces findings and the consultant writes every word. An
  AI-drafted fix, even scoped to communication only, is parked — see Out of scope.
- **Attempt first, always.** Nothing unlocks until the consultant has committed their own read.
  Ticket 10 found it was **not in the product** and the hosted page that held it was withdrawn on
  2026-09-20, so it existed nowhere a user could reach.
  **[Ticket 21](issues/21-decide-where-the-attempt-gate-lives.md) settled where it is built, and
  it is spec now, not a decision** — top of paste 3 and top of paste 1, refusal on absence, no
  word count the model enforces, a one-sided marker on line 2. Ticket 20 Group E owns the build.
  **Settled 2026-09-20 by the owner, twice: students type, leads do not.** One bundle serves both,
  so the gate is conditioned on the mode. Built as one named switch with one documented default,
  `ATTEMPT_GATE_AUDIENCE` in `build-bundle.js`, so flipping it to "everyone types" is a single edit
  in a single findable place. Ticket 09 resolved this the other way by inference from a remark the
  owner had already withdrawn; its HANDOVER §5.5 is corrected. **The branch is not free:** it is
  reachable by anyone who selects lead mode, which is an accepted gap rather than a solved one, and
  it made ticket 21's "16 of 16" a measurement of a different prompt, so the shipped gate had to be
  re-run. See ticket 20's answer, section 4.
- **No readiness level, for anyone.** Judged not important enough to carry, and it is the one
  component measured as untrustworthy (returns R0 and R2 on identical bytes).
- **No hosted page.** The tool is a prompt plus a methodology context bundle plus the deliverable,
  producing an output the consultant reads. HTML rendering is wanted but must stay optional.
- **Evals must change a decision.** Two survive that test: gating prompt releases, and showing a
  student their own trajectory. Telling a lead how much to trust one review does not — that was the
  readiness level's job and it failed.
- Success bar for the pilot: findings kept rather than cut, and no stop condition tripping.
  Convergence of student attempts toward the reviewer is the prize. Whether the client got a better
  deliverable is the defensible outcome, and nobody has said yet how it would be measured.

## Decisions so far

<!-- one line per closed ticket -->

- [Rewrite the finding for a student who has to act on it tonight](issues/26-rewrite-the-finding-for-a-student-who-has-to-act-tonight.md):
  **the register ships and the worked example is withdrawn.** Findings now carry a plain title,
  `The problem:`, `Why it matters:`, `Do this:` and `Answer first:`; **lead mode is untouched** on
  the owner's ruling, and `THE HABIT TO BUILD` is **deleted** -- his call, with the teaching moved
  inside the findings rather than restated under them. **The 90-word overrun that opened the ticket
  is fixed by splitting the field, not by restating the budget** -- and the stated 40 words was
  *wrong*, not merely ignored: three hand-written rewrites in the target register landed at 58, 53
  and 49. That is the one mechanism result clean across every round and both families.
  **The amendment is withdrawn by measurement, on the owner's own pre-set condition.** The
  target-versus-draft rule was settled and *is* auditable -- an example is a target when the
  conclusion inside it is controlled by a figure the deliverable does not yet have, checkable by
  striking the invented values and by flipping them -- and the blunt version on the ticket would
  have **forbidden the object the owner approved**. But no model holds it: three templates,
  **twenty-six runs, two families**, Codex swinging 6 of 10 -> 0 of 9 -> 7 of 10 on wording alone
  while Haiku never produced a reliable one, against a **pre-registered** bar of zero
  conclusion-asserting examples that failed 3 of 10. **The deciding evidence was collateral**:
  `Do this:`, a field with no exception, handed over finished pasteable sentences including one
  built entirely from the team's own figures -- the original "the human must visibly edit is
  unenforceable" objection returning verbatim, since finished text needs no edit. **And that leak
  survives the withdrawal**, milder, on Haiku only, so the amendment aggravated a defect it did not
  create; the session's own causal claim is corrected in the record rather than left standing.
  Two defects raised and not fixed: [ticket 28](issues/28-stop-do-this-handing-over-pasteable-text.md)
  and [ticket 29](issues/29-the-interlock-false-alarmed-on-a-complete-bundle.md) -- **the shipped
  truncation interlock refused a complete, byte-identical bundle once and reviewed it on re-run**,
  against ticket 12's 0 of 14. Paste 2 costs **+383 tokens, +6.2%**. Nothing is released.
  [RESULTS.md](ticket-26/RESULTS.md), [REWRITES.md](ticket-26/REWRITES.md).

- [Decide the default output path, HTML or prose](issues/13-decide-the-default-output-path.md):
  **the artifact path is reached, and it stops being an output path — it becomes a re-print of the
  review the prose path already produced.** Prose stays the default; the page is an optional extra,
  **both audiences**, reached by an extra paste after the review has arrived. *Retire* was live and
  was not taken; **"second reviewer, prettier" — which is what the file is today — was rejected.**
  `PASTE-2C-artifact-path.md:3` opens *"It replaces the JSON output that prompt asks for"* and then
  restates every content rule for itself; under this decision it carries **none**, and that rewrite
  is the largest item in ticket 27 and an item 27 did not have. Three of the ticket's four questions
  fall out of one owner sentence: same page for leads and students, and **the render-failure
  fallback is answered by construction** — the review is already in the chat above the page. **The
  verdict row is deleted** on his *"we don't need verdict, we already just have list of errors"*,
  including the lead's own "Your call" box, a named and accepted cost. **That answers stop
  condition 3 by construction rather than by guard:** 27's *item with no precedent* shrinks from an
  unbuilt no-level instrument to an **absence check on the box row** — and shrinks, does not vanish,
  because a grade can still reach a heading. Question 2 is **maintained**, and since he called drift
  *"not really important"* the drift answer is **filed as spec on 27, not as his decision**: the
  re-print is most of the defence because the page holds no copy of anything, but 2C is still not
  one of `build-bundle.js`'s three sources and is mentioned by no check, the exact state the two
  stale derivatives were in — **`--check` is the mechanism that exists and item 7 is not optional.**
  **Limits: the re-print has never been run, zero measurements**, and **ticket 04's "both families
  rendered it first try" does not transfer** — it measured the design being replaced. The design
  also introduces a failure the old one did not have, **the model rewriting the review while
  presenting it as a re-print**, which nothing checks and 27 must test first.
  [ANSWER.md](ticket-13/ANSWER.md).

- [Apply the accumulated edit lists to the product](issues/20-apply-the-accumulated-edit-lists-to-the-product.md):
  **all six groups landed. This is the first ticket on this map that changed something a user would
  notice, after twelve that did not.** The readiness level is gone from the prompt, the contract, the
  artifact path and both record variants, and the validator now *rejects* one rather than validating
  it; the truncation interlock, the attempt gate and ticket 22's count line are built; `build-bundle.js`
  makes the pasteable bundle a generated artifact with a key pair and a register. **The audience branch
  is one named switch**, `ATTEMPT_GATE_AUDIENCE`, default `students`, and ticket 09's HANDOVER §5.5 is
  corrected where it resolved this the other way by inference. Verified **6 of 6 on Haiku 4.5** —
  the gate refuses a student who typed nothing and one who argued back, lead mode goes through on
  byte-identical input, the truncation check still fires, the review's shape is unchanged.
  **Half the verification is missing: Codex hit its usage limit before any arm ran, and no release
  may be cut until it has.** Two rows of `22-trust-boundary.md` went NOT MET, dated and reasoned —
  because the page they measure was withdrawn, not because the reviewer regressed.
  [RESULTS.md](ticket-20/RESULTS.md).

- [Decide whether a stacked summary score gets added to the findings list](issues/22-decide-the-findings-based-severity-score.md):
  **a count line, no single score** — the owner's B. `COUNT: <n> high impact, <n> moderate, <n> minor`,
  arithmetic over the list directly beneath it, fenced in the template against being written as a
  verdict, because **the tool calls findings high impact about three times as often as a human does**
  and a count inherits that inflation rather than escaping it. Stop condition 3 is untouched: a count
  of items in a visible list is not a level, is not invented and is checkable by the reader. Over-flag
  rate stays open and stays with ticket 07, which still must not set a bar on it. Applied by ticket 20
  in the same pass rather than filed.

- [Decide where the attempt gate lives](issues/21-decide-where-the-attempt-gate-lives.md):
  **the gate goes at the top of paste 3, the paste the student fills in — a position that was not
  on the ticket's list, and the reason inverts the ticket's framing.** Eviction drops the *oldest*
  turn, so paste 1 is the worst available place for a rule, not a safe second copy, and the deck is
  the best because it is the newest. Measured over **39 runs on two model families**: where the gate
  text survived the cut the model refused to review with nothing typed **16 of 16**, and where the
  text was cut it reviewed **6 of 6** and **never invented a marker claiming an attempt had been
  given**. So the confabulation this ticket was built to fear did not appear, and **there is only
  placement.** Paste 1 still earns a second copy, for a failure that is not truncation — the student
  who never sends paste 2 — and that copy also suppresses ticket 04's JSON-fallback defect, a live
  stop-condition-3 violation. Paste 2 earns none. **Ticket 08's orphaned budget question, answered
  on merits: 198 tokens per copy, 396 for two, +4.3% of the bundle, against a free-tier ceiling
  nobody has measured.** Failure behaviour is **refusal**, which held under a student arguing back
  — though that arm is one family and four runs, the thinnest load-bearing number here.
  **Ticket 10's 20-word rule must not be given to the model to enforce**: run head to head, the
  enforced threshold refused a genuine eight-word attempt on both families, while the wording with
  no number never blocked a real one. It survives as a measurement-side rule only. And the ticket's
  own premise that a gate can check presence without judging quality is **false** — told to check
  presence the model judged anyway, and **the same junk attempt on the same model was refused once
  and reviewed once**, so nothing downstream may lean on its judgement. The output marker ships on
  **line 2, never line 1**, and is **one-sided: presence proves an attempt, absence proves nothing**
  (0 fabrications in 6, but present only 10 of 11 and correctly placed 7 of 11). **Ticket 12 is not
  the same decision and was not merged** — three of four questions here never depended on it — but
  the two share the first two lines of the output, and checked after 12 landed they fit: 12 extends
  line 1, this takes line 2. The pair also carries one rule neither found alone: **a check that
  reports a defect gets ignored (12 measured 5 of 5), a check that withholds the product holds (16
  of 16).** Working record: [ticket-21/RESULTS.md](ticket-21/RESULTS.md).

- [Decide the bundle's truncation self-check](issues/12-decide-the-bundles-truncation-self-check.md):
  **a check ships and it is not the three markers — the tester's instrument and the student's are
  two different mechanisms, and that is the decision.** Ticket 04's silent failure is closed: with
  the whole system prompt missing, every run on both families announced the loss and **refused**,
  where 04 measured the same cut returning 12/12 sections and verbatim quotes. The mechanism is a
  **cross-paste key interlock** — one key at the top of paste 1, one on paste 2A's last line, and
  the output template at 88% depth demanding both on the review's first line. Value and demand live
  in **different pastes**, so a cut that takes a value leaves the demand standing; the student's
  check is *does the first line read exactly this string*, compared against their cover sheet, with
  no control run and no judgement, and **it cannot be skipped because it is the first line of the
  review they came for.** 34 runs, two model families: student verdict right **34 of 34**, false
  alarms **0 of 14** complete-bundle runs, and **0 invented keys** — the confabulation the ticket
  exists to defend against never happened. **The ticket's premise was wrong in one place and it is
  recorded:** ticket 11's warning that the probe can fail on a good session **did not reproduce**
  (6 of 6 clean, no confabulated lens label on the cut arms), so the markers are excluded for
  reading the wrong moment and being skippable, not for being unreliable. **The one thing that broke
  was this session's own first design** — the refusal rule placed at the tail beside the key it
  protects was cut off with it, and the model detected the missing key and reviewed anyway 5 of 5;
  restating it in both pastes took the cut arms to refused 9 of 9. **A rule is not safe where the
  thing it guards is.** Cost **392 tokens, 4.2% of the bundle**, and ticket 08's orphaned budget
  question is answered here rather than left ownerless. Restating the **synthesis protocol** is
  recommended **against** (1,377 tokens buys a degraded review instead of a refusal) and routed to
  the owner; the **noise budget** is added because ticket 04 found it in neither paste — a missing
  rule, not redundancy. **Unblocks ticket 21's hardest constraint without merging with it**: paste 1
  can no longer vanish silently, so the attempt gate can be placed on its merits. Hands ticket 09 a
  version stamp for free, on an **untested** variant. Limits held tight: truncation is **induced,
  not observed**, the Claude arms are contaminated by their subagent framing so every conclusion
  rests on the Codex arms alone, and the false-alarm bound is **0 of 14, upper limit near one in
  five** — not "it rarely false-alarms". Results: `.scratch/deliverable-reviewer/proto-12-selfcheck/RESULTS.md`.

- [Design the consultant feedback loop](issues/10-design-the-consultant-feedback-loop.md):
  **three instruments, and only one is a feedback form** — a lead record per triage (exists, the
  paste-back block, no UI built), a **lead cycle census** once per project cycle, and on the student
  side **the typed attempt plus one question**. The census is the answer to the selection-bias trap
  and it is a denominator, not a form: the trap is stated one level too shallow as a response rate,
  because **non-response has a known direction** and returned feedback is therefore a systematic
  upper bound, so chasing the rate converts a known-direction absence into "looks fine" of unknown
  direction. Today the denominator is unobtainable — the chat path has no telemetry, so the record
  count *is* the response count, the standing caution again. Response rates are **pre-registered
  with the consequence of missing each**: census 100% or that team is excluded from every numerator
  and denominator and never imputed; records 60% floor 40%, below which lead-side figures are raw
  counts only and `readinessCall.lead`'s required reason unwinds first; student question 40% floor
  25%, below which self-report is dropped and only the overlap is kept; attempt captured 95% floor
  80%. Plus **five pre-registered ways the pilot comes back negative**, because a design that can
  only return "yes" answers nothing. **The finding that reshaped the ticket: the attempt gate is not
  in the product** — the map settled "attempt first, always" at charting, but it exists only in the
  HTML renderer and in instructions to testers; paste 1 and 2A have none, and there is **no student,
  no attempt field and no student-side record anywhere in the system**. Two corrections: the record
  spec's outstanding work (`17-override-log.md` sections 3 and 4) is **void, not pending**, because
  it is written against the out-of-scope Triage Desk — its manufactured-agreement bug is genuinely
  absent from the chat path, the bias having moved from anchoring to abandonment; and with no
  release gate, **feedback changes nothing without the nine-deck blind re-run**, which is named a
  change-detector and not a quality bar. Overlap must record its judge model and report a band, per
  ticket 14's drift. Owner answered A/A/A — accepted, recorded as thin. Surfaced
  [ticket 21](issues/21-decide-where-the-attempt-gate-lives.md): **put the gate in paste 1 and it
  vanishes silently**, because ticket 04 measured head-eviction as undetectable, on exactly the
  free-tier windows the pilot needs. Working record: `.scratch/deliverable-reviewer/ticket-10/FINDINGS.md`.

- [Name the pilot's minimum shippable set](issues/25-name-the-pilots-minimum-shippable-set.md):
  **four tickets stand between here and a pilot, out of twelve open** - 20 cut to its four pilot
  items, 12, 21 and 09. Resolved by a scope audit the owner triggered
  ([AUDIT-2026-09-20.md](AUDIT-2026-09-20.md)) rather than by its own session. **The diagnosis: the
  map kept building the eval after ticket 14 took the eval off the critical path** - thirteen
  tickets at charting became twenty-five, ten of the twelve descendants trace to the baseline run,
  and five of the six tickets created since 2026-09-19 are eval work. **Ten resolutions, zero
  changes a user would notice.** Eight tickets parked, each with its reason on the ticket; a
  six-item accepted-gaps list carries what the pilot knowingly ships without, including two live
  defects that cannot be reached from the pilot path. Three things the audit found by checking
  rather than assuming: **even ticket 20 is mostly not pilot work** (four of thirteen items, two of
  them editing the out-of-scope hosted page), **ticket 11's prep already answers ticket 12**, and
  **half of ticket 22 already ships**. The audit also found against two tickets the same session
  had just created and pitched as high-value, which is recorded rather than quietly deleted.

- [Decide whether to keep or roll back frozen-2026-08-09](issues/15-decide-whether-to-keep-or-roll-back-frozen-2026-08-09.md):
  **the pilot runs `frozen-2026-09-19`, and the ticket's own premise was false** - it asked which of
  three versions ships, but paste 1 of the chat path points at a **live file** rather than a frozen
  copy, so ticket 17's patch made the September prompt the shipped prompt with nobody choosing it.
  Now chosen, and **it does not ship until paste 2 matches it**: `CHAT-CONTEXT.md` still demands a
  confidence label paste 1 has deleted, and still stamps every pilot record `frozen-2026-08-09` /
  `override-log-2-chat`. Three edits appended to ticket 20 Group B, which this unblocks, plus a
  standing hazard routed there - **any session that edits section A of `04-prompt-templates.md`
  ships to the pilot immediately**, and `check-docs.js` has no check that the two pastes agree.
  The argument for shipping: the chat output shows a severity label on every finding and **no
  readiness grade at all**, so the three metrics that did not move under ticket 17 all describe
  something a pilot user never sees, and the one row that did move is the one they do see. Nothing
  rolls back - re-scored (not re-run) under the derived scorer, `frozen-2026-08-03` beats
  `frozen-2026-09-19` by **one deck in nine on exact and one on over-flag, tying on within-one**,
  on a comparison uncontrolled for reviewer model on both sides. **The chat path has never been
  scored on any version**; all thirty-six reviews on record ran the harness path. Question 2 (which
  change carries the regression) is **ruled out of scope**; question 4 (over-flag as a metric) is
  **not answered and passes to ticket 22**, because the owner reopened the axis instead.

- [Apply the three ticket 16 fixes and verify them on the nine cases](issues/17-apply-the-three-ticket-16-fixes-and-verify-them-on-the-nine-cases.md):
  **the pre-registered prediction is refuted, and that is the result.** Three of four rows missed:
  readiness exact did not move (11.1%), over-flag did not move (66.7%), within-one moved to
  **77.8%** against a predicted 100%. Only the severity row held, and it held well: minor findings
  **1 in 45 to 4 in 42**, and **the noise budget stopped saturating for the first time in the
  project's history** (three decks at 4 findings), unpredicted, with the cap untouched. The
  mechanism is clean: the tightened rule 1 stopped firing on **two of four** decks, and **the two
  the prediction got right are exactly the two whose fallback ceiling was rule 2, the two it got
  wrong are the two whose fallback was rule 4**. The method's invariance assumption is falsified by
  a case, not by inference: **real-02 fired [1,4] before and [1,2] after**, so rule 4 stopped
  firing on a deck where rule 1 survived and the ceiling the counterfactual banked on is simply not
  there. **Ticket 05's derivation is NOT collateral damage, and this run is what says so** - it was
  re-measured on a prompt it had never seen and scored **9 of 9, zero no-blocker decks, 35 of 36
  total**. The two are one ceiling table fed different inputs: 05 feeds it rules a review reported,
  16 fed it rules it assumed a future run would report. What 05 does lose is the licence to be used
  that way again: **it scores runs that exist, it does not predict runs that do not.** The
  comparison is **uncontrolled** - neither prior baseline recorded the reviewer model, both
  manifests say `model: undefined`, now fixed and marked declared-not-observed. Two of nine reviews
  came back **contract-invalid, caused by this patch** (a minor finding marked delivery-critical),
  left standing and now ticket 23. Prompt `frozen-2026-09-19`, sha `757a38ac6a14287b`.
  Measurements: `.scratch/deliverable-reviewer/ticket-17/MEASUREMENTS.md`.

- [Retire the readiness level everywhere it appears](issues/05-retire-the-readiness-level-everywhere-it-appears.md):
  **the level is deleted as a thing the tool produces and kept as a thing the harness computes** —
  the ticket treated those as one object and they are two. The tool states no level on any path;
  the harness derives one from the blocking rules the review already reports, which **reproduced
  the emitted level on 26 of 27 reviews across three prompt versions**. The one miss is the method's
  whole limit: the only review in twenty-seven where no rule fired, where the model's discretion
  beat the arithmetic — on a holdout, correctly. **This is not a new instrument: ticket 16's
  pre-registered prediction was computed by exactly this arithmetic.** So `readinessWithinOne`,
  exact, over-flag and under-flag all survive, the golds are not re-cut, and ticket 15's table
  stays measurable. **`readinessCall.lead` survives** as the only field in the record that is not
  a reaction to the tool's output; `.ai` and `.delta` are deleted, so the reason line becomes
  unconditionally required — the answer most worth unwinding if pilot record volume disappoints.
  **Stop condition 3 widens to "the tool produces a level, for anyone"**, which turns two shipped
  artifacts into violations and **puts two trust-boundary rows red**, knowingly. Blast radius was
  wider again than ticket 04 left it: the artifact path has **no redaction and no stop panel**, and
  six documents now assert something false. **Sequencing is not optional — ticket 17 runs before the
  prompt-side deletion**, or the only pre-registered falsification test this project has is
  destroyed. Derivation record: [ticket-05-derive.md](ticket-05-derive.md).

- [Decide what to do about the two prompt defects the baseline exposed](issues/16-decide-what-to-do-about-the-two-prompt-defects-the-baseline-exposed.md):
  **the ticket's own hypothesis was wrong and that is the finding** — the noise budget cannot cause
  the over-flagging, because readiness is set by the blocking rules and nothing else, so the number
  of findings has no path to it. **The six over-flagged cases and the six blocking false positives
  are the same six cases**: two scorecard rows that have been read as corroborating each other are
  one metric counted twice. **Blocking rule 1 carries the entire regression** — it fired on exactly
  the four gold-R2 decks predicted R0, and suppressing it puts readiness exact back to 33.3%,
  within-one to **100%** and over-flag to **44.4%**, below both prompt versions. **Rule 2 fires on
  9 of 9 and has never been edited in the prompt's history**; it is left alone because its effect
  cannot be calculated, and is now ticket 18. Three owner decisions: **rule 1 is tightened** (name
  the two different client actions or it fires nothing), **the severity demotion floor is ungated**
  (it was conditional on no blocking rule firing, which has happened on one real deck in
  twenty-seven reviews, so the floor has been dead text since it shipped — 1 minor finding in 45
  against the gold's 10 in 37), and **the confidence label retires**, because it has never varied
  on a real deck under either rule (Medium 29 of 29 before the August patch, Low 12 of 12 after,
  never High, never mixed) and is structurally incapable of varying. **The noise budget cap stays
  at 5**, decided not asked: saturation is chronic since the first run and 22% over gold, against
  severity errors of 4x. Every confidence reading in the evidence base is invalidated in both
  directions. Measurements: `.scratch/deliverable-reviewer/ticket-16/MEASUREMENTS.md`.

- [Decide how a fresh run's pairs get judged](issues/14-decide-how-a-fresh-run-gets-judged.md):
  **the judging pass is not built and the gate drops the matcher-dependent metrics** rather than
  pretend to have them — the owner's call, and the reason the destination above was redrawn. Costed
  first, by running a real pack rather than estimating: **~412K tokens and ~5 minutes per gated
  prompt change at one draw** (2,227 tokens/pair, **3.5x** what the pair text predicts). A
  deterministic pre-filter is dead — zero-error ceiling **12.4%, fitted in-sample**. Three draws buy
  nothing: draws 2 and 3 each reproduce the 3-draw majority on coverage **exactly**. The headline
  finding: **a fresh draw today agrees with that majority on only 86.7%, and 5 of the 6
  disagreements are against a *unanimous* verdict** — the "97.2% determinism" was the judge measured
  against itself in one sitting, **the standing caution's third instance by a third mechanism**, and
  the cache stores no model id so judge drift is undetectable. Drift is confined to the
  `partial`/`no` boundary; the `yes` axis that recall uses held **45/45 across six weeks**.
  Ticket 01's `must-catch recall 0%` and `gold coverage 0%` are **unmeasured and must never be
  quoted** — `score-review.js:466` gets this right and `scorecard.js:95` throws it away.

- [Recover a real inter-rater number from the four double-labelled cases](issues/03-recover-an-inter-rater-number-from-the-double-labelled-cases.md):
  gold-author vs second-reader readiness agreement is **2 of 4, 95% CI [7%, 93%]**, kappa 0.385
  unweighted and **-0.053 quadratic-weighted** — too wide to license any reliability claim, and
  blindness is unverified on half the pairs. What it does license: **0 of 4 cases had the second
  reader stricter than the gold author**, and a case for retiring readiness that does not depend
  on the model being bad. Nothing in `18-evidence-base.md` or `22-trust-boundary.md` becomes
  false; four edits recommended, and **readiness exact-match as a release-gate bar is routed to
  tickets 05 and 07**. Analysis is local-only (`eval-cases-real/_INTER-RATER-RECOVERY.md`).

- [Establish what the bundle can do on a free account and in Codex](issues/04-establish-what-the-bundle-can-do-on-a-free-account.md):
  the bundle costs **9,227 tokens before any deck**, ~13,300 for a typical review and ~24,000 worst
  case; **the free-tier ceiling itself was not measured** and is now ticket 11. The prompt survives
  a non-Claude model whole (**gpt-5.6-sol**, 12/12 sections) and **quote-or-abstain held across 55
  quotes, two model families and every truncation level, 0 fabricated** — even with the system
  prompt entirely absent. Truncation is **loud when paste 2 is lost** (the output shape flips;
  detector: *does the reply open with `REVIEW OF:`?*) and **silent when paste 1 is lost** (12/12
  sections, verbatim quotes, indistinguishable from a good run). The mechanism: truncation
  announces itself only where the truncated thing has a closure property the model checks, which is
  why the one HTML arm refused and named the cut. HTML emits and renders on both families.
  Two defects: **the noise budget and scope matrix are cited by paste 1 but present in neither
  paste**, and **the JSON fallback re-emits the full rubric and a readiness level**. Prototype is
  local-only (`proto-04-free-tier-ceiling/`).

- [Run the real-deck baseline on the current frozen prompt](issues/01-run-the-real-deck-baseline-on-the-current-prompt.md):
  nine cases re-run blind on `frozen-2026-08-09` (sha verified at run time), **9 of 9 valid against
  the contract**. On every metric that is actually measured the current prompt is **worse than
  `frozen-2026-08-03`**: readiness exact 33.3% -> **11.1%**, within-one 77.8% -> **55.6%**, over-flag
  55.6% -> **66.7%**. Three cases moved, all the wrong way, and **08-09 broke two of the three exact
  readiness matches 08-03 had** (real-04, real-13 — the latter a holdout, now over by two). Four
  cases at gold R2 are all predicted R0. The headline blocker: **`must-catch recall 0%` and
  `gold coverage 0%` are unmeasured, not zero** — mc-match-3 is a cache of 712 judge verdicts over
  its own 178-pair set, this run needed 185 new judgments, and `--emit` has no path to a run
  directory, so **the harness cannot score any new run at all**; that is now ticket 14, and ticket 07
  is blocked on it. Also exposed: **confidence is pinned Low on all 9 by construction** (the
  `EVIDENCE AND SOURCE NOTES` field is blank in every pack, which short-circuits the test), and the
  noise budget is **saturating every time** (exactly 5 findings on all nine decks, 11 to 45 slides).
  **real-10 and real-11 still unrun**, gated on ticket 02. Run tree is local-only.

- [Decide how the bundle is distributed and version-stamped](issues/09-decide-how-the-bundle-is-distributed-and-version-stamped.md):
  **Google Drive for students, GitHub for leads and the board, one generated source and a check
  that fails when they disagree** - two hand-maintained derivatives have already gone stale
  undetected, so intention is replaced by `build-bundle.js --check`. The Drive **folder** link is
  baked into the bundle's own refusal message, so it can never change; the setup ships as a Doc,
  verified by a copy-out diff at publish time. **The version stamp is the KEYS field the interlock
  already prints**, and the readable form was run rather than argued: `MMDD-XXXXXXX` for part 1,
  **11 runs, 0 inventions, 0 date drift** with the run date a day past the key's
  ([RESULTS-B3.md](proto-12-selfcheck/RESULTS-B3.md)) - which settles the one item ticket 12 left
  open. The prefix is a convenience; `releases/REGISTER.md` is the authority. **Mismatch rule: kept
  and flagged, never dropped, and comparisons are always within a key** - plus a truncation counter
  that hands back a floor on how often real windows cut, without reopening the deferred free-tier
  work. **One bundle for both populations**; the difference is MODE and documentation, never bytes.
  **Question 5 has no name as its answer** - no seat exists, an AI role is being recruited in about
  five months - so transferability is the requirement and the artifacts are this ticket's
  deliverable: [HANDOVER.md](ticket-09/HANDOVER.md), written for someone who was not here and built
  around the failure this project actually faces on total turnover - **someone re-adding the
  readiness grade in good faith** - and [PUBLISHING.md](ticket-09/PUBLISHING.md). Two things fell
  out sideways: the corroboration batch found ticket 12's *"refused 9 of 9, both families"* rests on
  **one** run of the second family, and three new ones went the other way (the string comparison
  still caught all three, so nothing that ships changes); and Q4's *"students only"* collides with a
  gate that does not branch by audience, resolved as unconditional and flagged for one line from the
  owner. Edits in ticket 20, Group F.

## Not yet specified

- **How client-level deliverable improvement gets measured.** Named as the defensible outcome. Hard,
  and probably not answerable before the pilot has a shape.
- **The pilot cohort itself** — which chapter, how many teams, over what period, and what trips a
  stop. No longer waits on the release gate (ticket 14 took it off the critical path); waits on the
  readiness retirement and on the bundle being distributable. **Its instrumentation is no longer
  fog** — ticket 10 fixed the three instruments and pre-registered their response-rate floors, so
  whoever sizes the cohort inherits those numbers rather than choosing them.
- **A comparison group for the attempt-overlap measure.** Ticket 10 made the student's attempt the
  whole student-side instrument and measures value as the review's content closing against it. That
  gap also closes because students improve over a term, so with one arm the measure evidences
  nothing about the tool. Whether the pilot can carry a comparison at all is pilot design, and it is
  fog until the cohort has a shape.
- **How the tool gets judged once it is in use**, now that the gating eval is deferred. Manuel named
  the mechanism — read the output as a human and as an AI agent on real engagements — but not what
  is recorded, by whom, or what would count as it going wrong. This is the replacement for the
  instrument just dropped, and it is fog, not a ticket, until the pilot has a shape.
- **How the record corpus actually gets read.** [28-shared-corpus.md](../../tools/quality-reviewer/v2/28-shared-corpus.md)
  maps the architecture; the reader over it is fog until records exist.

## Parked until the pilot has run

<!-- deferred by the 2026-09-20 scope audit. NOT out of scope: these return once the pilot has
     shown what it shows. Each ticket carries its own reason. -->

- **02** gold contradictions, **06** student-trajectory metric, **07** the release gate, **18**
  blocking rule 2, **24** how the shipping path gets measured - all eval, and the eval came off the
  critical path on 2026-09-19.
- **08** what goes in the bundle - improvements to things that already work. (**13** was parked
  here and was unparked the same day by the owner; it closed 2026-09-20.)
- **23** minor versus delivery-critical - a live defect, parked knowingly; it is unreachable from
  the pilot path, which has no such field.
- **11** the four free tiers - reduced rather than parked; run one tier if any doubt remains after
  ticket 12 lands, since 11's own prep is what answers 12.

**The accepted-gaps list** - what the pilot knowingly ships without - is in
[ticket 25's answer](issues/25-name-the-pilots-minimum-shippable-set.md).

## Out of scope

- **AI-drafted fixes**, including the communication-axis-only variant. Parked as a feature to
  reconsider, not a step on this route. Logged in [parked-features.md](parked-features.md).
- **A hosted page.** `180dc-reviewer.pages.dev` is not the product and is not maintained toward one.
  **Withdrawn 2026-09-20 on the owner's call.** The audit found it live, untouched since
  2026-08-07, still called "the working tool" in its own documentation, and displaying a readiness
  level, an overall score and a confidence label - all three retired by tickets 05 and 16. The kill
  switch is on in the source and `site/` is rebuilt; the deploy is the owner's to run. **This
  removes two items from ticket 20** (the `index.html` / `site/index.html` edits) and removes the
  surface that made ticket 13 look load-bearing. The attempt gate lived only here, which is
  precisely why ticket 21 exists.
- **The readiness level as a product feature, as a ceiling the model judges.** Retired by
  [ticket 05](issues/05-retire-the-readiness-level-everywhere-it-appears.md), closed 2026-09-19;
  rebuilding it is not in this map. The level survives **only** as a number the eval harness derives
  from the blocking rules, never as output. Ticket 05’s edit list — six documents that now assert
  something false, plus the prompt, contract, renderer, record and scorer changes — is **executable
  spec, not an open decision**, and since 2026-09-20 it is owned by
  [ticket 20](issues/20-apply-the-accumulated-edit-lists-to-the-product.md). It carries a hard
  ordering constraint: ticket 17 runs before the prompt-side deletion.
  **Amended 2026-09-20, during ticket 15.** The owner has put a *findings-based* score back in
  scope - arithmetic over the findings a review already produced, where criticals stack, rather
  than a ceiling the model judges. That is a different object and the specific defect that retired
  the level (identical bytes, two levels) does not reach it. It is
  [ticket 22](issues/22-decide-the-findings-based-severity-score.md), and its first question is
  whether stop condition 3 forbids it anyway. **The ceiling stays retired and ticket 20's Group B
  proceeds unchanged** - ticket 22 starts from a tool that produces no level.

- **Attributing the August regression to a particular prompt edit.** Ticket 15 question 2, closed
  2026-09-20 on the owner's call without an answer. Settling it meant re-running three prompt
  versions on one model on one day, 27 reviews, roughly the cost of one gated change, and nothing
  turns on the result: nothing rolls back under any attribution. The lesson it was to buy arrived
  free from ticket 17 in a stronger form - **real-02 fired rules [1,4] before the patch and [1,2]
  after, with rule 4 never edited**, so no edit to this prompt is isolated, paste 2 included. The
  honest cost: this map will never know whether the comparator fix, the chat-native edit or the
  2026-08-07 rule 1 guardrail carried it, and it is closed by argument rather than by running it.
- **Building the record corpus infrastructure.** In scope to map, out of scope to build — there are
  no records to read until a pilot produces them.
