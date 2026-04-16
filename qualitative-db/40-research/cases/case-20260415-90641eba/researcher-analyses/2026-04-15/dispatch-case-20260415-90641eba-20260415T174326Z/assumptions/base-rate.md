---
type: assumption_note
case_key: case-20260415-90641eba
dispatch_id: dispatch-case-20260415-90641eba-20260415T174326Z
research_run_id: 8420de76-85c2-4d2a-80b1-c872a9e340dc
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin-threshold-close
entity: bitcoin
topic: "Stability of BTC above 70000 into April 20 noon ET"
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close on April 20, 2026 be above 70000?"
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
upstream_inputs: ["qualitative-db/40-research/cases/case-20260415-90641eba/researcher-source-notes/2026-04-15-base-rate-binance-btcusdt-and-polymarket-rules.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-90641eba/researcher-analyses/2026-04-15/dispatch-case-20260415-90641eba-20260415T174326Z/personas/base-rate.md"]
tags: ["assumption-note", "crypto", "bitcoin", "threshold-market"]
---

# Assumption

BTC will remain sufficiently above 70,000 over the next five days that ordinary volatility does not push the specific Binance BTC/USDT 12:00 ET one-minute close on April 20 below the threshold.

## Why this assumption matters

The base-rate case for Yes depends less on a fresh bullish catalyst than on the current cushion above 70,000 surviving normal short-horizon crypto volatility.

## What this assumption supports

- A probability estimate above the market-neutral baseline and above 50%
- A view that current spot already provides meaningful structural support for Yes
- A conclusion that the main risk is drawdown / exact-minute timing rather than needing additional upside

## Evidence or logic behind the assumption

- Binance spot checked at roughly 73,974 on April 15, around 5.7% above 70,000.
- Recent Binance daily closes were also above 70,000 on multiple consecutive days.
- Over a five-day horizon, being already materially above the threshold usually helps, even in a volatile asset.
- But this is a single-minute close market, so the cushion is meaningful rather than decisive.

## What would falsify it

- BTC falling back below 70,000 for a sustained period before April 20
- A sharp macro or crypto-specific selloff that compresses BTC several percent lower
- Evidence that recent strength was a transient spike rather than a stable trading regime

## Early warning signs

- Binance daily closes slipping back toward or below low-71k / high-70k territory
- Rapid deterioration in broad crypto risk sentiment
- Repeated rejection with BTC unable to hold above 72k

## What changes if this assumption fails

The probability of Yes should move down materially because the contract requires a specific noon-ET minute close above 70,000, not just having traded above it earlier in the week.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260415-90641eba/researcher-analyses/2026-04-15/dispatch-case-20260415-90641eba-20260415T174326Z/personas/base-rate.md