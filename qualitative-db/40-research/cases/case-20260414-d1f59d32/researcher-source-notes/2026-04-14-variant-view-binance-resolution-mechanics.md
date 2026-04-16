---
type: source_note
case_key: case-20260414-d1f59d32
dispatch_id: dispatch-case-20260414-d1f59d32-20260414T144613Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: market-structure
entity: btc
topic: bitcoin-above-74k-on-april-15
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on April 15, 2026 close above 74000?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance spot API docs and live BTCUSDT market endpoints
source_type: primary-plus-direct-market-data
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: variant-view
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, resolution-mechanics, candle, timezone, source-note]
---

# Summary

Binance is the governing source of truth for this market, and its kline API documentation plus live BTCUSDT endpoints make the contract mechanics auditable: the relevant object is the BTC/USDT 1-minute candle, with close price decisive, and timezone handling explicitly supported.

## Key facts extracted

- Binance documents `GET /api/v3/klines` as the endpoint for kline/candlestick bars.
- Klines are uniquely identified by open time.
- The endpoint supports `interval=1m` and a `timeZone` parameter; docs state interval interpretation can be shifted by timezone while `startTime` and `endTime` remain UTC.
- The kline response includes open time, close time, and close price as separate fields.
- Live Binance BTCUSDT spot price fetched during this run was about 75.36k, above the 74k strike.
- Recent 1-minute klines fetched during this run also showed closes around 75.30k-75.36k.

## Evidence directly stated by source

- Binance docs explicitly say the market-data endpoint returns kline/candlestick bars and that the response contains a close price field.
- Binance docs explicitly support timezone-aware interpretation of kline intervals.
- The Polymarket contract explicitly names Binance BTC/USDT 1-minute candle at 12:00 ET as the resolution source.

## What is uncertain

- The Polymarket contract references the Binance trading UI with `1m` selected, while API docs describe the underlying market-data object; this is very likely equivalent for settlement, but the exact UI-display rounding/latency at resolution time is not independently verified here.
- A single live snapshot does not establish tomorrow noon ET price path.

## Why this source may matter

This is the primary source set for both contract interpretation and current market-state grounding. It reduces ambiguity about what counts: Binance BTC/USDT, one-minute candle, noon ET, close price, not another exchange and not an intraminute high.

## Possible impact on the question

It strengthens confidence that the key issue is not broad BTC direction alone but whether BTC/USDT remains above 74k exactly at the relevant Binance minute close tomorrow. It also highlights a variant risk: an otherwise bullish BTC narrative can still lose if a short-lived dip occurs at the settlement minute.

## Reliability notes

High credibility for resolution mechanics because Binance is the governing source and Polymarket rules independently point to the same source. Independence is limited on the mechanics side because both pieces refer to the same underlying venue, but that is appropriate for a source-of-truth question.