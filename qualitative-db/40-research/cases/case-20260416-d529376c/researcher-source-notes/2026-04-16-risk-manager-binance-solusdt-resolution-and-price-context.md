---
type: source_note
case_key: case-20260416-d529376c
dispatch_id: dispatch-case-20260416-d529376c-20260416T030247Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: markets
entity: sol
topic: case-20260416-d529376c | risk-manager
question: Will the Binance SOL/USDT 12:00 ET 1-minute candle on 2026-04-19 close above 80?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance SOLUSDT public market data API
source_type: exchange_api
source_url: https://api.binance.com/api/v3/klines?symbol=SOLUSDT&interval=1m
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [sol]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-d529376c/researcher-analyses/2026-04-16/dispatch-case-20260416-d529376c-20260416T030247Z/personas/risk-manager.md]
tags: [binance, resolution-source, price-data, timing-check]
---

# Summary

Binance is the governing source of truth for this market, and direct API pulls confirm both current SOL/USDT spot context and the timing mechanics needed for later resolution.

## Key facts extracted

- Binance ticker endpoint returned SOLUSDT last price near the time of review at `85.32`-`85.33`.
- Binance 24h stats showed a recent trading range of `82.65` to `85.83` with positive 24h change.
- Binance daily candles for Apr 7-16 showed SOL closing above 80 every day in that sample.
- A direct 1-minute kline pull around Apr 15 12:00 ET showed the relevant candle timestamps map to `16:00 UTC`, confirming noon ET should be interpreted as 16:00 UTC on Apr 19 while US daylight saving time is in effect.
- The Apr 15 16:00 UTC one-minute candle closed at `83.94`, showing the exact contract mechanic is operationally accessible via Binance kline data.

## Evidence directly stated by source

- Binance kline data directly exposes open/high/low/close for one-minute SOLUSDT candles.
- Binance ticker and 24h endpoints directly expose current last price and recent range.

## What is uncertain

- Current price is not resolution; the contract depends specifically on the Apr 19 noon ET one-minute close.
- Exchange API accessibility today does not guarantee no temporary outage, UI/API discrepancy, or market shock by resolution time.
- The market description references the Binance trading page UI, while this note used Binance public API endpoints as a direct machine-readable proxy for the same exchange price surface.

## Why this source may matter

This is the closest direct source to the contract’s stated governing surface. It is the main source for both resolution mechanics and the current base-rate price context.

## Possible impact on the question

The direct Binance data supports a high probability that SOL is already above the 80 threshold with some cushion, but it also highlights the fragility: only the exact noon ET one-minute close counts, so short-term volatility and operational issues remain live risks.

## Reliability notes

High credibility for exchange-native price data, but market settlement language still points to the Binance trading interface rather than an explicitly documented API endpoint. That creates low-to-moderate source-of-truth implementation ambiguity even though the economic signal is clear.