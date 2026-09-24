# Results: does the rewritten finding register hold?

Run for [ticket 26](../issues/26-rewrite-the-finding-for-a-student-who-has-to-act-tonight.md).
Haiku 4.5 arms 2026-09-20, Codex arms 2026-09-21 once the account's usage limit reset.

**Ten runs, two model families, one synthetic deck.** Five arms per family: three student repeats
on byte-identical input, two lead arms as the no-bleed control.

## The one-line result

**The template works and Haiku 4.5 cannot hold it.** On Codex the register lands almost
everywhere it was asked to: one-sentence `The problem:` **10 of 10**, worked examples that pass
both audit tests **6 of 6**, plain-English titles, verbatim quotes **15 of 15**. On Haiku the same
bytes produce one-sentence `The problem:` **0 of 10**, two examples of which one **fails the audit
test the prompt told the model to run on itself**, and the collapse this ticket predicted.

**This is a family split, not a prompt defect** — and it is the first time on this map that a
change has passed on one family and failed on the other. Everything downstream of that sentence is
a decision the owner has to make, because the pilot cannot choose its students' model.

## Side by side

| what was asked | Haiku 4.5 | Codex |
|---|---|---|
| `The problem:` is one sentence | **0 of 10** (2-8 sentences) | **10 of 10** |
| `Why it matters:` within about 55 words | 7 of 10 (19-77w, mean 43) | **10 of 10** (31-53w, mean 39) |
| worked example fires where a fact is missing | **2 of 10 findings** | **6 of 10 findings** |
| example carries "that is the shape, not your numbers" | **0 of 2** | **6 of 6** |
| example passes both audit tests, read by hand | **1 of 2** | **6 of 6** |
| plain-English title | **0 of 10** | 8 of 10, several exact |
| quotes verbatim, character for character | **3 misses** in 10 cited | **0 misses** in 15 cited |
| `The problem:` / `Why it matters:` stay distinct | collapsed on r3 f1 | no collapse seen |
| lead mode untouched | **2 of 2 clean** | **1 of 2** — one arm bled |
| habit section gone | 5 of 5 | 5 of 5 |

## What held on both families

**The mode branch, nearly.** Three of four lead arms came back in the dense shape with all four
old fields and no new ones. The owner's ruling that the new register binds on short and deep only
cost nothing to implement.

**The habit section is gone from 10 of 10 arms**, both modes, both families, with no model trying
to reinstate it. Its device is now distributed into the findings on Codex, which is what the
owner asked for.

**The word overrun that opened this ticket is fixed, and not by restating the budget.**
`Why it matters` ran 31-53 words on Codex and 19-77 on Haiku, against the 90-word unbroken block
in the review the owner reacted to. **Splitting the field moved it; the number never would have.**
This is the one mechanism finding that is clean across both families.

## What Codex shows the template can do

`codex--student-attempt-r2`, finding 1, unedited:

> **1. Nobody can tell why 5% is enough when the case is built on 8%** [Moderate]
> Slide 8 - *"If 8% of the mailing list joins at 45 pounds, that is about 5,000 pounds in year one."*
> Slide 10 - *"Month three: full launch if the soft launch clears 5%."*
> **The problem:** You build the £5,000 case at 8% but instruct full launch above 5%, without
> showing whether either result covers delivery costs or materially offsets lost grant income.
> **Why it matters:** The board is choosing whether the scheme is worth scarce coordinator
> capacity. A 5% result can be a sensible learning threshold yet still be economically too small,
> while an 8% result can look attractive before costs yet add little net diversification.
> **Do this:** Build a 5%, 8% and 12% sensitivity showing revenue, direct costs, coordinator
> hours, net contribution and share of the non-renewing grant gap.
> **Aim for a line like:** At 5%, 8% and 12% conversion, £1,200 of delivery cost leaves £1,950,
> £3,840 and £6,360, equal to 7%, 14% and 23% of a £28,000 grant gap: that is the shape, not your
> numbers.
> **Answer first:** What minimum net contribution makes membership worth the coordinator's time?

