# Apply the three ticket 16 fixes and verify them on the nine cases

Type: task
Status: resolved
Blocked by: 16

## Question

Nothing to decide. [Ticket 16](16-decide-what-to-do-about-the-two-prompt-defects-the-baseline-exposed.md)
settled three prompt changes and recorded a numerical prediction **before** the run. This ticket
produces the number that confirms or refutes it, and the pilot ship decision in
[ticket 15](15-decide-whether-to-keep-or-roll-back-frozen-2026-08-09.md) waits on it.

This is the map's stated exception: a `task` ticket that generates numbers other decisions are
blocked on. It is not licence to build anything else.

Do:

1. Patch the prompt, as a new frozen version with a new sha, recording all three changes in
   `11-decision-log.md`:
   - **Blocking rule 1** gains a naming requirement. The reviewer must state the two different
     things the client would do under the two readings, in the blocking issue label. If it cannot
     name them, the contradiction is an ordinary finding and fires no rule.
   - **The severity demotion floor** stops being conditional on the deck having no blocking issues.
     A finding is minor whenever closing it would not change what the client actually does.
   - **The confidence label is deleted** from the readiness block and the scorecard. The
     "what could change it" sentence stays.

   **This ticket is deliberately not blocked on ticket 05**, which is claimed and carries the wider
   doc sweep for readiness and now confidence. Make only the minimum confidence change this run
   needs — the output contract and `check-review-v2.js`, which currently rejects a review whose
   confidence is not one of three strings and would fail all nine otherwise. Leave the rest of the
   sweep to ticket 05 and tell whoever holds it what you touched.
2. **Write the change-isolation note honestly.** Every prompt-change document since 2026-08-05
   closes by promising no blocking rule, ceiling, severity definition or noise budget was touched.
   Two of those three changes break that promise deliberately. Say so, and say that readiness
   movement in this run is therefore an intended effect rather than noise. Do not copy the old
   sentence forward.
3. Regenerate the input packs on the new prompt. **Do not populate `EVIDENCE AND SOURCE NOTES`** —
   `run-reviews.js:210` explains why the blank fields are deliberate, and filling them would make
   the run and the gold answer different questions.
4. Run all nine cases blind per the manifest protocol, one subagent per input, reading nothing else
   from the project. Collect, and score.
5. Also record, per case and in total: **the count of findings at each severity**, and **which
   blocking rules fired**. Ticket 16's severity and blocking-rule figures came from parsing the
   review JSON by hand because the scorecard does not report them. It should.

The prediction to check, recorded 2026-09-19 before any run:

| metric | 08-09 now | predicted after |
|---|---|---|
| readiness exact | 11.1% | **33.3%** |
| readiness within one | 55.6% | **100%** |
| over-flag rate | 66.7% | **44.4%** |
| minor findings, of the total | 1 of 45 | materially more; gold sits at 10 of 37 |

**If the run comes back materially different from the first three rows, the counterfactual method
is wrong and that is the more important finding.** It was arithmetic over recorded blocking issues,
not a simulation, and it assumed the model changes nothing else about its output when one rule is
tightened. That assumption is untested.

Watch for the obvious failure mode: rule 1 stops firing, the model reaches for rule 2 or rule 3
instead, and the readiness distribution does not move. Rule 3 has never fired once in twenty-seven
reviews, which makes it the likeliest new home for a displaced contradiction finding.

Note the whole run tree is gitignored and local-only. Reviews quote client decks verbatim.

Answer records: the scorecard, the severity distribution, the rule-firing counts, and whether the
prediction held.

---

**Input from [ticket 05](05-retire-the-readiness-level-everywhere-it-appears.md) (closed 2026-09-19). Read this before patching the prompt.**

Ticket 05 resolved while this ticket was open, and it agrees with your step 1: **run first, sweep
after.** The readiness deletion is deliberately split so this run is not disturbed.

