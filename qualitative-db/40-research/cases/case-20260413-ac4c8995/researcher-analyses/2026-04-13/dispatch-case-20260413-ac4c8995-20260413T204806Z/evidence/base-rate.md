---
type: evidence_map
case_key: case-20260413-ac4c8995
dispatch_id: dispatch-case-20260413-ac4c8995-20260413T204806Z
research_run_id: 38ca8319-d97a-4030-a20a-1f490786b6c7
analysis_date: 2026-04-13
persona: base-rate
domain: politics
subdomain: elections
entity:
topic: "BSP–United Left at least one seat in 2026 Bulgarian parliamentary election"
question: "Will United Left (BSP) win at least one seat in the 2026 Bulgarian parliamentary election?"
driver: elections
date_created: 2026-04-13
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: medium
related_entities: []
related_drivers: ["elections"]
proposed_entities: ["BSP – United Left coalition"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "elections", "bulgaria", "base-rate"]
---

# Summary

Base-rate lean is Yes, but below the market, because BSP–United Left starts from a prior seat-winning position above threshold, while the dominant remaining risk is a threshold breach rather than outright irrelevance.

## Question being evaluated

Will United Left (BSP) win at least one seat in the 2026 Bulgarian parliamentary election?

## Current lean

Yes, more likely than not and likely materially above even odds.

## Prior / starting view

Starting outside-view prior: an already seated, nationally organized coalition that recently cleared a 4% threshold should usually retain at least some parliamentary representation unless there is evidence of acute collapse.

## Evidence supporting the claim

- Prior above-threshold result: accessible election context shows BSP–United Left around 6.85-7.32% in the prior cycle, well above the 4% threshold. Weight: high. Directness: contextual but highly relevant.
- Current parliamentary presence: the coalition currently holds 19 seats, indicating existing voter base and organization. Weight: medium-high. Directness: contextual.
- Continued ballot presence for 2026: accessible election context lists BSP–United Left among contesting formations in the April 2026 election. Weight: medium-high. Directness: contextual.
- BSP organizational durability: BSP remains a longstanding national party with deep legacy infrastructure, making total disappearance less likely than for a newly assembled fringe coalition. Weight: medium. Directness: contextual.

## Evidence against the claim

- Threshold discontinuity: because Bulgaria uses a 4% threshold, parties can go from meaningful vote share to zero seats if support weakens enough. Weight: high. Directness: structural.
- Limited fresh polling verification in this run: due to unreliable web search and blocked CIK access, I did not independently recover robust late polling. Weight: medium. Directness: process limitation.
- Slight ambiguity in public contextual tables and naming: BSP, BSP–United Left, and market label “United Left (BSP)” likely refer to the same formation, but resolution-relevant naming should still be handled carefully. Weight: medium. Directness: contract interpretation / entity mapping.

## Ambiguous or mixed evidence

- The accessible public election page shows slightly different prior percentages for the coalition in different tables, though both are safely above threshold.
- Being a legacy party cuts both ways: organizational durability helps, but legacy left parties can also erode over time.

## Conflict between inputs

No material factual conflict between the accessible sources used here. The main issue is incompleteness rather than contradiction.

## Key assumptions

- BSP–United Left remains the relevant ballot line for the contract.
- The coalition stays above the 4% threshold.
- No late split, disqualification, or identity ambiguity undermines seat attribution.

## Key uncertainties

- Fresh pre-election polling or seat projection quality
- Whether any late campaign events materially changed vote share near threshold
- Whether official CIK presentation of the formation name maps cleanly to the market label without ambiguity

## Disconfirming signals to watch

- Credible polls showing the coalition below 4%
- Reporting of coalition breakup or ballot challenge
- Reporting confusion suggesting the contract may not map cleanly to the official list

## What would increase confidence

- Direct CIK candidate/ballot page confirming the exact list identity
- One or two independent late polls putting the coalition safely above 4%
- Credible media consensus that BSP–United Left remains a routine parliamentary entrant

## Net update logic

The strongest base-rate anchor is simple: this is not a start-up party trying to break in, but an incumbent parliamentary coalition that recently cleared threshold by a meaningful margin. That keeps the answer on the Yes side. I downweight the market modestly because the market price implies a fairly comfortable outcome, while threshold elections remain nonlinear and my direct late-cycle verification was limited.

## Suggested downstream use

- Orchestrator synthesis input
- Forecast update with attention to threshold fragility
- Follow-up investigation focused only on late polls and exact official list naming
