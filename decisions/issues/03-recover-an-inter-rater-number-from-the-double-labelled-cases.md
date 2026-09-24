# Recover a real inter-rater number from the four double-labelled cases

Type: task
Status: resolved
Resolved: 2026-09-19
Blocked by: —

## Question

`STATUS.md` calls this the open wound: the 178-pair label set everything is validated against was
never double-adjudicated, "two independent adjudicators, kappa 0.971" was one opinion copied, and
the real figure is 0.562 — agreement between LLM passes, not correctness.

The audit of 2026-09-18 found something the docs do not mention. The labeling protocol was
deliberately single-pass, but **four cases were labelled twice by different people anyway**:

| case | worksheets |
|---|---|
| real-02 | MF, MS |
| real-08 | MF, MS |
| real-12 | GS, MS |
| real-13 | GS, MS |

That is four independent human pairs of opinions on real deliverables, sitting unused in
`eval-cases-real/labeling/`. It is a small n, and it is the only genuine human inter-rater signal
this project has ever had.

Do:

1. Extract the paired judgments per case — top issues, severities, must-catch.
2. Compute agreement honestly, and state the confidence interval. With n=4 cases the interval will
   be wide; report it rather than hiding it.
3. Say plainly what the number licenses and what it does not.

Answer records: the figure, its interval, the method, and whether it changes any claim currently
made in `18-evidence-base.md` or `22-trust-boundary.md`.

---

## Answer (2026-09-19)

Full analysis: `tools/quality-reviewer/v2/eval-cases-real/_INTER-RATER-RECOVERY.md`
(**local only, gitignored** — it quotes paired human judgments on real client decks).
Reproduction: [ticket-03-irr.py](../ticket-03-irr.py). `labeling/agreement-log.md` untouched;
ticket 02 owns it.

### The figure and its interval

**Readiness, exact level: 2 of 4, 50%, 95% Clopper–Pearson CI [6.8%, 93.2%].**
Cohen's kappa **0.385** unweighted, **0.200** linear-weighted, **−0.053** quadratic-weighted —
below chance once the ordinal distance is respected, which it should be, because one of the
four pairs is three levels apart.

| | agreement | 95% CI |
|---|---|---|
| readiness, exact level | 2/4 = 50% | [6.8%, 93.2%] |
| must-catch, same defect named (strict / lenient) | 1/4 / 2/4 | [0.6%, 80.6%] / [6.8%, 93.2%] |
| restraint call | 2/4 = 50% | [6.8%, 93.2%] |
| top-issue severity | 2/4 = 50% | [6.8%, 93.2%] |

No kappa CI is quoted: the asymptotic SE is invalid at n=4. Leave-one-out is given instead, and
it is brutal — dropping one case moves kappa between 0.143 and 0.571. **One case is worth up to
0.43 of kappa.** The interval on the raw rate spans 7% to 93%: this cannot distinguish good
agreement from none.

MS never committed on real-02 (R1–R2). Both resolutions are reported; the R1 limb gives 1/4,
kappa 0.077.

| case | second reader | MS (gold) | gap |
|---|---|---|---|
| real-02 | MF **R2** | **R1–R2 uncommitted** | 0 or 1 |
| real-08 | MF **R3** | **R0** | **3** |
| real-12 | GS **R1** | **R1** | 0 |
| real-13 | GS **R3** | **R2** | 1 |

### Method, and why the honest label is not "inter-rater reliability"

All four golds are MS's read, so this is one gold author checked against two other readers
(MS vs {MF, MF, GS, GS}), not a two-fixed-rater design — kappa is descriptive here, not a
properly specified coefficient. Three further weaknesses, all in the analysis: the two sides
were produced by **different elicitation processes** (AI-scribed spoken assessment with
dimension mapping vs. a typed paragraph; 3–5 ranked issues vs. one); **GS's blindness is
undeclared and doubtful** — those two worksheets are dated three days after the golds were
written into the directory GS was working in, on two cases that were not on GS's assigned list,
and everything is gitignored so there is no history to check; and the second readers' sheets are
too thin for any ranked-list comparison. Contamination inflates agreement, so **50% is an upper
bound**.

