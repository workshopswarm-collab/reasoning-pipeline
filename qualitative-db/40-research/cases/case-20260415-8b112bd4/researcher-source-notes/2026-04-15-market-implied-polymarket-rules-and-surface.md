---
type: source_note
case_key: case-20260415-8b112bd4
dispatch_id: dispatch-case-20260415-8b112bd4-20260415T153012Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-8b112bd4 | market-implied
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-16 be above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: medium-high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-8b112bd4/researcher-analyses/2026-04-15/dispatch-case-20260415-8b112bd4-20260415T153012Z/personas/market-implied.md]
tags: [polymarket, contract-rules, resolution-source, binance]
---

# Summary

The Polymarket market page states that this contract resolves from the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on 2026-04-16, using the candle's final Close price, and that the outcome is Yes only if that Close is higher than 70,000.

## Key facts extracted

- Market-implied probability for the 70,000 threshold was shown around 98.6%, consistent with the assignment's `current_price` of 0.985.
- Resolution source is Binance, specifically BTC/USDT with 1m candles.
- Resolution time is tied to 12:00 ET on Apr 16, 2026.
- The source uses the candle's final Close price, not an intraminute print, not another exchange, and not another pair.
- Price precision is whatever Binance shows in the source.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title."
- "The resolution source for this market is Binance... BTC/USDT... with \"1m\" and \"Candles\" selected."

## What is uncertain

- The webpage is not itself the final settlement artifact; it states the rules, but the actual settlement will depend on the Binance candle value visible at the relevant minute.
- The page does not independently confirm whether any Binance UI nuances could create ambiguity around the displayed 12:00 ET candle label, though the plain reading is straightforward.

## Why this source may matter

This is the governing contract/rules surface. It defines the relevant exchange, pair, timeframe, timestamp, and condition threshold. For a narrow-resolution crypto contract, those mechanics are material.

## Possible impact on the question

This source sharply narrows the question from general BTC directionality to a specific Binance BTC/USDT minute-close threshold at a specific ET time.

## Reliability notes

Good for contract interpretation and current market pricing. Moderate-high credibility as the platform's own rules page, but still distinct from the ultimate settlement datapoint, which is the Binance candle itself.