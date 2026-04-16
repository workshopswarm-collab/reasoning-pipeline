---
type: source_note
case_key: case-20260416-cd7fa6c7
dispatch_id: dispatch-case-20260416-cd7fa6c7-20260416T010113Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-74k-on-april-17
question: Will the price of Bitcoin be above $74,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-cd7fa6c7/researcher-analyses/2026-04-16/dispatch-case-20260416-cd7fa6c7-20260416T010113Z/personas/market-implied.md]
tags: [polymarket, rules, resolution, btc, binance]
---

# Summary

This source establishes the governing resolution mechanics and the current market-implied probability for the 74,000 strike.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17 has a final close price higher than 74,000.
- The relevant source of truth is Binance BTC/USDT with 1m candles, not another exchange or BTC/USD pair.
- The market page showed the 74,000 strike around 64%-65% at fetch time.
- Nearby ladder pricing was internally coherent: 72,000 around 92%, 76,000 around 27%, suggesting a reasonably smooth distribution rather than an obvious stale outlier.

## Evidence directly stated by source

- Resolution depends on the Binance BTC/USDT 12:00 ET candle close.
- Precision is determined by the source decimals.
- The strike-specific market price for 74,000 was displayed around 65 cents.

## What is uncertain

- The public page is not itself the final official settlement print; it only states the rule and current market price.
- The page does not directly provide the future April 17 noon candle close, only the contract mechanics and current crowd pricing.

## Why this source may matter

It is the primary contract source. For a date-sensitive and source-sensitive market, the answer depends materially on exact timing, exchange, pair, and candle-close interpretation.

## Possible impact on the question

This source frames the market-implied baseline at about 65% and makes clear that any thesis using BTC/USD from another venue would be secondary context only.

## Reliability notes

High relevance and high credibility for contract interpretation. Moderate limitation for price discovery because the webpage is a market interface rather than the Binance execution data itself.