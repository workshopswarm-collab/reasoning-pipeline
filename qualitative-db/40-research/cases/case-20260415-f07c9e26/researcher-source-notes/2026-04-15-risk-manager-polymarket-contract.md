---
type: source_note
case_key: case-20260415-f07c9e26
dispatch_id: dispatch-case-20260415-f07c9e26-20260415T013036Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-f07c9e26 | risk-manager
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market rules page
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-f07c9e26/researcher-analyses/2026-04-15/dispatch-case-20260415-f07c9e26-20260415T013036Z/personas/risk-manager.md]
tags: [polymarket, contract, rules, source-note]
---

# Summary

This source note captures the explicit contract wording and the contemporaneous market-implied probability from the Polymarket market page.

## Key facts extracted

- The relevant outcome is the 72,000 threshold for April 16.
- The Polymarket page displayed approximately `91%` for the 72,000 outcome at collection time, matching the assignment field `current_price: 0.905` to rounding.
- The rules state the market resolves to Yes if the Binance BTC/USDT 1-minute candle for `12:00` in the ET timezone on the specified date has a final close price higher than 72,000.
- The rules explicitly say the source is Binance BTC/USDT with `1m` and `Candles` selected.
- The rules explicitly exclude other exchanges and other trading pairs.
- Price precision is determined by the number of decimal places in the source.

## Evidence directly stated by source

- The market-implied probability from active trading is about 90.5%.
- The governing resolution mechanics are a single-minute, single-exchange, single-pair close-price test.

## What is uncertain

- The page text does not separately explain edge cases such as UI/data revisions, exchange disruptions, or how Polymarket would handle any Binance display anomaly.
- The page is a market/rules surface, not the exchange source itself.

## Why this source may matter

This is the binding contract-definition surface for what counts, which matters because the market is date-specific and mechanically narrow.

## Possible impact on the question

The rules materially narrow the claim: all of the following must hold for a Yes view to be right under the contract: Binance BTC/USDT remains the relevant source, the noon ET 1-minute candle exists and is the operative settlement candle, and that candle's final close is strictly greater than 72,000.

## Reliability notes

High relevance because this page defines the contract, but medium-high rather than fully authoritative on the final price because Binance is the named source of truth for settlement data.