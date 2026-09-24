REVIEW OF: final recommendation deck | MODE: deep | KEYS: SIGMA-7K/DELTA-3Q

BEFORE YOU USE THIS
1. Check the quotes. Every finding carries a verbatim quote and a location. Find each one in the deliverable yourself. It takes seconds. A quote you cannot find means that finding is discarded, not softened. Nothing is checking this but you.
2. There is no grade here, on purpose. This review does not say how ready the work is, because the same deliverable has been given two different answers on identical input. The findings below are the reliable part. Read them and make your own call.
3. This deliverable does not go to the client on this review alone, ever. A named human signs off on client work. That rule does not move.

Confidence in this review: High. Could change if: the appendix contains conversion benchmarks, staff workload sizing or soft-launch materials not included here.
Weakest areas: Evidence quality, Analysis and insight, Risks, assumptions and uncertainty
Effort to close the findings below: 4 to 8 hours

WHAT WORKS
- The answer is clear and appropriately bounded for the board. Slide 2: "Our answer is yes, with a deliberately small start."
- The implementation path has an owner, timing and a test gate. Slide 10: "The Client E coordinator owns the launch. Month one: soft launch to 200 contacts. Month two: review conversion against the 8% target. Month three: full launch if the soft launch clears 5%."
- The deck is honest that the main revenue assumption must be tested. Slide 8: "The 8% assumption is conservative against the 32% attendance rate and is the main thing to test."

WHAT TO FIX, IN ORDER

1. The 8% conversion assumption drives the recommendation but is not yet benchmarked against paid membership conversion. [High impact]
   Where: Slide 8
   Quote: "If 8% of the mailing list joins at 45 pounds, that is about 5,000 pounds in year one."
   Why it costs the client: The board may treat the 5,000 pounds as a defensible forecast when the deck only shows an internal assumption. If 8% is too high, the client may launch a scheme whose admin cost outweighs its income value.
   What to do: Separate the revenue case from the test case. Show what happens at lower conversion rates and name the minimum conversion that makes the launch worth the coordinator's time.
   Answer first: What conversion rate would make this scheme still worth doing for Client E?

2. The comparator for 8% is not decision-grade because attendance interest is not the same as paid conversion. [High impact]
   Where: Slide 4 and Slide 8
   Quote: "Client E has 1,400 people on its mailing list and a 32% event-attendance rate (box-office data, 2024)."
   Quote: "The 8% assumption is conservative against the 32% attendance rate and is the main thing to test."
   Why it costs the client: The client could overestimate willingness to pay by comparing a paid annual commitment to event attendance. That changes whether the board should approve a full launch or only a tightly capped experiment.
   What to do: Use the attendance rate only as engagement evidence. Add a paid-conversion comparator if available, or present 8% explicitly as a hypothesis with low, base and high scenarios.
   Answer first: Compared to what paid action is 8% conservative?

3. The risk section names staff strain but does not quantify whether the offer fits one part-time coordinator. [Moderate]
   Where: Slide 7 and Slide 9
   Quote: "Priority booking, two members-only events a year and a discount with local partners. These use capacity Client E already has."
   Quote: "We assume the mailing list is accurate and that members-only events do not strain staff."
   Why it costs the client: The board cannot see whether the benefits package is operationally light enough. If the events or partner discounts add hidden work, the right first offer may be simpler than the deck recommends.
   What to do: Add a simple workload check for each benefit and define what gets removed if the coordinator cannot absorb it. Keep the offer only as broad as the capacity evidence supports.
   Answer first: How many coordinator hours does the soft launch and each member benefit require?

4. The governing insight is clear across the deck but not stated in one sentence up front. [Minor]
   Where: Slide 1 and Slide 2
   Quote: "Client E should launch a paid membership scheme, starting with a single tier in the autumn."
   Quote: "Client E asked whether a paid membership could diversify income away from project grants. Our answer is yes, with a deliberately small start."
   Why it costs the client: A fast board reader gets the decision quickly, but has to assemble the reason from later slides. This weakens the first pass rather than the underlying recommendation.
   What to do: Put the action and the reason in the same opening sentence. Make the first page answer why this is worth doing despite the conversion risk.
   Answer first: What is the single reason the board should approve a small launch now?

THE HABIT TO BUILD
Build the habit of turning every decisive assumption into a testable threshold. The weak habit is treating a plausible number as support before showing what would make it good or bad. Exercise: for each recommendation, write the one number that would change your mind, then add the low, base and break-even cases.

WHAT THIS REVIEW COULD NOT JUDGE
I could not verify whether the three comparable local arts non-profits are genuinely comparable.
I could not assess whether the 45 pound price matches Client E's audience willingness to pay.
I could not assess the real coordinator workload without a task list or staff capacity estimate.
I could not check the 2024 accounts, box-office data or funder letters.
I could not judge whether member-only events are feasible in Client E's programming calendar.

QUESTIONS WORTH ASKING THE TEAM
1. What evidence, if any, supports 8% as a paid conversion rate rather than an engagement proxy?
2. What is the break-even conversion rate after coordinator time and event costs?
3. What would the team recommend if the soft launch converts at 3%, 5% or 8%?
4. Which member benefit would be removed first if staff capacity is tighter than assumed?
5. Are the three comparator organisations similar in audience, scale and offer?

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
  "quoteCheck": { "status": "lead-eye-check", "quotesChecked": 9, "quotesMissing": null },
  "ai": {
    "findings": [
      { "fid": "f1", "short": "8% unbenchmarked", "severity": "major",
        "issueType": "evidence",
        "dimension": "Evidence quality", "slides": [8] },
      { "fid": "f2", "short": "Weak comparator", "severity": "major",
        "issueType": "thinking",
        "dimension": "Analysis and insight", "slides": [4, 8] },
      { "fid": "f3", "short": "Capacity untested", "severity": "major",
        "issueType": "implementation",
        "dimension": "Risks, assumptions and uncertainty", "slides": [7, 9] },
      { "fid": "f4", "short": "Opening insight", "severity": "minor",
        "issueType": "communication",
        "dimension": "Storyline and pyramid logic", "slides": [1, 2] }
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
