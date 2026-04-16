---
type: evidence_map
case_key: case-20260415-7253c25f
dispatch_id: dispatch-case-20260415-7253c25f-20260415T220737Z
research_run_id: 6baf41ff-d46f-416e-9e15-2f3a5d698638
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-21
question: "Will the price of Bitcoin be above $72,000 on April 21?"
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-7253c25f/researcher-analyses/2026-04-15/dispatch-case-20260415-7253c25f-20260415T220737Z/personas/risk-manager.md"]
tags: ["evidence-map", "btc", "timing-risk", "binance"]
---

# Summary

The net evidence still leans Yes because current Binance BTCUSDT is materially above 72k and the horizon is short, but the case is more fragile than the raw 80% market price suggests because settlement depends on one exact exchange-specific minute close.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-21 close strictly above 72,000?

## Current lean

Lean Yes, but with meaningful timing and venue-specific fragility.

## Prior / starting view

Starting from the market-implied 80%, the initial baseline is that the event is more likely than not because BTC is already above the threshold by several thousand dollars.

## Evidence supporting the claim

- Current Binance BTCUSDT around 75,079 on 2026-04-15.
  - source: source note `2026-04-15-risk-manager-binance-api-and-contract.md`
  - causal relevance: provides a live cushion of about 4.3% above the threshold.
  - direct vs indirect: direct snapshot from the relevant venue/pair.
  - weight: high.

- Short remaining horizon to the event date.
  - source: contract timing and explicit date conversion to 2026-04-21 12:00 ET / 16:00 UTC.
  - causal relevance: less time for trend deterioration than a longer-dated contract.
  - direct vs indirect: direct timing fact with indirect probabilistic implication.
  - weight: medium.

- Governing contract mechanics are clear and do not appear ambiguous.
  - source: Polymarket market page + Binance kline docs.
  - causal relevance: lowers legal/interpretive uncertainty around what counts.
  - direct vs indirect: direct for mechanics, neutral for price direction.
  - weight: medium.

## Evidence against the claim

- Settlement is based on one exact minute close, not broader price behavior.
  - source: Polymarket rules.
  - causal relevance: increases path dependence and makes transient weakness decisive.
  - direct vs indirect: direct.
  - weight: high.

- The threshold is strict: 72,000 exactly or below resolves No.
  - source: Polymarket rules.
  - causal relevance: removes tie/near-miss comfort and matters in a volatile asset.
  - direct vs indirect: direct.
  - weight: medium.

- Current evidence base is mostly contract-mechanics plus current spot, with limited independent directional evidence about BTC path over the next six days.
  - source: current research set.
  - causal relevance: market confidence may outrun evidence depth.
  - direct vs indirect: meta-evidentiary.
  - weight: medium.

## Ambiguous or mixed evidence

- Market pricing at 80% could reflect good aggregate information, but it can also reflect overconfidence in a simple “BTC is already above the line” narrative without enough respect for single-minute resolution risk.

## Conflict between inputs

No major factual conflict found. The key issue is weighting: how much to discount current above-threshold spot because of path/timing risk.

## Key assumptions

- Current ~75k pricing is a meaningful enough cushion to survive normal volatility into April 21 noon ET.
- Binance venue-specific behavior will not diverge materially from broader BTC pricing at the critical minute.
- No major macro or crypto-specific shock arrives before the event.

## Key uncertainties

- Short-run BTC volatility between now and the target minute.
- Whether a rapid drawdown or venue-specific wick hits the exact settlement minute.
- Whether current market confidence is too high relative to the evidence depth.

## Disconfirming signals to watch

- BTC losing 73k and failing to reclaim it before April 21.
- Broad crypto risk-off or macro shock into the event window.
- Binance-specific dislocation around the measurement minute.

## What would increase confidence

- BTC holding well above 72k into the final 24 hours.
- Continued Binance pricing consistency versus broader market references.
- Additional context showing recent volatility is modest relative to the current cushion.

## Net update logic

The largest positive update is simply that the relevant exchange/pair is already well above the threshold. The largest negative update is that the contract is unusually path dependent because only one one-minute close matters. Netting those, the case still leans Yes, but with more fragility than the headline 80% price implies.

## Suggested downstream use

Use this as an orchestrator synthesis input and as a warning not to treat the 80% price as a high-confidence layup.