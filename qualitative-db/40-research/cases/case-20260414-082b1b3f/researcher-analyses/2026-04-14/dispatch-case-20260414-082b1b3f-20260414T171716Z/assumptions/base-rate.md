---
type: assumption_note
case_key: case-20260414-082b1b3f
dispatch_id: dispatch-case-20260414-082b1b3f-20260414T171716Z
research_run_id: 7cbc8246-8262-476a-a7ee-cd3fa1d2a7b9
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: tokens
entity: sol
topic: will-the-binance-sol-usdt-12-00-et-1-minute-candle-close-be-above-80-on-april-17-2026
question: "Will the Binance SOL/USDT 12:00 ET 1-minute candle close be above 80 on April 17, 2026?"
driver: operational-risk
date_created: 2026-04-14
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: short
related_entities: ["sol", "solana"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-082b1b3f/researcher-analyses/2026-04-14/dispatch-case-20260414-082b1b3f-20260414T171716Z/personas/base-rate.md"]
tags: ["assumption", "short-horizon", "crypto-volatility"]
---

# Assumption

SOL will not experience a roughly 6%+ Binance-specific drawdown by the Apr 17, 2026 12:00 ET one-minute close that leaves the settlement candle at or below 80.

## Why this assumption matters

The base-rate case is mostly an outside-view continuity argument: current price is already above strike, and recent history shows SOL spending most days above 80. If that continuity breaks before the specific settlement minute, the contract resolves No even if the broader medium-term thesis for SOL remains intact.

## What this assumption supports

- A high-probability Yes estimate.
- Treating recent Binance closes above 80 as a relevant reference class.
- Interpreting current distance above strike as meaningful cushion rather than noise.

## Evidence or logic behind the assumption

- Direct Binance spot on 2026-04-14 was about 85.25, leaving a modest but real buffer above 80.
- Last-30-day and last-180-day Binance daily closes were above 80 about 96.7% of the time in the pulled sample.
- No case-specific catalyst was identified in this run that clearly overwhelms that outside-view prior.

## What would falsify it

- A broad crypto risk-off move that takes SOL materially below 80 before the settlement minute.
- Solana-specific bad news or exchange-specific dislocation on Binance.
- A volatility spike that pushes SOL below 80 specifically at noon ET even if surrounding prices remain higher.

## Early warning signs

- SOL breaking below low-80s on Binance before Apr 17.
- BTC/ETH-led broad crypto selloff with alt underperformance.
- Exchange-specific abnormalities in Binance SOL/USDT pricing or candle behavior.

## What changes if this assumption fails

The probability should fall sharply because this contract is narrow and time-specific; once spot trades near or below 80 close to settlement, the base-rate cushion largely disappears and event risk dominates.

## Notes that depend on this assumption

- The main base-rate finding for this dispatch.
