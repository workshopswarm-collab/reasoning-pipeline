---
type: source_note
case_key: case-20260415-47643da0
dispatch_id: dispatch-case-20260415-47643da0-20260415T010752Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: reliability
date_created: 2026-04-15
source_name: Binance BTCUSDT API snapshot
source_type: exchange API / direct source-of-truth surface
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-47643da0/researcher-analyses/2026-04-15/dispatch-case-20260415-47643da0-20260415T010752Z/personas/base-rate.md]
tags: [binance, source-of-truth, spot-price, 1m-candles]
---

# Summary

Binance's public API provides a near-real-time BTC/USDT spot reference and recent 1-minute kline data that are directly relevant because the contract resolves using Binance BTC/USDT 1-minute candle close data.

## Key facts extracted

- Binance ticker endpoint returned BTCUSDT price of 74680.51000000 at fetch time.
- This is about $2,680.51 above the $72,000 contract threshold.
- Recent 1-minute kline closes in the same fetch window were approximately 74659.96, 74680.00, 74731.22, 74680.50, and 74680.51.
- The recent 1-minute closes observed were all materially above $72,000.

## Evidence directly stated by source

- Direct Binance spot price snapshot for BTC/USDT.
- Direct recent 1-minute kline data, including close values.

## What is uncertain

- The contract settles on the Apr 17 noon ET 1-minute close, not on the current snapshot.
- API ticker price is not itself the exact settlement candle.
- I did not independently verify the Binance web chart UI timestamp labeling, though the API data strongly supports the general interpretation of using Binance 1-minute close data.

## Why this source may matter

This is the closest direct source-of-truth surface available before settlement because the contract explicitly references Binance BTC/USDT 1-minute candle closes.

## Possible impact on the question

With BTC/USDT already trading around 74.68k, the market only needs Bitcoin to avoid falling roughly 3.6% below the threshold by the specific settlement minute on Apr 17 for YES to resolve. That strongly supports a high YES probability, though not certainty because short-horizon crypto moves of that magnitude are common enough to matter.

## Reliability notes

High credibility for current Binance pricing and recent minute closes. Limited only by the fact that this is a pre-resolution snapshot rather than the final settlement minute itself.