---
type: assumption_note
case_key: case-20260409-746679d3
dispatch_id: dispatch-case-20260409-746679d3-20260409T205932Z
research_run_id: 26c93914-c5c6-45b7-bbb4-2001b4d5f8b5
analysis_date: 2026-04-09
persona: risk-manager
domain: crypto
subdomain: exchange-market-structure
entity: ethereum
topic: ethereum-above-2100-on-april-10
question: "Will the price of Ethereum be above $2,100 on April 10?"
driver: operational-risk
date_created: 2026-04-09
agent: risk-manager
status: active
certainty: medium
importance: high
time_horizon: "through 2026-04-10 12:00 ET resolution window"
related_entities: ["ethereum"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: ["binance-global"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260409-746679d3/researcher-analyses/2026-04-09/dispatch-case-20260409-746679d3-20260409T205932Z/personas/risk-manager.md"]
tags: ["settlement-assumption", "timezone", "candle-labeling"]
---

# Assumption

The market resolves using the Binance ETH/USDT 1-minute candle that opens at 12:00:00 ET (16:00:00 UTC) on April 10, with the decisive value being that candle’s final close price at the end of the minute.

## Why this assumption matters

A directional view above or below $2,100 is only useful if the correct one-minute interval is identified. If the market instead used a differently labeled candle, or if the UI displayed a local-time convention inconsistent with the API, near-threshold situations could resolve differently.

## What this assumption supports

- Treating the case as a mostly straightforward price-level question rather than a heavily interpretive rules dispute.
- Assigning only moderate, not extreme, residual resolution risk.
- Framing the main downside as timing/operational ambiguity around a one-minute bar rather than broader source ambiguity.

## Evidence or logic behind the assumption

- Polymarket rules explicitly specify Binance ETH/USDT with `1m` candles as the resolution surface.
- Binance API exchange info reports `timezone: UTC`, and kline payloads clearly show 1-minute open and close times.
- On April 10, ET is UTC-4, so noon ET maps cleanly to 16:00 UTC.
- In Binance kline structure, the candle is naturally indexed by its open time, while the final close is set at minute end.

## What would falsify it

- Direct Binance chart documentation or a contemporaneous UI screenshot showing that the chart label `12:00 ET` corresponds to a different API candle than the one opening at 16:00 UTC.
- Market clarifications from Polymarket specifying a different minute-selection convention.

## Early warning signs

- Community comments or support clarifications debating which minute counts.
- UI chart labeling that appears shifted relative to API timestamps.
- Threshold hugging near $2,100 where a one-minute mismatch becomes outcome-relevant.

## What changes if this assumption fails

If the minute-selection convention differs, the case becomes less about simple directional ETH level risk and more about resolution-mechanics risk. Confidence should drop materially, and any probability estimate should move toward greater uncertainty unless the correct convention is clearly re-established.

## Notes that depend on this assumption

- Main finding for risk-manager persona.
- Evidence map for this run.
- Binance resolution-check source note.