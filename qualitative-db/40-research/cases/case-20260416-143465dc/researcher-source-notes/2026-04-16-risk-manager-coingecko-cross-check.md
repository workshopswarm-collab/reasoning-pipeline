---
type: source_note
case_key: case-20260416-143465dc
dispatch_id: dispatch-case-20260416-143465dc-20260416T191321Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: markets
entity: sol
topic: solana-touch-90-april-13-19
question: Will Solana reach $90 April 13-19?
date_created: 2026-04-16
source_name: CoinGecko simple price API cross-check
source_type: market_data_aggregator
source_url: https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_high=true&include_24hr_low=true&include_last_updated_at=true
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: orchestrator
related_entities: [sol]
related_drivers: [sentiment]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-143465dc/researcher-analyses/2026-04-16/dispatch-case-20260416-143465dc-20260416T191321Z/personas/risk-manager.md]
tags: [source-note, coingecko, cross-check, contextual]
---

# Summary

This source is a contextual cross-check on current SOL spot pricing. It is not the governing source of truth for settlement.

## Key facts extracted

- CoinGecko simple price returned SOL at approximately **$88.94** at the time of fetch.
- The CoinGecko reading was directionally consistent with the near-contemporaneous Binance ticker reading around **$88.84**.

## Evidence directly stated by source

- API output: `{"solana":{"usd":88.94,"last_updated_at":1776366967}}`

## What is uncertain

- This endpoint did not return the 24h high in the observed response despite the request parameter.
- CoinGecko aggregates across venues and therefore cannot answer the market directly.

## Why this source may matter

It serves as an independent contextual confirmation that SOL was trading in the high-88s rather than already well through $90 at the time of analysis.

## Possible impact on the question

It slightly increases confidence that the market is genuinely close to the threshold, but does not materially reduce the core contract risk because settlement depends on Binance 1-minute highs only.

## Reliability notes

Medium reliability for contextual price confirmation; low relevance for final resolution mechanics. Useful as an extra verification pass, not as a governing source.