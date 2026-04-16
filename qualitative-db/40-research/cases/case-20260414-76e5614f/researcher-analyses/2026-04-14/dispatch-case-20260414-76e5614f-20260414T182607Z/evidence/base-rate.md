---
type: evidence_map
case_key: case-20260414-76e5614f
dispatch_id: dispatch-case-20260414-76e5614f-20260414T182607Z
research_run_id: 1a8b2872-c720-425a-a90c-12814eac4adf
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-17
question: "Will the price of Bitcoin be above $72,000 on April 17?"
driver: reliability
date_created: 2026-04-14
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-76e5614f/researcher-analyses/2026-04-14/dispatch-case-20260414-76e5614f-20260414T182607Z/personas/base-rate.md"]
tags: ["evidence-map", "btc", "base-rate"]
---

# Summary

Netting the evidence yields a moderate Yes lean. The market is not asking whether BTC is structurally strong over months; it is asking whether Binance BTCUSDT avoids closing below 72,000 in one specified minute on April 17 noon ET. Current spot is above that threshold by several percent, which matters more than long-run averages, but the short horizon is still long enough for a meaningful crypto drawdown.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17 have a final close above 72,000?

## Current lean

Lean Yes, but not at near-certainty.

## Prior / starting view

Outside-view prior started below the market because 72,000 had not been consistently safe in the most recent 30-60 day window.

## Evidence supporting the claim

- Live Binance BTCUSDT near 74,573 on 2026-04-14.
  - direct
  - high weight
  - matters because the market only requires price to stay above 72,000 at one future minute.
- Several recent daily closes above 72,000 after a late-March dip.
  - direct
  - medium-high weight
  - matters because it suggests the market has recently re-established the threshold zone.
- Recent hourly realized volatility usually well below the 3.45% downside needed to break the threshold from the checked price.
  - direct/contextual hybrid
  - medium weight
  - matters because it frames how large a move is needed over a short horizon.

## Evidence against the claim

- Only 6 of the last 30 daily closes and 8 of the last 60 daily closes were above 72,000.
  - direct
  - medium-high weight
  - matters because it shows the threshold is not deeply embedded in the recent regime.
- Crypto can move several percent on short notice, and settlement depends on one exact minute rather than a daily average.
  - contextual
  - medium weight
  - matters because path dependence and timing precision can punish a superficially comfortable spot cushion.
- Binance-specific settlement creates some exchange-specific operational and print risk at the margin.
  - direct from rules / contextual for impact
  - low-medium weight
  - matters because a one-minute exchange-specific close can diverge slightly from broader BTC perception.

## Ambiguous or mixed evidence

- Longer lookbacks are very supportive: 119 of last 180 daily closes and 304 of last 365 daily closes were above 72,000. This supports Yes in a broad bull-regime sense but may overstate relevance because the most recent 30-60 day regime has been weaker.

## Conflict between inputs

There is no hard factual conflict. The tension is weighting-based: whether to emphasize current spot cushion and recent recovery, or the fact that recent 30-60 day history still has more closes below 72,000 than above.

## Key assumptions

- Recent volatility regime persists without a fresh shock.
- Binance remains a clean operational settlement source.
- The current spot cushion remains materially informative by settlement.

## Key uncertainties

- Macro/crypto headlines before settlement
- Whether BTC spends the next two days consolidating above 72k or revisits the low-70k area
- Whether the exact noon ET minute prints anomalously on Binance

## Disconfirming signals to watch

- BTC loses 73k and cannot reclaim it
- A sharp downside move pushes Binance BTCUSDT near or below 72k before settlement
- Operational oddities on Binance around the relevant minute

## What would increase confidence

- Continued trading above 74k into April 16-17
- Another clean daily close above 72k
- Stable intraday behavior around noon ET on preceding days

## Net update logic

The starting outside-view prior was restrained because 72k has only recently been re-cleared after a stretch of weaker closes. The strongest update upward was not narrative but simple geometry: price is already above the threshold by several percent, and ordinary short-horizon realized moves are generally smaller than the required decline. That shifts the view to Yes, but not all the way to the market's low-80s because crypto downside tails remain very real over a two-day horizon.

## Suggested downstream use

Use as an orchestrator synthesis input and as an audit trail for why the base-rate lane was somewhat below, but still broadly aligned with, the market.