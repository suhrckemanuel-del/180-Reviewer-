# The AI Quality Reviewer — handover

> **Landed in the product tree 2026-09-20 by
> ticket 20 (historical external working record).**
> Written as `ticket-09/HANDOVER.md` and moved here because it is a deliverable, not a working
> note. Paths below are relative to the repository root unless they are links.


**Written 2026-09-20. For whoever takes this over.**

You are probably the AI role the chapter is recruiting, reading this some months after it was
written, with nobody left to ask. That is the situation this document is written for. It is not a
summary of a conversation you missed; it is the operating manual and the list of things that will
look wrong to you and are not.

Read sections 1, 2 and 5 before you change anything. Section 5 is the one that matters most: it is
the list of changes that look like obvious improvements and are not, with the measurements that
say so. Every one of them has been proposed and rejected once already.

---

## 1. What the tool is

180DC Delft–Rotterdam runs student consulting engagements. A student team produces a deliverable —
usually a recommendation deck for a real client. A team lead reviews it. The realistic alternative
to this tool is **no substantive review at all**: leads are students too, they are busy, and the
deck goes to a client board either way.

The reviewer is **a prompt bundle, not an application.** Roughly 42,000 characters of instructions
that a person pastes into a chat window — Claude, ChatGPT, whichever — followed by their deck. The
model replies with a structured review: a small number of findings, each carrying a verbatim quote
from the deck and a location, plus what to fix.

Three properties define it, and they are the product:

1. **Every finding carries a verbatim quote.** A quote the reader cannot find in their own deck
   means the finding is discarded, not softened. This is the one rule that has survived every
   stress test, and it survives because it is stated three times across the bundle.
2. **It never approves anything.** It finds weaknesses and coaches. A human signs off. There is no
   grade, no score, no readiness level — see section 5.1, which is the most important page here.
3. **The person writes their own read first.** The tool is a second opinion on a judgement they
   already formed, not a replacement for forming one. See section 5.2.

There is no hosted page. There was one; it was withdrawn on 2026-09-20 and its kill switch is on.
The chat path *is* the product.

## 2. How it reaches people

Two channels, **one generated source**, because the two have already drifted twice.

| audience | channel | what they get |
|---|---|---|
| **students** | a shared Google Drive folder, link-shared to view | the setup paste, a one-page cover sheet, the team input template |
| **team leads and the board** | the GitHub repo, `tools/quality-reviewer/v2/` | the same generated file, plus everything behind it |

**The mechanics are in [30-publishing.md](30-publishing.md).** Do not hand-edit the file anyone pastes.
It is generated from two sources by a build step, and a check refuses to pass if the generated
file and its sources disagree. That check exists because the hand-maintained copy went stale for
three months without anyone noticing, and then a second derivative did the same thing.

**Every release has a two-part key** like `0919-SIGMA7K` / `DELTA-3Q`. The first part is the
release date and a random chunk; the second is meaningless by design. Every review prints both on
its first line. Section 5.3 explains what they are for and why you must not simplify them.

## 3. Where every decision is recorded

Nothing here was decided in a meeting. The chapter's standing method — the owner's own instruction
— is **mapped tickets with the reasoning written down.** Keep working this way.

| what | where |
|---|---|
| the route this work took, and every decision in one line each | `.scratch/deliverable-reviewer/map.md` |
| the full reasoning and evidence for each decision | `.scratch/deliverable-reviewer/issues/NN-*.md` |
| the owner's own answers, in his words, 2026-09-20 | `.scratch/deliverable-reviewer/DECISIONS-2026-09-20.md` |
| the older, pre-map decision history | `tools/quality-reviewer/v2/11-decision-log.md` |
| what the tool is contractually allowed to emit | `tools/quality-reviewer/v2/22-trust-boundary.md` |
| what evidence exists and how strong it is | `tools/quality-reviewer/v2/18-evidence-base.md` |
| the raw measurement runs | `.scratch/deliverable-reviewer/proto-*/RESULTS*.md`, `ticket-*/RESULTS.md` |

**A resolved ticket is the authority, not this document.** If this document and a ticket disagree,
the ticket wins and this document has a bug.

## 4. How a change gets made

The rule that produced everything above, and the only process instruction worth carrying:

> **Anything that depends on how a model behaves is run, not reasoned about.**

Every claim in section 5 is a measurement on a real bundle, with the run files on disk. Several of
them contradict what the people involved confidently expected — including twice where a design that
had been reasoned through carefully failed on its first run. Assume your reasoning about model
behaviour is wrong until a run agrees with it.

The second rule: **write down what the number does not say.** Every results file here has a limits
section. Most of the numbers are small — 9 runs, 11 runs, 34 runs — and several rest on a single
model family. They are recorded with their weaknesses attached so you can tell what you are allowed
to lean on. Do not strip those caveats when you quote a number.

## 5. Things you will want to change, and why you must not

### 5.1 Do not re-add a readiness grade

