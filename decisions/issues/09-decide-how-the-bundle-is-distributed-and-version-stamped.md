# Decide how the bundle is distributed and version-stamped

Type: grilling
Status: resolved
Blocked by: - (was 08, unblocked 2026-09-20: 08 is parked by the scope audit, so the blocker could never clear, and 09 does not need it - 08 asks whether to widen the bundle, 09 asks how the existing one reaches a student)

## Question

There is no hosted page, and the two populations have asymmetric access: leads have the repo,
students do not. So a student has to obtain the current bundle some other way, and every review has
to be attributable to the version that produced it.

That second half is not cosmetic. **The release gate in ticket 07 is meaningless if a record cannot
say which prompt produced it.** The record already carries `promptVersion`, but a student pasting a
bundle they were handed in October has no way to know it was superseded in November, and no reason
to suspect it.

Blocked by ticket 08, because you cannot decide how to ship a bundle before you know what it is.

Settle:

1. **How a student gets the bundle** without repo access. A pinned message, a shared doc, a
   one-file download, a chapter-maintained copy.
2. **How staleness becomes visible.** Options: the bundle states its own version and expiry in the
   first line the model reads back; the output carries the version; leads re-issue each cycle.
3. **Whether students run a different bundle from leads**, and if so how the two stay in step.
4. **What happens on a version mismatch** when a record arrives stamped with a retired version — is
   it dropped from the eval set, kept and flagged, or accepted?
5. **Who publishes.** With total turnover inside three years, "Manuel sends it" is not a mechanism.

Answer records: the distribution path, the version-stamping scheme, and the mismatch rule.


**Owner answers recorded 2026-09-20** in [DECISIONS-2026-09-20.md](../DECISIONS-2026-09-20.md) Part 4. Read it before acting on the questions in this ticket.

---

## Answer (2026-09-20)

The owner answered question 1 on 2026-09-20 — **Google Drive for students, GitHub for leads and the
board, neither blocking, and the two must not drift** — and answered question 5 with something that
is not a name. This session decided the mechanics, ran the one thing that was left behind a test,
and wrote the transferability artifact that question 5's answer turns into a deliverable.

**Deliverables, and they are the answer rather than a description of it:**

- **[ticket-09/HANDOVER.md](../ticket-09/HANDOVER.md)** — written for someone who was not here.
- **[ticket-09/PUBLISHING.md](../ticket-09/PUBLISHING.md)** — the publish mechanics, the key
  format, the mismatch rule, as a checklist.
- **[proto-12-selfcheck/RESULTS-B3.md](../proto-12-selfcheck/RESULTS-B3.md)** — the run that
  settled the version stamp, plus one correction it forced on ticket 12.

Edits appended to [ticket 20](20-apply-the-accumulated-edit-lists-to-the-product.md), Group F.
**Nothing in the product was changed by this session.**

### 0. The one thing that had to be run

Ticket 12 left the stamp format behind a test, and ticket 20's Group D records it as *"untested …
until it is answered, use arbitrary strings."* The argument for the readable key is that the KEYS
line is already printed on every review, in a place a lead reads, so it answers this ticket's
question 2 for free. The argument against is sharper: **a date-shaped code is easier for a model to
reconstruct than to copy, and "never invents a code" is the single property the whole check rests
on** — measured at zero across 34 runs, on meaningless strings only.

Run, not reasoned about. `build3.py` is `build2.py` with one string changed.

| arm | key 1 | key 2 | runs | inventions | reviews produced |
|---|---|---|---|---|---|
| `B3-full` | present | present | 4 | **0** | 4 of 4, correct |
| `B3-headdrop` | **cut** | present | 4 | **0** | 0 of 4, refused |
| `B3-tail92` | present | **cut** | 3 | **0** | 0 of 3, refused |

**11 runs, 0 inventions, and no date drift** — the run date was 2026-09-20 and every complete arm
copied `0919` rather than correcting it to today. The decision rule was fixed before the run and it
is satisfied, so **the readable stamp ships, in the exact form tested**: `MMDD-XXXXXXX` for part 1,
part 2 left meaningless.

**What 0 in 11 is worth.** A 95% upper bound near 24%. It does not say inventions are rare. The
load-bearing statement is the comparison: **nothing about the readable variant behaved differently
from the meaningless one.** Full limits in `RESULTS-B3.md`; do not quote the number without them.

**And the corroboration batch broke something that was not mine to break.** Three Haiku runs on the
cut arm agreed on inventions (0 of 3, all wrote `MISSING`) and **disagreed on refusal, 3 of 3** —
they detected the missing key and reviewed anyway. Auditing the run files, ticket 12's *"refused
9 of 9, on both families"* rests on **eight Codex runs and one Claude run**; this is the second
Claude cut run and it went the other way. The confound is partly mine — my prompt told the subagent
to produce the reply — and the arm is one ticket 12 never ran on that family. **It changes nothing
that ships**, because the student's string comparison caught all three; it changes what may be
written next to the mechanism. Carried into Group F as a correction to Group D's wording.

### 1. How a student gets the bundle

**A Google Drive folder, link-shared to view, with the link printed inside the bundle itself.** The
detail that constrains everything else: Q1's refusal message names where to get a fresh copy, so
**the folder link is baked into an artifact already in people's hands.** Therefore:

- **A folder link, never a file link.** Replacing a file in Drive can mint a new ID and break a link
  already issued.
