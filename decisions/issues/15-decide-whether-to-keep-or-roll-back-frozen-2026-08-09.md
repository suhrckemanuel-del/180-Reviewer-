# Decide whether to keep or roll back frozen-2026-08-09

Type: grilling
Status: resolved
Blocked by: 17

## Question

Surfaced in review on 2026-09-19. Ticket 01 measured it and routed the consequences to 07 and 14,
but **nobody owns the decision it forces**: the prompt that is live, frozen, and shipped inside
`CHAT-CONTEXT.md` is measurably worse than the one before it.

Against `frozen-2026-08-03`, on the same nine cases:

| metric | 08-03 | 08-09 |
|---|---|---|
| readiness, exact | 33.3% | **11.1%** |
| readiness, within one | 77.8% | **55.6%** |
| over-flag rate | 55.6% | **66.7%** |

Three cases moved and all three worsened. 08-09 broke two of the three exact matches 08-03 had,
including real-13, a holdout, now over by two levels. Four cases at gold R2 are all predicted R0.

Blocked by ticket 05 because **retiring the readiness level dissolves most of this table.** If
readiness goes, two of the three rows stop being metrics and the regression shrinks to over-flag —
still worse, but a different size of problem. Deciding before 05 would be deciding against numbers
that may not survive the week.

Settle, once 05 has landed:

1. **Does anything roll back?** The intervening changes were not arbitrary — `frozen-2026-08-05e`
   fixed the comparator gate that had suspended 11 of 11 figures, and 08-09 added the chat-native
   output block. A rollback to 08-03 would reopen the comparator gate. Rolling back is probably
   wrong; the question is what replaces it.
2. **Was the regression caused by the comparator fix or the chat-native edit?** The chat-native
   change was five lines inside the OUTPUT block and claimed to touch nothing protected. If the
   regression traces to it, that claim was wrong and the change-isolation discipline needs a look.
   If it traces to the comparator fix, a real improvement on one axis cost accuracy on another and
   that is a trade to make deliberately.
3. **What ships to the pilot in the meantime?** The pilot is the destination and it will run on
   some version. Name it.
4. **Does over-flag survive as a metric** once readiness is gone, and is 66.7% acceptable? It is
   the restraint signal, and ticket 01 also found the noise budget saturating at exactly 5 findings
   on every deck — see ticket 16.

Answer records: the version the pilot runs, whether anything is reverted, and which change carries
the regression.

---

**Owner decision on question 3, 2026-09-19 (during ticket 14).** **The pilot runs
`frozen-2026-08-09`, with the two ticket-16 defects fixed first.** Nothing rolls back: 08-09
carries the two-mode output shape and the chat-native path, and reverting to 08-03 would reopen the
comparator gate that `frozen-2026-08-05e` closed.

Manuel's reasoning as put to him: the regression is real but concentrated in readiness, the
component ticket 05 retires. The case against, which he accepted knowingly: **over-flag also got
worse (55.6% -> 66.7%)**, and over-flagging is the failure students will actually notice and
resent.

Questions 1, 2 and 4 remain open — in particular **which change carries the regression** (the
comparator fix or the five-line chat-native edit, whose author claimed it touched nothing
protected), and **whether over-flag survives as a metric** once readiness is gone. Question 4 now
matters more, not less: over-flag is close to the only number the gate is still allowed to hold.

---

**Input from [ticket 16](16-decide-what-to-do-about-the-two-prompt-defects-the-baseline-exposed.md)
(closed 2026-09-19). Question 4 is largely answered, and question 2 has a new suspect.**

**Question 4, does over-flag survive as a metric.** It survives, but not as an independent one.
**The six over-flagged cases and the six blocking false positives are the same six cases, exactly.**
Over-flag 66.7% and blocking false positives 66.7% are one metric counted twice, and the scorecard
has been presenting them as if they corroborated each other. Whatever gate eventually exists should
report one of them, not both.

