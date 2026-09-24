# Ticket 05: deriving the readiness level from the blocking issues

Local only. Reproduction: [ticket-05-derive.js](ticket-05-derive.js), run from
`tools/quality-reviewer/v2/eval-runs/real-baseline/`:

```
node ../../../../.scratch/deliverable-reviewer/ticket-05-derive.js \
  2026-07-29T16-29-44-subagent-packs \
  2026-08-02T20-40-19-subagent-packs \
  2026-09-18T22-00-30-subagent-packs
```

## The question

Ticket 05 retires the readiness level as something the tool produces. The owner also chose to keep
it as an eval metric. Those two answers collide: the harness scores gold against *predicted*, and
predicted came from the model's output.

They only reconcile if the harness can work the level out for itself. `PASTE-1-system-prompt.txt:167`
says it can: **"Readiness is the lowest ceiling among the blocking issues that fired."** The level is
defined as arithmetic over a field the review reports separately and which has to survive anyway,
because A1 (blocking rules missed) depends on it.

So: does the model actually obey its own rule?

## The result

```
2026-07-29T16-29-44  9/9   no-blocker cases: 0
2026-08-02T20-40-19  8/9   no-blocker cases: 1
    real-13: derived R3, emitted R2 (no blocking rule fired — discretionary branch)
2026-09-18T22-00-30  9/9   no-blocker cases: 0

total 26/27
```

Three prompt versions — `frozen-2026-07-26`, `frozen-2026-08-03`, `frozen-2026-08-09` — and
twenty-seven reviews. **The derived level reproduces the emitted level on twenty-six.**

## The one miss is the whole limit of the method

The rule at :167 is arithmetic only when a rule fires. Lines :169-181 hand the model discretion when
none does: default to Nearly ready, demote to Needs targeted revision if it can name a decision the
client would make differently. The harness cannot reproduce a judgment call.

real-13 under `frozen-2026-08-03` is the only review in twenty-seven where no blocking rule fired.
The model demoted, the arithmetic would not have, and **the model was right** — gold on real-13 is
R2, and real-13 is a holdout.

So the honest statement of the limit, which belongs anywhere the derived number is reported:

> The derived readiness level is void on any deck where no blocking rule fires. On the one such case
> observed, the model's discretion beat the arithmetic. The detector gets blinder as the decks get
> better.

At today's calibration that is a narrow blind spot — one case in twenty-seven, and zero in the
current baseline, where a rule fired on 9 of 9. It widens if the tool ever stops over-firing, which
is the direction ticket 16 is deliberately pushing it. Re-measure this after ticket 17.

## This is not a new instrument

Ticket 16's pre-registered prediction — readiness exact 33.3%, within-one 100%, over-flag 44.4%
after blocking rule 1 is tightened — was computed by exactly this arithmetic on the recorded blocking
issues of the 09-18 run. The project has already staked its only falsifiable prediction on the
derivation. This measurement just names the method and puts an error rate on it.

## Side effect worth carrying

Ticket 16 found that over-flag rate and blocking-false-positive rate are the same six cases. Under
the derived scorer both are computed from `blockingIssues`, which makes the duplication structural
rather than coincidental. They must stop being printed as two rows that corroborate each other.
