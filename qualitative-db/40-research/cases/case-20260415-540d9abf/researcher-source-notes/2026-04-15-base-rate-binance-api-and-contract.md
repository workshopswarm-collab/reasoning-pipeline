---
type: source_note
case_key: case-20260415-540d9abf
dispatch_id: dispatch-case-20260415-540d9abf-20260415T234706Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: market-structure
entity: sol
topic: solana-above-80-on-april-19
question: Will the price of Solana be above $80 on April 19?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance spot API docs + live SOLUSDT endpoints
source_type: primary_and_contextual
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [sol, solana]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-540d9abf/researcher-analyses/2026-04-15/dispatch-case-20260415-540d9abf-20260415T234706Z/personas/base-rate.md]
tags: [binance, resolution-source, source-note, base-rate]
---

# Summary

This note captures the governing resolution mechanics and a direct live-market context check from Binance for SOL/USDT.

## Key facts extracted

- Binance Spot API documents `GET /api/v3/klines` for candlestick data and states that klines are uniquely identified by their open time.
- The kline response schema shows the close price as the fifth element in each kline array.
- Binance documentation states a `timeZone` parameter can be supplied so kline intervals are interpreted in that timezone, while `startTime` and `endTime` remain UTC.
- A direct live query to Binance on 2026-04-15 returned SOLUSDT trading around 84.84, with 24h weighted average price around 83.96 and 24h range roughly 82.65 to 85.83.
- A direct daily-kline pull for recent days shows SOL closing above 80 on each of the last five completed daily candles observed in the check.

## Evidence directly stated by source

From Binance docs:
- `GET /api/v3/klines` provides kline/candlestick bars for a symbol.
- Klines are uniquely identified by open time.
- Close price is included in the response array.
- `timeZone` changes interval interpretation, while `startTime` and `endTime` are always interpreted in UTC.

From direct Binance API checks executed during the run:
- `avgPrice` returned price about 84.8614 for SOLUSDT.
- `ticker/24hr` returned lastPrice 84.84 and weightedAvgPrice 83.9615.
- Recent daily klines show closes of 84.93, 81.53, 86.51, 83.72, 84.84 for the last five completed observed daily candles.

## What is uncertain

- The market resolves on the Binance UI candle at 12:00 ET on 2026-04-19, not on the spot price at research time.
- Daily closes are only a coarse base-rate proxy for whether the noon ET one-minute close will exceed 80.
- The Polymarket rule text references the Binance UI surface specifically, so there is some small residual ambiguity about API/UI parity even though they should normally match.

## Why this source may matter

This is the most important source because the contract is explicitly governed by Binance SOL/USDT one-minute candle close data. It also gives a direct current-price context showing SOL already above the threshold by several dollars.

## Possible impact on the question

If SOL remains in its recent price regime, the outside-view probability that the specific noon ET one-minute close on April 19 is above 80 is high. The key remaining risk is a material crypto drawdown before or during the resolution window, not contract ambiguity.

## Reliability notes

- Binance docs are authoritative for API mechanics.
- Direct API pulls are strong contextual evidence for current price regime and instrument identity.
- The specific market rule names the Binance UI candle as source of truth, so the docs/API are highly relevant but slightly indirect relative to the exact UI chart surface.