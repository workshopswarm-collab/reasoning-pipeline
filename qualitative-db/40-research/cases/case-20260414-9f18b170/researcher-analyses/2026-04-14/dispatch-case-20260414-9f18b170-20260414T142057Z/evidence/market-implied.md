---
type: evidence_map
case_key: case-20260414-9f18b170
dispatch_id: dispatch-case-20260414-9f18b170-20260414T142057Z
research_run_id: abcd3038-d43e-479d-b74c-2b509a6fb3d6
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-bitcoin-reach-76-000-april-13-19
question: "Will Bitcoin reach $76,000 April 13-19?"
date_created: 2026-04-14
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["binance-intraperiod-threshold-touch"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-9f18b170/researcher-analyses/2026-04-14/dispatch-case-20260414-9f18b170-20260414T142057Z/personas/market-implied.md"]
tags: ["evidence-map", "bitcoin", "polymarket", "threshold-market"]
driver:
---

# Summary

The market's high-Yes probability looks largely justified because the contract is a Binance 1-minute high touch market and BTC is already trading within roughly 0.4% of the threshold early in the allowed window.

## Question being evaluated

Will Bitcoin reach $76,000 at any point during Apr 13-19 under the contract's Binance 1-minute high rule?

## Current lean

Lean Yes, with only a modest discount versus the market.

## Prior / starting view

Starting baseline was the market-implied probability of about 91.5% Yes.

## Evidence supporting the claim

- **Polymarket embedded rules metadata** — direct for contract mechanics; high weight.
  - Why it matters: clarifies this is any Binance 1m candle high, not a close-above requirement.
  - Direct vs indirect: direct for resolution mechanics.
- **Binance 24hr ticker** showing last around 75,701 and 24h high around 75,715 — direct contextual market evidence; high weight.
  - Why it matters: BTC is already very near the threshold on the governing venue.
- **Coinbase and Kraken spot checks around 75.7k** — contextual corroboration; medium weight.
  - Why it matters: confirms the price level is not a single-venue anomaly.
- **Time remaining in the Apr 13-19 window** — indirect but important; medium weight.
  - Why it matters: several trading days remain for a relatively small additional move.

## Evidence against the claim

- **Binance had not yet printed 76,000 at check time** — direct negative evidence; high weight.
  - Why it matters: the contract is not already settled by the observed data.
- **Threshold-touch markets are path dependent** — indirect but meaningful; medium weight.
  - Why it matters: being near 76k does not guarantee a qualifying 1m high will occur if momentum fades.

## Ambiguous or mixed evidence

- Cross-exchange prices near 75.7k help on level, but only Binance BTC/USDT matters for settlement.
- The market price itself may embed better intraday volatility intuition than a static spot snapshot, but this cannot be directly audited from the public page alone.

## Conflict between inputs

No major factual conflict. The only meaningful tension is between a very high market price and the still-unmet threshold at observation time.

## Key assumptions

- Near-threshold BTC conditions plus multiple remaining days make a 76k Binance 1m high likely.
- Binance remains representative enough of broader BTC price action to capture any marginal upside test.

## Key uncertainties

- Short-horizon realized volatility from here.
- Whether a reversal interrupts the expected threshold test.

## Disconfirming signals to watch

- BTC loses 75k and remains weak.
- Binance repeatedly tops out below 76k while time decays.
- Material spread emerges between Binance and other major venues in a way that hurts settlement odds.

## What would increase confidence

- A verified Binance print above 75.9k or 76k.
- Additional direct Binance kline evidence showing repeated threshold approaches.

## Net update logic

The evidence keeps me near the market rather than materially below it. The crucial update is not generic bullishness but the combination of (1) a touch-style contract, (2) Binance as the source of truth, and (3) BTC already sitting near 75.7k early in the qualifying period.

## Suggested downstream use

- Forecast update
- Orchestrator synthesis input
- Retrospective evaluation of extreme-probability threshold markets