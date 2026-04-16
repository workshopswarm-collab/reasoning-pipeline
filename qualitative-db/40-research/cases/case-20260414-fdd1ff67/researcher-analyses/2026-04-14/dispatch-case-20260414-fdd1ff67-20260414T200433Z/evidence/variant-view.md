---
type: evidence_map
case_key: case-20260414-fdd1ff67
dispatch_id: dispatch-case-20260414-fdd1ff67-20260414T200433Z
research_run_id: ca8bc1f5-e9c1-4900-a07d-ad70e7fb19df
analysis_date: 2026-04-14
persona: variant-view
domain: sports
subdomain: football
entity:
topic: "draw-market pricing vs contract ambiguity"
question: "Will Al Qadisiyah Saudi Club vs. Al Shabab Saudi Club end in a draw?"
driver:
date_created: 2026-04-14
agent: Orchestrator
status: draft
confidence: medium-low
conflict_status: active
action_relevance: high
related_entities: []
related_drivers: []
proposed_entities: ["al-qadsiah-fc", "al-shabab-club-riyadh"]
proposed_drivers: ["football-match-outcome-pricing", "market-contract-surface-integrity"]
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "variant-view", "draw-market", "source-of-truth"]
---

# Summary

The cleanest variant view is not a football-tactics edge; it is that the market as assigned looks overconfident and possibly malformed. A normal top-flight football draw price at 0.76 would be extraordinary, and the fetched Polymarket contract text appears to describe a different proposition entirely.

## Question being evaluated

Will Al Qadisiyah Saudi Club vs. Al Shabab Saudi Club end in a draw?

## Current lean

Lean against treating 0.76 as a trustworthy draw probability. Conditional on the assignment title being the intended proposition, my lean is that the true draw probability is materially lower.

## Prior / starting view

Starting view was that the market probably reflected a straightforward sports-outcome price. After review, the more material issue is contract-surface mismatch rather than ordinary football handicapping.

## Evidence supporting the claim

- Polymarket fetch shows the governing surface is a standard 90-minute football market with official-stat settlement rules.
  - directness: direct for settlement mechanics
  - weight: high
- The fetched Polymarket contract text says YES if **Al Qadisiyah wins**, not if the match ends in a draw.
  - directness: direct for ambiguity / mismatch
  - weight: very high
- In ordinary football pricing, a 76% draw probability would be highly unusual, making stale/mislabeled framing a more credible explanation than a genuine consensus draw number.
  - directness: indirect / base-rate reasoning
  - weight: medium

## Evidence against the claim

- The runtime assignment consistently labels the market as a draw market, which could mean the assignment metadata is correct and the fetched page text is the outlier.
  - directness: direct from assignment context, but not an external source
  - weight: high
- I did not obtain a clean independent sportsbook or fixture page with usable draw odds during this run.
  - directness: direct limitation of evidence collection
  - weight: medium-high

## Ambiguous or mixed evidence

- Wikipedia league/team context confirms the clubs and league context are real, but does not settle the exact proposition or provide direct pricing context.

## Conflict between inputs

- Main conflict: assignment title says **draw**; fetched market contract text says **Qadisiyah win**.
- Type: factual / contract-interpretation conflict.
- What would resolve it: a second clean market-surface retrieval for the same slug, or controller clarification.

## Key assumptions

- The intended market proposition is the assignment title rather than the fetched market-body text.
- A normal football base rate is relevant enough to reject a 76% draw price absent extraordinary evidence.

## Key uncertainties

- Whether the Polymarket slug/page fetch is attached to the intended contract.
- Whether there is hidden contextual information (for example, a special market grouping or display bug) explaining the mismatch.

## Disconfirming signals to watch

- Verified market metadata showing this really is a draw market priced near 0.76.
- Independent sportsbook or exchange pricing converging near that same level.

## What would increase confidence

- A clean independent odds screen or exchange page for the exact fixture.
- A second authoritative Polymarket/API source confirming contract wording.

## Net update logic

What mattered most was not team form but the mismatch between assignment framing and fetched contract text. That mismatch makes the apparent 76% draw consensus look fragile. I therefore downweight the raw market price and adopt a materially lower draw estimate, while also reducing confidence because the contract surface itself is ambiguous.

## Suggested downstream use

- Orchestrator synthesis input
- decision-maker review
- follow-up investigation into contract labeling / market metadata
