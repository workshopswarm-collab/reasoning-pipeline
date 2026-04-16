---
type: source_note
case_key: case-20260416-e0b8c17c
dispatch_id: dispatch-case-20260416-e0b8c17c-20260416T050131Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-e0b8c17c | market-implied
question: Will the price of Bitcoin be above $72,000 on April 20?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page for Bitcoin above $72,000 on April 20
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-16
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: market-implied
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-e0b8c17c/researcher-analyses/2026-04-16/dispatch-case-20260416-e0b8c17c-20260416T050131Z/personas/market-implied.md]
tags: [polymarket, contract-rules, market-price, settlement]
---

# Summary

This source establishes both the live market-implied probability and the contract mechanics. It shows the $72,000 strike trading around 84-85% and states that resolution depends on the Binance BTC/USDT 1-minute candle for 12:00 PM ET on April 20, specifically the final Close price.

## Key facts extracted

- The assigned market price is 0.835, implying an 83.5% Yes probability.
- The public Polymarket page showed the $72,000 line around 84-85% Yes at fetch time.
- The market resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 PM ET on April 20 has a final Close strictly higher than 72,000.
- The named source of truth is Binance BTC/USDT with 1m Candles selected.
- This is exchange-specific and pair-specific; other exchanges or BTC/USD quotes do not govern settlement.
- Price precision is determined by the source display.

## Evidence directly stated by source

- Resolution source: Binance BTC/USDT.
- Timing rule: 12:00 in ET timezone on the specified date.
- Condition rule: final Close price must be higher than the strike, not equal to it.

## What is uncertain

- The Polymarket page is a secondary display of contract rules, not Binance itself.
- The page does not itself prove what Binance will display on April 20; it only defines the intended settlement mechanics.

## Why this source may matter

This is the governing contract surface for what has to happen for the market to resolve Yes or No. It also anchors the market-implied consensus that must be compared against the independent estimate.

## Possible impact on the question

Because the contract is a narrow point-in-time, exchange-specific, strict-greater-than condition, settlement risk is higher than for a generic statement like "Bitcoin trades above 72k that day." The market can be directionally right on BTC strength but still lose on a brief noon ET dip or a Binance-specific print.

## Reliability notes

High value for contract interpretation and current market pricing; not sufficient by itself for the underlying BTC probability because it is not the authoritative settlement venue and does not provide the future resolving candle.