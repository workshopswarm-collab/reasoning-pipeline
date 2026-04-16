---
type: source_note
case_key: case-20260416-07c415fe
dispatch_id: dispatch-case-20260416-07c415fe-20260416T031541Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: tokens
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 12:00 ET one-minute candle on 2026-04-19 close above 80?
driver: reliability
date_created: 2026-04-16
source_name: Binance API SOLUSDT ticker and klines
source_type: exchange market data / primary resolution-adjacent source
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: supports yes
certainty: medium
importance: high
novelty: low
agent: market-implied
related_entities: [sol, solana]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, solusdt, price, klines, resolution-adjacent]
---

# Summary

Binance spot data is the most important practical evidence because the contract resolves from the Binance SOL/USDT one-minute candle at 12:00 ET on April 19. As checked on 2026-04-16 shortly after assignment time, Binance SOL/USDT was trading around 85.26, materially above the 80 threshold, and recent daily closes had mostly remained above 80.

## Key facts extracted

- Binance ticker endpoint returned `SOLUSDT = 85.26000000`.
- Recent daily kline closes from Binance:
  - Apr 2 close: 80.40
  - Apr 3 close: 80.83
  - Apr 4 close: 81.89
  - Apr 5 close: 80.03
  - Apr 6 close: 82.57
  - Apr 7 close: 83.33
  - Apr 8 close: 84.83
  - Apr 9 close: 84.93
  - Apr 10 close: 81.53
  - Apr 11 close: 86.51
  - Apr 12 close: 83.72
  - Apr 13 close: 84.90
  - Apr 14 partial/current session around assignment: 85.26
- Recent intraday 1h klines over the last ~72 hours showed trading mostly in the low-to-mid 80s, with multiple hours printing above 86.
- The recent 1m kline sample also showed current trade continuity around 85.19 to 85.27, supporting that the live ticker was not an isolated stale print.

## Evidence directly stated by source

- Current Binance spot price for SOL/USDT was above 80 by roughly 6.6% at check time.
- Binance has printed repeated daily closes above 80 for nearly two weeks, with only brief excursions toward the low 80s and upper 70s.

## What is uncertain

- This source does not directly settle the April 19 noon ET candle yet because the market is unresolved and several days remain.
- Spot can move sharply in crypto over a three-day window; present price level is supportive but not decisive.
- API data is resolution-adjacent rather than the exact UI candle view named in the market rules, though it is the same exchange and pair.

## Why this source may matter

This is the closest thing to a primary market-structure source for the actual contract: the event resolves from Binance SOL/USDT, so current Binance spot and recent Binance price path are more relevant than generic crypto commentary.

## Possible impact on the question

Strongly supports the market's high Yes probability because the contract only needs SOL/USDT to remain above 80 at one specific minute on April 19 noon ET, and current Binance trading plus recent daily closes indicate that 80 is presently below the active trading range.

## Reliability notes

- High credibility for current price/path because Binance is the named source of truth.
- Still not a final settlement source until the target minute arrives.
- Exchange-specific data matters more than cross-exchange averages here because the contract explicitly excludes other venues and pairs.