---
type: source_note
case_key: case-20260415-1a345042
dispatch_id: dispatch-case-20260415-1a345042-20260415T223206Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-1a345042 | catalyst-hunter
question: Will the price of Bitcoin be above $72,000 on April 21?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market venue / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: catalyst-hunter
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, contract-rules, pricing, resolution-source]
---

# Summary

This source establishes the market-implied probability and the exact resolution mechanics.

## Key facts extracted

- The $72,000 line was trading around 81% on the market page at time of review.
- The contract resolves on the Binance BTC/USDT 1-minute candle for 12:00 ET on April 21, 2026.
- The deciding value is the final candle close, not an average, not another exchange, and not a daily close.
- Price precision is determined by Binance source decimals.

## Evidence directly stated by source

- Resolution is tied specifically to Binance BTC/USDT.
- The relevant timestamp is 12:00 in ET timezone.
- The relevant field is the candle close for the 1-minute candle.

## What is uncertain

- The page itself is not the ultimate settlement feed; Binance is.
- The Polymarket page shows current market pricing but not why traders hold that view.

## Why this source may matter

It is the governing contract surface and therefore mandatory for interpreting what counts.

## Possible impact on the question

It narrows the operative catalysts to events that can move Binance BTC/USDT specifically into the noon ET April 21 one-minute close, rather than broader weekly Bitcoin sentiment alone.

## Reliability notes

Reliable for market rules and displayed odds, but settlement still depends on Binance as the source of truth.