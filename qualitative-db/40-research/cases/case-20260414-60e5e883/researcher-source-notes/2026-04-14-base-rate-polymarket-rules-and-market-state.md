---
type: source_note
case_key: case-20260414-60e5e883
dispatch_id: dispatch-case-20260414-60e5e883-20260414T190542Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the price of Bitcoin be above $70,000 on April 17?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket event page and rules for Bitcoin above on April 17
source_type: market rules / primary contract page
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-60e5e883/researcher-analyses/2026-04-14/dispatch-case-20260414-60e5e883-20260414T190542Z/personas/base-rate.md]
tags: [polymarket, market-rules, resolution-source, noon-et]
---

# Summary

This source establishes the governing contract mechanics and the market-implied baseline. It is the primary source for what counts at resolution and shows the current market price for the 70,000 threshold leg.

## Key facts extracted

- The market resolves to Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17 has a final close strictly higher than 70,000.
- The resolution source is Binance BTC/USDT with 1m candles selected.
- The contract is exchange-specific and pair-specific; other exchanges or pairs do not count.
- As fetched on 2026-04-14, the 70,000 threshold leg was trading around 93% Yes, implying roughly 0.925 to 0.93 market probability.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices... with \"1m\" and \"Candles\" selected"
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The public event page is a rendered web page rather than a structured rules API snapshot.
- The displayed market percentage can drift intraday; it is a snapshot rather than a time series.
- The page does not independently verify Binance data availability or any operational edge case around the final displayed candle.

## Why this source may matter

It governs the exact settlement condition and prevents using the wrong exchange, wrong pair, wrong timestamp, or wrong inequality. It also provides the market-implied probability against which the research view should be compared.

## Possible impact on the question

This source materially narrows the question from a vague "Bitcoin above 70k" call to a precise claim: Binance BTC/USDT 12:00 ET one-minute close on April 17 must print above 70,000. That means short-horizon price location and exact noon timing matter more than daily close narratives.

## Reliability notes

High relevance and high authority for contract interpretation, but only medium independence because Polymarket itself is the source of the rules and quoted market odds. It should be paired with direct Binance price checks for verification.
