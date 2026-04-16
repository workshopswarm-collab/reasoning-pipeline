---
type: assumption_note
case_key: case-20260414-4ed80a0a
dispatch_id: dispatch-case-20260414-4ed80a0a-20260414T174040Z
research_run_id: d4883d27-d611-489a-a1e9-e4968019a939
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: protocols
entity: ethereum
topic: "threshold-market source-of-truth assumption"
question: "Will Ethereum reach $2,400 April 13-19?"
driver:
date_created: 2026-04-14
agent: variant-view
status: active
certainty: medium
importance: high
time_horizon: days
related_entities: ["ethereum"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["contract source-of-truth ambiguity for exchange-threshold markets"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/personas/variant-view.md"]
tags: ["assumption-note", "source-of-truth", "threshold-market"]
---

# Assumption

The main residual risk is not whether ETH can print above $2,400 on a major exchange, but whether the contract’s designated settlement source cleanly records that print during the April 13-19 window.

## Why this assumption matters

The variant view is only mildly below the market because direct exchange data already shows a qualifying-style print on Binance. The remaining disagreement comes from contract interpretation rather than directional crypto price skepticism.

## What this assumption supports

- A modest under view versus the 91.6% market-implied probability.
- Treating source-of-truth ambiguity as the main reason not to simply match the market at the extreme.

## Evidence or logic behind the assumption

- Binance reported a 24h high of 2415.50.
- The Polymarket page fetch explicitly says rules and official data sources govern settlement.
- The actual rules text was not retrievable in this run, leaving a nontrivial interpretive gap.

## What would falsify it

- Recovery of the exact Polymarket rules showing settlement uses Binance or a broad spot high that already clearly exceeded $2,400.
- Independent confirmation from the designated settlement source that ETH already printed at or above $2,400 in-window.

## Early warning signs

- A reliable rule extract naming a source inconsistent with Binance.
- Evidence that the designated source never printed above $2,400 even though Binance did.

## What changes if this assumption fails

If the official source is clearly Binance-compatible and already above $2,400, the correct estimate should move upward toward the high 90s or effectively settled. If the official source is materially different and remains below $2,400, the current market would look overconfident.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/personas/variant-view.md