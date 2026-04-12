---
type: assumption_note
case_key: case-20260409-d9a24086
dispatch_id: dispatch-case-20260409-d9a24086-20260409T165631Z
research_run_id: 944c1d53-703a-409c-879d-4c3348385e9a
analysis_date: 2026-04-09
persona: risk-manager
domain: economics
subdomain: macro-data-and-indicators
entity: bureau-of-labor-statistics
topic: march-2026-cpi-threshold-risk
question: "Will monthly inflation increase by 0.8% or more in March?"
driver: operational-risk
date_created: 2026-04-09
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: immediate
related_entities: ["bureau-of-labor-statistics"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: ["threshold-resolution-risk"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260409-d9a24086/researcher-analyses/2026-04-09/dispatch-case-20260409-d9a24086-20260409T165631Z/personas/risk-manager.md"]
tags: ["assumption-note", "cpi", "threshold-risk", "seasonal-adjustment"]
---

# Assumption

The market is overconfident because reaching a published 0.8% seasonally adjusted monthly CPI-U print requires a tail monthly outcome, while the contract resolves on a single rounded official BLS number.

## Why this assumption matters

The price is about 94.65%, so most of the risk analysis is about whether uncertainty is being underpriced rather than whether the event is directionally plausible.

## What this assumption supports

- A below-market probability estimate.
- A view that the main edge is uncertainty/threshold risk, not a strong directional call against elevated inflation.
- A stress-test framing centered on rounding, seasonal adjustment, and one-print settlement.

## Evidence or logic behind the assumption

- The governing source is one official BLS print to one decimal place.
- BLS explicitly uses seasonally adjusted CPI-U for short-term trend analysis and updates seasonal factors annually.
- Boundary contracts can be fragile because a small underlying difference can separate 0.7% from 0.8% after seasonal adjustment and rounding.

## What would falsify it

- A credible pre-release nowcast consensus clustering clearly above 0.8% seasonally adjusted.
- Evidence that the market has already absorbed a strong, independent forecast stack pointing to 0.8%+.
- The official BLS release printing 0.8% or higher.

## Early warning signs

- Late-breaking high-frequency inflation previews or consensus summaries pointing materially above recent monthly prints.
- Multiple independent macro desks converging on 0.8%+ rather than a mixed or boundary distribution.

## What changes if this assumption fails

If strong independent pre-release evidence points to 0.8%+ as the central case rather than a tail threshold, the risk-manager view should move materially toward the market and treat current pricing as justified rather than overconfident.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260409-d9a24086/researcher-analyses/2026-04-09/dispatch-case-20260409-d9a24086-20260409T165631Z/personas/risk-manager.md