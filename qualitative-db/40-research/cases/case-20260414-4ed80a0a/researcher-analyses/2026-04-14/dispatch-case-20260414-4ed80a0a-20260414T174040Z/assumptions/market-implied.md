---
type: assumption_note
case_key: case-20260414-4ed80a0a
dispatch_id: dispatch-case-20260414-4ed80a0a-20260414T174040Z
research_run_id: 11f1ee38-19b5-4660-8255-0cc1fdcfb859
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: protocols
entity: ethereum
topic: will-ethereum-reach-2-400-april-13-19
question: "Will Ethereum reach $2,400 April 13-19?"
date_created: 2026-04-14
agent: orchestrator
status: active
certainty: high
importance: high
time_horizon: days
related_entities: ["ethereum"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["binance-venue-specific-resolution-dependence"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/personas/market-implied.md"]
tags: ["assumption", "source-of-truth", "venue-specific"]
driver:
---

# Assumption

A Binance ETH/USDT 1h candle high of 2415.50 within the contract window is sufficient practical evidence that at least one Binance 1m candle high also reached or exceeded 2400 in that same hour.

## Why this assumption matters

The final view leans heavily on the idea that the contract condition is already effectively satisfied, which makes the market's 91.6% price understandable and likely still slightly conservative rather than overextended.

## What this assumption supports

- A near-certain Yes estimate.
- The conclusion that the market is mostly pricing already-known qualifying evidence rather than speculative future upside.
- The interpretation that contract mechanics dominate broader ETH directional forecasting here.

## Evidence or logic behind the assumption

Hourly highs on Binance are built from underlying intrahour trade data. If an hourly candle's recorded high is above 2400, then some trade inside that hour necessarily occurred above 2400, which should also be reflected in at least one 1m candle high unless there is a data anomaly or charting discrepancy.

## What would falsify it

- Direct Binance 1m candle history for that hour showing all minute highs below 2400.
- Evidence that Binance's displayed 1h API high can diverge from the 1m chart high used for market settlement.
- A clarified Polymarket rule interpretation excluding the observed timestamp or price print.

## Early warning signs

- Minute-level Binance data becomes hard to reproduce.
- Traders meaningfully sell the Yes side despite the observed hourly high.
- Polymarket comments or moderators flag a data anomaly or rules dispute.

## What changes if this assumption fails

The market would revert from effectively-resolved to still-open, and the probability should drop materially toward a more ordinary path-dependent estimate based on remaining days and ETH volatility.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/personas/market-implied.md