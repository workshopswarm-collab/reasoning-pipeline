---
type: source_note
case_key: case-20260409-746679d3
dispatch_id: dispatch-case-20260409-746679d3-20260409T205932Z
analysis_date: 2026-04-09
persona: market-implied
domain: crypto
subdomain: spot-market-structure
entity: ethereal
question: Will the price of Ethereum be above $2,100 on April 10?
driver: reliability
date_created: 2026-04-09
source_name: Binance Spot API docs and live API surfaces
source_type: primary_documentation_plus_live_api
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: market-implied
related_entities: []
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-746679d3/researcher-analyses/2026-04-09/dispatch-case-20260409-746679d3-20260409T205932Z/personas/market-implied.md]
tags: [binance, ethusdt, klines, resolution-mechanics, timing]
---

# Summary

This note captures the direct contract-relevant mechanics from Binance documentation and live API checks for ETHUSDT 1-minute candles.

## Key facts extracted

- Binance `/api/v3/klines` defines klines as uniquely identified by their open time.
- The response includes both kline open time and kline close time, with close time ending at `...9999` for a one-minute bar.
- Binance documentation says `startTime` and `endTime` are always interpreted in UTC.
- Binance documentation says a `timeZone` parameter can be provided so kline intervals are interpreted in that timezone instead of UTC.
- Live Binance server time endpoint responded successfully, confirming the exchange is reachable and providing a direct timing surface.
- Live ETHUSDT exchange info confirmed spot symbol availability and a `PRICE_FILTER.tickSize` of `0.01000000`, which is relevant because the market rules say precision is determined by the source.
- A live ETHUSDT 1m kline pull returned standard 1-minute bars with close prices and close times exactly 59.999 seconds after the open.
- Querying the future bar beginning at 2026-04-10 16:00:00 UTC returned an empty array, which is expected because that bar has not happened yet; this is a useful sanity check that noon ET on Apr 10 maps to 16:00 UTC under daylight saving time.

## Evidence directly stated by source

- Binance docs: klines are uniquely identified by open time.
- Binance docs: if `timeZone` is provided, intervals are interpreted in that timezone instead of UTC.
- Binance docs: `startTime` and `endTime` remain UTC regardless of `timeZone`.
- Binance docs example response includes the close price as the fifth price field and a separate close-time field.

## What is uncertain

- Polymarket rules reference the Binance website chart rather than the REST API directly, so there remains small presentation-risk that the web UI and API could expose the same candle through slightly different labeling conventions.
- The wording “candle for ETH/USDT 12:00 in the ET timezone” could in theory be read as either the bar opened at 12:00:00 ET or the bar closed at 12:00:59 ET, though Binance’s own kline identification by open time makes the open-time interpretation stronger.

## Why this source may matter

This is the governing source-of-truth family for the market. It clarifies the timing mechanics, the candle identity convention, and the precision likely used to judge whether the close is above 2100.

## Possible impact on the question

Because the contract is tied to a single Binance 1-minute close, the market is primarily pricing whether ETHUSDT remains above 2100 at one specific minute tomorrow, not whether ETH is broadly strong over the day. The direct timing check also supports that noon ET on Apr 10 corresponds to 16:00 UTC, which is the case-specific verification requested.

## Reliability notes

Reliability is high for settlement mechanics because this is Binance’s own documentation plus live Binance API responses. Independence is low because both the docs and live API are within the same source family, so a separate contextual source is still useful for market-level interpretation.