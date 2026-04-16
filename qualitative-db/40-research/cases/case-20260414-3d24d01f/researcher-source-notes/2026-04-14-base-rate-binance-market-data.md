---
type: source_note
case_key: case-20260414-3d24d01f
dispatch_id: dispatch-case-20260414-3d24d01f-20260414T184328Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-19
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 70000 on April 19, 2026?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance Spot API market data and docs
source_type: primary
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-3d24d01f/researcher-analyses/2026-04-14/dispatch-case-20260414-3d24d01f-20260414T184328Z/personas/base-rate.md]
tags: [binance, settlement-source, market-data, btcusdt]
---

# Summary

Binance is the governing source of truth for this market, and its API documentation plus live BTCUSDT endpoints clarify both the contract mechanics and the current state of the underlying.

## Key facts extracted

- Binance klines are uniquely identified by open time, and the response includes a close price field.
- The API supports a `timeZone` parameter; if provided, kline intervals are interpreted in that timezone, while `startTime` and `endTime` remain UTC.
- Live Binance ticker price for BTCUSDT was 74281.10 on 2026-04-14 during this run.
- Recent 1-minute klines around the fetch time were all around 74250-74290, well above 70000.
- Recent 30 daily klines show 15 of the last 30 daily closes above 70000, with the latest daily close at 74281.10.

## Evidence directly stated by source

- Binance docs state `GET /api/v3/klines` returns candlestick bars and that the array contains open price, high price, low price, and close price.
- Binance docs state `timeZone` changes the interpretation of kline intervals from UTC to the provided timezone.
- Live API endpoints returned BTCUSDT current price and recent kline values above 70000.

## What is uncertain

- The market resolves on the April 19 noon ET 1-minute candle close, not on the current price or daily close.
- The exact noon ET candle on April 19 is still several days away, so a sharp move below 70000 by then remains possible.
- The Polymarket wording refers to the Binance trading UI, while verification here used Binance API docs/endpoints as a close proxy for the same underlying data.

## Why this source may matter

It directly governs settlement and also provides the strongest current price evidence for whether the market is near or far from the threshold.

## Possible impact on the question

Because BTCUSDT is currently around 74281 and recent minute-level prices are also above 70000, the contract would currently resolve Yes if evaluated now. This supports a high prior for Yes, though not certainty, because several days remain.

## Reliability notes

Primary and high-quality for settlement mechanics and live BTCUSDT data. Main limitation is timing: current and recent prices are not the actual April 19 noon ET candle.