**Do not remove the readiness level from `PASTE-1-system-prompt.txt`, `03-output-contract.md` or
`check-review-v2.js` in this ticket.** Ticket 16's prediction is stated in readiness metrics and
this run is its falsification test; deleting the emitted level first would destroy the only
pre-registered prediction this project has. Ticket 05's prompt-side edits land with or after your
verification run. Its record, renderer, doc-sweep and scorer edits land independently.

**Step 5 is now load-bearing beyond this ticket.** Ticket 05 measured that the emitted readiness
level is reproducible from the blocking rules alone — **26 of 27 across three prompt versions**,
with the one miss being the only review where no rule fired. That derivation is what lets the
harness keep readiness metrics after the level is deleted, and it is also how ticket 16 computed its
prediction. Your per-case record of **which blocking rules fired** is therefore the input to the
post-retirement scorer, not just a diagnostic.

**And re-measure the derivation after your run.** Tightening blocking rule 1 is expected to make
fewer rules fire, and the derivation is void on any deck where none does. Today that blind spot is
zero cases in nine. If your run produces no-blocker decks, say how many —
`.scratch/deliverable-reviewer/ticket-05-derive.js` reports it directly.

## Answer (2026-09-19)

**The prediction is refuted. Three of its four rows missed, and two of the three numeric rows
did not move at all.** Full record: [ticket-17/MEASUREMENTS.md](../ticket-17/MEASUREMENTS.md).
Prompt `frozen-2026-09-19`, sha `757a38ac6a14287b`. Nine cases, blind, one draw, all nine
scored at n=9 with nothing edited to make anything pass.

| metric | 08-09 | predicted | **actual** |
|---|---|---|---|
| readiness exact | 11.1% | 33.3% | **11.1%** |
| readiness within one | 55.6% | 100% | **77.8%** |
| over-flag rate | 66.7% | 44.4% | **66.7%** |
| minor findings, of total | 1 of 45 | materially more | **4 of 42** |

The ticket said a material miss means the counterfactual method is wrong and that this matters
more than the patch does. That is the result, and it is reported as the finding rather than as
a disappointment.

### 1. The confound, which is not optional context

Neither prior baseline recorded the reviewer model: both manifests say `model: undefined`,
because `--emit-packs` never wrote the field. **The "before" column has an unrecorded variable
in it.** This run records `claude-opus-5`, high, adaptive, deep, and `--emit-packs` now writes
all four, flagged in the manifest as *declared, not observed*, because the harness dispatches
nothing on the subagent path. Every comparison above is therefore **uncontrolled**: a moved row
is consistent with the prompt change, with a model difference, or with both, and the record
cannot separate them. The pre-registration is what makes the comparison worth making. It is not
what makes it controlled.

### 2. Why it missed, and the mechanism is clean

The counterfactual assumed rule 1 would stop firing on all four gold-R2 decks and that nothing
else in the output would move. **It stopped on two of four**, real-03 and real-14, both of which
landed on exactly the level predicted, via exactly the rule predicted. It still fires on real-02
and real-13, where the reviewer could write out two genuinely different client actions.

The split is not random: **the two it got right are the two whose fallback ceiling was rule 2,
and the two it got wrong are the two whose fallback was rule 4.** Both predicted exact matches
were rule-4 cases and both failed.

And the invariance assumption is falsified by a case, not by inference. **real-02 fired [1,4]
before and [1,2] after.** Rule 4 stopped firing on a deck where rule 1 survived. The
counterfactual banked on rule 4's R2 ceiling being there to catch real-02; today it is not there
at all, so even a successful suppression of rule 1 would have produced R1, not the predicted R2.
**The arithmetic was applied to a rule set the run did not reproduce.**

The failure mode the ticket told us to watch for did **not** happen: rule 3 fired zero times, as
it has in all thirty-six reviews on record, and nothing was re-homed.

### 3. Does this put ticket 05's basis in doubt? No, and the run is what says so.

The instruction that came with this ticket was to report plainly that a miss also undermines
ticket 05's basis for keeping readiness metrics, since 05's derivation and 16's prediction are
the same arithmetic. **They share a component, and this run separates them, so the honest answer
is the narrower one.**

