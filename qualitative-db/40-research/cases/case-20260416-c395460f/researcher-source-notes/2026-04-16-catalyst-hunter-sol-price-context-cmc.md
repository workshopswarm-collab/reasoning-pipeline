---
type: source_note
case_key: case-20260416-c395460f
dispatch_id: dispatch-case-20260416-c395460f-20260416T022702Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: token-market
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 12:00 ET 1-minute candle close above 80 on April 19, 2026?
driver: reliability
date_created: 2026-04-15
source_name: CoinMarketCap Solana page
source_type: market data / contextual secondary source
source_url: https://coinmarketcap.com/currencies/solana/
source_date: 2026-04-15
credibility: medium
recency: medium
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: orchestrator
related_entities: [sol, solana]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-c395460f/researcher-analyses/2026-04-16/dispatch-case-20260416-c395460f-20260416T022702Z/personas/catalyst-hunter.md]
tags: [source-note, sol, price-context, secondary-source]
---

# Summary

This source was used as a contextual check that SOL was trading in a regime where $80 is nearby rather than a distant outlier level. It is not the governing resolution source, but it helps assess whether the market's 89% Yes pricing is directionally sensible.

## Key facts extracted

- CoinMarketCap served a live Solana market page successfully during the run.
- The readable extraction was weak on exact quoted price, but it confirmed the page was the current Solana live-price surface rather than an archival article.
- The source remains useful only as a contextual secondary check, not a precise settlement reference.

## Evidence directly stated by source

- The page title identified it as "Solana price today, SOL to USD live price, marketcap and chart."
- The body extraction mainly returned static project background text rather than clean numerical spot data.

## What is uncertain

- Exact live price could not be cleanly extracted through the fetch tool.
- Because the extraction was noisy, this source adds only modest evidentiary weight.

## Why this source may matter

It helps verify that third-party market-data sites still present SOL as an actively traded live asset with charting support, but it does not by itself settle whether SOL will be above 80 at the exact Binance noon ET close.

## Possible impact on the question

Low-to-moderate. It modestly supports the view that the threshold is a normal spot-price question rather than an obscure or illiquid print problem, but it does not materially change the directional estimate.

## Reliability notes

Usable as contextual confirmation only. Independence from Polymarket is helpful, but extraction quality was poor, so this source should be downweighted relative to the contract page and any direct Binance check.