The title is the target register. The example's arithmetic is **correct** — 5% of 1,400 at £45 is
£3,150, less £1,200 is £1,950, which is 7% of £28,000 — and it invents the two numbers the deck
does not have (delivery cost, grant gap) while reusing the ones it does.

**All six Codex examples pass both audit tests, checked by hand.** Strike the invented values and
a hole is left where the evidence goes; change an invented value and the conclusion moves. The
rule the owner ruled on is applicable by a model and auditable by a reader — **on this family.**

## What failed on Haiku

### The audit test was not run, and that is the sharpest result

`haiku--student-attempt-r1`: *"Comparable nonprofits report membership conversion of X-Y% from
engaged audiences, making 8% conservative."*

Test 1 passes. **Test 2 fails**: "making 8% conservative" is asserted whatever X-Y turn out to be,
so the conclusion cannot move, which is the definition of writing the team's argument for them.
The prompt instructs the model to run both tests and delete the example if either fails. It did
not. **A rule a model will not apply to its own output is not a boundary, it is a comment** — on
the family that will not apply it.

### The example mostly did not fire at all

2 of 10 findings, and `student-attempt-r3` produced none across three findings. Findings that went
without one include *"the gate to scale from soft launch to full launch (5% conversion) has no
explicit reasoning"*, which names a missing fact and is exactly clause 1's trigger. The field is
being skipped, not judged.

### Drafting leaked into a field with no licence for it

`haiku--student-attempt-r1`'s `Do this:` contains *"We assume 8% because [reason]. The soft launch
will test whether it holds."* — finished fill-in-the-blank text, in the field restricted to "the
move, not the words". The predicted failure was the model drafting the finding around the example.
What happened is adjacent and was not predicted: **licensing one finished sentence appears to
relax the no-drafting rule in a neighbouring field.** Not seen on Codex.

### The predicted collapse, on r3 finding 1

`The problem:` asks *"Why should a 32% event-attendance rate lead to an 8% membership
conversion?"*; `Why it matters:` answers *"event attendance is not the same as willingness to pay"*.
Same argument twice, **124 words across the pair against 88 in the old single field**. On that
finding the change is a straight regression.

The mechanical proxy did not catch it — the passage names the board and the client, so it passes
"would this still be true with no client in it". A passage can name the board and still be a
restatement. The proxy is labelled a proxy in the scorer and this is the case that shows why.

### Quote fidelity slipped, three times, on one family

Haiku cited *"The 8% assumption is conservative against the 32% attendance rate."* twice — the
deck sentence continues *"and is the main thing to test"* — and *"Two members-only events a year"*
where the deck has a lowercase "two". Content is not fabricated and quote-or-abstain has held at
0 fabrications across 55 quotes historically, but "character for character" bent on the family
that could not hold the rest of the template either. **Codex: 0 misses in 15 cited quotes.**

## The lead-mode leak

`codex--lead-nothing-r2` kept the dense shape and then **appended `Aim for a line like:` to every
finding**. One arm of four. It is additive rather than a replacement — the lead fields are all
intact — but the owner's ruling was that lead mode takes none of it, and on one arm in four it
took some.

This is the cost of the mode branch arriving exactly where it was predicted to: a second shape in
the same prompt is a second thing that can leak, and it leaked on the family that reads the prompt
more thoroughly.

## Two things that moved and were not asked to

**Finding count varies on byte-identical input**: Haiku 2, 5, 3; Codex 4, 3, 3. The review that
opened this ticket had 2. Nothing in this change touches the noise budget, so this is either
ordinary variance that two prior reviews were too few to show, or the new template makes findings
cheaper to produce. **One deck cannot separate those.**

**Severity ran cooler on Codex than the tool's own history**: 1 high impact in 10 findings, against
a tool that over-calls high impact about threefold. Haiku called 3 in 10. This is exactly the
severity-adjacent movement the ticket warned about in `Why it matters`, but the two families have
never been severity-controlled against each other, so **this number identifies a question and
settles nothing.**

## Limits

- **One synthetic deck, unusually number-dense.** Clause 1 gives an example only to findings with
  a missing fact, so a deck whose problems are mostly structural would earn very few, and this
  material cannot say whether that is correct behaviour or the rule misfiring.
