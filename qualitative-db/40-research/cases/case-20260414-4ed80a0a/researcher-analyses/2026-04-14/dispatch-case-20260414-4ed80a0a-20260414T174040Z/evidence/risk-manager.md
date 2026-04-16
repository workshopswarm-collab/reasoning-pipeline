---
type: evidence_map
case_key: case-20260414-4ed80a0a
dispatch_id: dispatch-case-20260414-4ed80a0a-20260414T174040Z
research_run_id: c66d2b88-d6ed-44c7-ad54-6594d87a8cb8
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: protocols
entity: ethereum
topic: will-ethereum-reach-2-400-april-13-19
question: "Will Ethereum reach $2,400 April 13-19?"
driver:
date_created: 2026-04-14
agent: orchestrator
status: draft
confidence: high
conflict_status: low
action_relevance: high
related_entities: ["ethereum"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["binance-market-data-integrity"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/personas/risk-manager.md"]
tags: ["evidence-map", "eth", "binance", "resolution"]
---

# Summary

The evidence nets strongly toward `Yes already effectively achieved`, with the main residual risk coming from source-of-truth / settlement mechanics rather than further ETH price path.

## Question being evaluated

Will Ethereum reach $2,400 during Apr 13-19 under the exact Polymarket contract wording?

## Current lean

Strong lean to `Yes`, effectively near-settled because a qualifying Binance 1-minute high appears to have already printed.

## Prior / starting view

Starting baseline was the market price of 0.916, which implied high confidence but not certainty.

## Evidence supporting the claim

- **Polymarket rule text names Binance ETH/USDT 1-minute highs**
  - source: source note on Polymarket rules
  - causal relevance: defines the governing threshold and venue
  - direct or indirect: direct for contract interpretation
  - weight: very high

- **Binance 1-minute data shows max high of 2415.5 in the qualifying window**
  - source: Binance verification note
  - causal relevance: directly satisfies the contract trigger if valid
  - direct or indirect: direct
  - weight: very high

- **Threshold exceeded by 15.5 dollars, not a marginal print**
  - source: Binance verification note
  - causal relevance: lowers risk of rounding / display / micro-error arguments
  - direct or indirect: direct
  - weight: medium-high

## Evidence against the claim

- **Residual venue/data-surface integrity risk**
  - source: assumption note / contract interpretation
  - causal relevance: if API and chart/UI differ, settlement could become messy
  - direct or indirect: indirect
  - weight: low

- **Polymarket market price was 91.6% in assignment context rather than 99-100%**
  - source: assignment metadata versus page data
  - causal relevance: suggests either stale pricing, metadata timing mismatch, or a small residual dispute risk
  - direct or indirect: indirect
  - weight: low-medium

## Ambiguous or mixed evidence

- CoinGecko or other exchange references can contextualize where ETH is trading, but they do not settle this contract.

## Conflict between inputs

- Mild timing-based conflict between assignment metadata (`current_price: 0.916`) and later page-data check (`1.0`).
- This appears more likely to be a timestamp difference than substantive disagreement.
- Best resolution evidence is direct Binance minute-level data plus current market surface.

## Key assumptions

- Binance API output matches the operative Binance chart data referenced by Polymarket.
- The checked timestamp conversion correctly maps the qualifying ET window.

## Key uncertainties

- Whether any settlement dispute or data-surface mismatch emerges.
- Whether Polymarket uses any special handling for anomalous exchange prints.

## Disconfirming signals to watch

- Evidence from Binance UI that the relevant 10:32 ET candle did not print above 2400.
- Official market commentary indicating a dispute or exception.
- A sharp repricing of the market away from certainty without explanation.

## What would increase confidence

- Screenshot or archived Binance chart showing the qualifying 1-minute high.
- Official Polymarket comment or early resolution confirming the trigger.

## Net update logic

The market baseline already leaned strongly Yes, but the decisive update is that the condition appears realized already. That shifts the problem from forecasting to verification. Once a qualifying high is directly observed on the named venue, further macro or thesis discussion matters little except as sanity check.

## Suggested downstream use

- orchestrator synthesis input
- decision-maker review
- retrospective evaluation for rule-sensitive crypto threshold markets