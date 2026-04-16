---
type: assumption_note
case_key: case-20260415-1cbf2a82
research_run_id: 932f4045-a4d2-4d9f-aedd-340a296255ae
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-17
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-17 be above 72000?"
driver: operational-risk
date_created: 2026-04-15
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: short
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-1cbf2a82/researcher-analyses/2026-04-15/dispatch-case-20260415-1cbf2a82-20260415T144104Z/personas/base-rate.md"]
tags: ["timestamp-market", "assumption", "settlement"]
dispatch_id: dispatch-case-20260415-1cbf2a82-20260415T144104Z
---

# Assumption

The Binance website 1-minute candle used for market settlement will reflect the same underlying BTC/USDT price behavior as the publicly accessible Binance API data used for current-state and recent-range checks.

## Why this assumption matters

The base-rate memo relies on API-observed current price and recent trading range to estimate the chance that the April 17 noon ET 1-minute candle closes above 72,000. If website candle presentation diverged materially from accessible API data, the estimate would be less trustworthy.

## What this assumption supports

- Treating current Binance spot above 72,000 as the main direct support for Yes.
- Treating recent Binance daily volatility as relevant context for a 2-day horizon timestamp event.
- Viewing operational/settlement risk as low but nonzero rather than dominant.

## Evidence or logic behind the assumption

Binance website candles and public market-data APIs ordinarily reflect the same exchange market. The contract names Binance BTC/USDT specifically, and there is no visible reason in this run to think the website 1-minute close would be generated from a different venue or benchmark.

## What would falsify it

- Evidence that website candle close differs systematically from API-observed BTC/USDT market data.
- A contract clarification saying only a distinct website-rendered value counts even if API data differs.
- A Binance display or feed incident around the resolution window.

## Early warning signs

- Binance API outages or degraded responses.
- Reported mismatch between exchange UI candles and API values.
- Last-minute Polymarket clarification on data-source handling.

## What changes if this assumption fails

Confidence in the estimate should drop, and more weight should be put on operational-risk / source-of-truth ambiguity rather than on pure price-level base rates.

## Notes that depend on this assumption

- Main finding at `qualitative-db/40-research/cases/case-20260415-1cbf2a82/researcher-analyses/2026-04-15/dispatch-case-20260415-1cbf2a82-20260415T144104Z/personas/base-rate.md`