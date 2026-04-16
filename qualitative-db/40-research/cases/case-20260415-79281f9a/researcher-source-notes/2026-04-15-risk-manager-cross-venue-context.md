---
type: source_note
case_key: case-20260415-79281f9a
dispatch_id: dispatch-case-20260415-79281f9a-20260415T202526Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68k-on-april-20
question: Will the price of Bitcoin be above $68,000 on April 20?
driver: reliability
date_created: 2026-04-15
source_name: CoinGecko Bitcoin spot reference
source_type: market-data-aggregator
source_url: https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: supports-yes
certainty: medium
importance: medium
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-79281f9a/researcher-analyses/2026-04-15/dispatch-case-20260415-79281f9a-20260415T202526Z/personas/risk-manager.md]
tags: [cross-check, secondary-source, market-context]
---

# Summary
A secondary cross-venue check from CoinGecko also put Bitcoin near 74.7k on 2026-04-15, consistent with Binance and suggesting no obvious venue-specific anomaly around the time of review.

## Key facts extracted
- CoinGecko simple price endpoint returned Bitcoin at 74,748 USD.
- This was within about 100 dollars of the Binance average-price context and within roughly 0.15% of the Binance spot ticker used in the primary note.

## Evidence directly stated by source
- Bitcoin spot reference across CoinGecko's aggregation was approximately 74.7k.

## What is uncertain
- CoinGecko is contextual, not the governing settlement source.
- The endpoint does not resolve the exact noon ET Binance candle question.

## Why this source may matter
It is useful as an independence check that the large cushion above 68k was not an artifact of one stale or abnormal venue print.

## Possible impact on the question
This secondary confirmation slightly increases confidence in the directional view but should not be overweighted because the contract resolves only on Binance BTC/USDT.

## Reliability notes
- Good for contextual validation.
- Lower authority than Binance for this market because it is not the settlement venue.
- Independence is partial: aggregated spot data can still be correlated with Binance-led market structure.