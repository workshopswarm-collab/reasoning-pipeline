---
type: evidence_map
case_key: case-20260416-e0b8c17c
dispatch_id: dispatch-case-20260416-e0b8c17c-20260416T050131Z
research_run_id: 73723f3e-35c7-4229-b118-ca2b9c04b3b5
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-20
question: "Will the price of Bitcoin be above $72,000 on April 20?"
driver: operational-risk
date_created: 2026-04-16
agent: base-rate
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-e0b8c17c/researcher-analyses/2026-04-16/dispatch-case-20260416-e0b8c17c-20260416T050131Z/personas/base-rate.md"]
tags: ["evidence-map", "btc", "threshold-market"]
---

# Summary

The outside-view case is that a price already ~4% above the threshold with several recent closes above it should remain more likely than not to stay above over four days, but not at near-certainty because BTC routinely moves several percent over short horizons.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-20 have a final close above 72,000?

## Current lean

Lean Yes, but less bullish than the market.

## Prior / starting view

Starting base rate: short-dated crypto threshold markets should be favored if spot is already meaningfully above the strike, but four days is long enough that a few-percent move cannot be dismissed.

## Evidence supporting the claim

- Binance spot ticker showed BTCUSDT at 75,000 on 2026-04-16.
  - direct
  - high weight
  - matters because current distance from threshold is positive and nontrivial
- Recent Binance daily klines show several recent closes above 72k and recent highs in the mid-70ks.
  - contextual, exchange-consistent
  - medium weight
  - matters because it suggests the market is operating in a regime where 72k is not an outlier print
- Only four days remain until resolution.
  - structural / time-horizon logic
  - medium weight
  - matters because persistence often dominates absent a fresh shock

## Evidence against the claim

- The contract resolves on one specific minute close, not on average price, daily close, or weekly range.
  - direct rule effect
  - high weight
  - matters because narrow timing makes the event less certain than a broad "trades above" intuition
- BTC routinely moves several percent over a multi-day window.
  - contextual base-rate volatility consideration
  - high weight
  - matters because current cushion over 72k is only about 4.2%
- Market-implied probability is already 83.5%, leaving limited margin for error.
  - market context
  - medium weight
  - matters because extreme pricing deserves an extra verification pass and a skeptical outside-view check

## Ambiguous or mixed evidence

- CoinGecko contextual data are directionally consistent with Binance but are not the settlement source, so they add context more than decisive proof.

## Conflict between inputs

There was no major source conflict. The disagreement is mainly between the market's aggressiveness and a more conservative outside-view volatility adjustment.

## Key assumptions

- Recent above-72k trading regime is informative for the next four days.
- No major downside shock occurs before resolution.
- Binance settlement mechanics are applied exactly as described on Polymarket.

## Key uncertainties

- Intraday noon ET price path on April 20
- Near-term macro or crypto-specific volatility burst
- Whether price spends the next few days hovering close to the strike

## Disconfirming signals to watch

- Sustained move back below 72k on Binance
- Loss of 74k followed by failed reclaim attempts
- Sudden exchange or market microstructure stress

## What would increase confidence

- Continued Binance trading above 74k into the weekend
- Additional recent 1m/1h evidence showing stable support above 72k
- Absence of new downside macro shock

## Net update logic

The base rate starts from persistence because spot is already above the line and the horizon is short. I downweight the market slightly because the contract is a single-minute settle and BTC's short-horizon volatility is large enough that 83.5% feels somewhat rich relative to the available cushion.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review