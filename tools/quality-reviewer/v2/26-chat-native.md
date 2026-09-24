# 26. The chat-native path

Three pastes into any chat window. No Project, no login, no paid tier, no renderer, no
repository. Built 2026-08-09 because the hosted path reaches a team that already has a Claude
Project and a lead who knows what a JSON file is, and that is not most of 180 Degrees
Consulting.

Two artifacts came out of it. [CHAT-CONTEXT.md](CHAT-CONTEXT.md) is the pasteable document, and
it is the deliverable: part one is calibration knowledge distilled from the human gold
worksheets, part two is the output format. The prompt moved to `frozen-2026-08-09`, sha
`2371607aa850b674`, on a five-line edit to its OUTPUT block and nothing else.

Voice rules apply.

---

## 1. The shape, and the one prompt edit

| paste | what | where it lives |
|---|---|---|
| 1 | the system prompt | [04-prompt-templates.md](04-prompt-templates.md) section A, unchanged apart from section 1.1 |
| 2 | the calibration context and the output format | [CHAT-CONTEXT.md](CHAT-CONTEXT.md), whole file |
| 3 | the brief and the deliverable | [04-prompt-templates.md](04-prompt-templates.md) section B, filled in |

### 1.1 What changed in section A

Five lines appended to the OUTPUT block, and nothing else anywhere in the prompt:

> One exception, and only one. If the material you were given includes a context document that
> defines a chat-native output format, write that format instead of the JSON and follow its
> layout exactly. Everything above still binds unchanged: the same lenses, the same synthesis
> protocol, the same blocking rules and ceilings, the same severity definitions, the same noise
> budget, the same quote-or-abstain rule. Only the shape of what you return changes. If no such
> document is present, return the JSON.

The build prompt's hard line was that the synthesis protocol, the blocking rules, the ceilings,
the severity definitions and the noise budget must not be touched while adding an output format.
None of them was. The edit is inside OUTPUT, which is a statement about the shape of the return
value, and it restates the five protected things as still binding rather than modifying any of
them.

**The switch defaults to JSON and the harness never flips it.** `run-reviews.js --emit-packs`
builds a pack from section A plus the mode table, the scope matrix and the output contract. It
has never included a context document and does not now, so every scored run stays on the JSON
branch. That was the reason to key the switch on the presence of a context document rather than
on a new field in the section B template: the input template is read by
`loadInputTemplateLabels()` and asserted against the pack the harness builds, so a new field
there is a change to the measured path. A conditional the harness cannot satisfy is not.

Version bumped to `frozen-2026-08-09`. `frozen-2026-08-05e` archived verbatim at
`eval-runs/prompt-archive/frozen-2026-08-05e.txt` and **re-hashes to `5a8d4ef2d651a064`**, the
value STATUS.md carried for it, so reverting the whole change is one file copy.

### 1.2 Why the output format is defined in the context file and not here

Only what the user pastes reaches the model, and nobody on this path pastes a numbered document
out of this folder. So the normative text of the format has to live in `CHAT-CONTEXT.md`. A copy
of it in these pages would be a second source that drifts from the first, and the drift would be
invisible, because the copy would be the one nobody ever runs. This document describes the
format and does not restate it.

---

## 2. Constraint 1: no client-recoverable content, because this file will be public

`CHAT-CONTEXT.md` is the most widely distributed thing this project will produce. It gets pasted
into services this project does not run, by students, at branches nobody here will meet. Assume
it is public, because it effectively is.

Its raw material is the eleven human gold worksheets in `eval-cases-real/labeling/`, which are
gitignored because they name findings on real client deliverables. Specifically the five
sections the owner's 2026-08-02 correction identified as the valuable part: acceptable AI
feedback, unacceptable AI feedback, false positives to avoid, false negatives to catch, honest
uncertainty. **Not the readiness levels.** The golds are not an answer key to optimise against,
they are a record of how a human team lead reasons, and the reasoning is what was extracted.

### 2.1 The confidentiality self-audit

The draft was re-read against one question: could a person holding the fourteen real decks match
any passage to one of them. Six passages failed and were rewritten.

