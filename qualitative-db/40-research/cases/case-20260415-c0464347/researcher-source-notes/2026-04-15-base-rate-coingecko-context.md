---
type: source_note
case_key: case-20260415-c0464347
dispatch_id: dispatch-case-20260415-c0464347-20260415T011958Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: btc-usdt-price-level-into-april-20
driver: reliability
date_created: 2026-04-15
source_name: CoinGecko Bitcoin market snapshot
source_type: secondary_market_data
source_url: https://api.coingecko.com/api/v3/coins/bitcoin
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [source-note, coingecko, bitcoin, contextual-source]
---

# Summary

CoinGecko provides an independent contextual cross-check that Bitcoin is trading around the mid-74k area and has been positive over 7-, 14-, and 30-day windows.

## Key facts extracted

- CoinGecko returned Bitcoin USD price around `74717` during this run.
- Reported 7-day performance was about `+3.81%`.
- Reported 14-day performance was about `+9.51%`.
- Reported 30-day performance was about `+2.63%`.
- CoinGecko lists Bitcoin market-cap rank `#1`, consistent with deep liquidity and lower single-venue dislocation risk than thinner crypto assets.

## Evidence directly stated by source

- Current cross-venue reference price is in the same range as Binance spot.
- Recent multi-week momentum has been positive, not collapsing.

## What is uncertain

- CoinGecko is not the settlement source.
- Its aggregate/reference price can differ from Binance at the exact settlement minute.
- Positive trailing performance does not guarantee price persistence through Apr. 20.

## Why this source may matter

It is a meaningfully independent contextual source confirming that the Binance observation is not obviously a one-venue anomaly.

## Possible impact on the question

The cross-check supports a high Yes view and weakens the case for a sudden venue-specific or stale-data explanation for Binance trading above 70k.

## Reliability notes

Useful as an independent contextual source, but secondary to Binance because the contract is explicitly exchange-specific.