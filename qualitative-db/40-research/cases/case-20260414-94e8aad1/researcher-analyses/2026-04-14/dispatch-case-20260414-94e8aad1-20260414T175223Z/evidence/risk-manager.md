---
type: evidence_map
case_key: case-20260414-94e8aad1
dispatch_id: dispatch-case-20260414-94e8aad1-20260414T175223Z
research_run_id: b73d7c37-a0ca-4b44-9b81-707089044fae
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-70-000-on-april-16
question: "Will the price of Bitcoin be above $70,000 on April 16?"
driver: operational-risk
date_created: 2026-04-14
agent: risk-manager
status: draft
confidence: medium-high
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-94e8aad1/researcher-analyses/2026-04-14/dispatch-case-20260414-94e8aad1-20260414T175223Z/personas/risk-manager.md"]
tags: ["evidence-map", "btc", "resolution-risk"]
---

# Summary

The evidence nets to a strong Yes lean, but the residual risk is concentrated in contract mechanics rather than broad directional BTC sentiment.

## Question being evaluated

Whether the Binance BTC/USDT 1-minute candle labeled 12:00 ET on April 16 will have a final Close above 70,000.

## Current lean

Yes, with high probability but not near-certainty.

## Prior / starting view

Starting view was that a market priced around 95.95% Yes likely reflected BTC already trading materially above 70,000, but such an extreme price warranted stress-testing of timing and source-of-truth mechanics.

## Evidence supporting the claim

- Polymarket rules clearly define the resolution source and threshold.
  - Direct source.
  - Matters because it removes most interpretive ambiguity.
  - Weight: high.
- Binance spot and recent 1-minute kline closes were around 74.65k-74.70k on April 14.
  - Direct source relative to settlement venue.
  - Matters because current price is roughly $4.6k above threshold with only about two days left.
  - Weight: high.
- CoinGecko context check also showed BTC around 74.7k.
  - Contextual source.
  - Matters because it reduces concern that Binance reading was an isolated bad print.
  - Weight: medium.

## Evidence against the claim

- Settlement depends on one exact one-minute close at noon ET on April 16.
  - Direct contract-mechanics risk.
  - Matters because even a brief selloff or wick at the wrong minute could resolve No despite BTC spending most of the period above 70,000.
  - Weight: high.
- Source is Binance BTC/USDT specifically, not a generalized BTC/USD benchmark.
  - Direct contract-mechanics risk.
  - Matters because exchange-specific anomalies or pair-specific deviations could matter.
  - Weight: medium-high.
- Crypto can move several thousand dollars within a short window during risk-off episodes.
  - Contextual risk.
  - Matters because the current cushion is meaningful but not so large that a tail move is impossible.
  - Weight: medium.

## Ambiguous or mixed evidence

- The same narrow settlement rule both helps and hurts confidence: it is clear, but it concentrates risk in one timestamp and one venue.

## Conflict between inputs

No meaningful factual conflict was found. The main issue is weighting: whether the remaining single-minute path risk is underpriced by a 95.95% market.

## Key assumptions

- Binance remains operational and representative at settlement.
- BTC does not experience a sharp enough drawdown to threaten 70,000 by noon ET on April 16.
- No exchange-specific dislocation creates a misleading close at the target minute.

## Key uncertainties

- Near-term volatility into the exact settlement minute.
- Whether a transient wick on Binance could briefly break the threshold.
- Operational edge cases in Binance candle display versus API interpretation.

## Disconfirming signals to watch

- Binance BTCUSDT falling toward 71k or lower before April 16.
- Evidence of elevated exchange-specific instability or abnormal wicks.
- Broad crypto risk-off shock within the final 24 hours.

## What would increase confidence

- Continued Binance 1-minute closes above roughly 73k into April 15-16.
- No sign of Binance operational disruption near settlement.
- Narrow spread between Binance and broad BTC spot references.

## Net update logic

The evidence keeps the base case firmly on Yes, but pushes against treating the contract as almost locked. The main adjustment versus naive bullishness is not directional bearishness on BTC; it is acknowledging narrow timestamp, venue, and one-minute-close fragility.

## Suggested downstream use

- Orchestrator synthesis input.
- Decision-maker review for confidence calibration rather than directional reversal.