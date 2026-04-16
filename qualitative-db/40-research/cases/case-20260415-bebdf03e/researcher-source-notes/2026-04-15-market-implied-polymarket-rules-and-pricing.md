---
type: source_note
case_key: case-20260415-bebdf03e
dispatch_id: dispatch-case-20260415-bebdf03e-20260415T221944Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-bebdf03e | market-implied
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 72000 on April 21, 2026?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page and rules
source_type: market rules page
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: market-implied
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-bebdf03e/researcher-analyses/2026-04-15/dispatch-case-20260415-bebdf03e-20260415T221944Z/personas/market-implied.md]
tags: [polymarket, rules, source-note, settlement]
---

# Summary

The Polymarket event page states the market is about whether the Binance BTC/USDT 1-minute candle for 12:00 ET on April 21 closes above 72,000, and the page shows the 72,000 contract trading around 81% during this run.

## Key facts extracted

- Event date: April 21, 2026.
- Threshold: 72,000.
- Resolution source: Binance BTC/USDT with 1m candles selected.
- Relevant value: final Close price for the 12:00 ET candle.
- During fetch, the page displayed Buy Yes around 81 cents for 72,000, broadly matching assignment current_price 0.815.

## Evidence directly stated by source

- The contract resolves to Yes only if the specified Binance candle close is higher than 72,000.
- It is explicitly not about other exchanges or other trading pairs.
- Price precision is determined by the source display.

## What is uncertain

- The fetched webpage is a rendered market page rather than a formal rulebook document with edge-case examples.
- The exact 12:00 ET candle mapping to UTC time is implied but not explained in technical detail on the page.

## Why this source may matter

This is the governing contract and current market-pricing source. It defines both the market-implied probability baseline and the source-of-truth mechanics that must be checked before making a directional call.

## Possible impact on the question

It narrows the question to a specific venue, pair, timestamp, and close metric. That reduces ambiguity but also means cross-exchange BTC context is secondary to Binance-specific pricing at the resolution minute.

## Reliability notes

High authority for contract wording and current displayed pricing. Lower value for independent market context because it is the market itself, not an outside source.