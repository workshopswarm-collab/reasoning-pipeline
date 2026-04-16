---
type: source_note
case_key: case-20260416-a8277fc8
dispatch_id: dispatch-case-20260416-a8277fc8-20260416T001420Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: spot-market-context
entity: sol
topic: solana-above-80-on-april-19
question: Is SOL likely to be above 80 on the qualifying Binance noon candle on 2026-04-19?
driver: reliability
date_created: 2026-04-16
source_name: Binance public market data API
source_type: exchange market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-16
credibility: high
recency: current
stance: neutral
certainty: medium-high
importance: high
novelty: medium
agent: orchestrator
related_entities: [sol, solana]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-a8277fc8/researcher-analyses/2026-04-16/dispatch-case-20260416-a8277fc8-20260416T001420Z/personas/risk-manager.md
tags: [binance, api, spot, solusdt, date-sensitive]
---

# Summary

Current Binance spot context is supportive of a Yes answer because SOL/USDT is already trading materially above 80 with several days left, but the contract resolves on one specific minute close, so path and timing risk remain nonzero.

## Key facts extracted

- Binance ticker price at collection time: **84.67**.
- Binance 24h range at collection time: **82.65 to 85.83**.
- Recent daily candles from Binance show SOL trading above 80 for several consecutive days.
- Sample recent daily highs/lows/close from fetched klines:
  - 2026-04-11 UTC day: low 81.40, high 86.81, close 86.51
  - 2026-04-12 UTC day: low 83.30, high 87.67, close 83.72
  - 2026-04-13 UTC day: low 82.65, high 85.83, close 84.90
  - 2026-04-14 partial/current UTC day in fetched output: around 84.67

## Evidence directly stated by source

- Binance ticker endpoint returned `{"symbol":"SOLUSDT","price":"84.67000000"}`.
- Binance 24h endpoint returned `highPrice":"85.83000000"`, `lowPrice":"82.65000000"`, and `lastPrice":"84.67000000"`.
- Binance daily klines returned multiple recent closes above 80 and no recent daily low below 80 in the sampled window shown.

## What is uncertain

- The contract resolves on the specific **12:00 ET 1-minute close on Apr. 19**, not on current spot, daily close, or 24h average.
- Current fetched data does not prove what the qualifying minute close will be three days later.
- Crypto can move materially over a short weekend window; a drop below 80 by the qualifying minute remains plausible.

## Why this source may matter

This is the best direct contextual source for current price level and recent realized trading range on the exact governing exchange and pair.

## Possible impact on the question

Because SOL is already ~5.8% above the threshold, the market's bullish view is directionally sensible. The main residual risk is not whether 80 is remotely reachable, but whether the market is overconfident about holding above 80 into one exact settlement minute.

## Reliability notes

- High-quality direct exchange data for current market context.
- Not itself the settlement proof because it is not the future qualifying candle.
- Independence versus the governing source is low by design: this is the same exchange ecosystem as settlement, which is useful for mechanism fit but not independent confirmation.