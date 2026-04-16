---
type: source_note
case_key: case-20260415-bebdf03e
dispatch_id: dispatch-case-20260415-bebdf03e-20260415T221944Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-bebdf03e | market-implied
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 72000 on April 21, 2026?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance API BTCUSDT price and recent klines
source_type: exchange market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: supports-yes
certainty: medium
importance: high
novelty: medium
agent: market-implied
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-bebdf03e/researcher-analyses/2026-04-15/dispatch-case-20260415-bebdf03e-20260415T221944Z/personas/market-implied.md]
tags: [binance, btcusdt, price-level, source-note]
---

# Summary

Binance market data shows BTC/USDT trading near 75,012 on 2026-04-15, comfortably above the 72,000 threshold, with recent daily closes mostly above 72,000 since April 10 and recent highs extending above 76,000.

## Key facts extracted

- Spot price from Binance ticker endpoint during this run: 75,012.21.
- Recent daily closes from Binance API:
  - 2026-04-09: 71,787.97
  - 2026-04-10: 72,962.70
  - 2026-04-11: 73,043.16
  - 2026-04-12: 70,740.98
  - 2026-04-13: 74,417.99
  - 2026-04-14: 74,131.55
  - 2026-04-15: 75,006.44 at time of query
- Recent range remains wide enough to matter: 2026-04-15 daily low was 73,514 and recent 14-day low was 65,712.12.

## Evidence directly stated by source

- Binance API directly reports current BTCUSDT price and recent OHLCV values.
- These data are directly relevant because the market also resolves using Binance BTC/USDT rather than another venue.

## What is uncertain

- The contract resolves on the 12:00 ET 1-minute candle close on April 21, not current spot or daily close.
- Short-horizon volatility could still bring price below 72,000 by the relevant minute.
- API data used here is not the exact UI candle view named in the contract, though it is the same exchange/pair family.

## Why this source may matter

This is the closest direct evidence to the governing source of truth because it uses Binance BTC/USDT data. It supports the idea that the market is pricing from a live level already well above the threshold, while also showing that recent volatility is large enough that certainty should not be pushed too high.

## Possible impact on the question

Current Binance pricing materially supports a Yes lean and helps explain why the market is near 81.5%, but the recent range also argues against treating the contract as almost certain.

## Reliability notes

High relevance and recency. Strong source fit because the market resolves from Binance BTC/USDT. Main caveat is that the exact settlement object is a specific 1-minute candle close at noon ET on April 21, so this source is strong context rather than direct settlement evidence today.