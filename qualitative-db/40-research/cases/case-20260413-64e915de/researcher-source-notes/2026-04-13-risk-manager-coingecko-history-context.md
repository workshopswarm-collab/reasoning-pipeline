---
type: source_note
case_key: case-20260413-64e915de
dispatch_id: dispatch-case-20260413-64e915de-20260413T234340Z
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: protocols
entity: ethereum
topic: case-20260413-64e915de | risk-manager
question: Will Ethereum reach $2,400 April 13-19?
date_created: 2026-04-13
source_name: CoinGecko Ethereum historical daily snapshot
source_type: market-data-aggregator
source_url: https://api.coingecko.com/api/v3/coins/ethereum/history?date=13-04-2026
source_date: 2026-04-13
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: medium
novelty: low
agent: orchestrator
related_entities: [ethereum]
related_drivers: []
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260413-64e915de/researcher-analyses/2026-04-13/dispatch-case-20260413-64e915de-20260413T234340Z/personas/risk-manager.md
tags: [source-note, coingecko, price-context, verification]
---

# Summary
This source provided an additional independent verification pass on Ethereum's broad USD price context outside Binance.

## Key facts extracted
- CoinGecko historical endpoint for 2026-04-13 returned Ethereum market_data.current_price.usd of about 2192.16 for that date snapshot.
- The figure is lower than the later Binance same-day context because CoinGecko historical snapshots are date-based and not a live intraday maximum feed.
- The source still confirms ETH was trading in the low-2200s on the relevant date, meaning the market is asking for a roughly 9% move from the day-level historical snapshot rather than a multi-standard-deviation jump from far below.

## Evidence directly stated by source
- Ethereum existed in the low-2200s USD area on the relevant calendar date.

## What is uncertain
- CoinGecko historical date snapshots are not the contract resolution source and are not optimized for exact intraday high detection.
- This source cannot confirm whether Binance 1-minute highs touched 2400.

## Why this source may matter
It supplies a second, meaningfully independent source class: a market-data aggregator rather than the named exchange. That helps check whether the market is anchored to a broadly plausible ETH price regime rather than an exchange-specific anomaly.

## Possible impact on the question
This source supports the high-probability Yes view only contextually. It weakly argues that 2400 is near enough to current conditions to be reachable within the weekly window, but it is not decisive.

## Reliability notes
- Reasonably reliable for broad daily price context.
- Not authoritative for settlement and lower precision than Binance for this exact contract.
- Useful as extra verification because the assignment required an additional pass on an extreme market probability.
