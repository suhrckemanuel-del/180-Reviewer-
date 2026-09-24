# Apply the accumulated edit lists to the product

Type: task
Status: resolved
Blocked by: —

## Question

Nothing to decide. This ticket exists because the map had no way to reach its own destination:
**every resolved ticket produced a decision and none of them changed the product.** Tickets 05 and
16 both closed into edit lists the map files as "executable spec for a build session", and there
was no build session and no ticket for one. Created 2026-09-20 on the owner's call, after the
gap was drawn.

This is the map's second `task` exception, and it is a wider one than tickets 01, 02, 03, 11 and 17:
those generate numbers other decisions are blocked on. **This one ships changes.** It is deliberate
and it is bounded — this ticket applies decisions already recorded elsewhere and **decides nothing**.
If a question arises that the source ticket did not settle, stop and route it back rather than
resolving it here.

Blocked by 17 because ticket 05 wrote a hard ordering constraint: deleting the emitted readiness
level before 17's verification run destroys the only pre-registered falsification test this project
has. **If 17 stalls for any reason, the "land now" half below can be pulled forward on its own** —
it was separated for exactly that reason.

### Source of truth

The edit lists live in the resolved tickets, not here. Read them; do not work from this summary.

- [Ticket 05](05-retire-the-readiness-level-everywhere-it-appears.md) — "What is deleted", "What is
  kept", "The rewritten stop condition 3", "Documents that assert something now false", "Sequencing".
- [Ticket 16](16-decide-what-to-do-about-the-two-prompt-defects-the-baseline-exposed.md) — the three
  prompt changes. **Ticket 17 applies these**; confirm they landed rather than re-applying them.
- [Ticket 12](12-decide-the-bundles-truncation-self-check.md) — the truncation self-check, Group D below.
- [Ticket 14](14-decide-how-a-fresh-run-gets-judged.md) §5 — the scorecard's `unmeasured` handling
  and the corrupted `scores-log.jsonl` line.
- [Ticket 21](21-decide-where-the-attempt-gate-lives.md) — the attempt gate, Group E below.
- [Ticket 09](09-decide-how-the-bundle-is-distributed-and-version-stamped.md) — distribution, the
  version stamp and the handover documents, Group F below. **It settles Group D's one open item**
  (the key format) and corrects one number in Group D's write-up.

Later-resolving tickets append to this list. **08, 09, 12 and 13 will each produce edits with no
other owner** — when one closes, add a line here pointing at it rather than creating another
execution ticket.

### Do

