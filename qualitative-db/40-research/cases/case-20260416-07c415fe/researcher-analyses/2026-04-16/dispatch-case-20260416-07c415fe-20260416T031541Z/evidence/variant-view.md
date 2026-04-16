---
type: evidence_map
case_key: case-20260416-07c415fe
dispatch_id: dispatch-case-20260416-07c415fe-20260416T031541Z
research_run_id: 05f95fe8-6350-4696-8c66-12fa7e0c022d
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: market-structure
entity: sol
topic: solana-above-80-on-april-19
question: "Will the Binance SOL/USDT 12:00 ET one-minute candle close above 80 on April 19, 2026?"
driver: operational-risk
date_created: 2026-04-15
agent: variant-view
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["sol", "solana"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-07c415fe/researcher-analyses/2026-04-16/dispatch-case-20260416-07c415fe-20260416T031541Z/personas/variant-view.md"]
tags: ["evidence-map", "threshold-market", "timestamp-risk"]
---

# Summary

The net evidence favors Yes because SOL is already trading above the threshold on the named venue, but the strongest credible disagreement with the market is about overconfidence, not direction. The exact-minute settlement mechanic and crypto volatility keep No meaningfully alive.

## Question being evaluated

Will the Binance SOL/USDT one-minute candle at 12:00 ET on 2026-04-19 have a final close above $80?

## Current lean

Lean Yes, but at a slightly lower probability than the market.

## Prior / starting view

Starting baseline was the market-implied probability from current_price 0.92, i.e. about 92% Yes.

## Evidence supporting the claim

- Binance-specific spot reference shows SOL/USDT around 85.29 on 2026-04-16.
  - Source: Binance API source note.
  - Why it matters: same venue and pair as settlement source.
  - Direct vs indirect: direct contextual evidence.
  - Weight: high.

- Recent Binance daily closes in the checked sample all remained above 80.
  - Source: Binance API source note.
  - Why it matters: suggests recent trading regime is already on the right side of the threshold.
  - Direct vs indirect: direct contextual evidence.
  - Weight: medium-high.

- CoinGecko independently shows SOL around 85.23 with positive 24h/7d/14d changes.
  - Source: CoinGecko source note.
  - Why it matters: confirms Binance is not obviously off-market and that short-horizon momentum is not currently bearish.
  - Direct vs indirect: indirect/contextual evidence.
  - Weight: medium.

## Evidence against the claim

- The market settles on one exact minute, not on an average price or daily close.
  - Why it matters: timestamp markets are more fragile than broad directional views.
  - Direct vs indirect: direct contract interpretation.
  - Weight: high.

- SOL’s recent 30d performance remains negative despite short-term stabilization.
  - Source: CoinGecko source note.
  - Why it matters: reminds us the asset can still move materially over a few days.
  - Direct vs indirect: indirect/contextual evidence.
  - Weight: medium.

- The cushion above the strike is only about $5.2-$5.3, roughly 6-7%.
  - Why it matters: this is meaningful, but not large enough to make a sub-10% failure probability absurd in crypto.
  - Direct vs indirect: inference from current spot and strike.
  - Weight: medium-high.

## Ambiguous or mixed evidence

- Short-term positive momentum supports Yes, but can also indicate a more crowded and fragile setup if broader crypto risk sentiment turns.

## Conflict between inputs

There is little factual conflict. The disagreement is weighting-based: how much probability to assign to exact-timestamp downside versus current above-threshold spot conditions.

## Key assumptions

- SOL remains above 80 into the April 19 noon ET settlement minute.
- Binance UI candle data will align with exchange API behavior closely enough that current venue-specific spot context is a valid lead indicator.

## Key uncertainties

- Weekend price action before April 19 noon ET.
- Whether a broader crypto drawdown emerges before settlement.
- Small venue-specific discrepancies at the exact minute that might matter when price is near the threshold.

## Disconfirming signals to watch

- SOL breaks below 82 and fails to recover.
- Broader crypto market sells off sharply into the resolution window.
- Binance SOL/USDT trades near 80 shortly before noon ET on April 19.

## What would increase confidence

- Another Binance check closer to settlement still showing SOL in the mid-80s or higher.
- Continued market-wide risk-on behavior without a sharp reversal.

## Net update logic

The main update is not that the market is wrong directionally. It is that the market may be slightly too confident for a narrow, timestamp-based crypto threshold contract. Direct venue-specific evidence supports Yes, but the exact settlement mechanic and residual volatility justify trimming probability below the market’s implied level.

## Suggested downstream use

- Orchestrator synthesis input.
- Decision-maker review focused on whether extreme-probability threshold markets are being priced too tightly relative to timestamp risk.
