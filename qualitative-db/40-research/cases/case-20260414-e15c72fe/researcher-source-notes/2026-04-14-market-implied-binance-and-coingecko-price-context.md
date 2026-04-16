---
type: source_note
case_key: case-20260414-e15c72fe
dispatch_id: dispatch-case-20260414-e15c72fe-20260414T193100Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: reliability
date_created: 2026-04-14
source_name: Binance API daily/spot data and CoinGecko spot cross-check
source_type: exchange API plus market-data aggregator
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-14
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
downstream_uses: [market-implied-finding]
tags: [binance, coingecko, btc, spot, verification]
---

# Summary

A direct Binance API check showed BTCUSDT at 74,258.35 at research time, comfortably above the $70,000 threshold. A 7-day daily kline pull showed BTC/USDT daily closes mostly above $70,000 and recent highs up to 76,038. A CoinGecko cross-check printed BTC/USD at 74,215 with a positive 24-hour change, confirming broader market context consistent with Binance.

## Key facts extracted

- Binance spot ticker returned `{"symbol":"BTCUSDT","price":"74258.35000000"}`.
- Binance 7-day daily klines showed closes of approximately 71,069.93, 71,787.97, 72,962.70, 73,043.16, 70,740.98, 74,417.99, and 74,258.35.
- The sampled 7-day lows included values slightly above and below 70,000, with the weakest day low near 70,466 and another near 70,506; this indicates the threshold is not absurdly far away, even if current spot is well above it.
- CoinGecko returned `{"bitcoin":{"usd":74215,"usd_24h_change":1.6112879548238634}}`.

## Evidence directly stated by source

- Binance provides direct exchange price data for the exact BTC/USDT venue named in the contract.
- CoinGecko provides a contextual cross-check that broader market pricing is in the same area as Binance.

## What is uncertain

- The Binance API check here was spot-at-research-time and daily candles, not the exact April 20 noon ET 1-minute close that will settle the contract.
- Daily klines smooth intraday volatility and do not show whether the precise noon minute could briefly print below 70,000.

## Why this source may matter

This is the strongest direct support for why the market is pricing the contract as likely Yes: current price is roughly 6% above the threshold with only six calendar days until resolution. The daily kline context suggests the threshold is within normal volatility reach but not currently close enough to make the market's optimism look obviously reckless.

## Possible impact on the question

These sources support a high Yes probability and explain why market participants may reasonably cluster in the mid-80s to around 90% range, while still leaving room for a nontrivial No tail tied to crypto volatility and the very specific minute-based settlement rule.

## Reliability notes

Binance is highly relevant because it is both the trading venue named in the contract and the settlement source. CoinGecko is not the settlement source but is a useful independent contextual check that the Binance reading is not an isolated data artifact.