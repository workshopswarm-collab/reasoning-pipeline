---
type: source_note
case_key: case-20260415-d9ca8ddf
dispatch_id: dispatch-case-20260415-d9ca8ddf-20260415T195847Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-17 be above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-d9ca8ddf/researcher-analyses/2026-04-15/dispatch-case-20260415-d9ca8ddf-20260415T195847Z/personas/market-implied.md]
tags: [polymarket, contract-rules, market-implied, binance]
---

# Summary

The Polymarket event page establishes both the current market-implied probability for the 72,000 threshold and the contract resolution mechanics. The displayed probability for "72,000" on April 17 was 93% at fetch time, which is directionally close to the assignment's stated current_price of 0.91. The page also states that resolution is based on the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17, specifically the final close price.

## Key facts extracted

- The relevant threshold market was shown at 93% Yes on the event page at fetch time.
- The market resolves on the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17, 2026.
- The decisive field is the candle's final "Close" price.
- The page explicitly says the market is about Binance BTC/USDT, not other exchanges or pairs.
- Price precision is determined by the source's decimal precision.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title."
- "The resolution source for this market is Binance..."
- The outcome ladder displayed 72,000 at 93%.

## What is uncertain

- The page fetch is a website render, not a signed API record, so displayed market percentage could move after capture.
- The rules mention Binance web UI, but for research/audit purposes Binance API klines are the closest machine-readable contextual proxy for understanding how the final check should look.

## Why this source may matter

This is the governing source for what counts. It defines the exact exchange, pair, time window, and field that decide resolution, so any market-implied view must be filtered through these mechanics.

## Possible impact on the question

The rules sharply reduce ambiguity: the question is not whether BTC trades above 72,000 generally, but whether Binance BTC/USDT's 12:00 ET one-minute candle closes above 72,000 on April 17. That narrows risk to spot price level at a precise timestamp plus operational/source-of-truth issues.

## Reliability notes

Useful as the contract-defining surface, but the page itself is not a fully independent verification source for underlying BTC price conditions. It should be paired with Binance data for context and explicit timing checks.