---
type: evidence_map
case_key: case-20260409-d9a24086
dispatch_id: dispatch-case-20260409-d9a24086-20260409T165631Z
research_run_id: 944c1d53-703a-409c-879d-4c3348385e9a
analysis_date: 2026-04-09
persona: risk-manager
domain: economics
subdomain: macro-data-and-indicators
entity: bureau-of-labor-statistics
topic: march-2026-cpi-threshold-evidence-net
driver: operational-risk
date_created: 2026-04-09
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low-direct-conflict-high-forecast-uncertainty
action_relevance: high
related_entities: ["bureau-of-labor-statistics"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: ["threshold-resolution-risk"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260409-d9a24086/researcher-analyses/2026-04-09/dispatch-case-20260409-d9a24086-20260409T165631Z/personas/risk-manager.md"]
tags: ["evidence-map", "cpi", "threshold", "source-of-truth"]
---

# Summary

This evidence map nets out a simple but risk-sensitive case: the official BLS release mechanics are clear, but pre-release confidence at ~95% leaves little room for threshold, rounding, and forecast uncertainty.

## Question being evaluated

Will the March 2026 seasonally adjusted CPI-U monthly change, as reported by BLS to one decimal place, be 0.8% or more?

## Current lean

Lean no versus the market price; the event is plausible but current pricing appears too confident for a pre-release threshold contract.

## Prior / starting view

Starting view was that a 94.65% price likely embeds either a strong external consensus or market overconfidence; absent a clear independent nowcast stack, the safer risk-manager posture is to haircut confidence.

## Evidence supporting the claim

- BLS is the direct authoritative source and the contract wording is unambiguous about using the seasonally adjusted CPI-U monthly print. Direct, very high weight.
- Elevated recent monthly inflation readings make a high monthly print directionally plausible. Direct/contextual from recent BLS release, medium weight.
- The market itself is pricing the event near certainty, which is an informational signal even if not independent evidence. Indirect, low-to-medium weight.

## Evidence against the claim

- This is a one-decimal threshold market; 0.7% versus 0.8% is a narrow published boundary. Direct to contract mechanics, high weight.
- Seasonal adjustment matters explicitly, so intuitive raw-price narratives can mislead. Direct methodological risk, medium-to-high weight.
- No strong independent pre-release verification source was found in this run that would justify treating 94.65% as near-settled before the release. Indirect but important as a missing-evidence risk, high weight.

## Ambiguous or mixed evidence

- February CPI was 0.3%, which is below the target threshold but not dispositive for March.
- The BLS release notes sampling error and methodology limits; that supports caution around confidence, but the contract still settles on the published rounded number regardless.

## Conflict between inputs

There is no major factual conflict on settlement mechanics. The main conflict is weighting-based: how much confidence should be assigned before the official release in a threshold market with no strong independent nowcast verified in this run?

## Key assumptions

- The lack of a verified independent nowcast is informative enough to haircut the market.
- Threshold and rounding risk are materially underpriced by a 94.65% market.

## Key uncertainties

- Real March inflation dynamics before release.
- Whether a credible macro consensus already exists outside this run and genuinely supports 0.8%+.

## Disconfirming signals to watch

- A strong late consensus clustering above 0.8% seasonally adjusted.
- Any direct authoritative pre-release indication from BLS methodology notes or related official tables that materially raises the odds of 0.8%+.

## What would increase confidence

- A reputable independent nowcast/consensus source specifically for March 2026 CPI-U SA MoM.
- Cross-check against major macro wires or bank previews showing broad convergence at 0.8% or higher.

## Net update logic

The decisive update is not a directional macro thesis but contract-fragility logic: because the market is near certainty before the authoritative release, the main risk-manager edge is to discount certainty unless an independent forecast stack clearly justifies it.

## Suggested downstream use

- orchestrator synthesis input
- decision-maker review
- follow-up investigation for any missing nowcast/consensus source