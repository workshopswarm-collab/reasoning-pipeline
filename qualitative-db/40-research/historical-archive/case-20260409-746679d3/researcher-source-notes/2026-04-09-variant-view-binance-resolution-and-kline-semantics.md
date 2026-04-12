---
type: source_note
case_key: case-20260409-746679d3
dispatch_id: dispatch-case-20260409-746679d3-20260409T205932Z
analysis_date: 2026-04-09
persona: variant-view
domain: crypto
subdomain: spot-market-structure
entity: ethereum
topic: ethereum-above-2100-on-april-10
question: Will the price of Ethereum be above $2,100 on April 10?
driver: reliability
date_created: 2026-04-09
source_name: Binance spot API docs and live Binance spot API
type: source_note
source_type: primary_and_contextual
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [ethereum]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-746679d3/researcher-analyses/2026-04-09/dispatch-case-20260409-746679d3-20260409T205932Z/personas/variant-view.md]
tags: [binance, kline, resolution, market-rules, timing]
---

# Summary

This note captures the direct Binance surfaces most relevant to settlement mechanics for the April 10 ETH/USDT >2100 market.

## Key facts extracted

- Binance spot REST docs define `GET /api/v3/klines` as the kline/candlestick endpoint.
- Binance docs state: "Klines are uniquely identified by their open time."
- Binance docs list an optional `timeZone` parameter, default `0 (UTC)`.
- Binance docs further state that if `timeZone` is provided, kline intervals are interpreted in that timezone instead of UTC, but `startTime` and `endTime` remain interpreted in UTC.
- Live Binance API output for current ETHUSDT 1-minute candles returns rows with both open time and close time, where close time is the end of the minute minus 1 ms (for example `21:00:59.999Z` for the candle opened at `21:00:00Z`).
- Binance server time endpoint is accessible and returned `2026-04-09T21:00:24.463Z` during verification, confirming the exchange clock is in UTC on the authoritative API surface.

## Evidence directly stated by source

- Binance docs explicitly say klines are identified by open time.
- Binance docs explicitly expose timezone handling for interval interpretation and specify UTC treatment for start/end query bounds.
- Live API output directly demonstrates the 1-minute candle schema and the close-time field behavior.

## What is uncertain

- The Polymarket rule text points users to the Binance web trading interface with `1m` and `Candles` selected, not to the API docs or API endpoint directly.
- I could not reliably extract the rendered Binance web page content in this environment, so I cannot directly verify whether the consumer UI labels the candle by opening minute or by ending minute.
- Historical future-dated klines for 2026-04-10 are obviously unavailable before settlement, so this note verifies mechanics rather than the final resolving candle itself.

## Why this source may matter

The key variant risk in an otherwise straightforward market is rule interpretation rather than market direction: whether "12:00 in ET" should be mapped to the candle opened at 12:00:00 ET or some differently labeled minute on the Binance UI. The Binance docs materially reduce that ambiguity by making open-time identification explicit.

## Possible impact on the question

This source strengthens the view that the governing source of truth is Binance ETH/USDT 1-minute candle data, with the noon ET candle best interpreted as the candle opened at 12:00:00 ET / 16:00:00 UTC on April 10, 2026. That lowers but does not fully eliminate contract-interpretation risk.

## Reliability notes

- Primary strength: direct Binance documentation plus direct Binance API verification.
- Limitation: the exact Polymarket settlement language references the Binance web chart UI, so there remains a small UI-labeling / implementation ambiguity not fully closed by the API alone.
- Independence is limited because both sources are Binance-controlled, but that is acceptable here because Binance is also the explicit source of truth for settlement.