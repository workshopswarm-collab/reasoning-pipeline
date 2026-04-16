---
type: source_note
case_key: case-20260416-969f7c01
dispatch_id: dispatch-case-20260416-969f7c01-20260416T013210Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: spot-market-resolution
entity: ethereum
topic: april-17-binance-ethusdt-noon-threshold
question: Will the Binance ETH/USDT 12:00 ET 1-minute candle close above 2200 on April 17, 2026?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance spot API and Polymarket contract page
source_type: primary_market_and_exchange
authority_url: https://polymarket.com/event/ethereum-above-on-april-17
source_url: https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [ethereum]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [source-note, polymarket, binance, eth]
---

# Summary

This source set establishes both the governing resolution mechanics and the current spot context: Polymarket says resolution is the Binance ETH/USDT 1-minute candle for 12:00 ET on April 17, and Binance spot API shows ETH/USDT trading around 2353.84, comfortably above the 2200 threshold roughly 14.5 hours before resolution.

## Key facts extracted

- Governing source of truth is Binance ETH/USDT, specifically the 1-minute candle labeled 12:00 ET on April 17.
- Resolution requires the final candle close to be strictly higher than 2200; equal to 2200 would resolve No.
- Current Binance spot last price is 2353.84.
- Binance 24h stats show high 2385.61, low 2308.50, weighted average 2341.83.
- Recent 1-minute closes from Binance remained in the 2353.11 to 2353.85 range during sampling.

## Evidence directly stated by source

- Polymarket contract text directly states the source and the exact candle/threshold logic.
- Binance API directly states live spot price and recent executed-close data for ETHUSDT.

## What is uncertain

- Live spot context does not guarantee the noon ET print on April 17.
- The exact catalyst path between now and the resolving minute is uncertain.
- Binance website UI wording and API presentation could differ slightly, but the contract text is clear that Binance ETH/USDT 1m close governs.

## Why this source may matter

It is the highest-value source set because it both defines what counts for settlement and shows that the market currently has a sizeable cushion over the threshold.

## Possible impact on the question

Because spot is already more than 6% above 2200, the default lean is Yes unless a meaningful downside catalyst arrives before the resolving minute. The main residual risk is not contract ambiguity but a real price drawdown into noon ET Friday.

## Reliability notes

- Polymarket contract text is authoritative for what the market means.
- Binance API is highly relevant and near-direct for the underlying reference series, though final settlement references the Binance candle as available on Binance rather than this note's sampled API snapshot.
- Independence is only medium because both core facts are tightly linked to the same market structure, so broader catalyst/context sources are still useful.
