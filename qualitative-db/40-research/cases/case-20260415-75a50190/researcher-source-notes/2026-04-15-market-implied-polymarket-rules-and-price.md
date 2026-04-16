---
type: source_note
case_key: case-20260415-75a50190
dispatch_id: dispatch-case-20260415-75a50190-20260415T205116Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-21
question: Will the price of Bitcoin be above $72,000 on April 21?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page for Bitcoin above 72,000 on April 21
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: market-implied
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-75a50190/researcher-analyses/2026-04-15/dispatch-case-20260415-75a50190-20260415T205116Z/personas/market-implied.md]
tags: [polymarket, contract-rules, market-price, bitcoin]
---

# Summary

This source established the live market-implied baseline and the contract mechanics for the specific threshold market.

## Key facts extracted

- The 72,000 outcome was trading around 80-81% on the event page at time of review.
- The contract resolves based on the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 21, 2026.
- The relevant metric is the final candle close, not intraday high, not another exchange, and not another pair.
- Price precision is determined by the Binance source display.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title."
- "The resolution source for this market is Binance... BTC/USDT... with \"1m\" and \"Candles\" selected."

## What is uncertain

- The fetched page is a live market surface, so displayed probabilities can move after capture.
- The web snapshot is useful for rules and rough live price, but final resolution still depends on Binance at the specified time.

## Why this source may matter

It is the governing market surface for both current crowd pricing and the exact contract wording. For a date-specific threshold market, this is necessary to avoid evaluating the wrong exchange, wrong timestamp, or wrong condition.

## Possible impact on the question

The source shows the crowd is already pricing a fairly high chance of Bitcoin staying above 72,000 by the relevant noon ET snapshot. It also narrows the question to a specific Binance 1-minute close, which slightly increases operational/venue-specific resolution risk versus a generic spot-price question.

## Reliability notes

Useful and necessary for contract interpretation, but not itself the final source of truth for settlement. Reliability for rules is high enough; reliability for the displayed probability is only point-in-time and should be treated as a live snapshot.