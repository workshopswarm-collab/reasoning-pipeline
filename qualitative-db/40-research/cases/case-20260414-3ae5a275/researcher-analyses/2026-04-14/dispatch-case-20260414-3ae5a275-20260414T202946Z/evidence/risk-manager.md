---
type: evidence_map
case_key: case-20260414-3ae5a275
dispatch_id: dispatch-case-20260414-3ae5a275-20260414T202946Z
research_run_id: a6df7ab0-da5e-4153-866a-b4e8d8e43fe7
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-20
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-20 be above 70000?"
driver: operational-risk
date_created: 2026-04-14
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-3ae5a275/researcher-analyses/2026-04-14/dispatch-case-20260414-3ae5a275-20260414T202946Z/personas/risk-manager.md"]
tags: ["evidence-netting", "threshold-risk", "noon-print"]
---

# Summary

The evidence supports a Yes lean because BTC is already comfortably above 70k on the named exchange/pair, but the contract is fragile to one exact minute and one exact venue.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET 1-minute candle close on Apr. 20, 2026 finish above 70,000?

## Current lean

Lean Yes, but with meaningful haircut versus the market because the contract settles on a single noon ET minute close.

## Prior / starting view

Starting view was that the market was probably directionally right given the visible 85% price, but needed stress-testing because the contract is date-specific, exchange-specific, and at an extreme probability.

## Evidence supporting the claim

- Binance ticker check showed BTCUSDT around 74,306.57 at review time.
  - Direct.
  - High weight because Binance is the named settlement source.
- Recent Binance daily klines showed several closes above 70k and recent highs extending into the mid-70k range.
  - Direct for exchange price history, indirect for the exact settlement minute.
  - Medium-high weight because it shows current regime above threshold.
- Polymarket contract wording confirms no hidden multi-day averaging or non-Binance source substitution.
  - Direct for mechanics.
  - Medium weight because it removes some interpretation ambiguity.

## Evidence against the claim

- The contract resolves on one exact 1-minute candle close at noon ET, not on current price, daily close, or weekly average.
  - Direct contract fragility.
  - High weight.
- BTC can move several percent over a few days, and the current cushion above 70k is only modest in crypto terms.
  - Contextual inference from recent price range.
  - Medium-high weight.
- Binance-specific operational or market-structure noise could matter more than usual because a single minute on a single venue determines settlement.
  - Contextual mechanism risk.
  - Medium weight.

## Ambiguous or mixed evidence

- Recent strength above 70k helps the Yes case, but it may also be exactly why the market is overconfident about a narrow timestamp contract.

## Conflict between inputs

No major factual conflict across the checked sources. The disagreement is mainly weighting-based: whether current price cushion should justify an 85%+ confidence level for a single-minute, six-day-forward event.

## Key assumptions

- BTC remains materially above 70k into Apr. 20.
- No Binance-specific settlement anomaly meaningfully distorts the noon ET minute.
- The ET-to-Binance timestamp mapping will be handled as traders expect.

## Key uncertainties

- Near-term BTC volatility between now and Apr. 20.
- Whether market participants are underpricing one-minute path risk.
- Exact operational/timing implementation details at settlement minute.

## Disconfirming signals to watch

- BTC losing 72k then 70k before Apr. 20.
- Repeated intraday probes of 70k.
- Binance-specific pricing dislocations or service issues.

## What would increase confidence

- Additional days of Binance closes well above 70k.
- Lower realized volatility into settlement.
- A clean pre-settlement check confirming stable Binance pricing around the noon ET window.

## Net update logic

The main upward update comes from direct Binance price context: BTC is already above the threshold by a nontrivial amount. The main downward haircut comes from contract structure: this is not a broad directional call but a single-minute threshold event. That makes an 85% market price plausible but slightly too confident.

## Suggested downstream use

Use as forecast update and orchestrator synthesis input, with emphasis on path/timing fragility rather than broad directional bearishness.