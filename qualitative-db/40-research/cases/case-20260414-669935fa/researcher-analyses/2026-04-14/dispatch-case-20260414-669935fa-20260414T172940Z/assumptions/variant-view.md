---
type: assumption_note
case_key: case-20260414-669935fa
dispatch_id: dispatch-case-20260414-669935fa-20260414T172940Z
research_run_id: ddb797ea-2a2d-494b-8a17-dedaad196826
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: spot-price
entity: bitcoin
topic: will-bitcoin-reach-76-000-april-13-19
question: "Will Bitcoin reach $76,000 April 13-19?"
date_created: 2026-04-14
agent: variant-view
status: active
certainty: medium
importance: high
time_horizon: days
related_entities: ["bitcoin"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["weekly-price-resolution-methodology"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-669935fa/researcher-analyses/2026-04-14/dispatch-case-20260414-669935fa-20260414T172940Z/personas/variant-view.md"]
tags: ["assumption-note", "resolution", "source-of-truth", "btc"]
driver:
---

# Assumption

Polymarket will resolve this weekly BTC price-threshold market using a methodology that treats a major-market print above $76,000 during April 13-19 as sufficient, rather than requiring some narrower source that stayed below the threshold.

## Why this assumption matters

The run found strong evidence that Binance printed above $76,000, but the difference between near-certainty and residual uncertainty depends on whether the contract's governing source of truth aligns with broad market/exchange highs.

## What this assumption supports

- A probability estimate slightly below 100% but still extremely high.
- The conclusion that remaining risk is mainly rules-source ambiguity rather than price-action uncertainty.

## Evidence or logic behind the assumption

- Polymarket weekly crypto range markets usually track whether the asset hit the named level during the period, not whether it closed there.
- Major BTC venues usually show limited divergence at this threshold scale.
- A Binance print at $76,038 alongside CoinGecko composite pricing in the upper-$75k area makes it likely that any standard broad-source methodology will register a qualifying touch.

## What would falsify it

- Contract rules naming a different authoritative source that clearly did not print at or above $76,000.
- Official Polymarket clarification that only a particular index or exchange determines the outcome and that source stayed below threshold.

## Early warning signs

- Rules page references a narrow source not visible from the public page extract.
- Major tracked composite providers cluster below $76,000 despite Binance crossing it.
- Market price weakens materially from near-certainty after participants inspect settlement rules.

## What changes if this assumption fails

The case would shift from near-certain yes to a genuine source-of-truth dispute, and the probability should fall materially because threshold passage on one exchange would no longer be enough.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260414-669935fa/researcher-analyses/2026-04-14/dispatch-case-20260414-669935fa-20260414T172940Z/personas/variant-view.md