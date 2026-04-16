---
type: source_note
case_key: case-20260415-7b143efd
dispatch_id: dispatch-case-20260415-7b143efd-20260415T132144Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: exchange-market-data
entity: btc
topic: case-20260415-7b143efd | risk-manager
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: reliability
date_created: 2026-04-15
source_name: Binance spot API market data docs plus live BTCUSDT ticker/klines
source_type: exchange documentation + direct market data
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
source_date: 2026-04-15
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-7b143efd/researcher-analyses/2026-04-15/dispatch-case-20260415-7b143efd-20260415T132144Z/personas/risk-manager.md]
tags: [binance, api, klines, btcusdt, source-of-truth]
---

# Summary

Binance's official market-data documentation confirms that `GET /api/v3/klines` returns 1-minute candlestick data with an explicit `Close price` field and supports a timezone parameter for interval interpretation. Direct Binance API checks on 2026-04-15 show BTCUSDT trading around 74.27k-74.31k, materially above the 70k line five days before resolution.

## Key facts extracted

- Binance documents `GET /api/v3/klines` as the canonical kline/candlestick endpoint.
- The kline response explicitly includes `Close price` as the fifth main price field in each candle array.
- Binance documents a `timeZone` parameter, with intervals interpreted in that timezone; start/end times remain UTC.
- Current Binance spot price check returned BTCUSDT at 74,273.07.
- Recent 1-minute klines sampled around the same time show closes clustered near 74,275 to 74,301.

## Evidence directly stated by source

From Binance docs:
- "GET /api/v3/klines"
- "Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time."
- response field example includes `\"0.01577100\", // Close price`
- notes state that if `timeZone` is provided, "kline intervals are interpreted in that timezone instead of UTC."

From direct Binance API reads:
- ticker price response: `BTCUSDT = 74273.07000000`
- recent 1m closes sampled: 74279.50, 74291.99, 74301.20, 74274.83, 74279.67

## What is uncertain

- The Polymarket rule text references the Binance trading UI with 1m candles selected rather than the raw API endpoint, so there remains a small implementation ambiguity between UI presentation and API retrieval even though both are Binance-native.
- This source gives only a current snapshot, not a forecast path for April 20 noon ET.

## Why this source may matter

This source does two jobs: it verifies the operational meaning of a Binance 1-minute close and it gives the current baseline level relative to the 70k threshold.

## Possible impact on the question

Because current spot and recent 1m closes are already roughly 6 percent above the threshold, the market only fails if BTCUSDT drops materially by the exact April 20 noon ET minute. That supports a high Yes probability, but not certainty, because a single-minute timestamp can still be vulnerable to volatility and weekend risk.

## Reliability notes

High-quality source set. The docs are primary Binance documentation and the price/klines are direct exchange data. Independence is limited because both pieces come from Binance, but for a Binance-settled contract that concentration is appropriate rather than a flaw.