REVIEW OF: final recommendation deck | MODE: deep | KEYS: SIGMA-7K/DELTA-3Q

BEFORE YOU USE THIS
1. Check the quotes. Every finding carries a verbatim quote and a location. Find each one in the deliverable yourself. It takes seconds. A quote you cannot find means that finding is discarded, not softened. Nothing is checking this but you.
2. There is no grade here, on purpose. This review does not say how ready the work is, because the same deliverable has been given two different answers on identical input. The findings below are the reliable part. Read them and make your own call.
3. This deliverable does not go to the client on this review alone, ever. A named human signs off on client work. That rule does not move.

Confidence in this review: High. Could change if: the full deck contains conversion benchmarks, staff capacity calculations or a clearer soft-launch decision rule not present in the extracted text.
Weakest areas: Evidence quality, Analysis and insight, Feasibility and implementation
Effort to close the findings below: 3 to 6 hours

WHAT WORKS
- The recommendation is clear from the start. Slide 1: "Client E should launch a paid membership scheme, starting with a single tier in the autumn."
- The deck uses relevant internal evidence rather than only generic sector logic. Slide 3: "Project grants are 80% of Client E's income (2024 accounts) and each is single-year."
- The implementation is more concrete than many student recommendations. Slide 10: "The Client E coordinator owns the launch. Month one: soft launch to 200 contacts."

WHAT TO FIX, IN ORDER

1. The soft-launch decision rule conflicts with itself: the team says to test against 8% but proceed at 5%. [High impact]
   Where: Slide 10
   Quote: "Month two: review conversion against the 8% target. Month three: full launch if the soft launch clears 5%."
   Why it costs the client: The board cannot tell what result should trigger a full launch. At 6% conversion, one rule says the test missed target and the other says proceed, leading to different actions.
   What to do: Choose one decision rule and explain the logic behind it. If 5% is the go/no-go threshold, separate it from the 8% year-one planning assumption and say what each number is for.
   Answer first: What soft-launch conversion rate should make the board continue, pause or redesign?

2. The 8% conversion assumption is treated as conservative, but the comparison does not prove that paid conversion is likely. [High impact]
   Where: Slide 8
   Quote: "The 8% assumption is conservative against the 32% attendance rate and is the main thing to test."
   Why it costs the client: Attendance shows engagement, not willingness to pay for membership. If the board accepts 8% as defensible without a paid-conversion comparator, it may overestimate income and staff capacity.
   What to do: Reframe 8% as an explicit test assumption rather than a defended forecast, or add a relevant comparator such as prior donation conversion, paid supporter conversion or comparable membership take-up.
   Answer first: Compared with what real paid-conversion evidence is 8% conservative?

3. The capacity risk is named but not yet tested against the specific benefits being promised. [Moderate]
   Where: Slide 7
   Quote: "Priority booking, two members-only events a year and a discount with local partners. These use capacity Client E already has."
   Why it costs the client: The board needs to know whether one part-time coordinator can deliver the promised benefits without weakening existing programming. The deck asserts capacity rather than showing the workload.
   What to do: Add a simple workload check for each benefit: who does it, how often, what new admin it creates and what would be cut if capacity is tight.
   Answer first: Which member benefits can be delivered with no new recurring workload?

THE HABIT TO BUILD
Separate a planning assumption from a decision threshold. The weak habit is using one attractive number to do several jobs: forecast revenue, justify confidence and trigger rollout. Exercise: for every key number, label it as evidence, assumption, target or go/no-go rule, then check that no number is playing two roles without explanation.

WHAT THIS REVIEW COULD NOT JUDGE
I could not assess the visual slide design, chart quality or whether the board can skim the actual deck layout, because the input is extracted text only.
I could not verify the 2024 accounts, box-office data, funder letters or comparable pricing websites.
I could not judge whether 45 pounds is affordable for Client E's audience from the text provided.
I could not assess whether the promised local partner discount is already agreed or only proposed.
I could not test whether the mailing list quality supports a 200-contact soft launch beyond the team's statement.

QUESTIONS WORTH ASKING THE TEAM
1. What happens if the soft launch converts 5% to 7.9% of the 200 contacts?
2. What evidence, if any, makes 8% a reasonable paid-membership assumption rather than a hopeful target?
3. How many staff hours will priority booking, two member events and partner discounts require in a normal month?
4. Are the local partner discounts already secured?
5. Is 45 pounds meant to maximize income, accessibility or ease of administration?

HOW TO CHECK THIS FEEDBACK
Every point above quotes your own deliverable and says where. If you cannot find one of these quotes in your own work, that point is wrong. Drop it and say so. This review advises. A human decides, and nothing here goes to your client on its own.

=== PASTE-BACK RECORD ===

Fill the nulls once you have decided what to act on, then send this block back to whoever runs the reviewer. It is the only trace a chat review leaves, and the question it answers is which findings people actually keep. Two minutes.

Fill: capturedAt, model, deliverable.ref, lead.id, lead.vsByHand, quotesMissing, an action for every finding ("keep", "ask" or "cut", plus a cutReason when you cut), mustCatch, and your own readinessCall.lead with a one-line reason. cutReason is one of: wrong, not-an-issue, too-minor, duplicate, out-of-scope.

readinessCall.lead is **your** judgement, not the reviewer's — it has none. One of: Not ready for client review, Needs substantial revision, Needs targeted revision, Nearly ready with minor edits.

{
  "recordVersion": "override-log-2-chat",
  "capturedAt": null,
  "reviewer": {
    "promptVersion": "frozen-2026-08-09",
    "mode": "deep",
    "executionMode": "chat",
    "model": null
  },
  "deliverable": {
    "ref": null,
    "artifactType": "final recommendation deck",
    "stage": "final"
  },
  "lead": { "id": null, "secondsOnTask": null, "vsByHand": null },
  "quoteCheck": { "status": "lead-eye-check", "quotesChecked": 6, "quotesMissing": null },
  "ai": {
    "findings": [
      { "fid": "f1", "short": "Conflicting threshold", "severity": "major",
        "issueType": "implementation",
        "dimension": "Feasibility and implementation", "slides": [10] },
      { "fid": "f2", "short": "Weak comparator", "severity": "major",
        "issueType": "evidence",
        "dimension": "Evidence quality", "slides": [8] },
      { "fid": "f3", "short": "Capacity untested", "severity": "minor",
        "issueType": "implementation",
        "dimension": "Feasibility and implementation", "slides": [7] }
    ]
  },
  "decisions": [
    { "fid": "f1", "action": null, "cutReason": null, "note": "" },
    { "fid": "f2", "action": null, "cutReason": null, "note": "" },
    { "fid": "f3", "action": null, "cutReason": null, "note": "" }
  ],
  "added": [],
  "mustCatch": null,
  "readinessCall": { "ai": null, "lead": null, "reason": "" },
  "sent": false
}

=== END. ===
