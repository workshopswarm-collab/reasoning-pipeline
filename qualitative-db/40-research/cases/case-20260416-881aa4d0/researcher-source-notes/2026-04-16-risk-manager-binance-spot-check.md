---
type: source_note
case_key: case-20260416-881aa4d0
dispatch_id: dispatch-case-20260416-881aa4d0-20260416T044756Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-881aa4d0 | risk-manager
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close on April 17, 2026 be above 70000?
driver: reliability
date_created: 2026-04-16
source_name: Binance BTCUSDT price API spot check
source_type: direct exchange data / contextual verification
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-16
credibility: high
recency: current
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-881aa4d0/researcher-analyses/2026-04-16/dispatch-case-20260416-881aa4d0-20260416T044756Z/personas/risk-manager.md]
tags: [binance, direct-source, spot-price, verification]
---

# Summary

This source is a direct Binance API spot check confirming that BTC/USDT was already materially above 70,000 during the research run.

## Key facts extracted

- A direct request to Binance API returned BTCUSDT price 74911.37000000 during the run.
- This level is roughly 7.0% above the 70,000 threshold.
- The check occurred about one day before the contract observation window closes.

## Evidence directly stated by source

- Binance API response: {"symbol":"BTCUSDT","price":"74911.37000000"}

## What is uncertain

- This endpoint is not the exact settlement surface named by Polymarket, which is the Binance candles interface / underlying close for the 12:00 ET one-minute candle.
- Spot price at research time does not guarantee the later 12:00 ET candle close on April 17 remains above threshold.
- The API response is a current price snapshot, not a future or historical candle close.

## Why this source may matter

It is direct exchange data from the named venue and materially reduces the distance-to-threshold risk. It also makes the market's extreme confidence easier to understand.

## Possible impact on the question

A BTCUSDT price near 74.9k one day before settlement means Yes can still fail, but failure now requires a sizeable downside move before the exact resolution minute rather than only ordinary intraday noise.

## Reliability notes

High-value contextual verification because it comes from Binance directly, but it should be treated as contextual rather than dispositive for settlement since the contract references a specific future one-minute candle close.