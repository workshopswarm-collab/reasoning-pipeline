---
type: source_note
case_key: case-20260414-c44f46c0
dispatch_id: dispatch-case-20260414-c44f46c0-20260414T185449Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-c44f46c0 | risk-manager
question: Will the price of Bitcoin be above $68,000 on April 19?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and Binance BTCUSDT endpoints
source_type: primary-market-rules plus exchange-api
source_url: https://polymarket.com/event/bitcoin-above-on-april-19
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-c44f46c0/researcher-analyses/2026-04-14/dispatch-case-20260414-c44f46c0-20260414T185449Z/personas/risk-manager.md]
tags: [source-note, polymarket, binance, btc, resolution]
---

# Summary

The key direct source set for this case is the Polymarket contract text plus live Binance BTCUSDT pricing endpoints that mirror the exchange named in the resolution rules. Together they establish the governing resolution mechanics and the current distance from the $68,000 threshold.

## Key facts extracted

- Polymarket states this market resolves Yes if the Binance BTC/USDT 1-minute candle for **12:00 ET (noon) on April 19, 2026** has a final **Close** price above **68,000**.
- The contract explicitly says the source is Binance BTC/USDT with **1m** candles, not other exchanges or pairs.
- Price precision is determined by the source.
- Polymarket market price on the fetched page was about **95.5% Yes** for the 68,000 threshold.
- Binance API spot ticker returned BTCUSDT around **74,085** on 2026-04-14.
- Binance 1-minute kline data around the research time showed closes around **74,0xx to 74,1xx**, roughly **$6,000+ above** the threshold.
- Time conversion check: the contract’s noon ET timestamp equals **2026-04-19 16:00:00 UTC**.

## Evidence directly stated by source

Direct from Polymarket rules:
- resolution is tied to Binance BTC/USDT only
- the decisive datapoint is the 12:00 ET 1-minute candle’s final close on April 19
- threshold comparison is strictly higher than 68,000

Direct from Binance endpoints checked during this run:
- live ticker price was ~74,085
- recent 1-minute closes clustered near 74,000+

## What is uncertain

- Binance web UI was protected by a CloudFront challenge from this environment, so the exact browser-visible candle page could not be independently eyeballed here.
- The API endpoint is not the exact UI surface cited by Polymarket, though it is the same exchange and symbol family and exposes 1-minute klines directly.
- A rapid BTC drawdown before April 19 noon ET could still push the decisive candle below 68,000.

## Why this source may matter

This is the core resolution and measurement source set. It defines both what counts and what does not count, and it shows the market is currently several thousand dollars in the money versus the threshold.

## Possible impact on the question

This source set strongly supports a Yes-leaning baseline because the contract is simple once the source-of-truth and timing are pinned down: BTC/USDT on Binance needs to stay above 68,000 at one specific minute. The main remaining risk is not contract ambiguity but price path risk and exchange/source execution nuances.

## Reliability notes

- Polymarket rule text is the governing contract source for resolution mechanics.
- Binance API data is highly relevant direct exchange data, but the exact cited surface is the Binance trading UI candle display, so this remains a close proxy rather than a perfect UI-level verification.
- Evidence independence is moderate: both direct sources are tightly linked to the same underlying exchange/source-of-truth stack.