---
type: source_note
case_key: case-20260416-143465dc
dispatch_id: dispatch-case-20260416-143465dc-20260416T191321Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: prediction-markets
entity: sol
topic: will-solana-reach-90-april-13-19
question: Will Solana reach $90 April 13-19?
date_created: 2026-04-16
source_name: Polymarket market rules page for What price will Solana hit April 13-19?
source_type: market_rules
source_url: https://polymarket.com/event/what-price-will-solana-hit-april-13-19
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [sol, solana]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-143465dc/researcher-analyses/2026-04-16/dispatch-case-20260416-143465dc-20260416T191321Z/personas/base-rate.md]
tags: [market-rules, resolution-source, binance, touch-market]
---

# Summary

The governing resolution rule is explicit: this market resolves Yes if any Binance SOL/USDT 1-minute candle between 12:00 AM ET on April 13 and 11:59 PM ET on April 19 has a final High at or above $90. Other exchanges, pairs, or generic spot-price references do not count.

## Key facts extracted

- Resolution is based on Binance SOL/USDT only.
- The relevant field is the 1-minute candle High, not close, VWAP, or another aggregation.
- The observation window is the full title range from 12:00 AM ET on the first date through 11:59 PM ET on the last date.
- The market resolves immediately to Yes once any qualifying 1-minute High is at least $90.
- Prices from other exchanges, different pairs, or other spot references do not count.

## Evidence directly stated by source

- "This market will immediately resolve to \"Yes\" if any Binance 1-minute candle for SOL/USDT during the date range specified in the title ... has a final \"High\" price equal to or greater than the price specified in the title."
- "The resolution source for this market is Binance ... with the chart settings on \"1m\" candles selected."
- "Prices from other exchanges, different trading pairs, or spot markets will not be considered."

## What is uncertain

- The fetched page text states the rule, but the web extract does not itself provide historical qualifying candles; those must be checked separately.
- The exact operational ET-to-UTC boundary should be respected when checking Binance data.

## Why this source may matter

This is the primary source-of-truth for what counts. Because the case is explicitly exclusion-heavy and touch-based, contract mechanics materially determine the answer.

## Possible impact on the question

This source sharply narrows the evidence set. A near-touch on another exchange or a daily close near $90 is irrelevant unless Binance SOL/USDT prints a qualifying 1-minute High during the stated window.

## Reliability notes

Primary governing source. High reliability for contract interpretation, but not sufficient alone to answer whether the event occurred or is likely to occur.