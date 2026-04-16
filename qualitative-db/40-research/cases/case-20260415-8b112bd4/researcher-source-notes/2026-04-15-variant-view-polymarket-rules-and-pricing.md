---
type: source_note
case_key: case-20260415-8b112bd4
dispatch_id: dispatch-case-20260415-8b112bd4-20260415T153012Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-16 close above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules for bitcoin-above-on-april-16
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: medium
recency: current
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-8b112bd4/researcher-analyses/2026-04-15/dispatch-case-20260415-8b112bd4-20260415T153012Z/personas/variant-view.md]
tags: [polymarket, contract-rules, pricing, binance, resolution-source]
---

# Summary

Polymarket’s market page shows the 70,000 threshold trading around 98.6% Yes / 1.5% No and specifies a narrow settlement condition: the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 16, 2026 must have a final Close above 70,000.

## Key facts extracted

- The relevant market is the Apr 16, 2026 noon ET contract, not a daily close or end-of-day average.
- The 70,000 line was showing roughly 99% / specifically 98.6% Yes at time of fetch.
- Resolution source is Binance BTC/USDT with 1m candles selected.
- The deciding value is the candle’s final Close price, not intraminute high/low.
- Price precision follows the source’s displayed decimal precision.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- "The resolution source for this market is Binance... BTC/USDT ... with '1m' and 'Candles' selected on the top bar."

## What is uncertain

- The fetched page is a rendered public market page, not an immutable rules document export.
- The public page does not itself prove how Binance labels the relevant candle in ambiguous UI edge cases, so exchange/API cross-checking matters.

## Why this source may matter

This is the governing contract source for what counts. It defines the exact timing, exchange, pair, and price field to be used and therefore frames the whole probability question.

## Possible impact on the question

This source strongly favors Yes only if Binance BTC/USDT remains above 70,000 specifically at 12:00 ET on Apr 16. It also creates a nontrivial operational/rule edge: being well above 70,000 now is not alone sufficient if a sharp drawdown occurs before the exact one-minute settlement candle.

## Reliability notes

The market page is authoritative for Polymarket contract wording but not independent evidence about BTC price itself. It should be paired with Binance exchange/API checks for resolution mechanics and current price context.