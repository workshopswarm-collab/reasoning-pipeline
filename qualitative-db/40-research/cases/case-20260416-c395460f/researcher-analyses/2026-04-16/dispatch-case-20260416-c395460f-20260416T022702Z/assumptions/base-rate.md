---
type: assumption_note
case_key: case-20260416-c395460f
dispatch_id: dispatch-case-20260416-c395460f-20260416T022702Z
research_run_id: 33ea9486-e962-4197-ac83-060b4d5041db
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: tokens
entity: sol
topic: solana-above-80-on-april-19
question: "Will the Binance SOL/USDT 12:00 ET 1-minute candle close above 80 on April 19, 2026?"
driver: operational-risk
date_created: 2026-04-15
agent: base-rate
status: active
certainty: medium
importance: high
time_horizon: "through 2026-04-19 12:00 ET"
related_entities: ["sol", "solana"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-c395460f/researcher-analyses/2026-04-16/dispatch-case-20260416-c395460f-20260416T022702Z/personas/base-rate.md"]
tags: ["assumption-note", "crypto", "threshold-market"]
---

# Assumption

The main base-rate assumption is that SOL remains in roughly the recent Binance trading regime through April 19 noon ET rather than experiencing a fresh downside shock large enough to push the settlement minute below 80.

## Why this assumption matters

The finding leans Yes primarily because current spot is already above the threshold and recent Binance daily closes clustered in the low/mid-80s. If the regime changes abruptly, the current-above-threshold base rate becomes much less informative.

## What this assumption supports

- A Yes-leaning probability estimate above 50%
- Skepticism toward an extreme 89% market probability, because a 3-day crypto horizon still leaves room for meaningful downside volatility
- Use of recent Binance range behavior as the most relevant outside-view anchor

## Evidence or logic behind the assumption

- Current Binance SOL/USDT spot is about 84.94, already above 80.
- Recent Binance daily closes were mostly above 80.
- The threshold is only about 5.8% below the observed spot level at research time, which is not trivial but is within normal crypto move size over several days.

## What would falsify it

- A broad crypto risk-off move that takes SOL materially below 80 before the target minute
- Solana-specific negative news or exchange-specific disruption affecting Binance SOL/USDT pricing
- Repeated sub-80 trading that suggests recent low/mid-80 behavior is no longer the right reference class

## Early warning signs

- BTC/ETH-led market selloff with SOL underperforming
- SOL trading back toward the recent low-80s or high-70s region
- Weekend volatility spike or exchange-specific operational issue around Binance pricing

## What changes if this assumption fails

The view should move materially toward No, and the market’s 89% Yes pricing would no longer look obviously rich.

## Notes that depend on this assumption

- Main persona finding at the assigned base-rate finding path