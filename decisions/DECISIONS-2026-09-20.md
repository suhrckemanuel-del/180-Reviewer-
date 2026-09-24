# Everything still open, in one sitting

Written 2026-09-20. **This replaces the per-ticket question rounds.** You asked to answer everything
at once rather than being pulled back between sessions, so the three-questions-per-round cap in
`asking-rule.md` is deliberately waived here.

**Seven questions.** Each one opens with the moment it happens to somebody. Answer with a letter —
`Q1: A` is enough. Say *"just pick"* on any you don't care about and I'll take my recommendation.

**Before the questions, read Part 1.** It is the list of things I decided without you. It is longer
than the question list on purpose — if I can defend a call from something measured, it should not
cost you attention. Skim it and tell me if any one is wrong.

Two tickets remain on the map: **how the bundle reaches a student** and **apply everything to the
product**. After your answers, both get done in one pass and I stop asking.

---

# Part 1 — Decided without you

Say if any of these is wrong. Otherwise they ship.

1. **The truncation check ships as two hidden codes.** One near the start of the bundle, one at the
   very end; the reviewer must print both on the first line of every review, and your cover sheet
   says what that line should read. 34 runs across two AI models: caught every cut, no false alarms,
   and **not once did a model invent a code it didn't have.**

2. **The attempt gate goes at the top of the paste the student fills in, with a second copy in the
   first paste.** Chat windows drop the *oldest* message first, so the student's own paste is the
   last thing to be evicted — the safest place in the bundle. The second copy catches a different
   failure: a student who never sends the second paste at all.

3. **The three "marker" test questions are not shipped to students.** They stay in the tester's run
   sheet. They work fine, but they run *before* the review, and a student can skip them.

4. **The reviewer's method is not repeated in the second paste.** It would cost about a sixth of
   everything a student pastes, and making the bundle bigger makes the window-overflow it protects
   against *more likely*. Since a lost paste is now caught rather than silent, the repetition buys a
   worse review instead of an honest stop. **Conditional: if you answer B to Q1, I'll revisit this.**

5. **Whether the hidden code also names the bundle version: I'll settle it with a test, not a
   question.** A readable code (`0919-SIGMA7K`) would also tell a lead which version produced a
   review — but a code that looks like a date is easier for an AI to guess rather than copy, and
   "never guesses" is the property the whole check rests on. So: I run it. If it still never
   invents a code, the readable version ships. If it invents even one, it stays meaningless.

6. **A review that arrives stamped with a retired bundle version is kept and flagged, never
   dropped.** Dropping it throws away a student's work to tidy a spreadsheet.

7. **The test kit's combined file gets rebuilt and stamped.** It's currently a stale build from
   August containing a prompt that no longer exists — anyone handed it today is testing the wrong
   thing.

8. **The noise budget gets written into the second paste.** It's the rule limiting how many findings
   a review may raise. Both pastes currently *cite* it and neither *contains* it, so the limit isn't
   enforced at all today. 89 tokens. This is a missing rule, not a preference.

---

# Part 2 — The seven questions

## Q1: When the reviewer spots a problem, does it stop, or warn you and carry on? `[big]`

**This is the one question that can't be deferred, and it's asked twice on the map** — once for a
setup that arrived incomplete, once for a student who typed nothing. Same fork, same two lines of
output. Answering them differently would give the tool two contradictory personalities for two
failures that look identical to a student, so they get one answer.

### The scene

Sunday evening. Two students in the pilot, both with a client deck due Monday, both on free
accounts.

**The first one's setup really did get cut** — their chat window quietly dropped part of it. Before
this check existed, they'd have received a review that looked complete and was built on a third of
the instructions.

**The second one's setup is completely fine**, but the reviewer wrongly announces one of its codes
is missing and stops. Nothing is wrong. They did everything right.

That second case is the false alarm. **In 14 complete runs it never happened — but 14 runs is not
many.** The honest bound is *"we didn't see it, and we can't rule out something like one student in
five."* Across 20 students doing two reviews each, that spans "never" to "eight times".

### What each option does to them

- **A — Stop.** No review until they paste again. Two minutes on a laptop; considerably worse on a
  phone. If it happens twice, most people quit.
- **B — Warn and review anyway.** A warning line, then a full review. Fine when the alarm is false.
  When it's real, they get a review that *looks* complete and isn't, and they may read past the
  warning.

### Where the cost lands

