---
type: assumption_note
case_key: case-20260416-305ed3c4
dispatch_id: dispatch-case-20260416-305ed3c4-20260416T190054Z
research_run_id: 8adf7e65-044c-4c3f-b33c-1a3dccf75a17
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: exchanges
entity: ethereum
topic: will-the-price-of-ethereum-be-above-2-200-on-april-17
question: "Will the price of Ethereum be above $2,200 on April 17?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: "<24h"
related_entities: ["ethereum", "binance"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: ["intraday-volatility"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-305ed3c4/researcher-source-notes/2026-04-16-risk-manager-binance-polymarket-resolution-check.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-305ed3c4/researcher-analyses/2026-04-16/dispatch-case-20260416-305ed3c4-20260416T190054Z/personas/risk-manager.md"]
tags: ["assumption-note", "eth", "binance", "timing-risk"]
---

# Assumption

ETH/USDT on Binance will remain above 2200 through the specific April 17 12:00 ET 1-minute closing candle, not merely trade above 2200 beforehand.

## Why this assumption matters

The market resolves on one narrow timestamped Binance candle close, so the thesis depends on avoiding a sharp downside move into that exact window.

## What this assumption supports

- A high Yes probability despite not being 100%
- A view that current spot margin above 2200 is large enough to absorb ordinary noise
- A conclusion that the dominant risk is timing/path risk rather than contract ambiguity

## Evidence or logic behind the assumption

- Verified Binance spot price is roughly 2344, about 144 points above the 2200 threshold.
- Verified Binance 24h low is 2285.10, still above 2200.
- Recent 1-minute klines cluster near 2343-2345, suggesting no immediate proximity to the strike.

## What would falsify it

- ETH/USDT sells off below 2200 before or at the April 17 12:00 ET candle close.
- Binance-specific dislocation or outage creates an anomalous close below 2200 despite broader market strength.
- A late macro or crypto-specific shock produces a rapid move larger than the current cushion.

## Early warning signs

- ETH/USDT breaking materially below the recent 24h low near 2285.
- Acceleration in downside volatility during U.S. morning trading on April 17.
- Binance-specific order-book or operations problems.
- Broad crypto risk-off move led by BTC or macro headlines.

## What changes if this assumption fails

The high-confidence Yes thesis weakens quickly because the contract is all-or-nothing at a single timestamp. If ETH trades near or below 2200 into late morning ET, probability should be cut aggressively rather than linearly.

## Notes that depend on this assumption

- Main finding: `qualitative-db/40-research/cases/case-20260416-305ed3c4/researcher-analyses/2026-04-16/dispatch-case-20260416-305ed3c4-20260416T190054Z/personas/risk-manager.md`
- Evidence map: `qualitative-db/40-research/cases/case-20260416-305ed3c4/researcher-analyses/2026-04-16/dispatch-case-20260416-305ed3c4-20260416T190054Z/evidence/risk-manager.md`