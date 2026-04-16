---
type: source_note
case_key: case-20260416-1f25d147
dispatch_id: dispatch-case-20260416-1f25d147-20260416T035120Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: solana
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 12:00 ET one-minute candle on 2026-04-19 close above 80?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market rules / market pricing
source_url: https://polymarket.com/event/solana-above-on-april-19
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: orchestrator
related_entities: [sol, solana]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-1f25d147/researcher-analyses/2026-04-16/dispatch-case-20260416-1f25d147-20260416T035120Z/personas/catalyst-hunter.md]
tags: [polymarket, rules, resolution, pricing, catalyst-hunter]
---

# Summary

The Polymarket market page provides both the explicit contract mechanics and the current market-implied probability for the $80 strike. It says resolution is based on the Binance SOL/USDT one-minute candle at 12:00 ET on April 19, using the candle's final close.

## Key facts extracted

- The market resolves Yes if the Binance SOL/USDT 1-minute candle for 12:00 ET on April 19 has a final close above 80.
- The source of truth is Binance, not another exchange and not another trading pair.
- Price precision is determined by Binance source precision.
- On fetch, the $80 line was trading around 92% Yes.

## Evidence directly stated by source

- Resolution depends on a single specific timestamped one-minute candle.
- The operative market is Binance SOL/USDT.
- The market page displayed the $80 outcome around 92%.

## What is uncertain

- The page is a web rendering rather than an API pull, so it is adequate for rules/context but not ideal for high-precision live market microstructure.
- The page does not itself provide a clean downloadable historical time series for this exact line.

## Why this source may matter

This is the governing contract source for what counts. It narrows the question from general “Will SOL trade above 80 sometime?” to the much more specific condition that the Binance noon-ET one-minute close on April 19 must be above 80.

## Possible impact on the question

This source makes timing and exchange specificity decisive. A bullish view on SOL in general is insufficient unless SOL remains above 80 specifically into that noon ET minute on Binance.

## Reliability notes

High relevance because it states the operative rules directly. Moderate-high reliability overall for contract interpretation, though exchange-side verification is still needed for the actual price path and timing context.