Is 66.7% acceptable? On the ticket 16 fixes it is predicted to fall to **44.4%**, below the 55.6%
that `frozen-2026-08-03` scored, with readiness within-one going to 100%. That prediction is
recorded before the run and [ticket 17](17-apply-the-three-ticket-16-fixes-and-verify-them-on-the-nine-cases.md)
checks it. **Do not close this ticket before those numbers exist.**

**Question 2, which change carries the regression.** Neither candidate in this ticket's framing.
The regression traces to **blocking rule 1**, which fired on exactly the four gold-R2 decks
predicted R0. Rule 1's text gained its guardrail on 2026-08-07 in the trust-boundary commit, which
is *between* the two suspects named here. So the five-line chat-native edit is not implicated by
this evidence, and the change-isolation discipline is not obviously broken by it - but that is an
absence of evidence, not a clearance. What is now known is where to look.

**Question 1, does anything roll back.** Unchanged by ticket 16, and the case for rolling back gets
weaker: the 08-03 advantage was concentrated in readiness, and on the counterfactual the patched
08-09 matches 08-03 on readiness exact while beating it on over-flag.

---

**Input from [ticket 05](05-retire-the-readiness-level-everywhere-it-appears.md) (closed 2026-09-19). The 05 block is lifted; ticket 17 still gates this one.**

**The table survives intact.** This ticket was blocked on the expectation that retiring readiness
would dissolve two of its three rows. It does not: the level is deleted from the product and kept in
the harness, derived from the blocking rules the review already reports. Readiness exact, within-one
and over-flag all remain measurable on the same nine cases, and the 08-03 versus 08-09 comparison
stands exactly as written.

One caveat on the 08-03 column: **real-13 is the single case in twenty-seven where no blocking rule
fired**, so its 08-03 level came from the prompt's discretionary branch, which the derivation cannot
reproduce. Under a derived scorer 08-03 scores R3 there against gold R2 — one of its three exact
matches becomes a within-one. If this ticket re-states the comparison, state which scorer produced
it.

Question 2 (was the regression the comparator fix or the chat-native edit) is untouched. Note that
ticket 16 has since attributed the minus-two tail to blocking rule 1 and predicted the regression
mostly reverses when it is tightened; **ticket 17 produces the number that settles this ticket.**


---

**Input from [ticket 17](17-apply-the-three-ticket-16-fixes-and-verify-them-on-the-nine-cases.md) (resolved 2026-09-19). This ticket is now unblocked, and the number it was waiting for is weaker than ticket 16 expected to hand it.**

The question has also moved: the version on the table is no longer `frozen-2026-08-09` but
**`frozen-2026-09-19`**, which carries the three ticket 16 fixes. Read the verification result
before reading the improvement:

- **The pre-registered prediction was refuted on three of four rows.** readiness exact did not
  move (11.1%), over-flag did not move (66.7%), within-one moved but to 77.8% rather than the
  predicted 100%. Only the severity row held.
- **The baseline it is measured against is uncontrolled.** Neither prior run recorded the
  reviewer model. Any movement is consistent with the prompt change, a model difference, or both.
- **Two of nine reviews came back contract-invalid**, caused by the patch itself, and the defect
  is live on the shipped prompt. Now [ticket 23](23-settle-whether-a-minor-finding-can-be-delivery-critical.md).
- Genuinely better: minor findings 1 in 45 to 4 in 42, and **the noise budget stopped saturating
  for the first time in the project's history**, unpredicted and unattributable to one of the
  three changes.

**Do not take the within-one improvement on its own.** The shape of the evidence is: one of
three headline metrics moved, by half the predicted amount, against a baseline that was never
controlled, with a new contract defect attached. That may still be enough to ship for a pilot
whose stated alternative is no substantive review at all. It is not enough to claim the fixes
are verified, and the difference between those two sentences is this ticket's whole job.

---

## Findings, 2026-09-20. Questions are below them; this ticket is not closed.

Read in this order: the shipped state first, because it changes what question 3 is asking.

### 0. What is actually shipped today is none of the three candidates

The ticket asks which of `frozen-2026-08-03`, `frozen-2026-08-09` and `frozen-2026-09-19` ships.
**The premise is false. The pilot path is already running a hybrid that nobody chose.**

