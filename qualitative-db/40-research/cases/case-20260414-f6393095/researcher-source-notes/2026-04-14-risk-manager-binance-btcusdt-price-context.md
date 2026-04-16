---
type: source_note
case_key: case-20260414-f6393095
dispatch_id: dispatch-case-20260414-f6393095-20260414T222237Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close above 70000 on April 17, 2026?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance API BTCUSDT price and 1m kline context
source_type: exchange market data
source_url: https://api.binance.com/api/v3/uiKlines?symbol=BTCUSDT&interval=1m&limit=3
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, btcusdt, price-context, resolution-source]
---

# Summary

This source note captures the live Binance BTC/USDT context closest to the research time and the exact source family that governs market resolution.

## Key facts extracted

- Binance ticker at research time showed BTC/USDT around 74,066.
- Recent 1-minute candles from Binance were closing in the 74,061 to 74,085 range.
- Binance 24h stats showed intraday high near 76,038 and low near 73,795, implying normal volatility still leaves BTC materially above the 70,000 strike.
- Because the market resolves from the Binance BTC/USDT 1-minute candle at 12:00 ET on Apr. 17, exchange-specific prints and exact minute timing matter more than broader BTC/USD references.

## Evidence directly stated by source

- `ticker/price` returned `{"symbol":"BTCUSDT","price":"74066.00000000"}`.
- `uiKlines` returned recent 1-minute candles including closes at `74061.56000000`, `74084.75000000`, and `74066.00000000`.
- `ticker/24hr` returned `highPrice` `76038.00000000` and `lowPrice` `73795.47000000`.

## What is uncertain

- This source does not directly answer the Apr. 17 noon ET close; it only sets the current starting point and volatility context.
- API availability does not by itself guarantee smooth UI visibility at resolution time, though the contract names Binance as source of truth.

## Why this source may matter

It is the governing exchange/source family for settlement and also the most direct current measure of distance to the 70,000 threshold.

## Possible impact on the question

Starting from roughly 74.1k means BTC can fall about 5.5% over the next roughly 42 hours and still resolve Yes. That supports a high Yes probability, but not certainty, because a crypto asset can move that much over two days and the contract is tied to one exact minute on one exchange.

## Reliability notes

High relevance and high recency. This is the best direct source for both contract interpretation and current level context. Main residual risk is exchange-specific operational or data-access ambiguity at the exact resolution minute, not source irrelevance.