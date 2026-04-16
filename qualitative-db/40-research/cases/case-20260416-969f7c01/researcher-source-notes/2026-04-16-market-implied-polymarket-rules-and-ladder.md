---
type: source_note
case_key: case-20260416-969f7c01
dispatch_id: dispatch-case-20260416-969f7c01-20260416T013210Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: prediction-markets
entity: ethereum
topic: ethereum-above-2200-on-april-17
question: Will the price of Ethereum be above $2,200 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules for Ethereum above on April 17
source_type: market page / contract rules
source_url: https://polymarket.com/event/ethereum-above-on-april-17
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: market-implied
related_entities: [ethereum]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [market-implied-finding]
tags: [polymarket, contract-rules, source-of-truth, resolution]
---

# Summary

This source establishes the market-implied baseline and the contract-resolution mechanics. It is the key source for what must happen for the market to resolve Yes or No.

## Key facts extracted

- The specific threshold market is `2,200` for April 17.
- The displayed market price on the page was about 95% Yes for `2,200`, consistent with the assignment current_price of `0.945`.
- The contract resolves Yes if the Binance ETH/USDT 1-minute candle for `12:00` in ET timezone on April 17 has a final `Close` price strictly higher than 2200.
- The resolution source is Binance ETH/USDT with `1m` candles selected.
- The contract is specifically about Binance ETH/USDT, not other venues or trading pairs.
- Price precision is determined by Binance source decimals.

## Evidence directly stated by source

- Rules directly define the source of truth.
- The page directly shows the market ladder around the threshold; at fetch time, `2,200` traded around 95% Yes while `2,300` was materially lower and `2,400` much lower, implying a market-centered distribution in the low-to-mid 2300s rather than an indiscriminate bullish extreme.

## What is uncertain

- The page itself is not the final authoritative settlement record; Binance is.
- The fetched page is a snapshot and can move.
- The exact noon ET candle close is tomorrow, so the current market price remains an estimate, not a settlement.

## Why this source may matter

This is the governing interpretive source for the contract. It tells us both the probability baseline and the exact material conditions for resolution.

## Possible impact on the question

If the market is already pricing the threshold at ~95% while neighboring strikes show a plausible distribution, then the market is likely anchoring on current Binance spot being comfortably above 2200 plus only modest required time decay over less than one day.

## Reliability notes

Strong for contract interpretation and market baseline. Not sufficient alone for the factual price view because the actual resolution source is Binance and the market can be stale or overreactive.