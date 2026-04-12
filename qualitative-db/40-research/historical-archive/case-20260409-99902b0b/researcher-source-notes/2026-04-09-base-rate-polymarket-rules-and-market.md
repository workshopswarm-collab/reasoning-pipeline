---
type: source_note
case_key: case-20260409-99902b0b
dispatch_id: dispatch-case-20260409-99902b0b-20260409T203957Z
analysis_date: 2026-04-09
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260409-99902b0b | base-rate
question: Will the price of Bitcoin be above $70,000 on April 10?
driver: operational-risk
date_created: 2026-04-09
source_name: Polymarket market page and rules for Bitcoin above ___ on April 10
source_type: market rules / platform page
source_url: https://polymarket.com/event/bitcoin-above-on-april-10
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-99902b0b/researcher-analyses/2026-04-09/dispatch-case-20260409-99902b0b-20260409T203957Z/personas/base-rate.md]
tags: [polymarket, market-rules, resolution-source, btc]
---

# Summary

This source defines the contract mechanics and provides the current market baseline used for comparison.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 10 has a final close above 70,000.
- The resolution source is Binance BTC/USDT with 1m candles selected.
- The contract is exchange-specific and pair-specific; other exchanges or BTC/USD references do not govern.
- The market page showed the 70,000 line trading around 95% at fetch time.

## Evidence directly stated by source

- Resolution depends on a single Binance 1-minute candle close at noon ET on the specified date.
- Price precision is determined by Binance source decimals.
- The relevant condition is strictly greater than 70,000, not greater than or equal.

## What is uncertain

- The web fetch is not an authenticated exchange view and cannot itself verify the final candle mechanics beyond quoted rules text.
- The market page reflects a live price snapshot that may move before final settlement.

## Why this source may matter

It is the governing source for contract wording and the best direct read on the market-implied probability baseline.

## Possible impact on the question

This source makes the timing, venue, and threshold-specific resolution mechanics explicit. It also shows the market is pricing the event as highly likely, so any non-consensus estimate would need strong evidence.

## Reliability notes

High relevance and high credibility for rules interpretation because it is the platform hosting the market. It is not sufficient by itself to prove likely resolution because it is not the actual Binance candle data source.