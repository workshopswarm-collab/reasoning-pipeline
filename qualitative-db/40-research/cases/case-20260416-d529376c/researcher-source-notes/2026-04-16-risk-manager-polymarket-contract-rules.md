---
type: source_note
case_key: case-20260416-d529376c
dispatch_id: dispatch-case-20260416-d529376c-20260416T030247Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: prediction-markets
entity:
topic: case-20260416-d529376c | risk-manager
question: What exactly must happen for this market to resolve Yes?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket event page rules for solana-above-on-april-19
source_type: market_rules
source_url: https://polymarket.com/event/solana-above-on-april-19
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: []
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-d529376c/researcher-analyses/2026-04-16/dispatch-case-20260416-d529376c-20260416T030247Z/personas/risk-manager.md]
tags: [polymarket, contract-rules, resolution-mechanics, source-of-truth]
---

# Summary

The Polymarket rules define a narrow, timing-sensitive resolution condition: only the Binance SOL/USDT one-minute candle for 12:00 ET on Apr 19 matters, and the final close must be higher than 80.

## Key facts extracted

- Market resolves Yes if the Binance SOL/USDT 1-minute candle for `12:00` in ET on Apr 19 has a final close price `higher` than 80.
- Otherwise the market resolves No.
- Resolution source is Binance, specifically the SOL/USDT trading page with `1m` and `Candles` selected.
- The market is explicitly about Binance SOL/USDT, not other exchanges or pairs.
- Price precision is determined by the number of decimal places shown by the source.

## Evidence directly stated by source

- The contract wording directly defines the settlement test and governing venue.
- The page also shows the current market-implied probability around `89%` for the `80` strike outcome at review time.

## What is uncertain

- The rules do not elaborate on edge cases such as temporary chart glitches, delayed candle revisions, or any discrepancy between UI display and API values.
- The extracted page text showed duplicated rules blocks, but the wording itself was consistent.

## Why this source may matter

This is the formal contract surface. It determines what counts and what does not count, which is essential because this is a narrow-resolution, date-sensitive market.

## Possible impact on the question

This source makes clear that general bullishness on SOL is not enough. The exact noon ET Binance close must remain above 80, so timing and venue-specific path risk matter.

## Reliability notes

High credibility as the contract-governing market page. The main limitation is minor implementation ambiguity around how Binance page values are operationally read if the UI and API ever diverge.