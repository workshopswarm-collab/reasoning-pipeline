---
type: source_note
case_key: case-20260415-c8d6e83e
dispatch_id: dispatch-case-20260415-c8d6e83e-20260415T151858Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: btc-usdt-binance-resolution-source
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close above 68000 on April 20, 2026?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance Spot API BTCUSDT ticker and 1m klines
source_type: exchange_api
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-c8d6e83e/researcher-analyses/2026-04-15/dispatch-case-20260415-c8d6e83e-20260415T151858Z/personas/risk-manager.md]
tags: [source-note, binance, resolution-source, btc]
---

# Summary

This source note captures the governing exchange source used by the contract and verifies how Binance exposes the relevant BTC/USDT one-minute candle timestamps.

## Key facts extracted

- Binance spot ticker endpoint returned BTCUSDT at `74044.01000000` on 2026-04-15.
- Binance 1-minute klines endpoint returned recent candles with open times including `1776266400000`, which converts to `2026-04-15 11:20:00-04:00`.
- The returned kline structure includes open time, OHLC values, and close time, making it suitable for explicit minute-window verification.
- Recent sampled closes around the fetch time were all above 74k, materially above the market threshold of 68k.

## Evidence directly stated by source

- BTCUSDT ticker price: `74044.01000000`.
- Recent 1-minute kline close prices included `74169.42`, `74168.04`, `74144.65`, `74110.43`, and `74105.86`.
- The kline timestamps align with ET minute boundaries after conversion.

## What is uncertain

- This note does not itself prove what the April 20 12:00 ET candle will be; it only verifies the governing source mechanics and current margin over threshold.
- It does not independently verify Binance front-end presentation quirks versus API output, though the API is strong contextual evidence for timestamp and price formatting.

## Why this source may matter

The contract explicitly settles on the Binance BTC/USDT 12:00 ET one-minute candle close. For a narrow, date-specific market, verifying the exact source-of-truth mechanics and timezone mapping is part of the core risk check.

## Possible impact on the question

This source materially supports a bullish baseline because spot BTC/USDT is currently far above 68k, but more importantly it reduces resolution ambiguity by showing how the relevant 1-minute candle data is represented and how ET alignment can be checked.

## Reliability notes

- High credibility for contract-governing mechanics because Binance is the named resolution source.
- Some operational-risk remains because the Polymarket rule text references the Binance website UI rather than explicitly the API, so a front-end/API discrepancy or exchange data issue would still matter at the margin.