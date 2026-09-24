REVIEW OF: final recommendation deck | MODE: deep | KEYS: SIGMA-7K/DELTA-3Q

BEFORE YOU USE THIS
1. Check the quotes. Every finding carries a verbatim quote and a location. Find each one in the deliverable yourself. It takes seconds. A quote you cannot find means that finding is discarded, not softened. Nothing is checking this but you.
2. There is no grade here, on purpose. This review does not say how ready the work is, because the same deliverable has been given two different answers on identical input. The findings below are the reliable part. Read them and make your own call.
3. This deliverable does not go to the client on this review alone, ever. A named human signs off on client work. That rule does not move.

Confidence in this review: High. Could change if: the final deck has an appendix with conversion benchmarks, survey evidence or a capacity calculation not included in this extract.
Weakest areas: Evidence quality, Analysis and insight, Feasibility and implementation
Effort to close the findings below: 4 to 8 hours

WHAT WORKS
- The deck answers the client's decision directly and early. Slide 2: "Client E asked whether a paid membership could diversify income away from project grants. Our answer is yes, with a deliberately small start."
- The recommendation is scoped to the client's capacity constraint instead of proposing an overbuilt scheme. Slide 6: "Launching one tier at 45 pounds, rather than three tiers at once, keeps admin low and lets Client E learn before it scales."
- The implementation path has an owner, timing and a stage gate. Slide 10: "The Client E coordinator owns the launch. Month one: soft launch to 200 contacts. Month two: review conversion against the 8% target. Month three: full launch if the soft launch clears 5%."

WHAT TO FIX, IN ORDER

1. The 8% conversion assumption is treated as conservative without a valid comparator for membership conversion. [High impact]
   Where: Slide 8
   Quote: "The 8% assumption is conservative against the 32% attendance rate and is the main thing to test."
   Why it costs the client: The board may approve the scheme expecting about 5,000 pounds from a benchmark that does not measure the same behaviour. Attending an event and paying annually for membership are different commitments.
   What to do: Separate the attendance fact from the conversion assumption. Show what would make 8% reasonable: prior donor or attendee response, comparable membership conversion, or a clearly labelled scenario range with a downside case.
   Answer first: What evidence makes 8% the right planning case rather than just the team's chosen assumption?

2. The member benefits depend on staff capacity, but the deck asserts capacity and then calls it an assumption. [Moderate]
   Where: Slides 7 and 9
   Quote: "These use capacity Client E already has."
   Quote: "We assume the mailing list is accurate and that members-only events do not strain staff."
   Why it costs the client: The board could approve a benefits package that the part-time coordinator cannot deliver. That changes the practical recommendation from "launch this offer" to "launch only after simplifying or testing the benefits."
   What to do: Stress-test the benefits against the coordinator's time. Keep the principle of a small launch, but show the minimum viable benefit set and what gets removed if staff time is tight.
   Answer first: How many coordinator hours does the soft launch and two annual member events require, and where do those hours come from?

THE HABIT TO BUILD
Build the habit of matching every decision-driving number to the exact behaviour it measures. The weak habit here is using a nearby proxy as if it proved the assumption. Exercise: for each number in the recommendation, write "compared to what, so what, therefore what should the client do" in one line before it goes on a slide.

WHAT THIS REVIEW COULD NOT JUDGE
I could not verify the funder letters, accounts, box-office data or comparable pricing websites.
I could not assess slide design, chart readability or whether the visual hierarchy helps the board skim.
I could not judge whether two members-only events are operationally realistic without the coordinator's workload or event calendar.
I could not tell whether the wider deck has an appendix with sensitivity analysis or conversion evidence.

QUESTIONS WORTH ASKING THE TEAM
1. What is the strongest evidence for 8% conversion, beyond the 32% attendance rate?
2. What happens to year-one income if conversion is 2%, 5% and 8%?
3. How many hours will the coordinator spend on setup, communications, fulfilment and member events?
4. Which member benefit would be removed first if capacity is tighter than expected?
5. What exact result from the 200-contact soft launch would make the team recommend stopping?

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
      { "fid": "f1", "short": "conversion comparator", "severity": "major",
        "issueType": "evidence", "dimension": "Evidence quality", "slides": [8] },
      { "fid": "f2", "short": "capacity assumption", "severity": "major",
        "issueType": "implementation", "dimension": "Feasibility and implementation", "slides": [7, 9] }
    ]
  },
  "decisions": [
    { "fid": "f1", "action": null, "cutReason": null, "note": "" },
    { "fid": "f2", "action": null, "cutReason": null, "note": "" }
  ],
  "added": [],
  "mustCatch": null,
  "readinessCall": { "ai": null, "lead": null, "reason": "" },
  "sent": false
}

=== END. ===
