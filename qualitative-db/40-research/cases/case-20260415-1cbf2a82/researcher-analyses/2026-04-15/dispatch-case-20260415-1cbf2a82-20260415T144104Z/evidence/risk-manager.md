---
type: evidence_map
case_key: case-20260415-1cbf2a82
dispatch_id: dispatch-case-20260415-1cbf2a82-20260415T144104Z
research_run_id: a008134c-5a81-4bf2-95f7-d9bf32bb2829
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: spot-price
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-72-000-on-april-17
question: "Will the price of Bitcoin be above $72,000 on April 17?"
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
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-1cbf2a82/researcher-analyses/2026-04-15/dispatch-case-20260415-1cbf2a82-20260415T144104Z/personas/risk-manager.md"]
tags: ["evidence-map", "btc", "risk-manager"]
---

# Summary

The evidence favors Yes because Binance spot is currently well above $72,000, but the main risk-manager update is that the market appears somewhat overconfident relative to the remaining two-day volatility and the narrow exact-minute settlement condition.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17 have a final Close price above $72,000?

## Current lean

Yes lean, but less confident than the market.

## Prior / starting view

Starting from the market-implied baseline of about 84.5% Yes.

## Evidence supporting the claim

- Binance spot on April 15 was about $73,988.97.
  - source: Binance ticker/source note
  - why it matters causally: same exchange and same trading pair as settlement source
  - direct or indirect: direct contextual price evidence, though not final settlement evidence
  - weight: high

- Recent Binance 1-minute closes sampled around the check remained clustered near $74k.
  - source: Binance klines/source note
  - why it matters causally: shows BTC was not just momentarily above the threshold
  - direct or indirect: direct contextual evidence
  - weight: medium

- CoinGecko cross-check near $74,054 broadly confirmed BTC was trading comfortably above $72k across broader market data.
  - source: CoinGecko/source note
  - why it matters causally: reduces concern that Binance price check was anomalous
  - direct or indirect: indirect/contextual for this contract
  - weight: low to medium

## Evidence against the claim

- The contract resolves on a single exact one-minute Binance close at 12:00 ET on April 17, not on average price or broad daily trading range.
  - source: Polymarket rules/source note
  - why it matters causally: increases path dependency and exact-minute noise risk
  - direct or indirect: direct contract evidence
  - weight: high

- The cushion over the threshold is only about $1,989, roughly 2.7% from checked Binance spot.
  - source: combined from Binance price and contract threshold
  - why it matters causally: a normal crypto drawdown over two days could erase that margin
  - direct or indirect: direct arithmetic from direct price evidence
  - weight: high

- Market-implied confidence above 84% may underweight generic crypto volatility over a two-day horizon.
  - source: assignment price plus contract timing
  - why it matters causally: embedded confidence may be too aggressive for such a narrow settlement condition
  - direct or indirect: interpretive
  - weight: medium

## Ambiguous or mixed evidence

- CoinMarketCap page fetch was available but was mostly generic asset background and not very useful for near-term directional forecasting.
- Lack of a robust recent-news catalyst in this run cuts both ways: no bearish trigger identified, but also limited support for treating the next two days as unusually stable.

## Conflict between inputs

There is little factual conflict. The main disagreement is weighting-based: current spot level supports Yes, while the settlement mechanics and remaining volatility argue against paying full market confidence.

## Key assumptions

- Current Binance spot is informative for the April 17 noon ET close.
- No major downside catalyst emerges before settlement.
- Candle-time mapping between ET noon and Binance timestamps is straightforward at settlement.

## Key uncertainties

- Short-horizon BTC volatility over the next two days.
- Any macro or crypto-specific headline shock before noon ET April 17.
- Whether intraminute path noise near settlement could matter if BTC drifts toward the line.

## Disconfirming signals to watch

- BTC trading back under $73k with momentum.
- Macro risk-off shock or crypto-specific selloff before settlement.
- Settlement-minute precheck showing BTC hovering near or below $72k.

## What would increase confidence

- Another verification closer to settlement still showing Binance BTC/USDT comfortably above $72k.
- Evidence of stable price action and no emerging downside catalyst.

## Net update logic

The key update is not directional reversal but confidence haircut. Same-exchange spot above the threshold supports Yes, but the market's mid-80s confidence looks somewhat rich for a one-minute binary crypto settlement with only a ~2.7% cushion two days out.

## Suggested downstream use

Use as orchestrator synthesis input and as a caution against over-relying on a high market-implied probability without accounting for exact-minute settlement risk.