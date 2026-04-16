---
type: source_note
case_key: case-20260415-c0464347
dispatch_id: dispatch-case-20260415-c0464347-20260415T011958Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-c0464347 | market-implied
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance API docs and live BTCUSDT endpoints
source_type: official_exchange_docs_and_market_data
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-c0464347/researcher-analyses/2026-04-15/dispatch-case-20260415-c0464347-20260415T011958Z/personas/market-implied.md]
tags: [binance, settlement-source, btcusdt, contract-mechanics]
---

# Summary

This source note captures the governing source-of-truth mechanics and a live spot check of Binance BTC/USDT context for the April 20 >$70k market.

## Key facts extracted

- Binance Spot API docs show `GET /api/v3/klines` and `GET /api/v3/uiKlines` support `interval=1m` and a `timeZone` parameter; close price is returned in the fifth field of each kline row.
- The market rules specify resolution from Binance BTC/USDT with `1m` candles selected and the relevant candle is the 12:00 ET candle on April 20.
- A live Binance price check on 2026-04-14 21:21 ET / 2026-04-15 01:21 UTC returned BTCUSDT around 74.6k, comfortably above the 70k threshold.
- Recent 1-minute klines around the check time also closed around 74.6k-74.7k.
- Binance 24h ticker data at the same check showed last price ~74,590, 24h high ~76,038, low ~73,795, indicating substantial buffer above 70k.

## Evidence directly stated by source

- Binance docs explicitly define the kline endpoint, supported intervals including `1m`, and response structure including close price.
- Binance docs state that if `timeZone` is provided, kline intervals are interpreted in that timezone instead of UTC.
- Live endpoint outputs directly returned BTCUSDT ticker and kline values above 70,000.

## What is uncertain

- The Polymarket rule references the Binance website UI rather than the API docs; the API is a strong contextual verification surface but final settlement still points to the Binance chart/UI close.
- The relevant candle is April 20 noon ET, about five days after this check, so current spot level is only contextual rather than dispositive.
- Short-horizon crypto volatility could still move BTC below 70k by the resolution minute.

## Why this source may matter

It establishes both the contract mechanics and the present market buffer. For a narrow date/time crypto contract, verifying the exact candle convention and timezone handling materially improves auditability.

## Possible impact on the question

This source supports the market's high-probability stance because the governing exchange surface is clear and current BTCUSDT price is already several thousand dollars above 70k. It also highlights the main residual risk: a sharp selloff before the specific noon ET minute on April 20.

## Reliability notes

- Primary for mechanics: high, because Binance documentation is the exchange's own specification for kline data.
- Primary for current context: high, because the live Binance API is direct exchange data.
- Independence is medium: both mechanics and live context come from Binance, so a separate contextual source is still useful for triangulation.