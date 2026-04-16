---
type: source_note
case_key: case-20260416-cd7fa6c7
dispatch_id: dispatch-case-20260416-cd7fa6c7-20260416T010113Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-74k-on-april-17
question: Will the price of Bitcoin be above $74,000 on April 17?
driver: reliability
date_created: 2026-04-15
source_name: Binance BTCUSDT API spot and kline snapshots
source_type: exchange market data
source_url: https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-cd7fa6c7/researcher-analyses/2026-04-16/dispatch-case-20260416-cd7fa6c7-20260416T010113Z/personas/catalyst-hunter.md]
tags: [binance, btcusdt, spot, kline, price-level]
---

# Summary

Direct Binance market data showed BTC/USDT trading slightly above the contract strike around the research timestamp, but only by a modest margin. Recent daily action showed a rebound from roughly 70.7k on April 12 to 74.8k on April 15, with intraday trading on April 16 around 74.5k and a 24-hour range of roughly 73.5k to 75.4k.

## Key facts extracted

- Binance 24-hour ticker last price was about 74,541.59 at the check time.
- Binance best bid/ask snapshot was roughly 74,500.50 / 74,500.51, confirming spot trading near 74.5k.
- Recent daily closes from Binance were:
  - Apr 12: 70,740.98
  - Apr 13: 74,417.99
  - Apr 14: 74,131.55
  - Apr 15: 74,809.99
- Current-day Apr 16 intraday data showed BTC slipping from the prior daily close and trading near 74.5k.
- 24-hour ticker range was high 75,425 and low 73,514.

## Evidence directly stated by source

The Binance API returned BTCUSDT lastPrice near 74.54k, highPrice 75.425k, lowPrice 73.514k, and priceChangePercent about -0.233% over 24 hours. Depth data showed a live order book centered almost exactly at 74.5k.

## What is uncertain

- This snapshot is not the resolving candle itself; it is only contextual evidence one day early.
- Crypto trades continuously, so a one-day-forward noon print can still swing materially on macro headlines, ETF flow narratives, or liquidation cascades.

## Why this source may matter

Because the contract resolves from Binance itself, contemporaneous Binance price context is the most relevant direct evidence short of the actual resolving minute. It frames whether the market is asking for a large move or just stability above the strike.

## Possible impact on the question

With spot already above 74k but not far above it, the contract looks close to a coin flip plus modest edge rather than an easy Yes. The key practical question becomes whether BTC can hold that level through the next roughly 35 hours and specifically into noon ET.

## Reliability notes

High reliability for current spot context because it comes directly from Binance APIs, which are closer to the governing source than third-party aggregators. Limited because it is still a pre-resolution snapshot rather than the actual settling candle.