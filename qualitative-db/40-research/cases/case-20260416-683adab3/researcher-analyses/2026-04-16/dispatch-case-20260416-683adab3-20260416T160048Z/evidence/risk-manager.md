---
type: evidence_map
case_key: case-20260416-683adab3
dispatch_id: dispatch-case-20260416-683adab3-20260416T160048Z
research_run_id: c8d47c6a-8d60-4362-8756-f54ea97c7c9c
analysis_date: 2026-04-16
persona: risk-manager
domain: culture
subdomain: film-box-office-and-ranking-surfaces
entity: the-numbers
topic: lee-cronins-the-mummy-opening-weekend-box-office
question: "Will \"Lee Cronin's The Mummy\" opening weekend box office be between 10m and 15m?"
driver:
date_created: 2026-04-16
agent: Orchestrator
status: draft
confidence: medium-low
conflict_status: low
action_relevance: high
related_entities: ["box-office-mojo", "the-numbers"]
related_drivers: []
proposed_entities: ["lee-cronins-the-mummy", "warner-bros", "blumhouse", "atomic-monster", "new-line-cinema"]
proposed_drivers: ["opening-weekend-box-office", "distribution-scale", "pre-release-tracking"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-683adab3/researcher-analyses/2026-04-16/dispatch-case-20260416-683adab3-20260416T160048Z/personas/risk-manager.md"]
tags: ["evidence-map", "risk-manager", "box-office"]
---

# Summary

This evidence map nets out a modest lean toward the 10m-15m bracket while emphasizing that current confidence should stay below the market’s implied confidence because direct pre-release numeric evidence is sparse.

## Question being evaluated

Will the final The Numbers 3-day opening-weekend gross for Lee Cronin’s The Mummy on April 17-19, 2026 resolve between $10m and $15m?

## Current lean

Slight lean yes, but with meaningful fragility and less confidence than the market price implies.

## Prior / starting view

Starting baseline was the market price itself: 0.70 implied probability, suggesting the bracket is viewed as more likely than not and perhaps close to consensus.

## Evidence supporting the claim

- The Numbers source note: film has a confirmed domestic `Wide` release on April 17, 2026.
  - Why it matters causally: a wide release creates a plausible floor for a midrange opening.
  - Direct vs indirect: direct for timing/distribution format, indirect for gross size.
  - Weight: medium.
- Recognizable horror/IP/studio package from The Numbers and Deadline context.
  - Why it matters causally: recognizable genre/IP plus studio backing can support a middle-band debut even without breakout demand.
  - Direct vs indirect: contextual.
  - Weight: low-to-medium.

## Evidence against the claim

- No final weekend data exists yet on the governing source.
  - Why it matters causally: without direct numeric evidence, precision inside a narrow band is fragile.
  - Direct vs indirect: direct about information state.
  - Weight: high.
- No strong clean pre-release tracking source was recovered in this run.
  - Why it matters causally: the market may be pricing confidence that is not well supported by auditable public evidence.
  - Direct vs indirect: direct about evidence quality.
  - Weight: high.
- Contract is narrow and bracketed; outcomes just below 10m or just above 15m are live tails.
  - Why it matters causally: even if the movie opens near expectations, a narrow range can miss easily.
  - Direct vs indirect: direct from contract structure.
  - Weight: high.

## Ambiguous or mixed evidence

- Box Office Mojo was useful only as a mechanics cross-check because title-page retrieval looked noisy in this environment.
- Deadline confirms the project but does not provide decisive opening-weekend guidance here.

## Conflict between inputs

There is little factual conflict. The main issue is weighting-based: market confidence looks stronger than the directly auditable evidence recovered in this run.

## Key assumptions

- Wide release plus horror/IP recognition is enough to keep the film in the middle band.
- Lack of strong contrary tracking is not itself evidence of weakness.
- The final The Numbers weekend figure will not be distorted by unusual reporting/finality ambiguity.

## Key uncertainties

- True pre-release demand.
- Preview strength.
- Theater count and competitive pressure at launch.
- Whether final gross lands near a bracket edge.

## Disconfirming signals to watch

- Credible reporting that previews or Friday gross are soft enough to imply sub-10m.
- Any strong tracking/reporting implying breakout above 15m.
- Final The Numbers/Box Office Mojo mismatch that delays finality.

## What would increase confidence

- Clean pre-release tracking from a credible trade source.
- Theater count confirmation and competitive set context.
- Early Friday/Saturday grosses that point clearly to the middle of the band rather than the edges.

## Net update logic

The evidence supports a mild yes lean because the release is wide and real, but the lack of robust direct numeric evidence means confidence should be marked down relative to the market. The current lean comes more from plausible distribution/genre structure than from hard pre-release revenue evidence.

## Suggested downstream use

- Orchestrator synthesis input.
- Decision-maker review with explicit caution on confidence calibration.