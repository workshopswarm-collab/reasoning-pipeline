---
type: source_note
case_key: case-20260416-243d5bed
dispatch_id: dispatch-case-20260416-243d5bed-20260416T161511Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: exchange-market-structure
entity: ethereum
topic: ethereum-above-2300-on-april-17
question: Will the Binance ETH/USDT 1-minute candle for 2026-04-17 12:00 ET close above 2300?
driver: reliability
date_created: 2026-04-16
source_name: Binance Spot API ETHUSDT ticker and 1m klines
source_type: exchange-api
source_url: https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [ethereum]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-243d5bed/researcher-analyses/2026-04-16/dispatch-case-20260416-243d5bed-20260416T161511Z/personas/variant-view.md]
tags: [binance, ethusdt, api, settlement-source, timing]
---

# Summary

Direct exchange-data check on Binance's public spot API to validate current ETH/USDT level, confirm 1-minute kline availability, and map the contract's noon ET settlement minute into UTC.

## Key facts extracted

- Binance spot ticker returned `{"symbol": "ETHUSDT", "price": "2339.44000000"}` on 2026-04-16.
- Binance 1-minute klines endpoint returned recent candles with close values between roughly 2335 and 2339 during 2026-04-16 16:13-16:17 UTC.
- The contract's settlement minute of 2026-04-17 12:00 ET maps to 2026-04-17 16:00 UTC.
- Binance kline timestamps in the API are in UTC milliseconds, so the relevant resolution minute can be mapped cleanly even though the market wording expresses the time in ET.

## Evidence directly stated by source

- Current Binance ETH/USDT spot price is above 2300.
- Binance publishes 1-minute klines for ETHUSDT with distinct close prices and timestamps.

## What is uncertain

- The Polymarket rule references the Binance trading interface rather than the public API, so there is slight operational ambiguity over whether any UI rounding/display convention could differ from raw API values.
- This source does not itself say what ETH will be at 2026-04-17 16:00 UTC; it only establishes the current level and the practicality of the settlement mechanism.

## Why this source may matter

This is the closest direct machine-readable analogue to the named resolution source. It materially reduces ambiguity around whether the contract is really about a single Binance ETH/USDT 1-minute close and how the ET timestamp maps into Binance's UTC-based market data.

## Possible impact on the question

Because ETH/USDT is already about 1.7% above 2300 with less than a day remaining, the market only needs ETH to avoid a modest downside move into the specific noon ET minute. That supports a Yes-lean but not certainty, because a normal crypto intraday swing can still erase a 1.7% cushion.

## Reliability notes

- High credibility for current price/mechanics because the source is Binance's own public API.
- Medium relevance for final settlement because Polymarket names Binance UI candles as the governing source of truth, not the API explicitly.
- Best used as direct verification of current price and resolution mechanics, not as a standalone forecast source.