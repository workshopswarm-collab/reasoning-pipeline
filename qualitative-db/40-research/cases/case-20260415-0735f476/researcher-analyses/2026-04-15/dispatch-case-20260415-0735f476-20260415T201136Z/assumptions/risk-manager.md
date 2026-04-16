---
type: assumption_note
case_key: case-20260415-0735f476
dispatch_id: dispatch-case-20260415-0735f476-20260415T201136Z
research_run_id: 9cbbd9f1-24dc-4e3e-956f-801560384ced
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin-threshold-market
entity: bitcoin
topic: "Stability of BTC above 70000 into the exact Binance noon close"
question: "Will the price of Bitcoin be above $70,000 on April 20?"
driver: operational-risk
date_created: 2026-04-15
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: short-term
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260415-0735f476/researcher-source-notes/2026-04-15-risk-manager-polymarket-rules-binance-resolution.md", "qualitative-db/40-research/cases/case-20260415-0735f476/researcher-source-notes/2026-04-15-risk-manager-binance-spot-context.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-0735f476/researcher-analyses/2026-04-15/dispatch-case-20260415-0735f476-20260415T201136Z/personas/risk-manager.md"]
tags: ["assumption", "btc", "timing-risk", "threshold"]
---

# Assumption

BTC will remain above 70,000 on Binance through the specific April 20, 2026 12:00 ET 1-minute close, rather than merely trading above that level several days earlier.

## Why this assumption matters

The contract is not about current spot, weekly average, or intraday touch. It resolves on one exact future minute close on one exchange, so the bullish case depends on preserving enough price cushion into that timestamp.

## What this assumption supports

- A high Yes probability rather than a near-certain Yes probability.
- The judgment that current price cushion is meaningful evidence.
- The view that market odds in the low 90s are broadly justified but still leave room for downside path risk.

## Evidence or logic behind the assumption

- BTC currently trades around 74.7k on Binance, about 4.7k above the threshold.
- Cross-venue checks align closely, suggesting the level is not a single-venue anomaly.
- With several days remaining, the market has a buffer rather than needing a last-minute rally to get over the line.

## What would falsify it

- A material BTC selloff that brings Binance BTC/USDT below 70,000 into the April 20 noon ET minute.
- Clear evidence of elevated volatility or event risk that makes a 6%+ downside move likely before the deadline.
- A Binance-specific dislocation that causes BTC/USDT to print below the threshold even if broader BTC/USD references remain higher.

## Early warning signs

- Loss of the current multi-thousand-dollar cushion, especially a sustained move toward 71k-72k.
- Rising cross-venue divergence with Binance weakening versus major USD venues.
- Weekend or macro-driven risk-off conditions severe enough to compress BTC several percent quickly.

## What changes if this assumption fails

The Yes thesis weakens sharply because the contract has no averaging or touch protection. If BTC is near or below 70,000 approaching the deadline, confidence should fall materially and contract-interpretation risk should matter less than raw price-path risk.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260415-0735f476/researcher-analyses/2026-04-15/dispatch-case-20260415-0735f476-20260415T201136Z/personas/risk-manager.md