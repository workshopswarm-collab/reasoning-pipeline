---
type: evidence_map
case_key: case-20260414-625be8a3
dispatch_id: dispatch-case-20260414-625be8a3-20260414T002740Z
research_run_id: 1519c8fa-902d-4474-aa3a-ea3d4da47b07
analysis_date: 2026-04-14
persona: base-rate
domain: politics
subdomain: ballot-measures
entity:
topic: virginia-redistricting-referendum
question: "Will the Virginia redistricting referendum pass?"
driver: elections
date_created: 2026-04-14
agent: base-rate
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: []
related_drivers: ["elections", "legal"]
proposed_entities: ["Virginia Department of Elections", "Virginia redistricting referendum"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-625be8a3/researcher-analyses/2026-04-14/dispatch-case-20260414-625be8a3-20260414T002740Z/personas/base-rate.md"]
tags: ["evidence-map", "base-rate", "ballot-measure"]
---

# Summary

Base-rate lean is Yes, but less extreme than the market because statewide constitutional referenda usually pass only if the proposal is low-salience or institutionally backed, while this contract also carries nontrivial legal/timing failure risk.

## Question being evaluated

Will the Virginia redistricting referendum pass under the contract definition, which requires majority approval of valid votes cast by the contract deadline and otherwise resolves No?

## Current lean

Lean Yes, but with meaningful discount versus the 0.89 market price.

## Prior / starting view

Before source checks, a generic outside-view prior for a state constitutional referendum about process reform is above 50% if officially scheduled, but well below 90% unless there is unusually strong bipartisan elite support and low cancellation risk.

## Evidence supporting the claim

- Official Virginia Department of Elections amendment page exists and ties the measure to the April 2026 special election.
  - source: 2026-04-14-base-rate-virginia-dept-of-elections-amendment-page.md
  - why it matters causally: confirms an actual administered referendum path, not a speculative proposal
  - direct or indirect: direct on existence/timing, indirect on passage probability
  - weight: high for occurrence/source-of-truth, medium for passage
- The contract itself says postponement before November 3, 2026 does not automatically kill Yes; it can remain open until the vote occurs.
  - source: market description / Polymarket event page
  - why it matters causally: reduces some near-term scheduling risk versus an April-21-only interpretation
  - direct or indirect: direct on resolution mechanics
  - weight: medium
- Structural base rate: once a statewide referendum is formally on the calendar, outright cancellation is less common than occurrence, so the dominant path is a real vote rather than immediate contract failure.
  - source: outside-view institutional logic supported by election-administration context
  - direct or indirect: contextual
  - weight: medium

## Evidence against the claim

- The market description explicitly begins with “Pending legal challenges,” so a legal derailment path is not hypothetical.
  - source: market description / Polymarket event page
  - why it matters causally: contract can resolve No if the vote never happens by deadline or is definitively canceled
  - direct or indirect: direct on risk framing, indirect on actual legal odds
  - weight: high
- Even if the vote occurs, constitutional amendments and redistricting-related reforms are not automatic landslides; outside-view approval rates for institutional reforms are usually materially below the high-80s unless evidence of overwhelming support exists.
  - source: base-rate reasoning plus lack of strong confirming public evidence in this run
  - why it matters causally: the market may be pricing almost-certain passage without enough observable justification
  - direct or indirect: contextual
  - weight: medium-high
- The source set available in this run did not produce a strong independent confirming report of broad elite consensus or polling support.
  - source: verification pass results
  - why it matters causally: absence of robust confirmation makes an 89% estimate feel aggressive
  - direct or indirect: indirect
  - weight: medium

## Ambiguous or mixed evidence

- Postponement before November 3 is mixed: it weakens an April timing narrative but does not necessarily imply failure under contract rules.
- Sparse extraction from the official page confirms existence more than substance.

## Conflict between inputs

There is no major factual conflict in the sourced material. The main disagreement is weighting-based: how much to discount an officially scheduled referendum for legal/timing risk and ordinary ballot-measure failure rates.

## Key assumptions

- The referendum occurs by the contract deadline.
- No hidden polling or elite-consensus evidence exists that would justify a much higher passage probability.
- The official Virginia reporting process remains the operative source of truth if public reporting is mixed.

## Key uncertainties

- The strength of the underlying legal challenge.
- Whether there is meaningful public or bipartisan support data not surfaced here.
- Whether the amendment text itself is framed in a way that historically improves or hurts voter approval.

## Disconfirming signals to watch

- Court action delaying or invalidating the vote.
- Credible reporting of organized opposition or poor polling.
- Official calendar change pushing the vote beyond the contract deadline.

## What would increase confidence

- A clearer official statement that the referendum will proceed on schedule or within the contract window.
- Independent local reporting showing broad cross-party or public support.
- Historical Virginia-specific data suggesting similar procedural referenda usually pass comfortably.

## Net update logic

The official scheduling evidence moves the prior above 50%, but the explicit legal-challenge clause and lack of strong independent passage evidence keep the estimate well below the market's near-certainty. The biggest adjustment is not from a dramatic case-specific fact; it is from refusing to round ordinary institutional uncertainty down to almost zero.

## Suggested downstream use

Use as orchestrator synthesis input and as a check against overconfident market anchoring.
