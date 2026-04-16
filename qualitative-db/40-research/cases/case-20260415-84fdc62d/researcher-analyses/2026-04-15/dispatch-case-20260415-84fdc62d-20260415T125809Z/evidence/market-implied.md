---
type: evidence_map
case_key: case-20260415-84fdc62d
dispatch_id: dispatch-case-20260415-84fdc62d-20260415T125809Z
research_run_id: 3defca01-d4dc-4c55-97e5-39a6f3cb76eb
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-20
question: "Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-20 close above 70000?"
driver: operational-risk
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low-moderate
action_relevance: high
related_entities: ["binance", "bitcoin"]
related_drivers: ["operational-risk"]
proposed_entities: []
proposed_drivers: ["exchange-specific settlement microstructure"]
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "market-implied", "bitcoin"]
---

# Summary

The market's 87.5% Yes price looks directionally justified by current spot context, but not obviously cheap: most of the remaining gap to certainty is explained by exact-minute settlement risk, ordinary BTC volatility, and Binance-specific execution/resolution mechanics.

## Question being evaluated

Whether BTC/USDT on Binance will close above 70000 in the 12:00 ET one-minute candle on 2026-04-20.

## Current lean

Lean Yes, with a probability slightly above the market but still in the same band.

## Prior / starting view

Start from the market prior: 87.5% Yes from the live contract.

## Evidence supporting the claim

- Polymarket rule page and ladder: 70k trades around 86% while 74k is around 52%, implying crowd expectation for April 20 noon ET is meaningfully above 70k. Direct for baseline; medium-high weight.
- Secondary price context: CoinDesk snippet shows BTC around 74200 on Apr 15 08:32 EDT; Binance search snippet shows BTC/USDT around 74360. Direct/contextual for current cushion above strike; medium weight.
- Only five days remain, so the needed adverse move from ~74k to sub-70k is material rather than trivial. Contextual inference; medium weight.

## Evidence against the claim

- This is a single-minute, single-exchange contract, so resolution can fail even if the broader BTC thesis remains bullish. Direct contract-structure risk; high weight.
- BTC can move several percent in days; a ~6% cushion is good but not untouchable in crypto. Contextual volatility consideration; medium-high weight.
- Extreme market probabilities can overstate confidence when traders anchor to spot and underweight path/time-specific fragility. Interpretive counterpoint; medium weight.

## Ambiguous or mixed evidence

- The price ladder could mean strong information aggregation, but it could also partly reflect retail preference for obvious in-the-money strikes.
- Binance search snippet is useful as extra verification but is not a clean archival source note by itself.

## Conflict between inputs

There is no hard factual conflict. The disagreement is mainly weighting-based: how much discount should be applied for exact-minute settlement and exchange-specific microstructure versus the current several-thousand-dollar cushion.

## Key assumptions

- Current mid-74k price context is representative enough to anchor a 5-day view.
- No major downside catalyst hits before April 20 noon ET.
- Binance BTC/USDT remains close enough to broader BTC spot that exchange-specific distortion is not the deciding factor.

## Key uncertainties

- Near-term BTC realized volatility over the next five days.
- Whether the April 20 noon ET minute is unusually exposed to cross-market flows or event timing.
- Binance-specific data/display or microstructure quirks at resolution time.

## Disconfirming signals to watch

- BTC losing 72k decisively before April 20.
- A sudden macro risk-off move or crypto-specific negative catalyst.
- Evidence that Binance BTC/USDT is trading materially weaker than other spot references.

## What would increase confidence

- Independent confirmation from another live price source or derivatives/implied-vol source showing downside tail risk remains modest.
- Continued BTC stability above ~73k into the final 24-48 hours.

## Net update logic

Starting from the market prior was appropriate. External verification did not overturn the crowd view; it mainly confirmed that BTC is currently well above the 70k threshold. The only meaningful haircut comes from contract structure and crypto volatility, not from contrary spot evidence.

## Suggested downstream use

Use as orchestrator synthesis input and as an audit trail explaining why a market-respecting researcher stayed close to, but not blindly at, the live price.
