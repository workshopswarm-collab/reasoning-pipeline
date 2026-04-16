---
type: source_note
case_key: case-20260414-3691b692
dispatch_id: dispatch-case-20260414-3691b692-20260414T170231Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-3691b692 | market-implied
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance spot market data docs and live BTCUSDT endpoints
source_type: exchange docs + direct market data
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: market-implied
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-3691b692/researcher-analyses/2026-04-14/dispatch-case-20260414-3691b692-20260414T170231Z/personas/market-implied.md]
tags: [binance, klines, settlement-source, btc]
---

# Summary

Binance documentation confirms the relevant direct data surface is the spot `/api/v3/klines` endpoint for `BTCUSDT` with `interval=1m`, and recent live endpoint checks show BTCUSDT trading around 74.7k on 2026-04-14, materially above the 72k threshold with roughly two days remaining.

## Key facts extracted

- Binance spot docs state `GET /api/v3/klines` returns kline/candlestick bars for a symbol and that klines are identified by open time.
- Docs explicitly allow a `timeZone` parameter; if provided, kline intervals are interpreted in that timezone rather than UTC.
- Recent live endpoint check of `GET /api/v3/ticker/price?symbol=BTCUSDT` returned `74735.96000000` on 2026-04-14.
- Recent live endpoint check of `GET /api/v3/klines?symbol=BTCUSDT&interval=1m&limit=10` returned latest closes around 74.6k-74.7k, including a close of `74735.95000000` for the minute opening 2026-04-14 17:04 UTC.
- 12:00 ET on 2026-04-16 corresponds to 16:00 UTC because New York is on EDT (UTC-4) on that date.

## Evidence directly stated by source

- Binance docs: `GET /api/v3/klines` provides 1-minute candlestick data and supports timezone interpretation.
- Binance live data: current BTCUSDT spot price and latest 1-minute close are both well above 72,000.

## What is uncertain

- The market resolves on the specific 12:00 ET minute candle on 2026-04-16, not on current price.
- Binance web UI is the named settlement surface in the Polymarket rules; API parity is likely but not itself guaranteed by Polymarket text.
- BTC can move several percent in 43 hours, so being above 72k now does not directly settle the contract.

## Why this source may matter

This is the closest direct source-of-truth family because the contract explicitly resolves to Binance BTC/USDT 1-minute candle close. It also helps verify the timing mechanics and whether the market’s 90% price is plausible relative to current spot.

## Possible impact on the question

This source strongly supports the market’s high Yes probability because spot is already about 3.8% above the threshold with less than two days left. It also frames the main remaining risk as near-term downside volatility or a Binance-specific settlement mismatch rather than ignorance of the governing metric.

## Reliability notes

- Exchange operator documentation is high-credibility for endpoint mechanics.
- Direct API outputs are high-relevance and recent, but the contract names the Binance trading UI candle as the official settlement surface, so API data should be treated as a strong verification layer rather than the sole official resolver.
