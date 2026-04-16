---
type: source_note
case_key: case-20260414-082b1b3f
dispatch_id: dispatch-case-20260414-082b1b3f-20260414T171716Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: tokens
entity: sol
topic: case-20260414-082b1b3f | base-rate
question: Will the Binance SOL/USDT 12:00 ET 1-minute candle close be above 80 on April 17, 2026?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance spot API and Polymarket market page
source_type: primary_market_data_and_market_rules
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [sol, solana]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-082b1b3f/researcher-analyses/2026-04-14/dispatch-case-20260414-082b1b3f-20260414T171716Z/personas/base-rate.md]
tags: [binance, polymarket, contract-mechanics, market-data]
---

# Summary

This note captures the direct source-of-truth surface for the contract and a current Binance spot check relevant to the base-rate view.

## Key facts extracted

- Polymarket states the market resolves on the Binance SOL/USDT 1-minute candle for 12:00 in ET timezone on April 17, 2026, using the final Close price.
- The market is specific to Binance SOL/USDT, not other exchanges or pairs.
- A direct Binance spot API pull on 2026-04-14 returned SOLUSDT price 85.25000000.
- A direct Binance 1-minute kline API pull returned a latest sample 1-minute close of 85.25000000.
- A Binance 5-minute average price endpoint returned 85.27257717.
- A direct Binance daily-kline pull for the last 30 and 180 sessions showed 29/30 and 174/180 daily closes above 80.

## Evidence directly stated by source

- Polymarket rule text explicitly states the governing source and the exact condition: Binance SOL/USDT 12:00 ET 1-minute candle final Close must be higher than 80.
- Binance API responses directly state current SOLUSDT prices and historical kline close values.

## What is uncertain

- Current spot being above 80 does not itself settle the Apr 17 12:00 ET candle.
- Daily closes above 80 are only a contextual base-rate proxy, not the exact noon ET one-minute settlement value.
- API-accessed market data is a practical direct source, but the contract text names the Binance trading interface candle as the governing resolution surface.

## Why this source may matter

This is the most important direct evidence for contract interpretation and for establishing that SOL is currently trading meaningfully above the strike, which supports a high prior for a three-day-ahead noon ET close remaining above 80 absent a sharp selloff.

## Possible impact on the question

The combination of explicit contract mechanics plus current Binance pricing above 80 materially supports a high-probability Yes view, while also highlighting the real residual risk: the market resolves on one specific future minute, so short-horizon volatility and exchange-specific pricing still matter.

## Reliability notes

- Binance is the named resolution source, so source-of-truth quality for contract mechanics is high.
- Polymarket page extraction is reliable for reading the displayed rules but is still secondary to the governing exchange surface named in the contract.
- Daily-close base-rate evidence is structurally helpful but not fully independent from current spot because all series come from the same exchange and asset.
