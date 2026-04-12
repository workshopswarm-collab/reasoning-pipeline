---
type: source_note
case_key: case-20260411-6669dcdb
dispatch_id: dispatch-case-20260411-6669dcdb-20260411T003353Z
analysis_date: 2026-04-10
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-11
question: Will the price of Bitcoin be above $72,000 on April 11?
driver: reliability
date_created: 2026-04-10
source_name: Polymarket event page and rules
source_type: market rule page
source_url: https://polymarket.com/event/bitcoin-above-on-april-11
source_date: 2026-04-10
credibility: medium-high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260411-6669dcdb/researcher-analyses/2026-04-11/dispatch-case-20260411-6669dcdb-20260411T003353Z/personas/base-rate.md]
tags: [polymarket, contract-rules, threshold-market]
---

# Summary

Polymarket states that this market resolves to Yes if the Binance `BTC/USDT` one-minute candle for `12:00` in the ET timezone on April 11 has a final close above 72,000. The event page also showed the 72k line trading at roughly 91%, materially above the assignment snapshot of 71.25%, highlighting that the market moved sharply upward by research time.

## Key facts extracted

- Governing rule: Binance one-minute candle for `BTC/USDT` at `12:00` ET on April 11.
- Settlement condition: final close must be strictly higher than 72,000.
- Venue specificity matters: Binance BTC/USDT, not another exchange or pair.
- Price precision is determined by Binance source decimals.
- On the fetched page, the 72k bracket was trading around 90.8% Yes.

## Evidence directly stated by source

- Exact settlement logic and source-of-truth venue.
- The binary threshold is a strict `>` comparison, not `>=`.
- The exchange pair and candle granularity are explicit.

## What is uncertain

- The event page is not itself the authoritative price feed; Binance is.
- The event page price may differ from the assignment snapshot because of later market movement.
- The rule text says `12:00 in the ET timezone`; interpreting the exact corresponding Binance UTC candle still requires a timezone conversion step.

## Why this source may matter

This source defines what counts. For a narrow crypto threshold market, the rule wording and source-of-truth interpretation are materially important.

## Possible impact on the question

The rule page supports a Yes-leaning baseline because the crowd price had moved very high by research time, but the more important contribution is clarifying that only the Binance BTCUSDT noon-ET one-minute close matters.

## Reliability notes

High relevance and reasonably high reliability for contract wording, but only medium-high as evidence for truth of the future outcome because market prices are consensus signals rather than settlement facts.
