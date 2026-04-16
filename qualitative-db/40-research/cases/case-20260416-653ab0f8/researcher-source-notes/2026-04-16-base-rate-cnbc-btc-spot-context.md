---
type: source_note
case_key: case-20260416-653ab0f8
dispatch_id: dispatch-case-20260416-653ab0f8-20260416T090226Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: recent btc price context
driver: reliability
date_created: 2026-04-16
source_name: CNBC BTC.CM quote page
source_type: financial market data page
source_url: https://www.cnbc.com/quotes/BTC.CM=/
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [base-rate-finding]
tags: [btc-price, spot-context, threshold-distance]
---

# Summary

CNBC's BTC quote page showed Bitcoin trading materially above the 72,000 threshold on Apr 16, with an opening price around 75,063, day high around 75,441, day low around 74,495, and previous close around 74,977.

## Key facts extracted

- Open: 75,063.08
- Day high: 75,441.03
- Day low: 74,495.00
- Previous close: 74,976.85
- All reported levels were comfortably above 72,000.

## Evidence directly stated by source

- BTC spot context on Apr 16 was roughly mid-75k, not near the threshold.
- Intraday range shown was about 946 points from low to high.
- Distance from reported low to 72,000 was roughly 2,495 points.

## What is uncertain

- This is BTC/USD-style context, not the Binance BTC/USDT settlement source.
- The extract does not expose longer time-series or exact timestamp synchronization with the contract.

## Why this source may matter

It provides an independent contextual check that BTC was not hovering just above 72,000; it was several percent above. For a two-day horizon, that makes Yes more plausible than the raw contract wording alone would imply.

## Possible impact on the question

If BTC remains in a similar range, the market only needs price stability rather than a further rally. The key question becomes whether BTC can avoid a roughly 4%+ drawdown into the exact settlement minute.

## Reliability notes

Good for a quick independent spot context check. Not the settlement source, so it should not be used to resolve the market directly. Best used as contextual evidence paired with the Polymarket rule source and a direct Binance API or page check.