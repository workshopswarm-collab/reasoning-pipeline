---
type: source_note
case_key: case-20260415-f07c9e26
dispatch_id: dispatch-case-20260415-f07c9e26-20260415T013036Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-16 close above 72000?
driver: reliability
date_created: 2026-04-15
source_name: Binance spot API kline and ticker endpoints
source_type: exchange market data / direct source-of-truth surface
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=10
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, market-data, kline, ticker, source-of-truth]
---

# Summary

This source provides direct Binance BTC/USDT pricing close to run time and is the nearest accessible authoritative proxy for the eventual resolution source.

## Key facts extracted

- Binance ticker at research time showed BTCUSDT around 74,620.39.
- Recent 1-minute Binance klines around 2026-04-14 21:30-21:34 ET showed closes between roughly 74,620 and 74,678.
- That level is about 2,620 points above the 72,000 threshold, roughly a 3.6% cushion.
- Timestamp conversion confirms the returned kline times map cleanly from UTC to ET and that 12:00 ET on Apr 16 would correspond to 16:00 UTC while daylight saving time is active.

## Evidence directly stated by source

- Direct Binance market data places BTC/USDT materially above the contract threshold with less than 15 hours remaining until the settlement candle.
- Binance kline timestamps are machine-readable and compatible with explicit timezone conversion.

## What is uncertain

- This does not yet show the actual Apr 16 12:00 ET settlement candle because that time has not occurred.
- Binance API access is a direct data surface but not literally the exact UI path named in the Polymarket rule text.

## Why this source may matter

This is the most decision-relevant direct evidence because the contract settles on Binance BTC/USDT one-minute closes, and current Binance price level determines how much path risk remains.

## Possible impact on the question

With BTC/USDT already trading well above 72,000, the market only flips to No if Bitcoin falls materially before noon ET on Apr 16 and stays low enough for that exact settlement candle to close below the line.

## Reliability notes

High relevance and high credibility for direct pricing. Main residual risk is not data quality but path dependence between now and the specific settlement minute.