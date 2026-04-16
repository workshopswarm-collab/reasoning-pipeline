---
type: source_note
case_key: case-20260416-cd7fa6c7
dispatch_id: dispatch-case-20260416-cd7fa6c7-20260416T010113Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-74k-on-april-17
question: Will the price of Bitcoin be above $74,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules page for Bitcoin above on April 17
source_type: market rules / resolution source reference
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-cd7fa6c7/researcher-analyses/2026-04-16/dispatch-case-20260416-cd7fa6c7-20260416T010113Z/personas/catalyst-hunter.md]
tags: [polymarket, binance, resolution, noon-et]
---

# Summary

This source defines the governing resolution mechanics. It says the market resolves from the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 17, using the final Close price, and that the threshold comparison is strictly whether that close is higher than $74,000.

## Key facts extracted

- Resolution is based on Binance BTC/USDT, not other exchanges or pairs.
- The relevant interval is the 1-minute candle for 12:00 in ET timezone on April 17.
- The deciding field is the candle's final Close price.
- "Higher than" $74,000 means equality would still resolve No.
- Price precision is whatever Binance displays in the source.

## Evidence directly stated by source

The market page states: "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."

## What is uncertain

- The public rules page points to the Binance trading interface rather than a stable API endpoint, so later verification may still require mapping the noon ET candle to Binance timestamps carefully.
- The page itself does not clarify edge handling for delayed Binance UI updates, though the rule language strongly implies the final stored candle close is controlling.

## Why this source may matter

This is the governing source-of-truth surface for contract interpretation. For a narrow date-specific crypto close market, resolution mechanics materially affect the answer because exchange, pair, minute selection, timezone conversion, and strict threshold logic all matter.

## Possible impact on the question

It narrows the practical forecast to one specific Binance minute close at noon ET on April 17. That makes near-term price path and overnight-to-morning catalysts more important than broad medium-term Bitcoin direction.

## Reliability notes

Primary for contract wording, but not primary for the actual final price print itself. It is reliable for how the market will be judged; Binance is still the operative source for the price observation.