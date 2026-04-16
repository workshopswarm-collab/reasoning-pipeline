---
type: evidence_map
case_key: case-20260416-f29db686
dispatch_id: dispatch-case-20260416-f29db686-20260416T004058Z
research_run_id: a7e2708b-5f64-4919-97d2-073867d17ad8
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-74-000-on-april-17
question: "Will the price of Bitcoin be above $74,000 on April 17?"
driver: reliability
date_created: 2026-04-16
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: ["intraday-timing-risk"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-f29db686/researcher-analyses/2026-04-16/dispatch-case-20260416-f29db686-20260416T004058Z/personas/variant-view.md"]
tags: ["evidence-map", "btc", "binance", "intraday"]
---

# Summary

The net evidence supports a mildly bearish variant relative to the market: BTC is currently above the strike, but the contract resolves on a narrow Binance-specific one-minute close tomorrow at noon ET, and current distance from strike is small relative to recent realized range.

## Question being evaluated

Will Binance BTC/USDT print a final 12:00 ET one-minute candle close above 74,000 on April 17, 2026?

## Current lean

Slight lean No versus market pricing, even though spot is currently above strike.

## Prior / starting view

Starting baseline was the market-implied probability from assignment context, 60.5%, which suggests modest favoritism toward Yes.

## Evidence supporting the claim

- Binance spot during research was around 74,792, above the 74,000 threshold.
  - source: source note on Binance API and live price
  - causal relevance: current above-strike level gives Yes a real path without requiring a major rally
  - direct/indirect: direct current-price evidence
  - weight: medium

- Binance 24h high reached about 75,425.
  - source: source note on Binance API and live price
  - causal relevance: proves market recently traded comfortably above the threshold
  - direct/indirect: direct historical snapshot evidence
  - weight: low-to-medium

## Evidence against the claim

- Polymarket rules require the exact Binance BTC/USDT 12:00 ET one-minute close, not broad same-day price direction.
  - source: Polymarket rules source note
  - causal relevance: narrow resolution mechanics add timing/path sensitivity
  - direct/indirect: direct contract evidence
  - weight: high

- Current price cushion is only about 792 points, roughly 1.1% above strike.
  - source: Binance API note
  - causal relevance: small cushion can be erased by ordinary intraday movement
  - direct/indirect: direct current-price evidence
  - weight: medium-high

- Binance 24h range of about 73,514 to 75,425 spans both sides of the strike.
  - source: Binance API note
  - causal relevance: strike lies inside normal realized volatility rather than safely below market
  - direct/indirect: direct recent range evidence
  - weight: medium-high

## Ambiguous or mixed evidence

- A current above-strike price is supportive, but not decisively so because the contract is path-specific and next-day timed.
- Market price itself may embody some of this timing complexity already, which limits the size of any disagreement edge.

## Conflict between inputs

There is little factual conflict. The main disagreement is weighting-based:
- market appears to weight current above-strike status and broad bullish continuation
- variant view weights timing/path sensitivity and exchange-specific close risk more heavily

Evidence that would resolve this better:
- historical distribution of next-day noon ET Binance closes conditional on current distance above strike
- evidence of specific scheduled catalysts before noon ET April 17

## Key assumptions

- Intraday timing risk is underweighted by the market.
- No major bullish catalyst arrives before resolution.
- Binance-specific basis and minute-close noise remain material enough that a 1.1% cushion is not comfortable.

## Key uncertainties

- Lack of a fuller historical volatility / conditional distribution study.
- Possibility of meaningful macro or crypto-specific news before noon ET April 17.
- Possible gap between API interpretation and exact UI candle presentation, though likely small.

## Disconfirming signals to watch

- BTC sustaining >75.5k into the April 17 morning ET session.
- Strong bullish catalyst that meaningfully reprices BTC before noon.
- Evidence that Binance noon ET close tends to track current above-strike positioning more reliably than assumed.

## What would increase confidence

- Historical data showing many >1% moves over comparable windows into noon ET closes.
- Confirmation of no material scheduled catalyst before the decision point.
- A clearer independent contextual source on BTC realized volatility over similar horizons.

## Net update logic

The main update from baseline is not a new macro thesis on Bitcoin. It is a contract-specific reframing: because the question resolves on one exact Binance minute close tomorrow, current above-strike trading is less decisive than it first appears. The market may still be directionally right, but looks somewhat overconfident versus the narrowness of the resolution event and the modest distance from strike.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review