| what the source said | what would have identified it | what shipped |
|---|---|---|
| a specific slide count on one method against a specific count on another | the ratio is distinctive enough to fingerprint one deck | "many pages on the method the team enjoyed, one or two on the question the client is actually paying for" |
| two named sample sizes under a pricing conclusion | the pair of numbers is unique | "a small qualitative sample is fine for finding out what people care about. It is not fine as the sole basis for a pricing or monetisation decision" |
| a specific commission band recommended with no derivation | the band plus the artifact type recovers the case | "a number driving a recommendation with no reasoning behind it. A percentage, a rate, a price point, stated and never derived" |
| a closing section of a stated length containing no recommendations | length plus shape is close to a fingerprint | "the closing section names no decision, or names a decision without choosing" |
| a named persona treated as a real person exposed | the name is in the deck | "a named person in an illustrative scenario is not a confidentiality breach" |
| a named financing instrument the labeler did not recognise | names the sector and the case | folded into "whether the recommended funding route, partner, channel or model is the right one is very often not answerable from the artifact" |

**Categories excluded entirely rather than abstracted.** No sector nouns appear anywhere in
`CHAT-CONTEXT.md`, not one, because the eleven cases span eleven sectors and a sector word plus
a pattern is a match. No geography. No client names or pseudonyms. No case identifiers. No
verbatim text from any real deliverable. No figures from any real deliverable. No labeler
initials or dates.

**Readiness distributions were excluded on a second ground.** Aggregate counts across eleven
cases identify nobody, so confidentiality allowed them. They were left out anyway: publishing
how often human leads reached each level invites a reviewer to fit the distribution, which is
exactly the answer-key use the owner's correction rules out. The file teaches the reasoning and
sends readiness back to the blocking rules.

**What remains, honestly.** Two things survive that are worth naming rather than hiding. The
file says one deliverable in the labelled set had nothing worth praising, and that is a true
statement about one real deck, though it names nothing and eleven candidates remain. And the
pattern list is, in aggregate, a portrait of what this branch's student work looks like. Neither
recovers a client, and a reader who already holds the decks learns nothing from either that they
do not already know. The file states in its own section 0b that it is deliberately free of
client material and why, so a reader can hold it to that.

---

## 3. Constraint 2: the controls have to move into the output

This is the part most likely to be got wrong. In the renderer, three things are enforced by
code: no quote reaches anyone until it is machine-checked as a verbatim substring of the deck,
readiness and every blocking ceiling are stripped out of the student payload rather than hidden
in the view, and a committed flag plus a redeploy withdraws the tool. **In a chat window none of
that exists.** No quote check, no redaction, no kill switch, no record.

You cannot enforce. You can only construct. What construction bought, control by control:

| control | in the renderer | in chat | honest gap |
|---|---|---|---|
| readiness never reaches a student | stripped from the payload, a `MutationObserver` replaces the view if a level string appears anywhere | **no readiness level, ceiling, blocking-rule number or overall score is generated at all.** Nothing is fenced because nothing needs to be | **none on this control.** A value that is never written cannot leak. This is stronger than the renderer's, and it costs a signal A4 showed was not repeatable |
| every quote verbatim | `check-review-v2.js` normalisation, run in the browser, nothing outbound until it passes or a written waiver is recorded | the output tells the lead, in three numbered lines it cannot skip, that each finding carries a quote and a location, that finding each one takes seconds, and that a quote that cannot be found means the finding is **discarded, not softened** | **a lead's eyes are not a substring check.** It catches the blatant case and misses the near-miss |
| the grade is not the product | the picker chip reads "AI guess", the level is never preselected, differing requires a written reason | there is no grade to warn about. Every review prints why one is withheld: the same deliverable has been given two different answers on identical input | **transfers by removal.** The warning became unnecessary rather than weaker |
| the client prohibition | stated in the workflow and the trust boundary | printed in every single review, at the top, before the findings | transfers intact |
| the kill switch | a committed flag plus a redeploy | **nothing.** Two documents someone pasted into a service this project does not run | **no mitigation exists.** Recorded in [22-trust-boundary.md](22-trust-boundary.md) section 4 |

### 3.1 The layout decision that does the work

**There is no layout decision, and that is the decision.** An earlier version of this sprint
built three blocks — lead-only, team-facing, lead-only — with the forwardable part sandwiched so
that no lazy selection was ever right. It was careful work and it was solving the wrong problem.

