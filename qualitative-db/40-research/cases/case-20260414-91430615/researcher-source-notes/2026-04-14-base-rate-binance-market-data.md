---
type: source_note
case_key: case-20260414-91430615
dispatch_id: dispatch-case-20260414-91430615-20260414T235247Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-19
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-19 close above 70000?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance Spot API market data endpoints and live BTCUSDT data
source_type: primary_exchange_data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-91430615/researcher-analyses/2026-04-14/dispatch-case-20260414-91430615-20260414T235247Z/personas/base-rate.md]
tags: [binance, primary-source, resolution-source, btcusdt]
---

# Summary

Binance is the governing source of truth for this market, and Binance API documentation plus live BTCUSDT data support both the contract interpretation and the current base-rate setup. On 2026-04-14, Binance BTCUSDT last price was about 74,058-74,072 depending on retrieval time, comfortably above the 70,000 threshold.

## Key facts extracted

- Binance Spot API docs specify `GET /api/v3/klines` for candlestick bars and identify each kline by open time.
- The kline response includes open, high, low, and close prices; the close price is the relevant contract field.
- Binance docs state a `timeZone` parameter exists for kline interpretation, but `startTime` and `endTime` are always interpreted in UTC.
- Live `ticker/price` returned BTCUSDT around `74071.99` and `ticker/24hr` returned `74058.22` on 2026-04-14.
- `ticker/24hr` showed the 24h high at `76038.00` and low at `73795.47`, implying BTC was trading materially above 70,000 throughout that recent 24h window.

## Evidence directly stated by source

- Binance market-data docs explicitly document the kline endpoint and its response schema, including close price.
- Live Binance API responses directly provide current BTCUSDT spot price and recent 24h range.

## What is uncertain

- The exact final settlement check is the Binance website chart UI with 1m candles at 12:00 ET, not necessarily the API endpoint, though the API is the same exchange data family and should be a strong proxy.
- A future 2026-04-19 noon ET candle cannot yet be retrieved, so this source only establishes mechanics and current positioning, not the final outcome.

## Why this source may matter

This is the closest thing to the contract’s primary source of truth. It anchors both the threshold comparison and the operational interpretation of what counts as the relevant candle close.

## Possible impact on the question

Because BTCUSDT is currently about 5.8% above the threshold and recent 24h trading stayed above 70,000, the market starts from a favorable state for a Yes resolution. The main remaining risk is not contract misunderstanding but a price decline before the specific 12:00 ET 1-minute close on April 19.

## Reliability notes

High reliability for exchange-reported current price and documented market-data mechanics. Moderate residual ambiguity remains because the written Polymarket rules cite the Binance website chart UI as the settlement surface, so a small operational mismatch risk remains even if the API strongly reflects the same underlying exchange data.
