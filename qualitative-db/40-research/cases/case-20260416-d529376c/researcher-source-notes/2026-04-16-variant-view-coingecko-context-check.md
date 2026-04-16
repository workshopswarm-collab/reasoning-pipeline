---
type: source_note
case_key: case-20260416-d529376c
dispatch_id: dispatch-case-20260416-d529376c-20260416T030247Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: token-price
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 12:00 ET 1-minute candle close above 80 on April 19, 2026?
driver: reliability
date_created: 2026-04-16
source_name: CoinGecko simple price context
source_type: secondary_contextual
source_url: https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true
source_date: 2026-04-15T23:04:45-04:00
credibility: medium_high
recency: high
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: Orchestrator
related_entities: [sol, solana]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [variant-view-finding]
tags: [coingecko, verification, context]
---

# Summary

This note records an external verification pass from CoinGecko to check that Binance spot context was not obviously anomalous.

## Key facts extracted

- CoinGecko reported **Solana = $85.19**.
- CoinGecko reported **24h change = +2.22%**.
- This closely matched the Binance spot/ticker readings around **$85.28-$85.30** and a roughly **+2.3%** 24h move.

## Evidence directly stated by source

- Solana/USD price near 85.
- Positive 24h price change of a bit more than 2%.

## What is uncertain

- CoinGecko is not the settlement source and may aggregate across venues or have slight timestamp differences.
- It does not resolve the exact April 19 noon ET candle requirement.

## Why this source may matter

It serves as an independent contextual check that current market state is broadly consistent across external data providers and that Binance was not showing an obviously idiosyncratic print.

## Possible impact on the question

This verification modestly supports the baseline yes case by confirming that SOL is broadly trading in the mid-80s, but it does not materially reduce future path risk between now and settlement.

## Reliability notes

- Good as a contextual price verifier, weaker than Binance for exact contract settlement.
- Useful mainly for cross-source consistency rather than direct resolution.