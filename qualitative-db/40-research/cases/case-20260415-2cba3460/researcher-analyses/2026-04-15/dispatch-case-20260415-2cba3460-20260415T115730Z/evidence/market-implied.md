---
type: evidence_map
case_key: case-20260415-2cba3460
dispatch_id: dispatch-case-20260415-2cba3460-20260415T115730Z
research_run_id: 9774bb24-9aa8-41be-a493-88d9f4739b6f
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-72-000-on-april-16
question: "Will the price of Bitcoin be above $72,000 on April 16?"
driver: reliability
date_created: 2026-04-15
agent: market-implied
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-2cba3460/researcher-analyses/2026-04-15/dispatch-case-20260415T115730Z/personas/market-implied.md"]
tags: ["evidence-map", "bitcoin", "binance"]
---

# Summary

The evidence currently supports a pro-market lean: BTC is already materially above the strike on the governing Binance venue, contract mechanics are straightforward, and the main remaining risk is a short-horizon downside move before the exact noon ET resolution minute.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle labeled 12:00 ET on Apr 16 close above 72,000?

## Current lean

Lean Yes, with high but not near-certainty confidence.

## Prior / starting view

Starting view was that an 88.5% market price deserved respect because the strike is below current spot, but the narrow timing and exchange-specific mechanics required explicit verification before accepting the market at face value.

## Evidence supporting the claim

- Binance BTCUSDT spot around 07:58 ET Apr 15 was about 74,187.70.
  - direct
  - matters because the market only needs price to stay above 72,000 by tomorrow noon ET
  - weight: high
- Recent Binance 1m klines closed around 74.17k-74.22k.
  - direct
  - matters because the contract settles on a 1-minute close, not just spot headlines
  - weight: high
- Binance 24h low was about 73,514, still above the strike.
  - direct/contextual
  - matters because the threshold has remained below the recent realized trading range
  - weight: medium-high
- Polymarket rules clearly name Binance BTC/USDT 1m close at 12:00 ET as source of truth.
  - direct
  - matters because rule clarity reduces interpretation risk
  - weight: high

## Evidence against the claim

- BTC can move >3% within a day, especially in crypto; the threshold is not impossibly far below current price.
  - contextual
  - matters because the remaining risk is concentrated in one short window, not the broader daily average
  - weight: medium
- The contract is exchange-specific and minute-specific, so a Binance-only wick or dislocation could matter even if broader BTC remains firm.
  - contextual/rule-sensitive
  - matters because settlement depends on one venue and one minute
  - weight: medium

## Ambiguous or mixed evidence

- CoinGecko spot roughly matched Binance, which is comforting but not decisive because it is not the governing source.
- Binance API docs support candle interpretation but do not perfectly replicate the website UI language referenced by Polymarket.

## Conflict between inputs

No major factual conflict found. The main issue is weighting: how much short-horizon crash/dislocation risk should be priced into a contract that is already comfortably in the money.

## Key assumptions

- Binance API candle structure is a valid proxy for the chart-based settlement surface.
- No major shock moves BTC below 72,000 by tomorrow noon ET.
- Binance remains operational enough that its printed candle is representative.

## Key uncertainties

- Whether a macro or crypto-specific catalyst emerges before resolution.
- Whether Binance-specific microstructure creates a temporary print below 72,000.

## Disconfirming signals to watch

- BTC drifting back toward 72k later today.
- Sharp volatility increase or adverse macro news.
- Any sign of Binance-specific outage or pricing anomaly.

## What would increase confidence

- Additional Binance checks later today still showing price comfortably above 72,000.
- Continued realized trading range holding above the strike.

## Net update logic

The evidence did not overturn the market prior; it mostly validated it. The main adjustment is modest caution because the contract is narrow, exchange-specific, and resolves on one exact minute, which keeps tail risk alive despite favorable current pricing.

## Suggested downstream use

- orchestrator synthesis input
- decision-maker review
