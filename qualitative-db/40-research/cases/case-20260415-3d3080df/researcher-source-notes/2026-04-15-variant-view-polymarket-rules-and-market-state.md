---
type: source_note
case_key: case-20260415-3d3080df
dispatch_id: dispatch-case-20260415-3d3080df-20260415T002239Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: markets
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on April 20, 2026 be above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market rules / platform page
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
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
downstream_uses: [qualitative-db/40-research/cases/case-20260415-3d3080df/researcher-analyses/2026-04-15/dispatch-case-20260415-3d3080df-20260415T002239Z/personas/variant-view.md]
tags: [polymarket, rules, resolution, binance, btc]
---

# Summary

This source establishes the governing resolution mechanics and the contemporaneous market-implied probability. It matters more for contract interpretation than for directional BTC fundamentals.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 20, 2026 has a final Close price strictly higher than 70,000.
- The source of truth is Binance BTC/USDT, not other exchanges or BTC/USD pairs.
- Price precision is determined by Binance source precision.
- The market page showed the 70,000 line trading around 85% at the time of review.

## Evidence directly stated by source

- Resolution depends on the Binance BTC/USDT candle close at 12:00 ET.
- The market is explicitly tied to the noon ET minute, which means timing and timezone matter.
- The contract uses a strict greater-than threshold rather than greater-than-or-equal.

## What is uncertain

- The market page is not the primary exchange data source for the final close; it only restates the intended rules.
- The fetched page showed buy/sell quotes around 86c/16c rather than a clean midpoint, so the exact implied probability is approximate.

## Why this source may matter

This is the governing contract surface. The market is date-sensitive and rule-sensitive, so a correct reading of the resolution mechanics is mandatory before making any probability judgment.

## Possible impact on the question

The rules modestly support the Yes side because BTC is already above 70,000 by a wide margin, but they also highlight a hidden path to No: a brief drawdown specifically at noon ET on Binance could decide the contract even if broader BTC sentiment remains bullish.

## Reliability notes

Reliable for contract wording and displayed market state, but not sufficient by itself for final settlement because the actual source of truth is the Binance candle data referenced by the rules.