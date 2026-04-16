---
type: source_note
case_key: case-20260415-7d14e3a4
dispatch_id: dispatch-case-20260415-7d14e3a4-20260415T231343Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-7d14e3a4 | market-implied
question: Will the price of Bitcoin be above $72,000 on April 19?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT API ticker and 1m klines
source_type: exchange market data / primary settlement-context source
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-7d14e3a4/researcher-analyses/2026-04-15/dispatch-case-20260415-7d14e3a4-20260415T231343Z/personas/market-implied.md]
tags: [binance, settlement-source, btcusdt, 1m-candle]
---

# Summary

This source note captures the most relevant direct evidence for the contract mechanics: current Binance BTC/USDT spot price and recent 1-minute candle closes.

## Key facts extracted

- Binance API ticker returned BTCUSDT price `74695.61000000` at retrieval time.
- Recent 1-minute klines around the retrieval window showed closes of approximately `74789.58`, `74736.94`, `74713.13`, `74748.92`, and `74695.61`.
- The observed spot level is already materially above the contract threshold of $72,000.
- The contract resolves specifically on the Binance BTC/USDT 12:00 ET one-minute candle close on 2026-04-19, so these observations do not settle the market now, but they show the market starts several thousand dollars above strike.

## Evidence directly stated by source

- Binance ticker API exposes the current BTCUSDT last price.
- Binance kline API exposes one-minute OHLCV candles that match the contract's stated settlement family (1m candle close), though final resolution is defined by the Binance trading UI candle at 12:00 ET on Apr 19.

## What is uncertain

- Current price is not the settlement price.
- API data is highly relevant to contract mechanics but the contract text names the Binance trading interface candle as the resolution source of truth.
- Short-horizon BTC volatility can still move price below $72,000 by resolution time.

## Why this source may matter

This is the closest thing to a primary market-state source and is directly aligned with the exchange/pair named in the contract.

## Possible impact on the question

Because BTC is trading near $74.7k, the market's high yes probability can be understood as pricing a modest cushion above strike rather than demanding a fresh breakout to an untested level.

## Reliability notes

High reliability for current exchange state and strong relevance to settlement mechanics. Residual ambiguity is low-to-medium because the contract names the Binance UI candle as source of truth rather than the public API, but both are from the same exchange and price family.
