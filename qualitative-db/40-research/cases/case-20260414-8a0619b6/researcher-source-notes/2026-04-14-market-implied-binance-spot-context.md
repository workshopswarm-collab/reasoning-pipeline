---
type: source_note
case_key: case-20260414-8a0619b6
dispatch_id: dispatch-case-20260414-8a0619b6-20260414T194140Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-18
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 70000 on 2026-04-18?
driver: reliability
date_created: 2026-04-14
source_name: Binance public API spot and recent candle data for BTCUSDT
source_type: exchange_market_data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-8a0619b6/researcher-analyses/2026-04-14/dispatch-case-20260414-8a0619b6-20260414T194140Z/personas/market-implied.md]
tags: [source-note, binance, btcusdt, spot-price]
---

# Summary

This source provides direct exchange data from the same venue and pair used for resolution. At capture time on April 14, Binance showed BTC/USDT around 74.1k, with the 24-hour low still above 72.9k and recent 1-minute closes around 74.1k-74.25k.

## Key facts extracted

- Binance ticker price response showed BTCUSDT at 74,106.66.
- Binance 24-hour ticker showed:
  - lastPrice: 74,099.78
  - openPrice: 72,982.55
  - highPrice: 76,038.00
  - lowPrice: 72,975.66
- Binance average price endpoint showed a 5-minute average around 74,156.48.
- Recent 1-minute klines showed closes in a tight band around 74.1k-74.25k.

## Evidence directly stated by source

- Direct JSON from Binance API endpoints:
  - `/api/v3/ticker/price?symbol=BTCUSDT`
  - `/api/v3/ticker/24hr?symbol=BTCUSDT`
  - `/api/v3/avgPrice?symbol=BTCUSDT`
  - `/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5`

## What is uncertain

- This is only a current snapshot four days before resolution, not the resolution candle itself.
- BTC is volatile enough that a current 5%+ cushion above the strike can shrink materially over four days.

## Why this source may matter

It is the cleanest direct evidence for whether the market-implied 90% is broadly sensible right now, because the contract settles on Binance BTC/USDT specifically.

## Possible impact on the question

A spot price near 74.1k means the market only needs BTC to avoid a drop of roughly 5.5% by noon ET on April 18. That makes a high probability reasonable, though not risk-free.

## Reliability notes

This is the strongest primary source for current state because it is the exact exchange and trading pair used for settlement. Its weakness is that it says little by itself about path-dependent risk over the next four days.