---
type: evidence_map
case_key: case-20260413-e8e9e57e
dispatch_id: dispatch-case-20260413-e8e9e57e-20260413T224434Z
research_run_id: 591f929f-0818-4f72-80d6-96bfbf15871e
analysis_date: 2026-04-13
persona: risk-manager
domain: sports
subdomain: hockey
entity: connor-mcdavid
topic: will-connor-mcdavid-win-the-2025-2026-nhl-art-ross-trophy
question: "Will Connor McDavid win the 2025–2026 NHL Art Ross Trophy?"
driver: operational-risk
date_created: 2026-04-13
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["connor-mcdavid", "nhl"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-e8e9e57e/researcher-analyses/2026-04-13/dispatch-case-20260413-e8e9e57e-20260413T224434Z/personas/risk-manager.md"]
tags: ["evidence-map", "sports", "hockey", "art-ross"]
---

# Summary

This evidence map shows that the sporting case for Yes is strong, while the remaining nontrivial risk is mostly settlement mechanics and official-source alignment rather than the scoring race itself.

## Question being evaluated

Will Connor McDavid win the 2025–2026 NHL Art Ross Trophy?

## Current lean

Lean Yes, but with slightly less confidence than the market price implies.

## Prior / starting view

Starting view was that a 94.75% market price required checking whether the race was effectively over or whether the contract hid resolution mechanics risk.

## Evidence supporting the claim

- Hockey-Reference 2025-26 skater statistics: McDavid listed as points leader with 133 points, ahead of Kucherov (128) and MacKinnon (126).
  - Direct or indirect: indirect/contextual for settlement, direct for the underlying sporting fact.
  - Weight: high.
  - Why it matters causally: the Art Ross is awarded to the points leader.

- Same table shows McDavid also leading assists and having a nontrivial cushion over second place.
  - Direct or indirect: contextual.
  - Weight: medium-high.
  - Why it matters causally: reinforces that the apparent lead is not a razor-thin or ambiguous edge.

## Evidence against the claim

- The contract explicitly says official NHL information is the primary resolution source.
  - Direct or indirect: direct for settlement mechanics.
  - Weight: high.
  - Why it matters causally: secondary stat sites do not settle the market.

- The contract also says the market resolves No if the listed player is not announced as a finalist.
  - Direct or indirect: direct for contract interpretation.
  - Weight: medium.
  - Why it matters causally: creates an operational edge-case if finalist communication is unusual, delayed, or not standardized for this trophy.

## Ambiguous or mixed evidence

- NHL web pages were fetchable but not easily readable through the current extraction path, and NHL public API endpoints returned 403 in this environment. That does not contradict McDavid leading; it just weakens direct official verification in-run.

## Conflict between inputs

There is no substantive factual conflict between sources obtained. The tension is between strong contextual sporting evidence and slightly imperfect direct official verification access.

## Key assumptions

- Official NHL records/award communication will match the observed points-leader outcome.
- No late stat correction or unusual finalist-interpretation issue overturns the straightforward reading.

## Key uncertainties

- Whether the NHL publishes a clean finalist/winner surface in time for this contract’s resolution.
- Whether the finalist clause could create avoidable ambiguity despite the underlying stats being clear.

## Disconfirming signals to watch

- Official NHL naming another Art Ross winner.
- Disagreement between official NHL stats and major secondary tables.
- Credible reporting confusion around finalist qualification or award attribution.

## What would increase confidence

- A directly accessible NHL official trophy or season-leaders page naming McDavid as Art Ross winner/points leader.
- Clean consensus reporting citing NHL official confirmation.

## Net update logic

The evidence moved the view from “maybe the market is too extreme” to “the market is probably right directionally, but the remaining gap to certainty is mostly source-of-truth and contract-mechanics risk.” Sporting uncertainty appears low; operational resolution uncertainty remains small but not zero.

## Suggested downstream use

- orchestrator synthesis input
- decision-maker review
- retrospective evaluation of extreme-probability sports-award contracts where settlement mechanics can matter more than the race itself