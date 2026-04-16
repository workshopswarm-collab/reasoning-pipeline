---
type: source_note
case_key: case-20260416-7bf6a6c4
dispatch_id: dispatch-case-20260416-7bf6a6c4-20260416T025105Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: Binance noon ET close-above-74000 resolution mechanics
question: Will the price of Bitcoin be above $74,000 on April 17?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page and rules
source_type: market_rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [source-note, polymarket, binance, resolution-mechanics, bitcoin]
---

# Summary

This source defines the contract mechanics. It matters because the market is not about generic BTC spot, daily close, or intraday high; it resolves specifically on the Binance BTC/USDT 1-minute candle labeled 12:00 ET on April 17 and requires the final close to be higher than 74000.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 in ET on April 17 has a final close above 74000.
- The governing source is Binance, specifically BTC/USDT with 1m candles selected.
- Other exchanges and other trading pairs do not govern resolution.
- Price precision is whatever Binance displays in the source.
- The page showed the 74000 outcome around 73% at fetch time, consistent with assignment current_price 0.71.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/BTC_USDT with \"1m\" and \"Candles\" selected on the top bar."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The market page does not itself provide the future qualifying April 17 12:00 ET candle close yet.
- The fetched public page shows market prices and rules, but not a durable official chart snapshot for the resolving minute.
- The exact mapping from ET noon to Binance UTC candle timestamp must still be handled carefully at resolution time.

## Why this source may matter

It is the governing source-of-truth specification. It determines what counts and what does not count, and it is the main defense against over-reading generic spot or cross-exchange data.

## Possible impact on the question

This source makes timing risk the central issue. BTC being above 74000 tonight or on other venues is supportive context only; the contract still fails if the final Binance BTC/USDT 12:00 ET 1-minute close on April 17 is 74000 or lower.

## Reliability notes

High reliability for resolution mechanics because it is the contract source itself. It is not direct evidence of the eventual outcome; it is direct evidence of what the outcome must depend on.
