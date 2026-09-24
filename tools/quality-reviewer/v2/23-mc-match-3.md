# 23. mc-match-3: the matcher as an LLM judge

**Ran 2026-08-08. Method, split and decision rules were fixed before any result was seen.**

## Verdict

**Yes. On the held-out half it clears both bars: AUC 0.979 against a bar of 0.850, and accuracy
93.8% against a bar of 92%, next to 84.0% for a constant that ignores its input entirely.** The
same result holds against all three available label sets, and three of the four stability cases
now return a stable must-catch verdict where two of four did before.

**And the validation set is not what the project believed it was.** The 178 labels were
described everywhere as two independent adjudicators agreeing at kappa 0.971. 176 of the 178
free-text rationales in `adjudication-A.json` and `adjudication-B.json` are identical to the
byte. An independent re-adjudication run this sprint puts the real inter-rater number at kappa
**0.562**, not 0.971.

**So the bar is cleared and the trust-boundary row it gates still should not be signed off.**
Section 7 says exactly what would close it, and it is not a better AUC.

---

## 1. What was built

`mc-match-3.js`. The verdict is no longer a cut point on a text-overlap score; it is an LLM
judge answering one question per pair:

> Imagine a project lead who reads only the AI finding and never sees the gold issue. Would the
> problem the gold issue names actually get dealt with?

`yes` becomes `hit`, `partial` becomes `near` and is still not counted in recall, `no` becomes
`miss`. The full prompt is in `mc-match-3.js` and is hashed; its digest `1267e21848d1b620` is
stamped on every cached verdict and on every score file the matcher produces.

**Determinism is manufactured and then measured**, because a scorer that returns different
numbers on the same input is the A4 failure one level up:

| | |
|---|---|
| prompt | frozen, hashed, one version only |
| draws per pair | 3, majority vote, **ties resolved down** |
| cache key | `sha256(prompt digest, role, draw index, pair text)` |
| re-scoring cost | zero calls, zero key, works offline |
| draw disagreement | **measured and reported, section 5** |

A pair with no cached verdict returns **`unscored`, never `miss`**. That distinction is
load-bearing: `miss` is a value, and inventing it for pairs nobody has looked at would silently
depress recall in the flattering direction. `unscored` also ranks *above* `miss` when picking
the best candidate for a gold issue, so an unmeasured pair can never be reported as a clean
negative.

### One prior, declared

The judge prompt names two failure shapes and tells the judge to watch for them:
same-problem-different-words is a `yes`, same-slides-different-problem is a `no`. Those came
from [21-scorer-refit-sprint.md](21-scorer-refit-sprint.md) section 5.5, where both
adjudicators reported them independently. That is an aggregate observation from a published
document, not per-pair knowledge of the answer key, and it is recorded here so the reader can
discount it as they see fit.

**The judge prompt was written once and never revised against a result.** There was no second
version. Whatever else is true, nothing here was tuned toward the answer.

## 2. The split

178 pairs is small. Iterating a prompt against all 178 and then reporting accuracy on all 178
is the fiction-fitted-thresholds mistake in a new coat, so the split was built before the
prompt was written.

**89 dev, 89 held-out, 28 strata**, stratified on three axes at once:

| axis | why |
|---|---|
| case | real-01, real-03, real-04, real-13 all appear in both halves in proportion |
| label | `yes` is only 25 pairs in the whole set; it splits 12/13 |
| mc-match-2 score band | the ambiguous 0.24–0.39 band, where the old matcher coin-flipped, splits 38/36 |

Assignment is a pure function of the pair id (`sha256(id + salt)`, alternating within each
stratum, parity flipped per stratum so odd remainders do not all land in dev). Nothing is
stored; `node mc-match-3.js --split` reproduces it from the code alone.

**The method note asked for stratification by adjudicator agreement. That was not possible and
the reason turned out to matter** — see section 6. There are only 2 disagreements in the entire
set, and they are 2 because the two adjudication files are near-copies of each other.

## 3. The result

Both bars in [22-trust-boundary.md](22-trust-boundary.md) section 1, on labels A, the historical
target. Accuracy is the binary `yes` versus `no` task with `partial` excluded, defined to match
21 section 5.2 exactly so the numbers are comparable.