The chat path is three pastes, and `CHAT-CONTEXT.md:7-12` names them: paste 1 is *section A of
`04-prompt-templates.md`*, paste 2 is `CHAT-CONTEXT.md`, paste 3 is the team input template.
**Paste 1 points at a live file, not at a frozen copy.** Ticket 17 patched that file in place, so:

- **Paste 1 is `frozen-2026-09-19`** — rule 1 tightened, severity floor ungated, confidence deleted.
  `04-prompt-templates.md:244` now reads *"You report no confidence label."*
- **Paste 2 is unchanged since 2026-08-09.** `CHAT-CONTEXT.md:313` still instructs the reviewer to
  write `Confidence in this review: <Low | Medium | High>`, and `:287` asserts that everything in
  the system prompt "still binds without exception".

**The two pastes now contradict each other on a field ticket 16 formally retired**, and paste 2 is
the one that wins, because it holds the output template. Nobody decided this; it is the residue of
ticket 17 patching only the two files its harness run needed.

Two more things stale in paste 2, both load-bearing for the pilot rather than cosmetic:

- `CHAT-CONTEXT.md:367` stamps every paste-back record `"promptVersion": "frozen-2026-08-09"`.
  **Every record a pilot produces today would name the wrong prompt.** The record is the only trace
  a chat review leaves, and the version stamp is what a later reader uses to know what produced it.
- `:364` stamps `"recordVersion": "override-log-2-chat"`, which ticket 05 decision 2 bumps to
  `override-log-3-chat`.

`check-docs.js` does not catch any of this. It checks the rubric against the source register; it has
no check that paste 1 and paste 2 agree about what the output contains.

**And the chat path has never been scored on any version.** All thirty-six reviews on record ran the
harness path against generated packs. Every number in this ticket, on all three candidates, describes
a path the pilot does not use.

### 1. Question 1, does anything roll back. Stated, not asked: no.

The owner settled this on 2026-09-19 and nothing since argues the other way. What is new is that the
size of the thing being defended has shrunk, and that is worth recording honestly rather than as a
win.

Re-scored under the derived scorer that ticket 20 step 4 will actually build — **re-scored, not
re-run**; ticket 05 is licensed for exactly this and did the `real-13` step itself:

| metric, derived scorer | `frozen-2026-08-03` | `frozen-2026-09-19` | gap |
|---|---|---|---|
| readiness exact | 2 of 9 | 1 of 9 | **one deck** |
| readiness within one | 7 of 9 | 7 of 9 | **none** |
| over-flag | 5 of 9 | 6 of 9 | **one deck** |

`real-13` is the one review in twenty-seven where no blocking rule fired, so 08-03's third exact
match is the prompt's discretion, which the derived scorer cannot reproduce; derived it reads R3
against gold R2, which moves it out of exact and into under-flag rather than over-flag.

So the regression this ticket was opened over is, on the scorer that will exist, **two deck-level
differences out of nine**, against a reference two humans reproduced on 2 of 4 (95% CI [7%, 93%],
ticket 03), **with the reviewer model unrecorded on both sides**. Rolling back would still cost the
comparator gate that `frozen-2026-08-05e` closed (11 of 11 figures suspended before it) and the
entire chat-native path, which is the pilot's delivery mechanism. Nothing rolls back.

### 2. Question 2, which change carries the regression. Recommend ruling it out of scope.

Ticket 16 attributed it to blocking rule 1, whose guardrail changed on 2026-08-07 — between this
ticket's two named suspects, clearing the five-line chat-native edit by absence of evidence.
**Ticket 17 weakened that attribution and the ticket should say so.** The attribution was produced
by the counterfactual arithmetic that the run then refuted: rule 1 was predicted to stop firing on
four of four gold-R2 decks and stopped on two. On those two the level moved one step in the right
direction, so rule 1 carries *part* of the tail, measured on two decks. On `real-02` and `real-13`
it still fires and the level is still R0.

Settling question 2 properly means re-running 08-03, 08-05e and 08-09 on one model on one day —
27 reviews, roughly 360K tokens at ticket 04's ~13.3K per review, comparable to one gated change
under ticket 14's costing.

