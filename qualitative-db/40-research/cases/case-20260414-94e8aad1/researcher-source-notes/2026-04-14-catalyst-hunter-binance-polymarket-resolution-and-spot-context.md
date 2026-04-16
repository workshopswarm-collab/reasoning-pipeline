---
type: source_note
case_key: case-20260414-94e8aad1
dispatch_id: dispatch-case-20260414-94e8aad1-20260414T175223Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-16 close above 70000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket rules page + Binance API spot/market-data endpoints
source_type: primary_and_resolution_context
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-94e8aad1/researcher-analyses/2026-04-14/dispatch-case-20260414-94e8aad1-20260414T175223Z/personas/catalyst-hunter.md]
tags: [polymarket, binance, resolution, btc, timing]
---

# Summary

This source note captures the core settlement mechanics and current spot context for the April 16 BTC > 70k market.

## Key facts extracted

- Polymarket states the market resolves to Yes if the Binance BTC/USDT **1-minute candle for 12:00 in ET timezone (noon)** on April 16 has a final **Close** price higher than 70,000.
- The resolution source is Binance BTC/USDT with **1m** candles selected.
- The contract is explicitly about **Binance BTC/USDT**, not other exchanges or pairs.
- Binance API spot ticker fetched on 2026-04-14 showed BTCUSDT around **74,664.74**.
- Binance 1-minute kline endpoint returned recent closes in the **74.65k-74.70k** area.
- Binance exchange info for BTCUSDT shows **tickSize 0.01**, relevant to price precision.

## Evidence directly stated by source

- Polymarket rules explicitly specify the settlement surface and all material conditions: instrument, venue, candle frequency, timezone, and close-price threshold logic.
- Binance endpoints directly state current BTCUSDT price and recent 1-minute candles.

## What is uncertain

- The Polymarket page does not itself explain whether Binance UI timezone selection could differ from API UTC timestamps, so mapping noon ET to the relevant minute remains an operational interpretation risk to monitor.
- Current price is only a snapshot and not predictive by itself.

## Why this source may matter

This is the governing source-of-truth set for the contract. It also establishes that BTC is currently about 4.6k above the strike, making the key catalyst question whether a >6% drawdown can occur before the noon ET fixing minute on April 16.

## Possible impact on the question

The combination of explicit Binance settlement rules and a current spot price near 74.7k pushes the baseline toward Yes unless a near-term negative catalyst or exchange-specific dislocation appears.

## Reliability notes

- Polymarket rules page is the best direct contract-mechanics source available.
- Binance API is the most direct machine-readable price source related to the settlement venue, though final settlement references the Binance chart/candle surface rather than this API endpoint verbatim.
- Independence is limited because both price checks are Binance-linked, but that is acceptable here because the market itself is Binance-defined.