| | dev (89) | **held-out (89)** | all 178 |
|---|---|---|---|
| AUC, `yes` vs rest | 0.991 | **0.979** | 0.985 |
| accuracy | 96.3% on n=80 | **93.8% on n=81** | 95.0% on n=161 |
| the constant that ignores its input | 85.0% | **84.0%** | 84.5% |
| lift over the constant | +11.3 pts | **+9.9 pts** | +10.6 pts |
| precision / recall | 90.9% / 83.3% | **83.3% / 76.9%** | 87.0% / 80.0% |
| bar: AUC ≥ 0.850, accuracy ≥ 92% | PASS | **PASS** | PASS |

Dev and held-out are within 2.5 points of each other on accuracy and 0.012 on AUC, which is what
you would expect from a prompt that was never iterated against either.

### Against the instrument it replaces, on the identical pairs and split

| held-out half | mc-match-2, as deployed | **mc-match-3** |
|---|---|---|
| AUC | 0.704 | **0.979** |
| accuracy | 84.0% | **93.8%** |
| constant baseline | 84.0% | 84.0% |
| **lift over the constant** | **0.0 points** | **+9.9 points** |
| precision | 50.0% | **83.3%** |

**Read the mc-match-2 column again.** 21 section 5.2 reported 88% accuracy against an 85%
constant, and that was `textScore` **at its single best possible cut point anywhere on the
range** — a number the deployed matcher never achieved. At the thresholds actually shipped on
2026-08-05, fitted by F1 rather than accuracy, mc-match-2 scores **83.2% across all 178 against
an 84.5% constant: it is fractionally worse than having no model at all**, and exactly level
with it on the held-out half.

That is a harsher statement about the old instrument than the sprint that fitted it made, it
was not visible without this split, and it is the cleanest available answer to why the
measurement programme has been slow.

### The pre-registered criterion from 21 section 4

That sprint fixed the bar in advance: **the stability runs stop flipping.** A matcher that
improves F1 while leaving the coin toss in place has optimised the wrong thing.

| case | mc-match-1 | mc-match-2 | **mc-match-3** |
|---|---|---|---|
| real-01 | miss, near, miss | near, hit, near | **hit, hit, hit** |
| real-03 | miss, miss, near | near, miss, near | **near, near, near** |
| real-04 | hit, hit, hit | hit, hit, hit | **hit, hit, hit** |
| real-13 | miss, near, near | near, near, near | hit, hit, **near** |
| **stable cases** | **1 of 4** | **2 of 4** | **3 of 4** |

real-13 still flips, on a case where two draws say `hit` and one says `near`.

**This is a consequence, not independent evidence.** The 178 pairs were drawn from these twelve
runs, so these verdicts are the same judge calls reported in the table above, viewed downstream.
It is reported because section 4 of the previous sprint demanded it, not as a second result.

**Coverage, stated because it qualifies the row above:** 178 of the 282 gold-issue/finding pairs
in those twelve runs were ever judged, so **15 gold issues across the 12 run-cases come back
`unscored`**. No must-catch verdict is among them. Scoring anything outside these twelve runs —
the 07-29 baseline, the 08-02 calibration runs, the nine real cases — requires judging those
pairs first and will otherwise return `unscored`, loudly, by design.

## 4. Robustness to the choice of labels

The judge was scored against three different label sets on the same held-out half. If the result
depended on which one, it would be an artifact.

