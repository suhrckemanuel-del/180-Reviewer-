REVIEW OF: final recommendation deck | MODE: deep | KEYS: 0919-SIGMA7K/DELTA-3Q

BEFORE YOU USE THIS
1. Check the quotes. Every finding carries a verbatim quote and a location. Find each one in the deliverable yourself. It takes seconds. A quote you cannot find means that finding is discarded, not softened. Nothing is checking this but you.
2. There is no grade here, on purpose. This review does not say how ready the work is, because the same deliverable has been given two different answers on identical input. The findings below are the reliable part. Read them and make your own call.
3. This deliverable does not go to the client on this review alone, ever. A named human signs off on client work. That rule does not move.

Confidence in this review: High. Could change if: the full deck contains appendices or speaker notes that derive the 8% assumption, quantify staff capacity or explain the 5% launch gate.
Weakest areas: Analysis and insight, Risks assumptions and uncertainty, Feasibility and implementation
Effort to close the findings below: 4 to 8 hours

WHAT WORKS
1. The deck answers the client question early and directly.
   Where: Slide 2
   Quote: "Client E asked whether a paid membership could diversify income away from project grants. Our answer is yes, with a deliberately small start."

2. The recommendation is deliberately scoped to the client's capacity constraint.
   Where: Slide 6
   Quote: "Launching one tier at 45 pounds, rather than three tiers at once, keeps admin low and lets Client E learn before it scales."

3. The implementation path has an owner, timing and a test before scale-up.
   Where: Slide 10
   Quote: "The Client E coordinator owns the launch. Month one: soft launch to 200 contacts. Month two: review conversion against the 8% target. Month three: full launch if the soft launch clears 5%."

WHAT TO FIX, IN ORDER

1. The deck has two different success thresholds for the soft launch, so the board cannot tell what result triggers a full launch. [High impact]
   Where: Slide 10
   Quote: "Month two: review conversion against the 8% target. Month three: full launch if the soft launch clears 5%."
   Why it costs the client: The board could approve scale-up after 5% conversion or hold the team to 8%, which are different operating decisions. That changes whether the membership scheme launches broadly after the pilot.
   What to do: Define one decision rule for the soft launch. If 5% is the minimum viable threshold and 8% is the planning assumption, separate those roles and explain what happens at each outcome.
   Answer first: What conversion rate is enough evidence to justify full launch, and what action follows if the pilot lands between 5% and 8%?

2. The 8% conversion assumption is compared to engagement, not to actual membership conversion evidence. [High impact]
   Where: Slide 8
   Quote: "The 8% assumption is conservative against the 32% attendance rate and is the main thing to test."
   Why it costs the client: The board may treat the 5,000 pounds estimate as more grounded than it is. Attendance shows engagement, but it does not show willingness to pay for membership.
   What to do: Reframe 8% as a testable planning assumption unless the team can add a real comparator. The right comparator would be conversion from similar membership launches, the client's own past donation uptake or a sensitivity range.
   Answer first: What evidence would make 8% believable enough for a board decision, and what lower case still makes the pilot worth running?

3. The capacity risk is named but not tested against the proposed member benefits. [Moderate]
   Where: Slide 7
   Quote: "Priority booking, two members-only events a year and a discount with local partners. These use capacity Client E already has."
   Why it costs the client: The recommendation may add work to a one-coordinator organisation without showing whether the promised benefits fit existing capacity. The board needs to know if the offer is operationally realistic.
   What to do: Add a simple workload check for each benefit. Keep only benefits that can be delivered within current staff time or make the capacity trade-off explicit.
   Answer first: How many coordinator hours do priority booking, partner discounts and two member events require in the first three months?

THE HABIT TO BUILD
Separate assumptions, targets and launch gates every time a recommendation depends on a number. The weak habit here is using one conversion figure as forecast, benchmark and decision rule. Exercise: make a three-row table for any key number with "what we assume", "what we compare it to" and "what decision it triggers."

WHAT THIS REVIEW COULD NOT JUDGE
I could not verify the 2024 accounts, box-office data, funder letters or comparable pricing websites.
I could not assess the visual hierarchy, charts or slide design because the input is extracted text only.
I could not judge whether the listed member benefits are attractive to Client E's audience without audience research or client context.
I could not assess whether the coordinator has spare capacity beyond the stated constraint.

QUESTIONS WORTH ASKING THE TEAM
1. Why is 8% the right planning assumption rather than 5%, 10% or a range?
2. What exactly happens if the soft launch converts 5% to 7.9%?
3. How many hours will the coordinator need to run the soft launch and deliver the first member benefits?
4. Are the two member-only events new activity or re-labelled existing activity?
5. Which comparable organisations, if any, report membership uptake rather than only pricing?

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
  "quoteCheck": { "status": "lead-eye-check", "quotesChecked": 6, "quotesMissing": null },
  "ai": {
    "findings": [
      { "fid": "f1", "short": "Conflicting thresholds", "severity": "critical",
        "issueType": "implementation",
        "dimension": "Feasibility and implementation", "slides": [10] },
      { "fid": "f2", "short": "Weak conversion comparator", "severity": "major",
        "issueType": "thinking",
        "dimension": "Analysis and insight", "slides": [8] },
      { "fid": "f3", "short": "Capacity untested", "severity": "major",
        "issueType": "implementation",
        "dimension": "Risks, assumptions and uncertainty", "slides": [7] }
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
