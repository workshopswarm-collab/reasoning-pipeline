---
type: source_note
case_key: case-20260407-42a10bc6
dispatch_id: dispatch-case-20260407-42a10bc6-20260407T014927Z
analysis_date: 2026-04-07
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: binance
topic: case-20260407-42a10bc6 | catalyst-hunter
question: Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-07 close above 68000?
driver: reliability
date_created: 2026-04-07
source_name: Binance spot API docs plus direct Binance klines check and Polymarket market rules
source_type: documentation + direct market data + market contract
source_url: https://developers.binance.info/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-07
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [bitcoin, binance]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260407-42a10bc6/researcher-analyses/2026-04-07/dispatch-case-20260407-42a10bc6-20260407T014927Z/personas/catalyst-hunter.md]
tags: [binance, btcusdt, klines, resolution-source, timezone]
---

# Summary

This source bundle establishes the governing resolution mechanics and verifies that Binance 1-minute klines are keyed by open time, with `startTime`/`endTime` interpreted in UTC and optional `timeZone` support for interval interpretation. Polymarket’s contract explicitly says the governing source of truth is the Binance BTC/USDT 1-minute candle for 12:00 ET on April 7, 2026, with the final close required to be above 68,000.

## Key facts extracted

- Polymarket rules explicitly define the market as the Binance BTC/USDT 1-minute candle for `12:00` in ET timezone on the stated date.
- Polymarket specifies the relevant field is the candle’s final `Close` price.
- Binance API docs state klines are uniquely identified by their open time.
- Binance API docs state `startTime` and `endTime` are always interpreted in UTC, even if a `timeZone` parameter is supplied.
- Binance API docs expose a `timeZone` parameter, which confirms timezone interpretation is a first-class part of Binance kline mechanics rather than an improvised convention.
- A direct live pull of recent Binance BTCUSDT 1-minute klines around research time showed BTC trading near the threshold, roughly 68.35k-68.60k, which means the contract is not trivially settled from distance-to-strike alone.
- A direct API pull for the future target window corresponding to 2026-04-07 16:00 UTC returned no rows yet, which is expected and confirms the queried target timestamp is still ahead of the current research timestamp.

## Evidence directly stated by source

- From Polymarket market page: resolution is based on Binance BTC/USDT `Close` prices with `1m` candles selected.
- From Binance docs: `GET /api/v3/klines`; klines are uniquely identified by open time.
- From Binance docs: if `timeZone` is provided, kline intervals are interpreted in that timezone, but `startTime` and `endTime` remain UTC.

## What is uncertain

- The Polymarket rule text references the Binance website chart UI as the resolution source, while my direct verification used Binance’s official spot API documentation and API endpoint behavior rather than the website UI itself.
- I did not rely on broader macro/news sources because this case is a narrow date-specific source-of-truth market and the evidence floor is satisfied primarily by contract mechanics plus current spot context.

## Why this source may matter

This is the core source note because the market is mostly a timing-and-resolution-mechanics problem. The biggest error mode is misreading which minute counts, or misaligning ET noon with UTC.

## Possible impact on the question

This source strongly supports treating the decisive event as a single Binance minute close at ET noon, equivalent to 16:00 UTC on 2026-04-07 because New York is on EDT (UTC-4). It also supports viewing current spot above 68k as directionally favorable for Yes, while leaving substantial intraday path risk because the target is a single minute close many hours after the research timestamp.

## Reliability notes

- Primary source quality: high.
- Source-of-truth ambiguity: low to medium, because Polymarket names the Binance chart UI while Binance API docs are an official but adjacent surface. The underlying kline mechanics appear consistent.
- Independence: low, because both the direct data and the documentation come from Binance. That is acceptable here because Binance is also the named governing source of truth.