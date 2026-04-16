---
type: source_note
case_key: case-20260416-04100395
dispatch_id: dispatch-case-20260416-04100395-20260416T154804Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: price-markets
entity: ethereum
topic: case-20260416-04100395 | risk-manager
question: Will the Binance ETH/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 2300?
driver: reliability
date_created: 2026-04-16
source_name: CoinGecko Ethereum market snapshot
source_type: market_data_aggregator
source_url: https://api.coingecko.com/api/v3/coins/ethereum
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: orchestrator
related_entities: [ethereum]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-04100395/researcher-analyses/2026-04-16/dispatch-case-20260416-04100395-20260416T154804Z/personas/risk-manager.md]
tags: [coingecko, contextual-source, eth-price]
---

# Summary

CoinGecko provided an independent contextual snapshot showing ETH around 2338.05 during the run, with approximately +8.0% over 7 days and +14.9% over 14 days. This does not settle the contract, but it supports the view that ETH entered the final pre-resolution day modestly above the 2300 threshold and with recent upward momentum rather than obvious acute weakness.

## Key facts extracted

- Current price (USD-equivalent context snapshot): 2338.05.
- 24h change: about +0.09%.
- 7d change: about +8.00%.
- 14d change: about +14.91%.
- Market cap rank: #2.

## Evidence directly stated by source

- CoinGecko directly reported Ethereum spot context and recent percentage performance windows.

## What is uncertain

- This is an aggregated market-data source, not the settlement source.
- CoinGecko’s price context does not guarantee the Binance ETH/USDT 12:00 ET 1-minute close tomorrow.
- Short-term crypto volatility can overwhelm benign multi-day trend context.

## Why this source may matter

It is a meaningfully independent contextual check against relying entirely on Binance data. It suggests the research run did not catch a Binance-specific outlier; broader market pricing also had ETH above the contract threshold.

## Possible impact on the question

This source mildly supports Yes by showing ETH broadly above 2300 going into the final day, but from a risk-manager perspective its main value is calibration: it reduces concern that current Binance spot is a one-exchange anomaly, while leaving intact the main tail risk that a single minute tomorrow can still close below 2300.

## Reliability notes

- Good for contextual price confirmation and recent trend framing.
- Not authoritative for settlement.
- More independent than a second Binance surface, but still ultimately derived from exchange market data rather than fundamental information.