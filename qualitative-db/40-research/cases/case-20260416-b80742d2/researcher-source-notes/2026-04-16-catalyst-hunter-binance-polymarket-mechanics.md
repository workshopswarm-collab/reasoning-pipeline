---
type: source_note
case_key: case-20260416-b80742d2
dispatch_id: dispatch-case-20260416-b80742d2-20260416T014833Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: market-structure
entity: xrp
topic: xrp-above-1pt3-on-april-19
question: Will the price of XRP be above $1.30 on April 19?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket contract text plus Binance spot market-data documentation and live XRPUSDT endpoint checks
source_type: primary_and_contextual
source_url: https://polymarket.com/event/xrp-above-on-april-19
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [xrp]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-b80742d2/researcher-analyses/2026-04-16/dispatch-case-20260416-b80742d2-20260416T014833Z/personas/catalyst-hunter.md]
tags: [source-note, polymarket, binance, settlement-mechanics, xrp]
---

# Summary

This note captures the governing contract mechanics and the most relevant live price context for the April 19 XRP>$1.30 market.

## Key facts extracted

- Polymarket states the market resolves to Yes if the Binance XRP/USDT 1 minute candle for 12:00 ET on April 19 has a final Close price higher than 1.30.
- The specified source of truth is Binance XRP/USDT with 1m Candles selected.
- Binance spot API documentation says `/api/v3/klines` returns kline/candlestick bars, that klines are uniquely identified by open time, and that the response contains the candle close price as the fifth element.
- Binance documentation also states a `timeZone` parameter can be supplied for kline interval interpretation, but `startTime` and `endTime` are always interpreted in UTC.
- Live Binance endpoint checks during this run showed XRPUSDT around 1.4012-1.4013, above the 1.30 strike by roughly 7.8%.
- A 24h ticker check during this run showed XRPUSDT daily range approximately 1.3503 to 1.4086, meaning XRP was already trading comfortably above 1.30 at time of research.

## Evidence directly stated by source

Direct from Polymarket rules:
- the contract uses the Binance XRP/USDT 12:00 ET 1-minute candle on April 19
- the relevant field is the final Close price
- the threshold is strictly higher than 1.30

Direct from Binance documentation:
- klines are uniquely identified by open time
- the close price field is explicitly returned in the kline payload
- timezone handling is parameterized, with UTC still governing start/end timestamps

Direct from live Binance endpoints checked in run:
- current XRPUSDT spot is about 1.4013
- recent 1-minute klines are available from the public API
- recent 24h range remained above the 1.30 strike low-water mark

## What is uncertain

- The Polymarket page references the Binance chart UI rather than the API as the resolution surface, so there is a small implementation ambiguity about whether any UI-specific display rounding or backfill behavior could matter at the margin.
- The decisive candle is still several days away, so current spot being above 1.30 does not settle the market.
- XRP is volatile enough that a weekend move below 1.30 by the settlement minute remains plausible.

## Why this source may matter

This source set establishes both the exact contract mechanics and the live price distance to the strike. That is the backbone for any catalyst analysis because the relevant question is not whether XRP is strong in general, but whether anything before noon ET on April 19 is likely to drag the Binance 1-minute close below 1.30.

## Possible impact on the question

These sources push the case toward Yes unless a material negative catalyst emerges before settlement. Because the market is already far above the strike and the resolution source is a precise Binance minute close, the main remaining work is timing and catalyst risk rather than broad thesis-building.

## Reliability notes

- Polymarket is authoritative for contract wording and resolution criteria.
- Binance developer documentation is authoritative contextual guidance for how Binance exposes kline data, though the Polymarket rule points to the Binance trading UI as the actual resolution surface.
- Live Binance public API checks are strong direct context for current price state but are not themselves the final settlement event.