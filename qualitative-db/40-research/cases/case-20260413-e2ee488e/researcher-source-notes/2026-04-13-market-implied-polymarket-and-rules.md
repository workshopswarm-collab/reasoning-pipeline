---
type: source_note
case_key: case-20260413-e2ee488e
dispatch_id: dispatch-case-20260413-e2ee488e-20260413T222544Z
analysis_date: 2026-04-13
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-15
question: Will the price of Bitcoin be above $70,000 on April 15?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket event page and stated resolution rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-15
source_date: 2026-04-13
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
downstream_uses: [qualitative-db/40-research/cases/case-20260413-e2ee488e/researcher-analyses/2026-04-13/dispatch-case-20260413-e2ee488e-20260413T222544Z/personas/market-implied.md]
tags: [polymarket, contract-rules, binance, market-implied]
---

# Summary

The Polymarket market page showed the 70,000 line trading around 94.5% on 2026-04-13, matching the assignment's `current_price: 0.945`, and stated the exact contract mechanics.

## Key facts extracted

- The relevant contract is the Apr 15 noon ET BTC threshold market at 70,000.
- The market page displayed the 70,000 outcome near 94% / 94.5%.
- Resolution is based on the Binance BTC/USDT 1-minute candle for 12:00 in ET timezone on Apr 15.
- The contract resolves `Yes` only if the final candle close is strictly higher than 70,000.
- The page explicitly says this is Binance BTC/USDT, not other exchanges or pairs.
- Price precision is determined by Binance source decimals.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance... BTC/USDT... with \"1m\" and \"Candles\" selected..."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The scraped web page is not itself the ultimate resolution source; it is the contract/rules surface describing that Binance is the governing source of truth.
- The event page does not itself give the future settlement value; it only defines the rule and shows current market pricing.

## Why this source may matter

It defines both the market-implied baseline and the exact contract mechanics. Because this is a narrow, date-specific market, the distinction between Binance BTC/USDT, the 12:00 ET one-minute candle, and the strict `>` threshold is material.

## Possible impact on the question

This source strongly supports the view that the main analytical problem is not general BTC direction but whether BTC/USDT on Binance stays above 70,000 specifically at noon ET on Apr 15. It also makes exchange-specific operational or timing issues potentially relevant at the margin.

## Reliability notes

Useful and necessary as the contract/rules surface, but not sufficient alone for settlement because the actual resolving value comes from Binance. Reliability for contract interpretation is medium-to-high; independence is low because it is the market's own page summarizing its own rules.