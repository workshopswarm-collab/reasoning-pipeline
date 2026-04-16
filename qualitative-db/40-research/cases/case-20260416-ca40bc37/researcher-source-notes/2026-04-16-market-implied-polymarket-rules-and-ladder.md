---
type: source_note
case_key: case-20260416-ca40bc37
dispatch_id: dispatch-case-20260416-ca40bc37-20260416T053546Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-20
question: Will the price of Bitcoin be above $72,000 on April 20?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page and rules
source_type: market page / primary contract source
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-16
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
downstream_uses: [qualitative-db/40-research/cases/case-20260416-ca40bc37/researcher-analyses/2026-04-16/dispatch-case-20260416-ca40bc37-20260416T053546Z/personas/market-implied.md]
tags: [polymarket, resolution-rules, bitcoin, binance]
---

# Summary

This source establishes the market-implied baseline and the operative resolution mechanics for the contract.

## Key facts extracted

- The assigned current market price for the $72,000 line is 0.845, i.e. roughly 84.5% implied probability.
- The Polymarket page showed the $72,000 bracket around 85% at fetch time, broadly consistent with the assignment's 0.845 input.
- The contract resolves using the Binance BTC/USDT 1-minute candle for **12:00 in ET timezone (noon)** on **April 20, 2026**.
- The relevant value is the candle's final **Close** price, and it must be **higher than $72,000** for Yes.
- The market explicitly says the source is Binance BTC/USDT, not other exchanges or trading pairs.
- Precision is determined by the displayed decimal places in the source.

## Evidence directly stated by source

Directly stated rule text: the market resolves to Yes if the Binance 1-minute candle for BTC/USDT at 12:00 ET on the specified date has a final Close price above the strike; otherwise No.

## What is uncertain

- The page is not itself the settlement authority; Binance is.
- The page does not explain operational contingencies beyond the stated source/rule text.
- The fetched HTML is enough to preserve rule wording, but not a clean live chart state from Binance.

## Why this source may matter

This is the governing contract surface for what counts. Because the market is date-sensitive and wording-sensitive, the exact time, timezone, exchange, pair, and field (Close) materially matter.

## Possible impact on the question

This source narrows the problem from general BTC direction to a specific noon-ET Binance print on April 20. That makes timing and exchange-specific resolution more important than broad daily spot averages.

## Reliability notes

Good for contract wording and contemporaneous market-implied odds; only medium as a settlement source because the rules themselves point onward to Binance as the governing source of truth.