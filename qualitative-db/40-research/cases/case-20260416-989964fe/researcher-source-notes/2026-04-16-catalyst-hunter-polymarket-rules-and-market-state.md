---
type: source_note
case_key: case-20260416-989964fe
dispatch_id: dispatch-case-20260416-989964fe-20260416T020418Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: market-structure
entity: ethereum
topic: ETH above 2200 on April 17 resolution mechanics
question: Will the Binance ETH/USDT 12:00 ET one-minute candle on April 17 close above 2200?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket event page and rules
source_type: market rules / resolution criteria
source_url: https://polymarket.com/event/ethereum-above-on-april-17
source_date: 2026-04-16
credibility: medium-high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [ethereum]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-989964fe/researcher-analyses/2026-04-16/dispatch-case-20260416-989964fe-20260416T020418Z/personas/catalyst-hunter.md]
tags: [polymarket, resolution-rules, binance, ethusdt, date-sensitive]
---

# Summary

This source defines the governing market mechanics. The market resolves Yes only if Binance's ETH/USDT 1-minute candle labeled 12:00 in ET on April 17 has a final Close price strictly greater than 2200.

## Key facts extracted

- The source of truth is Binance, not an average across exchanges.
- The relevant instrument is ETH/USDT.
- The relevant timeframe is the 1-minute candle for 12:00 ET on April 17, 2026.
- The relevant field is the candle Close, not high/low/mark/index price.
- The threshold condition is strictly higher than 2200.
- Price precision is whatever Binance displays for that source.
- Current market pricing on the page showed the 2200 line around 95% Yes at fetch time.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for ETH/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the ETH/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/ETH_USDT with \"1m\" and \"Candles\" selected on the top bar."
- "Please note that this market is about the price according to Binance ETH/USDT, not according to other exchanges or trading pairs."
- "Price precision is determined by the number of decimal places in the source."

## What is uncertain

- The web fetch does not expose the live embedded chart itself, only the rules text and displayed market pricing.
- The page does not independently prove what the future Apr 17 12:00 ET candle will be; it only defines how resolution will be judged.

## Why this source may matter

This is the governing contract source, so it determines what exact timing and price field matter. For a date-sensitive market with extreme pricing, misunderstanding the candle timestamp or field would be a major error.

## Possible impact on the question

It narrows the question to a single one-minute spot close on Binance at noon ET rather than a broader daily ETH direction call. That makes intraday timing and exchange-specific microstructure more relevant than general ETH bullishness alone.

## Reliability notes

High relevance because it is the contract/rules page itself. Reliability for market-state snapshot is medium-high because the page can move quickly, but reliability for resolution mechanics is high.