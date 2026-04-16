---
type: evidence_map
case_key: case-20260414-60e5e883
dispatch_id: dispatch-case-20260414-60e5e883-20260414T190542Z
research_run_id: 6eb83b2f-9214-4416-a989-6741c98e7c7f
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-70-000-on-april-17
question: "Will the price of Bitcoin be above $70,000 on April 17?"
driver: operational-risk
date_created: 2026-04-14
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-60e5e883/researcher-analyses/2026-04-14/dispatch-case-20260414-60e5e883-20260414T190542Z/personas/risk-manager.md"]
tags: ["evidence-map", "threshold", "timing-risk", "binance"]
---

# Summary

The evidence supports a Yes lean because BTC is currently well above 70k, but the market’s 93% confidence appears a bit too high given the contract’s narrow Binance-specific noon ET one-minute close and the remaining three-day path risk.

## Question being evaluated

Will Binance BTC/USDT record a final 12:00 ET one-minute candle close above 70,000 on April 17, 2026?

## Current lean

Lean Yes, but with less confidence than the market.

## Prior / starting view

Starting view was that a 93% market price likely embeds either a very large spot cushion or a very short time-to-resolution, so the main task was to test whether hidden timing/venue risk was being ignored.

## Evidence supporting the claim

- Binance ticker check showed BTCUSDT around 74,163.
  - direct
  - high causal relevance because the contract resolves on Binance BTC/USDT
  - deserves substantial weight
- Recent Binance 1-minute klines also closed in the 74.2k-74.3k area.
  - direct
  - useful because the contract uses a 1-minute candle close, matching the basic data structure
  - deserves substantial weight
- CoinGecko BTC/USD around 74,274 broadly corroborated market level.
  - indirect/contextual
  - useful for independent sanity check that Binance is not showing an isolated odd print
  - deserves moderate weight

## Evidence against the claim

- The contract resolves on one exact minute, not on average daily trading or end-of-day level.
  - direct contract interpretation risk
  - high causal relevance because a brief move below 70k at the exact resolution minute would settle No
- Roughly 6% cushion over three days is meaningful but not enormous for BTC.
  - indirect / scenario-based
  - medium weight because crypto can move several percent quickly
- The market is at an extreme implied probability, which raises the bar for verification and increases sensitivity to underpriced tail paths.
  - interpretive
  - medium weight

## Ambiguous or mixed evidence

- Binance being the governing source is helpful because direct data is available, but it also concentrates exchange-specific operational and candle-display risk into one venue.

## Conflict between inputs

No major factual conflict. The main disagreement is weighting-based: whether current spot cushion justifies a 93% Yes probability versus a still-high but lower estimate due to path/timing risk.

## Key assumptions

- Binance spot remains representative enough through April 17.
- No major shock drives BTC below 70k near the noon ET resolution minute.
- The current interpretation of the noon ET candle timing is correct.

## Key uncertainties

- Short-horizon BTC volatility over the next three days.
- Any macro or crypto-specific shock before resolution.
- Exchange-specific dislocation at the exact settlement minute.

## Disconfirming signals to watch

- BTC losing the 72k area and compressing the buffer above 70k.
- Rising Binance-specific divergence versus broader spot prices.
- Clarification showing an unexpected timezone/candle mapping issue.

## What would increase confidence

- BTC holding comfortably above 73k-74k into late April 16 and early April 17.
- Additional Binance checks showing no venue-specific anomalies.

## Net update logic

The direct exchange data supports a clear Yes lean, but the contract structure prevents treating current spot alone as near-certain evidence. The market appears directionally right but somewhat too confident.

## Suggested downstream use

- orchestrator synthesis input
- decision-maker review