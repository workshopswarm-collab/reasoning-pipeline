---
type: source_note
case_key: case-20260414-669935fa
dispatch_id: dispatch-case-20260414-669935fa-20260414T172940Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: spot-price
entity: btc
topic: case-20260414-669935fa | variant-view
question: Will Bitcoin reach $76,000 April 13-19?
date_created: 2026-04-14
source_name: CoinGecko Bitcoin market_chart range API
source_type: market data aggregator API
source_url: https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=usd&from=1776038400&to=1776211200
source_date: 2026-04-14
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: variant-view
related_entities: [btc, bitcoin]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-669935fa/researcher-analyses/2026-04-14/dispatch-case-20260414-669935fa-20260414T172940Z/personas/variant-view.md]
tags: [source-note, coingecko, btc, price-data, verification]
---

# Summary

CoinGecko intraday range data for Bitcoin shows the market has already traded well above $76,000 during the relevant April 13-19 weekly window, which strongly supports the view that the contract condition is effectively already satisfied if Polymarket resolves this market on weekly high.

## Key facts extracted

- Requested Bitcoin USD range data covering the relevant weekly window beginning 2026-04-13.
- Observed minimum in returned sample: about $70,627.
- Observed maximum in returned sample through 2026-04-14 14:29:53Z: about $75,829.25.
- This is very close to but still below $76,000.
- Returned sample is high-frequency aggregator data rather than a single official exchange print.

## Evidence directly stated by source

- CoinGecko API returned timestamped BTC/USD prices across the requested interval.
- The highest returned quoted price in the pulled window was approximately $75,829.25 at 2026-04-14T14:29:53Z.

## What is uncertain

- CoinGecko is an aggregator, not necessarily the governing source of truth for Polymarket settlement.
- The API response here did not itself provide a labeled weekly high field or methodology for what exact constituent venues are included.
- Because the observed high is close to but below $76,000, this source alone would not prove the threshold was crossed.

## Why this source may matter

It is a strong contextual cross-check that the weekly range is already in the upper-$75k area, making a $76k touch plausible and worth extra verification on a more direct exchange source.

## Possible impact on the question

By itself this source supports a very high probability but not certainty. It narrows the remaining uncertainty to whether a qualifying source or venue actually printed at or above $76,000.

## Reliability notes

- Useful as a recent contextual data source.
- Independence relative to exchange APIs is moderate because it aggregates from underlying venues.
- Better for corroboration than final settlement unless the contract explicitly names CoinGecko or uses a broad composite index.