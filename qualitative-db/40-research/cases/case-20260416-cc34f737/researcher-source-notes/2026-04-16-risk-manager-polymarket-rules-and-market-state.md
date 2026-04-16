---
type: source_note
case_key: case-20260416-cc34f737
dispatch_id: dispatch-case-20260416-cc34f737-20260416T162722Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: prediction-markets
entity:
topic: case-20260416-cc34f737 | risk-manager
question: Will the Binance ETH/USDT 1 minute candle for 12:00 ET on 2026-04-17 close above 2300?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page and rules for Ethereum above 2300 on April 17
source_type: market rules / market state
source_url: https://polymarket.com/event/ethereum-above-on-april-17
source_date: 2026-04-16
credibility: medium-high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [ethereum]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-cc34f737/researcher-analyses/2026-04-16/dispatch-case-20260416-cc34f737-20260416T162722Z/personas/risk-manager.md]
tags: [polymarket, binance, resolution-rules, market-implied-probability]
---

# Summary

This source establishes both the governing resolution mechanics and the current market-implied baseline. It is the primary source for how the contract resolves and what the market currently prices.

## Key facts extracted

- Current market price for the 2300 line is about 71% Yes on the fetched page; assignment context lists current_price 0.72, so market-implied probability is roughly 71-72%.
- The market resolves Yes only if the Binance ETH/USDT 1 minute candle for 12:00 in ET timezone on 2026-04-17 has a final Close strictly higher than 2300.
- The resolution source is Binance ETH/USDT with 1m candles selected.
- The contract is specifically about Binance ETH/USDT, not other exchanges or other pairs.
- Price precision is determined by Binance source decimals.

## Evidence directly stated by source

- Exact resolution wording: Yes if the Binance 1 minute candle for ETH/USDT 12:00 in ET timezone on the specified date has a final Close price higher than 2300; otherwise No.
- Binance is the governing source of truth.
- The market page showed the 2300 bracket at roughly 71% Yes during fetch.

## What is uncertain

- The market page fetch is not a perfect archival record of every trade or intraday move.
- The rules point to Binance UI candles rather than a formal API schema, so an operational distinction remains between Binance UI display and raw exchange API values, though they should normally align.
- The exact final noon ET candle cannot be known until settlement time.

## Why this source may matter

This source is mandatory because the case is narrow, date-sensitive, and rule-sensitive. The risk analysis depends on the exact source of truth, the timezone, the candle granularity, and the strict-greater-than threshold.

## Possible impact on the question

This source narrows the question from generic ETH direction to a specific operational condition: ETH/USDT on Binance must still be above 2300 at the close of the noon ET 1-minute candle on April 17. That makes timing/path risk materially relevant.

## Reliability notes

High reliability on contract wording because this is the market operator’s own page. Moderate source-of-truth ambiguity remains because resolution references the Binance trading interface rather than a separately documented settlement API endpoint.