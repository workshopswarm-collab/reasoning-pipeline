---
type: source_note
case_key: case-20260415-540d9abf
dispatch_id: dispatch-case-20260415-540d9abf-20260415T234706Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: solana
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 12:00 ET one-minute candle close above 80 on April 19, 2026?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/solana-above-on-april-19
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [sol]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-540d9abf/researcher-analyses/2026-04-15/dispatch-case-20260415-540d9abf-20260415T234706Z/personas/market-implied.md]
tags: [polymarket, contract-rules, resolution-source, binance, noon-et]
---

# Summary

This source establishes the governing contract mechanics and the current market-implied probability for the >80 strike. It is the direct source for how the market will resolve and what traders are currently pricing.

## Key facts extracted

- The relevant strike market is the Apr 19, 2026 noon ET SOL > 80 market.
- The Polymarket page showed the 80 strike at roughly 90% at fetch time.
- The contract resolves using the Binance SOL/USDT 1-minute candle for 12:00 in the ET timezone on Apr 19.
- The resolution condition is the final candle close being higher than 80; otherwise No.
- The page explicitly says this is Binance SOL/USDT only, not other exchanges or pairs.
- The page says price precision is determined by the number of decimal places in the source.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for SOL/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- "The resolution source for this market is Binance, specifically the SOL/USDT 'Close' prices currently available at https://www.binance.com/en/trade/SOL_USDT with '1m' and 'Candles' selected on the top bar."
- "Please note that this market is about the price according to Binance SOL/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The Polymarket web page is a useful rule surface but not itself the ultimate settlement source; settlement still points outward to Binance.
- The page does not itself explain the ET-to-Binance timestamp mapping in API terms, so that mapping requires interpretation/verification.
- The displayed probability can move after fetch time.

## Why this source may matter

This is the clearest source for the market-implied baseline and for the exact multi-condition contract logic. It defines what has to be true for Yes: correct exchange, correct pair, correct one-minute interval, correct ET time, and a close strictly above 80.

## Possible impact on the question

The contract wording materially lowers ambiguity: this is not "roughly above 80 sometime that day" but a single narrow Binance one-minute close at noon ET on Apr 19. That makes date/time mapping and exchange-specific pricing central to the analysis.

## Reliability notes

Useful and likely authoritative for contract wording, but still not the final source of truth for the resolved price print itself; Binance is.