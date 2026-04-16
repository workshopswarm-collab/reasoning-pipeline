---
type: source_note
case_key: case-20260416-97839980
dispatch_id: dispatch-case-20260416-97839980-20260416T040518Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: market-structure
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 12:00 ET 1-minute candle close above 80 on April 19, 2026?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page and rules
source_type: market_contract
source_url: https://polymarket.com/event/solana-above-on-april-19
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: risk-manager
related_entities: [sol]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-97839980/researcher-analyses/2026-04-16/dispatch-case-20260416-97839980-20260416T040518Z/personas/risk-manager.md]
tags: [polymarket, rules, resolution, source-note]
---

# Summary

This source establishes the governing contract mechanics and the market-implied baseline. It matters because this is a date-sensitive, narrow-resolution market with a specific exchange, pair, and timestamp.

## Key facts extracted

- The market resolves Yes if the Binance SOL/USDT 1-minute candle for 12:00 in ET timezone on April 19, 2026 has a final Close price strictly higher than 80.
- The resolution source is Binance spot SOL/USDT with 1m candles selected.
- Price precision is determined by Binance source precision.
- The market page showed the 80 strike at roughly 92% at fetch time.

## Evidence directly stated by source

- Resolution depends on Binance SOL/USDT, not other exchanges or other pairs.
- The relevant observation is the final Close of the 12:00 ET one-minute candle, not intraday highs or daily closes.
- "Higher than" means strictly above 80; touching 80.00 would not be enough.

## What is uncertain

- The fetch is a website rendering rather than a structured API export, so displayed probabilities can move and UI extraction can be noisy.
- The page does not itself prove what the Binance candle will be; it only defines the contract and current market consensus.

## Why this source may matter

This is the source for what counts. In a narrow-resolution market, contract wording and timestamp interpretation can be as important as directional price view.

## Possible impact on the question

It narrows the relevant risk analysis to: (1) where SOL trades versus 80 near April 19 noon ET, (2) whether Binance spot specifically stays above that level, and (3) whether last-minute volatility could flip the one-minute close.

## Reliability notes

Useful as the governing contract source and market-consensus snapshot, but not independent evidence about future SOL price direction.