| held-out half, labels | AUC | accuracy | constant | verdict |
|---|---|---|---|---|
| **A** (the historical target) | 0.979 | 93.8% on n=81 | 84.0% | PASS |
| **C** (this sprint's independent re-adjudication) | 0.990 | 93.4% on n=61 | 82.0% | PASS |
| **consensus of A and C**, resolved down on a split | 0.992 | 96.2% on n=79 | 87.3% | PASS |

It does not depend on the choice.

## 5. Draw disagreement, which is the error bar on everything downstream

| | |
|---|---|
| pairs with 3 draws | 178 |
| **draws not unanimous** | **21, or 11.8%** |
| mean confidence spread across draws | 6.3 points of 100 |
| byte-identical prose across draws | **0 of 178** |

By label:

| label | draws split | rate |
|---|---|---|
| `no` | 13 of 136 | 9.6% |
| `partial` | 3 of 17 | 17.6% |
| **`yes`** | **5 of 25** | **20.0%** |

**One pair in five that the labels call a catch gets a split vote from the judge.** That is the
honest confidence interval on every recall number this matcher produces from here, and it should
be quoted with them. It is much better than the coin toss it replaces — mc-match-2 flipped
must-catch verdicts on hundredths of a score — but "much better" is not "settled", and a
single-draw run of this judge is not a measurement.

The zero identical rationales across draws is the check that the three draws are genuinely three
draws. It is the same test that caught the defect in section 6, and it is wired into
`--validate` so it cannot go unnoticed a second time.

## 6. The validation set is one opinion recorded twice

This was found while reading the input data, before anything was built on it.

`21-scorer-refit-sprint.md` section 5.1, `18-evidence-base.md` A8 and `STATUS.md` all rest on
one claim: two agents, fresh context each, blind to each other, agreed on 176 of 178 pairs at
**Cohen's kappa 0.971**, and section 5.7 argued that this is what makes the set trustworthy
because "a corrupted A would have shown up as disagreement".

**Cohen's kappa cannot detect a copy.** Two files that are the same file agree perfectly, and
perfect agreement reads as the strongest evidence available. Kappa was measured; independence
was assumed.

`check-adjudication-independence.js` tests the thing kappa cannot. It ignores the verdicts,
which are drawn from three labels and coincide often by chance, and compares the free-text
`why` field, a sentence of open prose per pair:

```
  same verdict            176/178   98.9%
  BYTE-IDENTICAL prose    176/178   98.9%   <-- the test
  pair order identical    true
```

Two agents writing independently do not produce the same sentence 176 times. The two files share
an origin. The 2 rows that differ carry genuinely different prose, so the likeliest mechanism is
that one file was rebuilt from the other with two verdicts re-decided — which is consistent with
the incident recorded in 21 section 5.7, where one adjudicator reported losing its working files
mid-task and rebuilding its output.

**Isolation was instructed and never enforced.** Both adjudicators wrote into the same directory
and could read each other's output. The design assumed a blindness the filesystem did not
provide.

### What the number should have been

A third adjudication was run this sprint on all 178 pairs: fresh agents, the **original**
question verbatim, one pack each, told explicitly why isolation was the entire point of their
run.

| A against an independent C | |
|---|---|
| pairs in both | 178 |
| raw agreement | **78.1%** |
| **Cohen's kappa** | **0.562** — moderate, not "near complete" |
| byte-identical prose | **0 of 178** — C is genuinely independent |

Confusion, rows A, columns C:

| | no | partial | yes |
|---|---|---|---|
| **no** | 104 | **32** | 0 |
| **partial** | 1 | 13 | 3 |
| **yes** | 1 | 2 | 22 |

**Almost the entire disagreement is one cell.** A called 32 pairs `no` that C called `partial`;
the two raters draw the `partial` boundary in different places, and C is markedly more generous
with it (47 partials against A's 17). On everything else they are nearly identical.

**On the `yes` versus `no` line — the only line the matcher is actually fitted to — they agree
126 of 127, 99.2%.** That is why the section 3 result survives the correction, and why the
`partial`/`near` band should be treated as the soft, rater-dependent thing it is.

### What this costs

- **kappa 0.971 must not be quoted again.** It is in three tracked documents; A8 is corrected,
  and `check-adjudication-independence.js` exits 1 so the claim cannot be re-derived quietly.
- **The `mc-match-3` versus `mc-match-2` comparison is unaffected.** Both were scored on the same
  pairs against the same labels, so whatever bias the labels carry, both inherit it equally. The
  relative claim is the robust one.
- **The absolute claim is weaker than the numbers look**, and section 7 says what would fix it.
- **Any future adjudication round is isolated by construction**, not by instruction. The pack
  emitter writes one pack per agent into a directory containing no labels, and `--validate` runs
  the prose test on every set of draws it reports.

### Behaviour on the pairs where the adjudicators split

| pair | A | B | judge (3 draws) |
|---|---|---|---|
| real-01-c-g2-f3 | partial | no | `no`, unanimous, confidence 12 |
| real-13-a-g3-f1 | no | partial | `partial`, unanimous, confidence 47 |

The method note asked for this and it settles nothing: **n = 2 carries no statistical
information**, and it is 2 only because the two files were near-copies. The 32-pair A/C
disagreement cell in the table above is the real population of hard pairs, and it is worth
reading what the judge does there: of those 32, it calls **16 `partial`, 15 `no` and 1 `yes`**.
It splits almost down the middle between the two raters rather than tracking either, which is
the correct behaviour on pairs where two competent raters genuinely disagree, and it is also a
reminder that `near` is the soft band and should never be quoted as a catch.

## 7. The limitation, plainly

**These labels are LLM adjudications, not ground truth, so what section 3 measures is agreement
between two LLM passes over the same question rather than correctness.**

Three things follow, in the order they bite:

1. **No human has checked a single one of the 178 pairs.** Not one. The judge, adjudicator A and
   adjudicator C are all the same model family, so shared blind spots would present as exactly
   the agreement reported above.
2. **The bar in 22 section 1 was written assuming a double-adjudicated set.** It is now known
   there never was one. The numbers clear the bar as written; the premise the bar was written
   under was false, so **the fourth row of the trust boundary — another branch getting the tool
   — should not be signed off on this evidence.** That is a call for the owner, not for this
   document, and it is the reason this sprint reports a pass and still recommends against
   acting on it.
3. **What would actually close it** is a human-adjudicated sample, not a better AUC. A
   stratified 40-pair sample, weighted toward the 32-pair A/C disagreement cell and the 21 pairs
   where the judge's draws split, is roughly an hour of an ex-consultant's time and it is the
   only thing here that would convert agreement into evidence. Cross-model adjudication is the
   cheaper half-measure and is worth running first.

## 8. What changed in the code

| file | change |
|---|---|
| `score-review.js` | `MATCHER_VERSION` → `mc-match-3`. **`T_HIT` and `T_NEAR` deleted**, not left beside the new path. Verdict comes from the judge; `textScore` and the three support signals survive as reported diagnostics that decide nothing. New `unscored` verdict, ranked above `miss`. |
| `mc-match-3.js` | new. Judge prompt, split, pack emitter, ingest, cache, validation, `--selfcheck`. |
| `check-adjudication-independence.js` | new. Exits 1 on the current data. |
| `scorecard.js` | **refuses to aggregate** a run whose score files mix matcher versions, or whose version is not the current one. Points at `rescore.js`. |
| `check-docs.js` | ground truth is now "the matcher has no cut points"; any present-tense mention of `T_HIT` or `T_NEAR` in a tracked document is drift. |
| `18-evidence-base.md` | A8 marked superseded; **A8d** added with the result and the label defect. |

`node mc-match-3.js --selfcheck` rebuilds all 178 pairs from their source golds and reviews and
checks the canonical text matches byte for byte. Without it, one character of drift in the pair
shape would make every cache lookup miss and quietly degrade the matcher to `unscored`
everywhere. It passes: 178 of 178.

## 9. Reproducing it

`20-running-it-free.md` governs. There is no API key anywhere in this path, and the API route is
still broken by the compiled-grammar 400.

```
node mc-match-3.js --split                    # the split, from code alone
node mc-match-3.js --selfcheck                # pair shapes still line up
node mc-match-3.js --validate                 # the section 3 table, from cache, offline
node mc-match-3.js --validate --labels C      # section 4
node check-adjudication-independence.js       # section 6, exits 1
```

Only `--emit` plus a subagent per pack costs anything, and only for pairs not already cached.
534 judge verdicts and 178 adjudications are cached; re-running the numbers above is free.

**Confidentiality.** Pairs quote real client deliverables verbatim. Everything this sprint
produced lives under `eval-runs/real-baseline/mc-match-3/`, inside the gitignored tree, verified
with `git check-ignore`. Subagents were instructed to write only there and to put no client text
in their reports. This document carries method and numbers only.
