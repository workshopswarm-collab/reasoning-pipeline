---
type: source_note
case_key: case-20260416-cc34f737
dispatch_id: dispatch-case-20260416-cc34f737-20260416T162722Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: market-context
entity: ethereum
topic: Ethereum spot context and short-horizon price path
question: What contextual evidence matters for ETH being above 2300 at noon ET on 2026-04-17?
driver: reliability
date_created: 2026-04-16
source_name: CoinGecko Ethereum spot and market-chart API
source_type: secondary
source_url: https://api.coingecko.com/api/v3/coins/ethereum
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: Orchestrator
related_entities: [ethereum]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-cc34f737/researcher-analyses/2026-04-16/dispatch-case-20260416-cc34f737-20260416T162722Z/personas/catalyst-hunter.md]
tags: [ethereum, coingecko, context, spot]
---

# Summary

CoinGecko provides a useful independent contextual check that broader ETH spot pricing is also around 2334 on 2026-04-16, with approximately -0.37% 24-hour change and an hourly path over the last two days mostly ranging above 2300, including prints in the mid-2300s and a recent local high around 2376.

## Key facts extracted

- CoinGecko current ETH/USD price was approximately 2334.39 at research time.
- 24-hour percentage change was about -0.367%.
- Hourly path over the prior two days included values around 2312-2376, with most recent observed regime staying above 2300.
- Market cap rank remained #2, indicating a highly liquid benchmark asset rather than an illiquid tail token.

## Evidence directly stated by source

- CoinGecko directly states current ETH/USD price and 24-hour change.
- CoinGecko hourly market chart directly states recent spot path.

## What is uncertain

- CoinGecko is not the settlement source and uses aggregated market data, so it cannot settle the contract.
- ETH/USD is not exactly ETH/USDT on Binance, though for a large-cap asset over a 24-hour horizon the contextual divergence is usually small.

## Why this source may matter

This source is a useful independence check against over-relying on one Binance snapshot. It shows the broader ETH spot regime is also currently above the strike, making the Yes thesis less dependent on a single venue artifact.

## Possible impact on the question

The contextual read supports a moderate Yes lean because ETH is not barely above the threshold only on one venue; the broader spot market also appears to be trading somewhat above 2300.

## Reliability notes

Good for context, not for settlement. Independence from Binance is partial rather than full because exchange aggregation may still include Binance among inputs, but it remains meaningfully useful as a separate market-data surface.