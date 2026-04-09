---
type: source_note
case_key: case-20260407-56d31eea
dispatch_id: dispatch-case-20260407-56d31eea-20260407T023203Z
analysis_date: 2026-04-07
persona: base-rate
domain: crypto
subdomain: market-structure
entity: binance
topic: case-20260407-56d31eea | base-rate
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-07 close above 66000?
driver: reliability
date_created: 2026-04-06
source_name: Binance Spot API market data endpoints and live BTCUSDT endpoint checks
source_type: exchange documentation + direct API check
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
source_date: 2026-04-06
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [bitcoin, binance]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260407-56d31eea/researcher-analyses/2026-04-07/dispatch-case-20260407-56d31eea-20260407T023203Z/personas/base-rate.md]
tags: [binance, api, kline, verification]
---

# Summary

Binance's spot API documentation confirms that kline/candlestick bars are identified by open time and that a timeZone parameter can be used to interpret intervals in a non-UTC timezone, while startTime and endTime are still interpreted in UTC. Direct endpoint checks also show BTCUSDT trading around 68.5k at research time, materially above the 66k threshold.

## Key facts extracted

- Binance documents GET /api/v3/klines for spot market data.
- Binance states that klines are uniquely identified by their open time.
- Binance documents an optional timeZone parameter; when provided, kline intervals are interpreted in that timezone instead of UTC.
- Binance also states startTime and endTime are always interpreted in UTC regardless of timeZone.
- Direct endpoint checks during this run returned BTCUSDT last price near 68,543 and recent 1-minute klines in the 68.54k-68.59k range.

## Evidence directly stated by source

- Kline bars are identified by open time.
- Timezone handling is explicit in the docs.
- Recent BTCUSDT spot price on Binance is above 66,000 by roughly 2,500 dollars during this run.

## What is uncertain

- The exact programmatic mapping of the future 12:00 ET candle cannot yet be observed because the relevant candle has not occurred.
- The direct API checks do not by themselves guarantee UI labeling will be interpreted identically by all humans without using the specified Binance chart surface.
- Intraday crypto volatility can still be large enough to move several percent by noon ET.

## Why this source may matter

This source is the best verification layer for the settlement mechanics beyond Polymarket's own rules. It clarifies how Binance defines a kline and confirms the exchange is currently trading materially above the threshold, which is the key outside-view input for a short-horizon above/below market.

## Possible impact on the question

The price evidence pushes toward Yes because the market only needs BTC/USDT to remain above 66,000 at one precisely defined minute close. The docs also reduce some source-of-truth ambiguity by confirming that Binance exposes a precise kline model rather than a loose or composite price concept.

## Reliability notes

High reliability on exchange mechanics because this is Binance's own developer documentation and direct endpoint output. Moderate residual ambiguity remains because the contract points human readers to the chart UI rather than explicitly to the API, so exact noon-ET labeling still merits attention even though the underlying exchange source is the same.
