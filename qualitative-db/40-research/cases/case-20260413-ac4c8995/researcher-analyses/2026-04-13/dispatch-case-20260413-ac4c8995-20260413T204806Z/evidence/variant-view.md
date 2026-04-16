---
type: evidence_map
case_key: case-20260413-ac4c8995
dispatch_id: dispatch-case-20260413-ac4c8995-20260413T204806Z
research_run_id: 7333fea4-29fd-4624-ad0c-c4b05a48d21e
analysis_date: 2026-04-13
persona: variant-view
domain: politics
subdomain: bulgarian-parliamentary-election
entity:
topic: bulgarian-parliamentary-election-2026
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
proposed_entities: ["Central Election Commission of Bulgaria (CIK)", "BSP–United Left"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-ac4c8995/researcher-analyses/2026-04-13/dispatch-case-20260413-ac4c8995-20260413T204806Z/personas/variant-view.md"]
tags: ["variant-view", "evidence-netting", "bulgaria"]
---

# Summary
The market already prices BSP–United Left as likely to win at least one seat, but the variant view is that the crowd may still be modestly underpricing how low the entry bar is relative to BSP’s current status.

## Question being evaluated
Will United Left (BSP) win at least one seat in the 2026 Bulgarian parliamentary election?

## Current lean
Yes, with probability modestly above market.

## Prior / starting view
Starting view was that a parliamentary incumbent in a 4% threshold system should usually be favored to retain at least minimal representation, but late-fragmentation or collapse risk needed checking.

## Evidence supporting the claim
- **Current parliamentary status of BSP–United Left** from the election-context source.
  - Why it matters causally: incumbent machinery and existing representation reduce the probability of a total wipeout.
  - Direct/indirect: indirect for the 2026 result, but structurally relevant.
  - Weight: high.
- **4% threshold structure** from the contextual source and market description.
  - Why it matters causally: the contract asks only for one seat, so threshold clearance is the dominant mechanism.
  - Direct/indirect: direct on mechanism, indirect on outcome.
  - Weight: high.
- **Official source-of-truth clause naming CIK** in the market description.
  - Why it matters causally: reduces resolution ambiguity; seat count will ultimately be official.
  - Direct/indirect: direct for settlement logic.
  - Weight: medium.

## Evidence against the claim
- **Snap-election instability and chronic political fragmentation in Bulgaria**.
  - Why it matters causally: repeated electoral churn raises risk that mid-sized blocs can erode quickly.
  - Direct/indirect: contextual.
  - Weight: medium.
- **Lack of robust independently verified current polling in this run** due search/fetch friction.
  - Why it matters causally: without late polling, there is residual risk that BSP is already near the threshold.
  - Direct/indirect: meta-evidentiary.
  - Weight: medium.

## Ambiguous or mixed evidence
- Existing parliamentary representation can either signal durable floor support or a stale anchor if the electorate has moved sharply since the last election.

## Conflict between inputs
No major factual conflict found; the main limitation is source depth, not contradictory evidence.

## Key assumptions
- BSP–United Left remains a coherent ballot-present entity.
- No late polling collapse toward or below 4% emerges before election day.

## Key uncertainties
- Exact current April 2026 polling position.
- Whether any coalition or branding changes alter ballot recognition.

## Disconfirming signals to watch
- Multiple independent polls putting BSP–United Left below 4%.
- Credible reports of coalition rupture or registration trouble.
- Sharp late-campaign scandal or tactical-voting squeeze.

## What would increase confidence
- Independent polling average above threshold with margin.
- Direct official candidate-list confirmation under the expected label.
- Credible local reporting on coalition continuity.

## Net update logic
The main netting logic is that the contract is easier than a broad performance question: one seat in a 4% threshold system for a current parliamentary bloc is a relatively forgiving target. The main reason not to be more bullish is unverified late polling / fragmentation risk.

## Suggested downstream use
- forecast update
- orchestrator synthesis input
- source collection gap
