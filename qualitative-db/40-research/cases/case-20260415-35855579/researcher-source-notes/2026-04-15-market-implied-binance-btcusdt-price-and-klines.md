---
type: source_note
case_key: case-20260415-35855579
dispatch_id: dispatch-case-20260415-35855579-20260415T225312Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-35855579 | market-implied
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close above 72000 on 2026-04-16?
driver: reliability
date_created: 2026-04-15
source_name: Binance API BTCUSDT price and recent 1m klines
source_type: exchange market data / direct exchange API
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: supports-yes
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-35855579/researcher-analyses/2026-04-15/dispatch-case-20260415-35855579-20260415T225312Z/personas/market-implied.md]
tags: [binance, btcusdt, market-data, resolution-source]
---

# Summary

Direct Binance API checks on 2026-04-15 showed BTC/USDT trading materially above 72,000 ahead of the Apr 16 noon ET resolution window, with recent one-minute candles clustering around 75,100.

## Key facts extracted

- Binance `ticker/price` returned `{"symbol":"BTCUSDT","price":"75124.27000000"}`.
- Binance `time` returned server time `1776293677342`, which converts to `2026-04-15T22:54:37.342Z`.
- Binance `klines?symbol=BTCUSDT&interval=1m&limit=5` returned five recent one-minute candles with closes between roughly `75085.68` and `75133.18`.
- These direct exchange prints were about 3,124 points above the 72,000 threshold roughly 13 hours before the noon ET settlement candle.

## Evidence directly stated by source

- Current Binance spot price at check time was 75,124.27 USDT per BTC.
- Recent one-minute candles were consistently in the low 75,000s rather than near the strike.
- Binance provides the exact one-minute kline structure that matches the market's specified source-of-truth family.

## What is uncertain

- The market resolves on the Apr 16 12:00 ET candle close, not the Apr 15 evening price.
- Spot BTC can still move several percent overnight and into the next morning.
- The Polymarket wording references the Binance web chart surface rather than the public API specifically, though both should reflect the same underlying one-minute market data unless there is an operational discrepancy.

## Why this source may matter

This is the closest available direct source to the stated resolution source. It establishes that the market is currently far above the strike and that the crowd is not pricing an immediately knife-edge outcome.

## Possible impact on the question

If Binance remains in the current trading neighborhood through the next day, the market should resolve Yes. The main way this source could mislead is if a sharp selloff of more than about 4% occurs before the relevant noon ET close, or if there is an exchange-display / resolution-surface discrepancy.

## Reliability notes

- High relevance because Binance is the named resolution venue.
- High recency because the data was pulled during the research run.
- Independence is limited: this is one venue and one data family, so contextual cross-checks are still useful for judging whether the market price is stale or sensible.
