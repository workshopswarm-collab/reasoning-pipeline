---
type: source_note
case_key: case-20260414-8a0619b6
dispatch_id: dispatch-case-20260414-8a0619b6-20260414T194140Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-8a0619b6 | variant-view
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-18 close above 70000?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance market-data endpoints and live BTCUSDT ticker context
source_type: primary_and_contextual
source_url: https://developers.binance.info/docs/binance-spot-api-docs/rest-api/market-data-endpoints
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-8a0619b6/researcher-analyses/2026-04-14/dispatch-case-20260414-8a0619b6-20260414T194140Z/personas/variant-view.md]
tags: [binance, btcusdt, resolution-source, 1m-candle]
---

# Summary

This note captures the governing resolution mechanics and current spot context for the April 18 BTC > 70k market.

## Key facts extracted

- Binance Spot API documents `GET /api/v3/klines` and `GET /api/v3/uiKlines` as the canonical candlestick endpoints for a symbol.
- Kline responses include open time, open, high, low, close, and close time; the close price is directly available in the returned array.
- Binance documents an optional `timeZone` parameter for kline interpretation, with `startTime` and `endTime` always interpreted in UTC.
- Live Binance BTCUSDT ticker data checked during this run showed BTCUSDT last price around 74.1k, with 24h high about 76.0k and 24h low about 73.0k.
- That means spot is currently about 5.9% above the 70k threshold with four days remaining, but the recent 24h range also shows multi-thousand-dollar realized movement.

## Evidence directly stated by source

- Binance market-data docs explicitly define kline/candlestick data and show the close-price field in the response.
- Binance docs explicitly note timezone handling for klines.
- Live ticker endpoint returned BTCUSDT lastPrice near 74126 and 24h low near 72972 at time of check.

## What is uncertain

- The exact April 18 12:00 ET candle close cannot be known yet.
- The market description says resolution uses the Binance trading UI candle, while this note relies on Binance’s API documentation and live ticker endpoints as the best machine-readable proxy for how that candle is represented.
- Short-horizon BTC volatility over the next four days could still move the 12:00 ET close below 70k even if current spot remains above it now.

## Why this source may matter

This is the best primary source for both settlement mechanics and current exchange-specific context. The contract resolves specifically to Binance BTC/USDT, so exchange-specific evidence matters more than generic BTC/USD references.

## Possible impact on the question

The source supports a high-probability Yes baseline because current Binance BTCUSDT spot is materially above 70k. But it also supports a nontrivial No tail because the contract is determined by one specific one-minute close at a specific future time, not by average price or broader weekly level.

## Reliability notes

- Primary-source quality is high for settlement mechanics because Binance is the named source of truth in the contract.
- Reliability is lower for final resolution than a settled historical candle because the API docs describe mechanics rather than pre-committing which exact UI representation Polymarket will inspect.
- The live ticker check is strong contextual evidence, but not direct evidence for the future noon ET candle on April 18.