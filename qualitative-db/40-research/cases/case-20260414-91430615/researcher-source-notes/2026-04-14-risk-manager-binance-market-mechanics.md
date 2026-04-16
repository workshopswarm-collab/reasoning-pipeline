---
type: source_note
case_key: case-20260414-91430615
dispatch_id: dispatch-case-20260414-91430615-20260414T235247Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-91430615 | risk-manager
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close above 70000 on April 19, 2026?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance spot API docs + live BTCUSDT endpoints
source_type: exchange documentation and live market data
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-91430615/researcher-analyses/2026-04-14/dispatch-case-20260414-91430615-20260414T235247Z/personas/risk-manager.md]
tags: [binance, btcusdt, resolution-source, market-mechanics]
---

# Summary
Binance documentation confirms that `GET /api/v3/klines` returns 1-minute candlestick bars with a distinct close-price field and supports a `timeZone` parameter. The live Binance ticker and recent 1-minute klines on 2026-04-14 show BTC/USDT trading materially above 70,000 at assignment time, around 74,072.

## Key facts extracted
- Binance documents `GET /api/v3/klines` for candlestick bars and explicitly shows the response field order, including close price as the fifth element in each kline row.
- Binance states klines are uniquely identified by open time.
- Binance documents a `timeZone` parameter for kline interpretation; however, Polymarket specifically names the Binance UI candle for `12:00` in ET as the settlement source.
- Live Binance ticker at fetch time returned BTCUSDT price `74071.99000000`.
- Recent 1-minute klines fetched from Binance also showed closes around 74,072.

## Evidence directly stated by source
- Binance docs directly describe the kline endpoint, supported intervals including `1m`, and the close-price field location.
- Binance live endpoints directly showed contemporaneous BTC/USDT spot price data.

## What is uncertain
- The API docs alone do not prove whether Polymarket resolves from the exchange API, the UIKlines endpoint, or the website chart rendering layer; Polymarket text points to the Binance trading page with 1m candles selected.
- Current price being above 70,000 on 2026-04-14 does not guarantee the 2026-04-19 noon ET close remains above 70,000.
- Short-horizon BTC path risk remains meaningful over five days.

## Why this source may matter
This is the closest thing to a governing primary source for both settlement mechanics and current market state. It grounds the exact object being resolved: the Binance BTC/USDT one-minute close, not a generic BTC spot print across venues.

## Possible impact on the question
It supports a high probability that the contract is currently in-the-money because BTC is already several thousand dollars above the threshold. It also surfaces the key risk-manager caveat: the contract depends on one exact minute close on one venue, so exchange-specific or timing-specific variance matters.

## Reliability notes
High credibility for market mechanics and current venue-specific price observation. Moderate limitation for exact Polymarket settlement implementation because the contract references the Binance UI page rather than the API docs directly.