Fencing assumes someone stands between the model and the reader, and on this path nobody does.
The person who pastes the deliverable in is the person who reads the reply. A marker asking a
human not to forward a block is a control whose whole strength is the presence of a second human
who was never there.

So the output is one review, forwardable whole, followed by a paste-back record. Nothing is
fenced, nothing has to be stripped, and there is no correct-versus-lazy way to copy it.

### 3.2 The scorecard is not produced either, for the reason the fencing failed

The renderer strips readiness and blocking ceilings from the student pack and leaves the
scorecard in, because it surrounds the number with a label, a legend and a warning strip saying
which half of the tool to trust. Chat prose has none of that furniture, and "2.6 of 5" reads as
a mark on someone's work whatever sentence sits beside it.

The earlier version moved the number to the lead-only block. With no lead-only block, the same
reasoning gives a cleaner answer: **do not compute a grade-shaped thing for this path at all.**
The three weakest dimensions are still named, because "your evidence and your framing are the
weak points" is coaching. The number is not, so it is not written.

### 3.3 The answer on the trust boundary

An earlier draft of this document scoped the chat path to leads, reasoning that a marker is
weaker than a redaction plus an assertion. The reasoning was right and the conclusion was wrong,
because **restricting the audience was never an available solution.** 180DC consultants are
students, many have no chargeable budget and no paid AI account, and a control bought by
excluding the people the tool exists for protects nobody — it leaves the same students reviewing
their own work with nothing at all.

The control therefore moved from redaction to non-production, which the table above records
control by control. Row two of `22-trust-boundary.md` turns on a readiness level never reaching
a student. On this path no level is generated, so the bar is **met by construction** and the
route is open to anyone. Section 1a there carries the full reasoning and the limits that remain
— no machine quote check, no kill switch on a paste, no measurement on the free models most of
the audience will use. Those are named as limits of the route, not as reasons to withhold it.

---

## 3.4 Parity with the hosted desk, and why it is deliberate

The two doors do **not** carry the same information, and that was decided with the difference on
screen rather than by drift.

| | hosted desk | three-paste chat |
|---|---|---|
| findings, quotes, fixes, coaching | yes | **identical** |
| readiness level | shown, labelled "AI guess", never preselected | **not produced** |
| diagnostic mean out of 5 | shown | **not produced** |
| blocking rule numbers and ceilings | shown | **not produced** |
| ten-criteria scorecard | full | weakest three named, no numbers |
| deck timeline | shown | not available in prose |

**How to explain it to a branch in one line:** both doors give you the same findings, and neither
gives you a grade you should pass on.

The delta is exactly the half of the output this project's own evidence does not support. A4 says
the level returns R0 and R2 on byte-identical input. The desk shows it anyway because the desk can
cage it, and its own status board says so on screen: "Unstable: it has returned two different
levels on identical input", above a panel headed "THE AI GRADE: DO NOT PASS IT ON". An anchor the
product instructs the lead to discount is not information the chat path is missing.

Recorded in [11-decision-log.md](11-decision-log.md), 2026-08-09.

---

## 3.5 The free visual route, and the packaging defect it exposed

**A free user can have the hosted desk today, with no new code.** Tested 2026-08-09 on Haiku 4.5,
the weakest model available, blind.

The renderer is a single self-contained page that runs in the browser and is served from a public
URL with no login. It was never the paid half of the product; the only thing gating a free user
from it was producing the JSON it eats. Haiku produced JSON that `check-review-v2.js` accepts:
contract-valid, every quote verbatim against the deck, ten dimensions scored, `diagnosticMean`
3.3 recomputing to 3.3 exactly, blocking rule 1 fired, and readiness matching the human gold.
Runs in [eval-runs/chat-native-2026-08-09/](eval-runs/chat-native-2026-08-09/).

So the free route is: paste section A, `03-output-contract.md` and the filled brief into any chat,
take the JSON, open the renderer, paste. The desk that comes back carries the same quote gate, the
same locked outbound buttons and the same redacted student pack a Claude Code user gets, **because
the caging lives in the page rather than in the account.**

