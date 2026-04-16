---
type: source_note
case_key: case-20260416-c395460f
dispatch_id: dispatch-case-20260416-c395460f-20260416T022702Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: prediction-markets
entity: sol
topic: solana-above-80-on-april-19
question: Will the price of Solana be above $80 on April 19?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules for "Solana above ___ on April 19?"
source_type: market_page
source_url: https://polymarket.com/event/solana-above-on-april-19
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: variant-view
related_entities: [sol]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-c395460f/researcher-analyses/2026-04-16/dispatch-case-20260416-c395460f-20260416T022702Z/personas/variant-view.md]
tags: [polymarket, contract, market-implied-probability, resolution]
---

# Summary

The Polymarket market page gives both the current crowd-implied probability and the governing resolution mechanics. For this case, the critical non-obvious point is that settlement depends on one Binance SOL/USDT 1-minute candle close at exactly 12:00 ET on April 19, not on a daily close, average price, or cross-exchange reference.

## Key facts extracted

- The $80 line was trading around 89-90% Yes at fetch time.
- The market resolves Yes only if the Binance SOL/USDT 1-minute candle for 12:00 ET (noon) on April 19 has a final close strictly higher than $80.
- Binance is the governing source of truth.
- The contract is explicitly about Binance SOL/USDT, not other exchanges or pairs.
- Precision is determined by the decimals shown by the source.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for SOL/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance..."
- Market state on fetch: outcome 80 showing about 89% with Buy Yes around 90¢ and Buy No around 13¢.

## What is uncertain

- The page is a secondary presentation layer, not the underlying exchange data itself.
- Polymarket page snapshots can move quickly; the exact displayed percentage is time-sensitive.
- The public page does not itself provide the future settlement candle, only the rule.

## Why this source may matter

This source defines what counts. Because the contract is keyed to a single minute close on a specific exchange at a specific time, any analysis based on broader daily crypto sentiment risks overstating certainty.

## Possible impact on the question

This source supports a variant view that the market may be directionally right but still overconfident, because a single-minute, exchange-specific close is materially noisier than a broad "SOL should still be above 80 by then" intuition.

## Reliability notes

Useful and necessary as the contract source, but not sufficient by itself for the price outlook. Best paired with direct Binance data and an independent market context source.