---
type: assumption_note
case_key: case-20260413-639ecb3f
research_run_id: 1254c21e-a2cb-4b07-86a9-f78680bcbc40
analysis_date: 2026-04-13
persona: base-rate
domain: crypto
subdomain: ethereum
entity: ethereum
topic: near-threshold-hit-probability-from-mid-2300s
question: "Will Ethereum reach $2,400 April 13-19?"
driver:
date_created: 2026-04-13
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: days
related_entities: ["ethereum"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["short-horizon-price-thresholds"]
upstream_inputs: ["2026-04-13-base-rate-polymarket-and-price-context.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-639ecb3f/researcher-analyses/2026-04-13/dispatch-case-20260413-639ecb3f-20260413T225424Z/personas/base-rate.md"]
tags: ["assumption-note", "ethereum", "base-rate", "threshold-market"]
dispatch_id: dispatch-case-20260413-639ecb3f-20260413T225424Z
---

# Assumption

When ETH starts a 6-day window only about 2% below a target level, its historical short-horizon volatility usually makes a single touch of that level modestly more likely than not, absent a fresh negative regime shift.

## Why this assumption matters

My estimate depends more on the ordinary frequency of small intrawweek threshold touches than on any special bullish narrative. If this assumption is wrong, the market could be materially overpricing a level that still looks psychologically close.

## What this assumption supports

- A probability estimate slightly above 50% and close to the market price.
- A view that the main mechanism is ordinary ETH volatility, not a special catalyst.
- A conclusion that there is no strong outside-view reason to fade the market aggressively.

## Evidence or logic behind the assumption

- Current spot is in the mid-2,300s, so 2,400 is only about a 2% move away.
- Recent 30-day history shows ETH has already traded above 2,400 in the recent past.
- CryptoCompare daily history suggests a rough empirical hit rate in the same ballpark as the market when scaling similar short-horizon move sizes.
- ETH is a high-volatility asset, so a weekly high-touch contract should have a higher hit probability than a weekly close-above contract at the same level.

## What would falsify it

- Evidence that the contract is actually settled on close rather than any touch.
- A sharp downside move or new macro/crypto shock that changes the volatility regime and pushes ETH materially below current levels.
- Better empirical calibration showing that from similar starting distances, 6-day touch rates are materially below the mid-70s.

## Early warning signs

- ETH quickly rejects lower and spends multiple sessions far below 2,350.
- BTC or broader crypto risk sentiment weakens sharply.
- New contract-rule detail reveals a more restrictive source-of-truth or settlement method than assumed.

## What changes if this assumption fails

If the relevant base rate is lower than assumed, my estimate should move down materially and the market would look too optimistic rather than roughly fair.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260413-639ecb3f/researcher-analyses/2026-04-13/dispatch-case-20260413-639ecb3f-20260413T225424Z/personas/base-rate.md
- qualitative-db/40-research/cases/case-20260413-639ecb3f/researcher-analyses/2026-04-13/dispatch-case-20260413-639ecb3f-20260413T225424Z/evidence/base-rate.md