---
type: source_note
case_key: case-20260415-2ce6159e
dispatch_id: dispatch-case-20260415-2ce6159e-20260415T142913Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-16 be above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page and rule text
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, contract-rules, market-implied-probability, binance]
---

# Summary

This source establishes the market-implied probability and the operative contract wording. It says the market resolves based on the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 16, using the final Close price, with price precision determined by Binance's displayed decimals.

## Key facts extracted

- The 72,000 strike was trading around 91% on the fetched page, while the assignment context reported current_price 0.925.
- The contract resolves Yes only if the relevant Binance BTC/USDT 1-minute candle Close is strictly higher than 72,000.
- The source of truth is Binance BTC/USDT, not other exchanges or pairs.
- Timing matters: the relevant candle is 12:00 ET on April 16, not any intraday high or nearby minute.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices..."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The fetched page is a rendered market page rather than an archival rulebook snapshot, so later UI changes are possible.
- The page does not by itself answer whether BTC will remain above 72,000 through the exact resolution minute.

## Why this source may matter

This is the governing contract source for what must happen for Yes to resolve. It defines the exact exchange, pair, minute, timezone, and close-price condition.

## Possible impact on the question

This source makes the main analytical issue narrow and date-specific: BTC can trade above 72,000 generally, but Yes only wins if Binance's 12:00 ET candle on April 16 closes above 72,000. That narrows the relevant base-rate question to near-term one-day downside risk and microstructure/timing risk rather than broad medium-term BTC direction.

## Reliability notes

Useful and necessary as the contract source, but only medium credibility for probability inference because market prices are endogenous and the page is not an independent external source.