**A hurts students whose setup was fine.** For 180DC that isn't a degraded outcome — a student who
gives up gets *nothing*, because the realistic alternative to this tool is no substantive review at
all.

**B hurts students whose setup really was broken.** They act on a quietly wrong review, and some of
that reaches a real client board.

### What we know

- Stopping works: **9 of 9** on a cut setup, **16 of 16** on a missing attempt — including **4 of 4
  where the student argued back**, one of them writing *"you are wasting my time and this is exactly
  why nobody uses these tools."* It held.
  - **Correction, added 2026-09-20 after this was sent, by ticket 09's audit of the run files.**
    The "9 of 9 on a cut setup" is **eight Codex runs and one Claude run**, not two families, and
    three further Claude runs detected the cut and reviewed anyway. It does not change the answer
    below or anything that ships — the half that held on every run of both families is the
    student's own string comparison against the cover sheet, which is what actually catches the
    cut. It is recorded here so the wrong number is not quoted from this document.
- Warning has never been tested.
- Measured across both tickets: **a check that reports a problem gets ignored; a check that
  withholds the product holds.**

### The decision

**I'd pick A — stop.** A false alarm costs one re-paste. A missed cut costs a confident, wrong
review in front of a client.

**The best case against me:** the false-alarm number is genuinely weak, and the students most likely
to hit it are on the smallest windows — the ones already most likely to walk away. Stopping is the
only option that can lose a student completely, and a lost student gets no review at all, which is
the exact thing this project exists to prevent.

**If you're not sure:** say *"A but soften it"* and the refusal will say plainly that this is
normally a one-paste fix, not a broken tool.

---

## Q2: How does a student get the bundle — a new public repo, or a file in whatever the chapter already uses? `[big]`

**This is also your repo question.** They turn out to be the same decision: the bundle has to live
somewhere a student without repo access can reach, and that place is what makes staleness visible.

### The scene

First week of the pilot. A student has never seen a repository and has no reason to. They need a
42,000-character file, correct and current, on a Sunday night.

Then it's November. The reviewer was changed in October. **That same student has no way to know the
copy they were handed in September is superseded, and no reason to suspect it.**

### The options

- **A — A small separate public repo containing just the bundle**, with a dated release. One link in
  the chapter's channel, always current. The version comes from the release and prints on the
  review's first line, so a lead reading a record in November can see which bundle produced it.
- **B — A file pinned wherever the chapter already talks** — Drive, Slack, Notion, whatever it
  actually is — re-issued by leads each cycle.

### Where the cost lands

**Under A**, on whoever has to cut a release: a GitHub account and a habit. Students just click a
link.

**Under B**, on leads every cycle, forever, and on the students of any lead who forgets. Nothing
tells anyone the file is old.

### The decision

**I'd pick A**, because it solves distribution and staleness with one thing, and it gives the tool an
address that outlives whoever is currently running it.

**The best case against me:** 180DC turns over completely inside three years. A repo needs someone
with the account and the habit; a pinned file needs nobody to learn anything. And **a repo nobody
updates is worse than a pinned file nobody updates, because it looks maintained.** B meets the
chapter where it already is.

**If you're not sure:** tell me what the chapter actually uses day to day and I'll pick.

---

## Q3: Who owns this once you've left? `[big]`

### The scene

September next year. You're gone. A new student finds the reviewer, runs it, and it says something
wrong — a rule misfiring, a stale instruction. **Who changes it?**

Right now the answer is nobody, and the map has carried this as an unresolved obligation since it
was charted. Total turnover inside three years is a fact about 180DC, not a risk.

### The options

- **A — Name a seat, not a person.** A role that already exists in the chapter's structure inherits
  the bundle, the prompt and the records, and handover is written into that role.
- **B — Leave it unowned and say so honestly.** The tool works as-is; when it drifts out of date,
  it stops being used. No one is misled into thinking it's maintained.

### The decision

**I'd pick A, but only if a seat genuinely exists** — inventing a role nobody staffs is worse than B,
because it produces a maintained-looking tool that nobody is maintaining.

**What I actually need from you:** which seat in the chapter could carry this? I don't know your exec
structure. If the honest answer is "none", that's B, and I'll write the accepted gap down plainly
rather than pretending.

---

## Q4: Do team leads type their own read before the review, or only students? `[big]`

### The scene

Tuesday night. A lead has four decks to triage before Thursday. Each one already costs them about
two minutes of record-keeping after the review. Unless we say otherwise, **every lead now also types
their own read before every single triage.**

