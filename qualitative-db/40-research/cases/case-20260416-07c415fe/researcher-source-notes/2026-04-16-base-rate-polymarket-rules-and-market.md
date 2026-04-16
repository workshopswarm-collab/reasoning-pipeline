---
type: source_note
case_key: case-20260416-07c415fe
dispatch_id: dispatch-case-20260416-07c415fe-20260416T031541Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: market-structure
entity: sol
topic: solana-above-80-on-april-19
question: Will the price of Solana be above $80 on April 19?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket event page and rules
source_type: market rules / market pricing
source_url: https://polymarket.com/event/solana-above-on-april-19
source_date: 2026-04-16
credibility: medium-high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [sol]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, rules, market-implied-probability, resolution]
---

# Summary

The Polymarket event page provides both the current market-implied probability for the "$80" threshold and the operative contract wording. For this case, it showed the "$80" outcome trading at roughly 89% Yes at fetch time, while the rules specify that resolution depends on the Binance SOL/USDT 1-minute candle labeled 12:00 ET on April 19, 2026 and specifically its final Close price.

## Key facts extracted

- The relevant threshold market is "$80" for April 19, 2026.
- The event page showed the "$80" line at roughly 89% Yes at fetch time.
- Resolution is based on the Binance SOL/USDT 1-minute candle for 12:00 ET (noon) on the specified date.
- The market resolves Yes only if the final Close price is higher than 80; otherwise No.
- The rules explicitly say the source is Binance SOL/USDT, not other exchanges or other trading pairs.
- Price precision is determined by the source decimals.

## Evidence directly stated by source

- Exact governing source of truth: Binance SOL/USDT candle interface.
- Exact timing reference: 12:00 in ET timezone on April 19, 2026.
- Exact condition: final 1-minute candle Close must be strictly greater than 80.

## What is uncertain

- The public page is not itself the settlement record; it points to Binance as source of truth.
- The fetched page is a rendered web surface and could lag transiently versus exchange data.

## Why this source may matter

This is the governing contract surface and the source for the market-implied baseline. It defines the exact condition set that must all hold for a Yes resolution and prevents substitution of other spot references.

## Possible impact on the question

This source sharply lowers source-of-truth ambiguity: the relevant question is not whether SOL is generally "around" or "over" 80 on April 19, but whether Binance's SOL/USDT 12:00 ET 1-minute candle closes strictly above 80.

## Reliability notes

High relevance and high authority for contract interpretation; medium-high reliability for live pricing snapshots because the page is a market UI rather than the underlying exchange settlement source itself.