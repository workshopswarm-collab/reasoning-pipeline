---
type: source_note
case_key: case-20260416-d529376c
dispatch_id: dispatch-case-20260416-d529376c-20260416T030247Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: tokens
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 12:00 ET one-minute candle on 2026-04-19 close above 80?
driver: reliability
date_created: 2026-04-15
source_name: Binance SOL/USDT API and market contract mechanics
source_type: exchange market data / direct resolution source
source_url: https://api.binance.com/api/v3/klines?symbol=SOLUSDT&interval=1m and https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [sol, solana]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, resolution-source, market-data, timing]
---

# Summary

Binance is the governing source of truth for this market. Direct exchange data confirms SOL/USDT is already trading above $80 at assignment time and that the relevant resolution timestamp is the 12:00 ET one-minute candle, which corresponds to 16:00 UTC in April under EDT.

## Key facts extracted

- Spot/ticker check from Binance API at assignment time returned `85.38000000` for `SOLUSDT`.
- Recent daily candles from Binance show closes around the mid-80s over the preceding several sessions.
- Direct one-minute kline pulls for 16:00 UTC on recent days returned:
  - 2026-04-13 close `82.74000000`
  - 2026-04-14 close `85.97000000`
  - 2026-04-15 close `83.94000000`
- Because the market resolves on the Binance one-minute candle for 12:00 ET, the relevant timestamp during daylight saving time is 16:00 UTC.
- The contract requires the final close of that exact minute candle to be strictly greater than 80; trading above 80 at other times is supportive but not sufficient on its own.

## Evidence directly stated by source

- Binance exposes the exchange pair, latest price, and one-minute kline close values directly.
- The market contract text names Binance SOL/USDT one-minute candles as the resolution source.

## What is uncertain

- The final 2026-04-19 12:00 ET candle has not occurred yet.
- Short-horizon crypto volatility means a move from the mid-80s to below 80 by resolution remains possible.

## Why this source may matter

This is the direct settlement surface. It anchors both the contract interpretation and the current distance-from-threshold analysis.

## Possible impact on the question

Current direct pricing materially favors Yes because SOL is already several dollars above the threshold, but the market remains exposed to any sharp downside move before the exact noon ET print on April 19.

## Reliability notes

High reliability for direct price and candle data because Binance is the named resolution source. The main limitation is that it does not itself predict future price moves; it only confirms current state and the settlement mechanism.