- **Three repeats shows a register failing; it does not measure a rate.** "2 of 10 findings" and
  "6 of 10 findings" describe these runs. They are not estimates of how often the example fires.
- **The Haiku arms are subagents given the bundle as a conversation**, the same framing as tickets
  04, 12, 20 and 21, so the model knew it was reading a transcript. The Codex arms are piped to a
  fresh process with no such framing. **The families differ in harness as well as in model**, and
  this run cannot separate those two explanations for the split. That is the single most important
  limit here and it was inherited, not introduced.
- The change costs **+673 tokens on paste 2, +10.9%** — the largest single addition the bundle has
  taken, against the truncation interlock's 392 and each attempt-gate copy's 198.
- Nothing is released. `build-bundle.js --release` still refuses while the Drive folder is unset.


---

# Round 2, 2026-09-21 to 2026-09-24: simplified for the weaker model, and reverted

The owner ruled **B** on the family split: cut the template to what the weaker model can hold,
then re-run both families. Two devices came out -- the plain-English title rule and every
sentence cap, both 0 of 10 on Haiku and produced unprompted by Codex. The boundary was not
weakened but **moved from a self-audit to a sentence form**: the example fires only where
`Answer first:` asks for a fetchable fact, and must be a conditional whose invented value is
the answer to it, so the flip test is carried by grammar rather than by the model agreeing to
check itself.

**It was worse on both families, and it is reverted.**

| worked example | round 1 | round 2 |
|---|---|---|
| Haiku 4.5 | fired **2 of 10** findings | fired **10 of 11** -- but by hand only 3 or 4 satisfy the rule, and **3 contain finished slide text** |
| Codex | fired **6 of 10**, all 6 passing both audit tests | **0 of 9** |

The rule tied the trigger to a judgement about a neighbouring field and **the two families
resolved that judgement in opposite directions**: Codex to never, Haiku to always. Haiku's
compliance is the worse outcome of the two, because the conditional form arrived as a shell
with a draft inside it -- *"For priority booking, 'members receive an email 48 hours before the
general public with a direct purchase link'"* is the parked feature, shipping.

**What held in round 2, on both families:** the field names, the habit section's absence, the
word budget, and the mode branch -- **no bleed on any of the four lead arms**, where round 1
leaked on one. The added lead clause is kept on revert.

## The confound, and clearing it

Round 1's Codex ran on binary `247581e40ee272fb`; **Codex self-updated and deleted it**, so
round 2 ran on `80f78947ad880e6e` (codex-cli 0.155.0-alpha.16.3). **Two variables moved between
the two Codex results**, which is the error this map has a standing caution against, and it was
introduced here rather than inherited.

Cleared by running the **round-1 template on the new binary**: 3 arms, 9 findings, **5 worked
examples**, every one a conditional with an invented figure and the disclaimer. Four of the five
pass both audit tests by hand; the fifth -- *"If the first ten memberships require six
coordinator hours each month, compare that workload with the capacity available"* -- has a
consequent that survives any value, so it **fails the flip test**.

So the round-2 collapse to zero is **caused by the template change, not the binary**, and
round 1's Codex result reproduces on an instrument that still exists: 6 of 10 then, 5 of 9 now.

## Where that leaves the amendment

On the best template tried, over two rounds and twenty-three runs:

- **Codex: the amendment works.** The example fires on about half the findings, is a conditional
  built on an invented figure, and passes the reader's audit 10 of 11 times across both binaries.
- **Haiku 4.5: it does not.** It fires twice in ten, carries the disclaimer zero times in two,
  and one of the two asserts *"making 8% conservative"* regardless of what the student finds --
  which is the exact claim the finding says is unsupported. An example that appears rarely and is
  sometimes actively misleading is the shape of the failure.

**Nothing here is a third wording attempt waiting to happen.** Two rounds moved the same device
in opposite directions on the two families, which is the evidence that the wording is not the
variable in control.


---

# Round 3, 2026-09-24: the owner's criterion, and the withdrawal

The owner reframed what the device is for: **not a final truth, but students having confidence in
work they can ground in evidence they found themselves.** That narrows the bar and makes absence
acceptable:

