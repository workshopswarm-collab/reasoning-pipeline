---
type: source_note
case_key: case-20260413-64e915de
dispatch_id: dispatch-case-20260413-64e915de-20260413T234340Z
analysis_date: 2026-04-13
persona: base-rate
domain: crypto
subdomain: protocols
entity: ethereum
topic: will-ethereum-reach-2400-april-13-19
question: Will Ethereum reach $2,400 April 13-19?
date_created: 2026-04-13
source_name: CoinGecko Ethereum market_chart API
source_type: price data API / contextual verification
source_url: https://api.coingecko.com/api/v3/coins/ethereum/market_chart?vs_currency=usd&days=7&interval=hourly
source_date: 2026-04-13
credibility: medium-high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [ethereum]
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [coingecko, price-data, source-note]
---

# Summary

CoinGecko's 7-day hourly ETH/USD market chart provided an independent price verification pass. The fetched series contained 174 hourly points and showed a maximum observed price of about $2,374.36 as of 2026-04-13T23:43:57Z.

## Key facts extracted

- Dataset: ETH market_chart, USD, 7 days, hourly interval.
- Observed maximum in the fetched data: about $2,374.36.
- Timestamp of that observed maximum: 2026-04-13T23:43:57Z.
- The latest point in the fetched series matched that same ~$2,374.36 level.

## Evidence directly stated by source

- Recent ETH/USD spot-price history remained below $2,400 in the fetched hourly series at verification time.

## What is uncertain

- CoinGecko is a strong contextual price aggregator, but it is not necessarily the Polymarket settlement source.
- Hourly sampled data can miss an intrahour wick above $2,400 if one occurred.
- The market window runs through April 19, so this source does not settle the final answer yet; it only informs whether the threshold had already been reached as of verification time.

## Why this source may matter

It is an independent, current, external price check against the market's very high implied probability.

## Possible impact on the question

The source modestly tempers the strongest bullish reading because, despite the market's 92% implied probability, the verified external hourly series still sat below $2,400 at check time. That matters most as disconfirming evidence against certainty, not as decisive evidence against eventual resolution.

## Reliability notes

Good for near-real-time contextual verification and stronger than narrative commentary, but still not the governing settlement source. The hourly interval and aggregator nature mean it should be treated as corroboration rather than final authority.