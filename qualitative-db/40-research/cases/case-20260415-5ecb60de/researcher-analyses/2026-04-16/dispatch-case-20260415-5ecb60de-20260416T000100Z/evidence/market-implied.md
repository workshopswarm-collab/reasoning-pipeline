---
type: evidence_map
case_key: case-20260415-5ecb60de
dispatch_id: dispatch-case-20260415-5ecb60de-20260416T000100Z
research_run_id: 2187d606-ae31-4a03-bd1c-a22b46c78fd9
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: tokens
entity: sol
topic: will-the-binance-sol-usdt-1-minute-candle-at-12-00-et-on-2026-04-19-close-above-80
question: "Will the Binance SOL/USDT 1-minute candle at 12:00 ET on 2026-04-19 close above 80?"
driver: reliability
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low-direct-conflict
action_relevance: high
related_entities: ["sol", "solana"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-5ecb60de/researcher-analyses/2026-04-16/dispatch-case-20260415-5ecb60de-20260416T000100Z/personas/market-implied.md"]
tags: ["evidence-netting", "threshold-contract", "binance"]
---

# Summary

The market is probably directionally right that Yes is more likely than No, but its 90% confidence appears a bit rich for a one-minute threshold contract with several days of crypto volatility still remaining.

## Question being evaluated

Will the Binance SOL/USDT 1-minute candle at 12:00 ET on April 19, 2026 close above 80?

## Current lean

Lean Yes, but below the market's current 90% implied probability.

## Prior / starting view

Started from the market prior: if traders price Yes at 90%, the burden is on a contrary view to explain why the remaining path to a sub-80 noon print is much larger than the market assumes.

## Evidence supporting the claim

- Binance spot around 84.87 with recent 1-minute candles clustered around 84.87-84.93.
  - direct source/note: `2026-04-16-market-implied-binance-solusdt-market-and-rule-check.md`
  - causal relevance: current settlement venue price is meaningfully above the threshold
  - direct or indirect: direct
  - weight: high

- Recent Binance daily closes all above 80 for the last 10 days returned.
  - direct source/note: `2026-04-16-market-implied-binance-solusdt-market-and-rule-check.md`
  - causal relevance: suggests current regime is mostly above threshold rather than barely touching it
  - direct or indirect: direct contextual
  - weight: medium-high

- CoinGecko corroboration near 84.93.
  - direct source/note: `2026-04-16-market-implied-coingecko-context-check.md`
  - causal relevance: reduces concern that Binance is showing an isolated anomalous print
  - direct or indirect: indirect/contextual
  - weight: low-medium

## Evidence against the claim

- The contract settles on one exact minute close, not average weekend price.
  - source/note: Polymarket rules in `2026-04-16-market-implied-binance-solusdt-market-and-rule-check.md`
  - causal relevance: one sharp intraday drop at the wrong moment is enough to lose
  - direct or indirect: direct rule interpretation
  - weight: high

- Current cushion over 80 is only roughly 4.9-6.2%, which is not huge for a high-beta crypto asset over ~3.7 days.
  - source/note: same Binance note, plus timing check from runtime
  - causal relevance: tail path to No is not negligible
  - direct or indirect: direct-plus-interpretive
  - weight: medium-high

- Recent 10-day daily data still contains intraday lows below or near the threshold, including 78.38 and 79.60 on older days.
  - source/note: Binance daily kline note
  - causal relevance: demonstrates sub-80 trading remains plausible in this regime
  - direct or indirect: direct
  - weight: medium

## Ambiguous or mixed evidence

- Consistent closes above 80 support Yes, but also may explain why the market is already expensive rather than mispriced.
- Lack of a clear bearish catalyst is supportive for Yes, but absence of catalyst is weaker than direct evidence about realized volatility.

## Conflict between inputs

There is no major factual conflict. The main disagreement is weighting-based: how much confidence should be assigned to a mid-80s spot price staying above 80 at one exact minute several days later?

## Key assumptions

- Current mid-80s trading is a durable enough cushion.
- Binance settlement mechanics will function normally.
- No major broad-crypto downside shock arrives before April 19 noon ET.

## Key uncertainties

- Short-horizon realized volatility between now and settlement.
- Whether a market already rich in Yes conviction is still efficient or mildly overextended.
- How much one-minute settlement-path risk should discount a seemingly comfortable spot cushion.

## Disconfirming signals to watch

- SOL trading down into the 81-82 zone before settlement.
- A broad crypto selloff led by BTC/ETH risk-off moves.
- Exchange or liquidity disruptions affecting Binance minute-close behavior.

## What would increase confidence

- Continued Binance trading in the mid-80s or higher into the final 24 hours.
- Evidence that intraday downside volatility is compressing rather than widening.
- Stable broader crypto tape with no obvious weekend risk catalyst.

## Net update logic

The market prior deserves respect because live Binance spot and recent daily behavior support a Yes lean. But after netting the exact-minute settlement mechanics and normal crypto path risk, the evidence supports a high Yes probability rather than an almost-done one.

## Suggested downstream use

Use as orchestrator synthesis input and as an audit trail for why this persona roughly agrees with the market direction while modestly discounting its confidence.