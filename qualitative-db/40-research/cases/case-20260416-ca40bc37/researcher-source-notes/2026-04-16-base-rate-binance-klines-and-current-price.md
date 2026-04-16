---
type: source_note
case_key: case-20260416-ca40bc37
dispatch_id: dispatch-case-20260416-ca40bc37-20260416T053546Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-20 close above 72000?
driver: reliability
date_created: 2026-04-16
source_name: Binance spot API docs and live BTCUSDT data
source_type: exchange documentation + market data primary/contextual
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-16
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, klines, btcusdt, market-data]
---

# Summary

Binance documentation confirms that klines are uniquely identified by open time, that a 1-minute candle has an explicit close field, and that timezone handling can matter for interval interpretation. Live Binance data shows BTC/USDT currently around 75.1k, above the market threshold.

## Key facts extracted

- Binance spot API `GET /api/v3/klines` returns open, high, low, close, volume, and close time for each candle.
- Klines are uniquely identified by open time.
- The API docs note that `timeZone` affects interval interpretation, while `startTime` and `endTime` are always interpreted in UTC.
- Live Binance ticker showed BTCUSDT at 75,093.11 during this run.
- Recent daily Binance closes before this run were mostly above 72,000, including 74,417.99, 74,131.55, 74,809.99, and an intraday current day print near 75,097.97 at time of sampling.

## Evidence directly stated by source

- Binance docs: "Klines are uniquely identified by their open time."
- Binance docs provide the response field order showing the candle close price explicitly.
- Binance live ticker endpoint returned BTCUSDT 75,093.11 during this run.

## What is uncertain

- This source does not by itself forecast the exact April 20 noon ET print.
- The Polymarket rule references the UI chart, so API-to-UI mapping is strongly suggestive but not a literal settlement guarantee.

## Why this source may matter

This is the best independent check on both market state and candle semantics. It reduces contract-interpretation ambiguity and anchors the base-rate analysis in the actual venue that settles the market.

## Possible impact on the question

Current level being ~4.3% above 72,000 only four days before resolution makes a Yes outcome the base-rate favorite, but not a lock; BTC can move that much over several days.

## Reliability notes

High credibility as the designated exchange source and official docs. Independence versus Polymarket is reasonably good on mechanics, though Polymarket still defines the contract.