**The packaging defect.** The first attempt at this test failed on both Haiku and Sonnet with
eight and eleven contract violations, and the cause was not model capability. Section A instructs
the reader to return JSON "matching the v2 output contract exactly" and **does not contain the
contract**, which lives in `03-output-contract.md`. The harness never hit this because
`run-reviews.js` injects the contract into every pack. Any human pasting section A into a chat
window gets an instruction that cannot be followed, at any model strength.

Fix required, not yet applied: section A either inlines the contract or states plainly that the
JSON path needs `03-output-contract.md` pasted alongside it. Today it says neither. The
chat-native path does not have this problem, because `CHAT-CONTEXT.md` carries its whole template
inline, which is why it worked first time on every model tested.

**Consequence for the prose-to-JSON parser idea:** downgraded from required to optional. It would
still save a paste and move the arithmetic off the model, but it is no longer the thing standing
between a free consultant and the full experience. Nothing is.

---

## 4. Constraint 3: a review nobody records is invisible

The pilot answers one question, whether communication findings are the ones leads actually keep,
and it answers it by joining `decisions[]` to `ai.findings[].issueType` on the override record.
Chat produces prose, so by default it produces nothing, and if most teams end up on this path
the evidence base stops growing exactly when it starts mattering.

The third block is a pre-filled record. **The reviewer fills everything it knows** and leaves
nulls only where the lead is the source: the timestamp, the model they ran it on, a reference
for the deliverable, their own id, `vsByHand`, how many quotes failed their check, an action per
finding, the must-catch, and their own readiness call with a reason. That is a two-minute job
because the reviewer did the typing.

Field names match `buildRecord()` in `index.html`. Three deliberate differences, each because
the underlying thing is genuinely different:

| field | hosted | chat | why |
|---|---|---|---|
| `recordVersion` | `override-log-2` | `override-log-2-chat` | a chat record has no machine quote check behind it and no review JSON it can be replayed against. A consumer has to be able to tell them apart. `applyRecord()` in `index.html` rejects it by design rather than by accident |
| `quoteCheck.status` | `passed`, `failed` or `waived` | `lead-eye-check` | naming a human check with the enum used for a mechanical one would be the same lie the trust boundary is built to avoid |
| `findings[].fid` | first six hex of a sha256 over the short title and first quote | `f1` to `f5` | a chat model cannot compute a sha reliably. The join the pilot actually runs is `decisions[].fid` to `ai.findings[].fid` inside one record, so a locally unique id is sufficient. It does not join across records, and it never did |

Everything the pilot query needs is present and named identically: `decisions[].action` with the
same `keep`, `ask`, `cut` vocabulary, `decisions[].cutReason` from the same closed list of five,
`ai.findings[].issueType` from the same five values, `ai.findings[].severity`,
`ai.findings[].dimension`, `mustCatch`, `readinessCall.lead`, and `lead.vsByHand`. **The two
paths feed one dataset.**

**Corrected 2026-09-20 (ticket 05, applied by ticket 20).** This paragraph used to say the
query joins `readinessCall.ai` against `readinessCall.lead`. That join was already impossible
on the path this document describes -- the chat path has always set `.ai` to null, because the
reviewer was never asked for a level -- and as of 2026-09-20 the field does not exist in either
record variant. The lead's own call survives and is the only readiness field in the record. It
is also the only field in the record that is not a reaction to the tool's output, which is why
ticket 05 kept it.

---

## 5. Constraint 4: honesty about the model

Every number this project has, including blocking rules missed 0% and no fabricated quote ever
surviving to a scored result, was measured on Claude Opus 5 at high effort. Run the same prompt
on a small free model and none of those numbers describe what the student is holding. Nobody has
looked. `20-running-it-free.md` section 4 says exactly this and says the measurement is cheap
and bounded.

`CHAT-CONTEXT.md` section 0 is the second thing in the file, before any calibration content, and
it is a four-row table with the word **unmeasured** in it twice. It also carries the row that is
true on every model, that the readiness level returned two different levels on identical input,
and ties that to why the format hides it.

It is not softened. It also does not discourage free use, because affordable access is the
entire point of the project: the closing line is that free access is the point rather than a
compromise, run it on whatever you have, and do not tell anyone the results carry evidence they
do not carry. The training opt-out from section 5 of that document is restated there too, since
a student on a free tier is the exact person the 2026 policy defaults are aimed at.

