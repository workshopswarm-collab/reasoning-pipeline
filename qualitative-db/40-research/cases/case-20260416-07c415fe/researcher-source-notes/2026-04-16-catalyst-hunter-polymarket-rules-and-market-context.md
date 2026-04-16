---
type: source_note
case_key: case-20260416-07c415fe
dispatch_id: dispatch-case-20260416-07c415fe-20260416T031541Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: tokens
entity: sol
topic: sol-above-80-april-19
question: Will the Binance SOL/USDT 12:00 ET 1-minute candle on 2026-04-19 close above 80?
driver: operational-risk
date_created: 2026-04-15T23:22:00-04:00
source_name: Polymarket market page and rules
source_type: market rules / prediction market context
source_url: https://polymarket.com/event/solana-above-on-april-19
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [sol]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-07c415fe/researcher-analyses/2026-04-16/dispatch-case-20260416-07c415fe-20260416T031541Z/personas/catalyst-hunter.md]
tags: [polymarket, rules, resolution, timezone]
---

# Summary

The Polymarket market page provides the contract wording, outcome prices, and the exact timing mechanic for settlement. For the 80 strike, the page showed roughly 89% Yes / 13% No at retrieval, while the assignment metadata gave current_price 0.92. The rule text makes clear that only the Binance SOL/USDT 1-minute candle closing at 12:00 ET on 2026-04-19 matters.

## Key facts extracted

- Resolution is based on the Binance SOL/USDT close for the 1-minute candle labeled 12:00 in ET on the specified date.
- The strike comparison is strict: the close must be higher than 80, not equal to 80.
- Price precision is whatever Binance shows.
- Other exchanges and other pairs do not count.
- At retrieval, the 80 line was trading around 89% Yes on-page; assignment metadata reported current_price 0.92.

## Evidence directly stated by source

- Governing source of truth: Binance SOL/USDT 1-minute candle.
- Governing timestamp: 12:00 ET on 2026-04-19.
- Market-implied probability from current price is about 92% using assignment metadata.

## What is uncertain

- The page price can move intraday; assignment metadata and on-page view were close but not identical.
- The page itself is not the settlement source for price; it only defines rules and market consensus.

## Why this source may matter

This source is necessary to avoid a contract-interpretation mistake. A case that looks easy on spot levels can still be misread if the wrong exchange, timezone, pair, candle, or inequality sign is used.

## Possible impact on the question

The rules narrow the analysis to a single Binance one-minute close on Sunday at noon ET. That makes timing and weekend crypto volatility more important than generic medium-term Solana fundamentals.

## Reliability notes

- Good source for contract wording and market baseline.
- Not independent evidence on actual future price path.
