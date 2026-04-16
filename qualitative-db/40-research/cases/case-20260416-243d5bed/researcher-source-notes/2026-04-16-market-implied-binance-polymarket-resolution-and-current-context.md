---
type: source_note
case_key: case-20260416-243d5bed
dispatch_id: dispatch-case-20260416-243d5bed-20260416T161511Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: market-structure
entity: eth
question: Will the Binance ETH/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 2300?
driver: reliability
date_created: 2026-04-16
source_name: Polymarket market page and Binance spot API docs / live API
source_type: market rules plus exchange documentation / exchange API
source_url: https://polymarket.com/event/ethereum-above-on-april-17
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: market-implied
related_entities: [eth]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-243d5bed/researcher-analyses/2026-04-16/dispatch-case-20260416-243d5bed-20260416T161511Z/personas/market-implied.md]
tags: [polymarket, binance, ethusdt, resolution-rules, source-note]
---

# Summary

This note captures the governing contract mechanics and the current Binance spot context most relevant to the market-implied view.

## Key facts extracted

- Polymarket states the market resolves Yes if the Binance ETH/USDT 1-minute candle for 12:00 in ET on 2026-04-17 has a final Close price above 2300.
- Polymarket explicitly says the resolution source is Binance ETH/USDT with 1m candles, and that the market is about Binance ETH/USDT rather than other exchanges or pairs.
- Binance spot API documentation for `GET /api/v3/klines` says klines are uniquely identified by open time and that the response includes a `Close price` field.
- Binance docs also say `timeZone` changes interval interpretation, while `startTime` and `endTime` remain interpreted in UTC.
- Live Binance spot API responses on 2026-04-16 showed ETHUSDT around 2338.67 to 2338.89, with 24h range 2285.10 to 2385.61 and weighted average price about 2340.82.
- A query for future-dated 2026-04-17 12:00 ET klines returned an empty array, which is expected and confirms the exact target candle is not yet available.

## Evidence directly stated by source

- Polymarket rules directly state the source of truth and the all-conditions-required settlement logic.
- Binance docs directly state that klines expose close price and are indexed by open time.
- Binance live ticker endpoints directly state current ETHUSDT spot price and 24h range data.

## What is uncertain

- The exact Binance web UI candle timestamp labeling convention relative to the API open-time indexing is not independently verified here from the UI itself.
- Market microstructure or macro news between now and 2026-04-17 12:00 ET could move ETH materially.
- It remains possible that Polymarket resolvers visually inspect the Binance UI rather than the API, though the underlying candle data should normally match.

## Why this source may matter

It establishes both the governing settlement mechanics and the relevant current price anchor. For a date-specific price-threshold market, those are the main inputs needed before estimating whether the market is pricing the threshold efficiently.

## Possible impact on the question

Because current Binance ETHUSDT is already above 2300 by roughly 39 dollars, a Yes probability above 50% is plausible. But only one specific future 1-minute candle close counts, so the market should still discount overnight volatility and any ETH-specific downside before noon ET tomorrow.

## Reliability notes

- Polymarket rules are the direct governing contract source.
- Binance spot API docs are authoritative for how klines are structured.
- Binance live ticker endpoints are authoritative for current Binance spot context, though they do not settle the market themselves.
- Evidence independence is medium rather than high because both contextual sources come from Binance surfaces, but that is appropriate here since Binance is also the designated source-of-truth family.