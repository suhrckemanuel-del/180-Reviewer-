REVIEW OF: final recommendation deck | MODE: deep | KEYS: SIGMA-7K/DELTA-3Q

BEFORE YOU USE THIS
1. Check the quotes. Every finding carries a verbatim quote and a location. Find each one in the deliverable yourself. It takes seconds. A quote you cannot find means that finding is discarded, not softened. Nothing is checking this but you.
2. There is no grade here, on purpose. This review does not say how ready the work is, because the same deliverable has been given two different answers on identical input. The findings below are the reliable part. Read them and make your own call.
3. This deliverable does not go to the client on this review alone, ever. A named human signs off on client work. That rule does not move.

Confidence in this review: High. Could change if: the full deck has backup evidence for the 8% conversion assumption or staff-capacity test that is not in this extract.
Weakest areas: Evidence quality, Risks, assumptions and uncertainty, Feasibility and implementation
Effort to close the findings below: 4 to 7 hours

WHAT WORKS
- The answer is clear and early. Slide 2 says: "Our answer is yes, with a deliberately small start."
- The income risk is tied to client-specific evidence. Slide 3 says: "Project grants are 80% of Client E's income (2024 accounts) and each is single-year."
- The implementation path is unusually concrete for a final student deck. Slide 10 says: "The Client E coordinator owns the launch."

WHAT TO FIX, IN ORDER

1. The 8% conversion assumption is not yet defensible enough for the board decision because the comparator is engagement, not paid conversion. [High impact]
   Where: Slide 8
   Quote: "The 8% assumption is conservative against the 32% attendance rate and is the main thing to test."
   Why it costs the client: The board could approve a revenue case that looks grounded but is measured against the wrong behaviour. Attending events and paying annually are different decisions, so the 5,000 pounds upside may be overstated or simply uncalibrated.
   What to do: Reframe 8% as a scenario to test, not as a defensible forecast, unless the team can add a paid-membership comparator. Show the board a low, base and stretch case and make the launch decision depend on the soft-launch result.
   Answer first: What observed behaviour makes 8% a reasonable paid conversion rate rather than a hopeful assumption?

2. The go or no-go rule is unclear because the deck uses both 8% and 5% as decision thresholds. [High impact]
   Where: Slide 10
   Quote: "Month two: review conversion against the 8% target."
   Why it costs the client: The board will not know whether a 5% soft-launch result is success, failure or a warning. That changes whether they scale the scheme, revise the offer or stop after the pilot.
   What to do: Separate the year-one revenue assumption from the pilot decision rule. Define what each threshold means, what action follows and why the lower threshold is enough to continue.
   Answer first: If the 200-contact soft launch converts at 5%, exactly what should Client E do next and why?

3. The capacity risk is named but not tested against the stated constraint of one part-time coordinator. [Moderate]
   Where: Slide 9
   Quote: "We assume the mailing list is accurate and that members-only events do not strain staff."
   Why it costs the client: The recommendation depends on existing capacity, but the deck does not show what work the launch adds. A board with one part-time coordinator needs to know whether this is a manageable pilot or hidden extra workload.
   What to do: Turn the capacity assumption into a workload check. Estimate the coordinator tasks for setup, communications, payment handling and two events, then state what must be dropped, simplified or automated if capacity is tight.
   Answer first: How many coordinator hours does the three-month pilot require, and where do those hours come from?

4. The member offer is plausible but not evidenced against what the 200 most engaged contacts value. [Moderate]
   Where: Slide 7
   Quote: "Priority booking, two members-only events a year and a discount with local partners."
   Why it costs the client: The client could launch benefits that are administratively real but not motivating enough to convert supporters. The board needs to know why these benefits fit this audience, not only that they are possible.
   What to do: Link each benefit to evidence from the engaged base or make benefit appeal part of the soft-launch test. Keep the offer simple, but show what would prove it is the right simple offer.
   Answer first: What evidence says these three benefits are the ones most likely to make engaged contacts pay?

THE HABIT TO BUILD
Separate assumptions from evidence every time a number drives a recommendation. The weak habit here is using a related metric as if it proves the forecast. Exercise: for each key number, write one line with source, comparator, implication and what would falsify it.

WHAT THIS REVIEW COULD NOT JUDGE
- I could not verify the 2024 accounts, box-office data, funder letters or comparable pricing websites from the extracted text.
- I could not assess slide design, chart clarity or visual hierarchy because the input is extracted text only.
- I could not judge whether the proposed member benefits match audience preferences because no supporter research is included.
- I could not assess legal, tax or payment-processing implications of paid membership from this extract.

QUESTIONS WORTH ASKING THE TEAM
1. What evidence, if any, supports the 8% paid conversion assumption beyond the 32% attendance rate?
2. Why is 5% enough to trigger full launch if the year-one target is 8%?
3. How many coordinator hours will the pilot require in each month?
4. What will Client E stop, delay or simplify if membership admin strains capacity?
5. Did the team test the proposed benefits with any current supporters?

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
      { "fid": "f1", "short": "8% comparator", "severity": "major",
        "issueType": "evidence",
        "dimension": "Evidence quality", "slides": [8] },
      { "fid": "f2", "short": "threshold unclear", "severity": "major",
        "issueType": "implementation",
        "dimension": "Feasibility and implementation", "slides": [10] },
      { "fid": "f3", "short": "capacity untested", "severity": "major",
        "issueType": "implementation",
        "dimension": "Risks, assumptions and uncertainty", "slides": [9] },
      { "fid": "f4", "short": "offer unevidenced", "severity": "major",
        "issueType": "evidence",
        "dimension": "Recommendation specificity", "slides": [7] }
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
