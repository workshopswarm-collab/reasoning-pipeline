---
type: source_note
case_key: case-20260415-10579f0a
dispatch_id: dispatch-case-20260415-10579f0a-20260415T184424Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-10579f0a | variant-view
question: Will the price of Bitcoin be above $70,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page and rules for bitcoin-above-on-april-17
source_type: market page / resolution rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: medium-high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, binance, usdt]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-10579f0a/researcher-analyses/2026-04-15/dispatch-case-20260415-10579f0a-20260415T184424Z/personas/variant-view.md]
tags: [polymarket, resolution-rules, binance, btcusdt, noon-et]
---

# Summary

This source established both the market-implied baseline and the operative contract mechanics. It shows the 70,000 strike trading around 97% Yes and states that resolution depends specifically on the Binance BTC/USDT 1-minute candle at 12:00 ET on April 17, using the final Close value.

## Key facts extracted

- The relevant strike is 70,000 for April 17, 2026.
- The market page showed the 70,000 line around 97% Yes at time of review, close to the assignment's `current_price` of 0.965.
- Resolution is not based on spot price at an arbitrary time or on another venue; it is based on the Binance BTC/USDT 1-minute candle for 12:00 ET.
- The deciding field is the final candle `Close` price, and it must be higher than 70,000.
- Price precision is determined by Binance source precision.

## Evidence directly stated by source

- Exact source of truth: Binance BTC/USDT chart with `1m` candles.
- Exact timing reference: 12:00 in ET timezone on the specified date.
- Exact win condition: final `Close` price higher than 70,000.

## What is uncertain

- The public event page is not itself the settlement source; it restates the rule.
- The page does not itself expose the eventual deciding candle value in advance.
- It does not clarify rare exchange outage or chart-display edge cases beyond naming Binance as source.

## Why this source may matter

This is the contract-definition surface. For a date-sensitive, source-specific market, the most important risk is often not broad BTC direction but contract interpretation drift. This source removes most ambiguity about venue, pair, time bucket, and condition.

## Possible impact on the question

It materially raises confidence that the correct analysis is: what is the chance Binance BTC/USDT final 12:00 ET 1-minute close on Apr 17 is >70,000, not whether BTC trades above 70k somewhere else or at some nearby time.

## Reliability notes

Reliable for contract wording and current market display, but not an authoritative independent price source. It should be paired with direct Binance data for verification.