**The recommendation is not to pay it, and to rule the question out of scope rather than leave it
open.** Two reasons:

1. **Nothing turns on the answer.** Question 1 is no under every attribution.
2. **The lesson it was going to buy has already been bought more cheaply and more generally.**
   Question 2 existed to test whether "this edit touched only the OUTPUT block" is a safe claim.
   Ticket 17 answered the stronger version by accident: **`real-02` fired rules [1,4] before and
   [1,2] after, and rule 4 was not edited.** The rule set moves under edits that do not touch it,
   so no edit to this prompt is isolated — which is the finding question 2 was chasing, and it
   covers paste 2 as well, where the entire content is output-block.

The decision-log row for 2026-09-19 already retires the change-isolation promise rather than
carrying it forward, so the discipline question 2 was meant to audit is not in force.

### 3. Question 3, what ships to the pilot

Given section 0, the real choice is between two internally consistent packages, not three versions.

**Option A — ratify `frozen-2026-09-19` and bring paste 2 up to it.** Three edits to
`CHAT-CONTEXT.md`, all in ticket 20 Group B: delete the confidence line at `:313`, stamp
`frozen-2026-09-19` / `override-log-3-chat` at `:364-367`, and walk the template against the
patched paste 1 for any other field that no longer exists.

**Option B — freeze paste 1 back to a verbatim copy of `frozen-2026-08-09`** under
`eval-runs/prompt-archive/`, point `CHAT-CONTEXT.md:8` at the copy rather than the live file, and
ship the package the chat-native document was written and reviewed against.

**The recommendation is A**, and the argument is about which axis the pilot path displays:

- **The chat template shows severity on every finding** (`[High impact | Moderate | Minor]`,
  `CHAT-CONTEXT.md:321`) and **shows no readiness level at all**, by design (`:288`). So the three
  metrics that failed to move under the patch — exact, within-one, over-flag — are all readiness
  metrics describing something a pilot user never sees. **The one row that moved is the one they
  do see.** Minor findings 1 in 45 to 4 in 42, criticals 13 to 11 against a gold count of 3, and
  the noise budget stopped saturating for the first time in the project's history.
- **The contract defect ticket 17 flagged does not exist on this path.** The chat template has no
  `deliveryCritical` field and no validator; `check-review-v2.js` rule 8b is a harness and
  artifact-path invariant. `real-01` and `real-05` are live defects on the JSON path, which is
  ticket 23's business, and they are not a reason to hold the pilot.
- The map's stated pilot success bar is findings kept rather than cut. Severity honesty is the
  closest thing on the record to that bar; readiness exact-match is not on it at all.
- Option B ships the dead severity floor — 29% criticals against a gold 8%, 2% minors against 27%.
  Over-flagging is the failure the owner named as the one students will notice and resent, and on
  a path with no readiness level, severity *is* the over-flagging.

**The best case against A, and it is real:** `frozen-2026-09-19` is the least-measured of the three
on the path that will run, it was never chosen by anyone, and its only measured improvement rides an
uncontrolled baseline. Option B at least ships a package whose two halves were written together and
read by a human as a whole.

### 4. Question 4, does over-flag survive as a metric, and is 66.7% acceptable

**66.7% is not acceptable or unacceptable. It is uninterpretable, and the honest move is to say so
rather than pick a bar.** Four discounts stack on it, and each was established by a different
ticket, so this is not one objection restated:

1. **It is one metric, not two.** The six over-flagged cases and the six blocking false positives
   are the same six cases (ticket 16). They must stop being printed as corroborating rows.
2. **It is coarse.** It counts membership, not distance. Three of the six escalate by less after
   the patch and over-flag structurally cannot see it — which is exactly why it read 66.7% before
   and after while within-one moved 55.6% to 77.8% (ticket 17).
3. **Its reference is noisy past the point of use.** Two humans reproduced the gold readiness on
   2 of 4, 95% CI [7%, 93%], quadratic kappa below chance (ticket 03).
4. **Post-retirement it is computed from a derived level that is void where no rule fires, and gets
   blinder as decks improve** (ticket 05) — the direction ticket 16 is pushing them.