---

## 6. Demonstrated end to end

> **SUPERSEDED 2026-08-09, and deliberately not doctored.** Everything in this section was
> produced under the earlier three-block format, before the path was reopened to all consultants
> and the readiness level was removed from it entirely (sections 3.1 to 3.3). The output below is
> a real model response and it is left exactly as it came back, because editing it to look like a
> demonstration of a format it was never asked to produce would make this document a fabrication
> rather than a record.
>
> **What still holds:** the findings themselves, the twelve verbatim quotes, the four-against-a-
> budget-of-five restraint, and every gold comparison in 6.3. None of those depend on the block
> structure.
>
> **What is void:** every claim about block separability, marker discipline and where
> ceiling-shaped content sits — there are no blocks now. The `ai.readiness` and
> `readinessCall.ai` fields shown in the paste-back record no longer exist.
>
> **Extended 2026-09-20 (ticket 20).** The record reproduced further down this document is a
> frozen demonstration and is now two versions behind. It stamps `override-log-2-chat` and
> `frozen-2026-08-09`; the shipped block stamps `override-log-3-chat` and `frozen-2026-09-19`,
> carries a `student` block and an `attempt` field, and has no `readinessCall.ai`. **Read the
> block in [CHAT-CONTEXT.md](CHAT-CONTEXT.md), never the copy below.**
>
> **The corrected format is unverified.** It has never been run. Re-running this demonstration
> under the current `CHAT-CONTEXT.md` is the first task of the next session, and until it happens
> nobody should describe the chat path as demonstrated.


Run on `eval-cases/case-01-vague-recommendation.md`, synthetic and fully anonymized, because the
output of this test goes in a document and no real deliverable can. Deep mode. The case has a
human gold at `eval-cases/case-01.gold.md`, so the review can be checked for the things the gold
says a review must catch and must not say.

### 6.1 Paste 3, the input

```
MODE: deep
CLIENT TYPE (anonymized): a regional food-redistribution non-profit, call it Client A
ARTIFACT TYPE: draft deck
CLIENT QUESTION: should Client A expand into a neighbouring region (Region B) or deepen
  operations in its current region
INTENDED AUDIENCE: the executive director and the board
PROJECT STAGE: mid
DRAFT MATURITY: working draft
SPECIFIC FEEDBACK REQUESTED: is the recommendation strong enough to take to the board
KNOWN CONSTRAINTS: one warehouse, two vans, volunteer drivers, one full-time coordinator
WHAT THE TEAM IS UNSURE ABOUT: whether we have enough on Region B to recommend it
EVIDENCE AND SOURCE NOTES: operating figures come from Client A. The Region B growth
  figure came from an early conversation and the team has not traced it to a source.
RECOMMENDATIONS (if any): expand to Region B
IMPLEMENTATION PLAN (if any): open a satellite hub in Region B

DELIVERABLE TEXT (one block per slide or section, with numbers):
<the ten slides of case-01-vague-recommendation.md>
```

### 6.2 The actual output

