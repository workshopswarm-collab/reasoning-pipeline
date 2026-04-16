---
type: source_note
case_key: case-20260414-9c18e804
dispatch_id: dispatch-case-20260414-9c18e804-20260414T135145Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-9c18e804 | market-implied
question: Will Bitcoin reach $76,000 April 13-19?
driver:
date_created: 2026-04-14
source_name: CoinGecko Bitcoin market chart range API
source_type: market data aggregator API
source_url: https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range
source_date: 2026-04-14
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: market-implied
related_entities: [btc, bitcoin]
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [case, source-note, crypto, bitcoin, market-data]
---

# Summary

CoinGecko intraday range data for Bitcoin over the April 13-14 window shows BTC trading from roughly $70.7k to $74.8k, with the latest sampled value in this pull around $74.4k. That leaves the $76k threshold close but still outside the observed range so far.

## Key facts extracted

- Sampled period used in this pull covered April 13-14, 2026.
- Earliest sampled price in the pull: about $70,904.
- Lowest sampled price in the pull: about $70,678.
- Highest sampled price in the pull: about $74,760.
- Latest sampled price in the pull: about $74,448.
- Threshold under study is $76,000, which is about 1.7% above the sampled high and about 2.1% above the latest sampled price.

## Evidence directly stated by source

- CoinGecko returned timestamped Bitcoin USD prices for the requested range.
- The maximum observed value in the returned dataset was below $76,000.

## What is uncertain

- CoinGecko is an aggregator rather than the contract's explicit governing source of truth.
- The returned range only covers data through the time of retrieval; BTC still has multiple days left in the contract window.
- Aggregator prints can differ slightly from exchange-specific highs used in venue-specific interpretations.

## Why this source may matter

This source gives a recent and reasonably independent contextual check on how far BTC is from the threshold and whether a 75% contract price is consistent with recent realized volatility.

## Possible impact on the question

The source supports a view that the contract is plausible but not close to settled yet: BTC has already rallied materially into the mid-$75k area on spot venues, but the target has not yet been observed in this dataset.

## Reliability notes

CoinGecko is widely used and timely, but it is still a secondary aggregation source rather than the market's explicit governing source. Best used as contextual price-path evidence, not as final settlement authority.
