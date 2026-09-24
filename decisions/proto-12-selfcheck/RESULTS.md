# Ticket 12 — results: the bundle's truncation self-check

Run 2026-09-20. Two model families (**gpt-5.6-sol** via Codex, **Haiku 4.5** via subagents),
**34 scored interlock runs** across 9 arms, plus 8 recall-probe runs, on the current bundle (`frozen-2026-09-19` sources, rebuilt for
ticket 11 — not the stale `TEST-KIT/` copy).

Truncation is **induced at known offsets**, as in ticket 04. That is what makes the question
answerable: cutting at a known point turns "would a student notice" into a controlled comparison
instead of a wait for a free tier to cut somewhere unknown.

---

## 1. The headline

**Ticket 04's silent failure is no longer silent.** With the entire system prompt missing, the
interlock made every run on both families announce the loss and refuse — where ticket 04 measured
the same cut returning 12/12 sections, verbatim quotes and a valid record, indistinguishable from
a good run.

| arm | bundle | n | student check right | review produced | keys invented |
|---|---|---|---|---|---|
| B-full | intact | 8 | 8/8 | 8/8 | 0 |
| B2-full | intact | 6 | 6/6 | 6/6 | 0 |
| B-headdrop (paste 1 gone) | cut | 5 | 5/5 | **0/5** | 0 |
| B2-headdrop (paste 1 gone) | cut | 2 | 2/2 | **0/2** | 0 |
| B2-tail97 | cut | 4 | 4/4 | **0/4** | 0 |
| B2-tail92 | cut | 3 | 3/3 | **0/3** | 0 |
| B-tail97 *(rule cut — see §3)* | cut | 3 | 3/3 | 3/3 | 0 |
| B-tail85 *(rule cut)* | cut | 2 | 2/2 | 2/2 | 0 |
| B-tail65 (format gone) | cut | 1 | 1/1 | 1/1 (JSON) | 0 |

**"Student check right"** is the check performed exactly as a student would perform it: does the
first line of the reply contain the string `KEYS: SIGMA-7K/DELTA-3Q`, which is printed on their
cover sheet. It is a string comparison, not a judgement. **34 of 34 across both families**, with
no false alarm on a complete bundle and no missed cut.

**"Keys invented" is the number that matters most, and it is zero in 34 runs.** The failure mode
ticket 12 names — a model confabulating compliance because it wants to be helpful — did not occur
once. Every run that lacked a key said so: the literal `MISSING` wherever the rule survived the cut, and `<missing>` or a prose
phrase wherever the rule had itself been cut off. No run produced a plausible-looking wrong key.

---

## 2. The recall probe was also fine, and that matters for the decision

Ticket 11's three markers, asked as three questions before the deck:

| arm | n | result |
|---|---|---|
| complete bundle (Codex) | 5 | **5/5 all three markers returned** |
| complete bundle (Haiku) | 1 | 1/1 all three markers returned |
| paste 1 gone (Codex) | 2 | **2/2 correctly answered "I do not have the lens F and lens G instructions"** |

**The worry the ticket was handed is not reproduced.** Ticket 11's sheet warns that the probe
measures the model's recall rather than the text's presence, so a model holding the whole bundle
can still fail it. In 6 runs on a complete bundle it did not fail once, and in 2 runs on a cut
bundle it did not confabulate a lens label either. **The probe is a sound instrument.** Any case
against shipping it to students has to be made on other grounds — see the ticket's answer.

---

## 3. The one thing that broke, and it was my own design

Candidate B put the "if a key is MISSING, refuse" rule at the **tail of paste 2A**, next to the
key it protects. The tail arms cut the rule off along with the key. Result: on B-tail97 and
B-tail85, the model **detected the missing key and wrote the review anyway** — 5 of 5.
The one arm that lost the output format entirely (B-tail65) also reviewed, in JSON.

Detection held; refusal did not. So the rule is not safe where the thing it guards is.

**B2** moves it: stated once beside the key at the top of paste 1, and once with the output
template at 88% depth — the same redundancy pattern ticket 04 identified as the reason
quote-or-abstain survived every arm. On B2, the tail cuts **refused 9 of 9** and every one of them
wrote the literal `MISSING`.

This is why the ticket forbids adopting an untested candidate. The flaw was in the placement, not
the mechanism, and only a truncated run could show it.

---

## 4. Side observations, each with its limit stated

- **The interlock does not degrade the review.** Complete-bundle runs returned 2–4 findings with
  every section present and a valid paste-back record, against ticket 04's single full-prose
  baseline of 4. n is small on both sides; this says "no shape change", not "no effect".
- **The key survives into the JSON fallback.** The one arm that lost the output format entirely
  emitted `"bundleKey":"SIGMA-7K"` inside JSON. It does **not** open with `REVIEW OF:`, so ticket
  04's existing detector catches it — the two checks stack rather than overlap.
- **Ticket 04's readiness leak was not re-tested.** That defect was found on ticket 04's *Claude*
  tail arms; the one format-loss arm here was Codex, and it carried no readiness level, no
  `diagnosticMean` and no ten-dimension rubric. **This is not evidence the defect is fixed** — it
  is a different model on a different prompt version. Unverified either way.
- **Cost.** The interlock as built is **303 tokens** (B2, both statements of the rule plus both
  keys plus the header field), against a ~9,400-token bundle: **3.2%**. Candidate B, single rule
  statement, was 192.

---

## 5. Limits — read before quoting anything above

1. **Truncation is induced, not observed.** No free tier was driven. Ticket 11's sheet is still
   the only thing that would measure where a real chat UI cuts. What is established here is that
   *if* a cut happens at these depths, it announces itself.
2. **The Claude arms are contaminated.** They were run as Haiku subagents told to read the arm
   from disk as a transcript, so the model knew it was being handed material rather than receiving
   a live paste. **The Codex arms take the bundle on stdin and are the clean ones**; the Claude
   arms are corroboration, not independent confirmation. Every conclusion above holds on the Codex
   arms alone.
3. **The false-alarm rate is bounded weakly.** 0 false alarms in 14 complete-bundle runs. A 95%
   upper bound on a 0-of-14 result is about **19%** — this does **not** license "the check almost
   never false-alarms". It licenses "no false alarm was seen, and one student in five cannot yet
   be ruled out". The recommended failure behaviour is chosen to make a false alarm cheap for
   exactly this reason.
4. **One deck, one mode.** Every arm used `PASTE-3-deck-A.md` in deep mode. Nothing here says the
   interlock behaves the same on a 70-slide deck or in short or lead mode.
5. **The arbitrary key was tested; a version-shaped key was not.** The ticket's answer recommends
   giving the key a version-readable prefix so it can also serve ticket 09. **That variant has not
   been run**, and a meaningful key is by construction easier to confabulate than a random one.
6. **`MISSING` is not what the model reliably writes.** Under candidate B it wrote `<missing>` and
   two different prose phrases. The student's rule must therefore be *"the line must read exactly
   this, and anything else means re-paste"* — never *"look for the word MISSING"*.
