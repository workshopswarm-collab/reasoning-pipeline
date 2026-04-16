---
type: evidence_map
case_key: case-20260413-ac4c8995
dispatch_id: dispatch-case-20260413-ac4c8995-20260413T204806Z
research_run_id: 1d891e3b-c016-4597-84a1-27c36126ccf6
analysis_date: 2026-04-13
persona: risk-manager
domain: politics
subdomain: elections
entity:
topic: will-united-left-bsp-win-at-least-one-seat-in-the-2026-bulgarian-parliamentary-election
question: "Will United Left (BSP) win at least one seat in the 2026 Bulgarian parliamentary election?"
driver: elections
date_created: 2026-04-13
agent: Orchestrator
status: draft
confidence: medium
conflict_status: "low-direct-conflict / high-residual-uncertainty"
action_relevance: high
related_entities: []
related_drivers: ["elections", "polling"]
proposed_entities: ["BSP – United Left"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-ac4c8995/researcher-analyses/2026-04-13/dispatch-case-20260413-ac4c8995-20260413T204806Z/personas/risk-manager.md"]
tags: ["risk-manager", "bulgaria", "bsp", "threshold-risk"]
---

# Summary

The evidence nets to a Yes lean because BSP–United Left starts from a recent parliamentary foothold well above the entry threshold, while the currently observed downside evidence is mostly about generalized Bulgarian political churn rather than a specific documented collapse of BSP below 4%.

## Question being evaluated

Will United Left (BSP) win at least one seat in the 2026 Bulgarian parliamentary election?

## Current lean

Lean Yes, but not as confidently as a mid-70s market price suggests.

## Prior / starting view

Starting view was moderately bullish because an established parliamentary coalition usually has several paths to retain at least token representation.

## Evidence supporting the claim

- October 2024 election baseline: BSP–OL won 7.32% and 19 seats.
  - Source: 2026-04-13-risk-manager-bulgaria-election-context.md and 2024 election reference.
  - Why it matters causally: an incumbent parliamentary coalition does not need breakout performance; it needs only to stay above threshold.
  - Direct or indirect: indirect but highly relevant baseline.
  - Weight: high.
- Electoral threshold remains 4%.
  - Source: 2026 Bulgarian election contextual reference.
  - Why it matters causally: defines the main failure mechanism; BSP has substantial room versus its last result.
  - Direct or indirect: direct on rules.
  - Weight: high.
- Active April 2026 campaign presence on BSP site.
  - Source: 2026-04-13-risk-manager-current-context.md.
  - Why it matters causally: lowers the chance of hidden operational non-participation.
  - Direct or indirect: direct on campaign activity, indirect on vote retention.
  - Weight: medium.

## Evidence against the claim

- Bulgaria remains in a prolonged snap-election crisis with churn, weak governments, and fragmented competition.
  - Source: POLITICO Bulgaria coverage page; election contextual references.
  - Why it matters causally: fragmentation and instability can compress mid-tier parties and create threshold accidents.
  - Direct or indirect: indirect.
  - Weight: medium.
- The source set available in this run did not include a clean, recent independent poll specifically confirming BSP–United Left safely above threshold.
  - Why it matters causally: without current polling, there is residual risk that the 2024 base has decayed more than expected.
  - Direct or indirect: evidence gap rather than direct negative evidence.
  - Weight: medium-high as a fragility point.

## Ambiguous or mixed evidence

- BSP's status as an incumbent parliamentary actor cuts both ways: it supports baseline durability, but association with failed government periods can also produce voter punishment.
- Consensus-reporting markets can look easy while still carrying temporary ambiguity before official certification.

## Conflict between inputs

There was no strong factual conflict across sources. The main issue is not contradiction; it is limited independent current-cycle measurement of BSP's vote share.

## Key assumptions

- BSP–United Left remains ballot-present and organizationally intact.
- Residual support has not fallen from 7.32% in 2024 to below 4% by election day.
- Consensus reporting and official CIK tabulation will identify any seat win cleanly.

## Key uncertainties

- Current true vote share.
- Whether late-cycle anti-incumbent or coalition-fragmentation effects are stronger than the prior-election baseline suggests.
- Whether any registration or coalition-structure issue creates an unexpected procedural tail risk.

## Disconfirming signals to watch

- Credible independent polling showing BSP at or below 4%.
- Reporting of coalition fracture, disqualification, or list-registration problems.
- Election-night credible reporting indicating BSP is below threshold nationally.

## What would increase confidence

- Recent independent polling placing BSP clearly above 4%.
- CIK candidate-registration surfaces confirming normal ballot participation.
- Multiple credible Bulgarian or international outlets describing BSP as expected to remain represented.

## Net update logic

The key update is that the contract asks only for any seat. Given a recent 19-seat baseline and no direct evidence of collapse, the default should be Yes. The risk-manager adjustment is to cut below the market because current-cycle independent confirmation is thin and Bulgarian fragmentation creates threshold tail risk.

## Suggested downstream use

Use as forecast update input and synthesis input, with emphasis on threshold risk and source-quality caveats rather than on directional novelty.