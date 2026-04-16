---
type: source_note
case_key: case-20260416-c395460f
dispatch_id: dispatch-case-20260416-c395460f-20260416T022702Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: tokens
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 12:00 ET 1-minute candle close above 80 on April 19, 2026?
driver: reliability
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market_contract_page
source_url: https://polymarket.com/event/solana-above-on-april-19
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: base-rate
related_entities: [sol]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-c395460f/researcher-analyses/2026-04-16/dispatch-case-20260416-c395460f-20260416T022702Z/personas/base-rate.md]
tags: [source-note, polymarket, contract, resolution]
---

# Summary

This source note captures the market-implied baseline and the contract mechanics that define what must happen for Yes to resolve.

## Key facts extracted

- The selected market threshold is 80.
- The market-implied probability at research time is about 89% for "above 80" on April 19.
- The market resolves Yes only if the Binance SOL/USDT 1-minute candle for 12:00 ET on April 19 has a final close strictly higher than 80.
- If the close is exactly 80.0 or below, the market resolves No.
- The contract explicitly names Binance SOL/USDT rather than another exchange or another pair.
- Price precision is governed by the source's decimal precision.

## Evidence directly stated by source

- The governing source of truth is Binance.
- The relevant timestamp is noon ET on April 19, 2026.
- The condition is multi-part: correct exchange, correct pair, correct one-minute candle, correct timestamp/timezone, and a strict-greater-than threshold.

## What is uncertain

- The market page is not the settlement source itself; it describes how settlement will be determined.
- The fetched page is a web rendering and should be cross-checked against the assignment prompt language for exactness.

## Why this source may matter

This source defines the contract interpretation. For a narrow, date-sensitive market, resolution mechanics are as important as directional price intuition.

## Possible impact on the question

This source raises verification needs. A strong directional view from current spot still has to survive contract details: the exact noon ET minute on Binance must close above 80, not merely trade above 80 sometime that day.

## Reliability notes

- High credibility for market pricing and listed rules.
- Not independent from the market itself; it tells us what traders currently believe and how the market says it will resolve, but not whether the price outcome will occur.