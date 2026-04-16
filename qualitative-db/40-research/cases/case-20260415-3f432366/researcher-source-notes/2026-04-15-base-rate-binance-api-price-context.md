---
type: source_note
case_key: case-20260415-3f432366
dispatch_id: dispatch-case-20260415-3f432366-20260415T074424Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-3f432366 | base-rate
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-17 be above 72000?
driver: reliability
date_created: 2026-04-15
source_name: Binance Spot API BTCUSDT ticker and klines
source_type: primary_exchange_data
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=120
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-3f432366/researcher-analyses/2026-04-15/dispatch-case-20260415-3f432366-20260415T074424Z/personas/base-rate.md]
tags: [binance, btcusdt, pricing, source-note, primary]
---

# Summary

Binance API data gives both the contract's governing venue and a usable recent price/base-rate context. As of the run, BTC/USDT spot was about 73.6k, above the 72k strike. Recent daily closes and recent intraday noon-ET candles were also above 72k.

## Key facts extracted

- Current spot ticker during the run: `73568.70` BTC/USDT.
- Recent daily closes from Binance API:
  - 2026-04-13: `74417.99`
  - 2026-04-14: `74131.55`
  - 2026-04-15 partial/current day during run: about `73564.74` at query time.
- Recent daily closes above 72k occurred on 2026-04-10, 2026-04-11, 2026-04-13, 2026-04-14, and current spot on 2026-04-15 was also above 72k.
- In a 120-day Binance daily sample, 59 of 120 daily closes were above 72k (~49.2%).
- Conditional base-rate from the same sample: when BTC daily close was already above 72k, the close two days later was still above 72k in 51 of 57 cases (~89.5%).
- Recent noon-ET proxy candles from Binance 1-minute klines:
  - 2026-04-13 16:00 UTC / 12:00 ET close: `71902.91` (just below strike)
  - 2026-04-14 16:00 UTC / 12:00 ET close: `75356.48` (well above strike)
- Last 1500 one-minute closes available during the run were all above 72k; min close in that sample was about `73566.00`, max about `75986.03`.

## Evidence directly stated by source

- Exact ticker price and exact OHLCV kline records from Binance.
- Timestamp format implies the exchange data can be mapped directly to the contract's specified 1-minute candle.

## What is uncertain

- The market resolves on the Binance web UI candle display, not explicitly the public API, so API/web parity is highly likely but not independently verified line-by-line here.
- The 2026-04-15 daily candle was still in progress during the run and should not be treated as a final daily close.
- The daily-close conditional base rate is only an approximation for a noon-ET 1-minute-candle contract.

## Why this source may matter

This is the closest thing to a primary source for both settlement mechanics and current state. It anchors whether the strike is currently in/out of the money and provides the best outside-view context from the same venue and pair named by the contract.

## Possible impact on the question

The source supports a bullish near-term base rate because BTC/USDT is already above 72k and has tended to remain above that level two days later when already above it. It also supports the operational interpretation that the relevant observation is a single Binance BTC/USDT 1-minute close at 12:00 ET on April 17.

## Reliability notes

Primary exchange data is high-quality for price context and likely high-quality for settlement context, but there is still mild source-of-truth ambiguity because the written contract names the Binance web candle display rather than the API endpoint directly.