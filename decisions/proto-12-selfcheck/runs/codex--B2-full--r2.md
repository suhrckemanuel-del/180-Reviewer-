REVIEW OF: final recommendation deck | MODE: deep | KEYS: SIGMA-7K/DELTA-3Q

BEFORE YOU USE THIS
1. Check the quotes. Every finding carries a verbatim quote and a location. Find each one in the deliverable yourself. It takes seconds. A quote you cannot find means that finding is discarded, not softened. Nothing is checking this but you.
2. There is no grade here, on purpose. This review does not say how ready the work is, because the same deliverable has been given two different answers on identical input. The findings below are the reliable part. Read them and make your own call.
3. This deliverable does not go to the client on this review alone, ever. A named human signs off on client work. That rule does not move.

Confidence in this review: High. Could change if: the full deck contains backup evidence on conversion benchmarks, staff workload or the 5% launch gate.
Weakest areas: Evidence quality, Analysis and insight, Risks, assumptions and uncertainty
Effort to close the findings below: 4 to 8 hours

WHAT WORKS
1. The recommendation is clear and early.
   Where: Slide 1
   Quote: "Client E should launch a paid membership scheme, starting with a single tier in the autumn."

2. The income-risk case is concrete and sourced.
   Where: Slide 3
   Quote: "Project grants are 80% of Client E's income (2024 accounts) and each is single-year."

3. The implementation plan has an owner, sequence and test point.
   Where: Slide 10
   Quote: "The Client E coordinator owns the launch. Month one: soft launch to 200 contacts. Month two: review conversion against the 8% target. Month three: full launch if the soft launch clears 5%."

WHAT TO FIX, IN ORDER

1. The success threshold is internally unclear: the deck says to review against 8% but launch at 5%. [High impact]
   Where: Slide 10
   Quote: "Month two: review conversion against the 8% target. Month three: full launch if the soft launch clears 5%."
   Why it costs the client: The board cannot tell whether 6% conversion means the pilot failed against target or succeeded enough to scale. That changes whether they proceed, redesign the offer or pause before spending scarce coordinator time.
   What to do: Separate the forecast assumption from the go/no-go threshold. Define what each number is for, what happens at 5% to 8% and what happens below 5%.
   Answer first: What exact pilot result would make the board launch, adapt or stop?

2. The 8% conversion assumption carries the financial case but is benchmarked to engagement, not to paid conversion. [High impact]
   Where: Slide 8
   Quote: "If 8% of the mailing list joins at 45 pounds, that is about 5,000 pounds in year one."
   Why it costs the client: The board is being asked to accept the revenue case before knowing whether 8% is a realistic paid-membership conversion rate. Event attendance proves engagement, but not willingness to pay for membership.
   What to do: Recast 8% as an explicit test assumption rather than a defensible forecast unless you can add a relevant comparator. Show sensitivity at lower conversion rates and say what minimum result still justifies launch.
   Answer first: What would year-one income look like at 3%, 5% and 8%, and which case still makes the launch worth the coordinator time?

3. The staff-capacity risk is named but not tested enough for a one-person operating constraint. [Moderate]
   Where: Slide 9
   Quote: "We assume the mailing list is accurate and that members-only events do not strain staff."
   Why it costs the client: The launch could succeed commercially but fail operationally if two events, partner discounts and member handling absorb the part-time coordinator. That would make the recommendation harder to execute than the deck implies.
   What to do: Add the operating model behind the soft launch: tasks, estimated hours, what gets deprioritised and which benefit can be cut first if capacity is tight.
   Answer first: How many coordinator hours does the soft launch require in month one and what work is displaced?

4. The member benefits are listed, but the deck does not show why these are the benefits most likely to convert. [Moderate]
   Where: Slide 7
   Quote: "Priority booking, two members-only events a year and a discount with local partners."
   Why it costs the client: If the offer is wrong, the conversion test may reject membership when only the package needed changing. The board needs to know whether the proposition matches what engaged contacts value.
   What to do: Link each benefit to evidence, even light evidence, or mark it as a hypothesis to test in the soft launch. Keep the package small enough to protect capacity.
   Answer first: What evidence says these three benefits matter more than alternatives such as donation recognition, free tickets or community access?

THE HABIT TO BUILD
Turn every assumption that drives the recommendation into a decision rule. The weak habit here is naming a test without making clear what result changes the action. Exercise: take the three most important numbers in the deck and write, for each, "if this is above X we do A, if it is between X and Y we do B, if it is below Y we do C."

WHAT THIS REVIEW COULD NOT JUDGE
I could not verify the 2024 accounts, box-office data, funder letters or public website comparisons.
I could not assess visual clarity, slide density or chart readability because only extracted text was provided.
I could not tell whether the full deck has backup analysis for the 8% assumption or coordinator workload.
I could not judge whether the proposed benefits match audience preferences beyond what the deck states.

QUESTIONS WORTH ASKING THE TEAM
1. Why is 5% enough to trigger full launch if 8% is the stated target?
2. What evidence, if any, supports 8% as a paid conversion rate rather than an engagement proxy?
3. What is the minimum year-one net benefit after coordinator time and event costs?
4. Which member benefit would be removed first if capacity becomes tight?
5. What would the team recommend if the 200-contact pilot converts at 6%?

HOW TO CHECK THIS FEEDBACK
Every point above quotes your own deliverable and says where. If you cannot find one of these quotes in your own work, that point is wrong. Drop it and say so. This review advises. A human decides, and nothing here goes to your client on its own.


=== PASTE-BACK RECORD ===

Fill the nulls once you have decided what to act on, then send this block back to whoever runs the reviewer. It is the only trace a chat review leaves, and the question it answers is which findings people actually keep. Two minutes.

Fill: capturedAt, model, deliverable.ref, lead.id, lead.vsByHand, quotesMissing, an action for every finding ("keep", "ask" or "cut", plus a cutReason when you cut), mustCatch, and your own readinessCall.lead with a one-line reason. cutReason is one of: wrong, not-an-issue, too-minor, duplicate, out-of-scope.

readinessCall.lead is your judgement, not the reviewer's. One of: Not ready for client review, Needs substantial revision, Needs targeted revision, Nearly ready with minor edits.

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
  "quoteCheck": { "status": "lead-eye-check", "quotesChecked": 7, "quotesMissing": null },
  "ai": {
    "findings": [
      { "fid": "f1", "short": "threshold unclear", "severity": "major",
        "issueType": "thinking",
        "dimension": "Analysis and insight", "slides": [10] },
      { "fid": "f2", "short": "conversion assumption", "severity": "major",
        "issueType": "evidence",
        "dimension": "Evidence quality", "slides": [8] },
      { "fid": "f3", "short": "capacity risk", "severity": "major",
        "issueType": "implementation",
        "dimension": "Risks, assumptions and uncertainty", "slides": [9] },
      { "fid": "f4", "short": "benefits evidence", "severity": "major",
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
