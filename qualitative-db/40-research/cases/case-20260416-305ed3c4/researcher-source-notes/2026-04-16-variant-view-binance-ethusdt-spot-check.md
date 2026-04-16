---
type: source_note
case_key: case-20260416-305ed3c4
dispatch_id: dispatch-case-20260416-305ed3c4-20260416T190054Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: market-structure
entity: ethereum
topic: ethereum-above-2200-on-april-17
question: Will the Binance ETH/USDT 12:00 ET 1-minute candle close on 2026-04-17 above 2200?
driver: reliability
date_created: 2026-04-16
source_name: Binance Spot API ETHUSDT ticker and 1m klines
source_type: exchange_api
source_url: https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1m
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: variant-view
related_entities: [ethereum]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-305ed3c4/researcher-analyses/2026-04-16/dispatch-case-20260416-305ed3c4-20260416T190054Z/personas/variant-view.md]
tags: [binance, ethusdt, settlement-source, timing-check]
---

# Summary

Direct spot-check of Binance's public spot API confirms ETH/USDT is trading well above 2200 on 2026-04-16 and that 1-minute klines are available with millisecond timestamps that can be mapped to the contract's noon ET settlement window.

## Key facts extracted

- Binance ticker endpoint returned ETHUSDT at 2343.62 during this check.
- Binance 1-minute kline endpoint returned recent candles around 2343-2345.
- A direct query using startTime `1776355200000` returned the candle opening at 2026-04-16 16:00:00 UTC, which is 2026-04-16 12:00:00 ET.
- Therefore the market's stated source-of-truth surface is practically queryable and the ET-to-UTC mapping is straightforward for verification.

## Evidence directly stated by source

- Recent ticker price: 2343.62000000.
- Example 1-minute close prices around the check window: 2343.10, 2343.37, 2343.36, 2343.55, 2343.62.
- The Binance klines response format includes open time and close price, which matches the market's dependence on the 1-minute candle close.

## What is uncertain

- This source does not itself guarantee tomorrow's noon ET close.
- The Polymarket wording references the Binance trading UI candle display rather than the API explicitly, though the API is strongly consistent with that same underlying market data.
- Intraday crypto volatility can still move ETH below 2200 before the relevant timestamp.

## Why this source may matter

This is the closest direct source to the actual settlement mechanism. It validates both the price regime and the operational mechanics of checking the exact noon ET minute candle.

## Possible impact on the question

Because ETH is currently about 6.5% above the threshold, the obvious market case is that only a sizable adverse move in the next roughly 21 hours would flip the answer to No. It also lowers ambiguity about how to verify the settlement candle when the market resolves.

## Reliability notes

High reliability for direct market-state observation and timing interpretation. Independence is limited because this is the same exchange family that serves as the governing source of truth, so it is excellent for settlement mechanics but not independent contextual confirmation.