---
type: source_note
case_key: case-20260415-6c8d8ca4
dispatch_id: dispatch-case-20260415-6c8d8ca4-20260415T084705Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-6c8d8ca4 | market-implied
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules for Bitcoin above ___ on April 17
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-6c8d8ca4/researcher-analyses/2026-04-15/dispatch-case-20260415-6c8d8ca4-20260415T084705Z/personas/market-implied.md]
tags: [polymarket, contract-rules, price-threshold, binance, market-implied]
---

# Summary

This source establishes both the live market-implied probability and the exact contract mechanics. It shows the 72,000 strike trading around 81-82% Yes and states that resolution depends specifically on the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 17, using the final Close price.

## Key facts extracted

- The 72,000 outcome was displayed at roughly 81% with buy Yes around 82 cents at fetch time.
- The relevant date is Apr 17, 2026.
- The contract resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 ET has a final Close price strictly higher than 72,000.
- The source of truth is Binance BTC/USDT, not another exchange or another trading pair.
- Price precision is determined by Binance source decimals.

## Evidence directly stated by source

- Market-implied probability for the 72,000 threshold is around 0.81 to 0.82.
- Resolution is tied to a very specific timestamp, timezone, exchange, instrument, and field: Binance, BTC/USDT, 1m candle, 12:00 ET, final Close.
- Equality is not enough; the close must be higher than 72,000.

## What is uncertain

- The market page is a trading venue UI, not the final Binance candle itself.
- The fetched HTML is not a signed API record and could reflect small display delays.
- The Polymarket page does not itself prove where the Binance close will be on Apr 17.

## Why this source may matter

This is the governing contract source for what counts. Because the market is date-sensitive and rule-sensitive, this source is essential for avoiding wrong-exchange, wrong-pair, wrong-time, or wrong-comparison mistakes.

## Possible impact on the question

It strongly supports treating the market's current ~81% as the baseline prior, but it also highlights a narrow operational-resolution risk: even if spot BTC is broadly above 72k elsewhere, the contract still depends on the exact Binance BTC/USDT noon-ET minute close on Apr 17.

## Reliability notes

Useful and necessary as the contract surface, but not fully independent from the market itself. For the actual probability judgment it needs to be paired with an independent BTC price context source.