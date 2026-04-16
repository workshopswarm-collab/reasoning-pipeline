---
type: source_note
case_key: case-20260415-58166133
dispatch_id: dispatch-case-20260415-58166133-20260415T083617Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-58166133 | market-implied
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-58166133/researcher-analyses/2026-04-15/dispatch-case-20260415-58166133-20260415T083617Z/personas/market-implied.md]
tags: [polymarket, rules, market-implied, btc, binance]
---

# Summary

This source establishes the market-implied baseline and the contract mechanics. It shows the April 16 ladder with the 72,000 line trading around 84% Yes and states that resolution depends on the Binance BTC/USDT 1-minute candle labeled 12:00 in ET, using the final Close price.

## Key facts extracted

- The assigned market is the April 16 BTC threshold ladder on Polymarket.
- The 72,000 line was displayed around 84% Yes / 17% No at fetch time, consistent with the assignment's `current_price: 0.845`.
- Resolution is not based on a daily close or another exchange; it is specifically the Binance BTC/USDT 1-minute candle for 12:00 ET on April 16.
- The market resolves Yes only if that candle's final Close is strictly higher than 72,000.
- Price precision is determined by Binance's displayed source precision.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance... BTC/USDT ... with \"1m\" and \"Candles\" selected..."

## What is uncertain

- The public market page is not itself the final settlement source; Binance is.
- The page does not by itself provide a full recent spot history or volatility estimate, only the current contract prices and rule text.

## Why this source may matter

This is the governing contract surface for interpreting what counts. The explicit timing, exchange, pair, and strict-greater-than condition materially matter because a view based on generic BTC/USD price, another venue, or an end-of-day close could be wrong.

## Possible impact on the question

It anchors the market-implied probability and clarifies that all of the following must hold for Yes: the relevant candle must be Binance BTC/USDT, it must be the 12:00 ET one on April 16, and its final Close must exceed 72,000 exactly.

## Reliability notes

Useful and necessary for contract interpretation, but only medium as a source for the underlying asset price because Polymarket is quoting its own market rather than the settlement price itself.