```
REVIEW OF: draft deck, 10 slides, regional strategy | MODE: deep
Two blocks follow. The middle one, between the BEGIN and END markers, is the only part
that goes to the team. Read the first block before you forward anything.

=== FOR THE LEAD ONLY. DO NOT FORWARD ANY PART OF THIS BLOCK. ===

READINESS: Needs substantial revision
Why this level: Needs substantial revision, because the recommendation to expand rests on a
growth figure the deck never sources, so the core decision is not yet supported.
Blocking rules fired:
  Rule 2, core recommendation unsupported. Ceiling: Needs substantial revision.
  Rule 4, ungrounded number the recommendation depends on. Ceiling: Needs targeted revision.
Confidence: Medium. Could change if: a sourced Region B demand estimate exists outside the
deck, or the recommendation turns out not to depend on that growth figure.
Diagnostic mean: 2.6 of 5. This is diagnostic, not a verdict. Weakest dimensions: Risks,
assumptions and uncertainty (1.0), then Evidence quality, Recommendation specificity,
Feasibility and implementation, Analysis and insight and Slide-level communication, all
level at 2.0.
Effort to close the findings below: 4 to 6 hours.

THREE THINGS TO DO BEFORE YOU USE THIS
1. Check the quotes. Every finding below carries a verbatim quote and a location. Find each
   one in the deliverable yourself. It takes seconds. A quote you cannot find means that
   finding is discarded, not softened. Nothing is checking this but you.
2. Work from the findings, not from the level. On this project the findings have never missed
   a problem a human rated blocking. The readiness level has returned two different answers on
   identical input, so treat it as a prompt for your own judgement and set your own level.
3. This deliverable does not go to the client on this review alone, at any level, ever. A
   named human signs off on client work. That rule does not move.

Questions to ask the team:
  Where did the 40% Region B growth figure come from, and has anyone traced it to a source.
  Did the team ask Client A whether it has the funding and the staff for a second site, or is
  that assumed. The deck does not say either way and I did not treat it as a finding.
  Has the unmet demand in Region A been quantified. Without it the two options cannot be
  compared on the same basis.
  What would success look like twelve months after whichever option is chosen.
What this review could not assess:
  Whether the 40% growth figure is true. No source was given.
  Whether Client A can fund or staff a Region B hub. The deck does not say.
  Visual design, layout and any chart. Only slide text was provided.
  Board politics, and whether either region is already favoured.

=== END OF THE LEAD-ONLY BLOCK. NOTHING ABOVE THIS LINE IS FORWARDED. ===


=== BEGIN NOTE TO THE TEAM. This block, and only this block, is what you forward. ===

WHAT WORKS
You put two real options on the table and gave each its own page, rather than presenting one
answer and defending it. Slide 6: "Add a second warehouse shift and recruit more volunteer
drivers to meet unmet demand in the current region." Slide 7: "Open a satellite hub in Region
B to serve the 30 new partners and capture the growing demand there." That is the right shape
for a decision the client has to make.

You commit to an answer. Slide 8: "Client A should prioritize Region B." Plenty of drafts
never do.

WHAT TO FIX, IN ORDER

1. The recommendation rests on a growth figure the deck never sources. [High impact]
   Where: slide 5
   Quote: "Region B demand will grow 40% over the next three years."
   Why it costs the client: the whole case for Region B is that it is the bigger prize, and
   this number is what makes it bigger. If it is wrong, the client has committed a warehouse
   and staff to the wrong region, and nothing in the deck lets them check it.
   What to do: trace the figure to whoever produced it and put the source, the baseline and
   the method on the slide. If it cannot be traced, say so on the slide and show whether the
   recommendation survives without it.
   Answer first: if that 40% turned out to be 10%, would you still recommend Region B.

2. The recommendation names actions without saying what any of them is. [Moderate]
   Where: slide 9
   Quote: "Scale up operations and improve partnerships to serve the new region."
   Why it costs the client: a director reading this cannot start anything on Monday. Scale up
   by how much, improve which partnerships, who does it and by when are all still on the
   client's side of the table, which is where the team was meant to take them from.
   What to do: give each action an owner, a first step, a timeframe and something measurable.
   Slide 10 needs the same treatment: "Review progress in due course." names no date and no
   measure.
   Answer first: what is the single first thing someone at Client A does on Monday morning.

3. Your answer arrives on slide 8 and the reason for it never arrives at all. [Moderate]
   Where: slides 2, 4, 8
   Quote: "Agenda"
   Quote: "Current operations"
   Quote: "Our view"
   Why it costs the client: read the titles and the opening line of each page, which is what a
   busy director does, and the deck is a list of topics with a verdict near the end. No single
   sentence anywhere both names the decision and gives the reason for it, so the reader gets
   the answer without the argument and cannot defend it to anyone else.
   What to do: put one sentence at the front that names the choice and the reason in the same
   breath, then make every page title a claim that supports it rather than a label for what is
   on the page.
   Answer first: write your recommendation and its reason as one sentence. If it takes two,
   you have not settled which reason is the load-bearing one.

4. Your numbers are never measured against anything, so the reader cannot tell what they mean.
   [Moderate]
   Where: slides 4 and 5
   Quote: "In the last year Client A moved 620 tonnes of food."
   Quote: "Region B has 30 potential partners and no comparable redistributor."
   Quote: "Partner demand in Region A frequently exceeds supply."
   Why it costs the client: 620 tonnes against what, and 30 partners against the 40 the client
   already serves, is the comparison the whole choice turns on. Region A's unmet demand is
   called real but is never sized, so the two options are argued on different terms and the
   client cannot weigh them.
   What to do: size the unmet demand in Region A in the same unit you use for Region B, then
   say what each number means rather than only what it is. Do not invent a comparator. If the
   Region A figure does not exist yet, go and get it, because the recommendation depends on it.
   Answer first: for each number on the page, so is that good or bad, and how would a reader
   know.

THE HABIT TO BUILD
A recommendation is only as strong as the weakest number under it, and this deck names the
number and never goes back for it. The habit to build is the check before the conclusion: list
every claim your recommendation depends on, write the source next to each, and treat any blank
line as the next piece of work rather than a detail to tidy later. Try it on this deck now, on
one page, and see how many lines come back blank.

WHAT THIS REVIEW COULD NOT JUDGE
Whether the 40% figure is actually right. Whether Client A can afford or staff a second site,
which the deck does not say either way, so it is a question for your lead rather than a
criticism of your work. Anything visual, because only the text was provided.

HOW TO CHECK THIS FEEDBACK
Every point above quotes your own deliverable and says where. If you cannot find one of these
quotes in your own work, that point is wrong. Tell your lead and drop it. This review advises.
A human decides, and nothing here goes to your client on its own.

=== END NOTE TO THE TEAM. ===


=== FOR THE LEAD ONLY. DO NOT FORWARD. Paste-back record. ===

Fill the nulls after you have triaged, then send this block back to whoever runs the reviewer.
It is the only trace a chat review leaves, and the question it answers is which findings leads
actually keep. Two minutes.

Fill: capturedAt, model, deliverable.ref, lead.id, lead.vsByHand, quotesMissing, an action for
every finding ("keep", "ask" or "cut", plus a cutReason when you cut), mustCatch, and your own
readinessCall.lead with a one-line reason. cutReason is one of: wrong, not-an-issue, too-minor,
duplicate, out-of-scope.

{
  "recordVersion": "override-log-2-chat",
  "capturedAt": null,
  "reviewer": {
    "promptVersion": "frozen-2026-08-09",
    "mode": "deep",
    "executionMode": "chat",
    "model": null
  },
  "deliverable": {
    "ref": null,
    "artifactType": "draft deck",
    "stage": "mid"
  },
  "lead": { "id": null, "secondsOnTask": null, "vsByHand": null },
  "quoteCheck": { "status": "lead-eye-check", "quotesChecked": 12, "quotesMissing": null },
  "ai": {
    "readiness": "Needs substantial revision",
    "blockingRules": [2, 4],
    "findings": [
      { "fid": "f1", "short": "Unsourced growth figure", "severity": "critical",
        "issueType": "evidence", "dimension": "Evidence quality", "slides": [5] },
      { "fid": "f2", "short": "Vague recommendation", "severity": "major",
        "issueType": "recommendation", "dimension": "Recommendation specificity",
        "slides": [9, 10] },
      { "fid": "f3", "short": "No governing insight", "severity": "major",
        "issueType": "communication", "dimension": "Storyline and pyramid logic",
        "slides": [2, 4, 8] },
      { "fid": "f4", "short": "Numbers without comparators", "severity": "major",
        "issueType": "thinking", "dimension": "Analysis and insight", "slides": [4, 5] }
    ]
  },
  "decisions": [
    { "fid": "f1", "action": null, "cutReason": null, "note": "" },
    { "fid": "f2", "action": null, "cutReason": null, "note": "" },
    { "fid": "f3", "action": null, "cutReason": null, "note": "" },
    { "fid": "f4", "action": null, "cutReason": null, "note": "" }
  ],
  "added": [],
  "mustCatch": null,
  "readinessCall": { "ai": "Needs substantial revision", "lead": null, "reason": "" },
  "sent": false
}

=== END. ===
```

