# 28. The shared corpus: free prompt, chapter repo, usage-fed evals

**Status: design map, written 2026-09-18. Nothing built.** The proposal is a free prompt for
everyone plus a reusable system for people with a paid account, backed by a shared repository
where reviews accumulate, deliverables improve visibly, and an eval loop feeds the prompt.

Scope: what of this already exists, what the outside research says the corpus may and may not be
used for, what it can and cannot measure, and the three things in it that are genuinely new.

---

## Headline

**Two thirds of this is already built, and the half that looks hardest — confidentiality — was
already solved by accident.** The [paste-back record](CHAT-CONTEXT.md) carries no client text at
all: a finding reduces to a two-to-four word label, a severity, an issue type, a rubric dimension
and slide numbers. The quotes stay in the chat window. What is missing is not the artifact. It is
somewhere for records to go, something that reads them in aggregate, and the student half of the
loop, which does not exist in any form.

So this is not a new build and it must not become one. [STATUS.md](STATUS.md) says building stops
and the pilot is next. **The corpus is the pilot's data plumbing, not a project that precedes it.**

The one thing that changes the value of the whole idea: [17-override-log.md](17-override-log.md)
§1 already establishes that a lead's triage decision costs about four minutes as a byproduct of
work they were doing anyway, against roughly thirty hours of expert time for nine gold labels.
That ratio is the argument. §5 of the same document is the reason it is not the whole argument,
and it is reproduced faithfully in section 5 below.

---

## 1. Three outside findings that constrain the design

### 1.1 Codify the reviewer, not the answers

Hansen, Nohria and Tierney, *What's your strategy for managing knowledge?*, HBR 1999 — the
foundational study of exactly this question in exactly this industry. Two strategies:

- **Codification.** People-to-documents. Knowledge is extracted from the person, made independent
  of them, and reused. Ernst & Young and Andersen built this; it is what makes scale possible.
- **Personalization.** Dialogue and networks. Documents exist to find out *who* worked on
  something, not to reuse the object. McKinsey, Bain and BCG sit here.

Their finding, and the one that matters to us: **effective firms pick one and use the other in a
supporting role. Pursuing both equally "can quickly undermine a business."** The choice follows
the work — standardised offerings reward codification, bespoke solutions reward personalization.

180DC is bespoke work done by people who are here to learn. That is the personalization end twice
over. It also cannot pay for codification: Ernst & Young ran 250 people in a Center for Business
Knowledge plus a codifier in each of 40 practice areas. We have volunteers on a three-year total
turnover.

**The design rule that falls out of it:** the corpus feeds the *evaluator*, never the student. It
is a calibration asset, not a deck library. If a student can browse past deliverables for a shape
to copy, we have built the codification strategy we cannot staff, at the cost of the teaching
mandate that justifies the tool. Students see their own review and their own history. Nothing else.

### 1.2 Confidence in the AI is the thing that destroys critical thinking

Lee et al., *The Impact of Generative AI on Critical Thinking*, CHI 2025 (Microsoft Research and
Carnegie Mellon; n=319 knowledge workers, 936 first-hand task examples). The relevant results:

- **Higher confidence in GenAI predicts less critical thinking. Higher confidence in oneself
  predicts more.** Both significant; confidence in AI is the strongest single coefficient in the
  model (−0.69, p<0.001).
- GenAI shifts the *nature* of the effort rather than removing it: information gathering becomes
  verification, problem solving becomes response integration, execution becomes stewardship.
- 69–79% of examples report less effort across the Bloom categories.
- **Users with GenAI produce a less diverse set of outcomes for the same task** than users without.
- The named inhibitors are lack of time, lack of incentive where critical thinking is not seen as
  part of the role, and lacking the skill to inspect and steer output.

Three consequences for us, all testable:

1. The existing rules are now externally grounded, not just principled. Never passing on the AI's
   grade, quote-or-abstain, findings instead of rewrites, and the attempt-before-answer lock all
   suppress confidence in the tool and raise confidence in the student. Keep every one of them.
2. **The corpus must never show a student how often the AI was right.** An accuracy figure pointed
   at a student is a direct intervention on the variable that predicts less thinking. Aggregate
   performance numbers are for whoever runs the reviewer, and for nobody else.
3. **Homogenisation is a real risk and it is the failure mode a shared corpus accelerates.** One
   calibration corpus reviewing every chapter's work pushes every chapter's work toward one shape.
   Structural diversity across deliverables has to be a tracked guardrail, where convergence is a
   failure signal. See section 6.3.

### 1.3 The answer key, and measuring the gap