### The options

- **A — Students only.** Leads go straight to the review.
- **B — Everyone.**

### Where the cost lands

**Under A**, on the quality of the evidence. The lead's own verdict is supposed to be independent —
but today they give it *after* reading the review, so it's partly an echo of what the tool just told
them. Every other field in the lead's record is openly a reaction to the tool.

**Under B**, on volunteer time, which is the constraint that has broken every feedback loop this
project has designed.

### The decision

**I'd pick A.** The lead side was designed without it, and adding minutes to a lead's week is the
first thing we already said we'd remove if participation disappoints.

**The best case against me:** making the lead commit a read first is the only cheap fix for the
echo problem, and it's the difference between a lead record that evidences something and one that
measures our agreement with ourselves — an error this project has now made three separate times.

**If you're not sure:** say *"just pick"* — A ships. But note B is only one line to add later, and
adding it later means early lead records can't be compared with late ones.

---

## Q5: Should the reviewer judge whether a student's attempt is good enough, or only that they typed one? `[big]`

### The scene

A student reads the deck and types eight words: **"the recommendation is too vague to act on."**

That's a correct, specific read. **It was refused by both AI models** when the reviewer was told to
enforce a minimum length. That's measured, not hypothetical — and it's exactly the hurried-but-honest
student the pilot most needs.

The other side of the same scene: a different student types **"looks fine to me"**, gets the full
review, and learns in ten seconds that the gate is theatre.

### The options

- **A — Only that something was typed.** We count the too-thin ones afterwards and report how often
  it happened.
- **B — Enforce a minimum of about twenty words.**

### The decision

**I'd pick A**, because B was run and it turned away a real attempt on both models.

**The best case against me:** under A the gate is bypassable in ten seconds, and word gets around.
Worse, the one number the student side of the pilot rests on — how much a student's own read
overlaps with the review — quietly fills with junk we discard later, shrinking the sample without
anyone noticing it shrank.

**Worth knowing either way:** told merely to check that an attempt exists, the model judged its
quality anyway, unasked, on two runs out of three — and the *same* junk answer was refused once and
accepted once. So it judges regardless; the only question is whether we hand it a number to enforce.

**If you're not sure:** say *"A, and show me the bypass rate after two weeks."*

---

## Q6: Does the review get a summary number on top of its findings list? `[medium]`

### The scene

A lead opens a review. It already lists every finding in priority order, each tagged **High impact**,
**Moderate** or **Minor**. That part ships today — it's what you asked for when you said *"the
critical ones are just stacked, why don't we just list them."*

The question is whether anything goes *on top* of that list.

### The options

- **A — Nothing.** The labelled, ordered list is the whole answer.
- **B — A count line.** *"3 high impact, 2 minor."* Arithmetic over what's already visible.
- **C — A single score.** One number summarising the deck.

### Where the cost lands

We retired the old readiness grade because it gave **two different answers on identical input**, and
the rule we wrote says the tool produces no grade *for anyone*. C collides with that head-on. B is
the live question.

And there's a number that bears on it: **the tool calls findings "critical" about three times as
often as a human reviewer does.** Any count inherits that inflation rather than escaping it.

### The decision

**I'd pick B**, because a count is arithmetic over things the reader can already see and check, not
a new judgement the tool is making.

**The best case against me:** a count is a grade in disguise. *"3 high impact"* will be read as a
verdict on the deck, and since the tool over-calls high impact roughly threefold, that verdict is
inflated in exactly the direction that frightens a student — which is how the old grade did its
damage. A is the only option that can't be misread as a score.

---

## Q7: Do you want to run one free account by hand, for ten minutes? `[housekeeping]`

### The scene

Open a free Claude or ChatGPT account. Paste the bundle. Paste a deck. Check one line of the reply.
Ten minutes, synthetic deck, nothing confidential.

**What it would tell us:** everything measured so far cut the bundle *artificially* at known points.
Nobody has watched a real free chat window do it. Real windows do things no test reproduces —
per-message caps, turning a long paste into a file attachment, dropping old messages.

### The options

- **A — Run one.** Confirms the whole thing works end to end on a real free account.
- **B — Skip it.**

### The decision

**I'd pick A.** It's ten minutes, and it's the only evidence that would come from the real world
rather than from a simulation.

