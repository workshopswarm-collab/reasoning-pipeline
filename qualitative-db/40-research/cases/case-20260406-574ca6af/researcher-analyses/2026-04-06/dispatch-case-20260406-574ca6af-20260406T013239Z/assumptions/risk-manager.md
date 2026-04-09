---
type: assumption_note
case_key: case-20260406-574ca6af
dispatch_id: dispatch-case-20260406-574ca6af-20260406T013239Z
research_run_id: 53b2f3c6-cb4c-4c59-80a6-9924143d9ad2
analysis_date: 2026-04-06
persona: risk-manager
domain: crypto
subdomain: ethereum
entity: ethereum
topic: case-20260406-574ca6af | risk-manager
question: Will Ethereum reach $2,200 March 30-April 5?
driver: settlement source hierarchy
date_created: 2026-04-06T01:37:00Z
agent: Orchestrator
status: active
certainty: medium-high
importance: high
time_horizon: immediate resolution
related_entities: [ethereum, binance, polymarket]
related_drivers: [resolution mechanics, source-of-truth ambiguity]
upstream_inputs: [polymarket contract, binance klines]
downstream_uses: [risk-manager finding]
tags: [assumption, binance-api, settlement]
---

# Assumption

The Binance ETH/USDT public kline API is materially consistent with the Binance 1m chart surface named in the Polymarket contract, so API-observed highs are a valid proxy for settlement verification.

## Why this assumption matters

The directional conclusion depends more on contract mechanics than on broader ETH market direction. If the contract-designated chart and the API materially diverged, the API check could misstate whether the threshold was hit.

## What this assumption supports

- The view that the market should resolve No.
- The interpretation that DEX highs or other CEX prints are irrelevant.
- Confidence that extra broad market research would not move the estimate much.

## Evidence or logic behind the assumption

Binance charting and Binance public kline API normally reflect the same exchange trade data for the same symbol and interval. The contract also names Binance ETH/USDT 1m candles specifically, which is very close to the API object queried.

## What would falsify it

- Evidence that the Binance chart UI showed a 1m high >= 2200 in the window while the API did not.
- Contract clarification from Polymarket that a different Binance data surface or transformed index is authoritative.
- A documented chart/API discrepancy for this exact symbol and interval.

## Early warning signs

- Community dispute around settlement despite seemingly clear API data.
- Screenshot evidence of a 2200 wick on the Binance GUI.
- Post-market clarification language from Polymarket moderators or rules pages.

## What changes if this assumption fails

Confidence drops materially and the market may require direct chart-level verification or settlement-admin clarification. The current No lean would weaken or become unresolved pending the exact authoritative surface.

## Notes that depend on this assumption

- risk-manager main finding
- evidence map for this dispatch