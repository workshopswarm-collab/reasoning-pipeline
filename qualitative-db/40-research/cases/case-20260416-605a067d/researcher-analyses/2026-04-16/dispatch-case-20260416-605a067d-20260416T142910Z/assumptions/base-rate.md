---
type: assumption_note
case_key: case-20260416-605a067d
research_run_id: 0bea9a8d-3bf2-4b6a-9261-3cc4d510709b
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: short-dated-price-thresholds
entity: ethereum
topic: "short-horizon ETH buffer versus fixed noon threshold"
question: "Will the Binance ETH/USDT 1-minute candle for 12:00 ET on April 17 close above 2200?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: "<48h"
related_entities: ["binance", "ethereum"]
related_drivers: ["operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-605a067d/researcher-source-notes/2026-04-16-base-rate-binance-and-reference-prices.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-605a067d/researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/personas/base-rate.md"]
tags: ["assumption-note", "eth", "binance", "noon-close", "threshold"]
dispatch_id: dispatch-case-20260416-605a067d-20260416T142910Z
---

# Assumption

ETH will not suffer a sustained downside move of roughly 4% or more on Binance before the April 17 12:00 ET 1-minute candle closes.

## Why this assumption matters

My outside-view estimate is mostly a hazard-rate judgment about how often a major crypto asset already trading materially above a threshold remains above that threshold one day later at a fixed daytime timestamp.

## What this assumption supports

- A Yes-leaning probability above 80%.
- Rough agreement with a bullish market, though somewhat below the market's implied confidence.
- The view that ordinary short-horizon variance is the main remaining risk, rather than contract-mechanics ambiguity.

## Evidence or logic behind the assumption

- ETH is currently around 2295 on Binance and nearby venues, giving about a 95-dollar buffer over the threshold.
- Cross-venue spot alignment suggests the price level is not a Binance-only anomaly.
- For a highly liquid major crypto asset, a move of that size in roughly one day is possible but not the modal outcome absent a fresh adverse catalyst.

## What would falsify it

- A meaningful broad crypto risk-off move before noon ET tomorrow.
- An ETH-specific negative catalyst that pushes Binance ETH/USDT back below 2200.
- Evidence that Binance-specific market structure is behaving unusually relative to other major venues.

## Early warning signs

- ETH losing the 2250 area across major venues.
- Sharp Bitcoin-led selloff or macro shock during U.S. hours.
- Binance trading materially weaker than Coinbase/Kraken into the resolution window.

## What changes if this assumption fails

The case flips from a comfortable Yes buffer to a live coin-flip or No-leaning setup, because this contract cares about one exact minute close rather than the broader daily average.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260416-605a067d/researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/personas/base-rate.md