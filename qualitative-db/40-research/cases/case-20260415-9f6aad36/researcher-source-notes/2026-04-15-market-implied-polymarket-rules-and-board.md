---
type: source_note
case_key: case-20260415-9f6aad36
dispatch_id: dispatch-case-20260415-9f6aad36-20260415T082436Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-9f6aad36 | market-implied
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-9f6aad36/researcher-analyses/2026-04-15/dispatch-case-20260415-9f6aad36-20260415T082436Z/personas/market-implied.md]
tags: [polymarket, contract-rules, resolution-source, btc]
---

# Summary

The Polymarket market page states that the contract resolves from the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 16, using the final Close price, and that the outcome is Yes only if that Close is higher than 72,000.

## Key facts extracted

- Current displayed market price for the 72,000 threshold outcome is about 84% Yes.
- The contract is not about spot BTC on other exchanges or BTC/USD broadly; it is specifically Binance BTC/USDT.
- The relevant observation is the final Close of the 1-minute candle for 12:00 in ET timezone on April 16.
- Price precision is determined by the Binance source display.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance... BTC/USDT... with \"1m\" and \"Candles\" selected."

## What is uncertain

- The market page is not itself the authoritative settlement source; it describes the governing source as Binance.
- The page does not independently verify whether Binance labels the relevant candle in ET or how the UI renders timezone versus UTC internally.

## Why this source may matter

This is the contract/rules surface that defines exactly what must happen for Yes to resolve and what source governs. It also gives the live market-implied probability that the market-implied persona must compare against.

## Possible impact on the question

This source matters because the case is date-sensitive and rule-sensitive: the correct question is not whether BTC is generally likely to remain above 72k, but whether the specific Binance BTC/USDT 12:00 ET 1-minute candle on April 16 closes above 72,000.

## Reliability notes

Useful and necessary for contract interpretation, but secondary to Binance itself for the underlying price data. Independence is low relative to the main market because it is the market operator's own rule page.