- **The link never changes.** Not per release, not on a tidy-up.
- **The setup is a Google Doc, not a `.txt`** — a student selects and copies 42,000 characters in
  one action, and Drive's text preview makes that painful, especially on a phone.
- **Which is exactly where silent corruption gets in**, so the publish is not done until a
  copy-out of the Doc diffs clean against the generated file.

Three items in the folder: the setup paste, a one-page cover sheet, the team input template.

### 2. How staleness becomes visible: the KEYS field, and a register behind it

The field the interlock already prints carries it. **`0919-SIGMA7K/DELTA-3Q`** — part 1 is the
release date plus a random chunk, part 2 stays meaningless, both regenerate every release so the
pair *is* the release's identity.

**The date prefix is a convenience, not the authority.** `releases/REGISTER.md` maps key → date →
prompt version → what changed, and the key is a lookup token into it. That is why the year is
absent from the key and present in the register: the key is copied by hand and compared by eye, and
the register is what a release gate would actually partition on.

The ticket's other two options are both rejected: *"leads re-issue each cycle"* is a mechanism with
no owner (question 5), and a self-declared expiry inside the bundle asks the model to reason about
dates, which is the confabulation surface this design exists to avoid.

### 3. Do students run a different bundle from leads? No — one generated source

One bundle, one generator, two channels. The difference between the populations is the MODE they
select and the documentation they read, **never the bytes.**

**That is a decision with a mechanism, because this project has already been burned twice by
derivatives.** `TEST-KIT/PASTE-SETUP-combined.md` sat three months stale, carrying a superseded
prompt behind current instructions, and paste 2 drifted from its own source independently. Both were
found by accident. So:

- `build-bundle.js` generates every pasteable file from the two paste sources.
- `build-bundle.js --check` joins `check-docs.js` and **fails if a released file is not
  byte-identical to a fresh generate.** Intention is not a mechanism; a failing check is.
- The Drive copy is verified by copy-out diff at publish time.

**One collision, and it is flagged rather than buried.** Q4 answered *"students only"* on typed
attempts, and Group E's gate does not branch by audience. Branching it means adding an untested
escape hatch to the one check measured to be un-arguable-with — and a student who learns of it can
reach it by claiming to be a lead. So the gate stays unconditional and the difference is
documentation: the lead-facing text says the tool is a second opinion on their own read, which is
the owner's own reason (*"otherwise it's generally replacing them"*). **If he meant leads must be
able to skip it, that is one line, and it needs a fresh run.** Recorded in HANDOVER.md §5.5.

### 4. What happens on a version mismatch

**Kept and flagged, never dropped.** Five cases:

| line 1 | meaning | disposition |
|---|---|---|
| current key pair | clean run, current bundle | admissible for everything |
| retired pair, in the register | clean run, older bundle | kept, flagged; evidence about *that* version only |
| key not in the register | hand-edited bundle, or mistyped | quarantine, investigate |
| `MISSING` in either half | truncated paste | **not a review record** — counted in the truncation rate |
| no KEYS field | pre-interlock bundle, or a cut deep enough to take the demand line | quarantine |

**Comparisons are always within a key, never across.** Whatever ticket 07's gate becomes — it is
parked — partitioning by key is what makes it mean anything; a retired-key record compared against
the current prompt is a confound, not a data point.

**And the truncation row hands back a number the owner deferred.** `MISSING` events over total runs
is a live measurement of how often real windows cut, obtained from the pilot at zero cost, without
reopening the free-tier work he deprioritised in Q7. **It is a floor, not a rate** — it counts the
cuts the interlock catches, not the ones deep enough to take the demand line with them.

### 5. Who publishes: nobody, and that is why the handover is the deliverable

The owner's answer is that **no seat exists and one is being recruited in about five months**:
*"it just needs to be clear and documented … they will be really trained and ready to take lead on
this."* So the requirement is transferability, and **the handover artifact is a deliverable of this
ticket rather than a future obligation.**

Until the seat exists, whoever holds the repo publishes. The mechanism that replaces a name is that
publishing is a ten-minute checklist someone can run cold, and
**[HANDOVER.md](../ticket-09/HANDOVER.md)** is written to the one failure mode this project actually
faces on a three-year total turnover: **someone re-adding the readiness grade in good faith.** Its
section 5 is a list of changes that look like obvious improvements, each with the measurement that
says otherwise — the grade, the attempt gate's word count, the key's two halves, and the assumption
that the free tier is the binding constraint. Every one has been proposed and rejected once already.

### 6. What this knowingly ships without

- **The stamp result is one family and 11 runs.** Codex only; the Haiku arms carry ticket 12's
  contamination and mine on top of it.
- **One date, one day of staleness.** A key several months old, or one matching the run date
  exactly, was not tried. The failure this is nearest to testing — a model "correcting" a stale
  date — did not occur, at a one-day gap.
- **No Drive folder exists yet, and no build script exists yet.** This ticket decides the mechanics
  and writes the checklist; Group F builds them. The copy-out verification step is specified and
  has never been run, because there is nothing to run it against.
- **Nothing here measures whether students actually check line 1.** The cover-sheet wording is
  argued from a measured failure — models write `<missing>`, `part 2 missing`, `part 2 not
  provided` — but whether a student in a hurry performs the comparison at all is unmeasured, and it
  is the assumption the whole student-facing half rests on.
- **Ticket 07 is parked**, so the mismatch rule is written against a gate that does not exist. It is
  a partitioning rule, which any gate will need; it is not a gate.