### 6.3 What the demonstration confirms

**[VOID — no blocks in the current format.] The lead-only block is separable.** Three markers, written in full. The team-facing block is
sandwiched between `BEGIN NOTE TO THE TEAM` and `END NOTE TO THE TEAM`, and everything
ceiling-shaped is outside it: the level, both rule numbers, both ceilings, the confidence, the
diagnostic mean and the questions for the lead. **Checked mechanically**: none of the four level
strings, no ceiling and no blocking rule number appears anywhere between the two team markers.
The one place the boundary was nearly breached is worth recording. Finding 1 wants to say the
deck is not ready for the board, and that phrasing is a level in everything but spelling. It is
written as the consequence to the client instead, which is what the prompt's `why` field asks
for anyway.

**The quotes are checkable.** Twelve quotes in the team block, each with its location, and
**all twelve verified as verbatim substrings** of `eval-cases/case-01-vague-recommendation.md`
under the same whitespace normalisation `check-review-v2.js` uses. The reader-test finding gives
each title its own quote line rather than joining three titles into one string, per the evidence
rule. Nothing in the lead-only block quotes the deck, so a lead who checks the team block has
checked everything that could reach anyone.

**The paste-back block parses.** `JSON.parse` accepts it as emitted, before the lead fills
anything. Four findings, four decision rows, same ids, same order.

