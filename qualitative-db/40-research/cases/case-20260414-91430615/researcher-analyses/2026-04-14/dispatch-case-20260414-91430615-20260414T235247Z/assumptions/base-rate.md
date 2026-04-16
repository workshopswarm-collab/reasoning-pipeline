---
type: assumption_note
case_key: case-20260414-91430615
dispatch_id: dispatch-case-20260414-91430615-20260414T235247Z
research_run_id: 96e76e5c-a20f-41f0-8f25-cae6c2e8512c
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-19
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-19 close above 70000?"
driver: reliability
date_created: 2026-04-14
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: short-term
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-91430615/researcher-analyses/2026-04-14/dispatch-case-20260414-91430615-20260414T235247Z/personas/base-rate.md"]
tags: ["threshold", "persistence", "settlement-mechanics"]
---

# Assumption

The best outside-view proxy for this contract is that a BTCUSDT market already trading around 74k on Binance behaves similarly enough over the next four days that recent daily-close persistence and nearby noon-ET 1-minute closes are informative for the final noon-ET 1-minute settlement.

## Why this assumption matters

The final estimate depends on treating recent Binance threshold-persistence behavior as relevant rather than assuming the exact settlement minute is either uniquely noisy or almost guaranteed to match the current spot margin.

## What this assumption supports

- An own probability estimate below, but not massively below, the market-implied 90%.
- The view that current cushion above 70k is meaningful but not dispositive.
- The view that contract mechanics create some extra path risk without dominating the whole forecast.

## Evidence or logic behind the assumption

- The governing source for both current pricing and settlement is Binance BTCUSDT.
- Recent noon-ET 1-minute closes and daily closes are both mostly above 70k, suggesting the exact noon print is not wildly disconnected from broader spot behavior.
- Over a four-day horizon, threshold persistence is meaningfully positive in recent Binance history when BTC already sits above 70k.

## What would falsify it

- Evidence that noon-ET 1-minute settlement prints are systematically more volatile or more failure-prone around threshold levels than daily closes suggest.
- A major regime shift in BTC volatility between now and April 19.
- A Binance-specific operational issue affecting the chart or settlement surface.

## Early warning signs

- BTCUSDT rapidly compressing back toward the 70k level.
- Large intraday swings that repeatedly cross 70k.
- Evidence of exchange-specific pricing dislocations or chart inconsistencies.

## What changes if this assumption fails

Confidence should drop, and the estimate would need to move either closer to an event-driven volatility model or closer to the raw market price depending on what new evidence showed about settlement-minute behavior.

## Notes that depend on this assumption

- The main base-rate finding for this dispatch.
- The source note on Binance history and persistence.
