---
type: source_note
case_key: case-20260416-04100395
dispatch_id: dispatch-case-20260416-04100395-20260416T154804Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: market-structure
entity: ethereum
topic: case-20260416-04100395 | base-rate
question: Will the Binance ETH/USDT 12:00 ET one-minute candle on 2026-04-17 close above 2300?
driver: reliability
date_created: 2026-04-16
source_name: Polymarket market page and rules
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
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-04100395/researcher-analyses/2026-04-16/dispatch-case-20260416-04100395-20260416T154804Z/personas/base-rate.md]
tags: [source-note, polymarket, contract-rules, eth]
---

# Summary

This source establishes the governing contract mechanics and provides the market-implied baseline at the time of research.

## Key facts extracted

- The relevant market asks whether ETH will be above 2300 on April 17.
- The market page showed the 2300 line trading around 64-65% Yes during retrieval.
- Resolution is based on the Binance ETH/USDT 1-minute candle for 12:00 ET on April 17.
- The deciding field is the final candle "Close" price, which must be strictly higher than 2300.
- The market is about Binance ETH/USDT specifically, not other venues or pairs.

## Evidence directly stated by source

- Contract wording explicitly says Yes resolves only if the Binance ETH/USDT 12:00 ET 1-minute candle has a final Close above 2300.
- Precision is determined by the number of decimals in the source.

## What is uncertain

- The public web page is not itself the authoritative Binance candle record; it just points to the source of truth.
- The fetched page is a scraped representation and may not perfectly reflect live intraday order book state at every second.

## Why this source may matter

This is the direct contract/rules source for what counts. The wording makes timezone, exchange, pair, minute selection, and strict-greater-than logic all material.

## Possible impact on the question

It prevents overgeneralizing from ETH spot commentary on other exchanges. A close of exactly 2300.00 would still resolve No, and a move above 2300 at other times of day would not settle the market unless the specific noon ET Binance 1-minute close is above 2300.

## Reliability notes

Useful as the governing market source, but not independent evidence about the eventual price path. Should be paired with exchange or market-data context.