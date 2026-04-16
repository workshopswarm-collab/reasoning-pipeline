---
type: source_note
case_key: case-20260416-bbc8ed19
dispatch_id: dispatch-case-20260416-bbc8ed19-20260416T072336Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-bbc8ed19 | base-rate
question: Will the price of Bitcoin be above $72,000 on April 20?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance Spot API docs and BTCUSDT market data
source_type: primary + direct market data
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-bbc8ed19/researcher-analyses/2026-04-16/dispatch-case-20260416-bbc8ed19-20260416T072336Z/personas/base-rate.md
tags: [binance, settlement-source, btcusdt, kline]
---

# Summary

This note captures the governing Binance data surface for settlement mechanics plus current BTC/USDT context relevant to a short-horizon base-rate view.

## Key facts extracted

- Binance Spot API documents `GET /api/v3/klines` as the candlestick endpoint and shows the response includes open time, open/high/low/close prices, and close time.
- The docs state klines are uniquely identified by open time.
- The docs support `interval=1m`, which matches the market rule language about the 1 minute candle.
- The docs allow a `timeZone` parameter for interpreting kline intervals in a chosen timezone, though `startTime` and `endTime` remain interpreted in UTC.
- On 2026-04-16, the live BTCUSDT ticker price retrieved from Binance was `74909.72`, already above the market threshold of 72000.
- Recent Binance daily closes from 2026-04-07 through 2026-04-16 were: 71924.22, 71069.93, 71787.97, 72962.70, 73043.16, 70740.98, 74417.99, 74131.55, 74809.99, 74909.72.

## Evidence directly stated by source

- Binance docs explicitly define kline/candlestick bars and show the close price field in the response schema.
- Binance docs explicitly list `1m` as a supported interval.
- Binance docs explicitly note timeZone support and UTC handling for request bounds.

## What is uncertain

- The public docs confirm the kline structure, but the Polymarket rule references the Binance web chart UI specifically rather than the API endpoint. The structure is closely aligned but not literally the same presentation surface.
- This note does not itself determine the final 2026-04-20 12:00 ET candle outcome; it only verifies mechanics and current spot context.

## Why this source may matter

The contract is narrow and date-specific. Verifying the actual settlement source mechanics matters more than generic BTC price commentary.

## Possible impact on the question

The note supports a high-probability prior for Yes because BTCUSDT is currently above 72k and the authoritative exchange family named in the rules uses a 1-minute candle close field that can be checked precisely at the relevant time.

## Reliability notes

- Binance is the named governing source of truth, so source-of-truth relevance is high.
- The API docs are authoritative for data structure and timing semantics.
- Live ticker and recent klines are direct exchange data, though not the final resolving candle.
- Operationally, a key residual risk is exchange-specific print behavior or a sharp short-term move before the exact noon ET candle on April 20.