**Group A — land now, independent of 17** (ticket 05's "Land now" half):

1. Both record variants: delete `readinessCall.ai` and `readinessCall.delta`; bump `recordVersion`
   to `override-log-3` / `override-log-3-chat`. `readinessCall.lead` stays and its `reason` becomes
   unconditionally required — the old `delta != 0` trigger is gone.
2. ~~`index.html` and `site/index.html`~~ — **struck 2026-09-20. The hosted page is withdrawn**
   (owner's call, scope audit). The kill switch is on in the source and `site/` is rebuilt; nothing
   here needs editing, because nothing here is served any more. Item 3's `MutationObserver` widening
   goes with it — that guard is a property of this page.
3. Widen stop condition 3 to "the tool produces a readiness level, for anyone", per ticket 05's
   rewritten text, and widen the `MutationObserver` stop panel accordingly.
4. `score-review.js`: the derived scorer, computing readiness from the reported `blockingIssues`.
   Ticket 05 measured this at **26 of 27** and named its blind spot — **it is void on any deck where
   no rule fires**, so the scorer must return `unmeasured` there, not a level.
5. `scorecard.js`: ticket 14 §5 — `pct()` returns `null` not `0` on a zero judged denominator,
   `unmeasured (0 of N pairs judged)` instead of a percentage, `renderShareable()` omits what it
   cannot substantiate, the "recall is a floor" note qualified to judged pairs, and the
   `frozen-2026-08-09|||mc-match-3` log line corrected to `mcRecall=null, mcCases=0` with a note.
   Also remove the readiness lines from `renderShareable()` (:223-234) per ticket 05 decision 3.
6. The doc sweep — six places that now assert something false: `26-chat-native.md:262`,
   `17-override-log.md:209`, `:132-134`, `:148-149`, `28-shared-corpus.md:188-194`, and
   `22-trust-boundary.md` §3.

**Group B — after ticket 17's verification run (done, 2026-09-19) and after ticket 15.**

Ticket 17 has landed, so 05's original constraint is satisfied. But 17 produced a **third** prompt
version, `frozen-2026-09-19`, and [ticket 15](15-decide-whether-to-keep-or-roll-back-frozen-2026-08-09.md)
now chooses between three candidates rather than two. **Group B edits `PASTE-1-system-prompt.txt`,
so it must know which version ships.** Group A does not touch the prompt and can land immediately.

7. `TEST-KIT/PASTE-1-system-prompt.txt`: the level assignment at :167, the no-blocker default and
   discretionary demote at :169-181, `readiness` from the OUTPUT block. **The five blocking rules
   and `blockingIssues[].rule` stay** — A1 needs them and so does the derivation in step 4.
8. `TEST-KIT/PASTE-2C-artifact-path.md`: the mandatory `aiLevel` (:42), its derivation rule (:96),
   the "AI guess" pill (:216). Note ticket 05's finding that **this path has no redaction and no
   stop panel** and the same template renders student mode — if fixing that is more than removing
   the field, it is ticket 13's business, not yours.
9. `03-output-contract.md` and `check-review-v2.js`: the `readiness` level field. Ticket 17 already
   touched these files for confidence; coordinate rather than reverting its change.

### Two things to get right

**`22-trust-boundary.md` rows `:21` and `:22` go red when Group B lands, and that was accepted
knowingly.** Mark them NOT MET with the reason and the date. Do not quietly leave them green, and
do not treat going red as a failure of this ticket — it is the honest state until the artifact path
and the JSON fallback stop emitting a level.

**Re-run `check-docs.js` and the contract validator after each group.** The rubric-versus-source-register
check has caught drift before (commit a036170) and six documents are changing here.

Answer records: what landed in each group, which trust-boundary rows moved and to what, the state of
`check-docs.js` after, and anything the source tickets left underspecified that had to be routed back.

---

## Appended 2026-09-20 from ticket 11 (prep, ticket 11 still open)

10. **`TEST-KIT/PASTE-SETUP-combined.md` is a stale build and must be regenerated.** It is
    41,873 chars built 2026-08-30 and embeds the **pre-ticket-17** paste 1 — the loose blocking
    rule 1 and the still-gated severity floor, both of which ticket 17 changed and measured.
    Anyone handed the test kit today tests a prompt that no longer exists. It is
    wrapper + `PASTE-1-system-prompt.txt` + `PASTE-2A-chat-path.md`; a current rebuild is at
    `.scratch/deliverable-reviewer/ticket-11/PASTE-SETUP-combined-CURRENT.md` (42,297 chars).
    **This belongs in Group B**, not Group A: it is a derivative of paste 1, so it must be
    rebuilt *after* the paste-1 edits in step 7 land, or it will be stale again on arrival.
    It also needs a build step or a version stamp so the drift cannot recur silently — it did
    recur silently, which is the whole reason this line exists.

---

## Appended 2026-09-20 from ticket 15 (closed). Group B's blocker is lifted.

**The version is named: the pilot runs `frozen-2026-09-19`.** Group B may proceed on the prompt.

Ticket 15 found that the question "which version ships" had a false premise. **Paste 1 of the chat
path is *"section A of `04-prompt-templates.md`"* — a live file, not a frozen copy
(`CHAT-CONTEXT.md:7-12`).** Ticket 17 patched that file in place, so `frozen-2026-09-19` has been
the shipped prompt since 2026-09-19 without a decision. It is now ratified rather than reversed.

But **paste 2 was never brought with it**, and the two documents now contradict each other:

11. **`CHAT-CONTEXT.md:313` — delete the confidence line.** It instructs the reviewer to write
    `Confidence in this review: <Low | Medium | High>`. Paste 1 at `04-prompt-templates.md:244`
    now reads *"You report no confidence label."* **Paste 2 wins**, because it holds the output
    template, so the retired label is still being emitted on the pilot path. Ticket 17 deleted
    confidence from the contract, the validator and the response schema, and stopped there.
12. **`CHAT-CONTEXT.md:364` and `:367` — the record stamp is wrong on both fields.** It stamps
    `"recordVersion": "override-log-2-chat"` (ticket 05 decision 2 bumps it to `override-log-3-chat`)
    and `"promptVersion": "frozen-2026-08-09"`. **Every record a pilot produces today would name
    the wrong prompt**, and the paste-back record is the only trace a chat review leaves.
13. **Walk the whole of paste 2's template against the patched paste 1.** Nobody has done this
    since 2026-08-09. Items 11 and 12 are what one read found; they are not a guarantee of
    completeness.

### The standing hazard, routed here rather than decided in ticket 15

**Any session that edits section A of `04-prompt-templates.md` ships to the pilot, immediately,
with no decision and no record.** That is how `frozen-2026-09-19` became live. It is the same
failure the ticket 11 append above found in `PASTE-SETUP-combined.md` — a derivative that drifted
silently from paste 1 — arriving from the other direction, and two independent instances in one day
make it structural rather than a slip.

Pick one and do it as part of Group B:

- **Pin paste 1.** Point `CHAT-CONTEXT.md:8` at an archived copy under
  `eval-runs/prompt-archive/frozen-2026-09-19.txt`, so shipping becomes an explicit act. Cost:
  another derivative to keep current, which is the thing that just failed twice.
- **Or check it.** Add a `check-docs.js` assertion that paste 1's version tag, paste 2's record
  stamp and the combined test-kit build all name the same frozen version. Cheaper, and it catches
  the class rather than the instance. `check-docs.js` has no such check today.

The second is the recommendation, on the grounds that both of today's instances were *drift between
artifacts*, which a check detects and a pin does not.

### One thing Group B must not wait for

The owner reopened the readiness question on 2026-09-20, in a different form — a score computed
from the findings rather than a ceiling the model judges. That is
[ticket 22](22-decide-the-findings-based-severity-score.md). **Group B does not wait for it and
does not preserve the old field.** Step 7 deletes the emitted level exactly as ticket 05 wrote it;
ticket 22 starts from a tool that produces no level.

---

## Appended 2026-09-20 from [ticket 10](10-design-the-consultant-feedback-loop.md)

Ticket 10 closed into four edits with no other owner. Source of truth is its section 8; read it
rather than working from these lines.

1. **A student-side record.** The paste-back block at `TEST-KIT/PASTE-2A-chat-path.md:348` is
   lead-shaped throughout — `lead.id`, `lead.vsByHand`, `readinessCall.lead`. It needs an `attempt`
   field and a student variant, or the student produces nothing recordable and the pilot has no
   student-side evidence at all. Land this with the `override-log-3-chat` bump in Group A rather
   than as a second version bump.
2. **The cycle census, written down** as a document alongside `17-override-log.md`: its five
   questions and ticket 10 section 5's response-rate table, which is pre-registered and must not be
   softened or re-derived when the pilot is designed.
3. **Correct `17-override-log.md`.** Mark sections 3 and 4.1 **void** against the product path, and
   say why — they are written against the Triage Desk in `index.html`, and the hosted page is out of
   scope. Mark 4.2 (`added[]`) and 4.3 (`mustCatch`) **already present** in the paste-back block. As
   the document stands, all four read as outstanding work, and a build session would build the
   wrong thing from it.
4. **The attempt gate on the chat path is NOT in this list.** Ticket 10 named it as an edit and then
   routed it out, because its placement is a live decision — see
   [ticket 21](21-decide-where-the-attempt-gate-lives.md). Do not add a gate from ticket 10's
   description; wait for 21. This is the routing rule this ticket was given, working as intended.

---

## Group D — the truncation self-check (from ticket 12, appended 2026-09-20)

Source of truth is [ticket 12](12-decide-the-bundles-truncation-self-check.md) and its prototype
[RESULTS.md](../proto-12-selfcheck/RESULTS.md). **Every item below was run against a truncated
bundle before it was written down** — that was the ticket's binding condition. Working copies of the
exact inserted text are in `proto-12-selfcheck/build2.py`.

**Three of these are one mechanism and must land together.** Items 1, 2 and 3 are a single
interlock; shipping 1 and 2 without 3 was measured and it fails — the model detects the missing key
and writes the review anyway, 5 of 5.

1. **`PASTE-1-system-prompt.txt`, very top, above `ROLE`:** add
   `BUNDLE KEY (part 1): <key 1>` followed by the KEYS rule (text in `build2.py`, constant `RULE`).
   It goes at the very top deliberately: it is then the first thing a partial head cut removes.
2. **`PASTE-2A-chat-path.md`, last line:** add `BUNDLE KEY (part 2): <key 2>`.
3. **`PASTE-2A-chat-path.md`, immediately above `## The template`:** restate the same KEYS rule
   verbatim, and change the template's first line from
   `REVIEW OF: <artifact type, one line> | MODE: <short | deep | lead>` to
   `REVIEW OF: <artifact type, one line> | MODE: <short | deep | lead> | KEYS: <part 1>/<part 2>`.
   **Do not move this rule to the tail beside the key it protects** — that placement was measured
   and it is cut off by exactly the truncation it exists to catch.
4. **`PASTE-2A-chat-path.md`:** state the noise budget, which ticket 04 found is cited by both
   pastes and present in neither. 89 tokens; text in ticket 12's resolution, values from
   `00-product-definition.md` section 6. **This is a missing rule, not redundancy** — the restraint
   ceiling is unenforced on the chat path today, truncated or not.
5. **`PASTE-1-system-prompt.txt`:** delete the dangling `(see the scope matrix you were given)`
   citation. The matrix is in neither paste; it feeds only the JSON/rubric branch, which is a defect
   path, so the citation is removed rather than the matrix added.
6. **Student-facing instructions (wherever the bundle is handed over — ticket 09 owns where):**
   one line, and the wording matters. *"The first line of your review must read exactly
   `KEYS: <key 1>/<key 2>`. Anything else means part of the setup did not arrive: start a new chat
   and paste it again."* **Never phrase this as "look for the word MISSING"** — where the rule had
   been cut off, models wrote `<missing>`, `part 2 missing` and `part 2 not provided` instead.
7. **`TEST-KIT/PASTE-SETUP-combined.md` is a stale build** and must be regenerated from the two
   paste sources, with a build step or stamp so it cannot drift silently again. Filed by ticket 11's
   run sheet, repeated here because items 1–4 change both sources and the combined file will
   otherwise ship the old prompt with the new instructions. **This one is not optional now.**

### Not to be built from this ticket

- **The three marker strings are not shipped to students.** They stay in ticket 11's run sheet as
  the tester's instrument, with its positive control. Ticket 12 decided this deliberately; do not
  add them to the bundle because they look like a self-check.
- **Do not restate the synthesis protocol in paste 2A.** 1,377 tokens, and ticket 12 routed the
  trade to the owner rather than deciding it (Q3). Wait for the answer.
- ~~**The keys' exact form is unsettled.**~~ **Struck 2026-09-20 by Group F item 1, which answers
  it by measurement: part 1 is `MMDD-XXXXXXX`, part 2 stays meaningless, 11 runs of the readable
  variant with 0 inventions and 0 date drift. The bullet is struck rather than deleted so that a
  reader coming from ticket 12 can see the question was closed rather than dropped.**

## Group E — the attempt gate (from ticket 21, appended 2026-09-20)

Source of truth is [ticket 21](21-decide-where-the-attempt-gate-lives.md) and its prototype
[RESULTS.md](../ticket-21/RESULTS.md). **Every item below was run against the ticket 04 truncation
arms before it was written down** — the ticket's binding condition. The exact gate text is in
`ticket-21/build-gate-arms.py`, constant `GATE` (the line-2 wording is the `AFTER` variant built
in the same file).

**This builds the gate for the first time. It does not move one.** The hosted page that carried it
(`PASTE-2B:154`) was withdrawn on 2026-09-20, so there is no existing gate on any path a user can
reach. Ticket 20 already carries an instruction not to build the gate from ticket 10's
description; **build it from this group instead.**

**Group E and Group D touch the same two lines of output and were measured to be compatible.**
Group D's item 3 extends line 1 to `REVIEW OF: … | MODE: … | KEYS: <part 1>/<part 2>`. Group E adds
line 2 and does not touch line 1. **If either group's line-1 decision changes, the other must be
re-checked before shipping.**

1. **`PASTE-3` / section B of `04-prompt-templates.md` (the team input template), very top:** add
   the gate block. **This is the primary copy and the position is the finding** — the deck is the
   newest turn, so it is the last thing a window evicts. Measured: it refused on the exact cut that
   left every other placement ungated, on both model families.
2. **`PASTE-1-system-prompt.txt`, top:** add the same gate block. **Not redundancy** — it covers a
   different failure, the student who never sends paste 2, measured (`p1only-no` refused; the same
   bundle without it fell through to the JSON branch and emitted the ten-dimension rubric **with a
   readiness level**, which is a live stop-condition-3 violation).
3. **Do not put the gate in `PASTE-2A-chat-path.md`.** It covers nothing the other two do not, and
   it dies in the one cut paste 3 survives. Two copies, 396 tokens, +4.3% of the instruction
   bundle.
4. **Failure behaviour is refusal, not a caveat.** With no attempt the reply is the
   `ATTEMPT REQUIRED` line and nothing else. Measured 16 of 16, including 4 of 4 where the student
   argued back after the refusal.
5. **The gate text must not contain a word count.** State presence and specificity in plain words.
   **Measured: a model-enforced 20-word rule refused a genuine eight-word attempt on both
   families.** Ticket 10's 20-word rule stays, as a measurement-side rule only — bypasses are
   counted after the fact and the bypass rate is reported beside the capture rate.
6. **`PASTE-2A-chat-path.md`, the output template:** add a second line, immediately under the
   `REVIEW OF:` line, reading `ATTEMPT ON RECORD: "<the consultant's own read, first sentence,
   verbatim>"`. **Line 2, never line 1** — line 1 belongs to Group D.
7. **Student-side record:** add an `attempt` field (the verbatim text) and a `bypass` boolean to
   the paste-back block. Ticket 10 called for this; the threshold that sets `bypass` is applied
   when the record is read, not by the model.
8. **Wherever the marker is documented, describe it as one-sided.** *Presence proves an attempt;
   absence proves nothing.* Measured: 0 fabrications in 6 ungated runs, but present only 10 of 11
   times when an attempt was given and on the instructed line only 7 of 11. **Do not write it up as
   a check that the gate fired** — that is the failure ticket 12 names, a check that reads as
   assurance.

### Not to be built from this group

- **No model-enforced attempt threshold**, in either paste, in any wording. See item 5.
- **No caveat-and-review branch.** Not measured, and it would give a student a review with no
  attempt, which is the whole thing the gate exists to prevent.
- **Nothing that claims the gate is guaranteed.** If eviction reaches into paste 3's head the gate
  is gone and the review proceeds normally. Group D's key interlock covers the nearest version of
  that cut — the paste-1 key is gone while the demand for it survives, so the review is refused
  before the missing gate matters — but a cut deep enough to take the demand line too leaves
  nothing. Whether a real free tier cuts that deep is unmeasured (ticket 11). **Ship Group D and
  Group E together; neither alone gives what the pair gives.**


**Owner answers recorded 2026-09-20** in [DECISIONS-2026-09-20.md](../DECISIONS-2026-09-20.md) Part 4. Read it before acting on the questions in this ticket.

## Group F — distribution, the version stamp, and the handover (from ticket 09, appended 2026-09-20)

Source of truth is [ticket 09](09-decide-how-the-bundle-is-distributed-and-version-stamped.md),
its two written deliverables `ticket-09/HANDOVER.md` and `ticket-09/PUBLISHING.md`, and the run in
[proto-12-selfcheck/RESULTS-B3.md](../proto-12-selfcheck/RESULTS-B3.md).

**This group resolves Group D's one open item.** Group D says *"the keys' exact form is unsettled …
until it is answered, use arbitrary strings."* It is answered, by measurement.

### 1. The key format is settled — amend Group D

**Part 1 becomes `MMDD-XXXXXXX`** (a release date, a hyphen, a random alphanumeric chunk:
`0919-SIGMA7K`). **Part 2 stays meaningless** (`DELTA-3Q`). Both regenerate every release.

Measured before it was written down: 11 runs of the readable variant, complete and truncated arms,
**0 inventions and 0 date drift** with the run date one day after the key's date. Delete Group D's
"Not to be built from this ticket" bullet about the keys being unsettled; this replaces it.

**The date prefix is not the authoritative version.** `releases/REGISTER.md` is. Anything that
parses the prefix as a version rather than looking the key up is a bug.

### 2. Correct one number in Group D's write-up

Group D inherits ticket 12's *"refused 9 of 9, on both families."* The run files say eight Codex
cut runs and **one** Claude cut run. Three further Claude runs on the `headdrop` arm detected the
missing key and **reviewed anyway, 3 of 3** (contaminated framing, and a prompt confound recorded
in `RESULTS-B3.md`).

**Nothing about what ships changes.** What changes is what may be written beside it:

- refusal: **8 of 8 on Codex; 1 of 4 on Haiku 4.5, contaminated** — not "both families"
- the **student-side string comparison** is the half that held on every run of both families, and
  it is the half that may be described as robust

Wherever the mechanism is documented, the refusal is the model's cooperation and the string
comparison is the check. Do not describe the interlock as resting on refusal.

### 3. Build `build-bundle.js`

One generator, because two hand-maintained derivatives have already gone stale undetected
(`TEST-KIT/PASTE-SETUP-combined.md`, three months; paste 2, independently).

- `--release` mints a key pair, writes `releases/<key1>/` with `REVIEWER-SETUP.txt`,
  `COVER-SHEET.md`, `TEAM-INPUT-TEMPLATE.txt`, `MANIFEST.json` (keys, byte counts, sha256, source
  versions), and appends a row to `releases/REGISTER.md`.
- `--check` joins `check-docs.js` and **fails** when a released file is not byte-identical to a
  fresh generate from its recorded sources, when a key is missing from or duplicated in the
  register, when the cover sheet's key differs from the one embedded in the setup file, or when
  `TEST-KIT/PASTE-SETUP-combined.md` exists as a hand-maintained file.
- `--verify-drive <file> --release <key>` diffs a copy-out of the Drive Doc against the generated
  file and prints `IDENTICAL` or the first difference.

**This supersedes Group D item 7 and the ticket 11 append's item 10** — regenerating
`PASTE-SETUP-combined.md` by hand is not the fix; it stops being a hand-maintained file.

### 4. The cover sheet, and the one line whose wording is load-bearing

Generated per release. Four items, in order: paste this as one message then your deck then your own
read; the exact line 1 to expect; where to get a fresh copy; what the tool does not do.

Item 2 is Group D item 6, verbatim and non-negotiable: *"The first line of your review must read
exactly `KEYS: <key 1>/<key 2>`. Anything else means part of the setup did not arrive: start a new
chat and paste it again."* **Never "look for the word MISSING"** — models wrote `<missing>`,
`part 2 missing` and `part 2 not provided`.

### 5. Google Drive

A single fixed folder, shared **anyone with the link — viewer**. Its link is printed inside the
bundle (Q1's refusal message), so it is baked into artifacts already in people's hands.

- **The folder link never changes.** Not per release, not on a tidy-up.
- **Link to the folder, never to a file** — replacing a Drive file can mint a new ID.
- **The setup goes in as a Google Doc, not a `.txt`** — 42,000 characters have to be selected and
  copied in one action, and Drive's text preview makes that painful on a phone.
- **Previous releases move to `archive/`, never deleted** — someone may be mid-engagement holding
  one, and the register must stay resolvable.
- **Publishing is not finished until `--verify-drive` prints `IDENTICAL`.** A Doc is where smart
  quotes and autocorrected dashes get in. The fix for a mismatch is to re-paste the Doc from the
  generated file, never to edit the Doc.

### 6. The mismatch rule, wherever records are read

| line 1 | disposition |
|---|---|
| current key pair | admissible for everything |
| retired pair, in the register | kept and flagged; evidence about that version only |
| key not in the register | quarantine — hand-edited bundle or mistyped key |
| `MISSING` in either half | not a review record; counted in the truncation rate |
| no KEYS field | quarantine — pre-interlock, or a cut that took the demand line |

**Comparisons are always within a key, never across.** Applies to whatever ticket 07 becomes.

**Add a truncation counter** — `MISSING` events over total runs. It is the only live measurement of
how often real windows cut, it costs nothing, and it does not reopen the free-tier work deferred in
Q7. **Report it as a floor, not a rate**: it counts the cuts the interlock catches.

### 7. Land the two documents in the repo

`ticket-09/HANDOVER.md` and `ticket-09/PUBLISHING.md` are written and are `.scratch/` artifacts
today. They are the deliverable of the owner's Q3 answer — *"it just needs to be clear and
documented"* — so they belong in the product tree, as `29-handover.md` and `30-publishing.md`
under `tools/quality-reviewer/v2/`, with their relative links fixed.

**Check them against reality when you land them**, in this order, because a handover document that
is wrong is worse than none: HANDOVER §5.1's claim that stop condition 3 is widened depends on
Group A item 3 having landed; §5.2's description of the gate depends on Group E; §5.3's description
of the key depends on Group D plus item 1 above. **If a group has not landed, fix the document, do
not fix the claim.**

### Not to be built from this group

- **No per-release Drive folder, and no direct file links.** See item 5; the link is already in
  circulation inside the bundle.
- **No expiry date inside the bundle.** It asks the model to reason about dates, which is the
  confabulation surface the whole interlock exists to avoid. Staleness is visible through the key
  and the register.
- **No separate student bundle.** One generated source, two channels. The difference between
  populations is MODE and documentation, never bytes.
- **Do not branch the attempt gate by audience** to satisfy Q4's "students only". It adds an
  untested escape hatch to the one check measured to be un-arguable-with, and a student who hears
  about it reaches it by claiming to be a lead. Flagged for the owner in HANDOVER §5.5; **one line
  and one fresh run if he wants it.**


**Owner ruling 2026-09-20, and it overrides ticket 09's resolution of the same point.** **Leads do not type; students do; the audience branch is one named switch with one documented default.** Ticket 09 resolved this as unconditional by inference from a remark the owner had already withdrawn; he has now confirmed students-only a second time, knowing the escape-hatch objection. Build the switch, do not resolve this from ticket 09's write-up, and correct HANDOVER section 5.5. Full ruling and its two consequences - the bypass as an accepted gap, and the mandatory re-run of the branched gate - are in [DECISIONS-2026-09-20.md](../DECISIONS-2026-09-20.md), Q4 final ruling.

---

## Answer (2026-09-20)

**Everything on this ticket landed except one thing, and that one thing is half the verification
run.** Working record: [ticket-20/RESULTS.md](../ticket-20/RESULTS.md).

**This is the first ticket on this map that changed something a user would notice.** Twelve
resolutions preceded it and not one of them did.

### 0. The one thing that did not land

**Codex did not run.** The account hit its usage limit before the first arm, at 21:09 on
2026-09-20, resetting 2026-09-21 01:13. Five arms, zero bytes of reply, stderr preserved in
`ticket-20/runs/codex-blocked/`. The Haiku family ran and passed **6 of 6**.

So the shipped configuration is **verified on one model family, not two**, and the rule this map
has applied throughout says one family is not enough. The consequence is concrete rather than
bookkeeping:

> **Do not cut a release until `bash .scratch/deliverable-reviewer/ticket-20/run-codex.sh`
> has run and `python score.py` is clean.**

Nothing is in a user's hands in the meantime, and that is structural rather than lucky — see
section 5.

### 1. What landed, by group

**Group A — the readiness retirement, land-now half.**

| item | where | state |
|---|---|---|
| 1. record variants: `readinessCall.ai` and `.delta` deleted, `recordVersion` bumped, `reason` unconditional | `CHAT-CONTEXT.md` (chat variant, `override-log-3-chat`), `17-override-log.md` (lead variant spec, `override-log-3`) | **landed** |
| 2. `index.html` / `site/index.html` | — | **struck by the ticket**; the hosted page is withdrawn. Consequence recorded in section 3 below rather than silently skipped |
| 3. stop condition 3 widened | `22-trust-boundary.md` | **landed**, and it is now enforced by the validator rather than asserted |
| 4. derived readiness scorer | `score-review.js` | **landed**. `deriveReadiness()` + `RULE_CEILING`; returns `unmeasured` where no rule fired, with the blind spot named in the code |
| 5. scorecard `unmeasured` handling | `scorecard.js` | **landed**, and it reached further than the ticket said — see section 2 |
| 6. the doc sweep, six places | `26-chat-native.md`, `17-override-log.md` x3, `28-shared-corpus.md`, `22-trust-boundary.md` §3 | **landed** |
| ticket 10's student-side record | `CHAT-CONTEXT.md`, `17-override-log.md` | **landed** as part of the same version bump, as instructed |

**Group B — the prompt, on `frozen-2026-09-19`.**

| item | where | state |
|---|---|---|
| 7. the level assignment, the no-blocker discretionary demote, the level out of the output | `04-prompt-templates.md` §A | **landed**. The five blocking rules and their ceilings stay, as ticket 05 specified; what goes is the instruction to turn them into a level |
| 8. `aiLevel`, its derivation rule, the "AI guess" pill | `TEST-KIT/PASTE-2C-artifact-path.md` | **landed**, plus the confidence label — see section 2 |
| 9. the `readiness` level field | `03-output-contract.md`, `check-review-v2.js` | **landed**. The validator now *rejects* a level rather than validating one |
| 10. `PASTE-SETUP-combined.md` regenerated | — | **superseded by Group F item 3.** The file is deleted and `--check` fails if it reappears |
| 11. the confidence line | `CHAT-CONTEXT.md` | **landed** |
| 12. the record stamp on both fields | `CHAT-CONTEXT.md` | **landed** |
| 13. walk paste 2 against the patched paste 1 | both | **done, and it found two things** — section 2 |
| the standing hazard: pin or check | `check-docs.js` + `build-bundle.js --check` | **check, as recommended.** It catches the class rather than the instance |

**Group D — the truncation interlock.** All seven landed. Items 1, 2 and 3 are one interlock and
shipped together, as the ticket requires. The KEYS rule is verbatim from `proto-12-selfcheck/
build2.py` and sits immediately above `## The template`, the position that was measured. Item 6's
wording is verbatim and is generated onto the cover sheet. Item 7 is superseded by Group F.

**Group E — the attempt gate, built for the first time.** All eight landed, in paste 3 and paste
1, not paste 2. Failure behaviour is refusal. No word count is written anywhere in the bundle.
The marker is on line 2 and is documented as one-sided everywhere it appears. The audience branch
is section 4.

**Group F — distribution, the stamp, the handover.** `build-bundle.js` is written with
`--release`, `--check`, `--sync-test-kit` and `--verify-drive`. Key format is `MMDD-XXXXXXX` /
meaningless, minted from an alphabet with `I`, `O`, `0` and `1` removed because these are copied
by hand. `HANDOVER.md` and `PUBLISHING.md` landed as
[29-handover.md](../../../tools/quality-reviewer/v2/29-handover.md) and
[30-publishing.md](../../../tools/quality-reviewer/v2/30-publishing.md). The cycle census landed as
[31-cycle-census.md](../../../tools/quality-reviewer/v2/31-cycle-census.md) (ticket 10 edit 2).
The "refused 9 of 9, on both families" wording is corrected at both places it lived.

**Ticket 22** resolved in the same pass and applied: a `COUNT:` line, no single score, fenced in
the template against being read as a verdict.

### 2. Four things the edit lists did not name, and why they were done anyway

Each is a recorded decision applied to a site the list missed, not a new decision. They are listed
separately so a reader can disagree with each one.

1. **The second false-zero log line.** Ticket 14 named `frozen-2026-08-09|||mc-match-3` as
   carrying `mcRecall=0, mcCases=9` when nothing was judged. **The 2026-09-19 run has the identical
   defect** — 9 of 9 `unscored` — and it postdates ticket 14, which is why the ticket could not
   name it. Correcting one and leaving the other would have left `--trend` still rendering a
   collapse. Both corrected, both carrying the note.
2. **Derived readiness gets the same judged-denominator treatment as must-catch.** Ticket 14 §5 is
   written about must-catch. The derived level has the identical failure — a case where no rule
   fired can never reach the numerator, so leaving it in the denominator makes it arithmetically a
   miss. Ticket 20 step 4 already requires `unmeasured` rather than a level; this is the other half
   of the same instruction.
3. **The confidence label in `PASTE-2C`.** Ticket 05's scope explicitly grew to cover it
   (*"the confidence label retires alongside readiness"*); ticket 17 removed it from the contract,
   the validator and the response schema and stopped, so this copy survived. Same class, same edit
   surface.
4. **`TEST-KIT/PASTE-1-system-prompt.txt` and `PASTE-2A-chat-path.md` became generated files.**
   Group F item 3 names one generator because *"two hand-maintained derivatives have already gone
   stale undetected"*. These two are byte-identical copies of the sources — exactly that class —
   so they are generated with a fixed test key pair and `--check` asserts identity.

**And two things the walk in item 13 found**, which are findings rather than applications:

- **Paste 1's noise-budget citation was dangling**, in the same way the scope-matrix citation was.
  It said "the noise budget for the mode (below)", and "below" is section C of
  `04-prompt-templates.md`, **which is not part of paste 1**. Ticket 04 found the budget was cited
  by both pastes and present in neither; Group D item 4 put it in paste 2, so the citation is
  repointed there with an inline fallback.
- **The severity vocabulary mapping was written down nowhere.** Paste 1 grades
  critical/major/minor, the template prints High impact/Moderate/Minor, and the record asks for
  critical/major/minor again. It now matters more than it did, because ticket 22's COUNT line
  counts those labels. Stated beside the template.

### 3. The trust-boundary rows

Both moved, both to NOT MET, both dated 2026-09-20 with the reason written in.

| row | before | after | why |
|---|---|---|---|
| `:21` a named pilot lead | **MET** | **NOT MET** | its A2 clause is enforcement "in the deployed path", and the deployed path is `index.html`, withdrawn. Its readiness clause is also rewritten per ticket 05 decision 4, and the lead picker's "AI guess" option was never removed because the page went out of scope before it was reached |
| `:22` a whole project team | **MET as of this build** | **NOT MET** | the student view, kept set and printable are the same withdrawn page. There is no payload, so the bar has nothing to be true of |
| `:25` the chat path | MET by construction | **unchanged** | no level is produced, so there is none to leak. This is the row that now carries the audience those two described |

**Neither red row is a regression in the reviewer**, and neither is something this ticket could
have fixed: they are red because the page they measure was withdrawn, which was a separate
decision. Ticket 20 was told not to leave them green and not to treat red as failure. They are
red, and the reason is in the cell.

### 4. The audience branch, which is the one place this ticket was told not to trust a source ticket

Ticket 09 resolved the gate as unconditional and wrote it into `HANDOVER.md` §5.2 and §5.5. The
owner's ruling reverses it, and **§5.5 is specifically the list of changes that look like
improvements and are not**, so an entry there contradicting a twice-given ruling was the most
damaging line in the document. It is rewritten rather than deleted, including what it used to say
and why that was wrong.

**How the switch is built.** `ATTEMPT_GATE_AUDIENCE` in `build-bundle.js`, default `'students'`.
The gate text in both pastes carries a `<<GATE_AUDIENCE>>` token that the generator fills. So:

- flipping to *everyone types* is **one line, in one findable place**, followed by a rebuild;
- both copies of the gate change together and cannot disagree;
- the clause is in the bundle bytes, so it survives paste 1 being evicted (which is the whole
  reason the gate has a paste-3 copy);
- the setting is stamped into `MANIFEST.json` and into the release register row, so a record can
  be read back to which audience rule produced it.

**The bypass is on the accepted-gaps list, in the owner's terms**: a student who selects lead mode
reaches the review without typing, that cannot be prevented from inside a prompt because there is
no identity to check, and it is detectable in aggregate through the capture rate and the
`ATTEMPT ON RECORD:` marker. Written into 29-handover.md §5.5 and 31-cycle-census.md §3.

### 5. Verification, and why nothing shipped unverified despite half of it being blocked

**Six arms, Haiku 4.5, 6 of 6.** The gate refuses a student who typed nothing and one who argued
after being refused; lead mode goes straight through on **byte-identical input differing only in
`MODE`**, which is the leak test; the truncation interlock still fires; the review's shape is
unchanged and no level appeared in any of the six replies. Full table and limits in
[RESULTS.md](../ticket-20/RESULTS.md).

**Two things that run surfaced and would not have been predicted:**

- The first cut arm refused for the **missing attempt**, not the missing key — the paste-3 gate
  fires before the key check, so that arm never tested the interlock at all. A second cut arm with
  the attempt supplied was added, and it is the one that tests it.
- The first scoring pass **failed** that arm, wrongly: it counted the `REVIEW OF:` header as a
  review, when writing that header is exactly what the refusal rule instructs. Scorer bug, fixed,
  and written down because retuning a scorer until a run passes is the failure this map keeps a
  standing caution about.

**Why nothing shipped unverified.** The standing hazard on this map is that editing section A of
`04-prompt-templates.md` ships to the pilot immediately, with no decision and no record. **That is
no longer true, and this ticket is what changed it.** The sources now carry `<<...>>` placeholders
and are not pasteable; what a person pastes is a generated release; and `--release` refuses while
`DRIVE_FOLDER_URL` is unset, which it is. So today's prompt edits reach nobody until someone
deliberately cuts a release — and the instruction in section 0 is not to cut one until Codex has
run.

### 6. Routed back rather than decided here

Only one, and it is small enough to state in full:

**The `readiness` object in `03-output-contract.md` still exists, holding `highestRiskIssue` and
`whatCouldChangeIt`.** Ticket 05 says to delete "the `readiness` level field". `level` is deleted
and so is `mainReason`, which was defined as *"the single reason readiness sits here"* and cannot
survive its referent. The other two fields are not levels, and `whatCouldChangeIt` is load-bearing
— the MISSING CONTEXT rule in paste 1 names it as the whole hedge. So an object called `readiness`
now contains no readiness. **That is cosmetic and it is ugly, and renaming it is a contract change
nobody authorised.** Left as-is, flagged here. It affects the JSON branch only, which is a defect
path on the pilot route.

### 7. Two preconditions for the pilot, neither of which is a decision

1. **The Google Drive folder does not exist.** Its link goes inside every bundle, in the refusal a
   student sees when their paste was cut, so it cannot be added afterwards to copies already
   issued. `--release` refuses while `DRIVE_FOLDER_URL` is null and prints what to do.
   30-publishing.md section 3 has the rules the folder has to satisfy.
2. **The Codex arms.** Section 0.

### 8. `check-docs.js` after

```
check-docs  ground truth from the code
  prompt   frozen-2026-09-19  sha256:1aa45d46b05e601b
  matcher  mc-match-3  (no cut points, LLM judge)
  record   override-log-2
  scope    74 markdown documents

clean. 74 documents, no version drift, no dead references.

build-bundle --check OK  (0 release(s), prompt frozen-2026-09-19, gate audience students)

PROVENANCE, 01-rubric-v1.md against 10-source-register.md:
  dimension 5 names S4, which does not list dimension 5
```

Three notes on that output:

- **The provenance finding is pre-existing** and this ticket did not touch either file. It is the
  same check that caught real drift in commit `a036170`. Not in scope here; worth a ticket.
- **`record override-log-2` is read out of `index.html`**, the withdrawn page, so check-docs's
  ground truth for the record version now comes from something that does not ship. It does not
  produce a false finding today — the check permits a document naming a *higher* version — but the
  ground truth is stale by construction. Recorded, not fixed.
- The bundle check is new and runs inside `check-docs.js`, as 30-publishing.md section 5 says.

The contract validator was run against `eval-cases/case-01.review.json` and correctly returns
INVALID on three counts: a `readiness.level`, and two blocking issues carrying a `ceiling`. Old
reviews failing the new check is the intended behaviour, not a regression.
