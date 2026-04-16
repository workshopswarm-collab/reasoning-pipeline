---
type: source_note
case_key: case-20260415-c8d6e83e
dispatch_id: dispatch-case-20260415-c8d6e83e-20260415T151858Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-c8d6e83e | market-implied
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close above 68000 on April 20, 2026?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules for Bitcoin above 68,000 on April 20
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: market-implied
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-c8d6e83e/researcher-analyses/2026-04-15/dispatch-case-20260415-c8d6e83e-20260415T151858Z/personas/market-implied.md]
tags: [polymarket, contract-rules, resolution-source, market-pricing]
---

# Summary

This source establishes both the market-implied baseline and the exact settlement mechanics. It shows the 68,000 contract trading around 95-96% Yes on April 15 and states that resolution depends specifically on the Binance BTC/USDT one-minute candle labeled 12:00 in ET on April 20, with the final Close needing to be strictly higher than 68,000.

## Key facts extracted

- The relevant outcome is "68,000" for April 20.
- The displayed market price is about 95% overall and specifically about 96 cents to buy Yes at the time fetched.
- The rule is strictly binary: Yes iff the Binance BTC/USDT 1-minute candle for 12:00 ET on April 20 has a final Close above 68,000.
- The governing source of truth is Binance, not another exchange or composite index.
- Price precision follows the Binance source decimals.

## Evidence directly stated by source

- Contract wording and resolution mechanics are explicit on the page.
- The page shows the market-implied probability directly through current share prices.
- The page explicitly warns that the relevant source is Binance BTC/USDT with 1m candles selected.

## What is uncertain

- The market page itself does not provide a historical audit trail for how the 95-96% price formed.
- The page does not itself prove Binance will remain available or unchanged at resolution time, though it names the intended source.

## Why this source may matter

This is the primary source for both contract interpretation and the live market prior. Because this is a date-specific and source-specific contract, using the exact resolution wording is essential.

## Possible impact on the question

The market is pricing a very high probability that BTC/USDT on Binance remains above 68,000 at ET noon on April 20. Any thesis against the market has to overcome both a large current spot cushion and the contract's narrow source-of-truth specification.

## Reliability notes

High reliability for contract wording and displayed price because this is the official market page. Lower reliability for broader explanatory FAQ text, which appears generic. The useful parts here are the rules and quoted market prices, not the marketing copy.