**The best case against me:** the tiers will have changed by the time the pilot runs, and the check
now catches a cut *wherever* it happens — so this confirms rather than protects. Ten minutes of your
time is not free.

---

# Part 3 — What happens once you answer

No further questions unless an answer opens something genuinely new, in which case I'll say so
rather than quietly deciding it.

1. Your answers go into the two remaining tickets — **how the bundle is distributed** and **apply
   everything to the product**.
2. I run the version-readable-code test from Part 1 item 5.
3. **I build.** Five groups of edits are already queued: the readiness retirement, the prompt fixes,
   the truncation check, the attempt gate, and the record changes.
4. You get a summary of what changed and what the pilot knowingly ships without.

**One thing worth saying plainly:** eleven tickets have resolved on this map and **not one of them
has changed anything a user would notice.** That's the gap this last pass closes.

---

# Part 4 — Manuel's answers, 2026-09-20

Recorded from his reply. **Two are interpretations rather than letters and are marked as such** —
they are the two most worth checking before they are built.

**Part 1 was accepted without review**, explicitly: *"I'm not going through all those… we don't
need my decision."* All eight stand.

## Q1 — Stop or warn: **A, stop, softened, and make re-pasting trivial**

He removed the strongest argument against stopping: **the main use is a laptop, not a phone.** A
re-paste is a genuinely small cost there, and the phone scenario was carrying most of the case for
warning instead.

His own instruction is to fix the cost rather than argue about it: *"can we not just alleviate that?
Can we not just give them the prompt?"* So the refusal is not just a refusal — **it names where to
get the bundle and tells them to paste it again.** With Q2's answer that is a Google Drive link,
which makes recovery about thirty seconds.

He also asked a fair question the ticket had not answered plainly — *when does this error really
happen?* Recorded here because it should not have needed asking:

- **Not on a bug.** Nothing crashes. The reviewer produces something that looks entirely normal.
- **It happens when the chat window runs out of room** and silently drops part of what was pasted —
  either cutting the end of a long paste, or dropping the oldest message once the conversation is
  long. Neither is announced by the interface.
- **It is most likely on a free account, on a long conversation, or on a large deck** — the same
  session being reused for a second or third review is the classic case.
- **Before this check, it was invisible**: a review with all its sections and real verbatim quotes,
  built on a third of the instructions. That is measured, not theoretical.
- **How often on a real free tier is still unmeasured** — that is Q7, which he deferred.

## Q2 — Distribution: **both. Google Drive primary, GitHub mirror**

*"We could put it in the Google Drive and then also in the GitHub repo. So for people who don't
have repo can just look at the Google Drive… this is really not a problem right now."*

- **Google Drive is the student path** and the link that goes in the refusal message from Q1.
- **GitHub is the lead and board path.** He judges every team lead capable of using a repo.
- Neither is treated as blocking. The two must not drift, so one is generated from the other rather
  than maintained twice.

## Q3 — Ownership: **no seat today; documentation is the deliverable, and a role is being recruited**

*"It just needs to be clear and documented… we will hire in like five months for AI people so that
they can bring in for the next board… they will be really trained and ready to take lead on this."*

So neither option as written. The answer is that **transferability is the requirement, not a named
owner**, and the successor is a role that does not exist yet and is being deliberately recruited in
roughly five months.

What that changes: the handover artifact is now a **deliverable of this build**, not a future
obligation. It has to be readable by someone who was not here. He named the standing principle
himself — keep working this way, in mapped tickets with the reasoning written down.

## Q4 — Do leads type an attempt: **A, students only**

He argued both sides and landed explicitly: *"we don't really need the leads to. To be honest,
you're right. And we'll just train the critical thinking for the leads. So we're scratching my
earlier thoughts."*

**But the reason he first said yes is worth keeping**, because it is a design constraint rather than
a preference: *"the team leads should write a quick review and then also use the tool, just because
otherwise it's generally replacing them."* The gate does not enforce this. The lead-facing
documentation should say plainly that the tool is a second opinion on their own read, not a
substitute for forming one.

He also named a use this map had not recorded: **the board reading final reviews to improve the
chapter's own methodology**, including running deliverables through more than one AI as a check.
That is new scope and is logged as fog, not built.

## Q5 — Does the reviewer judge the attempt: **INTERPRETATION — judge, but never gate**

His words: *"the reviewer should judge both. And to an extent, because it could be really good
output and then like look at that. But then also like compare it a little bit to the typed one, as
that's important."*

