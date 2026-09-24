# Decide how the path that ships gets measured

Type: grilling
Status: parked
Blocked by: —

## Question

Surfaced 2026-09-20, after ticket 15, while looking for the next high-value ticket. **The harness
cannot score the product, and no document in this project says so.**

**Zero of the thirty-six reviews on record ran the path the pilot ships.** Every one ran the
harness path: generated packs, JSON response, `check-review-v2.js`. The pilot runs the three-paste
chat path, which returns prose.

That is not merely "untested". It is structural, and it is worse in a specific way:

**`CHAT-CONTEXT.md:400` forbids the chat path from emitting a blocking rule number**, deliberately
and for a good reason — the fence argument, that nothing produced is nothing forwardable. But
`score-review.js:535,587` reads `review.blockingIssues[].rule` to compute `rulesFired` and the
derived readiness level, and ticket 05's whole retirement rests on that derivation. **So the
derived scorer — ticket 05's mechanism, ticket 20's step 4, and the metric family ticket 07 is
building its gate from — cannot read the product at all.** Not "reads it poorly". Cannot.

Against ticket 07's list of the gate's defensible contents, as ticket 05 last amended it:

| gate metric | available on the chat path? |
|---|---|
| contract validity | **partly** — no JSON contract for the prose; the paste-back block is JSON and can be validated |
| fabricated-quote count | **yes** — quote checking is mechanical against the deliverable |
| restraint violations | **yes** — findings are countable |
| blocking rules missed | **no** — not emitted |
| blocking false positives | **no** — not emitted |
| derived readiness: exact, within-one, over-flag, under-flag | **no** — all four need the rule numbers |
| must-catch recall, gold coverage | **no** — no judging pass (ticket 14) |

**Four of the seven rows are structurally unavailable, and they include every metric this project
has argued about for three weeks.** Tickets 01, 15, 16 and 17 are entirely about numbers that
describe a path nobody will use.

### What is genuinely available, and it is more than it first looks

- **Severity is recoverable.** The prose grades findings `High impact | Moderate | Minor`, and
  `03-output-contract.md:118` documents the mapping: critical to High impact, major to Moderate,
  minor to Minor. Better still, the paste-back record at `CHAT-CONTEXT.md:381` carries
  `"severity": "<critical | major | minor>"` in the contract's own vocabulary. **So the severity
  distribution — the metric ticket 15 recommended as the gate's new restraint bar — is measurable
  on the product path.** That is the strongest argument for it and ticket 15 did not have it.
- Findings count against the noise budget, and the quote check, both mechanical.
- The paste-back record is JSON and can be validated as a contract.

### Settle

1. **Does the chat path get scored at all before the pilot, and on what?** Options: score the prose
   directly against the golds; score the returned paste-back record; or run a shadow JSON review on
   the same deck and treat it as a proxy for the prose one. The third is cheapest and is the one to
   be most suspicious of — **it is a measurement of a different artifact presented as a measurement
   of this one**, which is the shape the map's standing caution exists to catch.
2. **If a proxy is used, what would have to be true for it to hold**, stated before it is run. The
   two paths share the system prompt and differ in the output section; ticket 17 already showed
   that a rule the patch never touched changed its firing, so "only the output shape differs"
   is exactly the assumption this project has watched fail once.
3. **Does ticket 07's gate get rewritten** to contain only what the product path can produce? On
   the table today it contains four metrics that cannot be computed for it.
4. **Does the chat path start emitting rule numbers after all?** This is the option that most
   people would reach for and it should be argued explicitly, because it reverses the fence
   decision in `26-chat-native.md` §1a and the widened stop condition 3. The honest case for it:
   the fence argument was about a *readiness level*, and a rule number is not a grade. The honest
   case against: it is exactly the kind of "harmless internal field" that becomes forwardable, and
   ticket 05's whole argument was that non-production beats redaction.

### What this does not do

**It does not invalidate the nine-case baseline work.** Those runs measured the system prompt,
which both paths share, and they caught real defects — the dead severity floor, the loose blocking
rule 1, the constant confidence label. What they do not do is describe the output a pilot user
receives.

### Interactions

- **[Ticket 07](07-set-the-release-gate-for-prompt-changes.md)** cannot set its contents before this
  resolves. Its current list assumes the JSON path.
- **[Ticket 22](22-decide-the-findings-based-severity-score.md)** — if a findings-based score ships,
  it is computed from severities, which *are* available on both paths. That makes 22 and this
  ticket mutually reinforcing rather than competing.
- **[Ticket 20](20-apply-the-accumulated-edit-lists-to-the-product.md)** step 4 builds the derived
  scorer. It should still be built — it is the right instrument for the harness path — but the
  ticket should record that it does not reach the product.

Answer records: whether the product path is scored before the pilot, on what, what the gate contains
once only product-path metrics are allowed, and whether rule numbers start being emitted.


---

**Parked 2026-09-20 by the owner, on the scope audit ([AUDIT-2026-09-20.md](../AUDIT-2026-09-20.md)).** Not cancelled and not out of scope: deferred until the pilot has run, at which point it is reconsidered against what the pilot actually showed.

Reason: the finding is real (the derived scorer cannot read the chat path) but its consequence lands on an eval already off the critical path. The one part that matters is a task, not a decision: read the output this path produces on one real deck.
