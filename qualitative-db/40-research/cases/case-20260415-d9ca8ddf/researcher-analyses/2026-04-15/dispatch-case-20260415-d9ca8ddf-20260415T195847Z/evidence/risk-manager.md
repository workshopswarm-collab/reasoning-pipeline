---
type: evidence_map
case_key: case-20260415-d9ca8ddf
dispatch_id: dispatch-case-20260415-d9ca8ddf-20260415T195847Z
research_run_id: 1b1ff630-2533-4f23-8628-6940abcb378b
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
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
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["risk-manager.md", "risk-manager.sidecar.json"]
tags: ["btc", "binance", "evidence-map", "stress-test"]
---

# Summary

This evidence map nets the live price cushion against the narrow-resolution timing and venue risks embedded in the contract.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for April 17, 2026 at 12:00 ET close above 72,000?

## Current lean

Lean Yes, but less confidently than the market.

## Prior / starting view

Starting view was that a market priced around 93% Yes probably reflected a substantial live spot cushion, but needed stress-testing because the contract is exact-minute and exact-venue sensitive.

## Evidence supporting the claim

- **Binance live spot above strike by ~3.9%**  
  - Source: `2026-04-15-risk-manager-binance-and-coingecko-price-check.md`  
  - Why it matters: the contract only needs BTC to avoid a moderate one-day drawdown.  
  - Direct or indirect: direct venue evidence.  
  - Weight: high.

- **Recent Binance 1-minute closes consistently above 72k during verification**  
  - Source: `2026-04-15-risk-manager-binance-and-coingecko-price-check.md`  
  - Why it matters: confirms the spot cushion is not a stale single print.  
  - Direct or indirect: direct venue evidence.  
  - Weight: medium-high.

- **CoinGecko broadly matches Binance current price region**  
  - Source: `2026-04-15-risk-manager-binance-and-coingecko-price-check.md`  
  - Why it matters: reduces concern that Binance was showing a one-off abnormal price at the time checked.  
  - Direct or indirect: contextual.  
  - Weight: medium.

## Evidence against the claim

- **Exact-minute contract structure creates path risk**  
  - Source: `2026-04-15-risk-manager-polymarket-rules-and-market-state.md`  
  - Why it matters: BTC can trade above 72k generally and still fail if the noon ET candle closes below it.  
  - Direct or indirect: direct contract evidence.  
  - Weight: high.

- **Single-exchange settlement risk**  
  - Source: `2026-04-15-risk-manager-polymarket-rules-and-market-state.md`  
  - Why it matters: Binance BTC/USDT can diverge modestly from other venues at the relevant minute.  
  - Direct or indirect: direct contract evidence.  
  - Weight: medium.

- **BTC can move several percent in a day**  
  - Source: inference from current cushion plus live crypto volatility context recorded in the price-check note.  
  - Why it matters: a ~3.9% cushion is solid but not overwhelming for BTC over roughly 44 hours.  
  - Direct or indirect: contextual.  
  - Weight: medium-high.

## Ambiguous or mixed evidence

- **Market price around 93% Yes**  
  Strong crowd confidence supports Yes, but it may also reflect underpriced timing fragility because the contract looks simpler than it is.

## Conflict between inputs

There is little factual conflict. The main disagreement is weighting-based: whether a ~3.9% live cushion warrants something near 93% confidence given the exact noon ET Binance close requirement.

## Key assumptions

- BTC will not suffer a sufficiently large downside move before the relevant minute.
- Binance BTC/USDT will remain representative enough of broad BTC spot into settlement.
- Noon ET maps cleanly to the intended Binance 1-minute candle without operational ambiguity.

## Key uncertainties

- Short-horizon BTC volatility over the next ~44 hours.
- Whether any macro/headline shock hits before the April 17 noon ET mark.
- Whether Binance-specific microstructure or operational anomalies emerge at resolution.

## Disconfirming signals to watch

- BTC breaking below 74k and trending toward 72k before April 17.
- Large risk-off move in crypto overnight or during U.S. morning trading on April 17.
- Evidence of Binance-specific price dislocation or data-display ambiguity.

## What would increase confidence

- BTC remaining comfortably above 73.5k-74k into late April 16 / early April 17.
- Continued cross-venue alignment with no Binance-specific anomalies.
- Stable or improving price action approaching the noon ET settlement window.

## Net update logic

The live Binance price check supports a Yes lean, but the risk-manager adjustment is to discount the market's very high confidence because the contract settles on one exact minute and one exact venue. The main reason not to simply copy the market is that BTC does not need a catastrophic move to lose this contract; it needs only a moderate drawdown at the wrong time.

## Suggested downstream use

Use this as input for orchestrator synthesis and decision-maker review, especially on whether the current market price is slightly overconfident relative to the remaining path and operational risks.