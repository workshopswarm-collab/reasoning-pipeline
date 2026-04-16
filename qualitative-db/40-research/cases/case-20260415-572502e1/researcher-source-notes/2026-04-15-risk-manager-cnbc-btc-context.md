---
type: source_note
case_key: case-20260415-572502e1
dispatch_id: dispatch-case-20260415-572502e1-20260415T124520Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: spot-market-context
entity: btc
topic: case-20260415-572502e1 | risk-manager
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: reliability
date_created: 2026-04-15
source_name: CNBC BTC.CM quote page
source_type: market-data-context
source_url: https://www.cnbc.com/quotes/BTC.CM=
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: risk-manager
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [source-note, cnbc, btc, spot-context]
---

# Summary
This source is a contextual price check rather than the governing settlement source. It showed Bitcoin trading materially above 72000 on April 15, with quoted open 74307.99, day high 74799.56, day low 73567.41, and previous close 74255.51.

## Key facts extracted
- BTC quoted open: 74,307.99.
- Day high: 74,799.56.
- Day low: 73,567.41.
- Previous close: 74,255.51.
- All visible quoted levels were above 72,000.

## Evidence directly stated by source
The page directly states the day's quoted BTC/USD range and prior close.

## What is uncertain
- This is not Binance BTC/USDT and therefore cannot settle the market.
- The extracted page is thin and does not provide methodology detail in the fetch output.
- A one-day contextual range cannot eliminate overnight volatility or exchange-specific divergence by the noon ET resolving minute.

## Why this source may matter
It is a useful contextual verification pass because it suggests BTC entered the final pre-resolution day with a cushion of roughly 1.5k-2.8k over the threshold, making Yes directionally plausible.

## Possible impact on the question
Supports a high-but-not-certain Yes view. The cushion lowers the probability that normal noise alone pushes BTC below 72000 at the resolving minute, but it does not remove timing risk, intraday volatility, or Binance-specific settlement risk.

## Reliability notes
Medium reliability as contextual price evidence. High recency, but only moderate independence and weaker relevance than Binance because it is a different venue/reference feed.
