---
type: source_note
case_key: case-20260415-fc70b9f6
dispatch_id: dispatch-case-20260415-fc70b9f6-20260415T072610Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page for Bitcoin above 72000 on April 16
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [market-implied-finding]
tags: [polymarket, contract-rules, market-implied, binance, btc]
---

# Summary

This source establishes both the live market-implied probability relevant to this assignment and the governing contract mechanics.

## Key facts extracted

- The assigned market outcome for "72,000" was trading around 85% on the fetched page, while assignment metadata listed current_price = 0.8.
- The market resolves Yes if the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 16 has a final Close price strictly higher than 72,000.
- The source of truth is Binance BTC/USDT with 1m candles selected.
- Other exchanges or other trading pairs do not govern settlement.
- Price precision is determined by the Binance source display.

## Evidence directly stated by source

Directly stated contract text says the market resolves to Yes if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the specified date has a final Close price higher than the listed threshold.

## What is uncertain

- The Polymarket page snapshot appears to show 85% while assignment metadata says current_price = 0.8; that looks like a minor live-market timing difference rather than a substantive contradiction.
- The fetched page is not itself the Binance candle; it is only the contract specification and market state.

## Why this source may matter

It is the clearest available contract and settlement-mechanics source, and therefore is mandatory for interpreting what conditions must all hold for a Yes resolution.

## Possible impact on the question

This source narrows the question to a date-specific Binance BTC/USDT 1-minute close at 12:00 ET on April 16. That makes timing, exchange-specific basis, and intraday volatility more important than broader end-of-day or cross-exchange BTC price summaries.

## Reliability notes

High reliability for contract wording and live market context because it is the market operator's own event page. It is not independent evidence about what tomorrow's Binance close will be.