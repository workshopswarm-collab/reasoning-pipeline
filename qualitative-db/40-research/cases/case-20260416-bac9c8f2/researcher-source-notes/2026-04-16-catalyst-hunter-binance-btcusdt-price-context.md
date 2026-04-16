---
type: source_note
case_key: case-20260416-bac9c8f2
dispatch_id: dispatch-case-20260416-bac9c8f2-20260416T033803Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-74k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on April 17, 2026 be above 74000?
driver: operational-risk
date_created: 2026-04-15T23:40:00-04:00
source_name: Binance API BTCUSDT price and kline endpoints
source_type: exchange market data / direct source-of-truth proxy
source_url: https://api.binance.com/api/v3/ticker/24hr
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-bac9c8f2/researcher-analyses/2026-04-16/dispatch-case-20260416-bac9c8f2-20260416T033803Z/personas/catalyst-hunter.md]
tags: [binance, source-note, btc, market-data, resolution-mechanics]
---

# Summary

Binance market data shows BTC/USDT trading around 74,983 shortly before this note, placing spot roughly 1.3% above the 74,000 threshold for the April 17 noon-ET contract. Recent 24h range and daily candles suggest the threshold is live but not far enough away to treat a Yes outcome as mechanically locked.

## Key facts extracted

- Binance 24h ticker returned `lastPrice` 74,983.50, `highPrice` 75,425.00, `lowPrice` 73,514.00, `priceChangePercent` +1.022%.
- Recent 1-minute klines showed BTC/USDT oscillating around 74,970 to 75,011 in the latest sampled minutes.
- Recent hourly klines showed intraday trading between roughly 74,451 and 75,425 over the last 12 sampled hours.
- Recent daily candles:
  - 2026-04-13 high 74,900, close 74,417.99
  - 2026-04-14 high 76,038, close 74,131.55
  - 2026-04-15 high 75,425, close 74,809.99
  - 2026-04-16 sampled-to-date high 75,267.85, low 74,451.49, close snapshot 74,988.48

## Evidence directly stated by source

- Binance API directly publishes current BTCUSDT last price and historical candlesticks.
- The market's governing source of truth is Binance BTC/USDT 1-minute candle close for the specified noon ET minute.

## What is uncertain

- The authoritative settlement surface named by the market is the Binance trading UI candle, not explicitly the public REST API, though the API is a close direct-source proxy.
- This snapshot is about 12+ hours before the April 17 noon ET resolution minute, so intervening macro or crypto-specific volatility could still move price materially.
- A point-in-time snapshot does not establish where the exact 12:00 ET candle on April 17 will close.

## Why this source may matter

This is the best direct evidence for the contract mechanics and current starting distance from the threshold. It bounds how much adverse price movement is needed for No to win and clarifies that the market is not pricing a deeply out-of-the-money strike.

## Possible impact on the question

Current spot modestly above 74,000 supports a Yes-leaning baseline, but only moderately because BTC has traded below the threshold within the past 24 hours and resolution depends on one exact one-minute close rather than a broad daily average.

## Reliability notes

Binance is the named governing source, so source-of-truth ambiguity is low on venue but medium on implementation detail because Polymarket cites the web chart UI specifically. API data should be treated as a strong proxy and checked against the published rule text, not as an independent alternative resolver.