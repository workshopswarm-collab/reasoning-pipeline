---
type: source_note
case_key: case-20260414-d1f59d32
dispatch_id: dispatch-case-20260414-d1f59d32-20260414T144613Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-d1f59d32 | risk-manager
question: Will the price of Bitcoin be above $74,000 on April 15?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules for bitcoin-above-on-april-15
source_type: market_rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-15
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-d1f59d32/researcher-analyses/2026-04-14/dispatch-case-20260414-d1f59d32-20260414T144613Z/personas/risk-manager.md]
tags: [polymarket, resolution-rules, binance, btcusdt, date-sensitive]
---

# Summary

This source establishes the governing contract mechanics for the case. The market resolves based on the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 15, 2026, using the final close price for that minute. The threshold test is strictly whether that close is higher than 74,000.

## Key facts extracted

- Resolution is tied to Binance, not a cross-exchange composite or another venue.
- The relevant instrument is BTC/USDT, not BTC/USD.
- The relevant observation is the final close of the 1-minute candle for 12:00 ET on April 15, 2026.
- The outcome is Yes only if that close is higher than 74,000.
- Price precision follows Binance source precision.
- The market page showed the 74,000 line trading around 83% at capture time.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices currently available at https://www.binance.com/en/trade/BTC_USDT with \"1m\" and \"Candles\" selected on the top bar."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The market page does not itself provide the future April 15 noon ET candle value; it only defines the settlement mechanism.
- It does not explain how daylight saving or exchange UI labeling issues might appear operationally, so timezone handling still deserves explicit attention.

## Why this source may matter

This is the governing source of truth for settlement and therefore determines which evidence classes matter. It also creates the main operational-risk angle: a highly specific one-minute ET timestamp on a single venue can resolve differently from broader market impressions or other exchange prices.

## Possible impact on the question

This source narrows the actual question from "will BTC generally stay above 74k" to "will Binance BTC/USDT print a >74,000 close exactly at noon ET tomorrow." That lowers confidence versus a looser daily-close interpretation and makes timing/path risk material.

## Reliability notes

High reliability for contract interpretation because it is the market’s own rule text. Low direct evidentiary value for the actual future price outcome beyond clarifying the conditions that must all hold.