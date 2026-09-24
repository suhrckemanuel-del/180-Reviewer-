REVIEW OF: final recommendation deck | MODE: deep | KEYS: SIGMA-7K/DELTA-3Q

BEFORE YOU USE THIS
1. Check the quotes. Every finding carries a verbatim quote and a location. Find each one in the deliverable yourself. It takes seconds. A quote you cannot find means that finding is discarded, not softened. Nothing is checking this but you.
2. There is no grade here, on purpose. This review does not say how ready the work is, because the same deliverable has been given two different answers on identical input. The findings below are the reliable part. Read them and make your own call.
3. This deliverable does not go to the client on this review alone, ever. A named human signs off on client work. That rule does not move.

Confidence in this review: High. Could change if: the full deck contains visual evidence, cost detail or board-facing assumptions not present in the extracted text.
Weakest areas: Evidence quality, Analysis and insight, Risks, assumptions and uncertainty
Effort to close the findings below: 4 to 8 hours

WHAT WORKS
1. The recommendation is clear and early.
   Where: Slide 1
   Quote: "Client E should launch a paid membership scheme, starting with a single tier in the autumn."

2. The deck gives a practical test before scaling.
   Where: Slide 9
   Quote: "A soft launch to the most engaged 200 contacts tests both before the full launch."

3. The implementation path has an owner, timing and a decision gate.
   Where: Slide 10
   Quote: "The Client E coordinator owns the launch. Month one: soft launch to 200 contacts. Month two: review conversion against the 8% target. Month three: full launch if the soft launch clears 5%."

WHAT TO FIX, IN ORDER

1. The 8% conversion assumption drives the case but is not benchmarked against a paid-membership conversion comparator. [High impact]
   Where: Slide 8
   Quote: "If 8% of the mailing list joins at 45 pounds, that is about 5,000 pounds in year one. The 8% assumption is conservative against the 32% attendance rate and is the main thing to test."
   Why it costs the client: The board could approve the launch on a revenue case that looks tested but is only compared with event attendance, not willingness to pay. Attendance rate does not establish paid conversion.
   What to do: Separate the arithmetic from the assumption. Show what year-one income looks like at lower, base and higher conversion, then explain why the board should treat the soft launch as the real validation point.
   Answer first: What paid-membership conversion range, from comparable groups or the soft launch design, makes 8% a defensible planning assumption?

2. The staff-capacity risk is named as an assumption but not tested with the same rigor as conversion. [High impact]
   Where: Slide 9
   Quote: "We assume the mailing list is accurate and that members-only events do not strain staff."
   Why it costs the client: With one part-time coordinator and no budget for staff, the board needs to know whether the scheme is operationally light enough to run. If not, the right decision may be to delay, simplify benefits or remove events.
   What to do: Turn capacity into a testable operating assumption. Estimate the coordinator tasks by launch month and steady state, then show which member benefits would be cut first if workload exceeds capacity.
   Answer first: How many coordinator hours does the soft launch and full launch require, and which promised benefits create the largest workload?

3. The core rationale appears later than the decision, so a fast board reader gets the answer before the reason. [Moderate]
   Where: Slide 1
   Quote: "Client E should launch a paid membership scheme, starting with a single tier in the autumn."
   Where: Slide 2
   Quote: "Our answer is yes, with a deliberately small start."
   Where: Slide 6
   Quote: "Launching one tier at 45 pounds, rather than three tiers at once, keeps admin low and lets Client E learn before it scales."
   Why it costs the client: The board can extract the recommendation, but not the governing reason from the opening pass. The important logic is that a small single-tier launch fits capacity and creates a learning test.
   What to do: Put the decision and the reason together at the front. The opening should make clear that the recommendation is conditional on a low-admin test, not just that membership is attractive.
   Answer first: What is the one sentence the board should remember about why this is the right first move?

THE HABIT TO BUILD
Make every key assumption earn its place. The weak habit is treating a plausible number as conservative because another adjacent number is higher. Exercise: for each decision-driving figure, write three lines underneath it: compared to what, what it means, and what the client should do differently if it is wrong.

WHAT THIS REVIEW COULD NOT JUDGE
I could not assess slide design, chart readability or visual hierarchy because the input is extracted text.
I could not verify the 2024 accounts, box-office data, funder letters or comparable pricing websites.
I could not judge whether 45 pounds is attractive to Client E's audience beyond the three comparable price points quoted.
I could not assess whether the member benefits are deliverable without seeing the current events calendar, partner commitments or staff workload.
I could not assess whether the 200 most engaged contacts are identifiable in the CRM or mailing-list data.

QUESTIONS WORTH ASKING THE TEAM
1. What evidence, if any, supports 8% paid conversion specifically, not engagement generally?
2. What is the expected coordinator time required in month one, month two and steady state?
3. What happens if the soft launch converts at 5% but creates more admin than expected?
4. Are the two members-only events incremental events or adapted from existing programming?
5. Are local partner discounts already agreed or still to be secured?

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
      { "fid": "f2", "short": "Capacity risk", "severity": "major",
        "issueType": "implementation",
        "dimension": "Risks, assumptions and uncertainty", "slides": [9] },
      { "fid": "f3", "short": "Late rationale", "severity": "minor",
        "issueType": "communication",
        "dimension": "Storyline and pyramid logic", "slides": [1, 2, 6] }
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
