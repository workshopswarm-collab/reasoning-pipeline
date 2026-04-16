---
type: source_note
case_key: case-20260415-68974052
dispatch_id: dispatch-case-20260415-68974052-20260415T183011Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-68974052 | risk-manager
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTC/USDT API and Polymarket market rules page
source_type: primary_and_resolution_context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-68974052/researcher-analyses/2026-04-15/dispatch-case-20260415-68974052-20260415T183011Z/personas/risk-manager.md]
tags: [binance, polymarket, resolution, btc]
---

# Summary

This note captures the direct source-of-truth mechanics and current reference price context for the Apr 17 BTC > 72,000 contract.

## Key facts extracted

- Polymarket rules state the market resolves from the Binance BTC/USDT 1 minute candle for **12:00 in ET timezone (noon)** on Apr 17, 2026.
- Resolution condition is the candle's final **Close** price being **higher than 72,000**.
- The contract is Binance-specific and pair-specific: **BTC/USDT**, not other exchanges or pairs.
- Current Binance spot API reference fetched on 2026-04-15 showed **BTCUSDT = 74,233.75**.
- Recent 1-minute Binance klines fetched at the same time showed closes clustered around **74.18k-74.23k**, confirming price was materially above the 72k threshold at time of research.
- The assignment resolution timestamp of **2026-04-17 12:00 ET** converts to **2026-04-17 16:00 UTC**.

## Evidence directly stated by source

- Polymarket directly states the governing market rule and source of truth.
- Binance API directly states current BTC/USDT price and recent 1-minute candle close data.

## What is uncertain

- These current prices do not settle the contract because the relevant print is the Apr 17 noon ET 1-minute close, about two days after the research timestamp.
- API snapshots do not guarantee Binance website candle display or future data availability edge cases.
- Short-horizon BTC volatility could still pull price below 72,000 by the governing minute.

## Why this source may matter

This is the core direct evidence for both contract interpretation and whether the threshold is presently in or out of the money. It also clarifies the key risk: the market is really about a single future minute close on one exchange, not about general BTC direction.

## Possible impact on the question

The current level above 74k supports a positive base case for >72k, but the risk-manager read is that traders may still be underpricing path risk and single-minute exchange-specific settlement risk when pricing the contract in the mid-80s.

## Reliability notes

- Binance is the named settlement source, so source-of-truth relevance is high even if exchange-specific operational idiosyncrasies remain.
- Polymarket market rules page is authoritative for contract mechanics but not for the future underlying value.
- Independence between these two sources is medium at best because both point back to the same settlement design; they help verify mechanics more than diversify causal evidence.