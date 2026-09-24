# The re-audit prompt

Hand this to a fresh session. It re-audits the reviewer against the realigned goal rather than
against the old map. Paste everything below the line.

---

Read `.scratch/deliverable-reviewer/REALIGNMENT-2026-09-24.md` first. It is the current instrument;
the wayfinder map is frozen and is history, not a to-do list.

**The goal you are auditing against, and nothing else:**

> A reviewer that prompts a student to think better and does not do the work for them. A student
> finishes with work they have confidence in, grounded in evidence they went and found. Not a final
> truth — a defensible choice.

**Audit the shipped bundle against that goal.** The bundle is whatever `build-bundle.js` generates:
`04-prompt-templates.md` sections A and B, plus `CHAT-CONTEXT.md`. Nothing else ships, so nothing
else counts as the product.

Answer these five questions with evidence from the files, not from the documentation about the
files:

1. **Where does the output tell the student the answer instead of making them find it?** Quote the
   lines. The `Do this:` field is the known offender — it has produced finished, pasteable sentences
   built from the team's own figures. Look for others.

2. **What does a student learn that they can name and reuse?** A finding they can act on once is
   worth less than a principle they carry to the next deck. Check whether the principle library and
   the principle tag are actually reaching the output, and whether the words used are ones a student
   could repeat to a team lead.

3. **What in the prompt has no basis in anything?** Some of it is grounded in `10-source-register.md`;
   some was invented in a design conversation and never checked. The nine lenses and the comparator
   test are the known cases — the evidence base labels the comparator *"the leading hypothesis, not
   a result"*. Find the rest. Report what is asserted without support, do not delete it.

4. **What does the tool refuse to do, and is each refusal still earned?** No grade, no readiness
   level, no drafting. Each was decided against real evidence. State for each whether the evidence
   still holds or whether it is now habit.

5. **What costs tokens and buys nothing?** The bundle is ~12,000 tokens against a free-tier ceiling
   nobody has measured. Name the passages that could come out without changing what a student sees.

**Rules for this audit:**

- **Read the shipped files.** Do not audit the docs that describe them; six documents in this repo
  already assert things that stopped being true.
- **Do not run model comparisons to answer this.** Reading is enough. Under decision 4, two-family
  verification is reserved for failures a human cannot see — the attempt gate, the key interlock,
  quote fidelity. An audit of register and content is not one of those.
- **Do not create tickets.** Write findings into one document with file paths and quotes.
- **Do not fix anything while auditing.** Separate passes.
- **Say what you could not judge.** Anything needing a real deck, a real student or a measurement
  that does not exist goes in a limits section, not a confident sentence.

**The two traps this project has fallen into repeatedly, so watch for them in your own output:**

- **A number that measures something against a copy of itself.** It has happened three times by
  three different mechanisms. Before any agreement or accuracy figure goes in, state what the two
  sides are and whether either saw the other.
- **A counterfactual presented as a measurement.** Computing what a change *would* do and tabling it
  beside a measured number is forbidden. State what would have to be true, then run it or say you
  did not.

**Deliverable:** one markdown file in `.scratch/deliverable-reviewer/`, named
`AUDIT-<date>-against-goal.md`. Lead with the single biggest gap between what the tool does and what
the goal says it should do. Then the five questions in order. Then limits.

**Do not start work on the findings.** The audit is the deliverable.
