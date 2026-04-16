---
type: evidence_map
case_key: case-20260414-4d440738
dispatch_id: dispatch-case-20260414-4d440738-20260414T195302Z
research_run_id: b5b9b1cb-398a-435e-97b6-9e89fa15e0e6
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-68k-on-april-20
question: "Will the price of Bitcoin be above $68,000 on April 20?"
driver: operational-risk
date_created: 2026-04-14
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-4d440738/researcher-analyses/2026-04-14/dispatch-case-20260414T195302Z/personas/risk-manager.md"]
tags: ["evidence-netting", "timing-risk", "crypto"]
---

# Summary

The evidence nets to a high-probability "Yes" lean, but the residual risk is not trivial because settlement is a single Binance one-minute close several days away and the market is already priced near certainty.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-20 close above 68,000?

## Current lean

Lean Yes, but less confidently than the market.

## Prior / starting view

Starting view was that Yes was likely because BTC was already well above the strike, but a risk-manager pass should haircut the near-certain market confidence for timestamp, venue, and volatility risk.

## Evidence supporting the claim

- Binance spot price around 74.2k on 2026-04-14, roughly 9% above strike. Direct, high weight.
- Recent Binance daily closes mostly above 68k; 11 of the last 14 daily closes were above the threshold. Direct/contextual, medium-high weight.
- Cross-exchange spot references from CoinGecko, Coinbase, and CNBC all clustered near 74.2k-74.3k. Indirect/contextual, medium weight.

## Evidence against the claim

- Contract resolves on one exact minute and one exact venue, so path risk is much higher than a broad weekly-above-threshold interpretation. Direct contract risk, high weight.
- BTC daily volatility is still meaningful; recent 29-day daily return standard deviation was about 2.33%, so an 8-9% downswing over several days is tail-ish but absolutely plausible in crypto. Direct/contextual, medium-high weight.
- BTC traded in the high 66k to 67k range earlier this month, proving the strike is not absurdly far away in current regime terms. Direct/contextual, medium weight.

## Ambiguous or mixed evidence

- Cross-venue alignment today is reassuring, but it does not answer whether Binance will remain aligned at the exact settlement minute.
- Strong current momentum can either support continuation above 68k or increase reversal risk after a sharp run-up.

## Conflict between inputs

There is little factual conflict in the source set. The main disagreement is weighting-based: how much probability should be deducted from the obvious in-the-money status to account for single-minute and venue-specific resolution risk.

## Key assumptions

- BTC retains enough buffer above 68k that ordinary volatility does not threaten the noon ET close.
- Binance remains a usable and representative settlement venue on April 20.
- No new macro or crypto-specific shock creates a fast drawdown into the resolution window.

## Key uncertainties

- Intraday price level at exactly 12:00 ET on April 20.
- Event risk between now and resolution.
- Potential Binance-specific basis or operational noise.

## Disconfirming signals to watch

- BTCUSDT losing 72k, then 70k, on sustained basis before the weekend.
- Material Binance-specific disruption or unusual BTC/USDT dislocation.
- A sharp risk-off macro impulse that compresses crypto broadly into April 20.

## What would increase confidence

- Continued daily closes above 72k into April 18-19.
- Stable cross-exchange alignment with no Binance-specific anomalies.
- Lower realized volatility into the resolution window.

## Net update logic

The direct source-of-truth evidence makes Yes the base case. The main downward adjustment versus the 93.5% market price comes from contract interpretation and volatility discipline, not from a competing bearish thesis. I downweighted generic bullish sentiment and upweighted the single-minute settlement mechanic because extreme market prices can hide tail-risk concentration.

## Suggested downstream use

forecast update
