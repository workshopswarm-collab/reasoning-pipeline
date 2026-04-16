---
type: evidence_map
case_key: case-20260415-7b143efd
dispatch_id: dispatch-case-20260415-7b143efd-20260415T132144Z
research_run_id: 20911a87-71cd-48c0-8cdc-124dfa4e259b
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: exchange-resolution
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-70-000-on-april-20
question: "Will the price of Bitcoin be above $70,000 on April 20?"
driver: operational-risk
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: ["timing-risk"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-7b143efd/researcher-analyses/2026-04-15/dispatch-case-20260415-7b143efd-20260415T132144Z/personas/risk-manager.md"]
tags: ["evidence-map", "bitcoin", "binance", "timing"]
---

# Summary

The evidence nets to Yes-leaning but less confident than the market because the contract is both threshold-based and timestamp-specific. Current spot level supports Yes; exact-minute settlement mechanics are the main risk discount.

## Question being evaluated

Will Binance BTC/USDT print a final close above 70,000 on the 1-minute candle corresponding to 12:00 ET on April 20, 2026?

## Current lean

Yes, with a high but not extreme probability.

## Prior / starting view

Starting view was that a market at 0.88 likely reflected spot already being comfortably above 70k, but might be too confident if traders were underweighting exact-minute settlement risk.

## Evidence supporting the claim

- **Current Binance spot materially above threshold**  
  - source: `2026-04-15-risk-manager-binance-klines-and-spot-context.md`  
  - direct evidence  
  - why it matters: current spot near 74.27k leaves roughly a 4.27k cushion versus the threshold.  
  - weight: high

- **Recent Binance 1m closes cluster above 74.27k**  
  - source: `2026-04-15-risk-manager-binance-klines-and-spot-context.md`  
  - direct evidence for current exchange state  
  - why it matters: the same data type used for settlement is presently above the line, not just an external index.  
  - weight: medium-high

- **Contract source-of-truth is exchange-native and operationally legible**  
  - sources: Polymarket rules note + Binance docs note  
  - direct on mechanics  
  - why it matters: less ambiguity than a vague media-source contract; operational path to settlement is clear enough.  
  - weight: medium

## Evidence against the claim

- **Single-minute timestamp risk**  
  - source: Polymarket rules note  
  - direct on contract mechanics  
  - why it matters: BTC can spend most of the day above 70k and still resolve No if the noon ET 1m close dips below.  
  - weight: high

- **Short horizon still leaves room for a >5 percent crypto drawdown**  
  - source: inference from current cushion plus crypto volatility; preserved explicitly in assumption note  
  - indirect/contextual  
  - why it matters: a 5-day move of this size is not tail-impossible for BTC.  
  - weight: medium-high

- **Binance-specific implementation risk**  
  - sources: rule text references UI; Binance docs describe API  
  - operational / interpretive  
  - why it matters: small residual ambiguity remains about UI-vs-API retrieval if a reviewer later checks the source differently.  
  - weight: low-medium

## Ambiguous or mixed evidence

- **CoinGecko spot confirmation near 74.3k**  
  - independent contextual confirmation that broad market level is similar to Binance, but it does not govern settlement.

## Conflict between inputs

There is no major factual conflict. The main disagreement is weighting-based: whether the current ~6 percent cushion should imply something close to market confidence (0.88) or a slightly lower estimate due to timestamp fragility.

## Key assumptions

- Current Binance cushion above 70k is large enough to absorb normal short-horizon volatility.
- No major exchange-specific anomaly will distort the settlement minute.
- ET/EDT noon interpretation remains straightforward and uncontroversial.

## Key uncertainties

- Path of BTC over the next five days.
- Whether weekend or macro volatility creates a sharp intraday dip near settlement.
- Residual source-of-truth ambiguity between Binance UI and API representation.

## Disconfirming signals to watch

- BTCUSDT retracing toward 71k-72k before April 20.
- Higher realized volatility or sharp downside moves into the weekend.
- Binance-specific data or platform irregularities.

## What would increase confidence

- BTC staying comfortably above 72k through April 19.
- Independent confirmation that Binance UI and API candle closes align cleanly for the settlement minute.
- No exchange-specific operational issues as settlement approaches.

## Net update logic

The evidence starts from a high baseline because direct settlement-relevant prices are currently well above 70k. The main downward adjustment comes from contract structure rather than bearish thesis evidence: exact-minute resolution and exchange-specific settlement create more fragility than a casual "BTC above 70k sometime that day" reading would imply.

## Suggested downstream use

- orchestrator synthesis input
- decision-maker review
- follow-up investigation on settlement-minute mechanics if pricing dislocation appears