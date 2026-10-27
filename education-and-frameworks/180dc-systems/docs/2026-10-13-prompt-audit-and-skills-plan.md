# Reviewer prompt audit and the 180DC skills plan

Written 2026-10-13. Audits release `1006-NCEECNQ` (candidate-2026-10-05-split) in
`suhrckemanuel-del/180-Reviewer-`, and proposes a shared skill suite for the branch.

## 1. Where things stand

| Piece | State on 2026-10-13 |
|---|---|
| Reviewer | First release exists: `releases/1006-NCEECNQ`, merged in PR #6 on 2026-10-05. Separate student and lead setups, a local HTML view, an intake helper. Labelled a supervised candidate awaiting owner review. Issues #1–#5 open |
| Real use | Improvement-log entries are owner feedback on archived reviews. No consultant or lead has used the release yet |
| Validation | Three real PDFs were reviewed on candidate 2e and audited by separate AI agents: 29 of 29 quotes confirmed, severity inflated across the sample, two missed decision questions. No human adjudication yet |
| Workshop | 2-hour plan agreed: `education/workshops/2026-10-deliverables-and-ai.md`. Materials not built |
| AI use-case research | About 110 sourced use cases: `research/07-ai-use-cases-for-consultants/` |
| Uncommitted | Both folders above are in this worktree only. The main checkout also has uncommitted reviewer edits from 2026-09-24 |

## 2. Prompt audit: `STUDENT-SETUP.txt`

Size: 715 lines, about 8,000 words (roughly 11k tokens), before the deck. The lead setup is about
97% the same text.

### What is strong and must survive

- Quote-or-abstain, with exact whitespace rules and the rule against joining separate items.
- "Things that look like defects and are not" (Part One, section 6). This is the most valuable
  content in the file.
- Severity defaults to minor; promotion needs two named actions or a material change in
  defensibility.
- Strengths first, zero findings valid, "what this review could not judge" always filled.
- The principle library (section 8), now grounded in the source register.

### What is wrong

1. **Leftover JSON plumbing.** Line 279 orders "ONE valid JSON object", and a chat-format
   exception follows. The file refers to `questionsForLead`, `notAssessed`, `highestRiskIssue`,
   `deliveryCritical`, `learningNote`, `issueType`, `fid` (9 times) and "the record". **The
   student template has no record block.** The model is told to fill fields that do not exist.
2. **Three overlapping taxonomies plus two more.** Nine lenses, ten dimensions, five blocking
   rules, five `issueType` values and three severities. The model reconciles them on every run.
3. **History the model doesn't need.** About 40 lines on the withdrawn readiness level, the
   ceilings ("Not ready", "Needs substantial revision") and "the hosted version of this tool".
   Explaining a removed feature costs tokens and puts the forbidden words in front of the model.
4. **Duplication.** The bundle-key block appears twice (lines 19–30 and 576–587). The audience
   contract appears twice (5–14 and 704–715). The noise budget is stated twice.
5. **Contradictions.**
   - "At most 5 questions for the project lead" (lines 153 and 679) vs "at most 2" (line 652).
   - The student template offers `MODE: lead` (line 593).
   - "A lead reads this once, on a phone" (line 699) sits in the student path.
   - The voice rule bans em dashes (line 274), and line 560 uses one.
6. **Patches from individual cases.** Map-placement scoring, disclosure labels, parallel surveys
   and model weights (lines 54–72, 176–183, 408–411) read as fixes for three specific decks.
   They belong in an examples file, not in the core rules every review must parse.
7. **233 negations** ("do not", "never", "not") in 8,000 words. Models follow positive
   instructions more reliably than long lists of prohibitions.
8. **Wall-of-text rules.** Lines 176 and 183 are single paragraphs of more than 100 words each.
9. **The vision and the product disagree.** `VISION.md` commitment 1 is still "Attempt first".
   The release says "NO ATTEMPT GATE". That may be the right call (coaching now happens after the
   review), but it is an owner decision and should be written into the vision. Outside evidence:
   practising with an AI that gives answers lowered later performance by 17%, and hints did no
   harm (Bastani et al., PNAS 2025). The post-review coaching should stay hint-shaped.

### Optimisation targets

- Cut about 40%: history, duplicates, JSON residue, the second taxonomy.
- One taxonomy: five review questions (decision, framing, storyline, evidence,
  recommendation/implementation), plus the severity rule.
- Move the case patches and the full rubric (with its real sub-checks) into reference files that
  load only when needed. The skill format makes this possible.
- Rewrite prohibitions as positive instructions where the meaning survives.
- Check quotes with a script, not with the student's eyes (see 3.1).

Verification, kept small: run the old and the new prompt on the same three real PDFs, compare
quote fidelity and severity, and have the owner read both. Nothing more before real use.

## 3. The skills suite

**Why skills.** A skill is a short `SKILL.md` plus reference files and scripts that load only when
needed. That fixes the reviewer's two biggest problems: an 11k-token paste with an unmeasured
ceiling, and quote checking that nobody enforces. Skills run on Claude's **Free** plan: each
person uploads the zip under Customize > Skills, with code execution turned on. Sharing one copy
org-wide needs Team or Enterprise. SKILL.md is an open standard: ChatGPT supports it and the Gemini
app is reportedly rolling it out. The paste bundle stays as the fallback for any other model.

**Shared design rules**
- One `principles.md` is the single source for all four skills, copied in at build time.
- Each `SKILL.md` stays short: when to use it, the non-negotiables, the workflow. Everything else
  goes in `references/`.
- Deterministic jobs go in `scripts/`: quote checking, deck extraction, chart rendering.
- Every skill teaches and leaves the client's words to the consultant.

### 3.1 `180dc-review`: deliverable reviewer
- `SKILL.md`: the non-negotiables (quote or abstain, no grade, no slide-ready copy, strengths
  first, zero findings valid, say what you could not judge) and the workflow.
- `references/`: `student.md`, `lead.md`, `rubric.md` (the full ten dimensions with sub-checks,
  affordable now that it loads on demand), `false-positives.md`, `severity.md`, `examples.md`
  (the case patches).
- `scripts/check_quotes.py`: verifies every quoted passage against the deck text before the review
  is shown. This restores the trust boundary the hosted version had.
- `scripts/extract_deck.py`: from the existing `deck-to-paste.py`.

### 3.2 `180dc-coach`: learning
Socratic practice on the consultant's own work, using the workshop's three principles and the
research's top moves: the "so what?" ladder, a MECE audit of an issue tree they built, red-teaming
their recommendation, and a Pyramid check of their storyline. It asks for their attempt first and
gives hints, not answers.

### 3.3 `180dc-visuals`: charts and slides from data
Title first, then a chart that proves it. It recomputes the plotted numbers from the data,
renders a clean PowerPoint-ready chart or an HTML artifact in the 180DC palette (#78B038), adds a
source line, and checks that the title states the so-what. A HyperFrames reference is included
only for Claude Code users.

### 3.4 `180dc-research`: desk research with verified sources
Every claim carries a source and a quote. The skill checks that cited sources exist (the Deloitte
failure mode), separates "not found" from "confirmed absent", and returns a sourced fact table.
It covers interview synthesis too: themes, counts, verbatim quotes, and what only one person said.

### Order
1. `180dc-review`, built from the optimised prompt. It proves the format and replaces the paste.
2. `180dc-coach`, which doubles as workshop material.
3. `180dc-visuals`, for the workshop build block.
4. `180dc-research`.

Each ships when the owner has used it once on real work and logged what was wrong.
