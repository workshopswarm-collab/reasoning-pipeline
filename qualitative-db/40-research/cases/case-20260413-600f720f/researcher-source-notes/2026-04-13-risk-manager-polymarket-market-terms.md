---
type: source_note
case_key: case-20260413-600f720f
dispatch_id: dispatch-case-20260413-600f720f-20260413T233138Z
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: markets
entity: btc
topic: will-bitcoin-reach-76k-april-13-19
question: Will Bitcoin reach $76,000 April 13-19?
date_created: 2026-04-13
source_name: Polymarket event page JSON
source_type: market contract / platform metadata
source_url: https://polymarket.com/event/what-price-will-bitcoin-hit-april-13-19
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-600f720f/researcher-analyses/2026-04-13/dispatch-case-20260413T233138Z/personas/risk-manager.md]
tags: [polymarket, contract-terms, source-of-truth, binance]
---

# Summary

This source is the Polymarket market metadata for the exact target contract. It supplies the market-implied probability, contract wording, and the governing resolution mechanics.

## Key facts extracted

- Target market slug: `will-bitcoin-reach-76k-april-13-19`.
- Question: `Will Bitcoin reach $76,000 April 13-19?`
- Outcome prices on retrieval: Yes `0.74`, No `0.26`; best bid `0.73`, best ask `0.75`, last trade `0.74`.
- Contract description states the market resolves Yes if **any Binance 1-minute candle for BTC/USDT** during **12:00 AM ET Apr 13 through 11:59 PM ET Apr 19** has a final **High** at or above $76,000.
- Resolution source is explicitly Binance BTC/USDT 1-minute chart highs.
- Contract says prices from other exchanges, different trading pairs, or other spot markets do **not** count.

## Evidence directly stated by source

- The relevant threshold is the Binance BTC/USDT **High**, not a daily close or another venue’s print.
- The event resolves immediately once a qualifying 1-minute high occurs within the date window.
- Market-implied probability at observation was roughly 74%.

## What is uncertain

- The Polymarket page JSON is platform metadata, not itself proof that Binance has or has not already printed $76,000.
- Page snapshots can move quickly; the probability and spread are time-sensitive.

## Why this source may matter

This is the clearest governing source for resolution mechanics. It sharply narrows what evidence matters: Binance 1-minute highs matter; Coinbase spot or Google Finance only matter as contextual proxies.

## Possible impact on the question

This source makes the key risk-management issue explicit: the contract is easier to hit than a close-based or cross-exchange interpretation, but still depends on a roughly 1.6% upside move from current spot-like levels near $74.8k. It also means disconfirming evidence should focus on path/time risk rather than close-vs-touch ambiguity.

## Reliability notes

High reliability for contract interpretation because it is the venue’s own market metadata for the exact contract. Independence is low versus the platform itself, so it must be paired with an external price source for actual market-state context.