---
type: source_note
case_key: case-20260416-653ab0f8
dispatch_id: dispatch-case-20260416-653ab0f8-20260416T090226Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-18
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 72000 on April 18, 2026?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance Spot API market data and live BTCUSDT prints
source_type: primary_exchange_data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-653ab0f8/researcher-analyses/2026-04-16/dispatch-case-20260416-653ab0f8-20260416T090226Z/personas/variant-view.md]
tags: [binance, btcusdt, source-note, timing, resolution]
---

# Summary

Binance primary data shows BTC/USDT trading materially above 72,000 at assignment time, with recent daily and hourly candles centered in the mid-74k area. Binance API documentation also confirms that 1-minute klines and uiKlines can be queried with a timezone parameter, which is directly relevant to the contract’s noon ET candle wording.

## Key facts extracted

- `ticker/price` returned BTCUSDT at `74720.00000000` on 2026-04-16.
- `ticker/24hr` returned last price `74720.00000000`, 24h high `75425.00000000`, low `73580.85000000`, weighted average `74540.67858079`.
- Recent daily klines show closes of `74417.99`, `74131.55`, `74809.99`, and `74719.99` over the last several sessions, i.e. consistently above 72,000.
- Recent hourly klines show price spending most of the past ~48 hours in a band roughly from 73.5k to 76.0k, with latest hourly close `74719.99`.
- Binance API docs state `GET /api/v3/klines` and `GET /api/v3/uiKlines` support `interval=1m` and a `timeZone` parameter, with note that kline intervals are interpreted in that timezone if provided.
- A live `uiKlines` query with `interval=1m&timeZone=-4` returned minute bars, confirming ET-aligned retrieval is available for verification workflow.

## Evidence directly stated by source

- Binance is the direct price source for BTCUSDT.
- Binance exposes 1-minute close prices and timezone-aware kline interpretation.
- Current and recent realized prices are well above the 72,000 threshold.

## What is uncertain

- This source does not directly settle the April 18 noon ET candle yet because the target time has not occurred.
- Current price being above 72,000 does not guarantee remaining above 72,000 at the exact settlement minute.
- The contract text references the Binance web chart, while the API documentation is a practical verification aid rather than the literal settlement UI.

## Why this source may matter

This is the governing market data source family. It establishes both the resolution mechanics and the core state variable: BTC/USDT is already several percent above the strike, so the key issue is whether a two-day downside move is likely enough to overcome that buffer by the exact noon ET minute.

## Possible impact on the question

Directly supportive of a Yes lean. The main implication is that the market does not need further upside to resolve Yes; it only needs BTC/USDT to avoid a drop of roughly 3.6% from current spot into the settlement minute.

## Reliability notes

High reliability for direct price observation and resolution-mechanic interpretation, but still subject to ordinary exchange-data caveats and the contract’s exact dependence on the final noon ET 1-minute close rather than broader spot averages.
