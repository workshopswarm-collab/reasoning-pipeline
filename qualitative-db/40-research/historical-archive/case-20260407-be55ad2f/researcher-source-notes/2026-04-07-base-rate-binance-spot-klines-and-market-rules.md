---
type: source_note
case_key: case-20260407-be55ad2f
dispatch_id: dispatch-case-20260407-be55ad2f-20260407T193635Z
analysis_date: 2026-04-07
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260407-be55ad2f | base-rate
question: Will the Binance BTC/USDT 1-minute candle for 2026-04-08 12:00 ET close above 66000?
driver: operational-risk
date_created: 2026-04-07T19:39:00Z
source_name: Binance spot market data endpoints docs and BTCUSDT klines/time/exchangeInfo
source_type: exchange docs + exchange API
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
source_date: 2026-04-07
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260407-be55ad2f/researcher-analyses/2026-04-07/dispatch-case-20260407-be55ad2f-20260407T193635Z/personas/base-rate.md]
tags: [binance, settlement-mechanics, klines, timezone, price-threshold]
---

# Summary

This source note records the governing settlement mechanics and a direct spot-data check for the April 8 BTC > 66k market. The key point is that the market resolves from Binance BTC/USDT 1-minute candle close, not from a cross-exchange composite price.

## Key facts extracted

- Polymarket rules say the market resolves from the Binance BTC/USDT 1-minute candle for 12:00 in ET on April 8, using the candle's final Close price.
- Binance spot API docs say klines are uniquely identified by open time.
- Binance spot API docs say default kline timezone is UTC, but a `timeZone` parameter can reinterpret intervals in another timezone; `startTime` and `endTime` remain UTC even when `timeZone` is set.
- Binance `exchangeInfo` for BTCUSDT returns `timezone: UTC` and rate-limit metadata, including request-weight limits.
- A direct API check on 2026-04-07 showed BTCUSDT spot around 68.48k, comfortably above the 66k threshold.
- A 120-minute recent kline sample had every 1-minute close above 66k.
- Attempting to fetch the exact April 8 12:00 ET candle in advance returns an empty result, as expected because that candle has not occurred yet.

## Evidence directly stated by source

- Binance docs: "Klines are uniquely identified by their open time."
- Binance docs: if `timeZone` is provided, intervals are interpreted in that timezone instead of UTC.
- Binance docs: `startTime` and `endTime` are always interpreted in UTC regardless of `timeZone`.
- Binance docs: `klines` and `uiKlines` are both available with the same parameters; `uiKlines` are modified for presentation.
- Binance API `exchangeInfo`: `timezone` is `UTC`.

## What is uncertain

- The exact April 8 12:00 ET close cannot be directly verified before the event occurs.
- The Polymarket rule text points users to the Binance trading UI; while the API is clearly consistent with Binance data and timing semantics, the final displayed UI candle at settlement time remains the governing practical surface.
- Sudden BTC moves of more than ~2.5k before settlement are unusual over one day but not impossible.

## Why this source may matter

This is the primary source for settlement mechanics. The main risk in this market is not interpreting generic BTC direction but correctly mapping ET noon to the Binance candle definition and understanding that exchange-specific candle close, not broader market consensus, determines settlement.

## Possible impact on the question

The source strongly supports a high Yes probability because current Binance BTCUSDT is materially above 66k, but it also justifies some discount versus an extreme near-certainty price because settlement depends on one narrow future minute close on one exchange.

## Reliability notes

- High reliability for mechanics: Binance docs and Binance API are direct exchange sources.
- High reliability for current spot level: live exchange API.
- Independence is limited because both the docs and live data come from Binance, but that is acceptable here since Binance is the governing source of truth.
- Rate-limit handling was light-touch: small-number queries only, well below published request-weight limits.
