---
type: source_note
case_key: case-20260416-dfb8f85e
dispatch_id: dispatch-case-20260416-dfb8f85e-20260416T140232Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-dfb8f85e | risk-manager
question: Will the price of Bitcoin be above $72,000 on April 21?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market rules page for bitcoin-above-on-april-21
source_type: market rule / resolution source summary
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-16
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-dfb8f85e/researcher-analyses/2026-04-16/dispatch-case-20260416-dfb8f85e-20260416T140232Z/personas/risk-manager.md]
tags: [polymarket, resolution-rules, binance, btcusdt, noon-et]
---

# Summary

This source establishes the governing contract mechanics. It says the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 21 has a final Close price strictly higher than 72,000.

## Key facts extracted

- Resolution depends on the Binance BTC/USDT pair only.
- The relevant datapoint is the 1-minute candle labeled 12:00 in ET timezone.
- The decisive field is the final Close value, not intraminute high or a broader daily close.
- The threshold is strictly higher than 72,000.
- Price precision is whatever Binance displays in the source.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title."
- "The resolution source for this market is Binance... BTC/USDT... with \"1m\" and \"Candles\" selected."

## What is uncertain

- The public web UI can be awkward to audit mechanically, so direct API or chart checks remain useful for context even though the rules identify the governing source.
- The exact candle labeling convention in the Binance UI should still be treated carefully at resolution time because timezone conversion matters.

## Why this source may matter

This is the source-of-truth surface for what counts. It narrows the question to one exchange, one pair, one minute, one timezone, and one field.

## Possible impact on the question

It materially raises timing/path risk. Bitcoin can trade above 72k over a multi-day window yet still resolve No if the specific Binance noon-ET 1-minute Close on April 21 finishes at 72,000 or lower.

## Reliability notes

Primary for contract interpretation. High relevance and high authority for settlement logic, but not itself evidence about where BTC will trade on April 21.
