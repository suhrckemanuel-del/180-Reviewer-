# Paste-ready build prompt: `mc-match-3`, the LLM judge (Track B)

**Run on Opus.** This is the gating build for the whole project and it is a measurement
instrument. An instrument that is wrong in a flattering direction is worse than none, and this
project has already shipped one. Do not run it on a fast model.

**Runs in parallel with Track A** (`BUILD-PROMPT-ambiguity-pass.md`). File ownership is at the
bottom. You own `STATUS.md`.

Paste everything below the line into a fresh chat. It is self-contained.

---

Working in `c:\Users\User\Desktop\180dc-ai`, branch `idea/reviewer-v2`. Everything lives under
`tools/quality-reviewer/v2/`. **Build and measure. Write no new strategy documents.**

## What this exists to close

Every other piece of work in this project is queued behind one fact: the scorer does not work.
On 2026-08-05 it was validated against 178 blind-adjudicated gold-issue/finding pairs and
returned **AUC 0.718, 88% accuracy — against 85% for a constant that ignores its input
entirely.** Precision after re-fitting is 46%. The cause is known and is not fixable by
tuning: `mc-match-2` scores vocabulary overlap, and the judgement that matters is whether two
texts describe the same problem. Both adjudicators independently reported the same two failure
shapes — real catches are same-complaint-different-vocabulary, false positives are
same-slides-different-problem.

Your job is `mc-match-3`: replace the overlap heuristic with an LLM judge, and prove it works
or prove it does not.

## Read first, in this order

- `21-scorer-refit-sprint.md` **section 5 in full**. It is the method you are extending and it
  is honest about its own failure. Section 5.2 is the baseline you must beat.
- `score-review.js`, `MATCHER_VERSION` at line 38 and the scoring path below it
- `22-trust-boundary.md` section 1, the fourth row — it names your acceptance bar
- `18-evidence-base.md` A8, and A9 on draw counts
- `eval-runs/real-baseline/threshold-refit/` — the data. `adjudication-set.json` is the 178
  pairs with the question as posed; `adjudication-A.json` and `-B.json` are the two blind
  verdicts; `answer-key.json` carries the current matcher's features and verdict per pair;
  `disagreements.json` is where A and B split.

## The bar, taken from 22 section 1

**AUC ≥ 0.85 and accuracy ≥ 92%** on the 178-pair set. Report both against the 85% constant
baseline every single time, in the same sentence. A number reported without that baseline is
the exact failure this sprint exists to correct.

If you cannot clear the bar, **say so and stop.** A recorded negative result is a good outcome
here — it is what the last sprint produced and it is why this one is well posed. Do not tune
until something passes.

## Four things that will go wrong if you do not plan for them

### 1. Fitting on your own test set

178 pairs is small. If you iterate the judge prompt against all 178 and then report accuracy on
all 178, you have re-run the fiction-fitted-thresholds mistake in a new coat, and the number
will be a fiction again. **Split before you write a single line of the judge prompt.** Stratify
by case and by adjudicator agreement so both halves carry hard pairs. Develop on one half,
touch the other exactly once, report both numbers separately and label which is which.

### 2. Circularity

You are building an LLM judge and validating it against labels produced by LLM adjudicators.
Agreement may mean the judge is right, or it may mean it shares their blind spots. This does
not invalidate the approach — kappa 0.971 between two independent agents is real signal — but
it caps what you may claim. State the limitation in the write-up in one sentence. The 178 pairs
are not ground truth; they are two agents' agreement.

`disagreements.json` is the most informative file in the directory: those are the pairs where
the call is genuinely hard. Report your judge's behaviour on them separately. A judge that
tracks the easy consensus and coin-flips the hard cases can still post a good headline number.

### 3. Determinism

A scorer that returns different numbers on the same input cannot be a measurement instrument —
that is the A4 failure, one level up. Fixed prompt, low temperature, **N draws with a majority
vote**, cached by a hash of the pair so re-scoring never re-calls. Report the rate at which the
N draws disagreed with each other; that number is the honest confidence interval on every score
the project publishes afterwards, and it belongs in the write-up whether it flatters or not.

### 4. Cost and reproducibility

`20-running-it-free.md` governs. The subagent path is the working one; the API path is still
broken by a "compiled grammar is too large" 400. Whatever you build must be re-runnable by
someone with no API key, and the cache must make a re-score free.

## Definition of done

- `mc-match-3` implemented, `MATCHER_VERSION` bumped, old thresholds removed rather than left
  beside it. Scores are not comparable across matcher versions — make that mechanical, not a
  comment.
- A results document, `23-mc-match-3.md`: the split and how it was stratified, dev and held-out
  numbers each against the 85% constant, behaviour on `disagreements.json`, the draw-disagreement
  rate, and the circularity limitation in one plain sentence.
- Verdict stated in the first three lines: **does it clear AUC 0.85 / 92%, yes or no.**
- `node check-docs.js` clean.
- `STATUS.md` updated — the scorer row in the state table, the measurement section, and item 1
  of "What happens next". You own this file; Track A does not touch it.

## What would make this sprint a failure

Reporting a headline accuracy without the constant baseline beside it. Tuning the judge prompt
against the held-out half. Declaring success on the easy pairs while the hard ones coin-flip.
Or quietly re-running the nine real cases because the matcher now looks good — that is step 2
and it is not yours; at 46% precision today nobody could attribute the movement, and the whole
point of this build is to earn the right to attribute it.

## File ownership, because Track A is running at the same time

**Yours:** `score-review.js`, `rescore.js`, `scorecard.js`, `eval-runs/real-baseline/`,
`23-mc-match-3.md`, `STATUS.md`, `11-decision-log.md`.
**Not yours, do not edit:** `04-prompt-templates.md`, `01-rubric-v1.md`, `24-*.md`. Track A owns
those. If you need a prompt change, write it down as a recommendation and leave it.
