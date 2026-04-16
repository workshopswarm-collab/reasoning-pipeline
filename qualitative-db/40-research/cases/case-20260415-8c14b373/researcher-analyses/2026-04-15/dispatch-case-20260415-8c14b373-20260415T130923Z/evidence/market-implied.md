---
type: evidence_map
case_key: case-20260415-8c14b373
dispatch_id: dispatch-case-20260415-8c14b373-20260415T130923Z
research_run_id: 71ccfc53-a2fe-4f74-84d7-4a67846b4892
analysis_date: 2026-04-15
persona: market-implied
domain: tech-ai
subdomain: benchmarks
entity:
topic: lm-arena-leadership-vs-contract-risk
driver: reliability
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["anthropic", "claude", "openai"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: ["Chatbot Arena / LM Arena text leaderboard", "claude-opus-4-6-thinking"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "leaderboard", "contract-interpretation"]
---

# Summary

The evidence currently nets to a high-probability YES view mainly because the named model appears to be current #1 on the exact leaderboard family used for settlement, with limited time left before the check. The main negative is that this is a future-timestamp resolution with possible rank volatility and a tie-sensitive contract.

## Question being evaluated

Will `claude-opus-4-6-thinking` occupy first place under the `Text Arena | Overall` leaderboard with style control off when checked on April 17, 2026 at 12:00 PM ET?

## Current lean

Lean YES, high probability but below the market.

## Prior / starting view

Starting from the market price, the default prior was that traders likely already knew the current leaderboard status and were mostly pricing persistence.

## Evidence supporting the claim

- LM Arena text leaderboard source note: current scrape shows `claude-opus-4-6-thinking` at #1 with score 1502±5.
  - Why it matters causally: this is the direct source family used to settle the market.
  - Direct or indirect: direct.
  - Weight: very high.
- Polymarket rules note: settlement depends only on the named table, score column, and future check time.
  - Why it matters causally: narrows the problem to leaderboard persistence rather than broad model reputation.
  - Direct or indirect: direct for contract interpretation.
  - Weight: very high.
- Short remaining time window before the scheduled check.
  - Why it matters causally: less time for a new model launch or rating update to displace the current leader.
  - Direct or indirect: indirect/contextual.
  - Weight: medium.

## Evidence against the claim

- The market resolves at a future timestamp, not now.
  - Why it matters causally: current leadership can change before settlement.
  - Direct or indirect: direct contract risk.
  - Weight: high.
- The observed score advantage is not enormous relative to leaderboard uncertainty / churn risk.
  - Why it matters causally: a modest shift or new row could alter first place.
  - Direct or indirect: indirect/contextual.
  - Weight: medium.
- Tiebreak risk may not favor `claude-opus-4-6-thinking` if another listed model reaches the same score and sorts earlier alphabetically.
  - Why it matters causally: contract wording can flip the winner even without a raw score deficit.
  - Direct or indirect: direct contract interpretation.
  - Weight: medium.

## Ambiguous or mixed evidence

- The current leaderboard extraction is strong for identifying the leader but weaker for cleanly reconstructing the full competitive set beneath it.
- Public model-launch cadence in frontier AI is fast enough that late surprises are possible, but no concrete displacing event was found in this pass.

## Conflict between inputs

There is little source conflict. The main issue is weighting: how much persistence risk remains between now and the check time.

## Key assumptions

- Current leaderboard leadership is real and maps cleanly to the listed market outcome.
- No competitor overtakes before the check.
- No tie emerges that changes the winner by alphabetical rule.

## Key uncertainties

- Leaderboard volatility over the final ~2 days.
- Whether any near-top competitor is closer than the parser-extracted context suggests.
- Low-probability source outage or fallback-resolution scenario.

## Disconfirming signals to watch

- Another public leaderboard check showing a different #1 model.
- A fresh high-profile model release entering directly near the top.
- Evidence of a tie or near tie with an alphabetically advantaged rival.

## What would increase confidence

- A cleaner manual or structured capture of the top few rows confirming the margin.
- Another leaderboard check closer to resolution still showing the same leader.
- Confirmation that the exact row name used by LM Arena matches the exact market outcome string without ambiguity.

## Net update logic

The market starts at an extreme YES probability because traders appear to be pricing current direct evidence from the governing leaderboard plus short-horizon persistence. I modestly downweight that confidence because the contract is time-specific, tie-sensitive, and not yet settled today.

## Suggested downstream use

- Orchestrator synthesis input.
- Forecast update with emphasis on persistence risk rather than on broad model-quality debate.
- Follow-up investigation shortly before resolution if the market remains live.