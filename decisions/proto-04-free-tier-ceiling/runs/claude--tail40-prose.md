{
  "findings": [
    {
      "title": "The 8% conversion assumption cannot be evaluated by the board",
      "diagnosis": "The recommendation depends on an 8% membership conversion rate, which the team states is 'our own assumption, not sourced.' The claim that this is 'conservative against the 32% attendance rate' provides no reasoning for how attendance predicts conversion. Without a source or logical connection, the board cannot assess whether this assumption is realistic.",
      "why": "The board cannot properly evaluate the recommendation if they cannot trust the financial projection. An unsourced assumption about a key revenue driver undermines the team's credibility and puts the decision at the mercy of board skepticism. The team themselves flagged this as 'the main thing to test,' signaling they are not confident in the assumption either.",
      "evidence": [
        {
          "slide": 8,
          "quote": "The 8% assumption is conservative against the 32% attendance rate and is the main thing to test."
        },
        {
          "slide": "Context",
          "quote": "The 8% conversion figure is our own assumption, not sourced."
        }
      ],
      "fix": "Provide either a sourced benchmark for membership conversion from comparable organizations or a logical derivation of the 8% figure. For example: 'Active attendees comprise roughly 32% of the 1,400-person list (450 people). We estimate that 8% of the full list will convert because active attendees convert at a higher rate, but not all are list members and not all list members are regular attendees.' If you cannot derive it logically, supplement with sensitivity analysis showing outcomes at 3%, 5%, 8%, and 10% conversion, making clear where breakeven sits and what the board should expect from the soft launch.",
      "severity": "major",
      "issueType": "evidence",
      "deliveryCritical": true
    },
    {
      "title": "The £5,000 revenue figure is never contextualized against Client E's budget or opportunity",
      "diagnosis": "The deck projects 'about 5,000 pounds in year one' from the membership program but never compares this to any benchmark that would let the board judge its significance. Is £5,000 material to Client E's budget, or minor noise? Is it a path to long-term income diversification, or a negligible supplement to grant funding?",
      "why": "The board cannot assess return-on-effort without knowing the financial context. A £5,000 opportunity might justify dedicating the part-time coordinator's time, or it might not, depending on the organization's scale and alternatives. The deck describes the financial outcome but does not analyze whether it is worth pursuing.",
      "evidence": [
        {
          "slide": 8,
          "quote": "If 8% of the mailing list joins at 45 pounds, that is about 5,000 pounds in year one."
        },
        {
          "slide": 3,
          "quote": "Project grants are 80% of Client E's income (2024 accounts)"
        }
      ],
      "fix": "Frame the £5,000 outcome in relation to Client E's existing income and implementation costs. For example: 'At 8% conversion, the membership program would generate £5,000 in year one, which represents X% of Client E's grant income and Y% of their total budget. This is material because [reason for why it matters], or this seeds a program we expect to grow to [X]% by year three.' Show whether the financial return justifies the coordinator's time and whether the program is a means to long-term diversification or a modest relationship-building tool.",
      "severity": "major",
      "issueType": "thinking",
      "deliveryCritical": true
    }
  ],
  "blockingIssue": {
    "rule": 4,
    "label": "Headline number the recommendation depends on is ungrounded: 8% membership conversion assumption has no source or logical derivation",
    "evidence": [
      {
        "slide": 8,
        "quote": "The 8% assumption is conservative against the 32% attendance rate and is the main thing to test."
      }
    ]
  },
  "readiness": "Needs targeted revision",
  "mainReason": "Rule 4 (ungrounded headline number) fires on the 8% conversion assumption. The board cannot evaluate the recommendation's financial case without understanding whether 8% is realistic, and no source or logic is provided.",
  "notAssessed": "We assume the funder letters confirming grant risk and the box-office data for attendance are current and on file. The organization's total budget, multi-year financial plan, and broader strategic context are unknown; with this, we could assess whether £5,000 is material and what a realistic conversion rate might be.",
  "questionsForLead": [
    "Can you provide a sourced benchmark for membership conversion from comparable arts organizations, or explain the logic for how 32% attendance yields an 8% conversion assumption?",
    "What does £5,000 represent as a percentage of Client E's annual operating budget, and does the team believe it justifies the coordinator's time commitment in year one?"
  ],
  "confidence": "High",
  "learningNote": {
    "habit": "When you flag an assumption as 'the main thing to test,' surface the reasoning you used to arrive at it, upfront.",
    "lesson": "For decision-driving assumptions (ones that change the recommendation or its value), provide either a sourced benchmark from comparables or a logical derivation. In this case, you would show either: (a) 'comparable orgs convert members at 5-10%, so our 8% is conservative,' or (b) 'Of the 450 regular attendees, we estimate 8% of the full list will convert because [logic].' This practice strengthens credibility and helps the board evaluate risk with you."
  },
  "diagnosticMean": 4.2,
  "resultLabel": "partial",
  "scores": [
    {
      "dimension": "1. Client decision usefulness",
      "checksPassed": 2,
      "checksTotal": 2,
      "score": 5
    },
    {
      "dimension": "2. Problem framing",
      "checksPassed": 2,
      "checksTotal": 2,
      "score": 5
    },
    {
      "dimension": "3. Storyline and pyramid logic",
      "checksPassed": 1,
      "checksTotal": 2,
      "score": 3
    },
    {
      "dimension": "4. Evidence quality",
      "checksPassed": 1,
      "checksTotal": 2,
      "score": 3
    },
    {
      "dimension": "5. Analysis and insight",
      "checksPassed": 1,
      "checksTotal": 2,
      "score": 3
    },
    {
      "dimension": "6. Recommendation specificity",
      "checksPassed": 2,
      "checksTotal": 2,
      "score": 5
    },
    {
      "dimension": "7. Feasibility and implementation",
      "checksPassed": 2,
      "checksTotal": 2,
      "score": 5
    },
    {
      "dimension": "8. Risks, assumptions, and uncertainty",
      "checksPassed": 1,
      "checksTotal": 2,
      "score": 3
    },
    {
      "dimension": "9. Slide-level communication",
      "checksPassed": 2,
      "checksTotal": 2,
      "score": 5
    },
    {
      "dimension": "10. Professionalism, tone, and confidentiality",
      "checksPassed": 2,
      "checksTotal": 2,
      "score": 5
    }
  ]
}