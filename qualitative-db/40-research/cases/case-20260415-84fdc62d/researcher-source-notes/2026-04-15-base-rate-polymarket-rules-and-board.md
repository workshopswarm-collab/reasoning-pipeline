---
type: source_note
case_key: case-20260415-84fdc62d
dispatch_id: dispatch-case-20260415-84fdc62d-20260415T125809Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-20 be above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page and rules
source_type: market rules / market board
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [base-rate-finding]
tags: [polymarket, rules, resolution-source, market-implied-probability]
---

# Summary

This source establishes the current market-implied probability and the governing resolution mechanics.

## Key facts extracted

- The specific line for this case is 70,000 and the displayed market probability is about 86% yes.
- The market resolves from the Binance BTC/USDT 1-minute candle labeled 12:00 in ET timezone on April 20, 2026.
- Resolution depends on the final candle close being strictly higher than 70,000.
- The contract is exchange-specific and pair-specific: Binance BTC/USDT, not another exchange or pair.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices..."

## What is uncertain

- The event page is not itself the final source of truth; it quotes the governing source and points to Binance.
- The page does not independently verify what the Binance candle will print on April 20.

## Why this source may matter

The case is date-sensitive and rule-sensitive. This source is required to identify the exact timing, price condition, and official settlement venue.

## Possible impact on the question

It narrows the question to a very specific noon ET Binance print. That means broad claims like "Bitcoin is trading above 70k this week" are insufficient unless they imply the Binance BTC/USDT noon candle on the exact date will likely remain above 70k.

## Reliability notes

Useful and necessary for contract interpretation, but only medium credibility as an outcome predictor. It is strongest for rules and current pricing, not for forecasting the final result.