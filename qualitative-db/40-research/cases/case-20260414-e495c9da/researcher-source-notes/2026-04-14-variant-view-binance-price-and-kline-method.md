---
type: source_note
case_key: case-20260414-e495c9da
dispatch_id: dispatch-case-20260414-e495c9da-20260414T191806Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-19
question: Will the price of Bitcoin be above $70,000 on April 19?
driver: reliability
date_created: 2026-04-14
source_name: Binance spot API docs and BTCUSDT price data
source_type: exchange documentation + market data
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: variant-view
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-e495c9da/researcher-analyses/2026-04-14/dispatch-case-20260414-e495c9da-20260414T191806Z/personas/variant-view.md]
tags: [binance, source-of-truth, kline, timezone, price-context]
---

# Summary

Binance documentation confirms that 1-minute klines are identified by open time and that the API supports a `timeZone` parameter for interval interpretation while `startTime` and `endTime` remain UTC. Live Binance BTCUSDT data on April 14 showed spot around 74.3k, about 6.1% above the 70k threshold, with recent daily candles mostly above 70k but with intraday ranges wide enough to matter.

## Key facts extracted

- `GET /api/v3/klines` returns kline/candlestick bars and klines are uniquely identified by open time.
- The endpoint supports a `timeZone` parameter; if provided, intervals are interpreted in that timezone instead of UTC.
- `startTime` and `endTime` are still interpreted in UTC even when `timeZone` is set.
- Live spot/ticker data on April 14 showed BTCUSDT around 74,293 to 74,326.
- Recent 1-day candles from Binance showed BTCUSDT closing above 70,000 on most of the preceding days, but with day ranges including swings of several thousand dollars.
- The 24h ticker showed a daily low around 72,525 and high around 76,038, implying ordinary volatility that is meaningful even when spot is materially above the strike.

## Evidence directly stated by source

- The API/timezone mechanics support an explicit audit path for the exact noon-ET candle.
- Current Binance price context is comfortably above 70k, which is supportive of Yes.
- The recent range and crypto volatility imply that a 92% probability may understate the chance of a sharp move or minute-specific wick into the relevant close.

## What is uncertain

- These data do not settle April 19 directly; they only establish current state and the mechanics for the eventual source-of-truth query.
- Daily candles are contextual rather than direct evidence for the exact noon-ET minute close.

## Why this source may matter

This is the governing data ecosystem for settlement and the best direct contextual evidence for where BTC sits relative to the threshold today.

## Possible impact on the question

Supports a Yes lean because BTC is already above threshold by several thousand dollars, but also supports a modest discount versus extreme confidence because the contract resolves on a single minute close rather than a daily close or broad market average.

## Reliability notes

Strong on mechanics and live pricing because it is the designated exchange source. Weaker on final event inference because it is still several days before resolution and crypto volatility can compress a 6% cushion quickly.