And a fifth, from section 0: **it measures a quantity the product no longer produces.** Over-flag
was a proxy for "the tool is harsher than a human would be". On a path that shows no level, the
thing that makes the tool read as harsh is the severity label on each finding.

**Recommendation: over-flag survives as a reported diagnostic with no bar on it, and the gate's
restraint bar moves to the severity distribution.** That replacement is not speculative:

- It is **matcher-free**. `score-review.js:313-317` already parses `severity:` out of the gold
  worksheets and `:582-585` already emits per-review `severityCounts` — both landed in ticket 17.
  Nothing in it needs mc-match-3, so it is not caught by ticket 07's constraint 1.
- It is **the only headline row that moved** under a deliberate change, so it has demonstrated it
  can move at all. Exact and over-flag have now sat still through a patch aimed squarely at them.
- It is **what the pilot path displays**.
- Current standing: gold 8% critical / 65% major / 27% minor; `frozen-2026-09-19` 26% / 64% / 9.5%.
  Criticals 3.3x the gold rate and minors a third of it — a number a non-author can read and argue
  with, unlike 66.7%.

**The honest limits, both of which belong in the bar if it is set:**

- **A distribution match is weaker than an alignment match.** Two reviews with identical
  distributions can disagree on the severity of every individual finding. `severityAlignment` is the
  per-finding version and it needs the judge, so it stays barred under ticket 07 constraint 1. The
  distribution bar is a restraint signal, not an accuracy one, and must be labelled that way.
- **Nobody has measured whether two humans agree on a finding's severity**, and the cheap route is
  closed: `_INTER-RATER-RECOVERY.md:163` records that the four second-reader worksheets are thin,
  one issue each and some fields empty. So the severity reference carries an unmeasured reliability
  exactly as readiness did — the difference is that readiness's was measured and came back unusable,
  where severity's is unknown. **Do not repeat ticket 03's discovery by assuming the better case.**

### 5. Housekeeping, fixed

There were **two tickets numbered 19**. A concurrent session renumbered "Apply the accumulated edit
lists to the product" to **20** while this session was renumbering the other one; the collision that
briefly created is resolved. "Settle whether a minor finding can be delivery-critical" is now
**[ticket 23](23-settle-whether-a-minor-finding-can-be-delivery-critical.md)**, and every reference
in the map and in tickets 15 and 17 points at the right file.

## Answer (2026-09-20)

Three owner decisions, and one of them reopens something this map had closed.

### Decision 1. The pilot runs `frozen-2026-09-19`, and it does not ship until paste 2 matches it.

Option A. **This ratifies a version that was already live by accident** — ticket 17 patched the file
paste 1 points at, so the September prompt has been the shipped prompt since 2026-09-19 with nobody
choosing it. It is now chosen.

The reasoning as put to the owner, and accepted: the chat output shows a severity label on every
finding and shows no readiness grade at all, so the three metrics that did not move under ticket
17's patch all describe something a pilot user never sees, and the one row that did move — severity
— is the one they do see.

**The case against, stated and accepted knowingly:** `frozen-2026-09-19` is the least-measured of
the three candidates on the path that will actually run, it was never chosen by anyone before now,
and its single measured improvement rides a baseline where the reviewer model was not recorded.
Option B would have shipped a package whose two halves were written and read together.

**This does not ship as-is.** Paste 1 and paste 2 currently contradict each other, per section 0.
Three edits to `CHAT-CONTEXT.md`, appended to **[ticket 20](20-apply-the-accumulated-edit-lists-to-the-product.md)**
Group B, which this decision unblocks:

1. Delete the confidence line at `:313`. Paste 1 at `04-prompt-templates.md:244` says the reviewer
   reports no confidence label; paste 2's template still demands one and paste 2 wins, because it
   holds the output template.
2. Stamp the paste-back record `"promptVersion": "frozen-2026-09-19"` at `:367` and
   `"recordVersion": "override-log-3-chat"` at `:364`. Today every record a pilot produces would
   name the August prompt, and the record is the only trace a chat review leaves.
