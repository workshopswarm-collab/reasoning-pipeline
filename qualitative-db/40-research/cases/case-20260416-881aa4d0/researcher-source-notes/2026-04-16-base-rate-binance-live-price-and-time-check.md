---
type: source_note
case_key: case-20260416-881aa4d0
dispatch_id: dispatch-case-20260416-881aa4d0-20260416T044756Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 70000?
driver: reliability
date_created: 2026-04-16
source_name: Binance API live price, server time, and recent 1-minute klines
source_type: exchange API / direct market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-881aa4d0/researcher-analyses/2026-04-16/dispatch-case-20260416-881aa4d0-20260416T044756Z/personas/base-rate.md]
tags: [binance, api, btcusdt, direct-source, source-note]
---

# Summary

This direct Binance API check shows BTC/USDT trading around 74.7k late on Apr. 15 / early Apr. 16 ET, well above the 70,000 threshold, with recent 1-minute candles also clustered near 74.7k-75.1k. It does not settle the market, but it provides the authoritative exchange context most relevant to the eventual settlement source.

## Key facts extracted

- Binance API ticker price fetched at runtime: 74,729.95 BTC/USDT.
- Binance server time at fetch: 2026-04-16T04:49:37.943Z, which is 00:49:37.943 ET on Apr. 16, 2026.
- Recent 1-minute klines were around 74,734 to 75,148 on the sampled window.
- In the sampled recent 10 one-minute candles, all closes were materially above 70,000.

## Evidence directly stated by source

Direct API outputs:
- `ticker/price` gives current Binance BTCUSDT price.
- `time` gives Binance server time.
- `klines` gives recent one-minute OHLCV candles for BTCUSDT.

## What is uncertain

- This is not the actual April 17 12:00 ET candle; it is current-state evidence only.
- BTC can move materially in less than 24 hours, so current price is only partial evidence.
- API access confirms the exchange source and present level, but not the exact UI display mechanics on the final settlement surface.

## Why this source may matter

Because the contract settles on Binance BTC/USDT, direct Binance data is the most relevant non-contract evidence for whether the threshold is likely to hold. A large current cushion above 70,000 materially raises the base-rate likelihood that the next day's noon ET close remains above that level absent a sharp selloff.

## Possible impact on the question

The live Binance level being roughly 6.8% above the threshold supports a high Yes probability. The remaining risk is ordinary BTC one-day volatility or exchange-specific operational anomalies, not lack of current price cushion.

## Reliability notes

High-value direct source because it comes from Binance API, the same venue named in the contract. Independence relative to the Polymarket rules page is medium-to-high: the rule source defines mechanics, while this source reports the actual relevant market state.