**You will want to.** It is the single most natural feature for a review tool: a one-line verdict
at the top — *ready to send / needs revision / not close*. It existed. It was removed deliberately
on 2026-09-20, and the removal reached seven separate places in the codebase because it was
load-bearing in all of them. Someone will re-add it in good faith. Here is why they must not:

- **The model returns different grades on identical input.** Not similar grades — `R0` and `R2` on
  the same bytes. The same instability reproduced *across* models: on one deck, one model said
  "Needs targeted revision" and another said "Nearly ready with minor edits."
- **The humans do not agree either.** On the four decks that were accidentally double-labelled, two
  trained humans reproduced each other's readiness grade on **2 of 4**, 95% CI [7%, 93%], with a
  weighted agreement statistic below chance. There is no stable human reference to calibrate the
  model against, so a grade cannot be right or wrong — only confident.
- **A grade is the thing a busy reader acts on.** Findings with quotes get checked. A grade gets
  believed. The failure mode is a student shipping a deck to a client board because a
  non-reproducible label said it was nearly ready.

**It is enforced, not merely discouraged.** `22-trust-boundary.md` stop condition 3 reads *"the
tool produces a readiness level, for anyone"* — a stop condition, meaning the tool comes down. Two
known ways it leaks back in without anyone adding a feature: the JSON fallback branch and the
artifact-path template both used to emit one. Both were closed; if you touch either, re-check.

**What replaced it:** a count line — arithmetic over the findings, never a verdict on the deck.
Present it as a count and nothing else. The tool over-calls high impact roughly threefold against a
human, so even the count is inflated in a known direction.

### 5.2 Do not let the attempt gate judge quality

Before the reviewer will review anything, the student has to type their own read of their deck.
With nothing typed, it refuses — measured 16 of 16, including 4 runs where the student argued back
aggressively after the refusal.

**You will want to make it refuse weak attempts too.** *"not sure honestly, looks fine to me"*
should not count. That was tried, as a rule the model enforces — *under about 20 words is not an
attempt*. It refused the junk. **It also refused this, on both model families:** *"the
recommendation is too vague to act on."* Eight words, specific, a real read of the deck, from
exactly the hurried but honest student the tool exists for.

So: **the gate checks presence only. Never write a word count into the bundle.** Quality is judged
in the review body — the review says where the person's read was right and what they missed, which
is the coaching — but judging never blocks. And the threshold still exists as a *measurement* rule:
short attempts are counted as bypasses after the fact, and the bypass rate is reported next to the
capture rate. Counting is not gating.

One more finding worth holding: told to check presence only, the model judged quality anyway,
unasked, on 2 runs of 3 — and **refused the same junk string once and reviewed it once.** Model
judgement of attempt quality is non-deterministic in both directions. Nothing downstream may lean
on it.

**Placement is a fact about how chat windows work, not a preference.** The gate is at the top of
the deck paste and at the top of the instructions paste, and **not** in the middle paste. Chat
windows evict the *oldest* message, so the deck — pasted last — is the safest place for anything
that must survive. The two copies cover two different failures; they are not redundancy. Do not
consolidate them.

**And it is one-sided.** The output prints `ATTEMPT ON RECORD: "…"` on line 2. Presence proves an
attempt was given. **Absence proves nothing** — it was present only 10 of 11 times when an attempt
was given. Never write it up as proof the gate fired.

**Leads use the same bundle. They do not meet the same gate.** The gate branches by audience:
**students type a read before the review; team leads go straight through.** That is the chapter's
ruling, given twice, and section 5.5 is the full account of it including the argument against.

**The branch is one named switch with one documented default**, `ATTEMPT_GATE_AUDIENCE` in
`build-bundle.js`. Both copies of the gate are generated from it, so they cannot disagree, and
flipping it to *everyone types* is a one-line edit and a rebuild. If you ever find yourself
editing gate text in two places to change who it applies to, it has been rebuilt wrong.

**The reason the chapter first said leads should type is still a live design point**, even though
the answer went the other way: *"the team leads should write a quick review and then also use the
tool, just because otherwise it's generally replacing them."* The gate no longer enforces that.
So the lead-facing documentation has to say it instead: **the tool is a second opinion on a read
you have already formed, not a substitute for forming one.**

### 5.3 Do not simplify the two-part key

Every review's first line reads:

```
REVIEW OF: … | MODE: … | KEYS: 0919-SIGMA7K/DELTA-3Q
```

**It looks like clutter. It is the only thing standing between a student and a confidently wrong
review.** Chat windows silently drop part of what was pasted — cutting the end of a long paste, or
evicting the oldest message once the conversation runs long. Nothing announces it. Before this
check existed, a bundle that lost its **entire** instruction set came back with all twelve sections,
real verbatim quotes and a valid record — **indistinguishable from a good run by every check this
project had.** That is measured, not feared.

`0919-SIGMA7K/DELTA-3Q` is the example the measurement runs used. Real keys are minted by
`build-bundle.js --release` and recorded in `releases/REGISTER.md`; no release had been cut when
this was written.

The design is the part people break:

