---
type: evidence_map
case_key: case-20260416-969f7c01
dispatch_id: dispatch-case-20260416-969f7c01-20260416T013210Z
research_run_id: 4e7d083c-b8c1-42b2-8b29-6600d2f3e6b9
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: spot-market-structure
entity: ethereum
topic: will-the-binance-eth-usdt-1-minute-candle-closing-at-12-00-et-on-2026-04-17-close-above-2200
question: "Will the Binance ETH/USDT 1-minute candle closing at 12:00 ET on 2026-04-17 close above 2200?"
driver: operational-risk
date_created: 2026-04-15
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["ethereum"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: ["binance-global"]
proposed_drivers: ["timestamp-resolution-risk"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-969f7c01/researcher-analyses/2026-04-16/dispatch-case-20260416-969f7c01-20260416T013210Z/personas/risk-manager.md"]
tags: ["evidence-map", "fragility", "timing"]
---

# Summary

The netted evidence still favors Yes, but the main residual risk is not broad ETH directionality. It is concentrated in short-horizon path risk and narrow settlement mechanics.

## Question being evaluated

Whether Binance ETH/USDT will have a final close above 2200 for the 12:00 ET 1-minute candle on 2026-04-17.

## Current lean

Lean Yes with high but not near-certain confidence.

## Prior / starting view

Starting baseline was the market-implied view around 94.5%-95% Yes, suggesting traders see the threshold as comfortably in the money.

## Evidence supporting the claim

- Binance spot ticker showed ETHUSDT at 2353.68 at research time.
  - source: `2026-04-16-risk-manager-binance-spot-and-kline-verification.md`
  - causal relevance: threshold is about 153.68 points below current price.
  - direct vs indirect: direct settlement-adjacent evidence.
  - weight: high.

- Recent 1-hour Binance klines show ETH trading broadly in the low-to-mid 2300s rather than near 2200.
  - source: `2026-04-16-risk-manager-binance-spot-and-kline-verification.md`
  - causal relevance: suggests a meaningful cushion and no immediate evidence of threshold stress.
  - direct vs indirect: direct settlement-adjacent evidence.
  - weight: high.

- Polymarket contract language is clear on exchange, pair, threshold, and timezone.
  - source: `2026-04-16-risk-manager-polymarket-contract-and-market-state.md`
  - causal relevance: limits venue ambiguity and clarifies what all must hold for Yes.
  - direct vs indirect: direct contract evidence.
  - weight: medium.

## Evidence against the claim

- This is a narrow time-specific contract; only one minute at noon ET matters.
  - source: contract note and Binance docs note.
  - causal relevance: even a generally bullish ETH day can still resolve No if the settlement minute dips below threshold.
  - direct vs indirect: direct contract risk.
  - weight: high.

- Market price is extreme, so even moderate overlooked tail risk can make 95% too high.
  - source: Polymarket contract and market state note.
  - causal relevance: risk-manager lens should discount overconfidence where confidence relies on continued calm.
  - direct vs indirect: contextual.
  - weight: medium.

- Timestamp/UI interpretation risk is small but nonzero.
  - source: Binance docs note.
  - causal relevance: wrong candle selection or timezone confusion can matter in edge cases.
  - direct vs indirect: contextual/operational.
  - weight: low-to-medium.

## Ambiguous or mixed evidence

- No strong independent news catalyst was identified in this pass that obviously points to a regime break before settlement.
- Lack of a visible catalyst supports calm continuation somewhat, but absence of catalyst is not strong evidence in a 24-hour crypto window.

## Conflict between inputs

There is little factual conflict across the main inputs. The disagreement is mostly weighting-based: whether a ~7% cushion one day out deserves ~95% confidence or something lower to account for crypto path risk and narrow settlement timing.

## Key assumptions

- ETH remains materially above 2200 into the settlement minute.
- Binance candle interpretation remains operationally straightforward.
- No large macro/crypto shock occurs before noon ET.

## Key uncertainties

- Short-horizon realized volatility between now and settlement.
- Whether any overnight macro or crypto-specific event produces a sharp selloff.
- Exact practical retrieval/display convention for the noon ET candle in edge-case discussion.

## Disconfirming signals to watch

- ETH/USDT trades down toward 2250 or below ahead of settlement.
- Cross-crypto selloff intensifies overnight.
- Confusion or dispute emerges over which Binance 1-minute candle corresponds to 12:00 ET.

## What would increase confidence

- Another verification pass closer to settlement still showing ETH comfortably above 2200.
- Continued low intraday volatility with ETH holding above the low 2300s.

## Net update logic

The direct exchange evidence supports Yes, but the risk-manager discount comes from concentrated path/timing risk rather than from bearish directional evidence. That keeps the estimate high but modestly below the market.

## Suggested downstream use

Use as synthesis input and as an audit trail for why this persona slightly faded an extreme market probability without flipping the direction.