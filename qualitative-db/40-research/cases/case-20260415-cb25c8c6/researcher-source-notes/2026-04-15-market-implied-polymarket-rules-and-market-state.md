---
type: source_note
case_key: case-20260415-cb25c8c6
dispatch_id: dispatch-case-20260415-cb25c8c6-20260415T194743Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68k-on-april-19
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-19 be above 68000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page and rules surface
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-19
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-cb25c8c6/researcher-analyses/2026-04-15/dispatch-case-20260415-cb25c8c6-20260415T194743Z/personas/market-implied.md]
tags: [polymarket, contract-rules, market-pricing, binance]
---

# Summary

Polymarket shows the Apr 19 BTC threshold ladder and lists the 68,000 outcome at roughly 98.6% Yes at fetch time. The rules specify the contract resolves from the Binance BTC/USDT 1-minute candle for 12:00 ET on Apr 19, using the final Close price; resolution is exchange-specific and pair-specific.

## Key facts extracted

- The relevant outcome is the 68,000 threshold for Apr 19, 2026.
- The displayed Yes price for 68,000 was 98.6 cents on the fetched page, consistent with the assignment's current_price 0.9805.
- The market resolves Yes only if the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on Apr 19 has a final Close strictly higher than 68,000.
- Other exchanges or trading pairs do not govern settlement.
- Price precision is whatever Binance displays on the source surface.

## Evidence directly stated by source

- The governing source of truth is Binance BTC/USDT with 1m candles selected.
- The relevant time window is explicitly 12:00 ET on the date in the title.
- The operator page displays the market-implied probability near 98% for the 68,000 threshold.

## What is uncertain

- The fetched Polymarket page is a rendered public surface rather than a signed API response.
- The page does not itself prove what Binance will print at settlement; it only defines the settlement mechanism and current crowd pricing.

## Why this source may matter

This is the direct contract/rules surface, so it is authoritative for how the question should be interpreted even though it is not authoritative for the future settlement value itself.

## Possible impact on the question

It strongly supports taking the question as a narrow, exchange-specific, time-specific settlement problem rather than a vague "BTC above 68k sometime that day" question. It also shows the market is already pricing the event as very likely.

## Reliability notes

High reliability for contract mechanics and displayed market price. Not sufficient alone for the actual BTC level on Apr 19, so independent spot verification remains necessary.