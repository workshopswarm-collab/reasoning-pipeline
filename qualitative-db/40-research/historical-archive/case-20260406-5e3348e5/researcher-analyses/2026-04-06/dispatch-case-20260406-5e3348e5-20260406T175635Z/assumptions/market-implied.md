---
type: assumption_note
case_key: case-20260406-5e3348e5
dispatch_id: dispatch-case-20260406-5e3348e5-20260406T175635Z
research_run_id: 77bfa70c-7514-40fa-83f1-9aff691acd70
analysis_date: 2026-04-06
persona: market-implied
domain: entertainment
subdomain: streaming
entity:
topic: netflix-us-top10-resolution-mapping
question: "Will \"XO, Kitty Season 3\" be the top US Netflix show this week?"
driver:
date_created: 2026-04-06
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: days
related_entities: []
related_drivers: []
proposed_entities: ["xo-kitty", "netflix-top-10-us-tv-chart"]
proposed_drivers: ["chart-label-resolution-mapping"]
upstream_inputs: []
downstream_uses: []
tags: ["assumption", "resolution", "mapping", "netflix"]
---

# Assumption

The market should resolve against Netflix's United States TV Top 10 page for the week 3/23/26-3/29/26, and the top-ranked `Season 2` entry on that page corresponds to the intended XO, Kitty contract subject despite the market title saying `Season 3`.

## Why this assumption matters

This assumption carries most of the confidence in the tradeable interpretation: if the title-level mapping is wrong, the 95% market price could be overstating certainty despite the governing page otherwise being clear.

## What this assumption supports

- A high probability estimate close to, but slightly below, the market-implied 95%.
- The interpretation that the market is mostly efficient because it is following the correct official chart and reporting window.
- A conclusion that residual risk is mainly contract-label ambiguity rather than ranking uncertainty.

## Evidence or logic behind the assumption

- The market description explicitly names Netflix's Top 10 TV shows update as the governing resolution surface.
- The market description also says the relevant update will reflect the previous week Monday-Sunday, which is 3/23/26-3/29/26.
- Netflix's own page currently displays `United States | 3/23/26 - 3/29/26` and a top-ranked `Season 2` entry at #1 in Shows.
- Streaming chart pages often abbreviate title cards in extraction output, so the franchise name can be partially lost even when the rank order is preserved.
- Given the market is priced at 0.95, the market likely assumes this mapping issue is either a harmless title typo or a non-issue in practice.

## What would falsify it

- A clearer Netflix surface showing the #1 title is a different `Season 2` show rather than XO, Kitty.
- Polymarket rules clarification that a market-title season mismatch is binding enough to force a different interpretation.
- A later Netflix page update or cleaner extraction showing a different title at #1 for the same US weekly window.

## Early warning signs

- Any alternate official or near-official Netflix surface that names a different #1 show for the same week.
- Visible market repricing away from the low-90s before close.
- Rule-discussion or trader commentary focused on the season-number mismatch rather than on chart leadership.

## What changes if this assumption fails

Confidence should fall sharply because the main remaining edge would become contract interpretation rather than chart confirmation. In that case, a lower estimate and more explicit rule-risk framing would be required.

## Notes that depend on this assumption

- `qualitative-db/40-research/cases/case-20260406-5e3348e5/researcher-analyses/2026-04-06/dispatch-case-20260406-5e3348e5-20260406T175635Z/personas/market-implied.md`
- `qualitative-db/40-research/cases/case-20260406-5e3348e5/researcher-source-notes/2026-04-06-market-implied-netflix-us-top10-week-2026-03-23.md`