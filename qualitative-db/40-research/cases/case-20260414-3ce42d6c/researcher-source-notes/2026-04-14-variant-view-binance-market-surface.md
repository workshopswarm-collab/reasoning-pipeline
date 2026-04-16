---
type: source_note
case_key: case-20260414-3ce42d6c
dispatch_id: dispatch-case-20260414-3ce42d6c-20260414T130958Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-14
question: Will the Binance BTC/USDT 1-minute candle for 2026-04-14 12:00 ET close above 70000?
driver: reliability
date_created: 2026-04-14
source_name: Binance public product/market surface for BTCUSDT
source_type: exchange market data surface
source_url: https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-products?includeEtf=true
source_date: 2026-04-14
credibility: high
recency: current
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [variant-view.md]
tags: [binance, btcusdt, exchange-surface, contextual]
---

# Summary

This source verified that Binance's public market surface showed BTCUSDT actively trading on the assignment date with a spot price well above 70,000.

## Key facts extracted

- Binance public product data included BTCUSDT in TRADING status.
- The same surface showed BTCUSDT last price (`c`) at 74544.71.
- Daily range values on the same surface were also entirely above 70,000 (low 70818.57, high 74924.64 in the fetched snapshot).
- This is contextual confirmation that BTC was not merely slightly above the strike; it was materially above it during the research window.

## Evidence directly stated by source

- Symbol: BTCUSDT.
- Status: TRADING.
- Last price field c: 74544.71.
- Low field l: 70818.57.

## What is uncertain

- This is not the exact noon-ET 1-minute settlement candle requested by the contract.
- The field snapshot is a current market surface, not a dedicated historical 1-minute archive.
- Binance API/historical endpoints queried separately did not provide the future candle directly in this environment, so the exact resolving candle remained unconfirmed from this surface alone.

## Why this source may matter

It materially strengthens the base case by showing BTCUSDT trading comfortably above 70,000 on the relevant date and reduces the plausibility of a hidden near-threshold risk.

## Possible impact on the question

Unless there is an exchange-specific settlement anomaly or a sharp intraminute move into the exact noon ET minute, this surface supports a Yes outcome.

## Reliability notes

High credibility as a Binance-operated market-data surface. Independence from Polymarket is high enough to count as a meaningful additional verification pass, but it is still not the exact source-of-truth candle required for final settlement.