# 17. The override log

**Status:** spec current at `override-log-3`; no renderer emits it. Written 2026-08-03 as a
spec. `index.html` emitted `override-log-2` and validated either earlier version on load, and
that page was **withdrawn on 2026-09-20** (kill switch on, out of scope), so nothing emits the
lead variant today. **The shipped record is the chat variant**, `override-log-3-chat`, typed by
hand into the paste-back block of [CHAT-CONTEXT.md](CHAT-CONTEXT.md). The two variants differ in
the `who` block and nothing else.
**Scope:** what a lead's decision captures, what that record is worth, and what it is not.

When this was written the Triage Desk rendered this string:

> You overrode the AI by 2 level(s). Logged for calibration.

and nothing was logged. This document specified the record that sentence was promising. It is
now the record the product actually writes, and the honest accounting of how far it goes, in
section 5, is unchanged and still the part to read before quoting the thirty hours.

---

## 1. Why this is the piece worth building

Nine gold labels cost about thirty hours of expert time and are the binding constraint on
every measurement in this project. A lead triaging a real deliverable produces a decision of
roughly the same shape in about four minutes, as a byproduct of work they were doing anyway.

That argument is strong and it is also the argument most likely to be over-claimed. Section 5
is the honest accounting. Read it before quoting the thirty hours.

---

## 2. The record

One JSON object per completed triage. `override-log-1`.

**Amended 2026-08-07 to `override-log-2`.** Two fields added, none removed or changed, so
anything that read version 1 reads version 2 and the renderer restores either.

**Amended 2026-09-20 to `override-log-3` (ticket 05 decisions 2 and 5).** Unlike the last bump
this one **removes** fields, so a version-3 reader cannot assume a version-2 shape and the bump
is not cosmetic:

| change | what | why |
|---|---|---|
| removed | `readinessCall.ai` | the reviewer produces no readiness level, for anyone. On the chat path this was already always `null`; the record now agrees with the product instead of holding a slot for an opinion that does not exist. |
| removed | `readinessCall.delta` | it is the difference between the lead's call and the AI's, and one side of the subtraction is gone. |
| kept | `readinessCall.lead` | **the only field in the record that is not a reaction to the tool's output.** Section 5.1 names selection bias as this record's core weakness, and this is the one field that does not suffer it. |
| changed | `readinessCall.reason` | now required unconditionally, not just when the lead differed from the AI. See section 2's note. |
| added | `student` block: `id`, `attempt`, `bypass` | the paste-back block was lead-shaped throughout, so a student produced nothing recordable and the pilot would have had no student-side evidence at all (ticket 10). `attempt` is the verbatim read the student typed; `bypass` is set when the record is read, never by the model. |

| added field | what it holds | why |
|---|---|---|
| `quoteCheck` | `status` (`verified`, `failed`, `waived`, `unverified`), `checkedAt`, `quotesChecked`, `quotesMissing`, `deckSha256`, `deckChars`, `waiveReason` | The renderer now verifies every quote against the deck text the lead supplies, and nothing goes out until it passes or the lead waives it in writing. A triage released on a waiver has to be findable afterwards. The deck text itself is client-confidential and is never kept, in the tab or in `localStorage`, so the record ties the verdict to a hash and not to content. |
| `lead.vsByHand` | `faster`, `same`, `slower` or `null` | `secondsOnTask` has always been recorded and has never been interpretable, because nothing captured what the same work costs without the tool. This is the counterfactual, asked once at release. |

Both exist to make a stop condition detectable rather than noticed. The control document is
[22-trust-boundary.md](22-trust-boundary.md).

