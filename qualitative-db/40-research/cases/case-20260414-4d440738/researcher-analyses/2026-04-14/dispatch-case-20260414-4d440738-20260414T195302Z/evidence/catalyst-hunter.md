---
type: evidence_map
case_key: case-20260414-4d440738
dispatch_id: dispatch-case-20260414-4d440738-20260414T195302Z
research_run_id: 6de363df-555d-4ab7-be15-d6c1c5ac005f
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-68k-on-april-20
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-20 be above 68000?"
driver: reliability
date_created: 2026-04-14
agent: catalyst-hunter
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["macro", "reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-4d440738/researcher-analyses/2026-04-14/dispatch-case-20260414-4d440738-20260414T195302Z/personas/catalyst-hunter.md"]
tags: ["evidence-map", "catalyst-analysis", "bitcoin"]
---

# Summary

This evidence map nets a short-horizon BTC threshold contract where contract mechanics are narrow and the current price cushion is meaningful.

## Question being evaluated

Whether the Binance BTC/USDT 1-minute candle at 12:00 ET on April 20, 2026 will close above 68,000.

## Current lean

Lean YES, but less confidently than the market price suggests.

## Prior / starting view

Starting view was that a 94% market for a six-day crypto threshold contract deserved skepticism and required a contract/timing audit plus an exchange-specific price check.

## Evidence supporting the claim

- Binance settlement venue currently shows BTC/USDT around 74.2k, more than 6k above the strike.
  - source: Binance API spot source note
  - causal relevance: gives the immediate cushion the market must lose before NO becomes likely
  - directness: direct
  - weight: high
- Recent Binance daily closes visible in the API response are also above 68k.
  - source: Binance API source note
  - causal relevance: suggests the threshold is not being cleared only by a transient spike
  - directness: direct
  - weight: medium
- The contract window is only six days, so absent a new shock, inertia favors the side already holding a sizable margin over the strike.
  - source: contract timing + current spot state
  - causal relevance: supports path dependence and limited time for a large adverse move
  - directness: mixed
  - weight: medium

## Evidence against the claim

- The contract resolves on one exact minute, not a daily average or weekly level.
  - source: Polymarket rules source note
  - causal relevance: increases sensitivity to intraday volatility and last-minute catalyst shocks
  - directness: direct
  - weight: high
- BTC can move several percent in a short period, especially around macro or crypto-specific news; an ~8% cushion is meaningful but not invulnerable.
  - source: contextual market structure knowledge plus need for extra verification
  - causal relevance: explains why 94% may overstate certainty
  - directness: indirect
  - weight: medium-high
- Weekend and Monday-morning timing create gap risk before the exact noon ET print.
  - source: calendar structure
  - causal relevance: fewer intervention points and more chance of fast repricing
  - directness: indirect
  - weight: medium

## Ambiguous or mixed evidence

- Macro calendar context points to ongoing sensitivity but the fetched CME FedWatch page did not provide a concrete dated catalyst inside this exact six-day window.
- CoinDesk markets fetch did not yield useful timely context beyond publisher identity, so it did not materially update the view.

## Conflict between inputs

There is little factual conflict. The main tension is weighting-based: current price cushion argues for YES, while the narrow single-minute settlement rule argues against assigning too much confidence.

## Key assumptions

- No major negative catalyst lands before Monday noon ET.
- Binance remains a usable and representative settlement source.
- BTC does not mean-revert sharply enough to test 68k by settlement.

## Key uncertainties

- Whether there is an underappreciated macro, regulatory, or crypto-specific headline risk between now and settlement.
- How much microstructure noise could matter if BTC drifts closer to the strike.

## Disconfirming signals to watch

- BTC quickly losing the low-72k to low-70k region.
- A sharp weekend selloff.
- Any exchange-specific disruption or broader risk-off shock.

## What would increase confidence

- BTC holding comfortably above 72k into the weekend.
- No meaningful negative catalyst emerging by Sunday night.
- Continued Binance trading stability with no venue-specific operational issues.

## Net update logic

The contract audit reduced the temptation to treat this as an easy terminal-direction call. The Binance price check then showed a large enough buffer that YES remains the base case. Net result: stay YES, but shade below the market because narrow-timestamp crypto contracts should not be priced as near-certainties unless the cushion is overwhelming or settlement is imminent.

## Suggested downstream use

Use as synthesis input for timing/catalyst weighting and for caution against over-trusting extreme market prices on narrow-resolution crypto threshold contracts.