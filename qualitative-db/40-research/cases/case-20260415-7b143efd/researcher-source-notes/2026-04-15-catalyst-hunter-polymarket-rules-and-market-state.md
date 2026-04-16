---
type: source_note
case_key: case-20260415-7b143efd
dispatch_id: dispatch-case-20260415-7b143efd-20260415T132144Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules for Bitcoin above ___ on April 20
source_type: market rules / market state
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-7b143efd/researcher-analyses/2026-04-15/dispatch-case-20260415-7b143efd-20260415T132144Z/personas/catalyst-hunter.md]
tags: [polymarket, contract-rules, market-implied-probability, resolution-source]
---

# Summary

This source establishes both the live market-implied probability for the 70,000 threshold and the contract mechanics that govern settlement.

## Key facts extracted

- The 70,000 outcome was trading around 86% on 2026-04-15.
- The market resolves using the Binance BTC/USDT 1-minute candle for 12:00 ET on April 20, 2026.
- The relevant value is the final candle close, not intraminute high, low, or another exchange.
- Price precision is determined by Binance source precision.

## Evidence directly stated by source

- Market rule: resolves Yes if the Binance 1-minute candle for BTC/USDT at 12:00 ET on the stated date has a final close above the threshold.
- Resolution source: Binance BTC/USDT with 1m candles selected.
- Current market state for the relevant threshold: 70,000 trading near 86%.

## What is uncertain

- The public page is not itself the final settlement print; actual resolution depends on the future Binance candle.
- The page does not specify any fallback if Binance UI/API availability changes.

## Why this source may matter

It is the governing contract surface for what counts, what timestamp matters, and which venue matters. That sharply limits the relevant catalyst set: only developments that can affect Binance BTC/USDT into noon ET on April 20 are material.

## Possible impact on the question

This source makes the market highly path-sensitive and rules out looser interpretations such as weekend average price, other exchanges, or intraday highs above 70,000.

## Reliability notes

Useful and necessary as the contract surface, but not independently authoritative on the eventual result; the authoritative settlement datapoint should come from Binance at resolution.