---
type: evidence_map
case_key: case-20260414-f6393095
dispatch_id: dispatch-case-20260414-f6393095-20260414T222237Z
research_run_id: 57dc8e44-4251-43d2-9e1f-c3a9cc26f3e8
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-70-000-on-april-17
question: "Will the price of Bitcoin be above $70,000 on April 17?"
driver: reliability
date_created: 2026-04-14
agent: Orchestrator
status: draft
confidence: medium-high
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-f6393095/researcher-analyses/2026-04-14/dispatch-case-20260414-f6393095-20260414T222237Z/personas/market-implied.md"]
tags: ["evidence-map", "btc", "polymarket"]
---

# Summary

Netting the direct evidence favors Yes and supports the market's high-probability view. The remaining uncertainty is mostly about short-horizon crypto volatility and the contract's exact venue/time-specific resolution rule, not about the current spot level being near the threshold.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17, 2026 have a final Close above $70,000?

## Current lean

Yes, high probability.

## Prior / starting view

Given the assigned market price of 0.935, the starting view was that the market likely saw the contract as mostly a question of whether BTC could avoid a roughly 6% drawdown over about 2.5 days.

## Evidence supporting the claim

- Binance live BTCUSDT around $74.1k.
  - Source: source note on Binance live price.
  - Why it matters: direct distance-to-threshold evidence from the governing exchange.
  - Direct or indirect: direct.
  - Weight: high.

- Polymarket ladder coherence around nearby strikes.
  - Source: source note on Polymarket event/API.
  - Why it matters: nearby strikes imply a reasonably smooth short-horizon distribution rather than a random mispricing at $70k.
  - Direct or indirect: direct for market state, indirect for true outcome.
  - Weight: medium-high.

- Limited time to resolution.
  - Source: Polymarket event/API timing and contract end date.
  - Why it matters: with only about 2.5 days left, a >$4k drawdown is possible but not base-case from current level.
  - Direct or indirect: indirect/contextual.
  - Weight: medium-high.

## Evidence against the claim

- Crypto can move 5%-6% in a short period.
  - Source: general market behavior inference; not modeled here with a full volatility dataset.
  - Why it matters: the current cushion is real but not untouchable.
  - Direct or indirect: contextual.
  - Weight: medium.

- The contract uses one exact minute close on one exchange.
  - Source: Polymarket resolution wording.
  - Why it matters: venue-specific print, volatility spike, or exchange anomaly could matter more than broader market averages.
  - Direct or indirect: direct for contract risk.
  - Weight: medium.

## Ambiguous or mixed evidence

- A simple cross-check from CoinGecko showed BTC near the same level as Binance, which is comforting but not independently decisive because the contract still settles on Binance only.

## Conflict between inputs

There is little hard conflict between the checked inputs. The main tension is between the market's very high confidence and the reality that single-minute crypto contracts remain exposed to short sharp downside moves.

## Key assumptions

- No major downside BTC shock before April 17 noon ET.
- No Binance-specific operational or print anomaly affecting the settlement minute.
- Market pricing around nearby ladder strikes remains broadly coherent.

## Key uncertainties

- Short-horizon volatility over the next ~2.5 days.
- Event risk not captured in the limited evidence sweep.
- Exact settlement-minute path dependence.

## Disconfirming signals to watch

- BTCUSDT falling quickly toward 72k or lower.
- Binance-specific issues near resolution.
- Nearby strike repricing that makes 70k look unusually rich versus the rest of the ladder.

## What would increase confidence

- Continued BTCUSDT stability above 73k into April 16-17.
- No Binance operational incidents.
- Consistent pricing across nearby ladder contracts as time decays.

## Net update logic

The evidence did not break the market prior; it mostly validated it. Live Binance price being more than $4k above the threshold made the market's 93.5% probability understandable, while the contract's single-minute Binance-specific nature justified keeping some residual discount versus near-certainty.

## Suggested downstream use

Use as forecast update and orchestrator synthesis input; little additional source collection appears likely to move the estimate by 5 points absent fresh price action or exchange-specific news.