---
type: assumption_note
case_key: case-20260416-605a067d
dispatch_id: dispatch-case-20260416-605a067d-20260416T142910Z
research_run_id: 68f599bc-70db-4afc-921d-575b6a9e57c6
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: threshold-close-markets
entity: ethereum
topic: "Market confidence rests on ETH remaining comfortably above 2200 into the exact noon ET close window"
question: "Will the Binance ETH/USDT 12:00 ET 1-minute candle close on April 17 be above 2200?"
driver: reliability
date_created: 2026-04-16
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: 24h
related_entities: ["binance", "ethereum"]
related_drivers: ["reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-605a067d/researcher-source-notes/2026-04-16-market-implied-polymarket-rules-and-market-state.md", "qualitative-db/40-research/cases/case-20260416-605a067d/researcher-source-notes/2026-04-16-market-implied-binance-klines-and-docs.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-605a067d/researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/personas/market-implied.md"]
tags: ["assumption-note", "crypto", "close-market"]
---

# Assumption

The market’s ~87% Yes pricing is mostly assuming that ETH can absorb ordinary 24-hour volatility and still print a final Binance ETH/USDT 12:00 ET one-minute close above 2200 on April 17.

## Why this assumption matters

The contract is not asking whether ETH is above 2200 now, or whether it touches 2200 at any point. It asks about one exact future one-minute close on the Binance settlement surface. If that distinction is underweighted, the market could be slightly too confident.

## What this assumption supports

- A high Yes probability well above 50%
- A view that current spot cushion is large enough to survive routine noise
- A view that the 2200 line is already safely in-the-money absent a sharp selloff

## Evidence or logic behind the assumption

- Live Binance ETHUSDT was about 2298 at the time of check, roughly 4.5% above 2200.
- Even the sampled 24h low near 2285 remained above 2200.
- Cross-strike market structure on Polymarket also implied 2200 as much safer than 2300 and far safer than 2400, which is internally coherent with current spot.

## What would falsify it

- A material ETH selloff before noon ET on April 17 that pushes Binance ETH/USDT under 2200 near the settlement minute
- Evidence that the Binance UI settlement candle differs materially from API-based checks in a way that disadvantages a Yes interpretation
- New market stress, liquidation, or macro shock large enough to erase the current cushion

## Early warning signs

- ETH losing the 2285-2290 area and trending downward into April 17 morning
- 2300-line odds weakening sharply while 2200-line odds remain sticky
- Sudden crypto-wide risk-off move during the hours before settlement

## What changes if this assumption fails

The contract would look much closer to a coin-flip between current cushion and event timing risk, and the market’s high-80s Yes pricing would likely be overstated.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260416-605a067d/researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/personas/market-implied.md