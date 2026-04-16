---
type: source_note
case_key: case-20260415-f07c9e26
dispatch_id: dispatch-case-20260415-f07c9e26-20260415T013036Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-14T21:33:00-04:00
source_name: Binance Spot API BTCUSDT ticker and 1m klines
source_type: exchange api
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=10
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
downstream_uses: []
tags: [binance, btcusdt, candles, resolution-source]
---

# Summary

This source note captures the direct exchange data source most relevant to the contract: Binance BTC/USDT spot API outputs for current price and recent 1-minute candles.

## Key facts extracted

- Binance spot ticker returned BTCUSDT price `74663.59000000` at fetch time.
- Recent 1-minute klines around the fetch showed closes in the `74648` to `74677` range.
- The kline open time `1776216600000` converts to `2026-04-14T21:30:00-04:00`, confirming the API timestamps can be mapped cleanly into ET for this style of market.
- At research time, BTC/USDT was roughly $2.66k above the contract threshold of $72,000.

## Evidence directly stated by source

- Binance API directly stated the latest spot price and recent 1-minute OHLC candle values.
- The kline endpoint directly provided timestamped 1-minute candle opens and closes needed to reason about the contract's eventual noon-ET resolution candle.

## What is uncertain

- This source does not settle the market yet because the relevant candle is the 12:00 ET candle on April 16, not the current candle.
- API output is strongly informative for current distance-from-threshold but does not by itself prove where BTC/USDT will trade at resolution.
- The market text points users to the Binance web trading interface; while the API appears aligned, final settlement will depend on the exchange surface Polymarket uses from Binance at resolution time.

## Why this source may matter

This is the closest available direct source to the contract's governing settlement surface. It is the best evidence for where BTC is trading relative to the threshold and for verifying the practical meaning of the 1-minute-candle mechanic.

## Possible impact on the question

Given BTC/USDT was trading materially above $72,000 and nearby 1-minute closes were stable in the mid-$74k area, this source supports the market's high implied probability that the noon-ET April 16 close will still be above $72,000 absent a sharp adverse move.

## Reliability notes

- High credibility as first-party exchange data from Binance.
- Main residual risk is operational/settlement-surface alignment between Binance API data now and the Binance interface candle Polymarket will actually inspect at settlement.
- Independence is limited because this is the same underlying venue referenced by the contract, so it is authoritative for mechanics but not independent corroboration of future price behavior.
