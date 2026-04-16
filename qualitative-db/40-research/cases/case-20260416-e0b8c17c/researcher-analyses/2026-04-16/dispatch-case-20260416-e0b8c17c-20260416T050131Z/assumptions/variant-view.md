---
type: assumption_note
case_key: case-20260416-e0b8c17c
research_run_id: f323ba38-840d-4af0-b5fb-b38a4f0c308c
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-20
question: "Will the price of Bitcoin be above $72,000 on April 20?"
driver: operational-risk
date_created: 2026-04-16
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: short
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-e0b8c17c/researcher-analyses/2026-04-16/dispatch-case-20260416-e0b8c17c-20260416T050131Z/personas/variant-view.md"]
tags: ["assumption", "settlement", "btc", "binance"]
dispatch_id: dispatch-case-20260416-e0b8c17c-20260416T050131Z
---

# Assumption

The practical settlement behavior of the Binance web candle referenced by Polymarket will match the Binance BTCUSDT 1-minute kline/API surface used for verification during this run.

## Why this assumption matters

The case depends on a very specific minute-candle close. If the UI and API diverged materially in timestamping or final displayed close, the operational path to settlement could differ from the verification path used here.

## What this assumption supports

- Confidence that the contract mechanics are understood correctly.
- Confidence that current distance above 72000 is being measured on the right venue and instrument.
- A conclusion that remaining uncertainty is mostly market-price risk rather than source ambiguity.

## Evidence or logic behind the assumption

- Polymarket explicitly names Binance BTC/USDT 1-minute candles as the source.
- Binance exposes the same BTCUSDT 1-minute candles through its exchange API.
- In normal exchange design, the trading UI candle and the kline API are two views into the same venue data.
- The recent timezone conversion check produced a coherent 12:00 ET candle for the prior day.

## What would falsify it

- Evidence that the web UI candle labeled 12:00 ET differs from the API-derived 1-minute kline for the same minute.
- A Polymarket clarification saying only the visible UI widget, not API-equivalent data, controls settlement in a way that can produce different numbers.
- Exchange-side issues such as candle corrections, UI lag, or settlement disputes.

## Early warning signs

- Community reports of Binance chart/API mismatches around the resolution minute.
- Missing or revised kline data for the relevant minute.
- Polymarket moderator comments indicating special handling for this market.

## What changes if this assumption fails

Contract-interpretation risk would rise and the confidence level on the forecast should fall, even if the directional BTC price view stayed the same.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260416-e0b8c17c/researcher-analyses/2026-04-16/dispatch-case-20260416-e0b8c17c-20260416T050131Z/personas/variant-view.md
- qualitative-db/40-research/cases/case-20260416-e0b8c17c/researcher-source-notes/2026-04-16-variant-view-binance-polymarket-rules.md
