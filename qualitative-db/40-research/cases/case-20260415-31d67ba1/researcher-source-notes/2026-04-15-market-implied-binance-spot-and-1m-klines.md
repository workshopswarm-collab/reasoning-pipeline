---
type: source_note
case_key: case-20260415-31d67ba1
dispatch_id: dispatch-case-20260415-31d67ba1-20260415T185542Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the price of Bitcoin be above $70,000 on April 17?
driver: reliability
date_created: 2026-04-15
source_name: Binance BTCUSDT ticker and 1m klines
source_type: exchange API / settlement-source context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: market-implied
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-31d67ba1/researcher-analyses/2026-04-15/dispatch-case-20260415-31d67ba1-20260415T185542Z/personas/market-implied.md]
tags: [binance, btcusdt, settlement-source, price]
---

# Summary

Binance spot data shows BTC/USDT around 74,374 on Apr 15, roughly 6.25% above the 70,000 threshold, and recent 1-minute candle closes in the 74,352-74,374 range.

## Key facts extracted

- Binance ticker price at fetch time: 74,374.14.
- Recent 1-minute closes fetched from Binance API: 74,351.78; 74,374.14; 74,369.97.
- The market settles off Binance BTC/USDT, so this is the most decision-relevant current spot reference.
- Current spot is about 4,374 points above the threshold.

## Evidence directly stated by source

- Direct exchange pricing shows BTC is currently above 70,000 by a substantial margin.
- Direct recent 1m candles illustrate that, at least at fetch time, ordinary minute-to-minute movement is occurring around mid-74k rather than near the threshold.

## What is uncertain

- Current spot does not guarantee the exact Apr 17 12:00 ET close.
- BTC can move materially over ~41 hours, so this source is direct on current level but only contextual for settlement.

## Why this source may matter

This is the named settlement venue and pair, so current Binance BTC/USDT level is the strongest direct evidence for why a 97% market price may be rational.

## Possible impact on the question

Given current spot around 74.37k, the contract only fails if BTC/USDT falls more than roughly 5.9% by the exact settlement minute, or if Binance-specific market conditions create an idiosyncratic print at or below 70,000.

## Reliability notes

High-quality and highly relevant because Binance is the explicit source of truth for settlement. Limitation: still not the future settlement print itself.