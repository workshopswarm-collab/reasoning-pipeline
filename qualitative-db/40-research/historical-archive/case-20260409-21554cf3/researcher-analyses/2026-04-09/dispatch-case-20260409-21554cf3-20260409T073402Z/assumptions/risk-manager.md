---
type: assumption_note
case_key: case-20260409-21554cf3
dispatch_id: dispatch-case-20260409-21554cf3-20260409T073402Z
research_run_id: bdb694fc-fb8e-4ff6-af28-2bb34b139a8f
analysis_date: 2026-04-09
persona: risk-manager
domain: crypto
subdomain: exchange-market-structure
entity: ethereum
topic: will-the-price-of-ethereum-be-above-2-100-on-april-9
question: "Will the price of Ethereum be above $2,100 on April 9?"
driver: operational-risk
date_created: 2026-04-09T03:36:20-04:00
agent: risk-manager
status: active
certainty: medium
importance: high
time_horizon: intraday
related_entities: ["ethereum"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: ["binance exchange global"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["settlement-minute", "timing-risk", "exact-candle"]
---

# Assumption

ETH/USDT on Binance will remain comfortably above $2,100 through the specific 12:00 ET one-minute close rather than merely trading above $2,100 earlier in the day.

## Why this assumption matters

The market is resolved by one exact candle close, so broad bullishness or a current spot cushion only matters if the cushion survives to the governing minute.

## What this assumption supports

- A high-probability Yes estimate.
- The interpretation that current trading roughly $80+ above the threshold is enough buffer for a confident but not certain view.
- The judgment that path risk is the main remaining issue rather than source ambiguity.

## Evidence or logic behind the assumption

- Direct Binance checks show ETH/USDT trading around 2181-2184 during the early-morning ET verification window.
- The threshold is materially below current spot, leaving room for normal minute-to-minute noise without flipping the outcome.
- The contract names a highly liquid major pair on a major exchange, which reduces random print risk versus a thin venue.

## What would falsify it

- A sharp downside move that pushes Binance ETH/USDT below 2100 near noon ET.
- Exchange-specific dislocation on Binance even if broader ETH remains above 2100 elsewhere.
- Evidence that the relevant candle interpretation differs from the expected 16:00 UTC / 12:00 ET mapping.

## Early warning signs

- ETH losing the $2150-$2160 area well before noon ET.
- Abrupt volatility spikes or exchange-specific wick behavior on Binance.
- Confusion or inconsistency between Binance display surfaces around timezone or candle labeling.

## What changes if this assumption fails

The high-confidence Yes view falls quickly. If ETH approaches the threshold before noon ET, the market should be treated as materially more uncertain than the current high-90s price implies.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260409-21554cf3/researcher-analyses/2026-04-09/dispatch-case-20260409-21554cf3-20260409T073402Z/personas/risk-manager.md
- qualitative-db/40-research/cases/case-20260409-21554cf3/researcher-analyses/2026-04-09/dispatch-case-20260409-21554cf3-20260409T073402Z/evidence/risk-manager.md