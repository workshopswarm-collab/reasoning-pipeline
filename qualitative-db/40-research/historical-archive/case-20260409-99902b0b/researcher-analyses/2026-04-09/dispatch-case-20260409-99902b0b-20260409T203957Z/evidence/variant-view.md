---
type: evidence_map
case_key: case-20260409-99902b0b
dispatch_id: dispatch-case-20260409-99902b0b-20260409T203957Z
research_run_id: eb480b52-1fbc-46c9-80db-5d83fa24e93b
analysis_date: 2026-04-09
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-10
question: "Will the Binance BTC/USDT 12:00 ET one-minute candle close on 2026-04-10 be above 70000?"
driver: operational-risk
date_created: 2026-04-09
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260409-99902b0b/researcher-analyses/2026-04-09/dispatch-case-20260409-99902b0b-20260409T203957Z/personas/variant-view.md"]
tags: ["evidence-map", "binance", "threshold-market", "verification"]
---

# Summary

The evidence nets to a high-probability YES, but the variant angle is that the market may still be somewhat overconfident because this is a single-candle, deadline-specific contract where one sharp risk-off move or Binance-specific operational discrepancy could still flip resolution.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET one-minute candle close on 2026-04-10 above 70,000?

## Current lean

YES, with high but not near-certain confidence.

## Prior / starting view

Starting baseline was the market-implied 88.5% YES from current_price 0.885.

## Evidence supporting the claim

- Direct Binance spot check showed BTCUSDT around 72,361.7.
  - direct source
  - matters because Binance is the governing resolution source
  - deserves very high weight
- Recent Binance 1-minute kline values were also clustered around 72.36k-72.39k.
  - direct source
  - matters because the contract resolves on a 1-minute candle close rather than broader daily averages
  - deserves high weight
- CoinGecko and Coinbase spot context were both near 72.38k.
  - indirect/contextual relative to settlement, but independent sanity checks
  - matters because they reduce concern that Binance is uniquely detached
  - deserves medium weight
- Time to resolution was short enough that absent a meaningful shock, the current cushion over 70k is material.
  - interpretive inference from direct price evidence
  - deserves medium weight

## Evidence against the claim

- BTC is volatile enough that a ~3% move lower within a day is plausible.
  - contextual market structure evidence rather than a single sourced datapoint here
  - deserves medium weight
- The contract is resolved by one exact Binance one-minute close at 12:00 ET, so path dependency is irrelevant and timing risk is concentrated.
  - direct rule interpretation
  - deserves high weight
- Small source-of-truth ambiguity remains between Binance API outputs and the website candle display referenced in rules, even though they should generally align.
  - operational/rules risk
  - deserves low-to-medium weight

## Ambiguous or mixed evidence

- Cross-venue consistency is supportive, but all spot venues are highly correlated; it helps sanity-check level rather than prove tomorrow’s noon close.

## Conflict between inputs

- No material factual conflict across checked sources.
- Main disagreement is weighting-based: how much downside volatility risk should be priced into a one-day threshold market that is already comfortably in the money.

## Key assumptions

- Current cushion above 70k is large enough to absorb ordinary volatility.
- Binance settlement display will align economically with accessible Binance market data.

## Key uncertainties

- Overnight macro or crypto-specific shock risk.
- Exact BTC level approaching the April 10 noon ET candle.
- Any exchange-specific anomalies at the governing source.

## Disconfirming signals to watch

- Binance BTCUSDT trading near 70.5k-71k on the morning of April 10.
- Broad crypto liquidation event.
- Binance-specific pricing or chart display discrepancy.

## What would increase confidence

- A fresh Binance price check shortly before 12:00 ET still showing BTC materially above 70k.
- No meaningful exchange-specific dislocations.

## Net update logic

The direct settlement-relevant evidence supports YES strongly because BTC is already above the threshold by more than trivial noise. The variant adjustment is that extreme market confidence may be a bit too high for a single-minute, deadline-specific contract where one downside impulse can dominate. That leaves a modestly lower probability than the strongest YES framing, but still clearly YES-leaning.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review only if other researchers are materially more bullish than the contract-risk framing here