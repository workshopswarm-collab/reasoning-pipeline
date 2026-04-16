---
type: source_note
case_key: case-20260415-b4a49d1b
dispatch_id: dispatch-case-20260415-b4a49d1b-20260415T000939Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page plus Binance BTCUSDT API check
source_type: primary_market_rules_and_exchange_data
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-b4a49d1b/researcher-analyses/2026-04-15/dispatch-case-20260415-b4a49d1b-20260415T000939Z/personas/variant-view.md]
tags: [polymarket, binance, resolution, timing, btc]
---

# Summary

This note captures the governing market wording from Polymarket and a direct Binance API verification pass to confirm what the contract is really asking and how close BTC/USDT currently sits relative to the 70,000 threshold.

## Key facts extracted

- Polymarket states the market resolves Yes if the Binance BTC/USDT 1-minute candle for **12:00 in ET timezone (noon)** on April 20 has a final **Close** price above 70,000.
- The contract is explicitly about **Binance BTC/USDT**, not other exchanges or other BTC pairs.
- Price precision is determined by Binance source precision.
- Binance API checks around 2026-04-14 20:11 ET showed BTC/USDT around **74.5k-74.6k**:
  - `/api/v3/ticker/price`: 74,567.09
  - `/api/v3/ticker/24hr`: lastPrice 74,581.95, 24h high 76,038.00, low 73,795.47
  - `/api/v3/avgPrice`: 5-minute average 74,611.00721070
- Binance server time 1776211872803 maps to **2026-04-14 20:11:12 ET**, confirming the timing conversion used in this run.

## Evidence directly stated by source

- Polymarket rules directly specify the settlement source and the material condition: the Binance BTC/USDT 1-minute candle close at 12:00 ET on April 20 must be higher than 70,000.
- Binance API directly states current spot-like reference values and recent intraday range for BTC/USDT.

## What is uncertain

- Current spot is not the same as the eventual April 20 12:00 ET 1-minute close.
- The Polymarket page is not itself the exchange source; it points to Binance as source of truth.
- The exact Binance web UI candle display can differ operationally from public API formatting, though the API strongly reduces ambiguity about pair, timing, and available price surfaces.

## Why this source may matter

This is the core rule-and-verification set for the case. It nails down the settlement mechanics, confirms the relevant pair and timing, and shows BTC currently trades well above the threshold, which explains why the market is highly priced.

## Possible impact on the question

The direct source check supports a pro-Yes baseline because BTC/USDT is currently roughly 6.5% above 70,000 with five calendar days remaining. The main variant concern is not the current level but the possibility that traders are underweighting path volatility and the fact that **all** material conditions must hold specifically at the April 20 noon ET 1-minute close on Binance.

## Reliability notes

- Polymarket market page is authoritative for contract wording but not for the final observed BTC price.
- Binance is the stated governing resolution source, so direct Binance data is the highest-value evidence in this run.
- Evidence independence is only moderate because both the contract and verification hinge on the same source-of-truth stack, but that is acceptable here because the market is explicitly source-bound.