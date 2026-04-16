---
type: source_note
case_key: case-20260415-fc70b9f6
dispatch_id: dispatch-case-20260415-fc70b9f6-20260415T072610Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-16 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance Spot API market data endpoints and live BTCUSDT data
source_type: exchange-api-docs-and-market-data
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, klines, settlement-source, btcusdt, resolution-mechanics]
---

# Summary

Binance documentation confirms that `GET /api/v3/klines` returns 1-minute BTCUSDT candles with a distinct close field and supports timezone interpretation for kline intervals, while live Binance BTCUSDT market data shows BTC trading materially above 72,000 at research time. This source set matters because the market resolves off a Binance 1-minute candle close, not an index or another venue.

## Key facts extracted

- Binance spot API docs state `GET /api/v3/klines` returns kline/candlestick bars and that the response includes a distinct `Close price` field.
- The docs note `timeZone` can be provided for kline interval interpretation, while `startTime` and `endTime` are interpreted in UTC.
- Polymarket’s market rules specify the governing source of truth is the Binance BTC/USDT 1-minute candle for `12:00` in ET timezone on the specified date.
- Direct live Binance BTCUSDT data fetched during this run showed:
  - `lastPrice`: 73711.33
  - `highPrice` (24h): 76038.00
  - `lowPrice` (24h): 73592.36
  - `weightedAvgPrice` (24h): 74722.04
  - sample recent 1-minute closes around research time were ~73692 to ~73720
- Recent daily klines from Binance show BTC closing above 72,000 on April 10, 11, 13, 14, and still trading above 72,000 on April 15 at research time.

## Evidence directly stated by source

- Binance docs directly define the kline endpoint and response structure including the close-price field.
- Binance live API directly states current BTCUSDT last price and 24h range.

## What is uncertain

- The exact settlement candle is the 2026-04-16 12:00 ET candle, which had not occurred yet at research time.
- Binance docs clarify how klines are structured, but Polymarket resolves from the chart surface currently available on Binance’s trading interface; operational or display discrepancies remain a low-probability but relevant tail risk.
- A direct API pull for the future settlement timestamp necessarily returns no row yet, so the settlement value itself remains unknown.

## Why this source may matter

This is the closest thing to an authoritative direct source for both settlement mechanics and present state. It anchors both the contract interpretation and the current distance from the 72,000 threshold.

## Possible impact on the question

Because BTCUSDT is currently about 1,700 points above the threshold and has traded above 72,000 throughout the sampled recent period, the base case favors Yes. The main residual risk is not ordinary drift but a sufficiently large downward move by the exact 12:00 ET minute close or a source/operational interpretation issue.

## Reliability notes

- High credibility for contract mechanics and live venue-specific price because Binance is the governing source named by the market.
- Independence is limited: the same venue supplies both live context and eventual settlement source, so this should be supplemented by the Polymarket rules page for contract interpretation.
- Good for direct evidence; weaker for broader contextual interpretation of path risk by tomorrow noon ET.