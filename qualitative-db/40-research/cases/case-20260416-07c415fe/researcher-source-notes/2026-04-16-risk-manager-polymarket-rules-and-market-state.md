---
type: source_note
case_key: case-20260416-07c415fe
dispatch_id: dispatch-case-20260416-07c415fe-20260416T031541Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: markets
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 12:00 ET one-minute candle on 2026-04-19 close above 80?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket event page and rules for "Solana above ___ on April 19?"
source_type: market rules / market state
source_url: https://polymarket.com/event/solana-above-on-april-19
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [sol]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-07c415fe/researcher-analyses/2026-04-16/dispatch-case-20260416-07c415fe-20260416T031541Z/personas/risk-manager.md]
tags: [polymarket, market-rules, resolution-source, timing]
---

# Summary

This source establishes the governing market rules, current market-implied probability, and the exact source-of-truth mechanics for resolution.

## Key facts extracted

- The market resolves based on the Binance SOL/USDT 1-minute candle for **12:00 ET (noon)** on **2026-04-19**.
- The relevant value is the candle's final **"Close"** price, not the intraminute high/low and not another exchange.
- The threshold is **strictly higher than $80** for a Yes resolution.
- The event page showed the **80** strike at roughly **89%-90% Yes** at fetch time.
- The page also showed nearby strikes with steep probability changes: around **12%-13% Yes at 90**, which is useful context for how traders are viewing the distribution over the next few days.

## Evidence directly stated by source

- Resolution source: Binance SOL/USDT with 1m candles selected.
- Resolution condition: the 12:00 ET candle close must be higher than the specified threshold.
- Precision is determined by Binance source decimals.

## What is uncertain

- The fetched page is not an official Binance rulebook and may not preserve every UI edge case.
- Market state on Polymarket can move quickly, so the implied probability is a timestamped observation rather than a stable constant.
- The page does not itself provide the future 2026-04-19 noon candle; it only defines how that later value will be checked.

## Why this source may matter

This is the governing contract source for what counts. The biggest risk in a simple-looking crypto price market is often not directional but mechanical: wrong exchange, wrong pair, wrong timestamp, or confusion between spot price and the exact one-minute closing print.

## Possible impact on the question

This source materially lowers interpretation ambiguity: to get Yes, all material conditions must hold simultaneously — Binance, SOL/USDT, the 12:00 ET one-minute candle on Apr. 19, and a final close strictly above 80. It supports a high Yes probability because current market state is already above 80, but it also highlights timing and microstructure risk.

## Reliability notes

The rules section is the direct market contract surface and therefore highly relevant, but the page is still a market venue page rather than the underlying settlement data source. For actual eventual settlement, Binance remains the stronger source of truth for the price print itself.