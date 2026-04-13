---
type: source_note
case_key: case-20260413-c5cf1f36
dispatch_id: dispatch-case-20260413-c5cf1f36-20260413T181345Z
analysis_date: 2026-04-13
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260413-c5cf1f36 | base-rate
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-15 close above 66000?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket event page and rules for Bitcoin above ___ on April 15
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-15
source_date: 2026-04-13
credibility: medium-high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-c5cf1f36/researcher-analyses/2026-04-13/dispatch-case-20260413-c5cf1f36-20260413T181345Z/personas/base-rate.md]
tags: [polymarket, contract-rules, settlement-source, market-implied-probability]
---

# Summary

This source establishes the governing contract language, current market-implied pricing, and the exact settlement mechanics for the April 15 BTC threshold market.

## Key facts extracted

- The relevant threshold for this lane is 66,000.
- The page showed the 66,000 contract trading around 99% / 99.1% Yes at fetch time, consistent with the assignment `current_price` of 0.9595 being an extreme-probability market.
- The market resolves to Yes only if the Binance BTC/USDT 1-minute candle for **12:00 ET** on April 15 has a final **Close** price **higher than** 66,000.
- The settlement source is Binance BTC/USDT specifically, not a broader BTC index and not another exchange.
- Precision is governed by Binance source decimals.

## Evidence directly stated by source

- Resolution depends on the Binance BTC/USDT 12:00 ET 1-minute candle close.
- The condition is strictly above 66,000, not at-or-above.
- The event page is the direct source for current market pricing and displayed threshold ladder.

## What is uncertain

- The event page itself is not the final settlement print; it only states the intended source-of-truth and current market odds.
- The page does not itself provide the April 15 noon ET close because that observation is in the future.

## Why this source may matter

It is the primary source for interpreting what exactly must happen for the contract to resolve Yes and for identifying market-implied probability.

## Possible impact on the question

This source sharply narrows the relevant uncertainty: the question is not whether BTC is generally strong, but whether Binance BTC/USDT remains above 66,000 specifically at the noon ET minute close on April 15.

## Reliability notes

- Strong for contract wording and current market state.
- Not sufficient alone for forecast confidence because it is not an independent price source and cannot directly settle a future observation yet.
- Important operational caveat: narrow timing and single-exchange settlement create some basis / microstructure risk even when broader BTC spot is comfortably above 66,000.
