---
type: evidence_map
case_key: case-20260413-1fcb4925
dispatch_id: dispatch-case-20260413-1fcb4925-20260413T212655Z
research_run_id: 187da139-4dd6-4a29-bf47-91b827dcc916
analysis_date: 2026-04-13
persona: base-rate
domain: politics
subdomain: elections
entity:
topic: bulgarian-parliamentary-election-winner
question: "Will Progressive Bulgaria (PB) win the most seats in the 2026 Bulgarian parliamentary election?"
driver: elections
date_created: 2026-04-13
agent: Orchestrator
status: draft
confidence: medium
conflict_status: moderate
action_relevance: high
related_entities: []
related_drivers: ["elections"]
proposed_entities: ["progressive-bulgaria", "rumen-radev", "gerb-sds", "pp-db", "revival", "movement-for-rights-and-freedoms", "central-election-commission-of-bulgaria"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "bulgaria", "pb", "first-place", "source-sensitive"]
---

# Summary

The net evidence supports a **below-market / lean-no** view on PB winning the most seats. The strongest reason is outside-view structure: PB appears to be a newly formed coalition with no incumbent seats, while GERB–SDS remains the largest established bloc, and the accessible evidence stack does not independently verify a near-certain PB lead.

## Question being evaluated

Will Progressive Bulgaria (PB) win the most seats in the 2026 Bulgarian parliamentary election?

## Current lean

Lean **no / sharply below market** on PB winning the most seats.

## Prior / starting view

Starting from the market alone, the baseline implied view is that PB has about a **95.95%** chance of winning the most seats.

## Evidence supporting the claim

- **PB is a listed contesting coalition for the 19 April 2026 election**
  - source: Polymarket contract plus election overview
  - why it matters causally: the outcome is live and contract-relevant, not a phantom listing
  - direct/indirect: direct for contract relevance, indirect for probability
  - weight: medium

- **PB is associated with former president Rumen Radev in accessible election context**
  - source: election overview
  - why it matters causally: a high-profile founder can create unusually strong early support for a new coalition
  - direct/indirect: contextual
  - weight: medium

## Evidence against the claim

- **PB appears to be a newly formed coalition with zero current parliamentary seats**
  - source: election overview
  - why it matters causally: new entrants rarely convert immediately into an almost-certain first-place seat win in proportional parliamentary systems
  - direct/indirect: contextual but highly relevant
  - weight: high

- **GERB–SDS remains the largest current parliamentary bloc at 66 seats**
  - source: election overview
  - why it matters causally: entrenched leading blocs create a strong outside-view hurdle for any newcomer to finish first on seats
  - direct/indirect: contextual
  - weight: high

- **The accessible source stack does not independently verify a strong late polling consensus with PB clearly first**
  - source: verification pass across available accessible sources
  - why it matters causally: without that confirmation, a 95.95% probability is too aggressive
  - direct/indirect: source-quality / verification evidence
  - weight: high

## Ambiguous or mixed evidence

- Bulgarian politics has been unstable and fragmented since 2021, which can create room for rapid party reordering.
- A charismatic new entrant backed by a former president can outperform normal new-party baselines.
- But fragmentation cuts both ways: it can help a new entrant break through, while also making exact first-place seat certainty harder.

## Conflict between inputs

The main conflict is not factual but **weighting-based**:
- the market price implies PB is essentially already the winner
- the accessible structural evidence shows PB as a new coalition facing entrenched parties and does not independently confirm that near-certainty

What would resolve it:
- multiple independent late polls or seat models with PB clearly first
- credible Bulgaria-focused reporting treating PB as the consensus front-runner
- election-night official or near-official results

## Key assumptions

- Structural outside-view priors remain informative this close to the election.
- Accessible sources are not merely missing a universally known domestic polling consensus that PB is already dominant.
- Exact first place on seats is a harder event than general relevance or strong debut performance.

## Key uncertainties

- Whether there are late Bulgarian-language polls or seat models not accessible here that put PB clearly first.
- How strongly Radev's involvement shifts the usual new-entrant base rate.
- Whether constituency-level seat conversion favors PB more than national baselines suggest.

## Disconfirming signals to watch

- Credible independent reporting that PB is the clear polling leader.
- Fresh seat projections showing PB ahead of GERB–SDS by a stable margin.
- Early official counts placing PB first on seats.

## What would increase confidence

- Direct accessible CIK confirmation of election administration pages without anti-bot blocks.
- At least one additional independent accessible source showing the same party ordering.
- A clean late polling or seat-projection table from a reputable outlet.

## Net update logic

The case starts with an extreme market price. The main update away from that price comes from the outside view: PB looks like a very new coalition with no incumbent seats, and the most accessible structural source still centers established blocs. That does not make PB unlikely in an absolute sense, but it makes **95.95%** look unjustified on the current public evidence floor.

## Suggested downstream use

- Forecast update away from near-certainty.
- Orchestrator synthesis input focused on whether hidden polling evidence exists that could overwhelm the structural prior.
