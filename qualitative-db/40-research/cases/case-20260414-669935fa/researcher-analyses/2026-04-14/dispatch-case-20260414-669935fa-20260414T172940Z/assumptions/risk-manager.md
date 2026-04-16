---
type: assumption_note
case_key: case-20260414-669935fa
dispatch_id: dispatch-case-20260414-669935fa-20260414T172940Z
research_run_id: 591764aa-483b-4dd8-b2ab-48ab921b4a9b
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: tokens
entity: bitcoin
topic: will-bitcoin-reach-76k-april-13-19
question: "Will Bitcoin reach $76,000 April 13-19?"
date_created: 2026-04-14
agent: orchestrator
status: active
certainty: medium_high
importance: high
time_horizon: immediate
related_entities: ["bitcoin"]
related_drivers: []
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["assumption", "settlement", "binance"]
driver:
---

# Assumption

The Binance public 1-minute klines API high of 76038.0 is materially the same underlying value stream the Polymarket rules intend when they reference Binance BTC/USDT 1-minute High prices.

## Why this assumption matters

The final probability estimate depends on whether the observed qualifying print should be treated as effectively settling the contract already, rather than merely making a future touch likely.

## What this assumption supports

- A near-certain Yes estimate rather than a merely high-probability Yes estimate.
- The view that residual risk is implementation/rules mismatch risk, not ordinary BTC path risk.
- The conclusion that the market’s 99.95% price is directionally understandable even if slightly overstated.

## Evidence or logic behind the assumption

- The Polymarket rules explicitly name Binance BTC/USDT 1-minute candle highs as the source of truth.
- Binance’s own public market-data API is a natural direct representation of those 1-minute highs.
- The qualifying print occurred squarely inside the contract window.

## What would falsify it

- A clear discrepancy between the Binance chart/UI high used for settlement and the public API high.
- A Polymarket clarification that the referenced chart source excludes or revises the observed print.
- Market resolution infrastructure later refusing to treat the observed 76038.0 high as qualifying.

## Early warning signs

- The contract remains unresolved or trades materially below certainty after broad participants have time to digest the print.
- Other independent checks of Binance 1-minute highs fail to reproduce the threshold breach.
- Public discussion identifies chart-setting quirks or data corrections affecting the candle high.

## What changes if this assumption fails

The estimate should fall back from near-certain to high-but-not-locked, with remaining uncertainty again concentrated in whether BTC can print a fresh qualifying wick before Apr 19 23:59 ET.

## Notes that depend on this assumption

- `qualitative-db/40-research/cases/case-20260414-669935fa/researcher-analyses/2026-04-14/dispatch-case-20260414-669935fa-20260414T172940Z/personas/risk-manager.md`
- `qualitative-db/40-research/cases/case-20260414-669935fa/researcher-analyses/2026-04-14/dispatch-case-20260414-669935fa-20260414T172940Z/evidence/risk-manager.md`