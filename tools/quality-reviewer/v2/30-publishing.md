# Publishing a release of the reviewer

> **Landed in the product tree 2026-09-20 by
> [ticket 20](../../../.scratch/deliverable-reviewer/issues/20-apply-the-accumulated-edit-lists-to-the-product.md).**
> Written as `ticket-09/PUBLISHING.md` and moved here because it is a deliverable, not a working
> note. Paths below are relative to the repository root unless they are links.


**The whole job is one command and about ten minutes.** It is written out at this length because
the person doing it may never have done it before and there may be nobody to ask.

Two channels, decided 2026-09-20: **Google Drive is the student path, GitHub is the lead and board
path.** They are not maintained separately. Both carry the same generated file.

---

## 0. The shape of it

```
tools/quality-reviewer/v2/
  04-prompt-templates.md  sec.A  <- SOURCE, hand-edited (the system prompt, paste 1)
  CHAT-CONTEXT.md                <- SOURCE, hand-edited (the context pack, paste 2)
  04-prompt-templates.md  sec.B  <- SOURCE, hand-edited (the team input template, paste 3)
  build-bundle.js                <- the only thing allowed to produce a pasteable file
  TEST-KIT/
    PASTE-1-system-prompt.txt    <- GENERATED (--sync-test-kit), test keys, not for use
    PASTE-2A-chat-path.md        <- GENERATED
    PASTE-3-team-input-template.txt <- GENERATED
  releases/
    REGISTER.md                  <- key -> date -> prompt version -> gate audience -> what changed
    <key1>/
      REVIEWER-SETUP.txt         <- generated; this is what a person pastes
      COVER-SHEET.md             <- generated; the one page a student reads first
      TEAM-INPUT-TEMPLATE.txt    <- generated
      MANIFEST.json              <- generated; keys, byte counts, sha256, source versions
```

**The three sources carry `<<...>>` placeholders** for the two bundle keys, the Drive folder link
and the attempt gate's audience clause. They are not pasteable as they stand, and that is
deliberate: pasting a source rather than a release ships the placeholders and breaks the key check.
`build-bundle.js` refuses to generate anything with a placeholder left unsubstituted.

**Before the first release, one thing must be set by hand:** `DRIVE_FOLDER_URL` in
`build-bundle.js`. It is `null` today and `--release` refuses while it is. The link goes inside
every bundle, in the message a student sees when their paste was cut, so it cannot be added
afterwards to copies already in people's hands. Create the folder first (section 3), then set it,
then release.

**Nothing under `releases/` is ever hand-edited.** If it is wrong, fix the source and rebuild. A
check (section 5) fails the build if a generated file and its sources disagree, because that exact
failure has already happened twice: `TEST-KIT/PASTE-SETUP-combined.md` sat three months stale
carrying a superseded prompt, and paste 2 drifted from its own source independently.

## 1. Generate

```bash
node tools/quality-reviewer/v2/build-bundle.js --release
```

It mints a fresh key pair, writes the release folder, and appends a row to `REGISTER.md`.

**The key format is fixed and was tested, not chosen.**

- **Part 1: `MMDD-XXXXXXX`** — the release date, a hyphen, and a random alphanumeric chunk
  (`0919-SIGMA7K`). The alphabet excludes `I`, `O`, `0` and `1`: these are copied by hand and
  compared by eye. The date is a convenience for a lead reading an old record. It is **not**
  authoritative: `REGISTER.md` is, and the key is a lookup token into it. The register carries the
  year; the key does not, deliberately, because it is copied by hand and compared by eye.
- **Part 2: a meaningless chunk** (`DELTA-3Q`). It stays meaningless. It is an end-of-bundle canary
  and there is no reason to make it readable.
- **Both parts change every release.** One release, one pair. That is what makes the pair the
  release's identity.
- **Never reuse a key, and never edit a released bundle in place.** A bundle whose contents changed
  under a key that already exists destroys the only thing the key is for. Rebuild and re-publish.

> **Why a date-shaped key is safe.** The whole check rests on the model *copying* a code rather
> than guessing one, and a code that looks like a date is the kind of thing a model can reconstruct
> from context. That was the objection, and it was run rather than argued: 11 runs of the readable
> variant against complete and truncated bundles, **0 inventions, 0 date drift** even though the
> run date was one day after the date in the key. `proto-12-selfcheck/RESULTS-B3.md`, and read its
> limits section before quoting it.

## 2. Publish to GitHub

Commit the release folder. That is the whole step. Leads and the board work from the repo; the
chapter's judgement is that every team lead can use one.

## 3. Publish to Google Drive

