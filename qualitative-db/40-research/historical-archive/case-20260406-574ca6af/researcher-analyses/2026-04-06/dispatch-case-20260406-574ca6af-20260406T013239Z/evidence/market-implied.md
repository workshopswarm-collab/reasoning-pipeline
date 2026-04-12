---
type: evidence_map
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
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["ethereum", "binance", "polymarket"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["crypto-price-threshold-resolution"]
upstream_inputs: []
downstream_uses: ["market-implied-finding", "orchestrator-synthesis"]
tags: ["evidence-map", "market-vs-source", "crypto"]
---

# Summary

The main netting issue is not broad ETH direction but whether traders are pricing the exact governing surface correctly. Contract language is unambiguous: only Binance ETH/USDT 1-minute candle highs count. Direct sampled Binance data did not show a 2200 touch, so the evidence currently leans against the market's 74% implied probability.

## Question being evaluated

Whether Ethereum reached 2200 at any point during March 30-April 5 under the contract's actual source-of-truth definition.

## Current lean

Lean No relative to the 2200 threshold; market appears rich versus the directly checked governing evidence.

## Prior / starting view

Start from the market's 74% implied probability and assume traders may know of a Binance-specific wick or late-window move.

## Evidence supporting the claim

- Market price at 0.74.
  - Directness: indirect for truth, direct for crowd belief.
  - Why it matters: indicates traders think a qualifying touch is more likely than not or may have seen supportive information.
  - Weight: moderate as prior, not decisive.

## Evidence against the claim

- Polymarket contract text makes Binance ETH/USDT 1m highs the exclusive settlement surface.
  - Direct.
  - Weight: very high because it determines what counts.
- Direct Binance klines sample showed max high 2085.00, well below 2200.
  - Direct.
  - Weight: high but not absolute because the pull was limited to 1,000 returned rows and therefore not a full-window exhaustive audit.
- Contract text explicitly excludes other exchanges, other pairs, and other price surfaces.
  - Direct.
  - Weight: high because it neutralizes DEX/CEX ambiguity in favor of a single CEX source.

## Ambiguous or mixed evidence

- The market price itself could reflect genuine trader knowledge of a later Binance wick, or it could reflect sloppy extrapolation from broader ETH price action.
- Third-party commentary like Lines is not reliable enough to resolve the case and may summarize the market loosely rather than audit the source-of-truth surface precisely.

## Conflict between inputs

- Conflict is mainly weighting-based: market price implies a likely touch, while direct sampled governing data does not.
- What would resolve it: a full-window Binance ETH/USDT 1m high audit or authoritative settlement confirmation from Polymarket after close.

## Key assumptions

- The sampled Binance data is directionally representative enough that a 2200 touch was unlikely.
- Traders may not have perfectly audited the exact source-of-truth hierarchy.

## Key uncertainties

- Whether an uncovered later minute in the full event window printed >=2200 on Binance.
- Whether the 74% price reflected information not visible in the sampled data.

## Disconfirming signals to watch

- Any Binance ETH/USDT 1m candle high >=2200 during the eligible ET window.
- Polymarket resolution materials confirming such a print.

## What would increase confidence

- A complete full-window Binance kline export or second archive reproducing the same max high below 2200.
- Post-close market resolution confirming No.

## Net update logic

I began from the view that the market might be efficiently pricing a venue-specific wick. Reading the contract sharply reduced source ambiguity, and the direct Binance sample then pushed the view below the market because the observed max high remained far from 2200. What mattered most was exact settlement logic, not generic ETH bullishness.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- retrospective evaluation of source-of-truth precision in crypto threshold markets