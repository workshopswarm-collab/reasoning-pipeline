---
type: evidence_map
case_key: case-20260415-1a345042
dispatch_id: dispatch-case-20260415-1a345042-20260415T223206Z
research_run_id: 830fd898-ad07-43df-b28f-ed89832dbb04
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-72-000-on-april-21
question: "Will the price of Bitcoin be above $72,000 on April 21?"
driver: operational-risk
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability", "liquidity"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-1a345042/researcher-analyses/2026-04-15/dispatch-case-20260415-1a345042-20260415T223206Z/personas/risk-manager.md"]
tags: ["evidence-map", "btc", "binance", "risk-manager"]
---

# Summary

The evidence leans Yes because BTC/USDT on Binance is currently well above 72,000 and the contract mechanics are clear, but the risk-manager adjustment is to discount the market slightly for timestamp-specific path risk and exchange-specific operational dependence.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-21 have a final Close price above 72,000?

## Current lean

Lean Yes, but less confidently than the market.

## Prior / starting view

Starting baseline was the market-implied 80.5% from current_price 0.805.

## Evidence supporting the claim

- Polymarket rules explicitly tie settlement to Binance BTC/USDT 1m close at noon ET on April 21.
  - source: Polymarket rules page / source note
  - why it matters causally: removes exchange/pair ambiguity
  - direct or indirect: direct
  - weight: high

- Live Binance verification on 2026-04-15 showed BTCUSDT around 74,989 to 75,013 in recent one-minute candles.
  - source: Binance public API / source note
  - why it matters causally: current level sits roughly 4.1% above threshold
  - direct or indirect: direct
  - weight: high

- A 1,000-minute sample of Binance 1m klines on 2026-04-15 had all closes above 72,000, with min 73,566.
  - source: Binance public API / source note
  - why it matters causally: suggests threshold is not currently near the margin
  - direct or indirect: direct
  - weight: medium

## Evidence against the claim

- The contract is about one exact one-minute close several days ahead, so path risk matters more than current spot alone.
  - source: Polymarket rules page / assumption note
  - why it matters causally: even a temporary dip at the wrong minute resolves No
  - direct or indirect: direct contract interpretation plus analytic implication
  - weight: high

- BTC is a volatile asset; a roughly 3,000 buffer can disappear over multiple trading days under routine crypto risk-off conditions.
  - source: contextual market knowledge plus liquidity/operational-risk framing
  - why it matters causally: the current cushion is meaningful but not remotely lock-safe
  - direct or indirect: contextual
  - weight: medium

- Binance-specific prints, outages, or microstructure dislocations could matter because the contract is exchange-specific rather than broad-market.
  - source: contract mechanics plus operational-risk driver
  - why it matters causally: even if broader BTC holds up, Binance-specific weakness can still settle No
  - direct or indirect: contextual
  - weight: medium

## Ambiguous or mixed evidence

- Market price itself is informative but may embed overconfidence because traders see a large current cushion and underweight timestamp-specific fragility.
- The sampled recent klines support Yes, but they do not directly describe volatility over the next five-plus days.

## Conflict between inputs

No major factual conflict. The main issue is weighting: whether current cushion deserves something near 80%+ confidence or should be discounted more for exact-minute and exchange-specific risk.

## Key assumptions

- Current BTC strength is persistent enough to survive until the observation minute.
- Noon ET maps cleanly to the Binance observation minute without hidden timezone ambiguity.
- Binance remains a reliable source surface at the relevant time.

## Key uncertainties

- Near-term BTC directional move over the next several days
- Intraday volatility into the precise noon ET observation minute
- Exchange-specific operational or microstructure anomalies on Binance

## Disconfirming signals to watch

- BTCUSDT losing most of the current cushion and trading back near 72,000 before April 21
- Macro or crypto-specific shock that increases realized volatility materially
- Signs that Binance price action is diverging from other major venues around the relevant period

## What would increase confidence

- BTC maintaining a multi-day buffer well above 72,000 into April 20-21
- Additional confirmation that Binance UI/API timestamp handling aligns cleanly with ET noon interpretation
- Continued normal exchange operation without incident

## Net update logic

The direct evidence is enough for a Yes lean, but not enough to fully accept the market's confidence. Current price support and clean rules do most of the work. The main downweight comes from the exact-minute structure and exchange-specific dependence, which create a failure mode where general bullishness is insufficient.

## Suggested downstream use

Use as an orchestrator synthesis input and as a caution against over-weighting current spot distance from threshold when the contract resolves on a single exact one-minute close.
