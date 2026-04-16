---
type: assumption_note
case_key: case-20260414-082b1b3f
dispatch_id: dispatch-case-20260414-082b1b3f-20260414T171716Z
research_run_id: 55161b68-a1d8-4a11-9380-579d5e0bf7f9
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: trading-markets
entity: sol
topic: solana-above-80-on-april-17
question: "Will the Binance SOL/USDT 1-minute candle labeled 12:00 ET on 2026-04-17 close above 80?"
driver: operational-risk
date_created: 2026-04-14
agent: risk-manager
status: active
certainty: medium
importance: high
time_horizon: short
related_entities: ["sol", "solana"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-082b1b3f/researcher-analyses/2026-04-14/dispatch-case-20260414-082b1b3f-20260414T171716Z/personas/risk-manager.md"]
tags: ["assumption", "threshold-market", "timing-risk"]
---

# Assumption

The current cushion of roughly 5-6 points above the 80 threshold is large enough that ordinary short-horizon SOL volatility will not push the Binance 12:00 ET close below 80 on April 17.

## Why this assumption matters

This is the main premise supporting a Yes probability above 50% despite the fact that the contract has not yet reached its settlement minute. If this assumption is weak, the current above-threshold price does not justify a high confidence estimate.

## What this assumption supports

- A directional Yes lean.
- A probability estimate below the market's 88.5% but still above even odds.
- The view that the main risk is path-dependent volatility rather than contract ambiguity.

## Evidence or logic behind the assumption

- Current Binance spot and recent 1-minute prices are near 85.25.
- Recent Binance daily closes have mostly held above 80, suggesting the threshold is not just barely in range.
- The market only needs a single specified minute close above 80, not a sustained multi-hour hold.

## What would falsify it

- SOL trades down toward the low 80s or below before April 17.
- A broad crypto risk-off move or SOL-specific negative catalyst compresses price by more than ~6% into settlement.
- Intraday volatility increases enough that a noon ET wick/close below 80 becomes plausible even if the broader day stays near the threshold.

## Early warning signs

- Repeated intraday tests of 82 or lower on Binance.
- Market-wide altcoin weakness with SOL underperforming beta peers.
- Increased realized intraday volatility or large liquidation-driven candles during US trading hours.

## What changes if this assumption fails

The case would move quickly from moderate-confidence Yes to roughly balanced or even No-leaning, because the contract is decided by a single minute close at a fixed time rather than a broader average or end-of-day print.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260414-082b1b3f/researcher-analyses/2026-04-14/dispatch-case-20260414-082b1b3f-20260414T171716Z/personas/risk-manager.md
- qualitative-db/40-research/cases/case-20260414-082b1b3f/researcher-analyses/2026-04-14/dispatch-case-20260414-082b1b3f-20260414T171716Z/evidence/risk-manager.md