```json
{
  "recordVersion": "override-log-3",
  "id": "2026-08-05T14-02-11Z--aurora--real-13",
  "capturedAt": "2026-08-05T14:02:11Z",

  "quoteCheck": {
    "status": "verified",
    "checkedAt": "2026-08-05T13:58:02Z",
    "quotesChecked": 15,
    "quotesMissing": 0,
    "deckSha256": "74642b9f8d33cf79",
    "deckChars": 41822,
    "waiveReason": ""
  },

  "reviewer": {
    "promptVersion": "frozen-2026-08-03",
    "promptSha256": "39c18fbca9e5d218",
    "mode": "deep",
    "executionMode": "claude-code-subagent"
  },

  "deliverable": {
    "ref": "real-13",
    "client": "Client Z",
    "artifactType": "final recommendation deck",
    "slideCount": 26,
    "stage": "final",
    "inputSha256": "6523e730acf321c3"
  },

  "lead": { "id": "ms", "role": "project lead", "ownsTheTeam": true, "secondsOnTask": 247 },

  "ai": {
    "readiness": "Needs targeted revision",
    "blockingRules": [],
    "findings": [
      { "fid": "a1c4e9", "short": "No sources named", "severity": "minor",
        "dimension": "Evidence quality", "issueType": "evidence", "slides": [10, 23] }
    ]
  },

  "decisions": [
    { "fid": "a1c4e9", "action": "keep", "cutReason": null, "note": "" }
  ],

  "added": [
    { "short": "Model basis never stated", "severity": "major",
      "dimension": "Analysis and insight", "slides": [17], "note": "" }
  ],

  "mustCatch": "a1c4e9",

  "readinessCall": {
    "lead": "Needs substantial revision",
    "reason": "The model on 17 is the whole recommendation and it is unexplained."
  },

  "sent": true
}
```

### Field notes that matter

**`fid` needs no contract change.** The output contract has no finding id and this spec does
not propose adding one — the contract is frozen and under measurement. Derive it:
`sha256(finding.short + '|' + firstEvidenceQuote).slice(0,6)`. Stable for a given review,
recomputable later from the stored review, and it survives reordering.

**`inputSha256`** ties the record to the exact bytes reviewed. Without it a record cannot be
replayed against a re-run, which is the whole point of collecting it.

**`cutReason`** is a closed vocabulary and it is the field that turns a cut into a label:

| value | meaning | what it labels |
|---|---|---|
| `wrong` | the finding is not true of this deck | a **false positive** |
| `not-an-issue` | true, but not a problem here | a **calibration** error, not a factual one |
| `too-minor` | true and real, below the bar for the team's time | a **restraint** failure |
| `duplicate` | already covered by another finding | a **dedup** failure |
| `out-of-scope` | true but the brief never asked | a **scope** error |

Without this split, a "cut" is uninterpretable: it conflates "the tool hallucinated" with
"correct, but I have bigger problems this week". Those two demand opposite fixes. **If only
one thing from this document gets built, build this field.**

**`reason` on `readinessCall` is required unconditionally** and must be refused empty.
Corrected 2026-09-20 (ticket 05 decision 5): the old trigger was `delta != 0`, a comparison
against the tool's own level, and it cannot fire now that the tool has no level to differ
from. On the chat path it never could. It remains the single highest-value free-text field in
the record -- a human explaining, in their own words, what they think the state of the
deliverable is.

**Flagged when this was decided, and worth holding:** ticket 10's binding constraint is that
anything over two minutes will not survive a volunteer's week, and mandatory free text is the
most reliable way to get a form abandoned or filled with "looks fine". **If record volume
disappoints in the pilot, unwind this first.**

---

## 3. What the current UI already gives for free

**VOID against the product path, 2026-09-20 (ticket 10, applied by ticket 20).** This section
is written against the Triage Desk in `index.html`. **That page was withdrawn on 2026-09-20**
and is out of scope, so there is no UI giving anything for free: on the path that ships, every
field is typed into a paste-back block by a human. Two of the rows below also name fields that
no longer exist (`ai.readiness`, `readinessCall.delta`, both deleted by ticket 05).

Kept because the argument it makes -- that a record is only cheap where the interface already
holds the answer -- is the right test to apply to whatever interface comes next. **Do not build
from this table.** As it stood, all of section 3 and section 4.1 read as outstanding work, and
a build session working from them would build the wrong thing.

