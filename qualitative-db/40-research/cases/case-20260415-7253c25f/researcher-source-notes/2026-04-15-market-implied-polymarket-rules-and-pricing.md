---
type: source_note
case_key: case-20260415-7253c25f
dispatch_id: dispatch-case-20260415-7253c25f-20260415T220737Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-21
question: Will the price of Bitcoin be above $72,000 on April 21?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-7253c25f/researcher-analyses/2026-04-15/dispatch-case-20260415-7253c25f-20260415T220737Z/personas/market-implied.md]
tags: [polymarket, contract-rules, market-implied, binance]
---

# Summary

Polymarket shows the 72,000 line at about 80%-81% Yes and states the market resolves based on the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 21, using the final Close price and requiring it to be higher than 72,000.

## Key facts extracted

- The relevant threshold contract is the 72,000 line for April 21.
- Visible price on fetch was roughly 80% with buy-Yes around 81 cents.
- Resolution source is Binance BTC/USDT, not another exchange or pair.
- The relevant data point is the 1-minute candle for 12:00 in ET timezone on the specified date.
- The deciding field is the final Close price for that candle.
- The contract requires the Close to be higher than 72,000, not equal to it.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices..."
- The market ladder displayed 72,000 at about 80%-81% on Apr 15.

## What is uncertain

- The fetched web page is a secondary presentation layer, not the Binance settlement print itself.
- The web page does not itself prove what the April 21 noon ET candle will be; it only establishes pricing and rules.

## Why this source may matter

This is the governing contract surface for what conditions must hold, and it provides the market-implied probability that this persona is meant to interpret.

## Possible impact on the question

This source anchors both the baseline probability and the exact mechanics that all must hold for a Yes resolution: correct exchange, correct pair, correct minute, correct timezone, and close strictly above 72,000.

## Reliability notes

Useful as the governing market/rules surface, but not independent evidence about future BTC price. The pricing read is timely but can move quickly. The rules text is the most important part of the source for this case.