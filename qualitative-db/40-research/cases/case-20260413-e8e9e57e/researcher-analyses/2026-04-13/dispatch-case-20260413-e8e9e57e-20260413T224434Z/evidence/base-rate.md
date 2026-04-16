---
type: evidence_map
case_key: case-20260413-e8e9e57e
dispatch_id: dispatch-case-20260413-e8e9e57e-20260413T224434Z
research_run_id: a80eaf7e-b215-47f4-be38-516200e5c854
analysis_date: 2026-04-13
persona: base-rate
domain: sports
subdomain: hockey
entity: connor-mcdavid
topic: "Art Ross Trophy resolution"
question: "Will Connor McDavid win the 2025–2026 NHL Art Ross Trophy?"
date_created: 2026-04-13
agent: base-rate
status: draft
confidence: medium-high
conflict_status: low
action_relevance: high
related_entities: ["connor-mcdavid", "nhl"]
related_drivers: ["reliability"]
proposed_entities: []
proposed_drivers: ["points-leader-to-trophy-award linkage"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-e8e9e57e/researcher-analyses/2026-04-13/dispatch-case-20260413-e8e9e57e-20260413T224434Z/personas/base-rate.md"]
tags: ["evidence-map", "art-ross", "scoring-leader"]
driver:
---

# Summary

The evidence strongly supports Yes because multiple statistics sources show McDavid finishing first in points, which ordinarily determines the Art Ross Trophy, but confidence stops short of absolute because direct NHL trophy confirmation was not cleanly retrievable through current tooling.

## Question being evaluated

Will Connor McDavid win the 2025–2026 NHL Art Ross Trophy?

## Current lean

Strong lean Yes.

## Prior / starting view

Before checking current-season sources, the outside-view prior for any named player winning a season scoring title is low. McDavid's player-specific prior is much higher than generic because he is a repeat elite scorer, but still nowhere near 95% without current leaderboard confirmation.

## Evidence supporting the claim

- Hockey-Reference season skater table lists McDavid as 2025-26 points leader with 133 points, ahead of Kucherov (128) and MacKinnon (126).
  - source: `researcher-source-notes/2026-04-13-base-rate-hockey-reference-scoring-leaders.md`
  - causal relevance: the Art Ross normally goes to the NHL points leader.
  - evidence type: direct contextual evidence
  - weight: high
- ESPN 2025-26 skating stats page ranks McDavid first and shows the same top-three ordering and point totals.
  - source: `researcher-source-notes/2026-04-13-base-rate-espn-scoring-leaders.md`
  - causal relevance: independent publication check reduces single-source error risk.
  - evidence type: direct contextual evidence
  - weight: medium-high
- Market description itself names official NHL information as primary source of truth and consensus credible reporting as fallback.
  - source: assignment contract text
  - causal relevance: clarifies that stats consensus can matter if direct official trophy page retrieval is difficult.
  - evidence type: contract / resolution evidence
  - weight: high

## Evidence against the claim

- I did not obtain a clean official NHL trophy-announcement page or official NHL stats output through available web-fetch and direct API attempts.
  - why it matters: the contract explicitly prefers official NHL information.
  - evidence type: source-of-truth gap
  - weight: medium
- Secondary sources in sports statistics often ultimately depend on the same underlying official data feed, so independence is not perfect.
  - why it matters: reduces the evidentiary boost from simple cross-site agreement.
  - evidence type: structural source-quality caution
  - weight: low-medium

## Ambiguous or mixed evidence

- The market description contains finalist language: `If the listed player is not announced as a finalist for the 2025-26 Art Ross Trophy, this market will resolve to No.` In practice the Art Ross is usually a points-leader award, so the `finalist` wording may be boilerplate or potentially awkward drafting rather than a meaningful extra condition.

## Conflict between inputs

There is no direct factual conflict in the sourced leaderboard data. The main tension is between strong secondary evidence and incomplete direct retrieval of the preferred official source.

## Key assumptions

- Standard Art Ross award mechanics hold.
- No late official stat correction overturns the points lead.
- Consensus reporting fallback would be accepted if direct official announcement retrieval remains awkward.

## Key uncertainties

- Whether an official NHL trophy page or announcement exists but was missed by current tooling.
- Whether the contract's finalist wording could create an unexpected interpretation issue.

## Disconfirming signals to watch

- NHL announcement naming a different winner.
- Official stat correction changing the points leaderboard.
- Any credible report of a dispute over scoring totals or award procedure.

## What would increase confidence

- Direct NHL page stating McDavid won the 2025-26 Art Ross Trophy.
- Official NHL stats page extract clearly showing final points leader in machine-readable form.

## Net update logic

The starting view was that extreme certainty required current-season confirmation because even elite players do not usually deserve a 95%+ ex post award probability without verified finishing position. Two strong statistics sources showing McDavid clearly ahead by 5 points pushed the estimate sharply upward. The remaining discount versus near-100% is almost entirely a source-of-truth / verification discount, not a substantive hockey-performance discount.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review focused on source-of-truth confidence rather than player-performance debate