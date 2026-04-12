---
type: source_note
case_key: case-20260411-6669dcdb
dispatch_id: dispatch-case-20260411-6669dcdb-20260411T003353Z
analysis_date: 2026-04-10
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260411-6669dcdb | market-implied
question: Will the price of Bitcoin be above $72,000 on April 11?
driver: operational-risk
date_created: 2026-04-10
source_name: Binance Spot API and server time
source_type: primary
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=3
source_date: 2026-04-10
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: market-implied
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, btcusdt, resolution-mechanics, timezone, source-note]
---

# Summary

This note captures the governing resolution mechanics directly from Binance-related surfaces and verifies the exact instrument and timing interpretation required by the contract.

## Key facts extracted

- Binance spot API accepts `symbol=BTCUSDT`; `BTC_USDT` returns HTTP 400, which supports that the underlying exchange symbol is the standard spot pair `BTCUSDT` even though the web UI path renders as `BTC_USDT`.
- Live Binance spot data around research time showed BTCUSDT trading at roughly 72.86k.
- Binance server time during the check was `2026-04-11T00:35:10Z`, which converts to `2026-04-10 20:35:10 ET` under DST.
- Recent 1-minute klines had open times mapping cleanly from UTC to ET, confirming that ET noon on Apr. 11 corresponds to 16:00 UTC, not 12:00 UTC.
- Querying the exact future resolution window for `2026-04-11 16:00 UTC` returned no data yet, as expected because the candle had not occurred.
- Binance API docs say kline data are uniquely identified by open time, and the `Close` field is the per-candle closing price.

## Evidence directly stated by source

- API docs: `/api/v3/klines` returns kline/candlestick bars for a symbol and klines are uniquely identified by open time.
- API docs: default `timeZone` is UTC; if provided, intervals are interpreted in that timezone, while `startTime` and `endTime` remain UTC.
- Live ticker endpoints returned BTCUSDT around 72.87k during the run.

## What is uncertain

- The contract says traders should look at the Binance web UI with `1m` candles selected, while the docs describe API semantics. This creates mild source-of-truth ambiguity if the UI ever displayed a revised or presentation-layer value different from the raw API.
- It is not directly verified from the UI screenshot itself whether Polymarket resolves by the candle labeled `12:00 ET` as the minute beginning at 12:00:00 ET or simply the candle visible after that minute closes; the API/docs strongly suggest the former because klines are indexed by open time.

## Why this source may matter

This is the key source for exact pair verification, timing conversion, and interpretation of what the candle close means. Those mechanics determine whether the market is mostly a near-spot-price question or whether hidden contract ambiguity could matter.

## Possible impact on the question

Because live Binance BTCUSDT was already above 72k by roughly 0.8k at research time and the contract resolves off the BTCUSDT 1-minute candle close at ET noon, the market's high Yes probability is mechanically understandable unless a sizeable overnight-to-noon drop occurs.

## Reliability notes

High reliability for live exchange data and API semantics. Moderate caution remains because the formal contract points to the Binance UI rather than an API endpoint, so there is still some operational/source-of-truth ambiguity even though the pair and timing interpretation look straightforward.