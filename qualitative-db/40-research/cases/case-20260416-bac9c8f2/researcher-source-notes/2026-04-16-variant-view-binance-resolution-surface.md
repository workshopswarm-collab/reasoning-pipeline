---
type: source_note
case_key: case-20260416-bac9c8f2
dispatch_id: dispatch-case-20260416-bac9c8f2-20260416T033803Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-74k-on-april-17
question: Will the price of Bitcoin be above $74,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance API BTCUSDT price, klines, and exchange metadata
source_type: exchange-api
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: variant-view
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, resolution-source, btcusdt, 1m-candle]
---

# Summary

Binance's own public API confirms BTCUSDT was trading around $75.0k at the time of review and provides the relevant market microstructure details needed to interpret the Polymarket contract: the traded pair is BTCUSDT, the market is active, klines are timestamped in UTC, and the pair has a $0.01 price tick size.

## Key facts extracted

- `ticker/price` returned BTCUSDT spot price `75042.98` at review time.
- Recent 1-minute klines show closes clustered around `75000`-`75043`, i.e. modestly above the 74,000 threshold.
- `exchangeInfo` shows `symbol=BTCUSDT` is `TRADING` and the `PRICE_FILTER.tickSize` is `0.01000000`.
- Binance API metadata reports `timezone: UTC`, so timestamp conversion is required when mapping the Polymarket rule's 12:00 ET candle to Binance's data surfaces.

## Evidence directly stated by source

- BTCUSDT exists and is actively trading on Binance spot.
- Binance exposes 1-minute kline data for the pair.
- Price precision on this pair is at least two decimal places, relevant because the contract says resolution precision follows the source.

## What is uncertain

- The exact April 17 12:00 ET candle close is not yet observable.
- The public API is not the literal UI surface named in the Polymarket rules, so there is some residual implementation ambiguity even though both should reflect the same underlying Binance market data.
- Exchange outages, data-surface inconsistencies, or exceptional volatility near the resolution minute could still matter.

## Why this source may matter

This is the closest direct source-of-truth evidence available before resolution because the market settles from Binance BTC/USDT 1-minute candle data. It also helps audit the timing and precision mechanics rather than relying on generic BTC/USD prices from other venues.

## Possible impact on the question

At review time, BTCUSDT is only about 1.4% above the 74,000 threshold, so the market does not need a large move to flip from yes to no by the relevant noon ET close. That supports a variant caution against an overly confident yes interpretation despite spot trading above the threshold right now.

## Reliability notes

High relevance and high recency because this is a Binance-owned surface for the exact pair named in the contract. Independence is low because multiple Binance endpoints reflect the same venue rather than separate evidence streams.