---
type: source_note
case_key: case-20260413-c5cf1f36
dispatch_id: dispatch-case-20260413-c5cf1f36-20260413T181345Z
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260413-c5cf1f36 | risk-manager
question: Will the Binance BTC/USDT 1m candle close at 12:00 PM ET on 2026-04-15 be above 66000?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket market page and rules
source_type: market rules / platform market state
source_url: https://polymarket.com/event/bitcoin-above-on-april-15
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-c5cf1f36/researcher-analyses/2026-04-13/dispatch-case-20260413-c5cf1f36-20260413T181345Z/personas/risk-manager.md]
tags: [polymarket, rules, resolution, market-state]
---

# Summary

The Polymarket market page provides the governing contract wording and current market-implied probability for the 66,000 threshold.

## Key facts extracted

- The contract resolves using the Binance BTC/USDT 1-minute candle for 12:00 in ET timezone on April 15.
- The market resolves Yes only if the final Close price is higher than 66,000.
- The source of truth is Binance BTC/USDT, not other exchanges or pairs.
- The page showed the 66,000 line trading around 99% Yes / 1.1% No at fetch time.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance... BTC/USDT... with '1m' and 'Candles' selected."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The page itself does not guarantee how Binance UI availability or API/UI discrepancies are handled if there is a transient platform issue at resolution time.
- The page is a live market surface and probability can move after capture.

## Why this source may matter

This is the direct contract-definition source and establishes the exact timing, instrument, and threshold logic that all have to hold for resolution.

## Possible impact on the question

It sharply narrows the risk question: not whether Bitcoin broadly stays strong, but whether Binance BTC/USDT specifically stays above 66,000 at one exact minute close, ET noon on April 15.

## Reliability notes

High relevance and high authority for contract wording and current market price. Less useful for independent contextual validation because it is the market itself, not an external data source.