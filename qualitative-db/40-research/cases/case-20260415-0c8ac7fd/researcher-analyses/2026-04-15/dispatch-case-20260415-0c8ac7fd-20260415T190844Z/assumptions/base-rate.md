---
type: assumption_note
case_key: case-20260415-0c8ac7fd
dispatch_id: dispatch-case-20260415-0c8ac7fd-20260415T190844Z
research_run_id: 50fa720d-a864-40e4-8184-6a9f5b56bbba
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin-threshold-close
entity: bitcoin
topic: "short-dated threshold-close persistence assumption"
question: "Will the Binance BTC/USDT 12:00 ET one-minute close on April 17 be above 72000?"
driver: reliability
date_created: 2026-04-15
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: "through 2026-04-17 12:00 ET"
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-source-notes/2026-04-15-base-rate-binance-polymarket-resolution-and-price.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-analyses/2026-04-15/dispatch-case-20260415-0c8ac7fd-20260415T190844Z/personas/base-rate.md"]
tags: ["assumption-note", "btc", "threshold-close", "short-dated"]
---

# Assumption

BTC/USDT will remain sufficiently above 72,000 through the next roughly two days that ordinary intraday volatility is more likely than not to leave the governing 12:00 ET April 17 one-minute close above the threshold.

## Why this assumption matters

The base-rate estimate depends less on a special catalyst and more on persistence: if current price altitude tends to persist over a short horizon, Yes is likely; if short-horizon BTC volatility is large enough to erase a 3% to 4% cushion by the governing minute, the market could still resolve No.

## What this assumption supports

- A Yes-leaning probability materially above 50%
- A view roughly aligned with, but slightly below, the current 87% market-implied probability
- A conclusion that the market is directionally reasonable but somewhat rich for a close-specific contract

## Evidence or logic behind the assumption

- BTC is currently around 74.6k on Binance, already above the 72k threshold.
- Recent Binance daily data show repeated trading and several closes above 72k, so this is not a one-minute outlier.
- For short-dated threshold-close markets, the relevant outside view is whether an asset already several percent above the line tends to stay above it over a two-day horizon more often than not.

## What would falsify it

- A material BTC selloff that takes Binance BTC/USDT decisively back below 72k before April 17 noon ET
- A volatility shock or macro/crypto-specific negative catalyst large enough to erase the current cushion
- Evidence that recent above-72k trading was unusually fragile rather than persistent

## Early warning signs

- BTC loses 73k and then 72k on Binance with momentum rather than brief noise
- Cross-market risk-off move in equities/crypto that coincides with BTC breaking recent support
- Visible deterioration in intraday price structure into the April 17 morning session

## What changes if this assumption fails

If BTC is no longer stably above the threshold heading into the final hours, the correct view shifts from persistence-favored Yes to a much more balanced or even No-leaning close-specific coin flip.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-analyses/2026-04-15/dispatch-case-20260415-0c8ac7fd-20260415T190844Z/personas/base-rate.md