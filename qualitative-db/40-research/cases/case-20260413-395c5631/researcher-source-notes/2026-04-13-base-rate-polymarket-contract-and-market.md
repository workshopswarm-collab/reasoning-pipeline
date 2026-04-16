---
type: source_note
case_key: case-20260413-395c5631
dispatch_id: dispatch-case-20260413-395c5631-20260413T221534Z
analysis_date: 2026-04-13
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-15
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close on 2026-04-15 be above 72000?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket event page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-15
source_date: 2026-04-13
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-395c5631/researcher-analyses/2026-04-13/dispatch-case-20260413-395c5631-20260413T221534Z/personas/base-rate.md]
tags: [polymarket, contract, resolution, source-note]
---

# Summary

This source established the market-implied probability and the exact contract mechanics that govern resolution.

## Key facts extracted

- Current market-implied probability for "Yes" at 72,000 was about 73% on fetch.
- The market resolves on the Binance BTC/USDT **1-minute candle** for **12:00 ET (noon) on April 15, 2026**.
- The relevant value is the candle's final **Close** price, not spot price at some other moment.
- The exchange/pair/source of truth is specifically Binance BTC/USDT, not other exchanges or USD pairs.
- Price precision follows the number of decimal places in the Binance source.

## Evidence directly stated by source

- The event page displayed the 72,000 line around 73%.
- The rules explicitly say resolution is based on the Binance BTC/USDT 12:00 ET 1-minute candle close.

## What is uncertain

- The webpage fetch is not an official API and may lag or round displayed probabilities.
- The page does not by itself show the future resolving candle; it only states the rules and current market pricing.

## Why this source may matter

This is the governing market source for both the market-implied baseline and the exact multi-condition contract interpretation.

## Possible impact on the question

It sharply narrows the event from a vague "Bitcoin above 72k on April 15" proposition to a precise one-minute, noon-ET, Binance BTC/USDT close condition. That makes timing and exchange-specific basis risk material.

## Reliability notes

Good for contract wording and displayed market baseline, but not sufficient alone for forecasting. It should be paired with independent price/context evidence.