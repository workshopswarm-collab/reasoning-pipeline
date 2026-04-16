---
type: evidence_map
case_key: case-20260414-4c35c81d
dispatch_id: dispatch-case-20260414-4c35c81d-20260414T204205Z
research_run_id: 02719a2b-735e-4389-83a6-a04c37a7db57
analysis_date: 2026-04-14
persona: risk-manager
domain: sports
subdomain: soccer
entity:
topic: al-qadisiyah-vs-al-shabab
question: "Will Al Qadisiyah Saudi Club win on 2026-04-23?"
driver: performance
date_created: 2026-04-14
agent: orchestrator
status: draft
confidence: medium
conflict_status: "timing-and-source-of-truth ambiguity"
action_relevance: high
related_entities: ["saudi-arabia"]
related_drivers: ["performance"]
proposed_entities: ["al-qadsiah", "al-shabab", "saudi-pro-league"]
proposed_drivers: ["resolution-timestamp-misalignment"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-4c35c81d/researcher-analyses/2026-04-14/dispatch-case-20260414-4c35c81d-20260414T204205Z/personas/risk-manager.md"]
tags: ["sports", "soccer", "evidence-map", "source-of-truth", "timing-risk"]
---

# Summary

The netted evidence says Al Qadisiyah was the stronger side on season performance, but the contract-level risk is that the relevant match already finished 2-2, making a win impossible absent source misidentification.

## Question being evaluated

Will Al Qadisiyah Saudi Club win on 2026-04-23?

## Current lean

Lean strongly no on settlement risk grounds, despite Al Qadisiyah being the stronger team.

## Prior / starting view

Initial prior from the 0.83 market price and league-table gap would have been that Al Qadisiyah was a strong favorite if the match were still upcoming.

## Evidence supporting the claim

- ESPN standings: Al Qadsiah 4th with 62 points and +36 GD versus Al Shabab 12th with 31 points and -6 GD.
  - Why it matters: strong season-quality gap.
  - Direct or indirect: indirect/contextual for the exact market.
  - Weight: moderate.
- Market itself priced Qadisiyah around 83%.
  - Why it matters: crowd baseline and embedded confidence signal.
  - Direct or indirect: indirect.
  - Weight: low-to-moderate because the price may be stale/misaligned.

## Evidence against the claim

- Polymarket page metadata for this exact slug states the Round 29 matchup ended in a 2-2 draw.
  - Why it matters: if accurate, a draw directly falsifies the win outcome.
  - Direct or indirect: direct to the contract outcome, though from market metadata rather than explicit settlement rules.
  - Weight: high.
- ESPN fixture page for 2026-04-14 shows `Al Qadsiah 2 - 2 Al Shabab FT`.
  - Why it matters: independent scoreboard confirmation that the teams drew.
  - Direct or indirect: direct to whether a win occurred.
  - Weight: high.

## Ambiguous or mixed evidence

- Assignment prompt says the game is scheduled for 2026-04-23, but external sources indicate it was already played on 2026-04-14.
- I did not retrieve an official league source cleanly in this run, so governing-source confidence is not maximal.

## Conflict between inputs

- Disagreement type: timing-based and source-of-truth based.
- The market assignment text implies a future event; external evidence points to an already completed draw.
- Best resolver: explicit market rules / settlement source or official league fixture/result page for this exact match.

## Key assumptions

- The Polymarket slug and ESPN fixture refer to the same underlying match.
- No administrative reversal changes the result from draw to Qadisiyah win.

## Key uncertainties

- Whether the date in the assignment is a stale or erroneous field.
- Whether the governing source of truth for settlement is official league data, Polymarket market rules, or another sports feed.

## Disconfirming signals to watch

- Any official source showing the match is actually on 2026-04-23.
- Any settlement documentation indicating this market references a different fixture.
- Any correction changing the final score from 2-2.

## What would increase confidence

- Official Saudi Pro League result page for the same fixture.
- Explicit Polymarket settlement source naming the authoritative sports data provider.

## Net update logic

The strongest contextual evidence favored Al Qadisiyah as the better team, but the direct outcome evidence dominates because a favorite that already drew cannot still satisfy a win contract. The risk-manager update is therefore driven by contract/timestamp fragility, not by a disagreement about team quality.

## Suggested downstream use

Use as an orchestrator synthesis input and decision-maker review input, with emphasis on possible stale market pricing or resolution-surface mismatch.