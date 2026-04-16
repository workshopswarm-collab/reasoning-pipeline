---
type: source_note
case_key: case-20260414-e15c72fe
dispatch_id: dispatch-case-20260414-e15c72fe-20260414T193100Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: market-implied
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [market-implied-finding]
tags: [polymarket, contract-rules, market-implied, resolution]
---

# Summary

The Polymarket event page provides the live outcome ladder and the contract mechanics. For the $70,000 line on April 20, the page showed roughly 89%-90% Yes at fetch time, consistent with the assignment's `current_price` of 0.845 as a slightly earlier snapshot. The rules state that resolution depends specifically on the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 20, using the candle's final Close price.

## Key facts extracted

- The market page displayed the April 20 ladder with the $70,000 line around 89%-90% Yes.
- The assignment snapshot listed `current_price: 0.845`, implying 84.5% market-implied probability at that moment.
- Resolution is based on the Binance BTC/USDT market, not other exchanges or pairs.
- Resolution uses the 1-minute candle for 12:00 PM ET on April 20.
- The final Close of that 1-minute candle must be strictly higher than 70,000 for Yes.
- Price precision is determined by the number of decimals shown by the source.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance... BTC/USDT... with \"1m\" and \"Candles\" selected..."

## What is uncertain

- The web fetch captured the public page text but not a timestamped trade history sufficient to reconstruct intraday moves in the $70k line.
- The page itself does not prove Binance UI accessibility at resolution time; it only states intended settlement mechanics.

## Why this source may matter

This is the governing contract source for what counts. It makes the question narrower than a generic "BTC above $70k on April 20" claim because all of the following must hold for Yes: correct date, noon ET timestamp, Binance as venue, BTC/USDT pair, 1-minute candle, and final Close strictly above 70,000.

## Possible impact on the question

This source supports the market's high confidence partly because the line is materially below the current spot area, but it also creates a contract-mechanics tail risk: a noon ET one-minute close on one exchange can differ from broader-day or cross-exchange intuition.

## Reliability notes

Polymarket is authoritative for the market's own rules but not for the underlying BTC price itself. It is the source of truth for contract interpretation, while Binance is the intended source of truth for settlement data.