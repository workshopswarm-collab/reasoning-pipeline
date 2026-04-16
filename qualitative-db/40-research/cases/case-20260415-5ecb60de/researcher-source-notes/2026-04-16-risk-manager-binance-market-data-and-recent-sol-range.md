---
type: source_note
case_key: case-20260415-5ecb60de
dispatch_id: dispatch-case-20260415-5ecb60de-20260416T000100Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: spot-price-resolution
entity: sol
topic: case-20260415-5ecb60de | risk-manager
question: Will the Binance SOL/USDT 12:00 ET 1-minute candle close on 2026-04-19 be above 80?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance Spot API market data docs plus live SOLUSDT price and recent daily klines
source_type: exchange_api_and_docs
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [sol]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-5ecb60de/researcher-analyses/2026-04-16/dispatch-case-20260415-5ecb60de-20260416T000100Z/personas/risk-manager.md]
tags: [binance, source-of-truth, resolution-mechanics, recent-price-context]
---

# Summary

Binance documentation confirms that the `GET /api/v3/klines` endpoint returns 1-minute candlestick bars whose close price is the fifth field in the returned array and that klines are identified by open time. A live Binance price fetch for `SOLUSDT` showed spot around 84.92 on 2026-04-15/16 UTC, and recent daily klines show SOL trading in the low-to-mid 80s with several recent daily lows still above 80 except for one dip to roughly 81.27 on April 12.

## Key facts extracted

- Binance market-data docs specify `GET /api/v3/klines` for candlestick data.
- For each kline array, the fifth field is the close price.
- The docs note klines are uniquely identified by open time.
- The docs allow a `timeZone` parameter for interval interpretation, while `startTime` and `endTime` remain UTC.
- A live Binance ticker price fetch for `SOLUSDT` returned `84.92000000`.
- Recent Binance daily klines retrieved from the API showed:
  - 2026-04-12 low about 81.27, close 81.53
  - 2026-04-13 close about 86.51
  - 2026-04-14 low about 83.30, close 83.72
  - 2026-04-15 close about 84.90

## Evidence directly stated by source

- The Binance docs directly describe the kline endpoint, fields, and timezone handling.
- The live ticker endpoint directly reports a current spot price for `SOLUSDT`.
- The daily kline endpoint directly reports recent open/high/low/close data for `SOLUSDT`.

## What is uncertain

- The authoritative Polymarket resolution surface is the Binance website candle display with `1m` selected, not necessarily the REST API, though both should normally match.
- A current spot price around 84.9 does not by itself establish the 2026-04-19 noon ET close.
- Daily lows above 80 recently reduce but do not eliminate the risk of a sub-80 1-minute close by April 19.

## Why this source may matter

This source does two jobs: it verifies the contract mechanics against a direct Binance source class and it provides recent direct price context close enough to the threshold to frame path risk.

## Possible impact on the question

The evidence pushes against an aggressively bearish view because SOL is already above the threshold by roughly 5 dollars and recent daily lows have mostly stayed above 80. But from a risk-manager perspective it also shows the key fragility: this is not a settled market, and a volatile weekend move of roughly 6% could still flip the outcome.

## Reliability notes

High credibility for mechanics and current/recent exchange data because Binance is the named source of truth in the contract. Independence is limited because the mechanics and the live price context both come from the same exchange/source family.