---
type: source_note
case_key: case-20260416-143465dc
dispatch_id: dispatch-case-20260416-143465dc-20260416T191321Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: markets
entity: sol
topic: solana-touch-90-april-13-19
question: Will Solana reach $90 April 13-19?
date_created: 2026-04-16
source_name: Polymarket market page / resolution text
source_type: market_contract
source_url: https://polymarket.com/event/what-price-will-solana-hit-april-13-19
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [sol]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-143465dc/researcher-analyses/2026-04-16/dispatch-case-20260416-143465dc-20260416T191321Z/personas/risk-manager.md]
tags: [source-note, polymarket, contract, binance, resolution]
---

# Summary

This source establishes the governing source of truth and the key resolution mechanics for the market. It is the most important source for avoiding contract-interpretation error.

## Key facts extracted

- The market resolves Yes if **any Binance 1-minute candle for SOL/USDT** during the specified date range has a final **High** price **equal to or greater than $90**.
- The relevant date range is from **12:00 AM ET on April 13** through **11:59 PM ET on April 19**.
- The resolution source is Binance, specifically the **SOL/USDT** chart with **1m candles** selected.
- Prices from other exchanges or other trading pairs do **not** count.

## Evidence directly stated by source

- "This market will immediately resolve to \"Yes\" if any Binance 1-minute candle for SOL/USDT during the date range specified in the title ... has a final \"High\" price equal to or greater than the price specified in the title."
- "The resolution source for this market is Binance... with the chart settings on \"1m\" candles selected on the top bar."
- "Prices from other exchanges, different trading pairs, or spot markets will not be considered."

## What is uncertain

- The market page does not itself display a durable historical proof artifact for whether a qualifying 1-minute high has already printed; that must be checked separately.
- The phrase "spot markets" appears in the fetched text even though SOL/USDT on Binance is itself a spot pair; the operational intent is still clear enough that the Binance SOL/USDT 1m high is the governing metric.

## Why this source may matter

This market is rule-sensitive and exclusion-heavy. The central risk is not directional crypto analysis alone, but using the wrong source of truth or the wrong definition of "reach." A touch on another venue, another pair, or a coarser candle would not settle the market.

## Possible impact on the question

It sharply narrows the question from "can SOL broadly trade near $90 this week?" to "will Binance SOL/USDT print at least one 1-minute high of 90.00+ before April 19 11:59 PM ET?"

## Reliability notes

High reliability for contract wording and settlement logic because this is the market operator's own resolution text. It is not sufficient by itself to answer whether the threshold has already been hit; independent price verification is still required.