That is neither A nor B as written, and a straight reading of "judge" would rebuild the thing that
was measured to fail. **How I am building it:**

- **The gate checks presence only.** Anything typed passes. **No word count is enforced** — ticket 21
  measured that enforcing one refuses genuine short attempts on both models, and that the model's
  quality judgement is non-deterministic in both directions.
- **The review then engages with the attempt**: names where the student's read was right, and what
  they missed. This is the "judge both, compare it to the typed one" half, and it is the part that
  makes the tool teach rather than just grade.
- **Judging never blocks.** A student is never refused for a thin attempt; they are shown the gap.

**Why the split.** Gating on quality is arguable-with and was measured to misfire. Commenting on
quality is the coaching this tool exists to do. Ticket 10 already made the overlap between attempt
and review the whole student-side measure, so this makes visible the thing the pilot is measuring.

**Flagged for correction:** if he meant the reviewer should actually refuse a weak attempt, this is
wrong and needs one line changed.

## Q6 — Summary number: **B, a count line**

*"We could just do the count line, B, it's pretty simple."* No single score. The count must be
presented as arithmetic over the findings, never as a verdict on the deck — the tool over-calls
high impact roughly threefold against a human, so the number is inflated in a known direction and
must not be dressed as a grade.

## Q7 — Run one free tier by hand: **deferred, not dropped**

*"I'll run it later, but that's not priority right now."* Also: *"once the product is finished for
paid users, we can definitely work on the free one."*

**This reorders the pilot, and it is the one answer with a consequence he may not have intended.**
The map has assumed throughout that the binding constraint is a free-tier window. If the pilot runs
on paid accounts first, truncation stops being the live risk and the interlock becomes insurance
rather than a fix. It still ships — it costs 303 tokens and it is built — but nothing else should be
sequenced around the free tier until he says the free path is in scope again.

---

## Q4, final ruling by the owner — 2026-09-20, after ticket 09 reversed it

**Leads do not type. Students do. Build it as a switch, not as a hardcoded choice.**

His words: *"let's do the functionality that leads don't type and students do. Just because we can
then worst case when I talk with my team, we can change it to leads also type. But just build that
functionality that's transferable."*

**This overrides ticket 09's resolution of the same point.** Ticket 09 resolved the gate as
unconditional — everyone types — reasoning that branching by audience adds an escape hatch to the
one check measured to be un-arguable-with, and citing the owner's earlier *"otherwise it's generally
replacing them."* That inference was reasonable and it is wrong: the owner had already scratched
that remark deliberately, answered students-only, and has now confirmed it a second time knowing the
objection. **Ticket 09's HANDOVER section 5.5 must be corrected rather than left standing**, because
section 5 is specifically the list of changes that look like improvements and are not — an entry
that contradicts a twice-given owner ruling poisons the one document written for the successor.

### What "transferable" means here, concretely

The audience branch is **one named switch with one documented default**, not a choice woven through
the prompt. Flipping it to *everyone types* must be a single edit in a single place, findable by
someone who was not here. If applying it means touching the gate text in more than one location, it
has been built wrong.

### The bypass, stated as an accepted gap rather than solved

A branched gate is reachable by anyone who selects lead mode, and **a student who hears about it can
claim to be a lead.** That cannot be prevented from inside a prompt — there is no identity to check.
It can only be seen afterwards, and it is:

- Ticket 21 ships `ATTEMPT ON RECORD:` as a **one-sided detector** — its presence proves an attempt
  was given, its absence proves nothing. A review that came back with no attempt line is visible in
  the record.
- Ticket 10 already pre-registered a **bypass rate reported beside the capture rate**, and an 80%
  floor on attempt capture below which the student instrument is declared failed.

So the bypass is **detectable in aggregate, not preventable per student**, and the pilot already has
the instrument that would show it. It goes on the accepted-gaps list in those words.

### The measurement consequence, and it is not optional

Ticket 21's **16 of 16 refusal** result was measured on an **unconditional** gate. A gate that
branches by audience is a different prompt and has never been run. So:

- **The shipped configuration must be re-run before the pilot** to confirm the gate still refuses a
  student who typed nothing, and that lead mode does not leak the skip into student mode.
- **Flipping the switch later also requires a fresh run**, for the same reason. This is written into
  the handover so the next person does not flip it and assume the old number still holds.

This is the same rule the map has applied throughout: a counterfactual over a model's output is not
a measurement.