Hancock, *Building expertise in the age of AI*, McKinsey Quarterly, July 2026
(historical research/06 reading list, outside this repository). The junior attempts
the work, AI grades it, the manager discusses the difference — our attempt gate, arrived at
independently. The part we do not have is the measurement: **track the narrowing gap between the
student's own attempt and the AI's output as the signal that judgment is forming.** That requires
the student's attempt to be recorded, which today it is not. Section 6.1.

Supporting, from McKinsey's *One year of agentic AI* (Sept 2025): evals and observability are the
discipline that separates a working deployment from AI slop, and "the best use case is the reuse
case" — build one validated set of components rather than a stack per workflow. The corpus is the
reuse case for a project that currently has one eval instrument per sprint.

---

## 2. The tiers

| tier | who | what they touch | what it costs them |
|---|---|---|---|
| **0. The prompt** | anyone, any chat window, no account | three pastes, [CHAT-CONTEXT.md](CHAT-CONTEXT.md) | nothing. No storage, no login, no readiness grade |
| **1. The record** | the lead who triaged the review | fills the nulls in the paste-back block, commits one file | about four minutes ([17](17-override-log.md) §1) |
| **2. The corpus** | one repo, records only | append-only `records/`, plus the prompt and the harness | one commit per review |
| **3. The loop** | whoever runs the reviewer | harness over new records, monthly | a frozen prompt version per change |

Tier 0 is shipped. Tier 1 is shipped as an artifact and unshipped as a habit —
[26-chat-native.md](26-chat-native.md) §593 already flags the weak point: *the record depends on a
lead choosing to send it*. Tiers 2 and 3 are the work.

Deliberately **not** in the tiers: students do not touch git. A student runs three pastes and
hands the output to their lead. Requiring a clone would restrict the tool to the population the
chat-native path exists to escape.

### 2.1 Why one file per record

Every record is a new file named by date and hash, never an edit to a shared file. Append-only
means two leads committing on the same day never produce a merge conflict, which is the difference
between a repo non-technical volunteers can use and one they abandon after the first conflict.

---

## 3. What may go in the shared repo

[CONTEXT.md](../../../CONTEXT.md) already sets the rule: real deck material, raw intake *and*
pseudonymised cases, is local-only and gitignored because it carries the full text of real client
deliverables. A shared repo of deliverables breaks that rule at larger scale and across chapters.
It is not a thing to solve later; it is the thing that decides whether this can exist.

It is already solved, because the record was designed not to carry content:

| in the record | client text? |
|---|---|
| `short` (2–4 words), `severity`, `issueType`, `dimension`, `slides` | no |
| `decisions[]` — keep / ask / cut, `cutReason` | no |
| `added[]`, `mustCatch`, `readinessCall.lead` | lead's own words, must stay generic |
| quotes, deck text, findings prose | **never leaves the chat window** |

Two fields leak today and both need a spec change before any record is shared beyond the chapter
that wrote it:

- **`deliverable.ref` must be an opaque identifier**, `<chapter>-<engagement-no>-<artifact-no>`,
  never a client or project name. A lead filling in "Warmtewerk final v3" publishes the client.
- **`lead.id` must be a chapter-scoped pseudonym**, not a name or an email.

Add a third, non-negotiable: **the engagement consents at intake, and a named person in the
chapter is accountable for the scrub.** The quote-check gate built in
[22-trust-boundary.md](22-trust-boundary.md) already knows how to scan text against a deck; the
same machinery can flag a `ref` or a `note` that looks like a name before it is committed.

**Deliverables themselves stay in the chapter.** If a chapter wants its own before/after archive,
that is a private chapter repo, under its own client agreements, and it is not this repo.

---

## 4. The loop, stated precisely

```
review (tier 0)  →  lead triages, fills record (tier 1)  →  record committed (tier 2)
      ↑                                                              ↓
   frozen prompt  ←  change justified in the decision log  ←  harness reads records (tier 3)
```

The only permitted path from a record to a prompt change runs through
[11-decision-log.md](11-decision-log.md) and a version freeze with a sha, as every prompt change
in this project already has. No automatic prompt rewriting. A corpus that edits the prompt without
a human argument in between is how the calibration drifts without anyone being able to say when.

---

## 5. What this corpus can measure, and what it cannot

Taken unchanged from [17-override-log.md](17-override-log.md) §5, because it is the honest version
and scaling the records does not repair any of it:

1. **Selection bias.** The record is conditioned on the AI's output. It measures precision well
   and recall barely.
2. **Anchoring.** The lead reads the AI first. That is the product working as intended and the
   opposite of the gold protocol.
