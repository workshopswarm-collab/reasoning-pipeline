---
type: source_note
case_key: case-20260414-4e668883
dispatch_id: dispatch-case-20260414-4e668883-20260414T133938Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: protocols
entity: ethereum
topic: case-20260414-4e668883 | risk-manager
question: Will Ethereum reach $2,400 April 13-19?
driver:
date_created: 2026-04-14
source_name: CoinGecko 7-day ETH/USD market chart and Binance ETHUSDT hourly candles
source_type: market-data-context
source_url: https://api.coingecko.com/api/v3/coins/ethereum/market_chart?vs_currency=usd&days=7
source_date: 2026-04-14
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: medium
agent: risk-manager
related_entities: [ethereum]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-4e668883/researcher-analyses/2026-04-14/dispatch-case-20260414-4e668883-20260414T133938Z/personas/risk-manager.md]
tags: [source-note, coingecko, binance, verification, price-path]
---

# Summary

Independent price checks did not show ETH at or above $2,400 yet. CoinGecko 7-day data showed a max around 2392.57, and a Binance hourly sample showed a max high around 2396.03.

## Key facts extracted

- CoinGecko 7-day market chart query returned:
  - latest: 2392.5652
  - max_7d: 2392.5652
  - min_7d: 2071.4092
  - crossed_2400: false
- Binance ETHUSDT hourly sample returned:
  - latest_close: 2391.83
  - max_high_sample: 2396.03
  - crossed_2400: false

## Evidence directly stated by source

- Both independent market-data sources place ETH just below the target level rather than already through it.
- The gap to target is small in absolute terms, roughly single-digit dollars.

## What is uncertain

- Neither source by itself proves what exact source the Polymarket market will use for settlement.
- Binance sample covered 200 hourly candles rather than an authoritative full-week settlement dataset.
- A brief intraperiod wick above $2,400 could still occur after this snapshot.

## Why this source may matter

This is the main disconfirming/contextual evidence against the market's very high confidence. It shows the contract is not already effectively settled and that modest short-term reversal or failure to wick through the level remains possible.

## Possible impact on the question

The evidence does not make a $2,400 touch unlikely, but it does support shaving probability below the market's 92.35% because the target still has to be reached within a narrow time window and has not yet been printed in the checked sources.

## Reliability notes

Good recency and useful cross-check independence across aggregating source classes, but still contextual rather than governing. Settlement-source ambiguity remains low-to-moderate until the exact Polymarket rule source is fully verified.