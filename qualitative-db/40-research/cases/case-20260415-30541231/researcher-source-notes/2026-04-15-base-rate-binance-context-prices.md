---
type: source_note
case_key: case-20260415-30541231
dispatch_id: dispatch-case-20260415-30541231-20260415T133406Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: reliability
date_created: 2026-04-15
source_name: Binance BTCUSDT kline API spot price context
source_type: exchange-market-data
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=10
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
downstream_uses: [qualitative-db/40-research/cases/case-20260415-30541231/researcher-analyses/2026-04-15/dispatch-case-20260415-30541231-20260415T133406Z/personas/base-rate.md]
tags: [binance, btcusdt, kline, source-note]
---

# Summary

This note records direct Binance market-data context used to anchor the outside-view estimate.

## Key facts extracted

Using Binance public kline API on 2026-04-15:
- 2026-04-13 daily BTC/USDT close: **74,417.99**
- 2026-04-14 daily BTC/USDT close: **74,131.55**
- 2026-04-15 partial day context from hourly candles around 13:00 UTC / 09:00 ET showed BTC/USDT trading roughly **74.0k-74.3k**.
- Recent daily closes in the preceding days included **73,043.16**, **70,740.98**, **74,417.99**, **74,131.55**, indicating BTC is already above the 72,000 threshold and not merely touching it intraday.

## Evidence directly stated by source

The Binance API returned recent BTCUSDT daily and hourly klines with open/high/low/close values. The relevant extracted values were taken directly from returned kline rows.

## What is uncertain

- This is contextual evidence, not the resolving 12:00 ET one-minute candle for April 17.
- Intraday volatility over the next ~2 days could still bring price back below 72,000 by the exact settlement minute.

## Why this source may matter

Because the contract resolves on Binance itself, Binance price context is the closest structural evidence short of the actual settling candle. It tells us whether the market is currently comfortably above or near the threshold.

## Possible impact on the question

The current distance above 72,000 matters for base-rate reasoning. A market already trading around 74k only needs BTC to avoid a drawdown of roughly 3% by the settlement minute, which is a materially easier condition than requiring an upside breakout.

## Reliability notes

High reliability as direct exchange data from the same venue named in the contract. Independence versus the contract source is limited because both point back to Binance, but that is acceptable here because Binance is the governing source of truth.
