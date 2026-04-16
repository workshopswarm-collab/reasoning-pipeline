---
type: evidence_map
case_key: case-20260415-47643da0
dispatch_id: dispatch-case-20260415-47643da0-20260415T010752Z
research_run_id: 305a03c2-90c5-4f3d-9b0b-10e9cbd16748
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: market-structure
entity: bitcoin
topic: bitcoin-above-72k-on-april-17
question: "Will the price of Bitcoin be above $72,000 on April 17?"
driver: operational-risk
date_created: 2026-04-15
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-47643da0/researcher-analyses/2026-04-15/dispatch-case-20260415-47643da0-20260415T010752Z/personas/risk-manager.md"]
tags: ["evidence-map", "bitcoin", "binance", "timing-risk"]
---

# Summary

Net evidence supports a Yes lean because BTC is currently well above the threshold on Binance, but the risk-manager adjustment is to discount the market's confidence because the contract depends on one exact future minute close.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET 1-minute candle on April 17 close above 72,000?

## Current lean

Lean Yes, but with more caution than the market's mid-80s implied confidence.

## Prior / starting view

Starting baseline was the market-implied probability of about 84% from current_price 0.84.

## Evidence supporting the claim

- `2026-04-15-risk-manager-binance-btcusdt-api.md`
  - Direct Binance data showed BTC around 74.68k.
  - Direct evidence.
  - High weight because the current level is materially above the threshold.
- `2026-04-15-risk-manager-polymarket-rules.md`
  - Rules confirm Binance BTC/USDT is the governing venue and the contract is a strict above/below threshold check.
  - Direct contract evidence.
  - High weight because it defines the exact resolution conditions.

## Evidence against the claim

- Contract is resolved on a single exact 12:00 ET minute close, not on general trading level across the day.
  - This creates timing/path fragility.
  - Indirect but structurally important.
  - Medium-high weight.
- BTC remains a volatile asset and the current cushion, while meaningful, is not so large that a sharp drawdown is implausible over ~38 hours.
  - Contextual evidence from asset-class behavior rather than a single direct citation in-run.
  - Medium weight.

## Ambiguous or mixed evidence

- The same current cushion that supports Yes also may explain why the market is expensive; whether 84% is too high depends on how much one discounts for short-horizon volatility into a single minute.

## Conflict between inputs

No major factual conflict. The disagreement is mainly weighting-based: how much probability mass to assign to short-horizon downside and timing risk versus the current buffer above 72,000.

## Key assumptions

- Binance spot remains representative enough for the contract's settlement surface.
- No large crypto or macro shock pushes BTC below 72,000 into the settlement minute.
- The ET-timestamped noon minute is interpreted as stated in the contract text.

## Key uncertainties

- Short-horizon BTC volatility over the remaining ~38 hours.
- Exact state of BTC momentum closer to the event.
- Small operational ambiguity between Binance display conventions and ET framing, though contract text is explicit.

## Disconfirming signals to watch

- BTC loses the 73k area before the target window.
- Binance BTC/USDT trades near 72k on the morning of April 17 ET.
- Venue-specific pricing anomalies emerge on Binance.

## What would increase confidence

- BTC holding comfortably above 73k into April 16 evening and April 17 morning ET.
- Continued Binance 1-minute closes materially above 72k without unusual downside spikes.

## Net update logic

The direct evidence made the directional view straightforward: BTC is currently well above the threshold on the named venue. The risk-manager adjustment is not a bearish reversal but a confidence haircut because a single future minute close creates failure modes the market may underweight.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review