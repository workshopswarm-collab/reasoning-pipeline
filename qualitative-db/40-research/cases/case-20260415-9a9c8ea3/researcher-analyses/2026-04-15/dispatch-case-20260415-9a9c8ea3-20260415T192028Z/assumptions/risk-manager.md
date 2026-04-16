---
type: assumption_note
case_key: case-20260415-9a9c8ea3
dispatch_id: dispatch-case-20260415-9a9c8ea3-20260415T192028Z
research_run_id: f021c5f4-4640-4535-8dfe-5e51a97f9de0
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-72-000-on-april-16
question: "Will the price of Bitcoin be above $72,000 on April 16?"
driver: operational-risk
date_created: 2026-04-15
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: intraday
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["risk-manager finding", "risk-manager evidence map"]
tags: ["assumption", "timing-risk", "binance", "btc"]
---

# Assumption

The Binance UI candle that Polymarket will use for settlement will align in practice with Binance's direct BTCUSDT 1-minute market data, so current API-observed distance above 72,000 is a valid proxy for settlement risk.

## Why this assumption matters

The whole view depends less on long-horizon BTC fundamentals than on minute-specific operational interpretation: correct venue, correct pair, correct timezone, and correct candle close. If the UI surface diverged from the API interpretation or if the relevant minute were misread, confidence would be overstated.

## What this assumption supports

- The conclusion that Yes is favored because BTC is currently materially above 72,000.
- The judgment that remaining risk is mostly timing/path risk rather than contract-definition ambiguity.
- The estimate that downside from mechanics is limited but nonzero.

## Evidence or logic behind the assumption

- Polymarket explicitly names Binance BTC/USDT 1-minute candles as the resolution source.
- Binance public API confirms BTCUSDT is active, exposes 1-minute klines, and shows price precision consistent with a usable settlement surface.
- There is no present evidence of a different venue, pair, or alternate pricing source being intended.

## What would falsify it

- Evidence that Polymarket uses a Binance UI candle timestamp convention that does not line up with the expected 12:00 ET minute.
- Evidence that the UI close differs from the API-observed close in a way that could cross the threshold.
- A published clarification from Polymarket narrowing the source-of-truth in a way not captured by current checks.

## Early warning signs

- Confusion about whether the relevant candle is the minute beginning at 12:00 ET or the close printed at 12:00 ET.
- UI/API discrepancies in sampled candle closes.
- Sudden high-volatility conditions near the resolution window that make minute-level print differences more consequential.

## What changes if this assumption fails

Confidence should fall materially and the market would become more about rules interpretation than spot distance from threshold. A lower probability and stronger operational-risk discount would then be appropriate.

## Notes that depend on this assumption

- Main finding at the assigned risk-manager path
- Evidence map at the assigned risk-manager evidence path