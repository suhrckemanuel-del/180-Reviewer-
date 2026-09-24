# 27. The governing-insight split, measured across four readers

**Ran 2026-08-09 on prompt `frozen-2026-08-09`, sha `2371607aa850b674`.** Four runs of the
three-paste chat path on the synthetic case `eval-cases/case-04-contradiction-no-implementation.md`.
Runs and method in [eval-runs/chat-native-2026-08-09/](eval-runs/chat-native-2026-08-09/).

## Headline

**The chat-native format holds, and the governing-insight test does not.**

Every run cleared the safety bar that the format exists to guarantee, including on the weakest
model tested. And four readers given identical input split four ways on one instruction — the
same instruction [24-ambiguity-pass-c.md](24-ambiguity-pass-c.md) confirmed as the one real
defect of its four predictions, and patched. **The patch narrowed the ambiguity rather than
closing it**, which is exactly the criticism that produced revision `c`.

## 1. What passed, and it is the important half

| check | authoring run | Opus blind | Sonnet blind | Haiku 4.5 blind |
|---|---|---|---|---|
| readiness level in the review body | none | none | none | none |
| blocking rule number / ceiling / overall score | 0 / 0 / none | 0 / 0 / none | 0 / 0 / none | 0 / 0 / none |
| quotes verbatim against the deck | 9 of 9 | 14 of 14 | 12 of 12 | 5 of 5 |
| findings against a deep budget of 5 | 4 | 5 | 4 | 4 |
| the gold's three top issues | 3 of 3 | 3 of 3 | 3 of 3 | 3 of 3 |
| the gold's two named false positives | neither | neither | neither | neither |
| paste-back record parses, `readinessCall.ai` null | yes | yes | yes | yes |

**Zero fabricated quotes across 40 quotes and four models.** A2 has only ever been established
on Opus 5 in the harness; this is the first evidence that quote-or-abstain survives on a weaker
model, in a format with no validator behind it.

**The non-production control works.** No run had to be trusted to withhold a level, because no
run generated one. The only level strings anywhere in any output are the four option names
inside the paste-back fill instructions, where `CHAT-CONTEXT.md` prints them so the human can
pick their own. That is the template working as designed.

## 2. The split

The prompt's step 4 decides PRESENT or ABSENT by one test: the governing insight is present only
if **one sentence, on its own, both names what the client should do and gives the reason.**

Slide 6 of the case reads, in two sentences:

> Open a retail shopfront within six months and hire three paid repair staff to meet demand.
> This will make Client D self-sustaining.

Four readers, four resolutions:

| reader | call | what it did |
|---|---|---|
| authoring run | **PRESENT**, and the reader reaches it | raised nothing |
| Opus blind | **PRESENT but late** | raised the reader test standalone as finding 5: "The answer to the client's question arrives on slide 6 of 9, and the pages before it are topic labels" |
| Sonnet blind | **ABSENT** | raised it as finding 3: "No single sentence states the recommendation and why it solves self-sustainability", quoting both sentences separately to show the halves are split |
| Haiku blind | not reached | raised no reader-test or insight finding at all |

**The crux is one sentence boundary.** Sentence one names the action and gives a purpose, "to
meet demand". Sentence two gives the reason that answers the client's actual question,
self-sustainability. Whether "to meet demand" satisfies "the reason" decides the call, and the
instruction does not say. Sonnet's evidence makes the mechanism visible: it quotes the two
sentences as separate entries, which is the reading that produces ABSENT.

This is a genuine executability defect, not a disagreement about the deck. All four reviews are
admissible and three of the four are demonstrably correct on everything else.

## 3. Why this was invisible until now

`24-ambiguity-pass-c.md` used two readers on one real case. Two readers can agree by luck. Four
readers on a case whose governing sentence sits exactly on the boundary is what exposed it, and
the case was not chosen for that property — it was chosen because it had a gold and had not been
used for the superseded demonstration.

Recorded so it is not re-learned: **the ambiguity pass should use more than two readers when the
budget allows**, because agreement between two is weak evidence of a closed instruction.

## 4. Not fixed here, and the reason

No patch is proposed in this document. The last two sprints both narrowed this instruction and
both believed they had closed it. A third narrowing written from the same armchair is the
predictable failure. What is now available and was not before is **four resolutions with their
reasoning attached**, which is the raw material for a boundary that can be tested rather than
argued.

Two smaller defects, also left open:

- **Haiku put two separate items on one `Quote:` line**, where the evidence rule requires each
  item its own entry with its own slide number. Both quotes were verbatim, so this is structure,
  not fabrication — but a parser keys on that structure.
- **Sonnet and Haiku dropped the paste-back fill instructions** that Opus reproduced, so their
  records give the human less guidance on completing the record. A compliance divergence on a
  block the template prints in full.

## 5. The method note worth keeping

Predictions made by reading the prompt scored **1 of 3** here, after **1 of 4** in the ambiguity
pass. Twice now, at the same rate. Reading a prompt to predict how it will behave is a coin flip;
running it finds different defects than the ones anyone expected.

Separately, the scoring script written for this sprint was **wrong three times** before it was
right: it miscounted Haiku's findings by sweeping up a numbered questions block, flagged two
false positives in Sonnet that were a quoted procedure and a JSON field name, and reported a
readiness leak in Opus that was the template's own fill instruction. Every error was caught by
reading the actual output. **The measuring instrument was wrong more often than the thing being
measured**, which is the third time this project has learned that lesson.
