REVIEW OF: final recommendation deck | MODE: deep | KEYS: SIGMA-7K/<missing>

BEFORE YOU USE THIS
1. Check the quotes. Every finding carries a verbatim quote and a location. Find each one in the deliverable yourself. It takes seconds. A quote you cannot find means that finding is discarded, not softened. Nothing is checking this but you.
2. There is no grade here, on purpose. This review does not say how ready the work is, because the same deliverable has been given two different answers on identical input. The findings below are the reliable part. Read them and make your own call.
3. This deliverable does not go to the client on this review alone, ever. A named human signs off on client work. That rule does not move.

Confidence in this review: High. Could change if: the full visual deck contains evidence, footnotes or assumptions not present in this extracted text.
Weakest areas: Analysis and insight, Risks, assumptions and uncertainty, Feasibility and implementation
Effort to close the findings below: 3 to 6 hours

WHAT WORKS
- The recommendation is clear and early.
  Where: Slide 1
  Quote: "Client E should launch a paid membership scheme, starting with a single tier in the autumn."

- The income problem is concrete and sourced to client records.
  Where: Slide 3
  Quote: "Project grants are 80% of Client E's income (2024 accounts) and each is single-year."

- The implementation path has an owner, timing and a test gate.
  Where: Slide 10
  Quote: "The Client E coordinator owns the launch. Month one: soft launch to 200 contacts. Month two: review conversion against the 8% target. Month three: full launch if the soft launch clears 5%."

WHAT TO FIX, IN ORDER

1. The soft-launch decision rule is internally unclear: the deck says to review against 8% but proceed at 5%. [High impact]
   Where: Slide 10
   Quote: "Month two: review conversion against the 8% target. Month three: full launch if the soft launch clears 5%."
   Why it costs the client: The board cannot tell whether 5% is success, warning or failure. In the 5% to 7.9% range, one reading tells Client E to proceed while another tells it to pause or redesign.
   What to do: Define one decision gate for the soft launch and explain what each result triggers. Separate the planning assumption from the minimum go/no-go threshold if both are needed.
   Answer first: What exact conversion result makes the board approve a full launch?

2. The 8% conversion assumption drives the financial case but is not defended by evidence of willingness to pay. [High impact]
   Where: Slide 8
   Quote: "If 8% of the mailing list joins at 45 pounds, that is about 5,000 pounds in year one."
   Why it costs the client: The recommendation turns on whether roughly 112 people will pay. Attendance proves engagement, not paid membership intent, so the board may overestimate revenue from the mailing list.
   What to do: Treat 8% as a test assumption, not a defended forecast. Add the evidence that would validate it, such as soft-launch responses, past donations, repeat attendance or a sensitivity range.
   Answer first: What observable behaviour makes 8% plausible enough for the board to use?

3. The capacity risk is asserted away rather than tested against the one-coordinator constraint. [High impact]
   Where: Slide 7
   Quote: "Priority booking, two members-only events a year and a discount with local partners. These use capacity Client E already has."
   Why it costs the client: The board is being asked to approve a scheme that adds admin, events and partner coordination. If capacity is wrong, the scheme can create work before it creates reliable income.
   What to do: Show the operating load behind the offer. Estimate the coordinator tasks, event burden and partner-management steps, then simplify the benefits if the load exceeds current capacity.
   Answer first: What work must the coordinator do each month to deliver this membership offer?

4. The deck names the right risks but does not make the downside visible enough for a board decision. [Moderate]
   Where: Slide 9
   Quote: "The main risk is low conversion. We assume the mailing list is accurate and that members-only events do not strain staff."
   Why it costs the client: The board needs to know what happens if the assumptions fail. As written, the risk section identifies the risks but does not quantify the consequence or name the stop-loss action.
   What to do: Add a downside case and a stop rule. Keep it directional: what revenue looks like at lower conversion, what work stops if uptake is weak and what cost is capped.
   Answer first: What is the worst acceptable soft-launch outcome before Client E stops or redesigns?

THE HABIT TO BUILD
Turn every recommendation into a decision rule. The weak habit here is naming a good idea and a plausible pilot but leaving the board to infer what result means proceed, pause or stop. Exercise: for each recommendation, write one sentence that says "If X happens, do Y. If not, do Z" before building the slide.

WHAT THIS REVIEW COULD NOT JUDGE
The visual deck was not provided, so layout, hierarchy and whether the message survives the actual slide design were not assessed.
The source documents were not provided, so I did not verify the 2024 accounts, box-office data, funder letters or comparable pricing.
The board's risk appetite was not provided, so I could not judge whether 5%, 8% or another threshold is commercially acceptable.
The operational calendar was not provided, so I could not verify whether two member-only events use existing capacity.
No part 2 bundle key was provided.

QUESTIONS WORTH ASKING THE TEAM
1. Why is 8% the right planning assumption rather than a sensitivity case?
2. Is 5% the minimum launch threshold or is 8% the threshold?
3. What work does the coordinator stop doing to run the membership scheme?
4. What happens if the soft launch converts 5% to 7.9%?
5. What evidence would make the board confident that attendance converts into paid membership?

HOW TO CHECK THIS FEEDBACK
Every point above quotes your own deliverable and says where. If you cannot find one of these quotes in your own work, that point is wrong. Drop it and say so. This review advises. A human decides, and nothing here goes to your client on its own.


=== PASTE-BACK RECORD ===

Fill the nulls once you have decided what to act on, then send this block back to whoever runs the reviewer. It is the only trace a chat review leaves, and the question it answers is which findings people actually keep. Two minutes.

Fill: capturedAt, model, deliverable.ref, lead.id, lead.vsByHand, quotesMissing, an action for every finding ("keep", "ask" or "cut", plus a cutReason when you cut), mustCatch, and your own readinessCall.lead with a one-line reason. cutReason is one of: wrong, not-an-issue, too-minor, duplicate, out-of-scope.

readinessCall.lead is your judgement, not the reviewer's. It has none. One of: Not ready for client review, Needs substantial revision, Needs targeted revision, Nearly ready with minor edits.

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
  "quoteCheck": { "status": "lead-eye-check", "quotesChecked": 8, "quotesMissing": null },
  "ai": {
    "findings": [
      { "fid": "f1", "short": "unclear gate", "severity": "major", "issueType": "thinking", "dimension": "Recommendation specificity", "slides": [10] },
      { "fid": "f2", "short": "weak assumption", "severity": "major", "issueType": "evidence", "dimension": "Analysis and insight", "slides": [8] },
      { "fid": "f3", "short": "capacity untested", "severity": "major", "issueType": "implementation", "dimension": "Feasibility and implementation", "slides": [7] },
      { "fid": "f4", "short": "downside thin", "severity": "minor", "issueType": "thinking", "dimension": "Risks, assumptions and uncertainty", "slides": [9] }
    ]
  },
  "decisions": [
    { "fid": "f1", "action": null, "cutReason": null, "note": "" },
    { "fid": "f2", "action": null, "cutReason": null, "note": "" },
    { "fid": "f3", "action": null, "cutReason": null, "note": "" },
    { "fid": "f4", "action": null, "cutReason": null, "note": "" }
  ],
  "added": [],
  "mustCatch": null,
  "readinessCall": { "ai": null, "lead": null, "reason": "" },
  "sent": false
}

=== END. ===
