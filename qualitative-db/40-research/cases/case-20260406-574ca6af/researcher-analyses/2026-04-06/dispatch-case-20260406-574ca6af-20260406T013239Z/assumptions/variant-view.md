---
type: assumption_note
case_key: case-20260406-574ca6af
dispatch_id: dispatch-case-20260406-574ca6af-20260406T013239Z
research_run_id: 4bdf6b0a-f878-4814-bdb6-1482c609fe49
analysis_date: 2026-04-06
persona: variant-view
topic: case-20260406-574ca6af | variant-view
question: Will Ethereum reach $2,200 March 30-April 5?
date_created: 2026-04-06
agent: Orchestrator
status: active
certainty: medium-high
importance: high
time_horizon: case-window
related_entities: [ethereum, binance, polymarket]
related_drivers: []
upstream_inputs: []
downstream_uses: [variant-view finding]
tags: [assumption, settlement-surface, binance]
---

# Assumption

The Binance ETH/USDT 1-minute kline API is a sufficiently faithful proxy for the Binance 1m chart surface named in the Polymarket rules to determine whether a $2,200 High occurred.

## Why this assumption matters

The finding depends on verifying the designated venue and interval rather than broad ETH price action across venues. If the API and the chart surface diverged materially, the direct No case would weaken.

## What this assumption supports

- The conclusion that the market should resolve No.
- The view that DEX/CEX divergence is not outcome-determinative here because the designated CEX itself never printed $2,200 on the checked series.
- The claim that no specific market-maker attribution carveout appears necessary for this case.

## Evidence or logic behind the assumption

- The Polymarket rules explicitly name Binance ETH/USDT 1m candles as source of truth.
- Binance’s public kline API reports the same pair/interval OHLC structure used by exchange charting surfaces.
- The observed max High remained materially below $2,200, leaving a nontrivial buffer rather than a borderline near-miss.

## What would falsify it

- A direct check of the Binance chart UI or another Binance-authenticated historical candle export showing at least one 1m High >= $2,200 during the window.
- Evidence that the API omitted relevant candles or used a materially different market/data feed than the rule-referenced chart.

## Early warning signs

- Any independent reviewer observing a Binance chart print above $2,200 for the same pair/window.
- Documentation showing discrepancies between Binance chart candles and the public kline API for historical highs.

## What changes if this assumption fails

The market could move from near-certain No to genuinely ambiguous, and a higher-fidelity chart-surface verification would become mandatory before keeping a decisive view.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260406-574ca6af/researcher-analyses/2026-04-06/dispatch-case-20260406-574ca6af-20260406T013239Z/personas/variant-view.md
