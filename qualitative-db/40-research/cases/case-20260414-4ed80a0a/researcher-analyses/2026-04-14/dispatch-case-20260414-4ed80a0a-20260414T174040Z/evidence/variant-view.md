---
type: evidence_map
case_key: case-20260414-4ed80a0a
dispatch_id: dispatch-case-20260414-4ed80a0a-20260414T174040Z
research_run_id: d4883d27-d611-489a-a1e9-e4968019a939
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: protocols
entity: ethereum
topic: "threshold hit by designated source vs general market impression"
question: "Will Ethereum reach $2,400 April 13-19?"
driver:
date_created: 2026-04-14
agent: variant-view
status: draft
confidence: medium
conflict_status: "low-explicit-source-conflict high-interpretive-ambiguity"
action_relevance: high
related_entities: ["ethereum"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["contract source-of-truth ambiguity for exchange-threshold markets"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/personas/variant-view.md"]
tags: ["evidence-map", "variant-view", "contract-interpretation"]
---

# Summary

The evidence strongly supports that ETH traded above $2,400 on at least one major venue, but the best variant case is that the market is a bit too confident because the governing settlement source was not directly recoverable in this run.

## Question being evaluated

Will Ethereum reach $2,400 April 13-19 under the Polymarket contract’s actual settlement rules?

## Current lean

Lean YES, but less extremely than the market price implies.

## Prior / starting view

Starting view was that a 91.6% market probably reflects either an already-observed price print or a near-consensus expectation of one.

## Evidence supporting the claim

- Binance 24h API reported ETHUSDT high of 2415.50.
  - direct exchange evidence
  - high weight
  - matters because it shows threshold-touch behavior is not hypothetical
- Market page fetch indicates ↑ 2,400 is the leading outcome and the market is already pricing near certainty.
  - direct market-surface evidence
  - medium weight
  - matters because the crowd likely saw similar price action

## Evidence against the claim

- Polymarket rules text and official source were not extractable from the page fetch.
  - direct contract-surface limitation
  - high weight for interpretation risk
  - matters because venue-specific highs are not necessarily dispositive
- Coinbase and other secondary fetch attempts were blocked or unavailable in-tool, reducing cross-venue confirmation.
  - indirect / tooling limitation
  - medium weight
  - matters because extra verification remained partial rather than complete

## Ambiguous or mixed evidence

- The Polymarket FAQ-like extract showed odd display behavior around 100% outcome labels, suggesting page extraction may not faithfully represent the live contract surface.

## Conflict between inputs

There is little factual conflict. The main disagreement is interpretive: whether exchange-level evidence is enough without the named settlement source.

## Key assumptions

- The market likely keys off a source that usually tracks major spot highs closely.
- Source-of-truth mismatch risk is real but not dominant.

## Key uncertainties

- Exact settlement venue / oracle.
- Whether the designated source has already printed above $2,400.

## Disconfirming signals to watch

- Official rules naming a source that remained below $2,400.
- Reliable evidence that the contract uses a narrower reference than broad spot market highs.

## What would increase confidence

- Exact rule text.
- Direct print from the designated settlement source.
- Cross-venue confirmation from another major exchange or index.

## Net update logic

Direct exchange data pushes strongly toward YES. The only meaningful reason not to mirror the market exactly is resolution mechanics ambiguity. That is enough for a mild discount, not a full contrarian thesis.

## Suggested downstream use

- orchestrator synthesis input
- decision-maker review
- source collection gap