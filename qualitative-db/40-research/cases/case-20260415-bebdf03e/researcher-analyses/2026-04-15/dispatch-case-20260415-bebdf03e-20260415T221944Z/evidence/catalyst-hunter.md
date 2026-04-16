---
type: evidence_map
case_key: case-20260415-bebdf03e
dispatch_id: dispatch-case-20260415-bebdf03e-20260415T221944Z
research_run_id: b5da4b4f-cc44-4354-949a-2fe5a30dcfe0
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-21
question: "Will the Binance BTC/USDT 12:00 PM ET 1-minute candle close on 2026-04-21 be above 72000?"
driver: operational-risk
date_created: 2026-04-15
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: ["short-horizon-crypto-volatility"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-bebdf03e/researcher-analyses/2026-04-15/dispatch-case-20260415-bebdf03e-20260415T221944Z/personas/catalyst-hunter.md"]
tags: ["evidence-map", "bitcoin", "timing"]
---

# Summary

Near-term evidence favors Yes because BTC is currently above the strike with a few days left, but the case remains sensitive to one sharp adverse catalyst because the contract resolves on a single minute candle at a single venue and timestamp.

## Question being evaluated

Will Binance BTC/USDT close above 72,000 on the 12:00 PM ET one-minute candle on April 21, 2026?

## Current lean

Lean Yes.

## Prior / starting view

Starting baseline was the market-implied probability around 81.5% Yes.

## Evidence supporting the claim

- Polymarket rule surface and ladder pricing show the 72k threshold as a high-probability but not near-certain outcome.
  - direct for contract mechanics, indirect for terminal truth
  - high weight because it defines the actual claim being priced
- Binance spot during the run was about 74,990, roughly 4% above the strike.
  - direct current-state evidence
  - high weight because the contract resolves on Binance
- Coinbase and CoinGecko were very close to Binance, reducing concern that the Binance print was an isolated anomaly.
  - indirect but independent contextual evidence
  - medium weight

## Evidence against the claim

- The resolution depends on one exact minute candle rather than a daily close or average.
  - direct contract-structure risk
  - medium-high weight because single-minute noise can matter
- BTC can move several percent in a few days, so the current buffer is meaningful but not huge.
  - contextual market-structure evidence
  - medium-high weight
- Any late negative macro or crypto-specific shock before Tuesday noon ET could reprice the market sharply.
  - catalyst/timing risk
  - medium weight

## Ambiguous or mixed evidence

- Adjacent ladder pricing implies a smooth distribution, which is sensible, but it does not tell us whether traders are underestimating tail downside over a six-day window.
- Cross-venue alignment is reassuring for current state but not decisive for settlement because Binance alone governs.

## Conflict between inputs

There is little factual conflict. The main disagreement is weighting-based: how much confidence current spot distance should receive versus the risk of a short-horizon downside shock.

## Key assumptions

- No major adverse catalyst hits before April 21 noon ET.
- Binance remains a usable and representative resolution venue.
- Short-horizon downside volatility does not exceed the current cushion in a sustained way.

## Key uncertainties

- Whether there is an underappreciated macro catalyst between now and settlement.
- Whether the market is slightly too complacent about single-minute settlement noise.

## Disconfirming signals to watch

- BTC losing 74k and failing to regain it.
- Large risk-off macro headline or sudden liquidation event.
- Binance-specific operational issue or visible price dislocation versus other venues.

## What would increase confidence

- BTC holding above 74k through the weekend.
- No major negative macro headlines before Tuesday.
- Continued cross-venue price alignment with Binance not lagging lower.

## Net update logic

The current lean remains Yes because direct current-state evidence puts BTC above the strike and the contract horizon is short. I downweight stronger bullishness because the market settles on one minute at one venue, and short-horizon crypto volatility can erase a 4% cushion.

## Suggested downstream use

Use as synthesis input for probability calibration and for identifying whether other personas have stronger evidence of a near-term negative catalyst.