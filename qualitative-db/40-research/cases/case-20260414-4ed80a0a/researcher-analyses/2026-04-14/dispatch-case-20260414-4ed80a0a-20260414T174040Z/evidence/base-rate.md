---
type: evidence_map
case_key: case-20260414-4ed80a0a
dispatch_id: dispatch-case-20260414-4ed80a0a-20260414T174040Z
research_run_id: 23445208-5ef6-4cd8-978c-62c7f846d319
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: protocols
entity: ethereum
topic: eth-price-threshold
question: "Will Ethereum reach $2,400 April 13-19?"
date_created: 2026-04-14
agent: orchestrator
status: draft
confidence: high
conflict_status: low
action_relevance: high
related_entities: ["ethereum"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["binance-venue-specific-price-threshold-resolution"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/personas/base-rate.md"]
tags: ["evidence-map", "threshold", "resolution", "binance"]
driver:
---

# Summary

This is a low-difficulty, rule-sensitive threshold market. Once the venue-specific source of truth is fixed, the evidence nets strongly to Yes and the remaining uncertainty is mainly about exact timestamp auditability rather than direction.

## Question being evaluated

Will Ethereum reach $2,400 April 13-19, where the contract defines this as any Binance ETH/USDT 1-minute candle High at or above $2,400 during Apr 13-19 ET?

## Current lean

Very strong Yes / effectively already satisfied.

## Prior / starting view

Before checking current evidence, the outside-view baseline for a weekly ETH threshold only ~3% above a spot level near the low-$2300s would already be fairly high, but not certainty. The case needed rules verification because the market price was extreme.

## Evidence supporting the claim

- Polymarket market metadata and CLOB response explicitly define the governing rule and showed the market already resolved Yes.
  - direct, high weight
  - matters because it names the exact source of truth and current contract state
- Binance 24hr ETHUSDT ticker reported highPrice 2415.50.
  - direct but confirmatory, high weight
  - matters because it comes from the exact exchange named in the contract and exceeds the threshold by 15.50

## Evidence against the claim

- The Binance verification endpoint used was a 24hr ticker summary, not the literal 1-minute candle table referenced in the rules.
  - indirect to exact settlement mechanics, low-to-medium weight
  - matters because a strict auditor would still prefer the precise minute candle and timestamp
- Cross-exchange prices can diverge in crypto microstructure.
  - contextual, low weight
  - matters in general, though the contract explicitly says non-Binance prices do not count

## Ambiguous or mixed evidence

- The web-rendered Polymarket page showed noisy/readability-extracted FAQ text with apparently inconsistent outcome percentages; this was not relied on for the conclusion.

## Conflict between inputs

No material factual conflict after switching from rendered web text to machine-readable market metadata and direct Binance data. The main issue was source cleanliness, not evidence disagreement.

## Key assumptions

- The Polymarket API description accurately matches the actual resolving contract.
- Binance's reported 24hr high corresponds to a qualifying minute within the contract window.

## Key uncertainties

- Exact minute and timestamp of first threshold breach were not captured in this run.
- I did not independently inspect the exact 1-minute candle history surface referenced in the rules.

## Disconfirming signals to watch

- Any settlement dispute or reversal by Polymarket.
- Any Binance minute-candle audit showing no >=2400 high within the stated ET window.

## What would increase confidence

- A saved Binance 1-minute candle extract or screenshot showing the qualifying high and timestamp.

## Net update logic

The base-rate prior already leaned Yes for a weekly ETH threshold near spot, but not at 100%. The decisive update was not narrative or market sentiment; it was resolution-mechanics evidence: Polymarket's own metadata plus a same-venue Binance high above threshold. That combination made additional broad market research unlikely to move the estimate by 5 percentage points.

## Suggested downstream use

- orchestrator synthesis input
- retrospective evaluation of rule-sensitive crypto threshold markets
- possible driver-candidate review for venue-specific threshold-resolution mechanics