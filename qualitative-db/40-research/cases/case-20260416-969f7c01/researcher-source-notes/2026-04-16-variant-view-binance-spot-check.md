---
type: source_note
case_key: case-20260416-969f7c01
dispatch_id: dispatch-case-20260416-969f7c01-20260416T013210Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: spot-market-structure
entity: ethereum
topic: case-20260416-969f7c01 | variant-view
question: Will the price of Ethereum be above $2,200 on April 17?
driver: reliability
date_created: 2026-04-15
source_name: Binance ETHUSDT ticker API spot check
source_type: exchange primary data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [ethereum]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [variant-view finding, evidence map]
tags: [binance, ethusdt, spot, price]
---

# Summary

A direct Binance spot check returned ETHUSDT at 2352.52 during this run, placing spot roughly 6.9% above the 2200 strike with less than one day remaining before the noon ET resolution minute.

## Key facts extracted

- Binance API response during the run: {"symbol":"ETHUSDT","price":"2352.52000000"}
- Absolute cushion over strike: about $152.52.
- Percentage cushion over strike: about 6.9%.
- Time to event is short relative to the size of the cushion.

## Evidence directly stated by source

- The returned Binance spot price was 2352.52 for ETHUSDT.

## What is uncertain

- This is not the exact future resolution candle; it is a current spot check.
- Ticker price is not the same object as the specific final close of the 12:00 ET one-minute candle on April 17.
- Crypto can move materially in 24 hours, so current cushion is informative but not dispositive.

## Why this source may matter

It is the closest primary exchange-specific reference to the contract's source of truth available before settlement. It directly tests whether the strike is already deeply in the money or still near the margin.

## Possible impact on the question

The large current cushion supports a Yes lean, but it also clarifies the variant thesis: if there is disagreement with the 95% market price, it should come from residual one-day volatility and exact-minute resolution risk rather than from a broad bearish ETH thesis.

## Reliability notes

High reliability for current exchange-specific spot state. Limited as a forecast because it is not yet the settlement candle and crypto intraday volatility remains meaningful.