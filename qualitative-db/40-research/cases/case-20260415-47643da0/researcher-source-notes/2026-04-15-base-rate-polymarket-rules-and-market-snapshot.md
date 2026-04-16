---
type: source_note
case_key: case-20260415-47643da0
dispatch_id: dispatch-case-20260415-47643da0-20260415T010752Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-47643da0/researcher-analyses/2026-04-15/dispatch-case-20260415-47643da0-20260415T010752Z/personas/base-rate.md]
tags: [polymarket, contract-rules, market-implied-probability]
---

# Summary

Polymarket's event page gives the live market-implied probability for the $72,000 threshold and the operative contract mechanics. For this contract, the relevant event is not a daily close or a cross-exchange average; it is the final close of the Binance BTC/USDT 1-minute candle labeled 12:00 PM ET on April 17, 2026.

## Key facts extracted

- The market title is "Bitcoin above ___ on April 17?" with a listed Apr 17, 2026 date.
- The $72,000 line was trading around 85¢ yes / 17¢ no when fetched, implying roughly 84-85% market probability for above $72,000.
- The contract resolves YES if the Binance BTC/USDT 1-minute candle for 12:00 in the ET timezone on Apr 17 has a final close price higher than $72,000.
- Otherwise it resolves NO.
- Resolution source is Binance BTC/USDT with 1m candles selected.
- Price precision is determined by the source.

## Evidence directly stated by source

- Direct contract wording specifying Binance BTC/USDT as source of truth.
- Direct timing condition specifying 12:00 PM ET.
- Direct condition that the relevant value is the final "Close" of the 1-minute candle, not intraminute high or some other exchange print.
- Direct market snapshot showing implied probability near 84-85% for the $72,000 threshold.

## What is uncertain

- The event page itself is not the authoritative settlement record; it points to Binance as the governing source.
- Page prices can move quickly, so the implied probability is a snapshot rather than a stable reference.
- The page wording says "12:00 in the ET timezone" but does not independently explain Binance's candle timestamp conventions, so a separate timing interpretation check remains useful.

## Why this source may matter

It defines the contract mechanics and gives the market baseline the analysis must compare against.

## Possible impact on the question

This source makes clear that the question is effectively: will Binance BTC/USDT still be above $72,000 at exactly the noon ET 1-minute close on Apr 17? That tends to support a high YES baseline when spot is already materially above $72,000, but it also means a short-lived dip at the exact minute can still flip the outcome.

## Reliability notes

Useful for contract interpretation and market baseline, but not sufficient alone for settlement certainty because Binance is the governing source of truth.