### The one claim the count supports where the rate does not

**In 0 of 4 cases was the second reader stricter than the gold author.** Both clear
disagreements run the same way, and the second reader called restraint on two cases where the
gold called restraint on none. Sign test p = 0.50 (R2 resolution) — not significant and not
claimed as such, but the direction is uniform and the gold author wrote every gold. Consistent
with a gold sitting at the strict end of the plausible human range.

### What it licenses

Converting an anecdote into a quantified unknown; the directional hypothesis above; **an
argument for retiring readiness that does not depend on the model being bad** (A4 says the
reviewer returns R0 and R2 on identical bytes — this says two humans return R3 and R0 on the
same deck, so the construct is weakly determined before any model touches it); and a cost
estimate — 30 double-labelled cases at 80% observed agreement still only yields a lower bound of
0.61, and the corpus is 14 cases. **A defensible inter-rater number on readiness is not reachable
at this corpus size.**

### What it does not license

Any claim of the form "inter-rater reliability is X" — never quote a figure here without its
interval, or the kappa without the leave-one-out spread. It says **nothing** about the 178-pair
problem (LLM adjudications of gold/finding *pairs* for the matcher; this is human judgments on
whole *cases* — different object, and the trust boundary's fourth row still has zero
human-adjudicated matcher labels). It invalidates no A-claim, flips no trust-boundary row, and
yields no correction factor.

### Does it change 18-evidence-base.md or 22-trust-boundary.md?

**Nothing in either becomes false** — neither states an inter-rater figure. Four edits are
recommended, none of them a status change:

1. **`18-evidence-base.md`, open-questions list, "whether the human gold labels generalise beyond
   one labeler."** The one item that changes. It currently carries real-08 as an anecdote; it
   should carry the figure, the interval and the direction, and stay on the not-known list.
2. **`18-evidence-base.md` A1, "blocking rules missed 0%", high confidence.** The claim survives
   as written — it is reviewer-versus-gold and this measures neither. **Its meaning needs a
   qualifier:** 0% of what *one reader* would have blocked. On real-08, the only case in the set
   where the gold fired a blocking rule and a second human read the same deck, **the second human
   did not fire it and called the deck R3.** The blocking-rule construct is not reliably
   reproducible between humans, and that caps what the 0% can mean at any sample size. Do not
   downgrade the confidence level on one case.
3. **`22-trust-boundary.md`, row "Another branch"**, whose bar includes readiness exact-match on
   the nine real cases. **A bar measured against a reference two humans reproduce at 50% is not a
   bar.** Either attach the stated noise floor or drop readiness exact-match as a bar — which is
   what the map's no-readiness-level decision already implies. **This is a decision, not an
   analysis result: routed to ticket 05 and ticket 07.** No row flips MET/NOT MET on n=4.
4. **`22-trust-boundary.md` section 1a** (why the chat path emits no readiness level) is
   *strengthened*: the argument currently rests on A4 alone, so adding the human figure makes the
   non-production decision hold even if the model is later stabilised. One line.

### Found on the way, and worth more than the number

`_LABELING-RECORD.md` records real-02 as *"single-pass gold and the bonus second read agree
exactly on readiness."* MS did not commit; the **owner resolved the straddle to R2 on 2026-07-27
while knowing MF had said R2**. The record is transparent about that sequence in the preceding
clause, so nothing is concealed — but the summary phrasing turns a resolution-made-knowing-the-
answer into an independent concordance. **That is structurally the same error as the kappa-0.971
problem in A8: a number measuring something against a copy of itself.** Second occurrence, second
mechanism, three days apart. The correction is a one-line fix; the pattern is the finding.
