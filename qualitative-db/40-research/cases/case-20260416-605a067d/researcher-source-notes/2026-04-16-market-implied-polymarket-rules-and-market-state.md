---
type: source_note
case_key: case-20260416-605a067d
dispatch_id: dispatch-case-20260416-605a067d-20260416T142910Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: threshold-close-markets
entity: ethereum
topic: Polymarket ETH above 2200 on April 17 contract terms and displayed market pricing
question: Will the Binance ETH/USDT 12:00 ET 1-minute candle close on April 17 be above 2200?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket event page for Ethereum above on April 17
source_type: market page / contract rules
source_url: https://polymarket.com/event/ethereum-above-on-april-17
source_date: 2026-04-16
credibility: high for displayed contract text and listed market prices
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [ethereum]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-605a067d/researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/personas/market-implied.md
tags: [polymarket, contract-rules, market-pricing, source-note]
---

# Summary

This source establishes the governing contract wording and the displayed market state for the April 17 ETH threshold ladder. For the 2200 line, the page showed roughly 91%-91.5% Yes at the time of capture.

## Key facts extracted

- The 2200 outcome on the Polymarket page was displayed around 91%-91.5% Yes.
- The market resolves Yes only if the Binance ETH/USDT 12:00 ET one-minute candle on April 17 has a final Close above 2200.
- The source of truth is Binance ETH/USDT with 1m candles selected, not other exchanges or pairs.
- Precision is governed by the source’s displayed decimal precision.
- The page also showed nearby ladder pricing: 2100 around 99%, 2300 around 55%-57%, 2400 around 12%.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for ETH/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the ETH/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/ETH_USDT with \"1m\" and \"Candles\" selected on the top bar."
- "Please note that this market is about the price according to Binance ETH/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The page is a live market surface, so displayed prices can move after capture.
- The page does not itself prove the future April 17 noon close; it only defines the rule and crowd pricing.
- The ladder format can tempt over-reading cross-strike consistency without full order-book depth.

## Why this source may matter

It is the primary contract-definition source for what conditions must hold. It also provides the market-implied prior that this persona is meant to decode rather than ignore.

## Possible impact on the question

This source anchors both the mechanism and the baseline probability. It supports the view that the market is pricing ETH 2200 as already comfortably in-the-money one day ahead, but does not by itself justify matching that confidence without checking Binance directly.

## Reliability notes

High reliability for rule text and listed prices on the event page. Medium reliability for inference beyond that, since the page is not the governing settlement database itself and prices reflect trader beliefs rather than proof of outcome.