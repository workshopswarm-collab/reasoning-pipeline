---
type: source_note
case_key: case-20260416-97839980
dispatch_id: dispatch-case-20260416-97839980-20260416T040518Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: tokens
entity: sol
topic: solana-above-80-on-april-19
question: Will the price of Solana be above $80 on April 19?
driver: reliability
date_created: 2026-04-16
source_name: Polymarket market page and rules for Solana above 80 on April 19
source_type: market rules / primary contract source
source_url: https://polymarket.com/event/solana-above-on-april-19
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [sol]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-97839980/researcher-analyses/2026-04-16/dispatch-case-20260416-97839980-20260416T040518Z/personas/market-implied.md]
tags: [source-note, polymarket, rules, resolution]
---

# Summary

Primary contract-definition source. The market page states that this resolves yes if the Binance 1-minute candle for SOL/USDT at 12:00 ET on April 19 has a final close above 80. This is the core source-of-truth document for what counts.

## Key facts extracted

- Outcome depends on the Binance SOL/USDT 1-minute candle labeled 12:00 in ET timezone.
- The relevant field is the candle's final `Close` price.
- The threshold condition is strictly higher than 80.
- The relevant venue/pair is Binance SOL/USDT, not another exchange or pair.
- Precision is determined by the source's displayed decimal precision.

## Evidence directly stated by source

- Exact resolution mechanic and source of truth.
- Exact timing reference: 12:00 ET on the specified date.
- Exact price comparison logic: higher than 80.

## What is uncertain

- The page itself does not provide a historical distribution for how likely SOL is to remain above 80 by settlement.
- The page does not clarify any exchange outage contingency on the visible snippet beyond naming Binance as the source.

## Why this source may matter

This market is date-sensitive and rule-sensitive. The main analytical risk is not misunderstanding SOL broadly; it is misunderstanding the exact resolution condition. This source governs that condition.

## Possible impact on the question

It narrows the question to one exchange, one pair, one minute, one closing field, and one timezone reference. Any probability estimate must be about that exact event, not about generic end-of-day crypto prices.

## Reliability notes

High credibility as the contract-definition surface. It is authoritative for market wording, but not independent evidence about the underlying asset path. It should be paired with Binance price context before making a probability judgment.