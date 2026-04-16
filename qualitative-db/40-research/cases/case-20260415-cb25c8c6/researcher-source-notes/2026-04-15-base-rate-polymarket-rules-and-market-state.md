---
type: source_note
case_key: case-20260415-cb25c8c6
dispatch_id: dispatch-case-20260415-cb25c8c6-20260415T194743Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68k-on-april-19
question: Will the price of Bitcoin be above $68,000 on April 19?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page and rules for Bitcoin above $68,000 on April 19
source_type: market/rules page
source_url: https://polymarket.com/event/bitcoin-above-on-april-19
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-cb25c8c6/researcher-analyses/2026-04-15/dispatch-case-20260415-cb25c8c6-20260415T194743Z/personas/base-rate.md]
tags: [polymarket, rules, resolution, btc, binance]
---

# Summary

This source establishes both the current market-implied probability and the contract mechanics. The market page showed the $68,000 line trading around 98.6% Yes on 2026-04-15, while the rules specify that resolution depends on the Binance BTC/USDT 1-minute candle for 12:00 ET on April 19 and specifically the final Close price of that candle.

## Key facts extracted

- The relevant threshold market was trading about 98.6% Yes.
- The contract resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 19 has a final Close price strictly higher than 68,000.
- The market is tied to Binance BTC/USDT, not another exchange or BTC/USD pair.
- Price precision is determined by the number of decimals shown by the source.

## Evidence directly stated by source

Direct rule text from the page states that resolution is based on the Binance BTC/USDT "Close" price with "1m" and "Candles" selected, for 12:00 in the ET timezone on the specified date.

## What is uncertain

- The fetched page is a web rendering of Polymarket content, not an official downloadable contract spec.
- The page does not itself prove what the April 19 noon candle will be; it only clarifies the settlement mechanism and current market pricing.
- Cross-market structure suggests these are grouped ladder markets, but that matters less than the direct rule text for this specific line.

## Why this source may matter

It is the governing context for the contract. Without the exact settlement rule, it would be easy to overgeneralize from spot BTC/USD levels on other venues or from end-of-day prices instead of the single Binance 1-minute close that actually determines payout.

## Possible impact on the question

High. This source determines what conditions must all hold for Yes: (1) the relevant candle must be the Binance BTC/USDT 12:00 ET 1-minute candle on April 19, (2) the final Close from that candle must be used, and (3) that close must be greater than 68,000.

## Reliability notes

Useful as the direct market/rules surface, but not independent evidence about Bitcoin price itself. It is authoritative for market wording, not for current or future BTC level.