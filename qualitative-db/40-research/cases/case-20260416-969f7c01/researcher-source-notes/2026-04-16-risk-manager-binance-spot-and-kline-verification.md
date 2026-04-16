---
type: source_note
case_key: case-20260416-969f7c01
dispatch_id: dispatch-case-20260416-969f7c01-20260416T013210Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: spot-market-structure
entity: ethereum
topic: case-20260416-969f7c01 | risk-manager
question: Will the Binance ETH/USDT 1-minute candle closing at 12:00 ET on 2026-04-17 close above 2200?
driver: reliability
date_created: 2026-04-15
source_name: Binance spot API ticker and klines
source_type: exchange market data / authoritative settlement-adjacent source
source_url: https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: supports-yes
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [ethereum]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-969f7c01/researcher-analyses/2026-04-16/dispatch-case-20260416-969f7c01-20260416T013210Z/personas/risk-manager.md]
tags: [source-note, binance, ticker, klines, verification]
---

# Summary

Direct Binance spot data shows ETH/USDT trading around 2353.68 at research time, roughly 7% above the 2200 threshold. Recent hourly and minute-level klines show ETH trading in the low-to-mid 2300s rather than hovering just above 2200.

## Key facts extracted

- Binance ticker endpoint returned ETHUSDT price 2353.68000000.
- Recent 1-hour klines in the fetch window showed repeated closes around roughly 2334 to 2391+.
- Recent 1-minute klines in the fetch window showed prices centered around roughly 2350-2355.
- The contract threshold of 2200 is therefore more than 150 points below the observed spot level at research time.

## Evidence directly stated by source

- Current Binance spot price at fetch time.
- Recent historical kline closes from Binance.
- Binance API documentation states klines are uniquely identified by open time and supports a timeZone parameter; start/end remain UTC even when timezone is specified.

## What is uncertain

- This is not tomorrow’s noon candle; it only establishes current distance from threshold and recent realized trading range.
- Crypto can move sharply in 24 hours, so current cushion is strong but not dispositive.

## Why this source may matter

Because the contract resolves on Binance ETH/USDT, direct Binance data is the most decision-relevant evidence short of the actual settlement candle itself.

## Possible impact on the question

Current spot and recent intraday range materially support Yes because ETH would need a sizable adverse move before 12:00 ET on April 17 to fall to or below 2200. The main remaining risks are a sharp drawdown, regime shock, or resolution/timestamp edge-case rather than slow drift.

## Reliability notes

High-quality source for this case because it is the exchange referenced by contract. Still only settlement-adjacent until the specific noon ET candle exists.