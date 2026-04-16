---
type: evidence_map
case_key: case-20260414-8a0619b6
dispatch_id: dispatch-case-20260414-8a0619b6-20260414T194140Z
research_run_id: dde761bd-86a8-487f-a7bf-29465ad9253a
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-18
question: "Will the price of Bitcoin be above $70,000 on April 18?"
driver: operational-risk
date_created: 2026-04-14
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-8a0619b6/researcher-analyses/2026-04-14/dispatch-case-20260414-8a0619b6-20260414T194140Z/personas/risk-manager.md"]
tags: ["evidence-map", "bitcoin", "settlement-risk"]
---

# Summary

This evidence map nets a high-Yes lean against the main fragility: a point-in-time settlement rule on a volatile asset.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET one-minute candle on April 18 close above 70,000?

## Current lean

Lean Yes, but with more fragility than a casual reading of the current 90% market price may suggest.

## Prior / starting view

Starting view was that a spot price already above 74k likely makes Yes favored, but an extreme market price still required extra verification because the contract resolves on one exact minute and one exact venue.

## Evidence supporting the claim

- Binance governing-exchange spot price was 74,110.63 at capture time. Direct. High weight.
- Recent Binance 1-minute kline sample showed prices consistently above 74k over the sampled minutes. Direct for current-state stability, though not direct for settlement day. Medium weight.
- Coinbase spot around 74,166.545 cross-checked the broad BTC level and reduced concern that Binance was showing a unique one-off print. Contextual. Medium weight.
- Polymarket market baseline at ~90% Yes shows crowd consensus that the threshold is currently comfortably in the money. Contextual because it is the object of analysis. Low-to-medium weight.

## Evidence against the claim

- The contract resolves on a single one-minute close at noon ET on April 18, so path risk matters more than average-level comfort. Direct contract fragility. High weight.
- A roughly 5.5% drawdown from 74.1k to below 70k over four days is not an absurd move for BTC, especially across a short horizon that can include weekend volatility. Contextual. Medium-to-high weight.
- Binance is the sole governing venue, so a localized exchange-specific print or short-lived dislocation could decide the market even if broader BTC benchmarks remain above 70k. Direct contract fragility. Medium weight.

## Ambiguous or mixed evidence

- Market price at 90% may be informative, but it can also overstate confidence if traders underweight point-in-time settlement mechanics.
- Cross-exchange agreement currently helps the Yes case, but it does not rule out future venue-specific noise at the decisive minute.

## Conflict between inputs

There is little direct source conflict. The main tension is between spot cushion evidence supporting Yes and contract-structure/timing risk arguing against overconfidence.

## Key assumptions

- BTC remains comfortably above 70k into April 18.
- No Binance-specific anomaly dominates the settlement minute.
- Current cross-exchange price alignment remains broadly intact.

## Key uncertainties

- Near-term BTC realized volatility through the settlement window.
- Whether weekend or macro-driven downside could compress the cushion quickly.
- Exact Binance microstructure conditions at the settlement minute.

## Disconfirming signals to watch

- BTC falling into the low 71k-72k area before April 18.
- Repeated sharp Binance downside wicks.
- Binance diverging materially below peer venues near settlement.

## What would increase confidence

- Continued Binance trading above 73k-74k into late April 17 / early April 18.
- Calm intraday volatility and tight Binance-peer exchange basis near the deadline.

## Net update logic

The extra verification pass did not overturn the obvious directional lean: current spot context strongly favors Yes. But it did keep the estimate below the market because the decisive mechanism is a single-minute, single-venue close, and BTC can plausibly move more than the remaining cushion over four days.

## Suggested downstream use

Use as an orchestrator synthesis input and as a reminder that this type of crypto ladder market should be treated as a point-settlement risk problem, not merely a spot-level snapshot.