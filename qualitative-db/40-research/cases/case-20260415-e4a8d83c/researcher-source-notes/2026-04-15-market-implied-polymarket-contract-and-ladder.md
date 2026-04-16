---
type: source_note
case_key: case-20260415-e4a8d83c
dispatch_id: dispatch-case-20260415-e4a8d83c-20260415T230345Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-74k-on-april-17
question: Will the price of Bitcoin be above $74,000 on April 17?
driver: reliability
date_created: 2026-04-15
source_name: Polymarket market page and rule text
source_type: market contract / venue page
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-e4a8d83c/researcher-analyses/2026-04-15/dispatch-case-20260415-e4a8d83c-20260415T230345Z/personas/market-implied.md]
tags: [polymarket, contract-rules, threshold-market]
---

# Summary

The Polymarket page states the specific resolution mechanics and shows the cross-threshold ladder for April 17. The 74,000 line was trading about 72% yes at fetch time, while adjacent strikes were about 93% for 72,000 and 34% for 76,000.

## Key facts extracted

- Current market-implied probability for above 74,000 on April 17 was approximately 0.72.
- Adjacent thresholds were roughly:
  - above 72,000: 0.93
  - above 76,000: 0.34
- Contract resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17 has a final close price strictly higher than 74,000.
- Governing source of truth named by the contract is Binance, specifically the BTC/USDT chart with 1m candles selected.
- Precision is determined by the source decimals.

## Evidence directly stated by source

- Explicit rule text for threshold, timestamp, exchange, pair, and comparison operator.
- Live market pricing for the relevant 74,000 threshold and neighboring strikes.

## What is uncertain

- The fetched page is a venue page, not an independent external price source.
- Neighboring contracts are informative about the market-implied distribution but can share the same trader base and are not independent evidence.
- The page text does not itself show the eventual resolving candle print.

## Why this source may matter

This is the authoritative contract-definition source for what counts, including the date, timezone, exchange, pair, and the fact that the condition is strictly greater than 74,000 at the specific noon ET minute.

## Possible impact on the question

The adjacent-strike ladder suggests the market currently sees BTC most likely remaining in the low-to-mid 70k range by noon ET April 17, making 74,000 materially but not overwhelmingly likely. That supports a market-respecting prior near the quoted 72%.

## Reliability notes

High reliability for contract wording and the venue's own displayed odds. Low independence relative to the price forecast itself, since it is the market being analyzed rather than an outside check.