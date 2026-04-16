---
type: source_note
case_key: case-20260415-48a4484b
dispatch_id: dispatch-case-20260415-48a4484b-20260415T180644Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: markets
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market rules / market state
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
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
downstream_uses: [qualitative-db/40-research/cases/case-20260415-48a4484b/researcher-analyses/2026-04-15/dispatch-case-20260415-48a4484b-20260415T180644Z/personas/variant-view.md]
tags: [polymarket, rules, market-implied-probability, binance, date-sensitive]
---

# Summary

Polymarket shows the 72,000 threshold outcome at about 94% and states that this market resolves from the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 16, using the final Close price.

## Key facts extracted

- The current market-implied probability for "above 72,000" is approximately 94%.
- The governing source of truth is not a daily BTC close and not a cross-exchange average; it is specifically the Binance BTC/USDT 1-minute candle for 12:00 ET on April 16.
- The market resolves Yes only if that candle's final Close is higher than 72,000.
- Price precision is whatever Binance displays in the source.

## Evidence directly stated by source

- Resolution depends on Binance BTC/USDT only.
- Resolution depends on the 1-minute candle at 12:00 ET.
- The operative field is the final Close.
- The listed market price for the 72,000 threshold was ~94% when checked.

## What is uncertain

- The public page itself is not the authoritative settlement source; it merely points to Binance.
- The page does not independently verify whether Binance charts are best interpreted in local timezone display or exchange/server time without user-side configuration.

## Why this source may matter

This source defines both the consensus baseline being challenged and the contract mechanics. For a date-sensitive, multi-condition market, those mechanics are materially important.

## Possible impact on the question

A trader can be directionally right on BTC staying strong overall and still lose if the noon ET Binance 1-minute Close prints below 72,000. That resolution narrowness is the main variant-view caution against a very high market probability.

## Reliability notes

Useful as the market's own rule statement and pricing snapshot, but settlement authority is downstream from Binance rather than Polymarket itself.