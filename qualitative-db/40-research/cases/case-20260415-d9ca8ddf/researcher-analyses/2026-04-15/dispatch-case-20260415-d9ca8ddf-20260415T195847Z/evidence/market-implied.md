---
type: evidence_map
case_key: case-20260415-d9ca8ddf
dispatch_id: dispatch-case-20260415-d9ca8ddf-20260415T195847Z
research_run_id: 18896f47-5aff-4a18-b913-2e3ce33bb79c
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-17
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-17 be above 72000?"
driver: reliability
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-d9ca8ddf/researcher-analyses/2026-04-15/dispatch-case-20260415-d9ca8ddf-20260415T195847Z/personas/market-implied.md"]
tags: ["evidence-map", "market-implied", "btc"]
---

# Summary

The market's extreme Yes pricing looks mostly justified by current Binance BTC/USDT spot trading well above the threshold, but not fully justified to the point of near-certainty because the contract resolves on a single future one-minute close.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET one-minute candle on April 17, 2026 close above 72,000?

## Current lean

Lean Yes with high but not extreme confidence.

## Prior / starting view

Starting baseline was the market-implied 91%-93% Yes probability.

## Evidence supporting the claim

- Binance spot price around 74,931 with 5-minute average around 75,031.
  - direct/context: direct current exchange data
  - why it matters: gives roughly 2.9k cushion above threshold with less than two days remaining
  - weight: high
- Recent daily closes around 74.4k, 74.1k, and 74.9k.
  - direct/context: direct recent exchange history
  - why it matters: suggests BTC is already trading in a regime above the threshold rather than needing a fresh breakout
  - weight: medium-high
- Contract wording is clean on exchange, pair, timestamp, and field.
  - direct/context: direct rules evidence
  - why it matters: reduces interpretive ambiguity and makes market pricing mostly a price-path problem
  - weight: medium

## Evidence against the claim

- BTC hit a recent daily low near 70,567 within the last several days.
  - direct/context: direct exchange history
  - why it matters: shows a move below 72k is plausible on this time horizon
  - weight: high
- The contract resolves on a single one-minute close at a precise timestamp.
  - direct/context: direct rules evidence
  - why it matters: timing-specific noise and short-lived selloffs matter more than for a daily close contract
  - weight: medium-high

## Ambiguous or mixed evidence

- The market page showed 93% while assignment metadata listed current_price 0.91; this is not a material contradiction, just evidence the market is moving within the same broad range.

## Conflict between inputs

No major factual conflict. The dispute is mainly weighting-based: how much probability mass should remain on a two-day drawdown below 72k into one exact minute.

## Key assumptions

- BTC remains in its recent above-threshold regime.
- No exchange-specific operational anomaly distorts Binance BTC/USDT settlement.

## Key uncertainties

- Near-term BTC volatility over the next ~44 hours.
- Whether macro or crypto-specific news triggers a sharp selloff before noon ET on April 17.

## Disconfirming signals to watch

- BTC losing 74k and then 73k with momentum.
- A widening Binance-specific dislocation.
- A sudden increase in realized volatility into the resolving window.

## What would increase confidence

- BTC holding above 74k into April 16 evening and April 17 morning ET.
- Independent confirmation from Binance UI or another data vendor that the expected 12:00 ET candle mapping aligns cleanly with 16:00 UTC.

## Net update logic

The market starts from a strong prior because spot is already comfortably above the threshold. The main reason not to fully accept 91%-93% is that the contract is point-in-time and BTC has shown enough recent downside range that a sub-72k print remains live.

## Suggested downstream use

Use as synthesis input supporting a modestly market-respecting stance: likely Yes, but not so certain that disconfirming timing risk should be ignored.