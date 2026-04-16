---
type: source_note
case_key: case-20260415-7253c25f
dispatch_id: dispatch-case-20260415-7253c25f-20260415T220737Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-21
question: Will the price of Bitcoin be above $72,000 on April 21?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance Spot API docs + live BTCUSDT endpoints
source_type: primary + contextual
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-15
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-7253c25f/researcher-analyses/2026-04-15/dispatch-case-20260415-7253c25f-20260415T220737Z/personas/risk-manager.md]
tags: [binance, contract-mechanics, resolution-source, btc]
---

# Summary

This source note captures the key contract-mechanics facts for a Polymarket market resolved off the Binance BTC/USDT 1-minute candle at 12:00 ET on 2026-04-21. It also records a live spot check that Binance's public API currently reports BTCUSDT around 75k, comfortably above the 72k threshold, while noting that the final settlement depends on the specific noon-ET minute close on the resolution date rather than the current spot price.

## Key facts extracted

- Polymarket rules say the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-21 has a final close strictly higher than 72,000.
- The governing source of truth is Binance BTC/USDT, not another exchange and not another trading pair.
- Binance API documentation for `/api/v3/klines` states that kline bars are uniquely identified by open time and that the response contains open, high, low, close, volume, and close time.
- A timezone parameter exists in Binance docs, but `startTime` and `endTime` are always interpreted in UTC.
- Converting 2026-04-21 12:00 ET yields 2026-04-21 16:00:00 UTC.
- A live API spot check on 2026-04-15 returned `{"symbol":"BTCUSDT","price":"75079.30000000"}`.
- A forward query for the exact target minute naturally returned no candle yet, confirming the market is unresolved and date-specific.

## Evidence directly stated by source

- Binance docs explicitly document the kline endpoint and show the close price field in the response payload.
- Polymarket explicitly states the relevant candle, exchange, pair, and strict-higher-than threshold condition.

## What is uncertain

- The final 12:00 ET candle close on 2026-04-21 is not yet observable.
- The public web chart and the API are closely related but not necessarily identical presentation surfaces; the market text points traders to the Binance chart UI, while the API docs clarify the underlying kline schema.
- Short-term BTC volatility over nearly six days can still move the market below 72k at the exact observation minute.

## Why this source may matter

This is the key source bundle for contract interpretation. It defines both the exact settlement mechanics and the operational risk: even if BTC trades above 72k most of the week, the market still resolves No if the final close of the single relevant 1-minute candle at noon ET is 72,000.00 or lower.

## Possible impact on the question

The source supports a favorable baseline for Yes because current BTCUSDT is already materially above 72k. But it also narrows the question to one exact minute on one exact venue, which creates path and timing risk that a risk-manager should not ignore.

## Reliability notes

- Polymarket market rules are the direct contract statement and should govern interpretation unless later clarified by Polymarket resolution staff.
- Binance developer docs are a strong contextual source for how the relevant kline data is structured.
- The live API spot check is direct but only a snapshot, not settlement evidence.
- Evidence independence is medium: Polymarket relies on Binance, and the contextual mechanics source is also Binance-related.