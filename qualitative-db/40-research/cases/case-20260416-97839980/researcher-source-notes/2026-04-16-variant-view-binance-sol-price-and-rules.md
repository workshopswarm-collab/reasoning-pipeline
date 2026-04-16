---
type: source_note
case_key: case-20260416-97839980
dispatch_id: dispatch-case-20260416-97839980-20260416T040518Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: trading
entity: sol
topic: solana-above-80-on-april-19
question: Will the price of Solana be above $80 on April 19?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance SOL/USDT API and Polymarket rules
source_type: primary_market_and_resolution_source
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [sol, solana]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, polymarket, resolution-source, sol]
---

# Summary

This source note captures the governing resolution mechanics and the most relevant near-term Binance price context for the April 19 SOL > $80 contract.

## Key facts extracted

- Polymarket resolves this market using the Binance SOL/USDT 1-minute candle for **12:00 ET (noon)** on April 19, 2026.
- The relevant value is the candle's final **Close** price, not the intraminute high, low, or another exchange's quote.
- Binance API snapshot fetched on 2026-04-16 showed SOLUSDT at **85.39**.
- Recent Binance daily closes fetched from the official Binance API show SOL trading above 80 for all of the last 10 daily observations in the fetched window, with closes including 85.56, 82.57, 83.33, 84.83, 84.93, 81.53, 86.51, 83.72, 84.90, and partial-current 85.39.

## Evidence directly stated by source

- Binance ticker endpoint directly reported `{"symbol":"SOLUSDT","price":"85.39000000"}`.
- Binance daily klines directly reported repeated closes above 80 in the recent sample.
- Polymarket rules directly specify Binance SOL/USDT, 1m candle, 12:00 ET, and Close price as the source of truth.

## What is uncertain

- The decisive value is the April 19 12:00 ET 1-minute close, which has not happened yet.
- The fetched daily klines are contextual rather than the exact settlement candle.
- Binance web UI wording refers to ET; exchange APIs are UTC, so timestamp conversion matters in later verification.

## Why this source may matter

It is both the governing source of truth and the strongest direct evidence that the market is currently asking whether SOL can remain above a threshold it already exceeds by roughly 6-7% with only a few days remaining.

## Possible impact on the question

This source materially supports a high Yes probability, but it also highlights the key variant-view caveat: the contract is path-insensitive until the exact noon ET close, so a short-lived weekend selloff or timing-specific dip still defeats a currently-comfortable spot level.

## Reliability notes

- Binance is the explicit settlement authority, so source-of-truth reliability is high for resolution.
- For context, Binance API data is stronger than third-party price aggregators because the contract is exchange-specific.
- The main reliability risk is not source credibility but timestamp / contract-interpretation error.