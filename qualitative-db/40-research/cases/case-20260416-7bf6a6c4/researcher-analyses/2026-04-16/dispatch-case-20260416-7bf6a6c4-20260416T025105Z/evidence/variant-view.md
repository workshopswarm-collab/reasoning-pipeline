---
type: evidence_map
case_key: case-20260416-7bf6a6c4
dispatch_id: dispatch-case-20260416-7bf6a6c4-20260416T025105Z
research_run_id: d9390331-d5ea-4393-9f6e-c636a3f328c3
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: bitcoin-threshold-close
entity: bitcoin
topic: "variant case against overconfident noon-close pricing"
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle on April 17 close above 74000?"
driver: reliability
date_created: 2026-04-16
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: medium
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: ["threshold-proximity", "timestamp-close-fragility"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-7bf6a6c4/researcher-source-notes/2026-04-16-variant-view-polymarket-rules-and-market-snapshot.md", "qualitative-db/40-research/cases/case-20260416-7bf6a6c4/researcher-source-notes/2026-04-16-variant-view-binance-api-spot-and-recent-1m-context.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-7bf6a6c4/researcher-analyses/2026-04-16/dispatch-case-20260416-7bf6a6c4-20260416T025105Z/personas/variant-view.md"]
tags: ["evidence-map", "btc", "noon-close", "variant-view"]
---

# Summary

The evidence leans Yes because BTC is already trading above 74,000 on Binance, but the variant case is that the market may be modestly overconfident because this contract settles on one exact noon ET 1-minute close rather than on a touch or broad daily level.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET 1-minute candle on April 17 close above 74,000?

## Current lean

Lean Yes, but less strongly than the market.

## Prior / starting view

Starting baseline was the market-implied probability from current_price: 0.71 in assignment metadata, with fetched public page snapshot closer to 0.66.

## Evidence supporting the claim

- **Direct Binance price context above threshold**
  - source: `2026-04-16-variant-view-binance-api-spot-and-recent-1m-context.md`
  - why it matters: the governing venue/pair is already above the trigger level
  - direct or indirect: direct
  - weight: high
- **Cross-market ladder shape supports nontrivial chance of staying above 74k**
  - source: `2026-04-16-variant-view-polymarket-rules-and-market-snapshot.md`
  - why it matters: neighboring outcomes imply the crowd sees 74k as plausible but not dominant, with 72k much stronger and 76k much weaker
  - direct or indirect: contextual
  - weight: medium

## Evidence against the claim

- **Exact-timestamp close requirement is stricter than touch logic**
  - source: `2026-04-16-variant-view-polymarket-rules-and-market-snapshot.md`
  - why it matters: being above 74k at many points before noon ET is insufficient if BTC slips below on the exact 12:00 ET close
  - direct or indirect: direct contract interpretation
  - weight: high
- **Recent minute-level drift lower reduces cushion**
  - source: `2026-04-16-variant-view-binance-api-spot-and-recent-1m-context.md`
  - why it matters: short-horizon weakness highlights path dependence and intraday volatility risk
  - direct or indirect: direct
  - weight: medium

## Ambiguous or mixed evidence

- Current BTC level is above threshold, which is bullish, but the margin is not so large that tomorrow's noon close is trivial.
- The assignment metadata says current_price 0.71 while the fetched public page showed 0.66 for the 74k rung; this does not change direction but does show some baseline movement/noise.

## Conflict between inputs

- No hard factual conflict on rules.
- Main disagreement is weighting-based: how much discount should exact-close path dependence get versus the current above-threshold cushion.
- Better overnight / morning volatility evidence on Binance would narrow that disagreement.

## Key assumptions

- Traders may be slightly over-anchoring to current spot >74k rather than the exact noon-close condition.
- No major new catalyst is required for either side; ordinary volatility can decide the outcome.

## Key uncertainties

- Overnight and U.S. morning BTC path into the exact settlement minute.
- Whether current support above 74k is stable or fragile.

## Disconfirming signals to watch

- BTC holding well above 75k into the settlement window.
- Stable Binance 1-minute closes above 74k through late morning ET.

## What would increase confidence

- More extended Binance intraday data across Asia/Europe/U.S. morning.
- Confirmation of realized volatility regime over the last 24 hours.

## Net update logic

Direct venue data says Yes is still the base case, but the contract mechanics justify a modest haircut versus a naive “currently above threshold therefore likely Yes” framing. The variant edge is not that No is more likely than Yes; it is that Yes may be slightly overpriced if traders are mentally converting a close-at-noon contract into a looser above-threshold narrative.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review