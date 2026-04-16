---
type: source_note
case_key: case-20260416-c395460f
dispatch_id: dispatch-case-20260416-c395460f-20260416T022702Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: market-data
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 1-minute candle at 12:00 PM ET on 2026-04-19 close above 80?
driver: reliability
date_created: 2026-04-15T22:28:00-04:00
source_name: Binance public API spot price and recent daily klines
source_type: exchange market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-16
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [sol]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-c395460f/researcher-analyses/2026-04-16/dispatch-case-20260416-c395460f-20260416T022702Z/personas/risk-manager.md]
tags: [binance, price, kline, solusdt]
---

# Summary

This source provides direct exchange-context evidence from Binance, the governing venue for settlement. It does not settle the April 19 noon candle yet, but it does show the current SOL/USDT level and recent trading range relevant to whether 80 is already in or out of the money.

## Key facts extracted

- Binance public API returned current SOLUSDT price of **85.33** on 2026-04-16 UTC fetch time.
- Recent daily klines from Binance show:
  - 2026-04-09 close 84.93
  - 2026-04-10 close 81.53
  - 2026-04-11 close 86.51
  - 2026-04-12 close 83.72
  - 2026-04-13 close 84.90
  - 2026-04-15 partial/current day around 85.33 at fetch time
- The recent 7-day range in the returned sample remained above roughly **81.27 low / 87.67 high**, so the market is only modestly above the 80 strike rather than massively above it.

## Evidence directly stated by source

- Current Binance spot-equivalent ticker was above 80 by about 6.7% at fetch time.
- Recent daily lows in the sample stayed above 80, but only by a few dollars in some sessions.

## What is uncertain

- Daily klines do not directly answer the exact noon ET 1-minute close on April 19.
- Crypto trades continuously, so substantial movement can occur before the resolution window.
- API access here does not by itself verify the exact future candle methodology used in the Binance UI, though it strongly aligns with Binance market data objects.

## Why this source may matter

It is direct venue-specific context. For a short-dated threshold market, the most decision-relevant question is whether current Binance trading leaves enough buffer above 80 to justify an 89% implied probability.

## Possible impact on the question

This evidence supports Yes more than No because SOL is currently above 80 on the governing venue and recent trading has remained above that threshold. But the margin is not so wide that a 1-minute-noon close three days ahead is risk-free; a normal crypto drawdown could still break the thesis.

## Reliability notes

High-quality direct market data for context because it comes from Binance itself. Still not a direct settlement observation, so it should be paired with the rule source and explicit timing verification rather than treated as fully dispositive.