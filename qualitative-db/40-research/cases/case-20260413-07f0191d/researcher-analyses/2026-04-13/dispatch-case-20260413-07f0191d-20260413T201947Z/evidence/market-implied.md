---
type: evidence_map
case_key: case-20260413-07f0191d
dispatch_id: dispatch-case-20260413-07f0191d-20260413T201947Z
research_run_id: 0a968c58-4f48-4ba0-9e30-f0ef20afb3b9
analysis_date: 2026-04-13
persona: market-implied
domain: politics
subdomain: elections
entity:
topic: "GERB-SDS second-place market audit"
question: "Will GERB-UDF (GERB-SDS) finish second in the 2026 Bulgarian parliamentary election?"
driver: elections
date_created: 2026-04-13
agent: Orchestrator
status: draft
confidence: medium
conflict_status: "market-vs-public-context conflict"
action_relevance: high
related_entities: []
related_drivers: ["elections"]
proposed_entities: ["GERB-SDS", "PP-DB", "Revival", "DPS", "Central Election Commission of Bulgaria"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-07f0191d/researcher-analyses/2026-04-13/dispatch-case-20260413-07f0191d-20260413T201947Z/personas/market-implied.md"]
tags: ["evidence-map", "market-implied", "bulgaria", "elections"]
---

# Summary

The market says GERB-SDS is about 96% likely to finish second, but the accessible public evidence reviewed in this run points toward GERB-SDS being more likely to finish first than second.

## Question being evaluated

Will GERB-UDF (GERB-SDS) finish second in the 2026 Bulgarian parliamentary election?

## Current lean

Lean no: the market appears overconfident or misaligned with public evidence.

## Prior / starting view

Start from the market at 96%, but test what would have to be true for GERB-SDS to be almost locked into second place.

## Evidence supporting the claim

- The market price itself is extreme at 0.96.
  - source: assignment / live market snapshot
  - why it matters causally: could reflect hidden information or trader consensus
  - direct or indirect: indirect
  - weight: low-to-medium unless corroborated

- It is at least conceivable in fragmented Bulgarian politics that GERB could end up behind one rival while still clearly ahead of the rest.
  - source: contextual electoral-system logic
  - why it matters causally: multiparty fragmentation can create stable rank outcomes
  - direct or indirect: indirect
  - weight: low without corroborating polling

## Evidence against the claim

- Accessible contextual polling/trend evidence from POLITICO shows GERB-SDS around 23.6%, ahead of peers in the mid-teens.
  - source: researcher source note
  - why it matters causally: a party leading the public polling picture is not the obvious second-place candidate
  - direct or indirect: contextual
  - weight: high for directional ranking

- Accessible election-context reporting on Wikipedia frames GERB-SDS as the largest prior force and a lead contender, not a runner-up.
  - source: researcher source note
  - why it matters causally: public baseline context does not match a 96%-second-place thesis
  - direct or indirect: contextual
  - weight: medium

- The contract resolves by seats won and falls back to official CIK reporting if consensus is ambiguous.
  - source: contract wording / assignment
  - why it matters causally: ranking, not broad competitiveness, is what matters; this raises the bar for a market price that appears inconsistent with rank evidence
  - direct or indirect: direct on mechanics
  - weight: high

## Ambiguous or mixed evidence

- CIK itself was inaccessible from this environment due Cloudflare, which limits direct inspection of the primary official election page before results.
- POLITICO is an aggregator, not an official source.
- Thin or stale market structure could explain the price without implying informed consensus.

## Conflict between inputs

- Disagreement: market price implies near-certainty of second place; accessible public context implies GERB-SDS is more likely first than second.
- Type: primarily weighting-based and possibly market-structure/timing-based.
- What would resolve it: independent late Bulgarian polling, visible liquidity/volume evidence, or official preliminary results.

## Key assumptions

- Publicly accessible ranking context is not missing a major late break against GERB-SDS.
- The market price is not being sustained by superior hidden information.

## Key uncertainties

- Whether any very recent domestic polling materially contradicts the accessible aggregation.
- Whether the contract order book is deep and informed or thin/stale.

## Disconfirming signals to watch

- Multiple independent late polls placing another bloc clearly ahead while GERB clusters safely in second.
- Election-night counts or credible exit polls pointing to GERB second.

## What would increase confidence

- Direct CIK pre-election materials and official results page access.
- Independent Bulgarian pollster confirmation.
- Market microstructure evidence showing the 0.96 price is actively defended with volume.

## Net update logic

The price was the prior, but the first meaningful contextual sources did not merely fail to support it; they pointed in the opposite rank direction. Because the contract is specifically about second place, leading-poll evidence for GERB-SDS meaningfully undermines the market-implied thesis.

## Suggested downstream use

Use as orchestrator synthesis input and as an audit trail for why this persona materially disagreed with the market.