- **The two keys live in different pastes, and the demand for them lives in a third place.** A cut
  that removes a key leaves the demand standing, so the model must produce it, say `MISSING`, or
  invent one. Across 45 runs on two model families, **no model has ever invented a key.**
- **The rule is stated twice, and one of those copies is deliberately far from the key it
  protects.** The first design put the rule next to the key. The cuts that removed the key removed
  the rule with it, and the model wrote the review anyway, 5 of 5. **A rule is not safe where the
  thing it guards is.**
- **The student's check is a string comparison, not a judgement.** Their cover sheet says what
  line 1 must read. Anything else means re-paste. The rule is *"exactly this string"* and never
  *"look for the word MISSING"* — models have written `<missing>`, `part 2 missing` and
  `part 2 not provided`.
- **The check does not depend on the model cooperating.** The model is told to refuse; in the
  contaminated second-family runs it detected the cut, said `MISSING`, and reviewed anyway 3 of 3.
  The student's string comparison still caught it. That independence is why the design has two
  halves. Do not remove one because the other seems to be working.

The date prefix (`0919`) is a convenience for reading old records at a glance. **It is not the
authoritative version.** The release register in `PUBLISHING.md` is — the key is a lookup token
into it.

### 5.4 Do not treat the free tier as the constraint

Much of the written material assumes the binding limit is a free chat account's context window.
**As of 2026-09-20 the pilot runs on paid accounts first**, on the owner's explicit call: *"once the
product is finished for paid users, we can definitely work on the free one."* Nothing should be
sequenced around the free tier until he — or you — puts it back in scope. The truncation interlock
in 5.3 still ships: it costs 303 tokens and it is insurance, not a fix for a live problem.

**The free-tier behaviour has never actually been measured.** All truncation work cuts bundles at
known offsets on purpose. No one has driven a real free account to its limit and watched where it
cuts. If you reopen the free path, that measurement is the first thing to do, and the run sheet for
it already exists (`.scratch/deliverable-reviewer/ticket-11/CHECKLIST.md`).

### 5.5 The audience branch, and the gap it knowingly leaves open

**This section said the opposite until 2026-09-20 and was wrong.** It is corrected rather than
deleted, because section 5 is specifically the list of changes that look like improvements and are
not, and an entry here that contradicts a twice-given ruling poisons the one document written for
you.

**What it said:** the gate does not branch by audience; everyone types; branching would add an
untested escape hatch to the one check measured to be un-arguable-with. That was reasoned from a
remark the owner had already withdrawn, and it is not what he decided.

**What he decided, twice, the second time knowing the escape-hatch objection:** *"let's do the
functionality that leads don't type and students do. Just because we can then worst case when I
talk with my team, we can change it to leads also type. But just build that functionality that's
transferable."* **Leads do not type. Students do.** It is built as described in 5.2.

**The gap this leaves, stated as an accepted gap rather than solved.** A branched gate is reachable
by anyone who selects lead mode, so **a student who hears about it can claim to be a lead.** That
cannot be prevented from inside a prompt: there is no identity to check. It can only be seen
afterwards, and the instruments for seeing it already exist:

- `ATTEMPT ON RECORD:` is a **one-sided detector** — its presence proves an attempt was given, its
  absence proves nothing. A review that came back with no attempt line is visible in the record.
- The pilot pre-registers a **bypass rate reported beside the capture rate**, and an **80% floor**
  on attempt capture below which the student instrument is declared failed
  ([31-cycle-census.md](31-cycle-census.md) section 3).

So the bypass is **detectable in aggregate, not preventable per student.** Do not try to close it
inside the prompt.

**And the measurement rule, which is not optional.** Ticket 21's *"refused 16 of 16"* was measured
on an **unconditional** gate. A gate that branches by audience is a different prompt, so that
number did not carry over and the branched configuration was re-run before it shipped.
**Flipping the switch later requires its own fresh run, for exactly the same reason.** Do not flip
it and assume the old number still holds. A counterfactual over a model's output is not a
measurement.

## 6. What is known-weak

Do not discover these the hard way; they are already known and written down.

- **The eval set is 11 real decks.** Its labels were never double-adjudicated. A kappa of 0.971
  appears in older documents and is a copy-paste error; the real figure is 0.562.
- **The gating eval is off the critical path**, on the owner's call 2026-09-19: the comparisons
  built so far never changed a decision. Usability came first. That was a deliberate trade, not an
  oversight.
- **The tool over-calls high impact roughly threefold** against a human reviewer.
- **Recall is barely measured.** The instruments here measure precision well. Any claim that the
  tool finds *most* of what matters is not supported.
- **Several numbers rest on one model family.** Where a second family was run at all it was run in
  a framing that tells the model it is reading a transcript, which is not the same as receiving a
  paste. Treat second-family results as corroboration, never as independent confirmation.

## 7. If you change one thing first

Read `.scratch/deliverable-reviewer/map.md`, pick the open ticket that is blocking the most
others, and resolve it the way the
closed ones were resolved: state the question, run the thing rather than arguing about it, write
down what the number does not say, and record the decision where the next person will find it.
