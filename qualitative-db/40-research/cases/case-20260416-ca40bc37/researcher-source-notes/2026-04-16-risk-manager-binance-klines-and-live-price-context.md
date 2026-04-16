---
type: source_note
case_key: case-20260416-ca40bc37
dispatch_id: dispatch-case-20260416-ca40bc37-20260416T053546Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-ca40bc37 | risk-manager
question: Will the price of Bitcoin be above $72,000 on April 20?
driver: reliability
date_created: 2026-04-16
source_name: Binance Spot API market-data documentation plus live BTCUSDT endpoints
source_type: primary resolution-context source
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, klines, btcusdt, resolution, market-data]
---

# Summary

Binance documents that `/api/v3/klines` returns 1-minute candlestick bars identified by open time, with start/end timestamps interpreted in UTC, while live BTCUSDT data at capture time showed spot price around 75.1k and 24-hour range roughly 73.5k-75.4k.

## Key facts extracted

- Binance documents `GET /api/v3/klines` for candlestick bars and says klines are uniquely identified by their open time.
- Supported interval includes `1m`.
- Binance documents that `startTime` and `endTime` are always interpreted in UTC, even if `timeZone` is provided.
- ET noon on 2026-04-20 converts to 2026-04-20 16:00:00 UTC.
- Live BTCUSDT ticker at capture time was about 75,076-75,080.
- Binance 24-hour ticker at capture time showed about +1.56% on the day, high about 75,425 and low about 73,514.
- Recent 1-minute klines retrieved successfully from Binance API, confirming data availability and current trading around the threshold region.

## Evidence directly stated by source

- Klines are keyed by open time.
- One-minute bars are a supported interval.
- UTC handling is explicit for timestamp parameters.

## What is uncertain

- Polymarket rules reference the Binance UI candlestick display, not the public REST API directly, although both should normally represent the same underlying minute bars.
- We do not yet have the actual April 20 noon ET candle, only current live context.
- Short-horizon BTC volatility can move several thousand dollars before resolution.

## Why this source may matter

This is the best primary source for interpreting minute-candle timing mechanics and verifying that the contract is operationally narrow: one exact Binance BTCUSDT minute close decides the market.

## Possible impact on the question

Because BTC was already trading materially above 72,000 at capture time, the base directional case favors Yes. But the same source also makes the fragility clear: only the exact 16:00 UTC / 12:00 ET 1-minute close on April 20 matters, so a transient drawdown into that minute would be enough for No.

## Reliability notes

High for timing and instrument interpretation. Moderate for actual forecasting power, since live spot data only gives current context and not a guarantee of the future noon close. This source is partly independent from Polymarket because Binance is the designated settlement reference while Polymarket is the contract wrapper.
