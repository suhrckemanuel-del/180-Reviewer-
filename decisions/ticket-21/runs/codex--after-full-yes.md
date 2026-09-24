REVIEW OF: final recommendation deck | MODE: deep
ATTEMPT ON RECORD: "My own read first: I think the weakest part is that we never say what the client should actually do on Monday morning."

BEFORE YOU USE THIS
1. Check the quotes. Every finding carries a verbatim quote and a location. Find each one in the deliverable yourself. It takes seconds. A quote you cannot find means that finding is discarded, not softened. Nothing is checking this but you.
2. There is no grade here, on purpose. This review does not say how ready the work is, because the same deliverable has been given two different answers on identical input. The findings below are the reliable part. Read them and make your own call.
3. This deliverable does not go to the client on this review alone, ever. A named human signs off on client work. That rule does not move.

Confidence in this review: High. Could change if: the source deck contains conversion benchmarks, capacity arithmetic or decision rules not present in the extracted text.
Weakest areas: Evidence quality, Analysis and insight, Feasibility and implementation
Effort to close the findings below: 6 to 10 hours

WHAT WORKS

- The top-line decision is explicit and appears early.
  Where: Slide 2
  Quote: "Our answer is yes, with a deliberately small start."

- The income problem is quantified and traced to named internal evidence.
  Where: Slide 3
  Quote: "Project grants are 80% of Client E's income (2024 accounts) and each is single-year."

- The recommendation uses a pilot before committing to a full launch.
  Where: Slide 9
  Quote: "A soft launch to the most engaged 200 contacts tests both before the full launch."

WHAT TO FIX, IN ORDER

1. The deck gives the board two incompatible thresholds for moving from pilot to full launch. [High impact]
   Where: Slide 10
   Quote 1: "Month two: review conversion against the 8% target."
   Quote 2: "Month three: full launch if the soft launch clears 5%."
   Why it costs the client: A 6% result would trigger full launch under the 5% rule but fail the 8% target, so the coordinator could take opposite actions from the same pilot result.
   What to do: Define one decision framework. Distinguish the target from the minimum threshold and specify the action for results below, between and above them.
   Answer first: If the pilot converts 6% of contacts, does Client E launch, revise the offer or stop?

2. The conversion case calls 8% conservative using attendance as if it were a membership benchmark, so the financial case cannot yet support the launch decision. [High impact]
   Where: Slide 8
   Quote 1: "If 8% of the mailing list joins at 45 pounds, that is about 5,000 pounds in year one."
   Quote 2: "The 8% assumption is conservative against the 32% attendance rate and is the main thing to test."
   Why it costs the client: The board could scale a scheme whose demand and net contribution are unknown. Attendance and paid membership are different behaviours, while 5,000 pounds of gross revenue is not compared with delivery cost or a minimum worthwhile contribution.
   What to do: Present 8% as a testable hypothesis rather than a conservative estimate. Add conversion scenarios and compare their net contribution with a break-even or minimum-value threshold. Use paid-membership evidence if available.
   Answer first: What result would make membership worthwhile after benefit costs and coordinator time?

3. The deck asserts that the member offer fits existing capacity but does not show how the pilot will test staff strain. [High impact]
   Where: Slides 7 and 9
   Quote 1: "These use capacity Client E already has."
   Quote 2: "We assume the mailing list is accurate and that members-only events do not strain staff."
   Why it costs the client: With one part-time coordinator and no budget for new staff, unmeasured workload could force the board to narrow the benefits, delay the scheme or abandon it after launch.
   What to do: Estimate the incremental tasks and hours for each benefit. During the pilot, measure actual administration time and set a capacity threshold that triggers launch, redesign or cancellation.
   Answer first: How many coordinator hours per month can membership consume without displacing existing work?

THE HABIT TO BUILD

Turn every major assumption into a decision rule. The weak habit is naming something as an assumption or target without connecting the measured result to an action. As an exercise, build a one-page table for the pilot with each assumption, its evidence, the measurement method, the threshold and the resulting decision.

WHAT THIS REVIEW COULD NOT JUDGE

The visual hierarchy and layout because only extracted text was provided.
Whether the three comparables are genuinely similar to Client E.
Whether any comparable publishes membership conversion or retention data.
The accuracy and engagement quality of the 1,400-contact mailing list.
The actual staff hours, event costs and partner-management workload.
Whether 8% is plausible for this audience without relevant conversion evidence.

QUESTIONS WORTH ASKING THE TEAM

1. Which single threshold governs the full-launch decision?
2. What evidence makes 8% plausible for paid membership rather than event attendance?
3. What is the minimum net income that would justify running the scheme?
4. What staff workload will the pilot measure and what result would stop or redesign the launch?
5. What is the coordinator's first concrete action on Monday morning?

HOW TO CHECK THIS FEEDBACK

Every point above quotes your own deliverable and says where. If you cannot find one of these quotes in your own work, that point is wrong. Drop it and say so. This review advises. A human decides, and nothing here goes to your client on its own.

=== PASTE-BACK RECORD ===

Fill the nulls once you have decided what to act on, then send this block back to whoever runs the reviewer. It is the only trace a chat review leaves, and the question it answers is which findings people actually keep. Two minutes.

Fill: capturedAt, model, deliverable.ref, lead.id, lead.vsByHand, quotesMissing, an action for every finding ("keep", "ask" or "cut", plus a cutReason when you cut), mustCatch, and your own readinessCall.lead with a one-line reason. cutReason is one of: wrong, not-an-issue, too-minor, duplicate, out-of-scope.

readinessCall.lead is your judgement, not the reviewer's. It has none.

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
  "lead": {
    "id": null,
    "secondsOnTask": null,
    "vsByHand": null
  },
  "quoteCheck": {
    "status": "lead-eye-check",
    "quotesChecked": 9,
    "quotesMissing": null
  },
  "ai": {
    "findings": [
      {
        "fid": "f1",
        "short": "Conflicting launch thresholds",
        "severity": "critical",
        "issueType": "implementation",
        "dimension": "Feasibility and implementation",
        "slides": [10]
      },
      {
        "fid": "f2",
        "short": "Unsupported conversion case",
        "severity": "major",
        "issueType": "evidence",
        "dimension": "Evidence quality",
        "slides": [8]
      },
      {
        "fid": "f3",
        "short": "Untested capacity claim",
        "severity": "major",
        "issueType": "implementation",
        "dimension": "Feasibility and implementation",
        "slides": [7, 9]
      }
    ]
  },
  "decisions": [
    {
      "fid": "f1",
      "action": null,
      "cutReason": null,
      "note": ""
    },
    {
      "fid": "f2",
      "action": null,
      "cutReason": null,
      "note": ""
    },
    {
      "fid": "f3",
      "action": null,
      "cutReason": null,
      "note": ""
    }
  ],
  "added": [],
  "mustCatch": null,
  "readinessCall": {
    "ai": null,
    "lead": null,
    "reason": ""
  },
  "sent": false
}

=== END. ===
