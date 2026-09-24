# Bring the artifact path level with the prose path

Type: task
Status: open
Blocked by: 26

## Question

Nothing to decide about *whether* — the owner asked for the HTML output on 2026-09-20, wanting to
see rendered output. This ticket exists because **the artifact path did not receive any of the
2026-09-20 build**, and the gap is wider than "it is a bit behind".

### The gap, measured 2026-09-20

[Ticket 20](20-apply-the-accumulated-edit-lists-to-the-product.md) shipped six things into the
prose path. `TEST-KIT/PASTE-2C-artifact-path.md` received **the deletions only** — `aiLevel`, its
derivation rule, the "AI guess" pill, and the confidence label.

| | prose path | artifact path |
|---|---|---|
| attempt gate | paste 1 + paste 3 | **absent** |
| bundle key, `KEYS:` on line 1 | present | **absent** |
| `ATTEMPT ON RECORD:` on line 2 | present | **absent** |
| `COUNT:` line | present | **absent** |
| `ON YOUR OWN READ` | present | **absent** |
| student-side record fields | present | **absent** |
| readiness level, confidence | removed | removed |

**The gate and the key are not cosmetic omissions.** The gate lives in paste 1 and paste 3, which
the artifact path also uses, so a student on the artifact path *does* meet the gate — but the
artifact template has no line-2 slot for the marker and no first-line slot for the keys, so
**neither the attempt nor a truncation is recorded in the output**. The detectors exist and their
output has nowhere to land. That is worse than absent: it is a check that appears to run.

### The blocker that is not about features

[Ticket 13](13-decide-the-default-output-path.md) already records it: **the artifact path has no
outbound scan, no payload redaction and no stop panel.** The guards at `index.html:1100-1168`
protect the renderer, and the renderer is withdrawn. Under the widened stop condition 3 — *the tool
produces a readiness level, for anyone* — **the artifact path does not ship until it carries an
equivalent check.**

The prose path meets that condition by construction: it produces no level, so there is nothing to
strip. The artifact path is HTML the model writes, so a level can reach the page by any route and
nothing is watching. **Whatever guard this ticket builds has to work without a renderer**, which is
a different problem from the one `index.html` solved, and it is the real work here.

### Blocked by 26 and by 13, for different reasons

- **[Ticket 26](26-rewrite-the-finding-for-a-student-who-has-to-act-tonight.md)** settles the shape
  of a finding. The artifact path *renders* findings. Building 2C against today's shape means
  building it twice, and the second build is the one that matters.
- **[Ticket 13](13-decide-the-default-output-path.md)** settles whether the artifact path is
  reached at all and how. If the answer is that it is retired rather than maintained, this ticket
  does not exist. **Answer 13 first; it is cheaper than this ticket and it can cancel it.**

### Do

Once unblocked:

1. Bring 2C to the settled finding template from 26.
2. Line 1 carries `KEYS:`, line 2 carries `ATTEMPT ON RECORD:`, in the rendered page and in any
   paste-back block, on the same rules the prose path uses. The marker stays **one-sided**
   wherever it is described.
3. The `COUNT:` line, presented as arithmetic over the findings and never as a verdict
   ([ticket 22](22-decide-the-findings-based-severity-score.md)).
4. `ON YOUR OWN READ`, with the same audience branch as the gate — `ATTEMPT_GATE_AUDIENCE` in
   `build-bundle.js`, which is the one place the branch is set. **Do not add a second switch.**
5. The student-side record fields (`student.id`, `attempt`, `bypass`) and `override-log-3`.
6. A no-level guard that works without a renderer. This is the item with no precedent; everything
   above is transcription.
7. 2C joins `build-bundle.js` as a generated artifact, or it drifts exactly as the two derivatives
   before it did. `--check` must cover it.

### Read against the current paste 1 before starting

Ticket 13 records that **2C is two prompt versions stale and nobody has read it against the current
paste 1.** Paste 2 of the prose path was in that state and turned out to contradict paste 1 in two
places, one of which put the wrong prompt version on every record. 2C has had less attention than
paste 2 had. Do that read first and file what it finds, rather than assuming the only gaps are the
ones tabulated above.

Answer records: what landed, what the no-level guard is and how it is tested, whether 2C became a
generated artifact, and what the read against paste 1 turned up.

---

**Input from [ticket 13](13-decide-the-default-output-path.md) (closed 2026-09-20). 13 is no longer
a blocker; 26 still is. This ticket is NOT cancelled, and its shape has changed more than its size.**

**The page is a re-print, not a second reviewer.** It shows the review the prose path already
produced — same findings, same quotes, same words, laid out — and it carries **no content rules of
its own**. `PASTE-2C-artifact-path.md:3` currently opens *"It replaces the JSON output that prompt
asks for"* and then restates every content rule for itself. **That is rejected, and rewriting it is
the largest single piece of work in this ticket — an item this ticket did not have.** Do it first;
the items below depend on it.

**The verdict row is deleted.** No grade box, no confidence box, and **no "Your call — Not set"
box** either. Remove the phrase *"the verdict pills"* at :15 — that phrase is the label on the hole.

### What that does to the Do list

| item | was | now |
|---|---|---|
| 0. rewrite 2C into a re-print | not on the list | **the largest item, and everything below depends on it** |
| 1. settled finding template from 26 | build | unchanged, still blocked on 26 |
| 2. line 1 `KEYS:`, line 2 `ATTEMPT ON RECORD:` | build on this path | **carry through** — already in the review being re-printed |
| 3. `COUNT:` line | build | unchanged |
| 4. `ON YOUR OWN READ`, same audience branch | build | unchanged. Still **one** switch, `ATTEMPT_GATE_AUDIENCE` |
| 5. student-side record fields, `override-log-3` | build | **carry through** |
| 6. a no-level guard with no renderer | *the item with no precedent* | **an absence check on the box row** — a string comparison, not a new instrument |
| 7. 2C joins `build-bundle.js`, `--check` covers it | build | **unchanged and not optional** |

**Item 6 shrinks, it does not vanish.** Deleting the row removes the shape most likely to invite a
grade; the model can still write one into a heading or a sentence. The check is cheap now and it is
still required.

**Item 7 is the whole of ticket 13's question 2, and the owner declined to weigh it** (*"not really
important"*), so it is filed here as spec rather than as a decision he made. The re-print is most of
the drift defence — the page holds no copy of anything — but the layout file itself still sits
outside the generator's three sources and outside every check, which is the exact state the two
stale derivatives were in.

### Two things to test that this ticket did not previously have to

- **The re-print has never been run. Zero measurements.** Both rendered pages on file
  (`proto-04-free-tier-ceiling/render/`) are the second-reviewer design on a pre-retirement
  template. **Ticket 04's "both model families rendered it first try" does not transfer** — it
  measured the design being replaced. Do not quote it for this design.
- **The new failure mode: the model rewriting the review while presenting it as a re-print.**
  Nothing checks that today. It was named as the best case against ticket 13's decision, at the
  time, and it is the **first** thing to test.

The instruction to read 2C against the current paste 1 before starting is unchanged, and becomes
step one of the rewrite rather than a separate pass.

