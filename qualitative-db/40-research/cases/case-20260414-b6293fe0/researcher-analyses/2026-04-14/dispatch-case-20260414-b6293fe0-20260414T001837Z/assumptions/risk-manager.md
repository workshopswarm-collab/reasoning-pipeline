---
type: assumption_note
case_key: case-20260414-b6293fe0
dispatch_id: dispatch-case-20260414-b6293fe0-20260414T001837Z
research_run_id: 38eb6f92-1ed9-4121-9c0c-4daf22c0fafe
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin-weekly-hit-price
entity: bitcoin
topic: will-bitcoin-reach-74-000-april-13-19
question: "Will Bitcoin reach $74,000 April 13-19?"
driver: operational-risk
date_created: 2026-04-14
agent: Orchestrator
status: active
certainty: high
importance: high
time_horizon: "immediate resolution window"
related_entities: ["bitcoin", "polymarket"]
related_drivers: ["operational-risk", "liquidity"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["assumption", "resolution-source", "narrow-contract"]
---

# Assumption

The contract is effectively decided once a qualifying Binance BTC/USDT 1-minute candle high at or above 74,000 has already occurred during the Apr 13-19 ET window.

## Why this assumption matters

The market is priced near certainty. That is only justified if the relevant threshold touch has already happened under the contract's exact venue-and-candle definition, not merely if BTC looks likely to trade there later in the week.

## What this assumption supports

- A near-certain `Yes` probability estimate.
- A view that remaining risk is mostly operational / interpretation risk rather than market-direction risk.
- Agreement with the market's extreme confidence rather than fading it.

## Evidence or logic behind the assumption

- Polymarket's rules explicitly define success as any Binance BTC/USDT 1-minute candle high >= 74,000 during the stated ET window.
- Polymarket embedded state showed the 74k market trading around 99.95% and included a proposed resolution object consistent with `Yes`.
- Independent market-data checks showed BTC trading above 74k in the relevant period, making it highly likely the qualifying Binance print exists.

## What would falsify it

- Evidence that no qualifying Binance BTC/USDT 1-minute high >= 74,000 occurred in the ET window.
- Evidence that the apparent 74k+ move came from another venue/pair only and not Binance BTC/USDT.
- A material rules nuance or dispute invalidating the seemingly qualifying print.

## Early warning signs

- The market price dropping sharply away from certainty.
- Polymarket removing or disputing a proposed resolution.
- A direct Binance 1-minute chart check showing highs below 74,000 despite aggregated sources printing above it.

## What changes if this assumption fails

If this assumption fails, the case reverts from "almost certainly already happened" to a live path-dependent weekly price-touch question, and the probability would drop materially because BTC was trading back in the low 70ks after the spike.

## Notes that depend on this assumption

- Main persona finding for this run.
- Evidence map for this run.