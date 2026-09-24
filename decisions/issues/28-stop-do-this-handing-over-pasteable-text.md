# Stop `Do this:` handing the team pasteable text

Type: grilling
Status: open
Blocked by: —

## Question

Surfaced 2026-09-24 by [ticket 26](26-rewrite-the-finding-for-a-student-who-has-to-act-tonight.md),
which found it while measuring something else and **did not fix it**.

`Do this:` is restricted to *"the move, not the words"* and has never carried an exception. It
hands over finished text anyway.

**Under the worked-example amendment** (now withdrawn), three full sentences in six arms:

> *Drop "conservative." Say "The 8% assumption is unproven and the main thing to test."*
> *Clarify in one phrase: "1,400 people on its mailing list, of which 32% attended at least one
> event in 2024 (so ~450 active attendees per box-office data)."*

The second is built entirely from the team's own figures and needs no evidence they do not already
have. It is pasteable as-is.

**After the amendment was withdrawn and the field explicitly hardened** -- "never a sentence the
team could paste, with or without an e.g. or Example: in front of it, and never one built from
their own figures" -- it still happens, milder:

> *(e.g. "this is about the size of Project Grant X from 2024")*
> *(e.g. "from past attendees and campaign sign-ups")*

Three across two arms, **Haiku only; Codex produced none in four arms.**

### Why this matters more than it looks

This is the **"no drafting"** rule failing in the field nobody was watching. The original objection
to AI-drafted fixes was that *"the human must visibly edit"* is unenforceable because a cosmetic
edit is undetectable. **Text that arrives finished needs no edit at all.** Ticket 26 withdrew the
worked example partly on this evidence and then found the leak survives the withdrawal, so the
amendment aggravated the defect rather than causing it.

### Settle

1. **Is a short illustrative phrase in parentheses actually a violation**, or is it the field doing
   its job? *"(e.g. 'from past attendees and campaign sign-ups')"* is five words the student could
   paste, and it is also the clearest way to say what kind of answer is wanted. The rule currently
   forbids it and the model does it anyway on one family.
2. **Whether a prose prohibition can work at all here.** Ticket 26 spent three templates learning
   that a rule the model must apply to its own output is unreliable across families. This is the
   same shape of rule.
3. Whether the hardening added by ticket 26 should stay, be strengthened, or come out as
   ineffective text that costs tokens.

### Do not

- **Do not reopen the worked example.** It is withdrawn, the reasoning is in
  [parked-features.md](../parked-features.md), and this ticket is about a defect that outlives it.
- **Do not fix it by restating the rule.** It is stated twice already and overshot on one family.

### Evidence

[ticket-26/RESULTS.md](../ticket-26/RESULTS.md), the `Do this:` sections. Runs are in
`ticket-26/runs*/`, local only.