3. Walk the whole template against the patched paste 1 for any other field that no longer exists.
   Nobody has done this since 2026-08-09 and `check-docs.js` has no check that the two pastes agree.

**A standing hazard this exposed, worth more than the three edits.** Paste 1 is *"section A of
`04-prompt-templates.md`"* — a live file, not a frozen copy. Any session that patches that file
ships to the pilot, immediately, without a decision. Ticket 20 should either pin paste 1 to an
archived copy under `eval-runs/prompt-archive/` or add a check that paste 1's version tag and paste
2's record stamp agree. Routed there rather than decided here.

### Decision 2. Question 2 is ruled out of scope. Nothing is re-run to attribute the regression.

The owner's answer was to close it. Recorded on the map's **Out of scope** section rather than in
Decisions so far, because a scope boundary is not a step on the route.

What is given up: this map will never know whether the August regression came from the comparator
fix, the five-line chat-native edit or the 2026-08-07 rule 1 guardrail. Settling it meant re-running
three prompt versions on one model on one day, 27 reviews, roughly the cost of one gated change.

What makes that acceptable: question 1 is *no* under every attribution, so nothing turns on it; and
the lesson the question was going to buy already arrived free from ticket 17, in a stronger form —
`real-02` fired rules [1,4] before the patch and [1,2] after, with **rule 4 never edited**. The rule
set moves under edits that do not touch it, so **no edit to this prompt is isolated**, which covers
paste 2 as well, where the entire content is output-block.

**The case against, stated and accepted:** this closes the only open question about why the tool got
worse in August, and closes it by argument rather than by running the thing — which is the exact
move ticket 17 punished three days ago.

### Decision 3. Question 4 is not answered as asked. The owner has reopened readiness, differently.

The question was whether the over-flag rate keeps a pass/fail bar. The owner did not pick either
option and proposed a third thing instead:

> *"i feel we need to re think about readness level i feel it could just be based on perfect
> deliverables but more like its based on the errors it finds in the deck. so the cirtiqual ones
> are just stacked why dones we just list them i feel htats so much more simplare we just a need a
> simple scorring system for the errors we find"*

**This is not the level ticket 05 retired and it must not be treated as a resumption of it.** The
retired level was a *ceiling*: the lowest ceiling among the blocking rules that fired, a model
judgement that returned two different answers on identical bytes. What is proposed is *arithmetic
over the findings the review already produced* — deterministic given a findings list, which dodges
the specific failure that killed the old level.

It does not dodge the others, and it collides with a decision taken last week. **Stop condition 3
was widened on 2026-09-19 to "the tool produces a readiness level, for anyone", and two
trust-boundary rows go red over it.** A stacked score over findings is arguably that level by
another name. That is a real decision, not a detail, and it is too big to fold into this ticket.

**Therefore: this ticket does not decide it.** It is
**[ticket 22](22-decide-the-findings-based-severity-score.md)**, and the map's Out of scope entry
for the readiness level is amended rather than deleted — the ceiling stays retired; a findings-based
score is a new object the owner has put in scope.

**What this ticket does settle, because ticket 20 Group B cannot wait on ticket 22:** the readiness
retirement proceeds exactly as ticket 05 wrote it. Group B still deletes the emitted level from the
prompt. Nothing about decision 3 preserves the old field, and ticket 22 starts from a tool that
produces no level.

**And the over-flag question is left open, deliberately.** My recommendation — report over-flag with
no bar, move the gate's restraint bar to the severity distribution — is recorded in section 4 above
and was **not** adopted, because the owner's answer reframes the whole axis. Ticket 22 inherits it.
Ticket 07 must not set a bar on over-flag before ticket 22 resolves.

### What ticket 15 recorded, against what it was asked to record

The ticket said: *"Answer records: the version the pilot runs, whether anything is reverted, and
which change carries the regression."*

| asked for | recorded |
|---|---|
| the version the pilot runs | `frozen-2026-09-19`, conditional on the three paste 2 edits |
| whether anything is reverted | nothing, and the gap it defends is two decks in nine on an uncontrolled comparison |
| which change carries the regression | **not recorded, ruled out of scope** |
