---
type: assumption_note
case_key: case-20260406-574ca6af
dispatch_id: dispatch-case-20260406-574ca6af-20260406T013239Z
research_run_id: cc52f383-6f3a-4425-8878-967e91ffab22
analysis_date: 2026-04-06
persona: market-implied
domain: crypto
subdomain: ethereum
entity: ethereum
topic: "case-20260406-574ca6af | market-implied"
question: "Will Ethereum reach $2,200 March 30-April 5?"
driver:
date_created: 2026-04-06
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: event-window
related_entities: ["ethereum", "binance", "polymarket"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["crypto-price-threshold-resolution"]
upstream_inputs: []
downstream_uses: ["market-implied-finding", "evidence-map"]
tags: ["assumption", "source-of-truth", "market-pricing"]
---

# Assumption

The 0.74 market price is partly reflecting generalized ETH price optimism or cross-venue price impressions rather than a fully audited Binance ETH/USDT 1-minute-high path to 2200.

## Why this assumption matters

The market-implied researcher should start by respecting the 74% price, but the price only deserves that weight if traders are correctly keying off the contract's exact settlement surface rather than a looser "ETH broadly looks close" intuition.

## What this assumption supports

- A below-market own probability estimate.
- The interpretation that the market may be over-weighting non-governing price information.
- The need to emphasize source-of-truth precision over broad crypto sentiment.

## Evidence or logic behind the assumption

- The contract explicitly settles on Binance ETH/USDT 1m highs, excluding other venues and price surfaces.
- A direct Binance klines pull from the queried sample showed a max high of only 2085, far from 2200.
- Source-of-truth ambiguity was flagged ex ante in the case prompt, which makes trader misweighting plausible.

## What would falsify it

- A full-window Binance ETH/USDT 1-minute record showing at least one candle high >=2200 during March 30-April 5.
- Clear evidence that the 0.74 price came after market participants verified such a Binance print.

## Early warning signs

- Discovery of a later-in-window Binance rally not covered by the sampled pull.
- Independent archival/chart evidence pointing to Binance-specific trade or wick activity near/above 2200.
- Contract comments or linked market materials showing trader attention focused tightly on Binance 1m highs.

## What changes if this assumption fails

If Binance did print >=2200, then the market was not overextended at all; instead it was correctly incorporating source-specific information and should have been priced near certainty.

## Notes that depend on this assumption

- `qualitative-db/40-research/cases/case-20260406-574ca6af/researcher-analyses/2026-04-06/dispatch-case-20260406-574ca6af-20260406T013239Z/personas/market-implied.md`
- `qualitative-db/40-research/cases/case-20260406-574ca6af/researcher-analyses/2026-04-06/dispatch-case-20260406-574ca6af-20260406T013239Z/evidence/market-implied.md`