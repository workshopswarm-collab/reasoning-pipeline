---
type: source_note
case_key: case-20260415-3d3080df
dispatch_id: dispatch-case-20260415-3d3080df-20260415T002239Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance BTCUSDT market data and API docs
source_type: primary_and_contextual
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-3d3080df/researcher-analyses/2026-04-15/dispatch-case-20260415-3d3080df-20260415T002239Z/personas/base-rate.md]
tags: [binance, resolution-source, btcusdt, market-data]
---

# Summary

Binance is the governing source of truth for this market. Current BTC/USDT spot price is already materially above $70,000, and recent Binance daily closes show BTC has spent most of the last 10 sessions above that threshold. Binance API documentation also clarifies that 1-minute klines are identified by open time and can be queried with timezone handling, which matters for the contract's noon ET resolution rule.

## Key facts extracted

- Binance ticker endpoint returned BTCUSDT at approximately 74,543 to 74,560 during this research pass.
- Binance 24h ticker showed high 76,038, low 73,795, and last price 74,559.59.
- Binance daily klines for the last 30 sessions show BTC below 70,000 for a stretch in late March but back above 70,000 in most recent sessions, including closes around 71.9k, 71.1k, 71.8k, 73.0k, 73.0k, 70.7k, 74.4k, 74.1k, and 74.6k.
- Binance API docs for `/api/v3/klines` specify 1m klines are uniquely identified by open time and support timezone parameterization, while startTime/endTime remain UTC.

## Evidence directly stated by source

- Current BTCUSDT spot on Binance is above the 70,000 strike by roughly 6%.
- Binance provides the exact market data family the contract says will be used for resolution.
- The relevant contract condition is not daily close or any other exchange, but the BTC/USDT 1-minute candle close at 12:00 ET on April 20.

## What is uncertain

- This source does not by itself tell us where BTC will trade on April 20 at exactly noon ET.
- Binance docs do not fully resolve whether Polymarket will rely on UI chart display versus API extraction if there is a display/API mismatch, though both should normally represent the same underlying kline.
- Spot price can move several percent in five days, so being above 70,000 now does not settle the market.

## Why this source may matter

This is the governing operational source for both contract interpretation and the current base-rate setup. It establishes that the market is asking about a live threshold already exceeded on the primary exchange used for settlement, reducing the amount of upside needed for a Yes resolution.

## Possible impact on the question

The source pushes toward Yes because the starting point is already around mid-74k rather than near the threshold. It also narrows the question to a specific exchange pair and one minute of time, which means operational and timing interpretation matter almost as much as directional BTC outlook.

## Reliability notes

High credibility for price and rule mechanics because Binance is the named settlement source. Independence is limited because price, ticker, and kline endpoints all come from the same institution, so a separate contextual source is still needed for robustness.