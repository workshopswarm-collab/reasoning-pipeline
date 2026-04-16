---
type: source_note
case_key: case-20260416-b80742d2
dispatch_id: dispatch-case-20260416-b80742d2-20260416T014833Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: market-structure
entity: xrp
topic: xrp-above-1pt3-on-april-19
question: Will the Binance XRP/USDT 12:00 ET one-minute candle on April 19 close above 1.30?
driver: reliability
date_created: 2026-04-15T21:52:00-04:00
source_name: Binance Spot API market data endpoints and live XRPUSDT data
source_type: exchange_api_and_documentation
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [xrp]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-b80742d2/researcher-analyses/2026-04-16/dispatch-case-20260416-b80742d2-20260416T014833Z/personas/base-rate.md]
tags: [binance, xrpusdt, settlement, source-note]
---

# Summary

Binance's spot API documentation confirms that `/api/v3/klines` returns one-minute candlestick bars with an explicit close price field, and live XRPUSDT data shows XRP trading materially above 1.30 during this research run.

## Key facts extracted

- Binance documents `GET /api/v3/klines` as the kline/candlestick endpoint and shows the returned array includes a `Close price` field.
- The Polymarket contract points to the Binance XRP/USDT 1m candle at 12:00 ET on the target date as the resolution source.
- Direct API checks during the run returned XRPUSDT spot around 1.4018.
- Binance 24h ticker data during the run showed open 1.3629, high 1.4086, low 1.3503, last 1.4018.
- A 1000-minute sample of recent 1m closes had min 1.3511 and max 1.4058; all 1000 sampled closes were above 1.30, while only about 2.6% were above 1.40.
- Recent daily candles show XRP closing above 1.30 on each of the last 10 sampled days from 2026-04-07 through 2026-04-16.

## Evidence directly stated by source

- Binance states that kline/candlestick bars are available via `/api/v3/klines` and that returned fields include close price.
- Binance states klines are uniquely identified by open time.
- Binance states `timeZone` can be provided for interval interpretation, while start and end times remain interpreted in UTC.

## What is uncertain

- The contract resolves from the Binance website chart surface rather than the API documentation alone, so there remains small operational risk that the website display and API retrieval differ in formatting or final displayed precision.
- The final relevant candle is on 2026-04-19 at 12:00 ET, so this source does not directly settle the market yet.
- This note does not by itself prove whether Polymarket will treat the 12:00 ET candle as the candle opening at 12:00 ET or the candle whose close prints at 12:00:59 ET, though the contract language strongly suggests the 12:00 minute bar.

## Why this source may matter

It is the best direct source for both settlement mechanics and current exchange pricing. It anchors both the contract interpretation and the base-rate view that a >1.30 print is currently the normal state rather than an outlier.

## Possible impact on the question

If XRP remains in its recent range, the event should be favored because the threshold is below all recently sampled one-minute closes. The main remaining risk is downward price movement before the target minute, not ambiguity about where the price is measured.

## Reliability notes

High reliability for exchange-native market data and endpoint mechanics. Moderate residual ambiguity remains because the market points to the website chart as the ultimate resolution surface, not explicitly to the API, so this should be paired with the contract text itself rather than used in isolation.