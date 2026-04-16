---
type: evidence_map
case_key: case-20260413-07f0191d
dispatch_id: dispatch-case-20260413-07f0191d-20260413T201947Z
research_run_id: 7193f87b-1ac8-4e02-8e83-58e04bae3a49
analysis_date: 2026-04-13
persona: risk-manager
domain: politics
subdomain: bulgaria-election
entity:
topic: "second-place finisher in 2026 Bulgarian parliamentary election"
question: "Will GERB-UDF (GERB-SDS) finish second in the 2026 Bulgarian parliamentary election?"
driver: elections
date_created: 2026-04-13
agent: orchestrator
status: draft
confidence: medium-low
conflict_status: unresolved
action_relevance: high
related_entities: []
related_drivers: ["elections"]
proposed_entities: ["GERB-SDS", "PP-DB", "Revival", "Central Election Commission of Bulgaria"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["risk-manager finding", "orchestrator synthesis"]
tags: ["auditability", "exact-rank", "fragility"]
---

# Summary

Evidence leans against accepting the market's 96% confidence that GERB-SDS specifically finishes second. The core issue is exact-rank fragility, not whether GERB-SDS is competitive.

## Question being evaluated

Will GERB-UDF (GERB-SDS) finish second in the 2026 Bulgarian parliamentary election?

## Current lean

Lean no at current market price; GERB-SDS finishing second is plausible but not remotely locked.

## Prior / starting view

Starting view was that GERB-SDS was probably one of the most likely top-two finishers, but that exact-rank markets in fragmented parliamentary systems are usually more fragile than very high prices imply.

## Evidence supporting the claim

- Market contract clearly resolves on seat ranking, so an orderly GERB-SDS second-place outcome is contract-compatible and straightforward if one challenger cleanly outruns it. Direct, moderate weight.
- GERB-SDS is a major established coalition and therefore clearly has enough baseline support to remain near the top of the field. Indirect/contextual, moderate weight.
- Current parliamentary structure shows GERB-SDS, PP-DB, and Revival as the main large blocs, which means a GERB-SDS second-place finish is a realistic scenario rather than an exotic tail. Indirect/contextual, moderate weight.

## Evidence against the claim

- The strongest disconfirming fact is that the contextual election overview shows GERB-SDS currently as the largest parliamentary bloc, not the second largest. If anything, that makes first-place rather than second-place a live competing path. Indirect but important, high weight.
- Multiple meaningful competitors exist (PP-DB, Revival, and others in a fragmented field), which creates rank volatility and makes exact second place much less certain than simple top-two competitiveness. Indirect/contextual, high weight.
- No primary official polling, official party vote projections, or strong independent reporting was successfully recovered in this run to justify a 96% exact-rank confidence level. Direct about evidence quality, high weight.
- Search/fetch environment limitations prevented robust poll aggregation and Reuters-style independent confirmation, increasing epistemic risk and arguing against copying an extreme price. Direct about process risk, moderate weight.

## Ambiguous or mixed evidence

- The same fragmentation that can make GERB-SDS vulnerable to dropping from first to second can also make it vulnerable to slipping below second if protest or anti-establishment voting concentrates unexpectedly.
- Coalition branding matters: the contract refers to GERB-UDF / GERB-SDS, and coalition-dissolution language exists, but no evidence in this run suggests an imminent dissolution issue.

## Conflict between inputs

- There is no hard factual conflict among recovered sources.
- The conflict is between market confidence and the relatively thin directly recovered evidence base.
- What would resolve it: fresh independent national polling, authoritative Bulgarian reporting, or official late-campaign vote-intention data indicating GERB-SDS is clustered around second specifically rather than broadly top-two.

## Key assumptions

- Current parliamentary ordering is a meaningful but imperfect prior for election ranking risk.
- No major coalition split or candidate shock occurs before election day.
- The market is not simply mispricing top-two probability as second-place probability.

## Key uncertainties

- Latest independent polls.
- Whether one challenger is clearly ahead of GERB-SDS.
- Whether Revival or another bloc can overperform enough to threaten top-two ordering.
- How much confidence should be placed in contextual secondary sources given limited primary recovery.

## Disconfirming signals to watch

- Any credible poll showing GERB-SDS clearly leading the field.
- Any credible poll showing GERB-SDS running third.
- Official campaign-period developments changing coalition cohesion or turnout assumptions.

## What would increase confidence

- At least two independent, recent national polls with consistent second-place positioning for GERB-SDS.
- Bulgarian authoritative media or election analysts converging on GERB-SDS as specifically second most likely by seats.
- Direct CIK election-day or post-election tallies.

## Net update logic

The evidence did not prove GERB-SDS unlikely to finish second. It did show that a 96% price demands stronger verification than was recoverable here. The decisive issue is not directional hostility to GERB-SDS but skepticism toward extreme certainty on an exact-rank outcome in a fragmented parliamentary contest.

## Suggested downstream use

Use as orchestrator synthesis input and as a caution against overweighting the raw market price without stronger polling confirmation.