**Against the gold.** The gold's single most important issue is the 40% figure, and a review
that misses it fails the case. It is finding 1. The gold's second and third issues are the vague
recommendation and the late governing insight with label titles, which are findings 2 and 3. The
gold's unacceptable list forbids rewriting slide 9, inventing a source, and claiming Client A
lacks capacity. No finished text is offered anywhere, no source is invented, and the capacity
question is in the lead's questions with an explicit note that it was not treated as a finding.
The gold's false positives are visual design, tone, and the client's own operating numbers on
slides 3 and 4. None is flagged. The 620 tonnes figure on slide 4 appears in finding 4, and not
as an unsourced claim: as a number with nothing to measure it against, which is a different
complaint and a legitimate one.

**Restraint held.** Four findings against a deep budget of five. Three candidates were pruned by
lens I: the absent risk and assumption layer, which the sourcing fix largely subsumes, the
feasibility gap, which the gold correctly says must be a question rather than a finding, and the
empty next-steps page, which folded into finding 2 rather than standing alone.

**What the demonstration does not show.** It was produced on Claude Opus 5. Whether a small free
model holds this layout, keeps the markers intact and keeps the level out of the middle block is
the single most important open question about this path and it is not answered here. See
section 7.

---

## 7. What is not solved

**1. Nobody has run this on a free model, which is the entire audience.** The format asks a
model to hold three delimited blocks, keep four specific strings out of one of them and emit
parseable JSON at the end. That is more structural discipline than the JSON path asks for, not
less, and it is being asked of weaker models. `20-running-it-free.md` section 4 already says the
comparison is cheap and bounded and that nobody has done it. This adds a second thing to measure
in the same run, and it is a sharper test than the JSON one, because a format failure here leaks
a readiness level rather than failing a validator.

**2. Nothing verifies that the level stays out of the team block.** In the renderer an assertion
fires and the view is replaced. Here the check is a sentence in the format and a human reading
the output. The cheapest real fix is a twenty-line local script that takes the pasted reply,
finds the two markers, and refuses to emit the middle if it contains a level string, a ceiling or
a rule number. That is the thing that would move the trust-boundary row, and it is not built.

**3. The paste-back record depends on a lead choosing to send it.** The hosted path produces a
record as a side effect of a workflow the lead was doing anyway. This one is a separate act of
goodwill at the end. Pre-filling everything the reviewer knows makes it two minutes rather than
ten, and two minutes of goodwill is still goodwill. If the pilot shows chat reviews returning
records at a much lower rate than hosted ones, that is a real finding about the path and not
about the leads.

**4. The calibration content is unmeasured, like everything else in the prompt.** Part one of
`CHAT-CONTEXT.md` is a distillation of what human leads wrote, and the claim that it makes a
reviewer judge more like a lead is a hypothesis. It sits with the reader test and the comparator
test in the same queue: plausible, argued from evidence, and not yet shown to change an output.
It should be measured the same way, by running the nine cases with and without it once there is
an instrument that can resolve communication-typed findings.

**5. `mode` is carried but not enforced anywhere new.** The format honours the noise budget by
telling the reviewer to, exactly as section A does. Nothing counts the findings. Same as the
hosted path before the contract validator, and the same failure would be invisible here.