3. **No adjudication.** One opinion, from an interested party — the lead is reviewing their own
   team's work and cannot be screened for conflict the way a gold labeler was.

**Therefore the flywheel improves restraint, not coverage.** Killing false positives, calibrating
readiness and retiring finding types nobody keeps are all well served. "The reviewer catches more"
is not a claim this corpus can support at any volume. A pilot reporting "the lead agreed with 90%
of findings" is reporting the default state of a form.

The high-yield use is the sampler, and it survives at scale: **a record carrying
`cutReason: wrong`, or an `added[]` entry at `severity: critical`, points thirty-hour expert
attention at the cases where it pays.** (Re-specified 2026-09-20, ticket 05 decision 7. The
trigger used to be "the lead moved readiness two levels" -- a delta against the tool's own
level, which no longer exists. Both replacements are already collected, the first is what
`17-override-log.md` calls the one field to build if only one gets built, and the second is
stop condition 1's own detector.) With a corpus instead of a handful of records, that sampler is the cheapest
route to the double-adjudicated label set the project has never had — which per
[STATUS.md](STATUS.md) is the open wound underneath every number here (real inter-rater kappa
0.562, not the 0.971 that was reported).

### 5.1 The trap this project has already fallen into once

The 2026-08-05 finding was that "two independent adjudicators, kappa 0.971" was one opinion copied,
so the numbers measured agreement between LLM passes rather than correctness. A usage-fed loop
walks straight back into it if the labels are generated by the same prompt whose output they judge.

**The protection is that the label must be a human decision with a consequence.** `keep` / `ask` /
`cut` is a lead committing to act or not act on their own team's deliverable, and `added[]` is a
lead writing down something they had to raise themselves. Those are outcomes, not opinions about
outcomes. Nothing that a model produced may ever be scored as a label. And a held-out slice of
records must never touch prompt iteration.

---

## 6. The three things here that are genuinely new

### 6.1 The student attempt record, and the convergence metric

Today the attempt gate makes a student type their own read before the findings unlock, and then
throws it away. Keep it — hashed or plain, in the chapter tier, never shared — and the gap between
what the student saw and what the reviewer raised becomes measurable across a semester.

That single change converts the reviewer from a feedback tool into a development-tracking
instrument, gives a chapter something to report that no prompt box can produce, and is the metric
the McKinsey Quarterly piece names. It is also the only metric in this document that measures the
thing 180DC actually exists to do.

Guardrail from §1.2: report it to the student as *their own* trajectory. Never as a ranking
against peers, and never as agreement with the AI.

### 6.2 Make `added[]` worth filling

It is the recall field and [17](17-override-log.md) §4.2 already calls it the one most likely to be
skipped. It is also the only field in the whole record that is not conditioned on the AI's output,
which makes it the only defence against the selection bias in §5.1. If the corpus is going to be
the instrument, `added[]` is the field to spend design effort on — ask for it before the findings
are revealed, not after, so the lead is not anchored when they answer.

### 6.3 A homogenisation guardrail

Per Lee et al., AI-assisted users produce less diverse outcomes. Track structural variance across
deliverables over time — distribution of storyline shapes, recommendation counts, section patterns.
If chapter decks converge as the corpus grows, the tool is flattening the work rather than
improving it, and that has to be visible as a failure rather than read as consistency.

---

## 7. What to do next, in order

1. **Nothing, until the pilot runs.** The pilot produces the first records. A repo with no records
   in it teaches us nothing and costs a sprint.
2. **Two spec edits before any record leaves a chapter**: opaque `deliverable.ref`, pseudonymous
   `lead.id` (§3).
3. **During the pilot, keep the student attempts** (§6.1). Costs nothing at capture time and cannot
   be reconstructed later.
4. **Move `added[]` ahead of the reveal** (§6.2).
5. **Then** stand up `records/` and a reader over it, sized to the record count that exists.
6. **First use of the corpus is the sampler**, not prompt tuning (§5) — point it at the cases worth
   double-adjudicating, and close the kappa problem.

---

## 8. Open for Manuel

- Is a cross-chapter repo in scope at all, or is this per-chapter until one chapter has run it for
  a full cycle? Cross-chapter multiplies the consent and scrub surface for benefit that only
  arrives at volume.
- Who owns the scrub, and what happens on turnover? Three-year total turnover means the accountable
  named person leaves, and this is a standing obligation, not a sprint task.
- Does a chapter's own before/after deliverable archive get built at all, given §1.1 says students
  must not browse it? There is a version of that archive that only a lead can open.
