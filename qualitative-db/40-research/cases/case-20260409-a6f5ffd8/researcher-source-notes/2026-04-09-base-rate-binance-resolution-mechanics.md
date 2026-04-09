---
type: source_note
case_key: case-20260409-a6f5ffd8
dispatch_id: dispatch-case-20260409-a6f5ffd8-20260409T071326Z
analysis_date: 2026-04-09
persona: base-rate
domain: crypto
subdomain: market-structure
entity: btc
topic: case-20260409-a6f5ffd8 | base-rate
question: Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-09 close above 70000?
driver: operational-risk
date_created: 2026-04-09
source_name: Binance spot API docs and live BTCUSDT endpoints
source_type: exchange documentation + direct exchange API
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: base-rate
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-a6f5ffd8/researcher-analyses/2026-04-09/dispatch-case-20260409-a6f5ffd8-20260409T071326Z/personas/base-rate.md]
tags: [binance, resolution-mechanics, timestamp, kline, btcusdt]
---

# Summary

This source note records the governing resolution mechanics for the market. Binance documentation says klines are identified by open time, default to UTC unless a `timeZone` parameter is provided, and report both open time and close time. Live Binance API data shows BTC/USDT trading above $70,000 around the time of research, which matters because the market resolves a few hours later on a single 1-minute close.

## Key facts extracted

- Binance `/api/v3/klines` defines kline/candlestick bars for a symbol and says klines are uniquely identified by their open time.
- Binance docs say `timeZone` defaults to `0 (UTC)` and that if `timeZone` is provided, intervals are interpreted in that timezone instead of UTC.
- Binance docs also say `startTime` and `endTime` are always interpreted in UTC regardless of `timeZone`.
- The market description specifically references the Binance BTC/USDT chart with `1m` candles selected and asks for the candle for `12:00 in the ET timezone (noon)`.
- On 2026-04-09 during this run, Binance live endpoints returned BTC/USDT spot price around `71051.11`, which is already above the $70,000 threshold.
- Recent 1-minute klines from Binance during this run also showed closes above $70,000.

## Evidence directly stated by source

From Binance docs:
- Klines are uniquely identified by open time.
- Default kline timezone is UTC unless a timezone override is provided.
- Kline response includes both open time and close time.

From direct Binance API:
- `/api/v3/ticker/price?symbol=BTCUSDT` returned `71051.11000000` during this run.
- `/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=3` returned three recent 1-minute candles, all with closes above $70,000.

## What is uncertain

- The exact resolving candle is still in the future at the time of research.
- The Polymarket description references the Binance web chart rather than the API explicitly, so there is modest operational ambiguity about whether UI presentation and API output could ever differ in edge cases.
- There is some contract-interpretation ambiguity around whether “12:00 ET” means the candle opening at 12:00:00 ET or the candle closing at 12:00:59 ET, though the market wording most naturally points to the 12:00 ET one-minute candle itself.

## Why this source may matter

This is the governing source-of-truth family for the contract. The market is not asking about a broad Bitcoin price consensus; it is asking about a specific Binance BTC/USDT 1-minute candle close at a specific ET timestamp.

## Possible impact on the question

This source sharply narrows the problem from a broad crypto-price forecast to a short-horizon exchange-specific threshold event. Because BTC/USDT was already trading above $70,000 by roughly 03:14 ET, the outside-view prior for remaining above $70,000 through noon ET is favorable, though nontrivial intraday volatility remains the main threat.

## Reliability notes

- Exchange documentation plus direct exchange API is high-credibility for contract mechanics.
- Evidence independence is limited because both the docs and the live data come from the same underlying venue, but that is appropriate here because Binance is the designated settlement source.
- The main remaining risk is not source credibility but timestamp interpretation and any UI/API mismatch at settlement.