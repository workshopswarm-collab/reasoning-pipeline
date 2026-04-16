---
type: source_note
case_key: case-20260416-989964fe
dispatch_id: dispatch-case-20260416-989964fe-20260416T020418Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: market-structure
entity: ethereum
topic: case-20260416-989964fe | base-rate
question: Will the price of Ethereum be above $2,200 on April 17?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page and rules for 'Ethereum above ___ on April 17?'
source_type: market/rules page
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
downstream_uses: [qualitative-db/40-research/cases/case-20260416-989964fe/researcher-analyses/2026-04-16/dispatch-case-20260416-989964fe-20260416T020418Z/personas/base-rate.md]
tags: [polymarket, contract-rules, market-implied-probability, settlement-source]
---

# Summary

Polymarket's own market page provides the assigned market-implied probability snapshot and the contract wording that governs what must happen for the market to resolve Yes.

## Key facts extracted

- The market page shows the 2,200 threshold trading around 95% Yes / 6% No at fetch time.
- The market resolves Yes only if the Binance ETH/USDT 1-minute candle for 12:00 PM ET on April 17 has a final Close price strictly higher than 2200.
- The settlement source is Binance ETH/USDT with 1m candles selected.
- The page also shows adjacent ladder strikes: 2,100 near 99%, 2,300 near 72%, 2,400 near 30%.

## Evidence directly stated by source

- Exact contract condition and source-of-truth surface.
- Current market-implied probability snapshot.
- Precision note: price precision determined by Binance source decimals.

## What is uncertain

- The market page itself is not the settlement authority; Binance is.
- Web fetch captured a rendered snapshot, not a guaranteed live websocket state.
- The page does not itself prove where ETH will trade at noon ET on April 17.

## Why this source may matter

This is the clearest single source for the contract mechanics and current market pricing. It defines the exact event being forecast rather than a looser ETH spot question.

## Possible impact on the question

This source anchors both the comparison baseline (market at ~95%) and the operational interpretation that all of the following must hold for Yes: correct date, correct timezone, correct exchange, correct pair, correct 1-minute candle, and a final Close strictly above 2200.

## Reliability notes

Useful and necessary for contract interpretation, but only medium credibility for final settlement because the authoritative source of truth is externalized to Binance. Evidence independence is limited because the market-implied probability and the rules come from the same venue.