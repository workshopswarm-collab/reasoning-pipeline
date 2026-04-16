---
type: source_note
case_key: case-20260416-cc34f737
dispatch_id: dispatch-case-20260416-cc34f737-20260416T162722Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: exchanges
entity: binance
topic: ETH/USDT recent price context and candle mechanics
question: Will the Binance ETH/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 2300?
driver: reliability
date_created: 2026-04-16
source_name: Binance Spot API market data endpoints and live ETHUSDT endpoints
source_type: primary
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [ethereum, binance]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-cc34f737/researcher-analyses/2026-04-16/dispatch-case-20260416-cc34f737-20260416T162722Z/personas/base-rate.md]
tags: [source-note, crypto, ethereum, binance, base-rate]
---

# Summary

Binance is both the governing resolution source and a useful contextual source because its API documentation specifies how klines are identified and how timezone is handled, while live ETHUSDT endpoints show ETH trading above the 2300 threshold on the day before resolution.

## Key facts extracted

- Binance Spot API documents `GET /api/v3/klines` for candlestick bars and states klines are uniquely identified by their open time.
- The API supports a `timeZone` parameter, but `startTime` and `endTime` are always interpreted in UTC.
- Binance documents the kline response format and explicitly labels the fifth field as the `Close price`.
- Live Binance public endpoints on 2026-04-16 returned ETHUSDT around 2335.94 spot and 2334.26 for 5-minute average price.
- Recent daily klines from Binance showed closes of 2245.05, 2284.99, 2191.65, 2369.46, 2322.44, 2359.95, and 2335.94 from 2026-04-10 through 2026-04-16.
- In that 7-day window, six of seven daily closes were above 2300, with only 2026-04-12 below.

## Evidence directly stated by source

- Binance states that kline/candlestick bars are available through `GET /api/v3/klines` and that the close price is part of the response.
- Binance states timezone handling explicitly: kline intervals can be interpreted in a provided timezone, but `startTime` and `endTime` remain UTC.
- Binance live endpoints directly returned ETHUSDT prices above 2300 on 2026-04-16.

## What is uncertain

- The Polymarket rule points users to the Binance website chart UI, not directly to the API, so there is still mild source-of-truth ambiguity about whether UI presentation and API output could differ at edge cases.
- A daily close above 2300 does not guarantee the specific 12:00 ET one-minute candle on 2026-04-17 will also close above 2300.
- Short-term crypto volatility can move ETH several percent inside a single day.

## Why this source may matter

This is the best primary source set for both contract interpretation and current base-rate context. It anchors the market to Binance mechanics and shows that ETH is entering the resolution window already above the threshold.

## Possible impact on the question

The source supports an outside-view lean toward Yes because the threshold is modestly below current Binance ETHUSDT pricing and recent daily closes have usually been above 2300. It does not settle the market, but it raises the baseline probability materially above 50%.

## Reliability notes

High reliability for settlement mechanics and live exchange price context because the data is directly from Binance. Moderate limitation: the market references the Binance website candle UI specifically, so final adjudication still belongs to the exchange display/candle as rendered at the specified minute.