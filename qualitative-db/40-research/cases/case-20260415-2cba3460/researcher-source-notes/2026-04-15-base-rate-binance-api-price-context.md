---
type: source_note
case_key: case-20260415-2cba3460
dispatch_id: dispatch-case-20260415-2cba3460-20260415T115730Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-16 close above 72000?
driver: reliability
date_created: 2026-04-15
source_name: Binance spot API price and kline endpoints
source_type: exchange API / authoritative market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, market-data, price, kline]
---

# Summary

This source set is the closest direct source-of-truth surface available during research because the contract resolves off Binance BTC/USDT candles. It shows BTC/USDT trading materially above 72,000 on April 15 and gives recent daily and hourly context.

## Key facts extracted

- Binance ticker price checked during research: about **74,187.69**.
- Binance 24h stats showed last price about **74,187.69**, 24h high about **76,038**, low about **73,514**, and open about **74,448.65**.
- Recent daily closes from Binance were:
  - 2026-04-10: **72,962.70**
  - 2026-04-11: **73,043.16**
  - 2026-04-12: **70,740.98**
  - 2026-04-13: **74,417.99**
  - 2026-04-14: **74,131.55**
  - 2026-04-15 (intraday check): about **74,187.69**
- In a 120-day sample of Binance daily closes, **59 / 120** daily closes were above 72,000 (~49%).
- In the most recent 20 daily closes, **5 / 20** were above 72,000 (25%), but the latest several sessions have mostly been above the threshold after a rebound.
- For the recent eight comparable **16:00 UTC** checkpoints (the UTC equivalent of **12:00 ET** during daylight saving time), 5 of 8 observed hourly closes were above 72,000.
- Explicit time conversion check: **2026-04-16 12:00 ET = 2026-04-16 16:00 UTC**, so the relevant Binance 1m candle should open at **1776355200000 ms** and close at 16:00:59.999 UTC.

## Evidence directly stated by source

- Binance BTC/USDT is currently above the target threshold by more than 2,000.
- Binance provides the direct price series and timestamp structure needed for the contract.

## What is uncertain

- This does not directly observe the future April 16 noon ET candle.
- Daily-close and hourly-close frequencies are only rough reference classes, not exact one-minute noon-on-date analogs.

## Why this source may matter

The market resolves to Binance. For a near-dated threshold market, the best outside-view anchor is the current Binance level plus recent frequency of staying above the threshold at similar horizons, not broad macro storytelling.

## Possible impact on the question

The fact that BTC is already trading well above 72,000 one day before resolution supports a high Yes probability, but the recent sample also shows that being above the line is not guaranteed and can reverse quickly enough to keep No materially live.

## Reliability notes

High credibility and high recency. This is the best available direct data source short of observing the exact settlement candle itself.