---
type: source_note
case_key: case-20260416-1f25d147
dispatch_id: dispatch-case-20260416-1f25d147-20260416T035120Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: solana
entity: sol
topic: case-20260416-1f25d147 | risk-manager
question: Will the Binance SOL/USDT 12:00 ET 1-minute candle on April 19, 2026 close above 80?
driver: reliability
date_created: 2026-04-15
source_name: CoinGecko Solana market context
source_type: secondary_market_context
source_url: https://api.coingecko.com/api/v3/coins/solana
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: Orchestrator
related_entities: [sol, solana]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-1f25d147/researcher-analyses/2026-04-16/dispatch-case-20260416-1f25d147-20260416T035120Z/personas/risk-manager.md]
tags: [coingecko, contextual-source, cross-check]
---

# Summary

CoinGecko provided an independent contextual price cross-check around 85.29 USD for Solana during the run, broadly consistent with Binance spot around 85.37 USDT. This does not govern resolution, but it reduces concern that Binance was showing an idiosyncratic price far from broader market context.

## Key facts extracted

- CoinGecko listed Solana current price around 85.29 USD at fetch time.
- CoinGecko identified Solana as a major layer-1 asset with high market-cap rank, implying deep liquidity and lower odds of an isolated random print relative to smaller assets.
- The cross-check level was close to Binance spot and therefore consistent with the market being several dollars above the 80 threshold.

## Evidence directly stated by source

- Direct contextual evidence: current broad-market SOL price was around mid-85s.
- Direct contextual evidence: Solana remains a top-tier crypto asset rather than a thinly traded microcap.

## What is uncertain

- CoinGecko is not the resolution source.
- CoinGecko aggregates market context and may lag or smooth venue-specific prices.
- This source does not answer the exact noon ET 1-minute close condition.

## Why this source may matter

It is a useful additional verification pass because the market probability is extreme and the contract is time-specific. The cross-check helps confirm that the bullish cushion is not purely a Binance-only artifact.

## Possible impact on the question

This source modestly supports the Yes side by confirming that the broader market level is similar to Binance and still above 80, but it should receive less weight than Binance because the contract resolves only on Binance SOL/USDT.

## Reliability notes

- Good contextual verification source, but not authoritative for settlement.
- Independence from Binance is only partial because price aggregators depend on exchange data feeds, so evidence independence is medium rather than high.