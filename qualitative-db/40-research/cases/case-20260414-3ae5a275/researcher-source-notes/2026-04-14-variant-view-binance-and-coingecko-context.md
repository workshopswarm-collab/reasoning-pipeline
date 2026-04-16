---
type: source_note
case_key: case-20260414-3ae5a275
dispatch_id: dispatch-case-20260414-3ae5a275-20260414T202946Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close be above 70000 on 2026-04-20?
driver: reliability
date_created: 2026-04-14
source_name: Binance API spot data with CoinGecko contextual pricing
source_type: market_data_plus_context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: variant-view
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-3ae5a275/researcher-analyses/2026-04-14/dispatch-case-20260414-3ae5a275-20260414T202946Z/personas/variant-view.md]
tags: [source-note, binance, coingecko, market-data, context]
---

# Summary

Binance spot API data on 2026-04-14 showed BTC/USDT around 74.3k, safely above the 70k threshold at assignment time. Recent daily candles indicate BTC has spent the last week mostly in a 70.5k-76.0k range, while CoinGecko contextual data showed BTC up roughly 8.5% over 7 days and ~4.0% over 30 days. This supports the market's bullish baseline but also shows that the buffer over 70k is only a few thousand dollars, not so large that a six-day move or a noon-minute dip is implausible.

## Key facts extracted

- Binance ticker price fetched near 74,269 BTC/USDT.
- Binance 5-minute average price fetched near 74,208.
- Recent Binance daily candles:
  - Apr 8 close ~72,963
  - Apr 9 close ~73,043
  - Apr 10 close ~70,741 after an intraday low near 70,506
  - Apr 11 close ~74,418
  - Apr 12 current-day trading had reached ~76,038 high and ~73,795 low at fetch time
- CoinGecko contextual snapshot:
  - current price ~74,235 USD
  - 7d change ~+8.5%
  - 14d change ~+9.6%
  - 30d change ~+4.0%

## Evidence directly stated by source

- Binance API returned current BTCUSDT spot and recent daily kline values.
- CoinGecko returned current BTC price and recent percentage-change context.

## What is uncertain

- These are current and recent context only; they do not directly forecast Apr. 20 noon.
- CoinGecko is contextual rather than governing for resolution.
- The Binance daily candles do not isolate the exact noon ET one-minute close condition.

## Why this source may matter

This source set anchors the current state of the underlying and helps assess whether the market's 85.5% pricing is being supported by a robust margin over the threshold or by a thinner cushion than the headline probability suggests.

## Possible impact on the question

The data support a Yes-leaning baseline because spot is comfortably above 70k today. But the margin is only around 6% above threshold, and recent realized trading ranges include sharp multi-thousand-dollar swings. That leaves meaningful residual risk for a single-minute timestamped contract six days away.

## Reliability notes

High reliability for current Binance spot context because Binance is also the governing resolution venue. Medium evidence strength for forecasting because this is still contextual/path evidence rather than direct settlement evidence.