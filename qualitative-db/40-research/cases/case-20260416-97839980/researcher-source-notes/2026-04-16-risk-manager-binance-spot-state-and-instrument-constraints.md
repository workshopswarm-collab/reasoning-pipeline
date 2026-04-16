---
type: source_note
case_key: case-20260416-97839980
dispatch_id: dispatch-case-20260416-97839980-20260416T040518Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: exchange-data
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 12:00 ET 1-minute candle close above 80 on April 19, 2026?
driver: reliability
date_created: 2026-04-16
source_name: Binance API spot price, klines, and exchange info
source_type: primary_exchange_data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: risk-manager
related_entities: [sol, solana]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-97839980/researcher-analyses/2026-04-16/dispatch-case-20260416-97839980-20260416T040518Z/personas/risk-manager.md]
tags: [binance, spot, klines, source-note]
---

# Summary

This source provides the most direct contextual evidence available before resolution: current Binance SOL/USDT spot price, recent daily and hourly candles, and exchange instrument precision.

## Key facts extracted

- Binance spot ticker returned SOLUSDT price of 85.39 at research time on 2026-04-16.
- Recent daily closes from Binance show SOL closing above 80 for the last several daily candles in the sample, with closes including 84.83, 84.93, 81.53, 86.51, 83.72, 84.90, and current day around 85.39.
- Recent 72 hourly candles show repeated trading mostly in the low-to-mid 80s, with lows in the sample staying above roughly 81.5 after the rebound.
- Binance exchange info for SOLUSDT shows a tick size of 0.01, implying contract-relevant precision at the cent level for spot pricing.

## Evidence directly stated by source

- Spot SOL/USDT is currently above the 80 threshold by about $5.39.
- Recent market structure has repeatedly held above 80 rather than merely touching it briefly.
- The relevant instrument is live and trading on Binance spot.

## What is uncertain

- This does not directly settle the April 19 noon ET one-minute close; it is only a current-state and recent-path reference.
- Short-horizon crypto volatility can be large enough to cross a $5 buffer over multiple days, especially if macro or crypto-specific sentiment shifts.

## Why this source may matter

For this contract, Binance spot is the governing exchange. Using Binance API data reduces exchange-basis ambiguity and directly checks whether current state already gives the Yes side substantial cushion.

## Possible impact on the question

This materially supports Yes because SOL is already above 80 on the correct exchange with a several-dollar buffer and recent realized trading has mostly held above the strike. It also defines the main remaining risk as path/timing reversal rather than needing a fresh breakout.

## Reliability notes

High-quality primary data for current state and market mechanics. Independence is limited because the same exchange is also the settlement source, but for this contract that is a feature rather than a flaw.