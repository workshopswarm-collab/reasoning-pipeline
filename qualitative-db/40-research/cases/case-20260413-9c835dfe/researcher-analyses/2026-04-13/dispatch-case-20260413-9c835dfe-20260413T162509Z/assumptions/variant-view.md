---
type: assumption_note
case_key: case-20260413-9c835dfe
research_run_id: 9121e3c6-f005-4128-93cc-a16e903fc68b
analysis_date: 2026-04-13
persona: variant-view
domain: crypto
subdomain: institutions
entity: strategy
topic: "official-announcement timing governs resolution"
question: "Did Strategy announce a purchase of more than 1000 BTC during April 7-13, 2026?"
driver: reliability
date_created: 2026-04-13
agent: variant-view
status: active
certainty: high
importance: medium
time_horizon: immediate
related_entities: ["strategy", "bitcoin"]
related_drivers: ["reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["resolution-assumption", "timing"]
dispatch_id: dispatch-case-20260413-9c835dfe-20260413T162509Z
---

# Assumption

The market resolves on the timing of the public announcement by Strategy/Michael Saylor, not on when the underlying BTC was economically purchased.

## Why this assumption matters

The contract explicitly says the market resolves based on announcements made within the designated time frame regardless of when the purchases were made. If that reading were wrong, one could mis-handle cases where the purchase happened earlier but the announcement landed during the window.

## What this assumption supports

- A high-confidence Yes view despite possible ambiguity about the exact execution dates of the BTC buys.
- Weighting the April 13 official disclosure as decisive.

## Evidence or logic behind the assumption

- The market description explicitly says it resolves based on announcements made within the market's designated time frame.
- It explicitly names official information from MicroStrategy or Michael Saylor as the resolution source.
- Strategy's official purchases page and linked filing/public text constitute such official information.

## What would falsify it

- A clarifying market rule or moderator note saying announcement timing does not count unless the purchase itself also occurred in-window.
- Evidence that the official April 13 post was not actually public within the window.

## Early warning signs

- Conflicting market comments or moderator guidance emphasizing trade-execution date over announcement date.
- Discovery that the company page was updated retroactively after the window close.

## What changes if this assumption fails

The case would require re-checking the actual purchase execution dates and possibly lowering confidence materially if those dates were outside April 7-13.

## Notes that depend on this assumption

- Main finding at `qualitative-db/40-research/cases/case-20260413-9c835dfe/researcher-analyses/2026-04-13/dispatch-case-20260413-9c835dfe-20260413T162509Z/personas/variant-view.md`
- Source note on the Strategy purchases page
