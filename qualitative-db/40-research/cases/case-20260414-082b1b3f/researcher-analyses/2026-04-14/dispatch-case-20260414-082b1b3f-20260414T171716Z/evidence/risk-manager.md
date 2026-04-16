---
type: evidence_map
case_key: case-20260414-082b1b3f
dispatch_id: dispatch-case-20260414-082b1b3f-20260414T171716Z
research_run_id: 55161b68-a1d8-4a11-9380-579d5e0bf7f9
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: trading-markets
entity: sol
topic: solana-above-80-on-april-17
question: "Will the Binance SOL/USDT 1-minute candle labeled 12:00 ET on 2026-04-17 close above 80?"
driver: operational-risk
date_created: 2026-04-14
agent: risk-manager
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["sol", "solana"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-082b1b3f/researcher-analyses/2026-04-14/dispatch-case-20260414-082b1b3f-20260414T171716Z/personas/risk-manager.md"]
tags: ["evidence-map", "timing-risk", "settlement-mechanics"]
---

# Summary

Direct evidence supports a Yes lean because SOL is currently trading comfortably above 80 on Binance, but the market price appears to embed more confidence than a risk-manager should accept for a single-minute crypto threshold three days out.

## Question being evaluated

Will the Binance SOL/USDT 1-minute candle for 12:00 ET on 2026-04-17 have a final close strictly above 80?

## Current lean

Lean Yes, but less confidently than the market.

## Prior / starting view

Starting view: likely Yes given the 88.5% market-implied level and the threshold sounding low relative to recent SOL trading.

## Evidence supporting the claim

- Binance current spot around 85.25 on 2026-04-14.
  - direct source: Binance ticker/avgPrice APIs
  - causal relevance: gives current distance from strike
  - direct or indirect: direct
  - weight: high
- Recent 1-minute Binance candles clustered near 85.2-85.3 during the run.
  - direct source: Binance 1m klines API
  - causal relevance: shows the market was not merely printing one stale above-80 mark
  - direct or indirect: direct
  - weight: medium
- Recent daily closes mostly above 80, including 86.51 and 85.25 on the two latest sessions available.
  - direct source: Binance daily klines API
  - causal relevance: indicates the threshold is below recent trading regime rather than just barely crossed
  - direct or indirect: direct contextual
  - weight: medium
- Polymarket rules only require the specified minute close to be above 80, not a sustained period above 80.
  - direct source: Polymarket market rules page
  - causal relevance: lowers the bar relative to broader end-of-day or average-price conditions
  - direct or indirect: direct contract evidence
  - weight: high

## Evidence against the claim

- Resolution is still about three days away, and SOL only has a ~6.2% cushion over the threshold.
  - source: current Binance price versus strike
  - causal relevance: short-horizon crypto can move that much easily
  - direct or indirect: direct plus contextual volatility inference
  - weight: high
- Contract resolves on a single specified 1-minute close at 12:00 ET, increasing timing/path dependence.
  - source: Polymarket rule text
  - causal relevance: even temporary weakness exactly at noon can settle No
  - direct or indirect: direct contract evidence
  - weight: high
- Market-implied probability is extreme at 88.5%, which leaves little room for ordinary volatility, adverse headlines, or broad crypto drawdowns.
  - source: assignment current_price 0.885
  - causal relevance: indicates possible underpricing of uncertainty rather than directional error alone
  - direct or indirect: direct market baseline
  - weight: medium-high

## Ambiguous or mixed evidence

- Recent daily price action is supportive, but it can also signal realized volatility high enough that a several-percent move by settlement is normal rather than exceptional.
- Lack of a specific identified bearish catalyst cuts both ways: there is no obvious reason for an imminent breakdown, but crypto can reprice abruptly without a single clean catalyst.

## Conflict between inputs

There is no strong factual conflict. The main disagreement is weighting-based: the market appears to weight current above-threshold level more heavily than the remaining timing/path risk.

## Key assumptions

- Current price regime above 80 largely persists into April 17 noon ET.
- No exchange-specific or market-wide shock pushes SOL below 80 at the settlement minute.
- Binance API/current market state is a good proxy for the eventual Binance candle state three days later, though not a guarantee.

## Key uncertainties

- Short-horizon realized volatility between now and settlement.
- Whether noon ET on April 17 is a vulnerable intraday timing window for a dip.
- Whether any macro or crypto-specific catalyst emerges before resolution.

## Disconfirming signals to watch

- SOL losing the 83-82 area on Binance before April 17.
- A rapid broad crypto selloff with SOL beta amplifying downside.
- Volatility spikes that make a noon ET sub-80 close plausible even if the broader day remains mixed.

## What would increase confidence

- Continued Binance trading above 84 through April 16-17.
- Reduced realized intraday volatility into settlement.
- Additional confirmation that noon ET liquidity conditions do not create unusual one-minute dislocation risk.

## Net update logic

I started with a likely-Yes baseline because the market was already above the strike. Direct Binance checks confirmed that the threshold is indeed currently well below spot and that contract mechanics are clear. That kept the lean on Yes. The risk-manager adjustment is that a single-minute settlement three days away should not be priced almost like a settled market when the asset needs only a modest drawdown to flip the outcome.

## Suggested downstream use

- orchestrator synthesis input
- forecast update
- decision-maker review
