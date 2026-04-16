---
type: source_note
case_key: case-20260414-3ae5a275
dispatch_id: dispatch-case-20260414-3ae5a275-20260414T202946Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 1-minute candle close at 12:00 PM ET on 2026-04-20 above 70000?
driver: reliability
date_created: 2026-04-14
source_name: Binance API daily candles and spot ticker; CoinGecko 30-day market chart
source_type: exchange data + independent contextual market data
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=30
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [base-rate-finding]
tags: [binance, coingecko, btc-price, base-rate, verification]
---

# Summary

Recent price context strongly favors the Yes side on an outside-view basis because BTC/USDT is already materially above 70,000 and has spent much of the past month at or above that level, including multiple recent daily closes in the low-to-mid 70s.

## Key facts extracted

- Binance spot ticker around analysis time showed **BTCUSDT near 74,250**.
- Binance 30-day daily candles show BTC traded both below and above 70,000 over the last month, but several recent sessions closed **above 70,000**.
- From the extracted daily series, BTC daily closes below 70,000 were common in late March and early April, but the most recent cluster has shifted upward into the **71k-74k** range.
- The last several daily closes before analysis include approximately **71,924**, **71,069**, **71,788**, **72,963**, **73,043**, **70,741**, **74,418**, and **74,250**.
- CoinGecko's 30-day market chart broadly agrees with Binance on the level and recent upward regime, providing an independent contextual cross-check.

## Evidence directly stated by source

- Binance directly reports current BTCUSDT spot and recent daily OHLC data.
- CoinGecko independently reports a similar 30-day price path for BTC in USD.

## What is uncertain

- Daily closes are only a contextual proxy; the contract resolves on a specific 1-minute close at noon ET on April 20.
- Crypto can move several thousand dollars over six days, so current cushion above 70,000 does not guarantee a Yes resolution.
- CoinGecko is not the settlement source and BTC/USD is not perfectly identical to BTC/USDT, though for context the distinction is usually small.

## Why this source may matter

This is the most relevant base-rate context: where BTC is trading now relative to the threshold, and how often the asset has recently spent time above or below that line.

## Possible impact on the question

The current level around 74.25k gives the market roughly a 4.25k cushion over the threshold with six days remaining. Base rate alone therefore supports a high Yes probability, but not near-certainty, because BTC has shown recent multi-day excursions into the 66k-69k range.

## Reliability notes

Binance is the best available primary price source because it is also the governing settlement venue. CoinGecko is a useful independent contextual check. Evidence independence is medium rather than high because both ultimately reflect broad BTC spot market conditions, but they are operationally distinct data surfaces.