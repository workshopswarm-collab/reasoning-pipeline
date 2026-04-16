---
type: source_note
case_key: case-20260414-4e668883
dispatch_id: dispatch-case-20260414-4e668883-20260414T133938Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: protocols
entity: ethereum
topic: case-20260414-4e668883 | base-rate
question: Will Ethereum reach $2,400 April 13-19?
date_created: 2026-04-14
source_name: Cross-exchange ETH spot cross-check
source_type: secondary_market_context
source_url: https://api.coinbase.com/v2/prices/ETH-USD/spot
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: medium
novelty: low
agent: Orchestrator
related_entities: [ethereum]
related_drivers: []
upstream_inputs: []
downstream_uses: [base-rate-finding]
tags: [coinbase, coingecko, binance, ethereum, spot-price]
---

# Summary

A cross-check across Coinbase, CoinGecko, and Binance during the run showed ETH spot clustered around $2,386-$2,389, i.e. very close to but still below $2,400.

## Key facts extracted

- Coinbase spot API returned ETH-USD at 2388.945.
- CoinGecko simple price returned ethereum at 2386.89 USD.
- Binance ticker returned ETHUSDT at 2386.80.
- These values are tightly clustered, suggesting the market was trading within roughly 0.5% of the threshold during the verification pass.

## Evidence directly stated by source

- Each source directly states a current spot price snapshot.

## What is uncertain

- These are spot snapshots, not the governing settlement source.
- Spot snapshots alone do not tell us whether Binance will print a 1-minute High above 2400 later in the week.

## Why this source may matter

It provides an independent contextual check that ETH is already near the threshold, making a touch plausible without requiring a large move.

## Possible impact on the question

This contextual evidence pushes the probability upward relative to a generic weekly threshold-touch prior, because the threshold is only about $11-$13 above checked spot during the run.

## Reliability notes

Reliability is high for contemporaneous market context because the sources are standard pricing providers and mutually consistent. Independence is only medium because all reflect the same underlying market state.
