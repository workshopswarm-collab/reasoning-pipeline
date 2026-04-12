---
type: evidence_map
case_key: case-20260407-56d31eea
dispatch_id: dispatch-case-20260407-56d31eea-20260407T023203Z
research_run_id: e93bb59d-0c6b-40b7-95b9-70c4a9abc391
analysis_date: 2026-04-07
persona: base-rate
domain: crypto
subdomain: market-structure
entity: bitcoin
topic: will-the-binance-btc-usdt-12-00-et-1-minute-candle-on-2026-04-07-close-above-66000
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-07 close above 66000?"
driver: reliability
date_created: 2026-04-06
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin", "binance"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260407-56d31eea/researcher-analyses/2026-04-07/dispatch-case-20260407-56d31eea-20260407T023203Z/personas/base-rate.md"]
tags: ["threshold-market", "verification", "evidence-map"]
---

# Summary

This is a simple but audit-sensitive threshold market. The main netting question is whether the clean single-source settlement rule plus current Binance price cushion justify staying close to the 95.95% market-implied probability.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-07 have a final Close price above 66,000?

## Current lean

Lean Yes with high but not near-certain confidence.

## Prior / starting view

Before checking sources, a same-day Bitcoin threshold set only ~3-4% below current spot would usually deserve a strong Yes prior, but not automatic certainty because crypto can move several percent intraday.

## Evidence supporting the claim

- Polymarket rules specify a single authoritative source and an unambiguous metric: Binance BTC/USDT 1-minute candle Close at 12:00 ET. This sharply reduces interpretive resolution risk.
- Direct Binance endpoint checks during the run show BTCUSDT around 68.5k, roughly 2.5k above the threshold. This means the market only needs price retention, not an additional rally.
- Outside-view logic for short-horizon threshold questions on a highly liquid asset favors the side already materially in the money, absent a clear catalyst for a reversal.

## Evidence against the claim

- Bitcoin can easily move 3-4% over a sub-14-hour horizon, so the current buffer is meaningful but not enormous.
- Binance-specific operational or chart anomalies, while unlikely, matter more here than in cross-exchange or consensus-priced markets because the contract is single-source.
- The exact future settlement candle cannot yet be observed, so there remains some residual implementation / labeling risk until noon ET.

## Ambiguous or mixed evidence

- The market price itself (95.95%) is informative but may already overcompress short-horizon downside tail risk.
- Binance API documentation lowers ambiguity around candle mechanics, but the contract references the chart UI, not the API explicitly.

## Conflict between inputs

No major factual conflict across inputs. The disagreement is mainly weighting-based: whether a ~2.5k spot cushion deserves a price closer to the market's 96% or somewhat lower to respect crypto gap risk.

## Key assumptions

- No major BTC selloff before noon ET
- No Binance-specific settlement anomaly affecting the relevant candle
- The Binance chart UI and documented kline model are effectively aligned for the relevant minute

## Key uncertainties

- Overnight / morning volatility magnitude
- Tail risk from macro or crypto-specific shock headlines before noon ET
- Residual UI-versus-API interpretation ambiguity

## Disconfirming signals to watch

- BTC/USDT trading below 67k late in the morning ET
- Exchange incident notices from Binance
- Sharp rise in realized downside volatility before the settlement minute

## What would increase confidence

- A fresh morning check showing Binance BTC/USDT still comfortably above 66k
- A direct view of the chart UI confirming expected ET labeling behavior

## Net update logic

The evidence keeps the run on Yes, but not at certainty. The biggest update is that the contract is operationally clean and the observed Binance spot level is materially above threshold. The main reason not to simply mirror the market is that same-day BTC moves can still erase a 3-4% cushion.

## Suggested downstream use

forecast update
