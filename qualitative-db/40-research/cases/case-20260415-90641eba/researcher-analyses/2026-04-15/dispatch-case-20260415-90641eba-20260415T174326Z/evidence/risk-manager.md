---
type: evidence_map
case_key: case-20260415-90641eba
dispatch_id: dispatch-case-20260415-90641eba-20260415T174326Z
research_run_id: 5a9faab7-79fb-4b21-b3ce-4db9167a2052
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: daily-close-threshold
entity: bitcoin
topic: "Evidence netting for BTC above 70000 on April 20"
question: "Will the price of Bitcoin be above $70,000 on April 20?"
driver: operational-risk
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["binance", "bitcoin"]
related_drivers: ["liquidity", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260415-90641eba/researcher-source-notes/2026-04-15-risk-manager-polymarket-rules.md", "qualitative-db/40-research/cases/case-20260415-90641eba/researcher-source-notes/2026-04-15-risk-manager-price-context.md", "qualitative-db/40-research/cases/case-20260415-90641eba/researcher-analyses/2026-04-15/dispatch-case-20260415-90641eba-20260415T174326Z/assumptions/risk-manager.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-90641eba/researcher-analyses/2026-04-15/dispatch-case-20260415-90641eba-20260415T174326Z/personas/risk-manager.md"]
tags: ["evidence-map", "btc", "close-market", "binance"]
---

# Summary

The net evidence supports Yes, but with more fragility than the 0.87 market price may suggest because this is a single-minute close-above contract on a specific venue, not a broader weekly-above-level proposition.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET one-minute candle on April 20 close above 70000?

## Current lean

Lean Yes, but not at near-certainty.

## Prior / starting view

Starting view from market was high-confidence Yes because the market priced around 0.87.

## Evidence supporting the claim

- Current Binance spot is about 73999, roughly 5.7% above threshold.
  - Source: price-context note.
  - Why it matters causally: gives immediate cushion above the required level.
  - Direct or indirect: indirect/contextual for final resolution, but direct about current venue state.
  - Weight: high.

- Cross-venue checks from CoinGecko and Coinbase are directionally consistent around 74k.
  - Source: price-context note.
  - Why it matters causally: lowers risk that Binance print is anomalous.
  - Direct or indirect: contextual.
  - Weight: medium.

- Contract uses close-above 70000, not a much higher level like 74k, so the current margin is nontrivial.
  - Source: rules note plus current prices.
  - Why it matters causally: the market only needs BTC to avoid a roughly 5-6% drawdown into settlement minute.
  - Direct or indirect: mixed.
  - Weight: medium-high.

## Evidence against the claim

- The contract is extremely narrow: one exact Binance minute close at 12:00 ET on April 20.
  - Source: rules note.
  - Why it matters causally: path and timing risk remain even if BTC spends most of the week above 70k.
  - Direct or indirect: direct.
  - Weight: high.

- A 5-6% BTC move over five days is entirely plausible.
  - Source: inference from crypto volatility and short-dated price behavior; not separately modeled here.
  - Why it matters causally: current cushion is meaningful but far from invulnerable.
  - Direct or indirect: contextual.
  - Weight: medium-high.

- Settlement is Binance-specific, so venue-specific divergence or chart interpretation issues could matter at the margin.
  - Source: rules note.
  - Why it matters causally: wrong-venue confidence would be false confidence.
  - Direct or indirect: direct for mechanics.
  - Weight: medium.

## Ambiguous or mixed evidence

- Current market price near 0.87 may reflect informed expectations, but it may also compress uncertainty because BTC is currently well above threshold.
- Cross-venue spot agreement is reassuring, but only Binance BTC/USDT at the exact minute matters.

## Conflict between inputs

There is little factual conflict. The main disagreement is weighting-based: how much probability should be discounted for exact-minute close risk versus current 4k cushion.

## Key assumptions

- BTC remains comfortably above 70000 into April 20.
- No sudden macro or crypto-specific drawdown erases the cushion.
- Binance settlement surface remains straightforward to interpret.

## Key uncertainties

- Short-horizon BTC volatility over the next five days.
- Whether noon ET on April 20 arrives during a temporary pullback.
- Whether market participants are slightly underpricing the distinction between "above now" and "above on that exact minute close."

## Disconfirming signals to watch

- BTC drifting back toward 71k or 70k before April 20.
- Sharp risk-off move in crypto broadly.
- Binance-specific prints or mechanics creating ambiguity around the close.

## What would increase confidence

- BTC holding materially above 70k closer to the event date.
- Additional direct Binance checks near settlement confirming sustained cushion.
- Evidence that noon ET is not a structurally fragile time for this pair.

## Net update logic

The strongest update is simple: the event is already in the money by several thousand dollars on the settlement venue. That supports Yes. The risk-manager discount comes from the contract mechanics: a single exact close can fail even when the broader thesis is right. That keeps me below a naive "already above threshold, so basically done" view.

## Suggested downstream use

Use as forecast update and Orchestrator synthesis input, especially to preserve the distinction between current price comfort and exact-minute close fragility.