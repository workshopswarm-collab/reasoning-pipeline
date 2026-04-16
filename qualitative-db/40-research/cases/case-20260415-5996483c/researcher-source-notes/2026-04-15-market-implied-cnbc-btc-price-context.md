---
type: source_note
case_key: case-20260415-5996483c
dispatch_id: dispatch-case-20260415-5996483c-20260415T193222Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-20 close above 70000?
driver: reliability
date_created: 2026-04-15
source_name: CNBC BTC.CM quote snapshot
source_type: market_data_context
source_url: https://www.cnbc.com/quotes/BTC.CM=
source_date: 2026-04-15
credibility: medium
recency: high
stance: supportive
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-5996483c/researcher-analyses/2026-04-15/dispatch-case-20260415-5996483c-20260415T193222Z/personas/market-implied.md
tags: [btc, price-context, threshold-distance]
---

# Summary

This source provides an independent contextual BTC/USD price snapshot showing Bitcoin comfortably above 70,000 on Apr 15, several days before the settlement window.

## Key facts extracted

- Open: `74,307.99`
- Day high: `74,898.00`
- Day low: `73,567.41`
- Previous close: `74,255.51`
- All quoted levels are materially above the 70,000 contract threshold.

## Evidence directly stated by source

- "Open 74,307.99"
- "Day High 74,898.00"
- "Day Low 73,567.41"
- "Prev Close 74,255.51"

## What is uncertain

- CNBC’s quote is not the governing settlement source; it is contextual BTC/USD reference data.
- It does not prove where Binance BTC/USDT will print at exactly 12:00 ET on Apr 20.
- It also does not isolate exchange-specific basis or microstructure effects.

## Why this source may matter

It shows that the market’s high Yes price is not obviously detached from broad spot context. BTC appears to be trading roughly 5%+ above the threshold with several days left, making the current market price directionally plausible.

## Possible impact on the question

This source supports the market’s optimistic stance by showing that BTC already has a sizable buffer above 70,000. It mainly informs whether the market’s extreme probability is broadly reasonable, not whether the exact settlement candle is already assured.

## Reliability notes

Useful independent contextual source with strong recency, but not authoritative for settlement. Best used as a secondary cross-check on threshold distance and market reasonableness.