---
type: evidence_map
case_key: case-20260416-f08c3dae
dispatch_id: dispatch-case-20260416-f08c3dae-20260416T041907Z
research_run_id: 89381137-def4-4dce-b5b0-809757080f68
analysis_date: 2026-04-16
persona: base-rate
domain: sports
subdomain: soccer
entity:
topic: "evidence net for CD Tolima vs Deportivo Pereira"
question: "Will CD Tolima win on 2026-04-18?"
driver:
date_created: 2026-04-16
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: medium
related_entities: []
related_drivers: []
proposed_entities: ["CD Tolima", "Deportivo Pereira"]
proposed_drivers: ["home-field strength in domestic league matches", "favorite-price calibration in soccer 1X2 markets"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-f08c3dae/researcher-source-notes/2026-04-16-base-rate-polymarket-market-page.md", "qualitative-db/40-research/cases/case-20260416-f08c3dae/researcher-source-notes/2026-04-16-base-rate-context-note.md", "qualitative-db/40-research/cases/case-20260416-f08c3dae/researcher-analyses/2026-04-16/dispatch-case-20260416-f08c3dae-20260416T041907Z/assumptions/base-rate.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-f08c3dae/researcher-analyses/2026-04-16/dispatch-case-20260416-f08c3dae-20260416T041907Z/personas/base-rate.md"]
tags: ["evidence-map", "soccer", "base-rate"]
---

# Summary

Evidence net modestly favors a Yes lean, but the case is being carried more by structural prior + market anchor than by rich independent football-data retrieval.

## Question being evaluated

Will CD Tolima win the April 18, 2026 Colombia Primera A match versus Deportivo Pereira?

## Current lean

Lean Yes, but slightly below market confidence.

## Prior / starting view

A domestic home team priced this strongly is usually a legitimate favorite, but outright-win contracts are still materially exposed to draw risk.

## Evidence supporting the claim

- **Market price at 0.76**
  - Source: assignment context / market page.
  - Why it matters: a strong favorite price is usually informative in ordinary league football.
  - Direct or indirect: indirect.
  - Weight: medium.
- **No strong accessible contrary evidence recovered during this run**
  - Source: contextual retrieval note.
  - Why it matters: absent a clear negative catalyst, large contrarian deviations from a strong favorite price are hard to justify.
  - Direct or indirect: indirect.
  - Weight: low-to-medium.
- **Low-difficulty case framing**
  - Source: assignment context.
  - Why it matters: suggests this is probably not a rule-sensitive or hidden-complexity trap.
  - Direct or indirect: indirect.
  - Weight: low.

## Evidence against the claim

- **Soccer draw risk remains substantial even for favorites**
  - Source: outside-view structural prior.
  - Why it matters causally: a team can be better and still fail to win because the contract requires an outright victory, not just avoiding defeat.
  - Direct or indirect: indirect.
  - Weight: medium.
- **Independent contextual evidence depth was limited**
  - Source: contextual retrieval note.
  - Why it matters causally: without good odds/team-news/stat sources, confidence should be capped and sharp disagreement with market should be avoided.
  - Direct or indirect: direct about workflow, indirect about match outcome.
  - Weight: medium.

## Ambiguous or mixed evidence

- The market itself is informative, but because this persona is base-rate oriented, it should not simply mirror the market without some discount for ordinary soccer upset/draw risk and incomplete independent confirmation.

## Conflict between inputs

- Little true factual conflict.
- The main tension is weighting-based: how much to trust the market anchor versus how much to discount for limited accessible independent context.

## Key assumptions

- The market is roughly capturing a real favorite setup.
- No late lineup or injury shock materially changes the matchup before kickoff.

## Key uncertainties

- Exact team news and current form.
- Clean independent odds confirmation.
- Whether any late market move signals hidden information.

## Disconfirming signals to watch

- Sharp late drift against Tolima.
- Credible reporting of absences or squad rotation.
- Strong preview data showing the matchup is materially closer than the market implies.

## What would increase confidence

- A clean bookmaker odds page showing Tolima as a clear home favorite.
- Reliable form / lineup confirmation from a trusted football-data source.

## Net update logic

The outside-view prior starts with "favorite, but not certainty". The market's 0.76 price pushes toward Yes, but limited independent context and ordinary draw risk justify a modest discount rather than full agreement.

## Suggested downstream use

- Forecast update.
- Orchestrator synthesis input, with explicit note that this lane is more valuable as calibration discipline than as rich case-specific scouting.
