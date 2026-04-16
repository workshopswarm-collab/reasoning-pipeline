---
type: source_note
case_key: case-20260416-63fb3082
dispatch_id: dispatch-case-20260416-63fb3082-20260416T145628Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: market-structure
entity: btc
topic: bitcoin-above-68k-on-april-21
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close above 68000 on April 21, 2026?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket event page and rules
source_type: market rules / platform listing
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-16
credibility: medium-high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, resolution-rules, market-implied-probability, binance]
---

# Summary

This source establishes the contract mechanics, the market-implied baseline, and the governing source of truth.

## Key facts extracted

- Current market price provided in case metadata is 0.9525, implying about 95.25% Yes probability.
- The contract resolves Yes only if the Binance BTC/USDT 1-minute candle for **12:00 ET** on 2026-04-21 has a final **Close** strictly higher than 68,000.
- The contract is specifically tied to Binance BTC/USDT, not other exchanges or other pairs.
- Price precision is determined by Binance source precision.

## Evidence directly stated by source

- The Polymarket rules page states the market resolves using the Binance BTC/USDT candle with 1m interval and Candles selected.
- The page lists the April 21 68,000 line at roughly 96%, consistent with the case snapshot current_price 0.9525.

## What is uncertain

- The public web page does not itself prove what the future 2026-04-21 12:00 ET candle will be.
- The page references Binance UI as the resolution surface, but operationally the relevant underlying data come from Binance market data; UI display details or late corrections are not fully specified.

## Why this source may matter

This is the primary contract-definition source. For a narrow, date-specific crypto price market, wording around exchange, pair, timeframe, timezone, and strict greater-than condition matters as much as directional BTC price context.

## Possible impact on the question

This source sharply limits what counts. Even if spot BTC trades above 68k elsewhere or at nearby times, the market is No unless the Binance BTC/USDT 12:00 ET one-minute candle close itself is above 68,000.

## Reliability notes

High utility for contract interpretation; medium-high credibility for market mechanics because it is the platform listing itself. It is not evidence about future price direction, only about how resolution will be determined.