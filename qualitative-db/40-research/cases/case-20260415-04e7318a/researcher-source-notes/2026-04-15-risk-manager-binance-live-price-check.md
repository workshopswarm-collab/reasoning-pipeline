---
type: source_note
case_key: case-20260415-04e7318a
dispatch_id: dispatch-case-20260415-04e7318a-20260415T145259Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-04e7318a | risk-manager
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: reliability
date_created: 2026-04-15
source_name: Binance public API BTCUSDT spot and 1m klines check
source_type: exchange-api
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
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [risk-manager-finding, risk-manager-assumption-note, risk-manager-evidence-map]
tags: [binance, btcusdt, spot, klines, timing]
---

# Summary

This source note captures a live verification pass against Binance public API endpoints to check current BTC/USDT level and confirm how 1-minute candles map into ET timestamps.

## Key facts extracted

- Binance ticker endpoint returned BTCUSDT spot price **74163.71** on 2026-04-15.
- Binance avgPrice endpoint returned 5-minute average **74153.31308821**.
- Binance 1-minute kline endpoint returned recent closes around **74122 to 74164** for the 10:51-10:55 ET period.
- Converting the returned kline open times from epoch milliseconds to America/New_York produced clean ET alignment:
  - 1776264660000 -> 2026-04-15 10:51 ET
  - 1776264720000 -> 2026-04-15 10:52 ET
  - 1776264780000 -> 2026-04-15 10:53 ET
  - 1776264840000 -> 2026-04-15 10:54 ET
  - 1776264900000 -> 2026-04-15 10:55 ET

## Evidence directly stated by source

Direct API outputs captured during the run:
- ticker price: {"symbol":"BTCUSDT","price":"74163.71000000"}
- avg price: {"mins":5,"price":"74153.31308821","closeTime":1776264918931}
- recent 1m kline closes: 74122.69, 74129.72, 74102.41, 74154.47, 74163.71

## What is uncertain

- This is only a spot check on April 15, not evidence of April 20 outcome.
- Public API availability now does not guarantee uninterrupted availability at settlement time.
- The API note does not itself prove that Polymarket resolvers will use the API rather than the chart UI, but it does confirm that Binance publishes consistent 1-minute candle data and that ET conversion is straightforward.

## Why this source may matter

This check materially reduces two researcher risks:
1. a false narrative that BTC is near or below 70k when Binance spot is actually already well above it, and
2. a timing implementation mistake about how Binance 1-minute candles line up with ET noon.

## Possible impact on the question

Current Binance BTCUSDT around 74.1k means the market only needs BTC to remain above a threshold roughly 5.6% below spot over the next five days. That supports a high Yes probability. The risk-manager wrinkle is that a 5-6% drawdown in BTC over five days is absolutely plausible, so the market should not be treated as near-certainty just because spot is currently above threshold.

## Reliability notes

- High reliability for current live exchange data from the named settlement venue.
- Direct evidence for current state, not direct evidence for April 20 outcome.
- Independent from Polymarket rules text in function: one source defines mechanics, the other shows current market state on the actual exchange.