---
type: source_note
case_key: case-20260416-bbc8ed19
dispatch_id: dispatch-case-20260416-bbc8ed19-20260416T072336Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-bbc8ed19 | risk-manager
question: Will the price of Bitcoin be above $72,000 on April 20?
driver: reliability
date_created: 2026-04-16
source_name: Binance spot/API snapshot
source_type: exchange direct data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-bbc8ed19/researcher-analyses/2026-04-16/dispatch-case-20260416-bbc8ed19-20260416T072336Z/personas/risk-manager.md]
tags: [binance, btcusdt, price, direct-source, spot]
---

# Summary

This source provides direct current Binance BTC/USDT price context and recent 1-minute candles, which matter because the contract settles on Binance BTC/USDT specifically.

## Key facts extracted

- Binance ticker snapshot returned BTCUSDT price 74909.73 on 2026-04-16.
- Recent 1-minute UI klines showed closes around 74902.03, 74922.68, 74915.41, 74909.72, and 74909.73.
- The current spot level is roughly 2.9k above the 72,000 threshold, about 3.9% over the strike.

## Evidence directly stated by source

The exchange API directly reports the current BTCUSDT spot price and recent one-minute candle closes from Binance.

## What is uncertain

- This is not the settlement candle itself; it is only current context four days before resolution.
- Short-horizon crypto volatility can easily move several percent over four days, so current spot alone is not dispositive.

## Why this source may matter

Because the contract resolves on Binance BTC/USDT, exchange-specific spot context is more decision-relevant than generic crypto price commentary from other venues.

## Possible impact on the question

This supports a Yes lean because BTC is already above the threshold with some buffer, but it also quantifies the key fragility: only a moderate drawdown by April 20 noon ET is needed to flip the outcome to No.

## Reliability notes

High authority for direct price context because it is exchange-native data. Independence from the Polymarket rules page is limited in source class but still meaningfully separate in function: one defines mechanics, the other reports the underlying price state.