- a good conditional example models grounded confidence -- the win;
- **no example is neutral** -- the student is no worse off;
- an example that hands over a conclusion is the only harmful outcome, because it is confidence
  without the grounding.

Round 3 kept round 1's trigger (which is what makes the example fire) and added round 2's
**conditional form** (which is what makes asserting a conclusion structurally hard), plus an
instruction to omit when in doubt.

**Pre-registered before the run:** pass = zero examples, either family, asserting a conclusion the
invented figure does not control. Firing rate explicitly not a bar. Guards: no drafting in
`Do this:`, lead mode unchanged.

## It failed, 3 of 10

Six arms, 20 findings, 10 examples. Seven are clean conditionals whose conclusion moves with the
invented figure -- for instance *"If a comparable or representative test converts at 3%, projected
membership income falls far below the 8% case, so the board should revisit the offer."*

Three failed, and one is the harmful kind:

> *"If <specific driver> converts attendees to members, then <comparable organization> sees
> <percentage>, **which aligns with your 8% target**."* (Haiku r1)

Three empty slots, no invented figure, and the conclusion -- your 8% is fine -- asserted whatever
fills them. **That is the round-1 defect recurring under a third wording**, and it is exactly the
failure the owner's criterion names.

The other two fail the flip test without handing over a claim: one has no invented figure at all
(a conditional shell around a plan), one has a figure whose consequent survives any value
(*"the team can test whether that fits"*).

## The deciding evidence was not the examples

`Do this:` is restricted to "the move, not the words" and has never had an exception. Across the
same six arms it produced **three finished, pasteable sentences**:

> *Drop "conservative." Say **"The 8% assumption is unproven and the main thing to test."***
> *Clarify in one phrase: **"1,400 people on its mailing list, of which 32% attended at least one
> event in 2024 (so ~450 active attendees per box-office data)."***

The second is built entirely from the team's own figures and needs no evidence they do not already
have. **That is the original "no drafting" objection returning verbatim** -- the human does not
have to visibly edit anything, because the sentence is finished.

## The withdrawal, and the verification

`Aim for a line like` and its rule block are **removed from the prompt**. What stays is the half
that held on both families in all three rounds: the `The problem:` / `Why it matters:` split, the
deleted habit section, the lead-mode dense shape, the fixed word overrun. `Do this:` is hardened
against pasteable text. Paste 2 cost falls from **+808 tokens to +383 (+6.2%)**.

Verified on four student arms, both families: **no example line anywhere, the field split intact
on every finding, the habit section absent, lead mode unchanged.**

## A correction to this document's own causal claim

An earlier draft of this file said that licensing one finished sentence relaxed the no-drafting
rule in the neighbouring field. **The withdrawal arms do not support that as stated.** With the
example gone, Haiku still produced pasteable parentheticals in `Do this:` -- *"(e.g. 'this is about
the size of Project Grant X from 2024')"*, *"(e.g. 'from past attendees and campaign sign-ups')"*
-- three of them across two arms, with nothing licensing them. Codex produced none.

What the evidence supports is weaker and worth stating precisely: the leak is **worse** under the
amendment (three full slide sentences in six arms) and **milder but present** without it (three
short phrases in two arms, one family). The worked example aggravated a problem in `Do this:`; it
did not create it, and the hardening added here is **not sufficient**. That is a separate defect
and it gets its own ticket rather than being folded into this one.

## An interlock false alarm, on a complete bundle

`codex--student-attempt-r2` **refused** on its first run -- *"KEYS: MISSING/OMEGA-9X. Part 1 is
missing"* -- on a bundle that contains both keys and is **byte-identical to r1**, which reviewed
normally. Re-run on the same bytes, it reviewed normally too.

Ticket 12 measured false alarms at **0 of 14 complete-bundle runs**. This is the first observed,
and it is **stochastic on identical input**, which is the same class of defect as the readiness
level returning two answers on the same bytes. A student hitting it is told to re-paste when
nothing is wrong. Preserved as `runs/codex--student-attempt-r2--refusal1.md`. Not ticket 26's to
fix; raised separately.
