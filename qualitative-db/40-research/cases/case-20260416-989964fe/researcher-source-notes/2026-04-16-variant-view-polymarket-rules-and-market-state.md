---
type: source_note
case_key: case-20260416-989964fe
dispatch_id: dispatch-case-20260416-989964fe-20260416T020418Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: prediction-markets
entity: binanaliases: [Binance Exchange]ge]
topic: eth-above-2200-april-17-resolution-and-market-state
question: Will the Binance ETH/USDT 12:00 ET 1-minute candle close above 2200 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page and market rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/ethereum-above-on-april-17
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: variant-view
related_entities: []
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-989964fe/researcher-analyses/2026-04-16/dispatch-case-20260416-989964fe-20260416T020418Z/personas/variant-view.md]
tags: [polymarket, contract-rules, resolution-source, market-implied-probability]
---

# Summary

The Polymarket event page provides both the current market-implied probability for the 2200 line and the contract wording needed to interpret what actually counts at resolution.

## Key facts extracted

- The 2200 outcome was trading around 95% Yes at fetch time, matching the assignment's `current_price: 0.955` baseline.
- The event resolves based on the Binance ETH/USDT 1-minute candle for **12:00 ET** on April 17.
- The relevant field is the candle's final **Close** price, not intraminute highs, lows, or prices from other venues.
- The page explicitly says price precision is determined by the number of decimals shown in the Binance source.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for ETH/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the ETH/USDT \"Close\" prices ... with \"1m\" and \"Candles\" selected on the top bar."
- The market board listed 2200 at roughly 95%.

## What is uncertain

- The event page is a derivative surface quoting both market state and rules; it is not itself the final exchange print.
- The visible website is sufficient for contract interpretation, but not for proving the actual April 17 noon close in advance.

## Why this source may matter

This is the governing contract surface for what counts. In a date-specific crypto market, source-of-truth mechanics and timezone interpretation are central to whether an otherwise obvious directional thesis is actually applicable.

## Possible impact on the question

It sharply narrows the question from "Will ETH stay above 2200 broadly?" to "Will Binance ETH/USDT print a final 12:00 ET 1-minute close above 2200?" That reduces some ambiguity but introduces operational and timestamp-specific tail risk.

## Reliability notes

Reliable for contract wording and contemporaneous market state, but only medium as a primary source because the actual settle print still depends on Binance at the exact resolution minute.