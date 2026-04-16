---
type: evidence_map
case_key: case-20260415-1a345042
dispatch_id: dispatch-case-20260415-1a345042-20260415T223206Z
research_run_id: b3c68472-9e18-4321-b20e-43c4636e968d
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-binance-btc-usdt-12-00-et-1-minute-candle-close-on-2026-04-21-be-above-72000
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-21 be above 72000?"
driver: reliability
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-1a345042/researcher-analyses/2026-04-15/dispatch-case-20260415-1a345042-20260415T223206Z/personas/market-implied.md"]
tags: ["evidence-map", "market-implied", "btc"]
---

# Summary

The market's 80.5% Yes price looks mostly like a distributional statement about BTC staying above an already-cleared threshold rather than a claim that BTC must break out further.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle at 12:00 ET on 2026-04-21 close above 72,000?

## Current lean

Lean Yes, with only mild skepticism versus the market's confidence.

## Prior / starting view

Starting from the live market prior, 80.5% Yes looked plausible if BTC was already meaningfully above 72,000 and contract mechanics were straightforward.

## Evidence supporting the claim

- **Current distance to threshold is substantial**
  - source: Binance ticker/API spot check + source note
  - why it matters causally: BTC was about 74,991.76 during the run, roughly 4.2% above the threshold; the contract only needs one specified noon close above 72,000
  - direct or indirect: direct/contextual to current state, not direct settlement
  - weight: high

- **Contract mechanics are simple and specific**
  - source: Polymarket rules page + source note
  - why it matters causally: the outcome depends on a single Binance BTC/USDT 1-minute close, reducing ambiguity about what counts
  - direct or indirect: direct
  - weight: high

- **Cross-threshold ladder is internally coherent**
  - source: Polymarket market page
  - why it matters causally: 70k ~91%, 72k ~81%, 74k ~62%, 76k ~41% is consistent with current spot in the mid/high-74k area and a short-horizon volatility distribution
  - direct or indirect: contextual market structure evidence
  - weight: medium

## Evidence against the claim

- **There are still ~5.5 days to resolution**
  - source: contract timing check
  - why it matters causally: BTC can easily move several percent over that window, and a ~4% drawdown would be enough to lose the market
  - direct or indirect: direct timing/context
  - weight: high

- **Settlement is exchange-specific**
  - source: Polymarket rules page
  - why it matters causally: the relevant truth is Binance BTC/USDT, not aggregate BTC/USD across exchanges, so exchange-specific dislocations or outages are residual risks
  - direct or indirect: direct contract interpretation
  - weight: medium

## Ambiguous or mixed evidence

- **Generic BTC price pages (CoinDesk/CoinMarketCap)**
  - useful for contextual confirmation that BTC is trading in the mid-70k region
  - not authoritative for settlement and not meaningfully independent in methodology from broader market aggregation

## Conflict between inputs

There was no material source conflict. The main issue is weighting: how much downside volatility risk remains over the next ~5.5 days versus how much comfort should be taken from BTC already trading well above 72,000.

## Key assumptions

- current spot distance from threshold remains the dominant driver
- no major Binance-specific pricing anomaly changes the relevant close
- no major negative catalyst produces a >4% downside move by the Tuesday noon ET observation point

## Key uncertainties

- near-term BTC volatility between now and resolution
- whether current market confidence slightly underprices downside path risk
- exchange-specific operational or microstructure issues at the exact observation minute

## Disconfirming signals to watch

- BTC losing 74k and failing to reclaim it
- broad crypto risk-off move before Monday/Tuesday
- Binance-specific pricing or service issues near the relevant time window

## What would increase confidence

- BTC holding >74k through the weekend
- continued monotonic pricing coherence across the Polymarket threshold ladder
- absence of exchange-specific anomalies on Binance as resolution approaches

## Net update logic

The evidence largely validated the market prior rather than overturned it. What mattered most was the combination of simple contract mechanics and meaningful current distance above the threshold. I downweighted generic commentary and broad Bitcoin narrative material because this is a narrow, date-specific threshold market. The remaining skepticism comes from the fact that a single ~4% move over several days is not remotely rare for BTC.

## Suggested downstream use

- orchestrator synthesis input
- forecast update
- decision-maker review