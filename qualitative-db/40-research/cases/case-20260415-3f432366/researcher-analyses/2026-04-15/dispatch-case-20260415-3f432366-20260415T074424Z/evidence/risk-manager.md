---
type: evidence_map
case_key: case-20260415-3f432366
dispatch_id: dispatch-case-20260415-3f432366-20260415T074424Z
research_run_id: 6d792eeb-7534-425f-91be-1cb9896b9436
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-17
question: "Will the price of Bitcoin be above $72,000 on April 17?"
driver: operational-risk
date_created: 2026-04-15
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-3f432366/researcher-analyses/2026-04-15/dispatch-case-20260415-3f432366-20260415T074424Z/personas/risk-manager.md"]
tags: ["evidence-map", "btc", "threshold-market", "settlement-risk"]
---

# Summary

This market is a short-horizon threshold test with a favorable current spot backdrop for Yes, but with meaningful timing and threshold fragility that makes very high confidence hard to justify.

## Question being evaluated

Will Binance BTC/USDT print a final 1-minute candle close strictly above 72,000 at 12:00 ET on April 17, 2026?

## Current lean

Lean Yes, but with lower confidence than the market price implies.

## Prior / starting view

Starting view was that a 74.5% market price might be plausible if BTC were comfortably above the strike with stable momentum, but likely too confident if the cushion were only a couple percent.

## Evidence supporting the claim

- Current Binance spot is around 73.6k, above the strike by roughly 1.6k or a bit above 2%.
  - source: Binance ticker endpoints
  - causal relevance: less price appreciation is needed; BTC mainly needs to avoid a modest drawdown by settlement
  - direct/indirect: indirect contextual evidence
  - weight: high

- Recent sampled Binance 1-minute closes remained in the 73.5k-73.6k zone.
  - source: Binance klines endpoint
  - causal relevance: shows immediate microstructure above the strike rather than a one-off spike
  - direct/indirect: indirect contextual evidence, but exchange-consistent with settlement source
  - weight: medium

- CoinGecko independently cross-checks the broader BTC spot level around 73.6k.
  - source: CoinGecko simple price endpoint
  - causal relevance: reduces concern that Binance spot snapshot was anomalous
  - direct/indirect: indirect contextual evidence
  - weight: medium

## Evidence against the claim

- The contract is not "BTC above 72k sometime that day"; it is one exact Binance minute close at noon ET.
  - source: Polymarket rules
  - causal relevance: timing risk can defeat an otherwise broadly correct directional thesis
  - direct/indirect: direct contract evidence
  - weight: high

- BTC was down about 1.16% over the prior 24 hours during collection, and the 24h low was 73,514, not far from current spot.
  - source: Binance 24h ticker
  - causal relevance: negative momentum plus thin cushion means ordinary volatility could still push price below 72k by settlement
  - direct/indirect: indirect contextual evidence
  - weight: high

- The cushion above 72k is modest for BTC over a roughly two-day horizon.
  - source: net inference from current spot versus strike and observed range
  - causal relevance: market may be overpricing confidence rather than direction
  - direct/indirect: interpretive
  - weight: high

## Ambiguous or mixed evidence

- Binance-specific settlement is helpful because Binance data is directly observable now, but it also creates exchange-specific operational and print risk.
- CoinGecko corroborates general spot but does not resolve the exact settlement mechanism.

## Conflict between inputs

There is little direct factual conflict. The main conflict is between the market's confidence level (about 74.5%) and the risk-manager interpretation that threshold-plus-timing fragility deserves a discount.

## Key assumptions

- Current spot is informative for the April 17 noon ET minute close.
- No major crypto volatility shock occurs before settlement.
- Binance remains a reliable and representative settlement venue at the relevant time.

## Key uncertainties

- Short-horizon BTC realized volatility over the next ~2 days.
- Whether selling pressure continues and erodes the 72k cushion.
- Whether Binance-specific print behavior diverges materially from broader BTC spot near settlement.

## Disconfirming signals to watch

- BTC/USDT trading near or below 72.5k on April 16 or early April 17.
- A sharp risk-off move in crypto that expands downside range.
- Any Binance market data or UI irregularity near the settlement window.

## What would increase confidence

- BTC holding above roughly 74k into April 16-17.
- Reduced realized intraday volatility and repeated rejection of moves toward 72k.
- Another independent market-data check confirming similar spot and stable liquidity closer to settlement.

## Net update logic

The evidence supports Yes directionally because spot is already above the threshold and the contract does not require a rally. But the exact-minute close condition and only modest price cushion make the market's confidence look a bit rich. So the net is not "No"; it is "Yes, but with underappreciated path and timing fragility."

## Suggested downstream use

Use as orchestrator synthesis input and forecast calibration input, especially to prevent overweighting the current Yes favorite price as if the contract were a looser end-of-day settlement.