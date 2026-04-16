---
type: source_note
case_key: case-20260414-e495c9da
dispatch_id: dispatch-case-20260414-e495c9da-20260414T191806Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-e495c9da | risk-manager
question: Will the price of Bitcoin be above $70,000 on April 19?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market rules page
source_type: market contract / resolution rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-19
source_date: 2026-04-14
credibility: medium-high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, resolution-rules, binance, btc]
---

# Summary

This source establishes the governing contract mechanics. The market resolves Yes if the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 19 has a final Close strictly above 70,000. It is not enough for BTC to trade above 70,000 elsewhere, earlier in the day, or on another venue.

## Key facts extracted

- Governing source of truth is Binance BTC/USDT.
- Relevant data field is the 1-minute candle Close, not high/low/average.
- Relevant time is 12:00 PM ET on April 19, 2026.
- Resolution is strict inequality: higher than 70,000.
- Price precision is whatever Binance displays for the source candle.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance... BTC/USDT... with '1m' and 'Candles' selected."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The page does not itself provide the future April 19 candle; it only defines the resolution method.
- The page does not clarify any fallback if Binance UI/API presentation changes, though Binance remains the named source.

## Why this source may matter

This is the direct contract source. For a date-specific, narrow-resolution market, correct interpretation of the venue, pair, timestamp, and price field is more important than general BTC direction.

## Possible impact on the question

This source narrows the thesis materially: for Yes, BTC must still be above 70,000 specifically on Binance BTC/USDT at the noon ET close on April 19. Intraday spikes or non-Binance prices do not settle the contract.

## Reliability notes

Primary contract source. High relevance. Some operational ambiguity remains because Polymarket references the Binance trading interface rather than an immutable API endpoint, but the source-of-truth instruction is still explicit enough for practical interpretation.