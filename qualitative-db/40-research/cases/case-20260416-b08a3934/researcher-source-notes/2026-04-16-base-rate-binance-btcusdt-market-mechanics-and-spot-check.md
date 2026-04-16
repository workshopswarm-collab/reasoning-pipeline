---
type: source_note
case_key: case-20260416-b08a3934
dispatch_id: dispatch-case-20260416-b08a3934-20260416T023832Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 72000?
driver: operational-risk
date_created: 2026-04-15T22:41:00-04:00
source_name: Binance API and market data surfaces for BTCUSDT
source_type: primary
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-b08a3934/researcher-analyses/2026-04-16/dispatch-case-20260416-b08a3934-20260416T023832Z/personas/base-rate.md]
tags: [binance, btcusdt, market-mechanics, resolution-source]
---

# Summary

Binance is the governing source of truth for this contract. Direct API checks confirm BTCUSDT is an actively trading spot pair, that 1-minute kline data are available in exchange time series, and that spot price at research time is already materially above the 72,000 threshold.

## Key facts extracted

- Binance spot ticker endpoint returned BTCUSDT price `75072.79000000` at research time.
- Binance 1-minute kline endpoint returned recent candles for BTCUSDT with close prices around 75,000.
- Binance exchangeInfo for BTCUSDT shows `status: TRADING` and price filter tick size `0.01000000`, which implies cent-level precision for settlement comparison.
- The contract specifies the Binance BTC/USDT `1m` candle at `12:00` ET on 2026-04-17 and resolves on the final `Close` of that minute candle.

## Evidence directly stated by source

- Direct exchange API output showed BTCUSDT current spot price above 72,000.
- Direct exchange API output showed BTCUSDT recent 1-minute candles with standard open/high/low/close structure.
- Direct exchange metadata showed trading status and decimal precision constraints.

## What is uncertain

- The exact 12:00 ET candle close on 2026-04-17 is not yet known at research time.
- The Polymarket rules cite the Binance web chart surface rather than the API explicitly; in normal conditions these should match, but operational display differences are still a theoretical settlement risk.
- A sharp BTC selloff before noon ET on 2026-04-17 remains possible.

## Why this source may matter

This is the direct settlement venue named by the market. It establishes the relevant trading pair, live price level, candle structure, and practical precision for the threshold test.

## Possible impact on the question

Because BTCUSDT is already about 4% above the threshold with less than a day until the measurement window, the base rate for staying above 72,000 over one additional day is high unless there is a meaningful downside shock or settlement/mechanics issue.

## Reliability notes

This is the highest-quality source for this case because Binance is the named resolution source. Reliability risk is not zero because the contract refers to a specific chart surface and final candle close, but source-of-truth ambiguity is still low relative to most crypto price markets.
