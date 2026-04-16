---
type: source_note
case_key: case-20260416-04100395
dispatch_id: dispatch-case-20260416-04100395-20260416T154804Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: market-data
entity: ethereum
topic: case-20260416-04100395 | base-rate
question: Will the Binance ETH/USDT 12:00 ET one-minute candle on 2026-04-17 close above 2300?
driver: reliability
date_created: 2026-04-16
source_name: Binance API and CoinGecko ETH market data
source_type: exchange API plus contextual aggregator
source_url: https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [ethereum]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-04100395/researcher-analyses/2026-04-16/dispatch-case-20260416-04100395-20260416T154804Z/personas/base-rate.md, qualitative-db/40-research/cases/case-20260416-04100395/researcher-analyses/2026-04-16/dispatch-case-20260416-04100395-20260416T154804Z/assumptions/base-rate.md]
tags: [source-note, binance, coingecko, eth]
---

# Summary

These sources provide current price context and recent realized ETH distribution around the 2300 threshold.

## Key facts extracted

- Binance spot ticker during retrieval showed ETHUSDT around 2333.42.
- CoinGecko simple price showed ETH around 2338.82, broadly confirming cross-source spot context.
- Binance daily closes over the recent month show ETH frequently trading both above and below 2300 rather than holding far above it.
- In the most recent several daily closes before this run, ETH printed roughly 2285.00, 2191.65, 2369.46, 2322.44, 2359.95, and 2333.43, indicating a regime near the threshold rather than one far away from it.
- The latest Binance daily candle available in retrieval closed around 2333.43, only about 1.45% above the 2300 line.

## Evidence directly stated by source

- Binance API provided direct ETHUSDT spot and recent daily kline data.
- CoinGecko provided contextual confirmation that broader market data places ETH in the same range.

## What is uncertain

- Daily close data is contextual, not the exact noon ET 1-minute candle that settles the contract.
- Crypto volatility over a 24-hour horizon is large enough that current spot near 2330s does not imply a very high probability of remaining above 2300 at the exact settlement minute.

## Why this source may matter

For a base-rate view, the main question is whether ETH is meaningfully above the threshold already or sitting close enough that normal day-scale volatility could easily cross it.

## Possible impact on the question

Because the threshold is close to current spot and recent realized prices have crossed the threshold repeatedly, the outside-view prior should remain relatively moderate rather than treating this as nearly settled.

## Reliability notes

Binance is the strongest data source here because it is also the governing venue for settlement. CoinGecko is useful as a secondary contextual check, though it is not the source of truth for resolution.