<details><summary>The original table, for the argument only</summary>

| record field | already in the UI | where |
|---|---|---|
| `ai.findings` | yes | rendered from the review JSON |
| `ai.readiness` | yes | the "AI said" marker |
| `decisions[].action` | yes | the keep / ask / cut buttons |
| `readinessCall.lead` | yes | the readiness picker |
| `readinessCall.delta` | yes | already computed for the warning string |
| `lead.secondsOnTask` | trivial | timestamp on first interaction |

</details>

---

## 4. Three gaps, and the smallest thing that closes each

### 4.1 The desk defaults to total agreement — fix this first

**VOID against the product path, 2026-09-20 (ticket 10, applied by ticket 20).** The desk is
`index.html`, withdrawn and out of scope, so there are no defaults to fix and nothing here is
outstanding work. The second of the two lines below also reads `R.readiness.level`, a field
ticket 05 deleted.

**The failure it names did not go away with the page, and that is why this stays.** On the
chat path the lead types the record by hand, so nothing is pre-set — but nothing forces a
decision either, and a record can still come back endorsing everything by default. The
measurement-side protections are the ones that survive: `cutReason`, the mandatory `reason`,
and `added[]`. Whatever interface comes next, start it undecided.

Two lines set the entire starting state:

- `renderLC` line 602: `if(!triage[i]) triage[i] = 'keep';` — every finding starts **kept**.
- `renderLC` line 603: `if(leadLevel === null) leadLevel = LEVELS.indexOf(R.readiness.level);`
  — the lead's readiness call starts **pre-set to the AI's**.

A lead who opens the desk, reads nothing and clicks Send produces a record identical to one
who studied the deck and genuinely endorsed every word. As a UI default this is friendly. As
a **measurement** default it is fatal: it manufactures agreement and it biases in exactly the
direction that flatters the tool.

The gold protocol went to real trouble to avoid this — labelers worked before seeing AI
output, and declared conflicts. Shipping a pre-agreed desk and calling its output a label
would discard that discipline silently.

**Fix:** start `triage[i]` as `null` and `leadLevel` as `null`. Findings render in an
undecided state, Send stays disabled until every finding has been touched and a readiness
level has been clicked. Record `touched: true` per decision so an untouched record can never
be mistaken for an endorsement. The cost is a handful of lines and one disabled button.

### 4.2 Nothing captures what the AI missed

Keep/ask/cut can only ever describe findings the AI produced. Recall is structurally
invisible. Worse, the omission is silent: nothing on the screen prompts a lead to notice an
absence, so the records will look best exactly when the tool has missed the most.

**ALREADY PRESENT, 2026-09-20.** `added[]` is in the paste-back block of the chat path and
has been since it shipped. This is not outstanding work; do not build it twice. What is still
true is the reason it matters: an empty `added[]` from a lead who was *asked* means
considerably more than one from a lead who was not, and the chat block does ask.

**Fix (as originally written):** one "Add what it missed" affordance writing into `added[]`.
Short text, severity, page number. Even mostly-empty this is the only recall signal the loop can produce, and an
empty `added[]` from a lead who was *asked* means considerably more than one from a lead who
was not.

### 4.3 No must-catch

The gold worksheet forces exactly one `[MUST-CATCH]`: the issue a review that misses it has
failed. It is the backbone of `score-review.js`'s headline metric.

**ALREADY PRESENT, 2026-09-20.** `mustCatch` is in the paste-back block of the chat path.
Not outstanding work. One caveat on the claim that it makes a record scoreable: `mc-match-3`
judged 0 of 9 pairs on both 2026-09 runs, so the matcher it feeds is currently scoring
nothing. The field is right; the instrument behind it is not yet.

**Fix (as originally written):** one radio click across the kept set. Ten seconds, and it is
the field that makes a record scoreable by the existing matcher rather than only readable by
a human.

---

## 5. What an override record is NOT

