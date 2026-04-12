---
type: assumption_note
case_key: case-20260406-574ca6af
dispatch_id: dispatch-case-20260406-574ca6af-20260406T013239Z
research_run_id: aac3fefe-c0dd-4f02-a63d-013876480c2a
analysis_date: 2026-04-06
persona: base-rate
topic: case-20260406-574ca6af | base-rate
question: Will Ethereum reach $2,200 March 30-April 5?
date_created: 2026-04-06
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: case-resolution
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [assumption, resolution-mechanics, binance, polymarket]
---

# Assumption

The operative assumption is that Polymarket will settle this contract exactly as written using Binance ETH/USDT 1-minute candle High values, not broader ETH/USD spot or other-exchange reference prices.

## Why this assumption matters

The directional answer flips on contract interpretation. Broad market summaries can imply Ethereum "roughly reached" higher levels, but the contract only cares about a specific exchange, pair, interval, and field.

## What this assumption supports

- The conclusion that the market should resolve NO despite a high pre-close market price of 0.74.
- The decision to downweight generalized ETH price commentary and cross-exchange summaries.

## Evidence or logic behind the assumption

- The market page states the precise resolution rule and the specific resolution source.
- The rule explicitly excludes prices from other exchanges, different trading pairs, or spot markets.
- The referenced Binance 1-minute kline data is directly queryable and auditable.

## What would falsify it

- Polymarket publishes a different controlling resolution rule for this exact market.
- A dispute or settlement note shows that another source hierarchy overrides the market page text.
- Binance’s own referenced data surface shows a 1-minute ETH/USDT high at or above 2200 within the relevant window.

## Early warning signs

- Polymarket clarifies that the market title or another hidden ruleset supersedes the displayed source language.
- An official market comment cites an index, another pair, or another exchange as relevant after all.
- Independent re-pulls of the Binance kline history show materially different highs.

## What changes if this assumption fails

If the contract is not governed by Binance ETH/USDT 1-minute highs, the analysis would need to be rebuilt around the actual controlling source and cross-exchange price evidence could matter materially more.

## Notes that depend on this assumption

- Main finding at personas/base-rate.md
- Source note: 2026-04-06-base-rate-binance-polymarket-rules.md