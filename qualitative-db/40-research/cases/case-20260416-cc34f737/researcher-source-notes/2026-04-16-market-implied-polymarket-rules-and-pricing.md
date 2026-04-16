---
type: source_note
case_key: case-20260416-cc34f737
dispatch_id: dispatch-case-20260416-cc34f737-20260416T162722Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: prediction-markets
entity: ethereum
topic: case-20260416-cc34f737 | market-implied
question: Will the price of Ethereum be above $2,300 on April 17?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page and rules for Ethereum above $2,300 on April 17
source_type: market page / contract rules
source_url: https://polymarket.com/event/ethereum-above-on-april-17
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [ethereum]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [market-implied-finding]
tags: [polymarket, resolution-rules, market-price, source-note]
---

# Summary

This source establishes both the current market-implied baseline and the contract mechanics. On the fetched page, the `2,300` threshold traded around 71%, implying the market currently prices ETH/USDT as more likely than not to close above 2300 on Binance's 12:00 ET one-minute candle on April 17.

## Key facts extracted

- The relevant contract is the `2,300` line inside Polymarket's `Ethereum above ___ on April 17?` market.
- The displayed probability for `2,300` was about `71%` / `71¢` at fetch time.
- Resolution is not based on spot price at arbitrary times, daily close, or other exchanges.
- The contract resolves from the Binance `ETH/USDT` `1m` candle for `12:00` in the ET timezone on April 17.
- The winning condition is that the final Binance candle `Close` price must be strictly higher than `2300`.
- Price precision is determined by Binance's displayed decimal precision.

## Evidence directly stated by source

- The market itself prices `2,300` at roughly 71%.
- The rules explicitly name Binance `ETH/USDT` and the `1m` candle at `12:00` ET as the source of truth.
- The rules explicitly require the final `Close` to be higher than the threshold.

## What is uncertain

- The market page is a live interface and can move quickly.
- The page does not itself prove Binance availability or absence of later settlement quirks beyond the visible rules text.

## Why this source may matter

This is the primary contract and price source, so it is necessary for both the market-implied baseline and the resolution-logic audit.

## Possible impact on the question

It sets a relatively bullish prior: with ETH around the low-to-mid 2330s on April 16, the market appears to assume only modest downside over the next ~20 hours is needed to fail, so a >50% yes price is understandable.

## Reliability notes

Strong for contract wording and current displayed odds, but not independent for price validation. It is authoritative for the market's own rules, not for the eventual Binance print itself.