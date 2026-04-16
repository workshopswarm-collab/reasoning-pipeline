---
type: source_note
case_key: case-20260416-969f7c01
dispatch_id: dispatch-case-20260416-969f7c01-20260416T013210Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: spot-market-data
entity: ethereum
topic: ethereum-above-2200-on-april-17
question: Will the price of Ethereum be above $2,200 on April 17?
driver: reliability
date_created: 2026-04-15
source_name: Binance ETHUSDT ticker and 1-minute kline API
source_type: exchange API / primary market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT
source_date: 2026-04-15
credibility: high
recency: very-high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: market-implied
related_entities: [ethereum]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [market-implied-finding]
tags: [binance, exchange-data, primary-source, ethusdt]
---

# Summary

This source is the best current factual anchor because the contract resolves using Binance ETH/USDT 1-minute candles.

## Key facts extracted

- Binance API returned live ETHUSDT around `2352.52` to `2352.64` during the check.
- Binance 24h ticker showed:
  - lastPrice `2352.64`
  - openPrice `2335.41`
  - highPrice `2385.61`
  - lowPrice `2308.50`
  - weightedAvgPrice `2341.80`
- Recent 1-minute klines fetched successfully and showed normal trading around the same level.
- Timestamp conversion check confirmed retrieved klines corresponded to the current evening in America/New_York, validating that the API timestamps were interpreted correctly.

## Evidence directly stated by source

- Binance itself currently prints ETHUSDT comfortably above 2200 by roughly 150 points.
- The last 24h low in the fetched 24h ticker was still `2308.50`, above the 2200 threshold.
- Recent 1-minute klines were tightly clustered near the current price, not near the threshold.

## What is uncertain

- This is still a pre-resolution snapshot; ETH can move sharply in crypto markets.
- The contract resolves on one specific minute close tomorrow at noon ET, not the current spot or 24h average.
- API availability today does not guarantee no future Binance display/API issue during settlement, though the contract points to the exchange display rather than the public API specifically.

## Why this source may matter

Because the market resolves on Binance ETH/USDT, current Binance pricing is direct evidence rather than merely contextual evidence.

## Possible impact on the question

With spot near 2353 and even the recent 24h low above 2308, the market only needs ETH to avoid dropping more than about 6.5% by tomorrow noon ET. That supports a high Yes probability and explains why the market is near 95% instead of near 70%.

## Reliability notes

High-quality direct evidence for current state and contract-relevant venue. Limited by time horizon because settlement is tomorrow, not now.