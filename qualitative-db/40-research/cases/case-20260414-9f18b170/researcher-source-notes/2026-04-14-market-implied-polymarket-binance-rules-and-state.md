---
type: source_note
case_key: case-20260414-9f18b170
dispatch_id: dispatch-case-20260414-9f18b170-20260414T142057Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-9f18b170 | market-implied
question: Will Bitcoin reach $76,000 April 13-19?
date_created: 2026-04-14
source_name: Polymarket event page embedded market metadata
source_type: market page / embedded JSON
source_url: https://polymarket.com/event/what-price-will-bitcoin-hit-april-13-19
source_date: 2026-04-14
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-9f18b170/researcher-analyses/2026-04-14/dispatch-case-20260414-9f18b170-20260414T142057Z/personas/market-implied.md]
tags: [polymarket, bitcoin, resolution-rules, market-state]
---

# Summary

The Polymarket event page's embedded JSON exposes the exact resolution mechanics and current quoted probability for the specific $76,000 threshold contract.

## Key facts extracted

- Contract slug matched: `will-bitcoin-reach-76k-april-13-19`.
- Resolution rule on the page: the market resolves Yes if **any Binance 1-minute BTC/USDT candle** during Apr 13 00:00 ET through Apr 19 23:59 ET has a final **High** greater than or equal to 76,000.
- The page explicitly states the resolution source is Binance BTC/USDT with 1m candles.
- Embedded current outcome prices for the specific 76k threshold contract were `Yes 0.915 / No 0.085` at fetch time.
- Updated timestamp in embedded metadata was `2026-04-14T14:17:39.174846Z`.

## Evidence directly stated by source

- The governing source of truth is Binance BTC/USDT 1-minute candle highs, not a generic cross-exchange spot price average.
- The contract is a touch-style threshold market over a 7-day window, not a close-above market.
- Market state at observation time priced Yes at roughly 91.5%.

## What is uncertain

- The public page exposes current quoted prices but not the full order-book rationale.
- The page itself does not prove whether 76,000 has already printed; it only defines how that will be judged.

## Why this source may matter

This is the primary contract/rules source. For a date-specific threshold market, the exact trigger mechanics matter more than generic BTC commentary.

## Possible impact on the question

If Binance is already trading in the high 75.7k area early in the week, a 76k touch requirement over several remaining days can plausibly justify a very high Yes price.

## Reliability notes

High relevance and likely authoritative for contract wording, but only medium-high overall because it is still a market platform page rather than the underlying exchange print itself. It is best paired with direct Binance market data.