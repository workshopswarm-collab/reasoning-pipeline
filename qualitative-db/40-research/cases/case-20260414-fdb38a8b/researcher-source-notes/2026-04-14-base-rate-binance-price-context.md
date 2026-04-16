---
type: source_note
case_key: case-20260414-fdb38a8b
dispatch_id: dispatch-case-20260414-fdb38a8b-20260414T180238Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-fdb38a8b | base-rate
question: Will the Binance BTC/USDT 1-minute candle at 12:00 PM ET on 2026-04-17 close above 72000?
driver: reliability
date_created: 2026-04-14
source_name: Binance BTCUSDT API price and recent klines
source_type: exchange market data / primary contextual
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-14
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
downstream_uses: [qualitative-db/40-research/cases/case-20260414-fdb38a8b/researcher-analyses/2026-04-14/dispatch-case-20260414-fdb38a8b-20260414T180238Z/personas/base-rate.md]
tags: [binance, btcusdt, spot-price, historical-context]
---

# Summary

This source note captures the primary contextual evidence from Binance itself: current BTC/USDT level and recent realized trading range relevant to a three-day-ahead above-72k question.

## Key facts extracted

- Binance ticker price on 2026-04-14 during the run was about 74,798.68.
- Binance 5-minute average price endpoint showed about 74,766.66.
- Recent daily candles from Binance show closes of approximately:
  - Apr 8: 71,787.97
  - Apr 9: 72,962.70
  - Apr 10: 73,043.16
  - Apr 11: 70,740.98
  - Apr 12: 74,417.99
  - Apr 13: 74,798.69 intraday/current daily row for Apr 14 fetch context
- Recent hourly data on Apr 14 showed BTC/USDT trading mostly in the mid-74k to mid-75k area, with intraday highs over 76k and no sign of immediate collapse toward 72k during the sampled window.
- Relative to the 72,000 strike, current spot carried a buffer of roughly 2,800 points, or around 3.9%.

## Evidence directly stated by source

- Binance API directly reports the current BTCUSDT price.
- Binance kline endpoints directly report recent OHLC candles for 1d and 1h intervals.

## What is uncertain

- The exact resolving candle is the 12:00 PM ET 1-minute candle on Apr 17, which is not yet observable.
- Crypto can move several percent in hours, so recent trading above 72k is supportive but not dispositive.
- The API endpoints used here are not the exact UI candle surface named in Polymarket’s rule text, though they are Binance market-data endpoints for the same symbol and are a strong proxy for contextual price state.

## Why this source may matter

For a short-dated threshold market, the most important base-rate input is whether spot is already comfortably above the threshold and whether recent volatility has repeatedly revisited the strike region.

## Possible impact on the question

Because BTC is already above 72k and has recently spent multiple days near or above that level, the outside-view prior for staying above the strike three days later is favorable but not close to certainty. A one-minute noon close can still be lost through a broad crypto selloff or a sharp intraday drawdown.

## Reliability notes

High-quality as primary exchange data for current price context and recent realized ranges. Limited only by the fact that it is contextual rather than the future settlement print itself.