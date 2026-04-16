---
type: source_note
case_key: case-20260415-2ce6159e
dispatch_id: dispatch-case-20260415-2ce6159e-20260415T142913Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-16 be above 72000?
driver: reliability
date_created: 2026-04-15
source_name: Binance public API price and 1-minute kline checks
source_type: exchange API / primary market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, price-data, kline, resolution-source, verification]
---

# Summary

This source note captures a direct Binance verification pass. Around 10:30 ET on 2026-04-15, BTC/USDT on Binance was roughly 74.4k, with the Binance 1-minute candle for 10:30 ET closing at 74,380.97. That places spot comfortably above the 72,000 strike roughly 25.5 hours before the resolution minute.

## Key facts extracted

- Binance ticker price returned 74,380.98 USDT for BTCUSDT.
- Binance 1-minute kline for timestamp 2026-04-15 10:30:00 ET had close 74,380.97.
- Binance 24h ticker showed high 76,038, low 73,514, last price ~74,402.68, and a 24h move of about -1.96% at time of check.
- Binance avgPrice endpoint returned about 74,449.67 over the prior 5 minutes.
- Exchange info confirms BTCUSDT spot trading is active and tick size is 0.01, implying cent-level precision for the threshold comparison.

## Evidence directly stated by source

Direct API outputs checked during the run:
- ticker/price: 74,380.98
- 1m kline for 2026-04-15 10:30 ET: close 74,380.97
- 24h low: 73,514.00
- exchangeInfo PRICE_FILTER tickSize: 0.01000000

## What is uncertain

- This is a current-state snapshot, not the actual April 16 noon ET settlement candle.
- Intraday crypto volatility can move BTC by several percent in a day, so being above 72,000 now does not guarantee staying above it at the exact resolution minute.

## Why this source may matter

This is the most directly relevant non-contract source because the contract itself settles on Binance BTC/USDT. It shows the current margin above strike and gives a base-rate sense of how much downside room exists before No becomes more likely.

## Possible impact on the question

With BTC around 74.4k and the prior 24h low still above 73.5k, Yes starts from a favorable position. For No to win, BTC would need to fall more than about 3.2% from the checked spot level and still be below 72,000 exactly at the April 16 12:00 ET close minute on Binance.

## Reliability notes

High credibility and direct relevance because this is Binance market data from the same venue/pair used for resolution. Independence from the contract source is only partial because both point back to Binance for settlement logic, but this is still the right primary evidence set for a rule-sensitive market.