The claim worth making is that these records are cheap and plentiful. The claim **not** to
make is that they are golds. Field by field against
[worksheet-template.md](eval-cases-real/labeling/worksheet-template.md):

| gold worksheet section | override record | honest verdict |
|---|---|---|
| Expected readiness (level, reason, rules) | `readinessCall` | **partial, downgraded 2026-09-20.** It was rated full match, the only row here with no caveat. Two things undercut that. The record no longer carries an AI side at all (ticket 05), so there is nothing to compare the gold level against except a human's. And the human side is weak: on the four accidentally double-labelled decks, two trained readers reproduced each other's level on **2 of 4**, 95% CI [7%, 93%], weighted agreement below chance (ticket 03). A field both sides of which are this soft is not a full match to anything. |
| Real top issues, ranked | kept findings, in AI severity order | **partial** — a subset of what the AI happened to raise, and the lead never ranks |
| `[MUST-CATCH]` | §4.3 affordance | full match once built |
| Acceptable AI feedback | the kept set | **full match**, and free |
| Unacceptable AI feedback | cuts with `cutReason: wrong` | full match once §2's vocabulary exists |
| False positives to avoid | cuts with `wrong` / `not-an-issue` | full match once built |
| False negatives to catch | `added[]` | **weak** — §4.2, and it is the field most likely to be skipped |
| Honest uncertainty | `ask` decisions | **decent proxy**: converting a finding to a question is a lead saying they cannot settle it from here |
| Conflicts declaration | `lead.ownsTheTeam` | **structurally absent**. The lead is reviewing their own team's work. Gold labelers declared conflicts and were screened; a lead cannot be. |

Three structural differences remain no matter what gets built:

1. **Selection bias.** The record is conditioned on the AI's output. It measures precision
   ("are its flags right?") well and recall ("what did it miss?") barely.
2. **Anchoring.** Even with §4.1 fixed, the lead reads the AI first. That is the product
   working as intended and it is also the opposite of the gold protocol.
3. **No adjudication.** Golds were double-labelled and adjudicated, with an agreement log.
   An override record is one opinion from an interested party.

**Therefore:** override records are a *complementary* instrument, not a substitute. They are
the right tool for calibrating readiness and for killing false positives, and they will
systematically flatter recall. A pilot that reports "the lead agreed with 90% of findings"
without §4.1 is reporting the default state of a form.

The high-value derived use is cheap and safe: **a record where the lead moved readiness two
levels, or cut a finding as `wrong`, is a high-yield candidate for real gold labelling.**
That turns the log into a sampler that points thirty-hour expert attention at the cases where
it pays, rather than a replacement for it.

---

## 6. Storage and confidentiality

An override record embeds finding text and evidence quotes, so **it is client-confidential by
construction** and follows the same rule as everything else in this project: it never enters
the repo.

- Local sink: `tools/quality-reviewer/v2/eval-runs/override-log/`, added to `.gitignore`
  as a whole directory before the first record is written.
- Committed instead: this spec, the schema, and any aggregate that carries no client text
  (counts, deltas, `cutReason` distributions).
- The pilot version can be a single append-only JSONL file. There is no reason to build a
  service.

---

## 7. What Wednesday needs

The live desk already runs on a real review
(build-desk.js (historical sibling-repository tool, not distributed here) `--live`), so the demo shows
the real loop rather than a picture of one.

For the demo itself, in priority order:

1. **§4.1 undecided defaults.** Without it the demo shows a form that agrees with itself, and
   an attentive board member will notice.
2. **`cutReason` on cut.** One dropdown. Converts the whole exercise from a UI into a
   measurement.
3. **Serialize the record and show it.** Print the JSON on Send. The point being made is "this
   is a labelled datapoint", and the most convincing way to make it is to show the datapoint.

§4.2 and §4.3 can wait; they change what the log is worth over a term, not what the demo
shows in a room.

**Deliberately not in this spec:** any change to the prompt, the rubric, or the output
contract. `fid` is derived rather than added for exactly that reason.
