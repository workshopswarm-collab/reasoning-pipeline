---
type: source_note
case_key: case-20260414-f6393095
dispatch_id: dispatch-case-20260414-f6393095-20260414T222237Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the price of Bitcoin be above $70,000 on April 17?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules for bitcoin-above-70k-on-april-17
source_type: market rules / prediction market page
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-14
credibility: medium
recency: current
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, contract, resolution-source, btc]
---

# Summary

This source establishes the market-implied baseline and the exact contract wording. It is not itself the settlement source; it points to Binance BTC/USDT 1-minute candles as the governing source of truth.

## Key facts extracted

- The quoted current market price for the $70,000 line is about 93.9%, matching the assignment current_price of 0.935 within rounding.
- The contract resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 in ET on April 17 has a final close strictly higher than 70,000.
- The source explicitly says the market is about Binance BTC/USDT, not other exchanges or other trading pairs.
- Price precision is determined by the number of decimals shown by the source.

## Evidence directly stated by source

- Resolution source: Binance BTC/USDT candle data.
- Relevant interval: 1 minute.
- Relevant timestamp: 12:00 in ET on the date in the title.
- Threshold logic: strictly higher than 70,000.

## What is uncertain

- The market page does not itself provide the final settlement candle; it only specifies where to look.
- The page does not clarify any fallback if Binance UI/API displays change, so some operational interpretation risk remains.

## Why this source may matter

This is the governing contract interpretation surface for what counts. Because the case is narrow, date-sensitive, and already priced at an extreme probability, correct resolution mechanics matter almost as much as directional BTC price view.

## Possible impact on the question

This source materially reduces ambiguity about what must happen for Yes: not just BTC above 70k in a general sense, but Binance BTC/USDT above 70k on the exact ET noon candle close.

## Reliability notes

Useful and necessary for contract wording, but not independent evidence on BTC direction. Reliability is medium because Polymarket is authoritative for its own rule text, yet the actual source of truth is externalized to Binance.