Both use one ceiling table. They differ in what they feed it:

- **Ticket 05** feeds it the blocking rules **the review actually reported**, and asks whether
  the emitted level follows. That is a consistency claim about one run's own output.
- **Ticket 16** fed it blocking rules it **assumed a future run would report**. That is a
  forecast about a model under an edited prompt.

The shared half was re-measured here, on a prompt version it had never seen: **9 of 9, zero
no-blocker decks, total now 35 of 36.** The half that failed is the half ticket 05 does not use.
Reporting 05 as collateral damage would be manufacturing a second casualty the data refuses to
support, and this map has a standing caution about numbers that are copies of each other. The
mirror-image error is treating two things as one when a measurement has just told them apart.

What the miss **does** cost ticket 05: its derivation must never again be used the way ticket 16
used it. The sentence in 05's answer reading "this is not a new instrument, ticket 16's
prediction was computed by exactly this arithmetic" was offered as reassurance and it now cuts
the other way. **The derivation is licensed to score runs that exist. It is not licensed to
predict runs that do not.** That correction belongs in 05's record.

### 4. What the patch did achieve, stated without inflation

- **Within-one moved 55.6% to 77.8%**, right direction, less than half the predicted distance.
  Two decks moved from two levels over to one.
- **Minor findings went 1 in 45 to 4 in 42**, the one row that held. Still a third of the gold's
  27%. Criticals barely moved, 13 to 11, against a gold count of 3.
- **The noise budget stopped saturating for the first time ever.** Three decks returned 4
  findings. Every prior run on every prior prompt sat at a mean of 4.89 to 5.00 with the cap hit
  almost everywhere. The budget was not touched. Unpredicted, and with three changes shipped
  together it cannot be attributed to one of them.
- **Over-flag is unchanged at 66.7% because the same six decks over-flag, an identical set.**
  Three escalate by less, which over-flag structurally cannot see: it counts membership, not
  distance. Ticket 16 called over-flag and blocking false positives one metric counted twice.
  This run adds that the metric is also **coarse**, and it is close to the only survivor on the
  gate. Worth a look before it carries weight it cannot bear.

### 5. Two contract failures, caused by this patch, left standing

`real-01` and `real-05` are contract-invalid on the same check: a **minor finding marked
`deliveryCritical: true`** (`check-review-v2.js` rule 8b). Both are QA artifacts, placeholder
text and leftover internal notes. The reviewer's position is coherent in plain words: it does
not change what the client decides, so minor, and it must not go out of the door, so
delivery-critical. The prompt does not settle it, because its deliveryCritical clause is written
only for the no-blocker case and the severity floor no longer has that gate, so the two rules no
longer meet. Rule 8b has been in the validator since the beginning and almost never fired,
because minors were almost never produced. **Ungating the floor made minors common and the
latent conflict surfaced immediately, on two of the four new minors.** Now ticket 23.

### 6. Where this leaves ticket 15

The pilot ship decision waits on this number, and the number is: **the patch helped on one of
three headline metrics, by half the predicted amount, against an uncontrolled baseline, and
introduced a contract conflict on two of nine cases.** That is a weaker hand than ticket 16
expected to deal ticket 15, and ticket 15 should be told so directly rather than handed the
within-one improvement on its own.

### What was changed, for whoever holds ticket 05

Prompt-side readiness was **not** touched, per 05's ordering constraint. Confidence was deleted
from `03-output-contract.md`, `check-review-v2.js` and the `run-reviews.js` response schema,
which is the minimum this run needed. `04-prompt-templates.md` section A and
`TEST-KIT/PASTE-1-system-prompt.txt` were both patched and remain byte-identical. Harness:
`--emit-packs` records model, effort, thinking and mode; `score-review.js` reports per-case
`severityCounts` and `rulesFired`; `scorecard.js` aggregates both and names any no-blocker deck
as void for the derived level. Five rows in `11-decision-log.md`, including a standalone row
retiring the change-isolation promise rather than copying it forward.
