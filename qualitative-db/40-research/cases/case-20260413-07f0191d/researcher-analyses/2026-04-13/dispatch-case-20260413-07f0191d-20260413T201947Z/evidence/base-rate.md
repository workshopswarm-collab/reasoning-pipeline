---
type: evidence_map
case_key: case-20260413-07f0191d
dispatch_id: dispatch-case-20260413-07f0191d-20260413T201947Z
research_run_id: 5ce06f01-c313-4c0b-8dad-fa0dc11eba92
analysis_date: 2026-04-13
persona: base-rate
domain: politics
subdomain: elections
entity:
topic: "2026 Bulgarian parliamentary election second-place market"
question: "Will GERB-UDF (GERB-SDS) finish second in the 2026 Bulgarian parliamentary election?"
driver: elections
date_created: 2026-04-13
agent: Orchestrator
status: draft
confidence: medium
conflict_status: "low-direct-conflict high-source-sensitivity"
action_relevance: high
related_entities: []
related_drivers: ["elections"]
proposed_entities: ["bulgaria", "gerb-sds", "pp-db", "revival", "dps"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-07f0191d/researcher-analyses/2026-04-13/dispatch-case-20260413-07f0191d-20260413T201947Z/personas/base-rate.md"]
tags: ["evidence-map", "elections", "base-rate"]
---

# Summary

The netted evidence points strongly toward GERB-SDS being the most likely first-place party, which mechanically makes a second-place finish relatively unlikely. The main fragility is source quality and independence rather than conflicting directional evidence.

## Question being evaluated

Will GERB-UDF (GERB-SDS) finish second in the 2026 Bulgarian parliamentary election?

## Current lean

No; GERB-SDS looks much more likely to finish first than second.

## Prior / starting view

A disciplined outside-view prior for a party that won clearly in the previous election and still leads most recent polling would assign low probability to an exact second-place finish unless the race were visibly two- or three-way close.

## Evidence supporting the claim

- Contract wording focuses on seats and second-place rank, not narrative popularity. Source: Polymarket contract note. Direct for resolution mechanics, but not supportive of GERB-SDS specifically.
- In some individual polls, GERB-SDS is materially down from its prior result, which in principle leaves room for a weaker-than-expected finish. Weight: low to medium, because the same polls still generally show it first.

## Evidence against the claim

- 2024 baseline: GERB-SDS led the last parliamentary election with 25.52% and 66 seats, while PP-DB, Revival, and DPS trailed. Source: Wikipedia election overview note. Weight: medium as historical structural context.
- Multiple March-April 2026 polls in the compiled table keep GERB-SDS first in projected seats: examples include Gallup 70 seats, Alpha 64, MarketLinks 66, Sova Harris 55. Source: Wikipedia election overview note. Weight: high as the best available current outside-view evidence.
- The next-tier parties appear to be competing with each other for second, often in the 20s to 40 projected-seat band, while GERB-SDS sits materially above them. Weight: high.

## Ambiguous or mixed evidence

- Wikipedia is not an authoritative polling source, but it aggregates several firms. This raises independence and validation concerns.
- Proportional representation means raw vote gaps do not translate perfectly into seat gaps, but the compiled seat estimates still place GERB-SDS first.

## Conflict between inputs

There is little substantive conflict among the available contextual inputs. The real conflict is between those inputs and the market price of 0.96 on GERB-SDS finishing second.

## Key assumptions

- The compiled polling table is directionally accurate.
- No major coalition-label or ballot-status issue makes the contract's GERB-UDF mapping diverge from GERB-SDS seat ranking.
- No late campaign shock of unusual magnitude occurs in the final days.

## Key uncertainties

- Lack of direct CIK access during this run because the site blocked fetches.
- Limited direct verification of individual pollster releases.
- Possible market-labeling or market-UI issue that is not visible from the contract text alone.

## Disconfirming signals to watch

- A reputable direct poll showing GERB-SDS in an actual race for second.
- Credible reporting of coalition reclassification or dissolution affecting the seat-attribution rule.
- Clear explanation that current public reporting consensus already treats GERB-SDS as second, not first.

## What would increase confidence

- Direct access to CIK election materials or registration / ballot pages for 2026.
- Direct pollster releases from Gallup, Alpha Research, MarketLinks, or Sova Harris confirming the compiled polling table.
- Independent media synthesis describing GERB-SDS as the first-place favorite and second place as a contest among other parties.

## Net update logic

The base-rate prior already leaned against GERB-SDS finishing second because it was the last election's first-place party. The available polling compilation reinforced that prior rather than challenging it. The market's 96% implied probability appears inconsistent with the best accessible outside-view evidence, so I net toward a low probability despite acknowledging source-sensitivity.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- source collection gap