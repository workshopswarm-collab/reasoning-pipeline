---
type: evidence_map
case_key: case-20260415-0735f476
dispatch_id: dispatch-case-20260415-0735f476-20260415T201136Z
research_run_id: 9cbbd9f1-24dc-4e3e-956f-801560384ced
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin-threshold-market
entity: bitcoin
topic: "Bitcoin above 70000 on April 20 noon ET Binance close"
question: "Will the price of Bitcoin be above $70,000 on April 20?"
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
upstream_inputs: ["qualitative-db/40-research/cases/case-20260415-0735f476/researcher-source-notes/2026-04-15-risk-manager-polymarket-rules-binance-resolution.md", "qualitative-db/40-research/cases/case-20260415-0735f476/researcher-source-notes/2026-04-15-risk-manager-binance-spot-context.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-0735f476/researcher-analyses/2026-04-15/dispatch-case-20260415-0735f476-20260415T201136Z/personas/risk-manager.md"]
tags: ["evidence-map", "btc", "threshold", "timing-risk"]
---

# Summary

The evidence leans Yes because BTC is currently well above 70,000 and the governing exchange is the same venue showing that cushion, but the market is not risk-free because settlement depends on one future minute close rather than current level.

## Question being evaluated

Will Binance BTC/USDT close strictly above 70,000 on the 12:00 ET 1-minute candle on April 20, 2026?

## Current lean

Lean Yes, but with meaningful residual path risk that keeps the estimate below certainty.

## Prior / starting view

Starting from the market price, the baseline was about 93% Yes.

## Evidence supporting the claim

- Polymarket rules clearly identify Binance BTC/USDT 1-minute close as the governing source.
  - Source: Polymarket rules source note.
  - Why it matters causally: removes ambiguity about what counts.
  - Direct or indirect: direct for contract mechanics.
  - Weight: high.

- Binance ticker and recent 1-minute klines show BTC around 74.7k, roughly 6.6% above 70k.
  - Source: Binance spot context source note.
  - Why it matters causally: the asset currently has a meaningful buffer above threshold on the governing venue.
  - Direct or indirect: direct contextual evidence.
  - Weight: high.

- Independent contextual cross-checks from CoinGecko and Coinbase also place BTC around 74.6k-74.7k.
  - Source: Binance spot context source note.
  - Why it matters causally: suggests the level is market-wide, not a Binance-only artifact.
  - Direct or indirect: indirect/contextual for settlement.
  - Weight: medium.

## Evidence against the claim

- The contract resolves on one exact future minute close, not on current spot or any intraday high.
  - Source: Polymarket rules source note.
  - Why it matters causally: a temporary or final selloff into the deadline would fully reverse the outcome.
  - Direct or indirect: direct for mechanism risk.
  - Weight: high.

- Several days remain, which is enough time for BTC to move more than the current cushion in a volatile market.
  - Source: timing structure implied by case dates plus current price context.
  - Why it matters causally: crypto can move several percent quickly, especially over weekends or macro shocks.
  - Direct or indirect: indirect/contextual.
  - Weight: medium-high.

- Binance-specific print risk remains possible even if broader BTC pricing stays healthier elsewhere.
  - Source: contract settlement mechanics.
  - Why it matters causally: settlement is venue-specific.
  - Direct or indirect: direct mechanism risk.
  - Weight: medium.

## Ambiguous or mixed evidence

- Current cushion is large enough to justify a strong Yes lean, but not so large that tail volatility can be ignored over a multi-day horizon.

## Conflict between inputs

There is little factual conflict. The main disagreement is weighting-based: whether the current 4.7k cushion should be treated as nearly decisive or still quite vulnerable given the exact-minute-close rule.

## Key assumptions

- BTC remains above 70,000 on Binance through the specific deadline minute.
- No Binance-specific dislocation creates a misleading sub-70k print at the exact close.

## Key uncertainties

- Short-horizon BTC volatility between now and April 20 noon ET.
- Whether macro or crypto-specific news introduces a downside break large enough to erase the cushion.

## Disconfirming signals to watch

- Sustained move down toward 71k-72k before the deadline.
- Evidence of exchange-specific dislocation on Binance.
- Increased realized volatility or sharp risk-off catalysts.

## What would increase confidence

- Continued Binance closes materially above 70k into April 19-20.
- Repeated cross-venue confirmation that Binance remains aligned with broader market pricing.

## Net update logic

The evidence supports a high-probability Yes because the governing venue already sits well above threshold and the contract is simple once the mechanism is understood. The main downweight comes from path dependence: this is a future exact-minute close market, so current comfort does not eliminate downside tail risk.

## Suggested downstream use

Use as forecast update and Orchestrator synthesis input, with emphasis on residual exact-minute-close risk rather than questioning the primary direction.