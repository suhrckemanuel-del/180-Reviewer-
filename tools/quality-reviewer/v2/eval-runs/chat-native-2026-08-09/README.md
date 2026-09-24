# Chat-native split test, 2026-08-09

Four runs of the three-paste chat path on `eval-cases/case-04-contradiction-no-implementation.md`,
a **synthetic** case. No real client material is in this directory, which is why it is excepted
from the `eval-runs/*/` ignore rule.

| file | model | blind |
|---|---|---|
| `case04-chat-run.txt` | Opus 5, in the authoring session | **no** — the author of the format ran it, treat as a contaminated control |
| `run-opus-blind.txt` | Opus 5 | yes |
| `run-sonnet-blind.txt` | Sonnet 5 | yes |
| `run-haiku-blind.txt` | Haiku 4.5 | yes |

Blind runs were given exactly three inputs and nothing else: `04-prompt-templates.md` section A,
`CHAT-CONTEXT.md`, and the case file. They were told nothing about what was being measured.

Prompt `frozen-2026-08-09`, sha `2371607aa850b674`. Result in
[27-governing-insight-split.md](../../27-governing-insight-split.md).
