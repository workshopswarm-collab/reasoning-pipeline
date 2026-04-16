---
type: source_note
case_key: case-20260415-1cbf2a82
dispatch_id: dispatch-case-20260415-1cbf2a82-20260415T144104Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-17 be above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance public API market data
source_type: exchange_market_data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=14
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-1cbf2a82/researcher-analyses/2026-04-15/dispatch-case-20260415-1cbf2a82-20260415T144104Z/personas/base-rate.md]
tags: [binance, btcusdt, market-data, direct-evidence]
---

# Summary

Direct exchange data shows BTC/USDT already trading above the contract threshold on 2026-04-15, with spot at about 74,002 and multiple recent daily closes above 72,000. This matters because the market resolves on a specific Binance BTC/USDT print, so current level versus threshold is the core direct evidence.

## Key facts extracted

- Binance ticker price at retrieval: `74002.00000000` for BTCUSDT.
- Recent daily closes from Binance public klines (latest 14):
  - 2026-04-06 close `71924.22`
  - 2026-04-08 close `71787.97`
  - 2026-04-09 close `72962.70`
  - 2026-04-10 close `73043.16`
  - 2026-04-12 close `74417.99`
  - 2026-04-13 close `74131.55`
  - 2026-04-14 intraday retrieval day spot around `74002.00`
- In the last ~9 completed daily candles before retrieval, BTC closed above 72,000 on 5 of them.
- Recent daily range remains material: examples include 2026-04-10 low `70505.88` and 2026-04-12 high `76038.00`.

## Evidence directly stated by source

- Binance public API directly states current BTCUSDT price and recent daily OHLCV values.
- The source does not directly state the April 17 noon ET candle outcome; it provides current level and recent volatility context.

## What is uncertain

- The contract resolves on the 12:00 ET 1-minute candle close on 2026-04-17, not on current spot or daily close.
- A 2-day horizon leaves meaningful room for a move below 72,000 even if BTC is above that level now.
- Public API and website display should align, but the market rules point specifically to Binance website candles rather than the API endpoint.

## Why this source may matter

This is the closest thing to primary market-state evidence because the contract explicitly uses Binance BTC/USDT as source of truth.

## Possible impact on the question

Being ~2.8% above the threshold with several recent closes above 72,000 supports a high-but-not-certain Yes prior. It argues against an outside-view estimate far below the market, but recent daily swings show the event is still meaningfully losable over two trading days.

## Reliability notes

- High credibility for direct price state because Binance is the governing exchange in the contract.
- Slight implementation ambiguity remains because resolution references the website 1-minute candle, not the API specifically, though these should ordinarily be sourced from the same underlying market data.