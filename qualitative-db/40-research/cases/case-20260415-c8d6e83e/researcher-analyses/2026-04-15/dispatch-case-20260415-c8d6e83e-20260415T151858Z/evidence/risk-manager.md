---
type: evidence_map
case_key: case-20260415-c8d6e83e
dispatch_id: dispatch-case-20260415-c8d6e83e-20260415T151858Z
research_run_id: 616327f5-a7af-4e94-b562-c23a949e04c4
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: btc-above-68k-april-20-risk-netting
question: "Will the Binance BTC/USDT 12:00 ET one-minute candle close above 68000 on April 20, 2026?"
driver: operational-risk
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-c8d6e83e/researcher-analyses/2026-04-15/dispatch-case-20260415-c8d6e83e-20260415T151858Z/personas/risk-manager.md"]
tags: ["evidence-map", "btc", "risk-manager"]
---

# Summary

The evidence still leans clearly to Yes because BTC is materially above the threshold, but the market's near-certainty likely compresses real path and resolution mechanics risk too aggressively.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-20 have a final close above 68,000?

## Current lean

Lean Yes, but less confidently than the market.

## Prior / starting view

Starting view was that a spot level above 74k should make Yes highly likely, but an extreme 95.5% market demanded a check on narrow settlement mechanics and one-minute path risk.

## Evidence supporting the claim

- Binance spot ticker shows BTCUSDT around 74,044 on 2026-04-15.
  - Source: Binance API source note.
  - Why it matters causally: creates a large current cushion over 68k.
  - Direct or indirect: direct for current state, indirect for April 20 settlement.
  - Weight: high.

- Recent Binance 1-minute candles are clustered around 74.1k and timestamp cleanly into ET minute boundaries.
  - Source: Binance API source note.
  - Why it matters causally: supports both current price strength and mechanical clarity on the relevant settlement interval.
  - Direct or indirect: direct for source mechanics and current price behavior.
  - Weight: high.

- Polymarket pricing at ~95.5% indicates broad consensus that current price buffer is substantial relative to the threshold.
  - Source: Polymarket contract and pricing source note.
  - Why it matters causally: market baseline reflects that a >8% drop in a few days is not the base case.
  - Direct or indirect: indirect/contextual.
  - Weight: medium.

## Evidence against the claim

- The contract is narrow: one exchange, one trading pair, one exact ET minute, one final close field.
  - Source: Polymarket contract and pricing source note.
  - Why it matters causally: many ways exist for a broadly bullish BTC view to still miss this exact resolution condition.
  - Direct or indirect: direct for contract risk.
  - Weight: high.

- A roughly 6k buffer can disappear in crypto on multi-day horizons without a structural thesis break.
  - Source: inference from current threshold distance plus asset class volatility; not a separate direct source.
  - Why it matters causally: this is the main hidden assumption under a 95%+ price.
  - Direct or indirect: contextual.
  - Weight: medium-high.

- Binance-specific operational or venue dislocation risk is small but not zero, and matters more here than in a broad price question.
  - Source: contract structure and Binance-as-sole-source setup.
  - Why it matters causally: venue-specific prints or data issues can decide the market.
  - Direct or indirect: contextual.
  - Weight: medium.

## Ambiguous or mixed evidence

- CoinGecko confirms Bitcoin remains a major, liquid benchmark asset, but this is mostly background context and does little to resolve the exact April 20 noon candle question.

## Conflict between inputs

There is no hard factual conflict. The main tension is weighting-based: current spot and market pricing strongly support Yes, while the risk lens says the market may still be overconfident given the narrow settlement mechanics.

## Key assumptions

- BTC retains enough price buffer into April 20 noon ET.
- Binance BTC/USDT remains a representative, orderly venue at settlement.
- No sharp downside shock occurs close enough to settlement to overwhelm the current cushion.

## Key uncertainties

- Short-horizon BTC realized volatility over the next five days.
- Whether Binance-specific microstructure creates noise near settlement.
- Whether the price buffer remains wide or compresses materially before April 20.

## Disconfirming signals to watch

- BTC moving back toward 70k or below.
- A spike in intraday downside volatility.
- Any Binance outage, market-data discrepancy, or unusual venue divergence.

## What would increase confidence

- BTC still holding comfortably above 72k-74k into April 19-20.
- Independent confirmation that Binance front-end candle display and API output remain aligned at the relevant minute.

## Net update logic

The evidence kept the directional Yes lean intact because spot is still well above the threshold, but the resolution-mechanics audit reduced confidence versus the market. What mattered most was not a new bearish fact; it was the realization that the market is pricing almost no room for ordinary crypto path risk in a single-minute settlement contract.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review