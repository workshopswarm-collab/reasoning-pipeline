---
type: source_note
case_key: case-20260415-58166133
dispatch_id: dispatch-case-20260415-58166133-20260415T083617Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-16 close above 72000?
driver: reliability
date_created: 2026-04-15
source_name: Polymarket rules page plus direct Binance API checks
source_type: mixed_primary
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, binance, resolution-source, timing]
---

# Summary

This source note combines the market rules surface from Polymarket with direct Binance API checks that mirror the contract's source of truth closely enough to audit timing and current price context.

## Key facts extracted

- Polymarket states the market resolves Yes if the Binance BTC/USDT 1 minute candle for 12:00 ET on 2026-04-16 has a final Close price above 72,000.
- The rules explicitly say the governing source is Binance BTC/USDT with 1m candles, not other exchanges or pairs.
- Direct Binance API checks on 2026-04-15 around 04:37 ET showed BTCUSDT spot around 74,112 to 74,129.
- The Binance 1m kline endpoint returned comparable noon ET candles for recent days:
  - 2026-04-13 12:00 ET candle close: 71,902.91
  - 2026-04-14 12:00 ET candle close: 75,356.48
- The target resolution time maps to 2026-04-16 16:00:00 UTC.

## Evidence directly stated by source

From Polymarket rules:
- resolution condition is strictly the Binance BTC/USDT 12:00 ET one-minute candle close
- threshold is above 72,000
- price precision is determined by the Binance source

From direct Binance API responses:
- current BTCUSDT price is materially above the threshold at the time of research
- recent one-minute and hourly candles show BTC trading in the mid-74k area with overnight range still above 73.5k in the sampled window

## What is uncertain

- The direct API checks are a close operational proxy for the named Binance candle source, but the market text specifically references the Binance trade UI candle display.
- A full day remains before settlement, so current spot being above 72k does not settle the market.
- Binance could experience data-display quirks or late candle revision risk, though that appears low for a standard BTCUSDT 1m candle.

## Why this source may matter

This is the governing contract mechanics source plus the most direct available check of the referenced exchange, pair, and timeframe logic.

## Possible impact on the question

It supports a high Yes prior because the market resolves off a single exchange/time-specific print and BTC is already roughly 3% above the threshold with recent comparable noon ET candles mostly above that level.

## Reliability notes

- Polymarket rules are authoritative for contract interpretation.
- Binance API is highly relevant for operational verification because it exposes the same BTCUSDT pair and 1m candle structure named in the contract.
- Independence between these two surfaces is medium rather than high because both ultimately point back to Binance as the governing market data source.