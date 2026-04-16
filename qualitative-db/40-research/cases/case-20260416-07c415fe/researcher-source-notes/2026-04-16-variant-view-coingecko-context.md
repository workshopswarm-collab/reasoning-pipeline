---
type: source_note
case_key: case-20260416-07c415fe
dispatch_id: dispatch-case-20260416-07c415fe-20260416T031541Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: market-context
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 12:00 ET one-minute candle close above 80 on April 19, 2026?
driver: reliability
date_created: 2026-04-15
source_name: CoinGecko Solana API market context
source_type: market_data_aggregator
source_url: https://api.coingecko.com/api/v3/coins/solana
source_date: 2026-04-16
credibility: medium_high
recency: high
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: variant-view
related_entities: [sol, solana]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-07c415fe/researcher-analyses/2026-04-16/dispatch-case-20260416-07c415fe-20260416T031541Z/personas/variant-view.md]
tags: [coingecko, source-note, market-context]
---

# Summary

CoinGecko API context independently places Solana around $85.23 on 2026-04-16 and shows modestly positive 24h/7d/14d performance, though still negative over 30 days. This supports the view that spot is currently above the threshold, while also showing enough recent volatility to keep a sub-100% probability on the Yes side.

## Key facts extracted

- CoinGecko current price for Solana was about $85.23.
- 24h change was about +2.25%.
- 7d change was about +3.69%.
- 14d change was about +7.46%.
- 30d change was about -10.57%.
- Market cap rank was 7.

## Evidence directly stated by source

- Current aggregated USD spot reference.
- Short-horizon percentage change metrics.

## What is uncertain

- CoinGecko is not the formal settlement source; Binance remains the governing source of truth.
- Aggregated pricing can differ somewhat from Binance SOL/USDT at the exact minute that matters.

## Why this source may matter

It gives an independent contextual check that Binance is not showing an obvious outlier price. The negative 30d change is the useful caution flag: SOL is above 80 now, but this is still a volatile asset capable of moving several percent before the settlement window.

## Possible impact on the question

This source modestly supports Yes while also reinforcing the strongest non-consensus caveat: the market may be a bit too close to certainty for a short-dated crypto threshold market that still requires holding above 80 at one exact minute.

## Reliability notes

- Good as an independent contextual source.
- Not authoritative for resolution.
- Useful mainly for cross-checking direction and recent volatility regime.
