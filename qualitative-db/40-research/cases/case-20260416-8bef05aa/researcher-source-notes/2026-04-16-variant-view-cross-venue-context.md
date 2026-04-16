---
type: source_note
case_key: case-20260416-8bef05aa
dispatch_id: dispatch-case-20260416-8bef05aa-20260416T144205Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: bitcoin-threshold-daily-close
entity: btc
topic: Cross-venue BTC spot context around the 72k threshold
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-21 be above 72000?
driver: reliability
date_created: 2026-04-16
source_name: Coinbase ticker and CoinGecko spot reference
source_type: contextual_market_data
source_url: https://api.exchange.coinbase.com/products/BTC-USD/ticker ; https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-8bef05aa/researcher-analyses/2026-04-16/dispatch-case-20260416-8bef05aa-20260416T144205Z/personas/variant-view.md]
tags: [source-note, coinbase, coingecko, cross-check, btc]
---

# Summary

This note captures an independent contextual cross-check that BTC was trading materially above 72,000 around research time, reducing concern that the Binance print was an outlier.

## Key facts extracted

- Coinbase BTC-USD ticker showed about 73,991.88 at 2026-04-16T14:44:00Z.
- CoinGecko simple price endpoint showed bitcoin at about 73,893 USD.
- These levels were close to Binance BTCUSDT around 73,982, suggesting no major venue divergence at collection time.

## Evidence directly stated by source

- BTC was near 73.9k across multiple widely used market data surfaces.

## What is uncertain

- These are not the governing resolution source.
- Cross-venue alignment now does not imply Binance noon ET close on April 21 will remain above 72,000.

## Why this source may matter

It supports the contextual claim that BTC is presently not barely above the line by exchange-specific accident; it is broadly trading ~2.6%-2.8% above the threshold.

## Possible impact on the question

This raises the baseline chance of a Yes outcome versus a world where BTC were already below or exactly at the threshold, but it should not be over-weighted because the contract cares about a specific future minute close.

## Reliability notes

- Coinbase and CoinGecko are credible contextual sources.
- Independence is medium: they are distinct from Binance and from Polymarket, but still all reflect the same underlying BTC market.
- Good as a verification pass, not as the governing source.
