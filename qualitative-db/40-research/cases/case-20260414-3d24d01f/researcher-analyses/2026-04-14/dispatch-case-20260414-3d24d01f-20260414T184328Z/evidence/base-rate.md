---
type: evidence_map
case_key: case-20260414-3d24d01f
dispatch_id: dispatch-case-20260414-3d24d01f-20260414T184328Z
research_run_id: 771da640-d96f-424f-b8af-1ae086b15ce5
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-19
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 70000 on April 19, 2026?"
driver: reliability
date_created: 2026-04-14
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-3d24d01f/researcher-analyses/2026-04-14/dispatch-case-20260414-3d24d01f-20260414T184328Z/personas/base-rate.md"]
tags: ["evidence-map", "base-rate", "btc"]
---

# Summary

The evidence nets to a high-probability Yes view, but with some discount from current spot because the contract is a narrow single-minute threshold event several days away.

## Question being evaluated

Will Binance BTC/USDT print a final close above 70000 for the 12:00 ET 1-minute candle on April 19, 2026?

## Current lean

Lean Yes.

## Prior / starting view

Given current market price near 0.89 and BTC trading materially above 70000, the outside-view prior started high but not near certainty because crypto can move several percent in days and the contract resolves on one specific minute.

## Evidence supporting the claim

- Binance live BTCUSDT ticker was about 74281 during the run.
  - direct
  - high weight
  - matters because the threshold is currently about 5.8% below spot
- Recent 1-minute Binance klines fetched during the run were all around 74250-74290.
  - direct
  - medium weight
  - matters because it confirms the current trading regime is not based on a stale last price
- Last 30 daily Binance closes had 15 closes above 70000, and the latest daily close was 74281.10.
  - direct/contextual
  - medium weight
  - matters because recent regime has moved back above threshold rather than hovering barely above it
- Polymarket rules specify Binance BTCUSDT noon ET 1-minute close and current market price around 0.89.
  - direct for rules, contextual for crowd view
  - medium weight
  - matters because the market already prices a high-probability Yes and the contract mapping is clear

## Evidence against the claim

- The contract resolves on a single minute close on April 19, not on current spot or average price.
  - direct from rules
  - high weight
  - matters because even a generally bullish week can fail on timing noise
- BTC daily closes over the last 30 days were above 70000 only about half the time.
  - direct/contextual
  - medium weight
  - matters because the threshold is not so low that historical frequency alone implies near-certainty
- Crypto can move more than 5% in a few days, which is enough to erase the current buffer.
  - contextual structural fact inferred from observed daily range and asset behavior
  - medium weight
  - matters because the remaining time window is several days, not several hours

## Ambiguous or mixed evidence

- The market's 89% price may partly reflect strong current spot and partly trader tendency to over-round short-horizon threshold events toward certainty.
- Binance API documentation supports timezone interpretation, but the market text references the Binance UI. This is probably not a real ambiguity, but it is worth noting.

## Conflict between inputs

There is little factual conflict. The main disagreement is weighting-based: whether current spot around 74.3k justifies near-90% confidence for a specific minute several days ahead.

## Key assumptions

- BTC stays in roughly the current trading regime through Sunday noon ET.
- No exchange-specific operational issue distorts the relevant Binance BTCUSDT minute candle.

## Key uncertainties

- Weekend volatility into the exact settlement minute
- Whether any fast macro or crypto-specific shock occurs before April 19 noon ET

## Disconfirming signals to watch

- Spot falling back below 72k or especially 71k before settlement
- Rising realized volatility into the weekend
- Any Binance-specific trading disruption near settlement time

## What would increase confidence

- BTC still trading comfortably above 72k late on April 18 or early April 19
- Continued minute-level stability on Binance

## Net update logic

The base-rate prior rises because current spot is comfortably above threshold and recent regime is supportive. It is capped below market certainty because the event is a single-minute print several days ahead, and recent 30-day history is not overwhelmingly above 70k.

## Suggested downstream use

Use as a synthesis input arguing that Yes is likely but the market may be mildly overconfident if other personas are also leaning heavily on current spot without discounting single-minute timing risk.