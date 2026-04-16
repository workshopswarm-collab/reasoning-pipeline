---
type: source_note
case_key: case-20260415-10579f0a
dispatch_id: dispatch-case-20260415-10579f0a-20260415T184424Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-17 close above 70000?
driver: reliability
date_created: 2026-04-15
source_name: Binance public API spot and kline check
source_type: authoritative exchange market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, btcusdt, market-data, authoritative-source]
---

# Summary

A direct Binance API check showed BTC/USDT at 74,338.37 on 2026-04-15, comfortably above the 70,000 threshold two days before resolution. Recent 1-minute klines also showed stable trading in the 74.3k area during the check window.

## Key facts extracted

- Binance ticker endpoint returned `{"symbol":"BTCUSDT","price":"74338.37000000"}`.
- Recent 1-minute klines were all around 74.30k-74.34k during the fetch window.
- Recent daily klines from Binance showed closes of 72,962.70 on Apr 10, 73,043.16 on Apr 11, 70,740.98 on Apr 12, 74,417.99 on Apr 13, 74,131.55 on Apr 14, with Apr 15 trading around 74,338 during the intraday check.
- ET noon on 2026-04-17 corresponds to **16:00 UTC**, which is the candle time that will matter if Binance timestamps are checked in UTC.

## Evidence directly stated by source

- Direct exchange-reported spot price was above 70,000 by roughly 4,338 points at check time.
- Recent realized trading range across the last several days stayed above 70,000 on daily closes, though Apr 12 dipped intraday below it before recovering to a close just above 70,740.

## What is uncertain

- This does not settle the future 2026-04-17 16:00 UTC one-minute close.
- Crypto can move sharply within 48 hours, so current spot only provides margin-to-threshold context rather than certainty.

## Why this source may matter

This is the most relevant direct source for both current price level and the eventual resolution source family, because the contract explicitly points to Binance BTC/USDT candles.

## Possible impact on the question

With spot around 74.3k, the market only fails if BTC sells off by more than about 5.8% by the relevant minute close. That makes the key catalyst question less about ordinary noise and more about whether a specific downside trigger appears before Friday noon ET.

## Reliability notes

High reliability for current exchange price and highly relevant because Binance is also the stated source-of-truth family for settlement. Main residual risk is not data quality but future price volatility and exact candle timing.