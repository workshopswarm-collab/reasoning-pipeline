---
type: source_note
case_key: case-20260415-48a4484b
dispatch_id: dispatch-case-20260415-48a4484b-20260415T180644Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: exchange-market-data
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: reliability
date_created: 2026-04-15
source_name: Binance public API spot price and recent 1m klines
source_type: exchange primary data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-48a4484b/researcher-analyses/2026-04-15/dispatch-case-20260415-48a4484b-20260415T180644Z/personas/variant-view.md]
tags: [binance, primary-source, spot-price, kline, verification]
---

# Summary

Direct Binance API checks show BTC/USDT trading around 74.3k on April 15 with recent one-minute closes in the low-to-mid 74.2k range, leaving roughly a 2.2k buffer above the 72k threshold one day before resolution.

## Key facts extracted

- Binance ticker price check returned BTCUSDT at 74,268.25.
- Recent 1-minute klines printed closes around 74,096 to 74,279 during the verification window.
- Recent minute-to-minute volatility in the sampled window was tens to low hundreds of dollars, not thousands.

## Evidence directly stated by source

- Current BTCUSDT spot was materially above 72,000 when checked.
- Recent Binance one-minute closes were consistently above 74,000 in the sample.

## What is uncertain

- A short kline sample does not prove where price will be at noon ET tomorrow.
- The public API data fetched here is not the exact same chart UI path referenced in the market rules, though it is the same exchange/instrument family and should be strongly informative.

## Why this source may matter

This is the closest primary evidence available for the actual underlying series the contract references. It supports the consensus case that BTC has meaningful cushion above the threshold, while also clarifying that resolution is on a single minute close rather than a broad daily state.

## Possible impact on the question

The existing buffer makes Yes more likely than not by a wide margin, but not close to certainty if BTC can move sharply over the next ~22 hours or if a temporary intraday downtick happens exactly at the resolution minute.

## Reliability notes

High relevance and high recency. This is primary exchange data, though I would still treat the exact noon-ET chart close tomorrow as the final governing truth rather than this pre-resolution API snapshot.