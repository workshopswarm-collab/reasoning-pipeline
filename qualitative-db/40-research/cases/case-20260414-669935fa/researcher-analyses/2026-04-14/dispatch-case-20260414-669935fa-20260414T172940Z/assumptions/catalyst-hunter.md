---
type: assumption_note
case_key: case-20260414-669935fa
dispatch_id: dispatch-case-20260414-669935fa-20260414T172940Z
research_run_id: f6f42fe2-b2d9-4818-842e-60d900aec762
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-bitcoin-reach-76-000-april-13-19
question: "Will Bitcoin reach $76,000 April 13-19?"
driver: liquidity
date_created: 2026-04-14
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: intrawindow
related_entities: ["bitcoin"]
related_drivers: ["liquidity", "macro", "sentiment"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-669935fa/researcher-analyses/2026-04-14/dispatch-case-20260414-669935fa-20260414T172940Z/personas/catalyst-hunter.md"]
tags: ["assumption", "binance", "threshold", "timing"]
---

# Assumption

A Binance hourly high above $76,000 is sufficient evidence that at least one qualifying Binance 1-minute candle high at or above $76,000 occurred during the contract window.

## Why this assumption matters

My near-certainty view depends on treating the observed hourly Binance high as strong enough contract-aligned evidence that the trigger event already happened, even though I did not independently archive the exact qualifying 1-minute candle in this run.

## What this assumption supports

- The thesis that the decisive catalyst has already occurred.
- A probability estimate slightly below but broadly in line with the market's ~99.95% implied probability.
- The conclusion that remaining uncertainty is mostly administrative / source-transcript risk rather than market-direction risk.

## Evidence or logic behind the assumption

- An hourly candle high above $76,000 implies trades occurred above that level within the hour.
- The contract resolves on any Binance 1-minute candle high >= $76,000, so a valid hourly high strongly implies at least one underlying minute candle touched that level.
- Independent case-level source notes already documented both the rule language and the Binance >$76k print.

## What would falsify it

- Evidence that the hourly high was erroneous and later corrected below $76,000.
- Evidence that no final Binance 1-minute candle high actually reached $76,000 despite the hourly print.
- A materially different official Polymarket rule or settlement interpretation than the one captured in the rule note.

## Early warning signs

- Polymarket delays settlement despite the alleged threshold hit.
- A later archived Binance minute-candle transcript fails to show any 1-minute high >= $76,000.
- Contradictory support replies or rule clarifications from Polymarket.

## What changes if this assumption fails

The case would move from near-settled Yes toward a more ordinary timing question about whether BTC can still tag $76,000 later in the Apr 13-19 window, which would raise the importance of macro and sentiment catalysts over the already-occurred-trigger thesis.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260414-669935fa/researcher-analyses/2026-04-14/dispatch-case-20260414-669935fa-20260414T172940Z/personas/catalyst-hunter.md