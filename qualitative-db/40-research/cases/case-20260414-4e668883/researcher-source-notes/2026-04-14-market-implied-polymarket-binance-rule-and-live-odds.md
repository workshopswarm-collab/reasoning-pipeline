---
type: source_note
case_key: case-20260414-4e668883
dispatch_id: dispatch-case-20260414-4e668883-20260414T133938Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: protocols
entity: ethereum
topic: will-ethereum-reach-2400-april-13-19
question: Will Ethereum reach $2,400 April 13-19?
driver: liquidity
date_created: 2026-04-14
source_name: Polymarket Gamma API event payload for ETH weekly price ladder
source_type: market contract / resolution source metadata
source_url: https://gamma-api.polymarket.com/events?slug=what-price-will-ethereum-hit-april-13-19
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: market-implied
related_entities: [ethereum]
related_drivers: [liquidity]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-4e668883/researcher-analyses/2026-04-14/dispatch-case-20260414-4e668883-20260414T133938Z/personas/market-implied.md]
tags: [polymarket, binance, rules, resolution, live-odds]
---

# Summary

This source provides the actual contract mechanics and current pricing for the target market. It is the key source for both the governing source of truth and the market-implied probability baseline.

## Key facts extracted

- The exact target market slug is `will-ethereum-reach-2400-april-13-19`.
- The market resolves Yes if **any Binance 1-minute candle for ETH/USDT** during Apr 13 12:00 AM ET through Apr 19 11:59 PM ET has a final **High** at or above 2400.
- The resolution source is Binance ETH/USDT with the chart set to 1-minute candles.
- Other exchanges, other pairs, and generic spot references do not govern settlement.
- Current outcome prices in the API snapshot were `["0.9185", "0.0815"]`, implying about a 91.85% Yes probability.
- Reported last trade was 0.913, best bid 0.902, best ask 0.935, with roughly $40.3k volume in this line and material liquidity across the full ETH ladder event.

## Evidence directly stated by source

- Direct rule text states the market resolves on Binance 1-minute candle highs during the specified ET date range.
- Direct pricing fields state current market odds and recent price change.

## What is uncertain

- The API snapshot is a point-in-time quote and can move.
- The source does not itself explain why traders are willing to pay such high odds; that requires contextual interpretation.

## Why this source may matter

It is both the primary contract-definition source and the cleanest direct read on what the market is currently implying.

## Possible impact on the question

It sharply lowers source-of-truth ambiguity. Because settlement only requires one qualifying Binance 1-minute high, the bar is easier to clear than requiring a sustained close above 2400 across exchanges.

## Reliability notes

High reliability for rules and live market state because it is the platform's own event payload. It is less useful for independent price validation, so it should be paired with external live price references.