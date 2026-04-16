---
type: source_note
case_key: case-20260415-47643da0
dispatch_id: dispatch-case-20260415-47643da0-20260415T010752Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
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
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, rules, market-implied, binance, settlement]
---

# Summary

This source establishes the market-implied baseline and the relevant contract mechanics. For the $72,000 threshold on April 17, the page showed the line trading around 84% at fetch time, which is consistent with the assignment's `current_price: 0.84`. The rules state that resolution depends on the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on Apr. 17, using the candle's final Close price, not another exchange or benchmark.

## Key facts extracted

- The $72,000 line for Apr. 17 was displayed around 84% / 85¢ Yes.
- The market resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 ET on Apr. 17 has a final Close price strictly higher than 72,000.
- The specified source of truth is Binance BTC/USDT with 1m candles selected.
- The contract is exchange-specific and pair-specific: Binance BTC/USDT, not other exchanges or pairs.
- Precision is determined by the decimal places on the source.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/BTC_USDT with \"1m\" and \"Candles\" selected on the top bar."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The fetched page is a public web rendering, not an authenticated exchange or Polymarket API payload.
- The market page itself does not prove future Binance behavior; it only defines the contract and shows current market pricing.
- The page does not itself provide the eventual settlement candle.

## Why this source may matter

It is the governing market-definition source for what must happen to resolve Yes or No, so it is necessary for interpreting the threshold, time, timezone, exchange, pair, and strict-greater-than condition.

## Possible impact on the question

This source narrows the question to a very specific operational test: by Apr. 17 at 12:00 ET, Binance BTC/USDT's 1-minute candle close must be above 72,000. Any broader Bitcoin price discussion only matters insofar as it informs that specific Binance close.

## Reliability notes

The contract text is the key direct source for the resolution mechanics, but the page is still a market venue page rather than the eventual settlement output itself. Reliability for market pricing and rules is good enough for setup, while the actual settlement value will still need to come from Binance.