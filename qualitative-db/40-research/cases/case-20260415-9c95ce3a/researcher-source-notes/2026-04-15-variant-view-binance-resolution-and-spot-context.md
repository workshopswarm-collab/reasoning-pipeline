---
type: source_note
case_key: case-20260415-9c95ce3a
dispatch_id: dispatch-case-20260415-9c95ce3a-20260415T173129Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance spot market data docs + live BTCUSDT ticker
source_type: primary
author: Binance
source_url: https://developers.binance.info/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, resolution-source, btcusdt, kline]
---

# Summary

This source note captures the direct resolution mechanics for the market and the contemporaneous spot context from Binance.

## Key facts extracted

- Binance spot API documents `GET /api/v3/klines` for symbol-level candlestick data.
- For `interval=1m`, the returned array includes a distinct close-price field.
- Binance documents that klines are uniquely identified by open time.
- The API supports a `timeZone` parameter; interval interpretation can be adjusted by timezone, while `startTime` and `endTime` remain interpreted in UTC.
- Live Binance `ticker/price` for `BTCUSDT` fetched during this run showed approximately `74100.01`.

## Evidence directly stated by source

- The Binance docs explicitly define the kline response structure and identify the `Close price` field.
- The Polymarket contract text aligns to Binance BTC/USDT 1-minute candle close price at 12:00 ET.
- The live Binance ticker confirms BTC is currently above the market threshold by roughly $2.1k, though that is not itself the settlement print.

## What is uncertain

- The contract settles on the final 12:00 ET 1-minute candle close on April 17, not the current spot price.
- The Binance public website chart and the API are closely related but the contract names the website candle view, so there remains minor operational ambiguity around presentation vs API retrieval if Binance UI/API ever diverged.
- Intraday volatility over the next ~43 hours can easily exceed the current cushion.

## Why this source may matter

This is the governing source of truth for how the contract resolves. It also shows that the current BTC/USDT level is above 72k, which makes the market's bullish baseline understandable.

## Possible impact on the question

The source supports a baseline Yes lean because BTC is already above 72k, but it also highlights that the true contract condition is narrow: BTC/USDT must still close above 72k on the specific Binance 12:00 ET one-minute candle on April 17.

## Reliability notes

High for contract mechanics and direct price reference. Lower for forecasting because a live ticker is only a snapshot and not the final settlement candle.