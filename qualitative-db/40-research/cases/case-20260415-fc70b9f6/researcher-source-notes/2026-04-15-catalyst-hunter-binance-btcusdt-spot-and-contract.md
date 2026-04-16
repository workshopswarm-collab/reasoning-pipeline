---
type: source_note
case_key: case-20260415-fc70b9f6
dispatch_id: dispatch-case-20260415-fc70b9f6-20260415T072610Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: binance-btcusdt-spot-and-contract-mechanics
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on April 16, 2026 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance spot API market data endpoints and live BTCUSDT data
source_type: primary
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-fc70b9f6/researcher-analyses/2026-04-15/dispatch-case-20260415-fc70b9f6-20260415T072610Z/personas/catalyst-hunter.md]
tags: [binance, btcusdt, contract-mechanics, source-note]
---

# Summary

This source note captures the governing source-of-truth mechanics for the market and a direct Binance spot datapoint check relevant to the current probability view.

## Key facts extracted

- Binance spot API documents `GET /api/v3/klines` for 1-minute candlestick data and specifies that the response includes the candle close price.
- The API documentation states `timeZone` can be provided for kline interval interpretation, while `startTime` and `endTime` remain interpreted in UTC.
- A live check of `GET /api/v3/ticker/price?symbol=BTCUSDT` at approximately 2026-04-15 03:30 ET returned `73713.24` / `73697.22` in adjacent calls, placing spot BTC/USDT already above 72,000 by roughly 1,700 points.
- A live check of `GET /api/v3/ticker/24hr?symbol=BTCUSDT` returned last price `73713.24`, 24h change `-1.253%`, high `76038.00`, low `73592.36`.
- Recent 1-minute klines around 03:21-03:30 ET all closed between roughly `73655` and `73728`.

## Evidence directly stated by source

- Binance documentation directly states that `GET /api/v3/klines` returns kline/candlestick bars and includes the close price field.
- Binance live API directly states current BTCUSDT last price and recent 24-hour range.

## What is uncertain

- The market resolves specifically off the Binance web chart with `1m` candles at 12:00 ET on April 16, not off the API endpoint directly, though the API is still a strong direct Binance surface for contract interpretation and spot verification.
- This note does not itself prove the April 16 noon ET close; it establishes mechanics and current distance from the strike.

## Why this source may matter

This is the cleanest direct source for the market’s governing venue and for verifying that the strike is currently below spot by a meaningful margin.

## Possible impact on the question

Because BTC/USDT is already trading materially above 72,000 on Binance, the base state favors Yes unless there is a meaningful drawdown before the noon ET observation window on April 16.

## Reliability notes

High reliability for venue-specific price mechanics and current spot state. Moderate limitation: Polymarket names the Binance web chart as the resolution source, so the API is best treated as a direct contextual verification surface rather than the final legal settlement surface.