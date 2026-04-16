---
type: source_note
case_key: case-20260414-d5888900
dispatch_id: dispatch-case-20260414-d5888900-20260414T143228Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-14
question: Is Binance BTC/USDT currently far enough above 70,000 that the noon ET candle is very likely to resolve Yes?
date_created: 2026-04-14
source_name: Binance public API spot and 1-minute kline checks
source_type: exchange API
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, btcusdt, live-price, kline, verification]
---

# Summary

This source note captures an additional verification pass against Binance public API data shortly before the market's noon ET settlement window.

## Key facts extracted

- Binance ticker endpoint returned BTCUSDT at 75,553.40 during the research run.
- A separate Binance 1-minute klines query returned recent candles with closes around 75,708.26, 75,649.19, and 75,553.39.
- These observed prices were roughly 7.9% to 8.2% above the 70,000 threshold.
- The assigned resolution time of 12:00 ET corresponds to 16:00 UTC.

## Evidence directly stated by source

- Direct exchange-specific BTC/USDT pricing on Binance is currently well above the contract threshold.
- Recent one-minute candles on Binance are also well above the threshold, reducing concern that the live ticker is an outlier or stale.

## What is uncertain

- This is not yet the specific 12:00 ET settlement candle; there is still residual intraday path risk before noon.
- The exact catalyst between now and noon would likely need to be a sharp negative BTC move or exchange-specific disruption.

## Why this source may matter

Because the contract settles on Binance BTC/USDT, exchange-specific direct price data is the most decision-relevant evidence available before resolution.

## Possible impact on the question

If BTC remains even moderately near this level into noon ET, the market should resolve Yes. The threshold is far enough below observed price that only a substantial pre-noon drawdown or settlement-source issue would flip the outcome.

## Reliability notes

High-quality direct source for pre-settlement verification because it matches the contract's named exchange and pair. Residual risk is timing: this check is pre-resolution, not the final noon candle itself.