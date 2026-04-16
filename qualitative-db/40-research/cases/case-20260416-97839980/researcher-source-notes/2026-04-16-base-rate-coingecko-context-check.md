---
type: source_note
case_key: case-20260416-97839980
dispatch_id: dispatch-case-20260416-97839980-20260416T040518Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: spot-price
entity: sol
topic: case-20260416-97839980 | base-rate
question: Will the price of Solana be above $80 on April 19?
driver: reliability
date_created: 2026-04-16
source_name: CoinGecko simple price API
source_type: secondary_contextual_market_source
source_url: https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd
source_date: 2026-04-16
credibility: medium_high
recency: high
stance: neutral
certainty: medium_high
importance: medium
novelty: low
agent: Orchestrator
related_entities: [sol]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-97839980/researcher-analyses/2026-04-16/dispatch-case-20260416-97839980-20260416T040518Z/personas/base-rate.md]
tags: [coingecko, context, cross-check, spot-price]
---

# Summary

Used CoinGecko simple price API as an independent contextual cross-check on SOL spot level. It returned $85.21, close to Binance's $85.32 snapshot, suggesting no obvious exchange-specific distortion at research time.

## Key facts extracted

- CoinGecko simple price API returned `{"solana":{"usd":85.21}}`.
- This was within roughly $0.11 of the Binance spot snapshot collected during the same run.

## Evidence directly stated by source

- CoinGecko reports current USD price for Solana near $85.21.

## What is uncertain

- CoinGecko is an aggregator, not the contract settlement source.
- The exact exchange mix behind the aggregate price is not the same as Binance SOL/USDT.
- This source does not speak to the April 19 noon ET close directly.

## Why this source may matter

It provides an independent contextual verification pass, useful because the market is priced at an extreme 92% and the assignment explicitly requires extra verification.

## Possible impact on the question

The close agreement with Binance reduces concern that the current >$80 reading is a Binance-only artifact. It modestly supports the view that Yes is favored, but only as contextual evidence.

## Reliability notes

- Reasonably reliable as a secondary price cross-check.
- Not authoritative for settlement.
- Valuable mainly for independence and anomaly detection, not for final resolution.
