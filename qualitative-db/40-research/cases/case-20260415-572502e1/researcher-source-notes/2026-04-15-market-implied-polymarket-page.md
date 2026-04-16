---
type: source_note
case_key: case-20260415-572502e1
dispatch_id: dispatch-case-20260415-572502e1-20260415T124520Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: polymarket-contract-page-and-cross-threshold-context
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: reliability
date_created: 2026-04-15
source_name: Polymarket event page for April 16 Bitcoin threshold ladder
source_type: market_contract_page
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: medium_high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, threshold-ladder, market-implied]
---

# Summary

The Polymarket event page provides the current market-implied probability and useful adjacent-threshold context for whether 72k looks efficiently priced relative to nearby strikes.

## Key facts extracted

- The assigned current_price is 0.895, implying an 89.5% Yes probability for BTC above 72,000 at the relevant noon ET minute close on 2026-04-16.
- The page also shows adjacent threshold pricing around the same time: above 70k about 98%, above 74k about 57%, above 76k about 18%.
- The rules section states the market resolves from the Binance BTC/USDT 1-minute candle for 12:00 in ET timezone and uses the final Close value.

## Evidence directly stated by source

- The crowd is pricing 72k as well above the center of likely outcomes but not remotely certain.
- The neighboring strikes create an internal distribution: 72k is strongly favored, 74k is roughly coin-flip, and 76k is clearly minority.

## What is uncertain

- The fetched page is a rendered web page and may lag ultra-recent order-book changes.
- The page duplicates some sections in extraction output and should not be treated as a clean API feed.

## Why this source may matter

It is the direct market-implied baseline and also helps test whether the 72k line is coherently embedded within a broader probability ladder instead of being an isolated mispricing.

## Possible impact on the question

The surrounding thresholds make 89.5% for 72k look directionally coherent with a spot price in the mid-74k range: the market appears to be pricing a decent chance of being below 74k by noon tomorrow, but still a smaller chance of falling all the way below 72k.

## Reliability notes

Useful and directly relevant for the market prior and contract wording, but less authoritative than Binance for the underlying settlement data. Evidence independence versus Binance is low-to-medium because Polymarket traders are ultimately pricing the same underlying BTC state.
