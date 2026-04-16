---
type: source_note
case_key: case-20260413-395c5631
dispatch_id: dispatch-case-20260413-395c5631-20260413T221534Z
analysis_date: 2026-04-13
persona: market-implied
domain: crypto
subdomain: prediction-markets
entity: btc
topic: bitcoin-above-72k-on-april-15
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-15 be above 72000?
driver: reliability
date_created: 2026-04-13
source_name: Polymarket event page and outcome ladder
source_type: market_contract_page
source_url: https://polymarket.com/event/bitcoin-above-on-april-15
source_date: 2026-04-13
credibility: medium_high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, market-implied, contract, ladder]
---

# Summary

The Polymarket event page shows the 72,000 line trading around 73%, with adjacent strikes at 70,000 around 94% and 74,000 around 36%. That ladder is internally coherent with BTC spot trading in the low-to-mid 73k area and suggests the market is pricing a meaningful but not dominant chance of a downside move through 72k by noon ET on Apr. 15.

## Key facts extracted

- The 72,000 outcome was displayed around 73% on the event page during this run.
- Adjacent ladder prices were approximately 70,000 at 94% and 74,000 at 36%.
- The page explicitly states resolution uses the Binance BTC/USDT 1-minute candle at 12:00 ET on the specified date.
- Event volume displayed around $408k total, with the 72k band showing nontrivial line-specific volume.

## Evidence directly stated by source

- Market-implied probability for the target threshold is about 0.725.
- The market is not pricing 72k as nearly certain despite spot already being above the threshold; traders are preserving substantial room for a reversal.
- Cross-strike pricing is monotonic and looks broadly sensible, reducing concern that the 72k contract is an obvious stale misprice in isolation.

## What is uncertain

- The fetched page is a webpage representation, not a signed market-data API response.
- The page does not by itself explain why traders hold a 27% No probability; that requires interpretation.
- The displayed volumes are useful context but do not prove market depth at every price level.

## Why this source may matter

This is the clearest source for the market-implied prior, and the neighboring strikes help decode what the market collectively assumes about short-term BTC volatility around the resolution time.

## Possible impact on the question

Supports taking the market seriously: the price appears consistent with current spot and a plausible 1.5-day volatility distribution rather than obviously overreactive or stale.

## Reliability notes

Good for market-implied odds and contract wording, but not a primary exchange feed. Should be paired with Binance data or a strong contextual crypto price source for a fuller assessment.