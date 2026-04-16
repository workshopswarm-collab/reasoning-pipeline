---
type: assumption_note
case_key: case-20260414-4ed80a0a
dispatch_id: dispatch-case-20260414-4ed80a0a-20260414T174040Z
research_run_id: c66d2b88-d6ed-44c7-ad54-6594d87a8cb8
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: protocols
entity: ethereum
topic: will-ethereum-reach-2-400-april-13-19
question: "Will Ethereum reach $2,400 April 13-19?"
driver:
date_created: 2026-04-14
agent: orchestrator
status: active
certainty: high
importance: high
time_horizon: intrawindow
related_entities: ["ethereum"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["binance-market-data-integrity"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/personas/risk-manager.md"]
tags: ["assumption", "binance", "settlement-risk"]
---

# Assumption

Polymarket settlement will treat the observed Binance ETH/USDT 1-minute high above $2,400 as valid and sufficient evidence for a `Yes` resolution.

## Why this assumption matters

The remaining uncertainty in this case is no longer mainly about Ethereum price path; it is about whether the already-observed qualifying print will be recognized cleanly by the contract’s settlement path.

## What this assumption supports

- A near-certain `Yes` estimate rather than merely a high-probability forward-looking estimate.
- The view that most residual risk is operational / source-of-truth risk, not market-direction risk.

## Evidence or logic behind the assumption

- Polymarket explicitly names Binance ETH/USDT 1-minute highs as the governing source.
- Binance API data in the checked window showed a max high of 2415.5, comfortably above the 2400 threshold.
- The threshold was exceeded early in the market window, reducing dependence on future path.

## What would falsify it

- Evidence that the Binance chart UI contradicts the API-reported high for the relevant minute.
- A Polymarket clarification or dispute saying the observed print was invalid, erroneous, or outside the eligible window.
- Discovery that the queried data window or timezone mapping was wrong.

## Early warning signs

- Inconsistent reported highs across Binance surfaces.
- Market price backing away materially from near-certainty despite no new price action.
- User comments or official market notes raising a resolution dispute.

## What changes if this assumption fails

The case would revert from effectively settled to a live path-dependent threshold question, and the probability would need to be re-estimated from current spot/volatility rather than from realized evidence.

## Notes that depend on this assumption

- Main persona finding at the assigned risk-manager path.
- Binance price verification source note.
- Evidence map for this run.