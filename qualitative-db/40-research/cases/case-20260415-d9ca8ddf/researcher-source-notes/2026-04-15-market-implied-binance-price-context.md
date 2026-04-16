---
type: source_note
case_key: case-20260415-d9ca8ddf
dispatch_id: dispatch-case-20260415-d9ca8ddf-20260415T195847Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-17 be above 72000?
driver: reliability
date_created: 2026-04-15
source_name: Binance spot API ticker and kline context
source_type: exchange API / market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-d9ca8ddf/researcher-analyses/2026-04-15/dispatch-case-20260415-d9ca8ddf-20260415T195847Z/personas/market-implied.md]
tags: [binance, btcusdt, price-context, kline]
---

# Summary

Binance spot API data shows BTC/USDT trading materially above 72,000 on April 15, 2026, supporting the market's high Yes probability for an April 17 noon ET close above that threshold. At capture time the spot ticker was 74,931.21, and recent 1-day candles showed closes around 74.4k, 74.1k, and 74.9k after a rebound from roughly 70.7k. Recent hourly data also sat mostly in the low-to-mid 74k range.

## Key facts extracted

- Binance ticker/price endpoint returned BTCUSDT at 74,931.21.
- Binance avgPrice endpoint returned a 5-minute average around 75,031.20.
- Recent daily candles included closes of 74,417.99, 74,131.55, and 74,944.83.
- The daily low two days earlier reached roughly 70,566.99, showing the threshold is not infinitely safe even though current spot is above it.
- Recent hourly candles around the most current window were clustered near 74k rather than barely above 72k.

## Evidence directly stated by source

- Ticker endpoint: BTCUSDT 74,931.21000000.
- Daily kline data captured the recent rebound and current cushion above 72,000.
- Exchange info confirmed BTCUSDT is an active trading symbol and recent 1-minute klines were accessible.

## What is uncertain

- These are current and recent context data, not the actual resolving candle.
- BTC can move more than 3% in under two days, so current cushion does not guarantee the April 17 noon ET close remains above threshold.
- Binance API is a practical contextual source, but the contract text points users to Binance's candle display interface as the governing visible settlement surface.

## Why this source may matter

This is the strongest contextual evidence for why the market is pricing Yes at an extreme. Spot is already about 2.9k above the threshold, so the market only needs price stability or modest softness rather than a fresh rally.

## Possible impact on the question

The current level makes the market's 91%-93% probability look understandable: with BTC already near 74.9k, the contract only fails if BTC falls back below 72k by the exact noon ET minute on April 17.

## Reliability notes

High-quality direct exchange data for current price context, but still contextual rather than dispositive because the contract resolves on one future minute-candle close.