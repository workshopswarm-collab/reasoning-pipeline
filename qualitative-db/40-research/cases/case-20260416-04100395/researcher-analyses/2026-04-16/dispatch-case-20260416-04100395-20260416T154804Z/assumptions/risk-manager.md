---
type: assumption_note
case_key: case-20260416-04100395
dispatch_id: dispatch-case-20260416-04100395-20260416T154804Z
research_run_id: 5d28a326-6ea4-49d7-ab83-b240db3558aa
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: price-markets
entity: ethereum
topic: will-the-binance-eth-usdt-12-00-et-1-minute-candle-on-2026-04-17-close-above-2300
question: "Will the Binance ETH/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 2300?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: "through 2026-04-17 12:00 ET"
related_entities: ["binance", "ethereum"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-04100395/researcher-analyses/2026-04-16/dispatch-case-20260416-04100395-20260416T154804Z/personas/risk-manager.md"]
tags: ["key-assumption", "settlement-minute", "path-risk"]
---

# Assumption

ETH will still be trading safely enough above 2300 on Binance spot near 12:00 ET on 2026-04-17 that ordinary intraday noise will not flip the final 1-minute close below the threshold.

## Why this assumption matters

The market is not asking whether ETH is generally strong, or whether it trades above 2300 sometime before resolution. It asks about one exact exchange, one exact pair, and one exact minute close. A view above 50% therefore depends heavily on there being enough cushion over 2300 to absorb routine noise.

## What this assumption supports

- A modest Yes lean rather than a neutral or No lean.
- Confidence that current spot above 2300 is informative instead of misleading.
- The judgment that the market’s confidence should be discounted somewhat for timing/path fragility but not fully inverted.

## Evidence or logic behind the assumption

- Binance spot during the run was around 2333, giving roughly a 33-dollar cushion versus the threshold.
- Recent Binance 1-minute candles observed during the run stayed above 2330 rather than constantly testing 2300.
- CoinGecko context also showed ETH broadly above 2300, reducing concern that the Binance print was uniquely elevated.

## What would falsify it

- ETH falling back toward or below 2300 during the final pre-resolution hours.
- Heightened volatility that repeatedly swings Binance spot through the threshold.
- A Binance-specific dislocation that breaks alignment with broader ETH pricing.

## Early warning signs

- Loss of the current cushion from low-2330s toward the low-2300s or high-2290s.
- Sharp crypto risk-off move overnight or during the U.S. morning session.
- Multiple one-minute Binance closes clustering near 2300 ahead of settlement.

## What changes if this assumption fails

If the cushion compresses materially, the risk-manager view should move quickly toward the market or below it in favor of No, because a single-minute settlement contract becomes much more fragile when price is hovering near the strike.

## Notes that depend on this assumption

- Main finding: `qualitative-db/40-research/cases/case-20260416-04100395/researcher-analyses/2026-04-16/dispatch-case-20260416-04100395-20260416T154804Z/personas/risk-manager.md`
- Evidence map: `qualitative-db/40-research/cases/case-20260416-04100395/researcher-analyses/2026-04-16/dispatch-case-20260416-04100395-20260416T154804Z/evidence/risk-manager.md`