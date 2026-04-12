---
type: source_note
case_key: case-20260411-6669dcdb
dispatch_id: dispatch-case-20260411-6669dcdb-20260411T003353Z
analysis_date: 2026-04-11
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260411-6669dcdb | risk-manager
question: Will the Binance BTC/USDT 1m candle for 2026-04-11 12:00 ET close above 72000?
driver: operational-risk
date_created: 2026-04-10
source_name: Binance Spot API docs + live BTCUSDT endpoints
source_type: exchange documentation and market data API
source_url: https://developers.binance.info/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-11
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [risk-manager finding, risk-manager evidence map, risk-manager assumption note]
tags: [binance, resolution-mechanics, btcusdt, candle-close]
---

# Summary

This source set established the governing settlement mechanics for the market and verified that BTCUSDT is a live Binance spot symbol with 1-minute kline support. It is the key source for interpreting what actually counts at resolution.

## Key facts extracted

- Binance Spot API documentation states that `/api/v3/klines` returns kline/candlestick bars and that klines are uniquely identified by their open time.
- The response schema explicitly labels field 4 as the candle `Close` price.
- The docs state `timeZone` defaults to UTC and that if a `timeZone` is provided, kline intervals are interpreted in that timezone, while `startTime` and `endTime` are always interpreted in UTC.
- Live `exchangeInfo?symbol=BTCUSDT` confirms the exact Binance spot symbol is `BTCUSDT` with base asset BTC and quote asset USDT, which matches the market contract language.
- Live `ticker/price?symbol=BTCUSDT` and `ticker/24hr?symbol=BTCUSDT` showed BTCUSDT trading around 72.9k at research time.

## Evidence directly stated by source

- "Klines are uniquely identified by their open time."
- Kline response field 4 is `Close price`.
- `timeZone` changes interval interpretation, but `startTime` and `endTime` remain UTC-interpreted.
- `exchangeInfo` reports the symbol as `BTCUSDT`.

## What is uncertain

- The Polymarket rules reference the Binance website chart UI rather than the API directly, so there is a small operational risk that chart presentation or ET labeling could create an edge-case mismatch even if the underlying data should align.
- The market wording says "candle for BTC/USDT 12:00 in the ET timezone"; that most naturally maps to the 12:00:00-12:00:59 ET minute, but the contract does not separately spell out whether the relevant candle is identified by open time or close time. Binance docs support open-time identification.

## Why this source may matter

This is the governing source-of-truth surface for pair selection, candle mechanics, and time interpretation. It sharply reduces ambiguity about what price is relevant and prevents accidental substitution of BTC/USD or non-Binance reference prices.

## Possible impact on the question

It does not answer the future price directly, but it materially narrows resolution risk: the relevant object is Binance spot BTCUSDT, 1-minute candle, using the candle close, with 12:00 ET corresponding to 16:00 UTC on 2026-04-11.

## Reliability notes

- Strong for mechanics because it is primary exchange documentation plus live first-party endpoints.
- Slight residual ambiguity remains because Polymarket resolves from the Binance web chart UI, not an explicit API endpoint, so there is mild source-of-truth presentation risk rather than price-feed risk.