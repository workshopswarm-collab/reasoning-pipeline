---
type: source_note
case_key: case-20260415-7d14e3a4
dispatch_id: dispatch-case-20260415-7d14e3a4-20260415T231343Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-7d14e3a4 | market-implied
question: Will the price of Bitcoin be above $72,000 on April 19?
driver: reliability
date_created: 2026-04-15
source_name: CNBC BTC.CM quote snapshot
source_type: secondary market-data context
source_url: https://www.cnbc.com/quotes/BTC.CM=
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-7d14e3a4/researcher-analyses/2026-04-15/dispatch-case-20260415-7d14e3a4-20260415T231343Z/personas/market-implied.md]
tags: [secondary-source, btc-price-context]
---

# Summary

This source note preserves an independent contextual price check outside Binance.

## Key facts extracted

- CNBC quote snapshot showed Bitcoin open around `74,307.99`, day high `75,441.03`, day low `73,567.41`, previous close `74,255.51`.
- These levels are directionally consistent with Binance spot trading in the mid-$74k area.
- The intraday low remained above $72,000 in this snapshot.

## Evidence directly stated by source

- Open, high, low, and previous close for a Bitcoin/USD market-data reference.

## What is uncertain

- This is not the settlement venue or pair.
- Quote methodology differs from Binance BTC/USDT.
- The fetched page did not provide a full timestamped candle series.

## Why this source may matter

It provides an independent cross-check that the broader BTC market is also trading materially above the strike, reducing concern that a Binance-only anomaly explains the current level.

## Possible impact on the question

Supports the idea that the Polymarket price is anchored in a broader market state where BTC has a multi-thousand-dollar cushion over $72,000 rather than in an isolated venue quirk.

## Reliability notes

Moderate reliability as contextual market data. Useful for independence and sanity-checking, but clearly secondary to Binance for settlement interpretation.