**One fixed folder, shared "anyone with the link — viewer".** Its link is printed inside the bundle
itself, in the message the reviewer shows when it detects a truncated paste, so a student who
needs it most is the one being handed it. That has consequences:

- **The folder link must never change.** Not a new folder per release, not a tidy-up that recreates
  it. If it ever must change, the bundle is rebuilt and every issued copy is stale.
- **Link to the folder, never to a file.** Replacing a file in Drive can mint a new file ID and
  break a link already baked into bundles in the wild. Use *Manage versions → upload new version*
  on the existing file so the ID survives, or let people find the current file in the folder.
- **Keep one release visible.** Move the previous release into an `archive/` subfolder rather than
  deleting it — a student mid-engagement may be holding it, and the register needs it to stay
  resolvable.

**The setup goes in as a Google Doc, not a `.txt`.** A student has to select and copy ~42,000
characters in one go, and Drive's text preview makes that awkward, especially on a phone. A Doc is
`Ctrl+A`, `Ctrl+C`.

**And a Doc is exactly where silent corruption gets in** — smart quotes, autocorrected dashes, a
stray paste of formatting. So the publish is not finished until section 4 passes.

## 4. Verify the Drive copy — do not skip this

1. Open the Doc, select all, copy.
2. Paste into a file and run:

```bash
node tools/quality-reviewer/v2/build-bundle.js --verify-drive <that file> --release 0919-SIGMA7K
```

3. It must print `IDENTICAL`. Anything else means the Doc is not the bundle, and the fix is to
   re-paste the Doc from the generated file, not to edit the Doc.

**This is the step that makes "the two cannot drift" true rather than intended.** Everything else
is a promise; this is a check.

## 5. What the build check enforces

`build-bundle.js --check` runs in `check-docs.js` alongside the existing checks, and fails if:

- a `releases/*` file is not byte-identical to a fresh generate from the sources it records
- a key appears in a release folder but not in `REGISTER.md`, or appears twice
- the key printed on `COVER-SHEET.md` differs from the key embedded in `REVIEWER-SETUP.txt`
- `TEST-KIT/PASTE-SETUP-combined.md` exists as a hand-maintained file (it must be a generated
  artifact or gone)

## 6. The cover sheet

One page. A student reads it before pasting anything. It says, in this order:

1. **Paste this whole document as one message. Then paste your deck. Then type your own read of it.**
2. **The first line of your review must read exactly:**
   `REVIEW OF: … | MODE: … | KEYS: 0919-SIGMA7K/DELTA-3Q`
   **Anything else means part of the setup did not arrive. Start a new chat and paste it again.**
   It is a one-paste fix, not a broken tool.
3. Where to get a fresh copy: the Drive folder link.
4. What the tool does not do: it does not approve anything, and it does not give a grade.

**The wording of item 2 is load-bearing.** It is *"exactly this string"*, never *"look for the word
MISSING"* — models have written `<missing>`, `part 2 missing` and `part 2 not provided` instead of
`MISSING`, and a student told to look for one word would pass all three.

## 7. When a record comes back

Every review carries its key. The rule for what to do with it:

| what line 1 says | what it means | what happens to the record |
|---|---|---|
| the **current** key pair | a clean run on the current bundle | admissible for everything |
| a **retired** key pair, in the register | a clean run on an older bundle | **kept and flagged, never dropped.** Valid evidence about the version that produced it; inadmissible as evidence about the current one |
| a key **not in the register** | the bundle was hand-edited, or the key was mistyped | quarantine. Do not pool it; find out which |
| `MISSING` in either half | the paste was truncated; no review was produced, or one was produced that should not have been | **not a review record.** Count it in the truncation rate instead |
| **no KEYS field at all** | a bundle from before this shipped, or a cut deep enough to take the demand line | quarantine |

**Two consequences worth stating plainly.**

**Comparisons are always within a key, never across.** Whatever the release gate becomes — that
decision is still open — a record stamped with a retired key cannot be evidence about the current
prompt. Partitioning by key is what makes the gate mean anything at all.

**The truncation row gives the pilot a number the chapter deferred.** Counting `MISSING` events
against total runs is a live, free measurement of how often real windows actually cut — the thing
nobody has yet measured on a real account. It is a floor, not a rate: it counts the cuts the
interlock catches, not the ones that take the demand line too.

## 8. Who does this

**There is no seat for it today, and that is a known gap rather than an oversight.** The chapter is
recruiting an AI role in roughly five months to take it over. Until then whoever holds the repo
publishes — Manuel, in practice.

The requirement that replaces a name is **transferability**: this document plus
[29-handover.md](29-handover.md) must be enough for someone who was not here. If you publish a release
and something in here was wrong, misleading, or missing, fix it in the same commit. That is the
only maintenance this document gets.
