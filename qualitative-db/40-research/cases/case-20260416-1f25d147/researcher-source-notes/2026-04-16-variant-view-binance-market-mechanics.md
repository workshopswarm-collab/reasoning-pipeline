---
type: source_note
case_key: case-20260416-1f25d147
dispatch_id: dispatch-case-20260416-1f25d147-20260416T035120Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: trading-markets
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 1-minute candle closing at 12:00 PM ET on 2026-04-19 close above 80?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance SOLUSDT spot API and market surface
source_type: primary_exchange_data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [sol, solana]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-1f25d147/researcher-analyses/2026-04-16/dispatch-case-20260416-1f25d147-20260416T035120Z/personas/variant-view.md]
tags: [binance, settlement-source, candle-resolution, solusdt]
---

# Summary

Binance is the governing source of truth for this market. Direct checks of Binance's public spot API show SOLUSDT trading around 85.25 on 2026-04-16, with a price filter tick size of 0.01 and standard 1-minute kline data available for recent candles. A direct query for the eventual settlement minute on 2026-04-19 12:00 PM ET returns an empty array today, which confirms only that the market is not yet settled and that the correct target timestamp is future-dated.

## Key facts extracted

- `ticker/price` returned `{"symbol":"SOLUSDT","price":"85.25000000"}` on 2026-04-16.
- `avgPrice` returned a 5-minute average near 85.29, consistent with spot price being materially above 80 at research time.
- `exchangeInfo` for SOLUSDT shows status `TRADING` and `PRICE_FILTER.tickSize` of `0.01000000`.
- Recent 1-minute klines are available and include OHLCV fields with close prices reported to 8 decimals in API output.
- Querying the exact settlement minute timestamp corresponding to 2026-04-19 12:00 PM ET / 2026-04-19 16:00:00 UTC currently returns `[]`, confirming the target candle has not yet occurred.

## Evidence directly stated by source

- SOLUSDT is actively trading on Binance spot.
- Current direct Binance price is above 80.
- Binance exposes 1-minute kline close values that can be queried at minute-level granularity.
- The relevant noon ET settlement timestamp converts to 16:00 UTC on 2026-04-19 because New York is on EDT.

## What is uncertain

- The eventual 2026-04-19 12:00 PM ET candle close is still unknown.
- Public API formatting may differ from the website candle display used for official market resolution, even if the underlying price should match.
- Short-horizon crypto volatility between now and settlement remains substantial.

## Why this source may matter

This is the closest direct source to the contract's governing settlement surface. It establishes both present price context and the operational mechanics needed to verify the exact candle and timestamp later.

## Possible impact on the question

This source strongly supports the idea that the market's high probability is anchored to a real current price cushion above 80 rather than pure narrative momentum. At the same time, because the contract settles on one exact minute close several days in the future, current spot price alone does not guarantee resolution.

## Reliability notes

High reliability for present Binance spot conditions and market mechanics. Moderate caution remains because the official resolution references the Binance website candle interface rather than the API explicitly, and because this is a future-dated settlement event rather than a direct resolved observation.
