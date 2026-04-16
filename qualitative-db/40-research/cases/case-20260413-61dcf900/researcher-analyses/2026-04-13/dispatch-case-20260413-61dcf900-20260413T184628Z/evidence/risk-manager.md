---
type: evidence_map
case_key: case-20260413-61dcf900
dispatch_id: dispatch-case-20260413-61dcf900-20260413T184628Z
research_run_id: 3cc1ceda-5a8b-4a9d-83ac-296d591c64da
analysis_date: 2026-04-13
persona: risk-manager
domain: sports
subdomain: hockey
entity: nhl
topic: los-angeles-kings-playoff-status
question: "Will the Los Angeles Kings make the 2025-26 NHL Playoffs?"
driver: operational-risk
date_created: 2026-04-13
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["nhl"]
related_drivers: ["operational-risk", "reliability", "seasonality"]
proposed_entities: ["los-angeles-kings"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-61dcf900/researcher-analyses/2026-04-13/dispatch-case-20260413-61dcf900-20260413T184628Z/personas/risk-manager.md"]
tags: ["evidence-map", "wildcard", "path-risk", "playoffs"]
---

# Summary

The Kings look more likely than not to make the playoffs because they are currently occupying a wild-card berth late in the season, but the key risk-manager takeaway is that they had not yet clinched in the extracted standings and therefore still carry nontrivial path risk.

## Question being evaluated

Will the Los Angeles Kings make the 2025-26 NHL Playoffs under official NHL qualification rules?

## Current lean

Lean Yes, but not at a confidence level that eliminates late-path fragility.

## Prior / starting view

Starting from the market price of 0.735, the baseline expectation was that Los Angeles was probably in favorable shape but perhaps not yet secure enough to justify very high confidence without checking official standings context.

## Evidence supporting the claim

- ESPN Western wild-card standings list Los Angeles as wild card 2 on 2026-04-13.
  - Direct/contextual: direct current-status evidence from a secondary standings source.
  - Why it matters: being above the cut line late is the single most important structural fact.
  - Weight: high.
- Official NHL standings surface is the market's governing resolution authority.
  - Direct/contextual: direct source-of-truth evidence for settlement mechanics.
  - Why it matters: confirms that qualification status is governed by official NHL information, not subjective reporting.
  - Weight: high for resolution logic.
- Only a few calendar days remain before market close/resolution on 2026-04-15.
  - Direct/contextual: contextual timing evidence.
  - Why it matters: fewer remaining games usually reduce the number of ways to lose a currently held berth.
  - Weight: medium.

## Evidence against the claim

- The Kings were not shown with an official clinch marker in the extracted ESPN wild-card page.
  - Direct/contextual: direct contextual evidence of unresolved risk.
  - Why it matters: if they had already clinched, this market would be nearly settled; absence of clinch means the downside path still exists.
  - Weight: high.
- The extraction leaves exact point and tie-break margins hard to parse.
  - Direct/contextual: data-quality / auditability issue.
  - Why it matters: unclear margins make overconfidence dangerous.
  - Weight: medium.
- Consensus-reporting fallback in the contract introduces some source-class ambiguity if official surfaces lag or extract poorly.
  - Direct/contextual: contract interpretation risk.
  - Why it matters: low direct settlement ambiguity, but enough to note because the assignment flagged consensus reporting dependency.
  - Weight: low-medium.

## Ambiguous or mixed evidence

- The Kings being on the line is bullish; the lack of an x-clinch marker is bearish. Together they imply likely qualification but not certainty.

## Conflict between inputs

There is no material factual conflict between sources in this run. The tension is between directional status (currently in) and confidence level (not yet clinched).

## Key assumptions

- Current wild-card positioning is robust enough to survive the final games.
- No hidden tie-break or remaining-schedule dynamic makes the position much weaker than it looks.

## Key uncertainties

- Exact margin over the first team out.
- Remaining-game difficulty and tie-break exposure.
- Whether official NHL standings would already show a clinch if extracted more cleanly.

## Disconfirming signals to watch

- Official NHL update moving the Kings below the line.
- Immediate chasing teams winning while Los Angeles loses.
- Official or independent standings showing materially smaller cushion than assumed.

## What would increase confidence

- Official NHL standings explicitly tagging Los Angeles with an x-clinch marker.
- Cleaner direct parsing of the point/tie-break gap over Nashville or the nearest chaser.

## Net update logic

The evidence keeps the case on the Yes side because Los Angeles is presently in a playoff berth near season end. The reason the estimate stays below the market is that the cleanest contextual extraction still does not show a clinch, and in a late-season race that means path risk is real even if limited.

## Suggested downstream use

Use this as an orchestrator synthesis input and decision-maker review input, with emphasis on uncertainty calibration rather than reversing the directional call.