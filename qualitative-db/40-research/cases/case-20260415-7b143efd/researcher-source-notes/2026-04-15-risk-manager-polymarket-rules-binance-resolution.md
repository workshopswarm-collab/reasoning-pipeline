---
type: source_note
case_key: case-20260415-7b143efd
dispatch_id: dispatch-case-20260415-7b143efd-20260415T132144Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: markets
entity: btc
topic: case-20260415-7b143efd | risk-manager
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules page for Bitcoin above ___ on April 20
source_type: market contract / resolution rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: medium-high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-7b143efd/researcher-analyses/2026-04-15/dispatch-case-20260415-7b143efd-20260415T132144Z/personas/risk-manager.md]
tags: [polymarket, contract-rules, binance, resolution]
---

# Summary

This source establishes the contract mechanics. The market resolves Yes only if the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 20 has a final close strictly above 70,000. It also makes clear that Binance BTC/USDT is the governing source rather than any broader spot composite or other exchange.

## Key facts extracted

- Resolution depends on the Binance BTC/USDT 1-minute candle for 12:00 ET on April 20, 2026.
- The relevant field is the candle's final `Close` price.
- The threshold test is strictly `higher than` 70,000, not equal to 70,000.
- The source of truth is Binance's BTC/USDT candles, not other exchanges or pairs.
- Precision is determined by the source display / source decimals.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices..."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The Polymarket page itself does not specify whether Binance UI display or API retrieval is the fallback if the website presentation differs, though the source family is clear.
- The page does not independently explain ET/EDT conversion mechanics; that has to be inferred from the market wording and checked against Binance time handling.

## Why this source may matter

This is the governing contract text. For a narrow date-and-time market, rule interpretation and source-of-truth handling are as important as directional BTC price opinion.

## Possible impact on the question

This source limits the relevant forecast to one exact timestamped Binance minute close. That compresses the thesis into timing risk: BTC can trade above 70k before and after noon ET and still resolve No if the exact Binance close for that one minute is below the threshold.

## Reliability notes

High relevance because it is the market's own rule surface. Moderate rather than perfect credibility only because it is a platform market page rather than an exchange documentation source, and because the page text alone does not resolve every implementation edge case.