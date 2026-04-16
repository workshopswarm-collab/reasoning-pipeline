---
type: evidence_map
case_key: case-20260415-33c2f26e
dispatch_id: dispatch-case-20260415-33c2f26e-20260415T211658Z
research_run_id: af226156-e75b-4398-81aa-fcea90775c19
analysis_date: 2026-04-15
persona: market-implied
domain: sports
subdomain: soccer
entity:
topic: al-nassr-vs-al-ettifaq-2026-04-24
question: "Will Al Nassr Saudi Club win on 2026-04-24?"
driver:
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: []
related_drivers: []
proposed_entities: ["al-nassr-saudi-club", "al-ettifaq-saudi-club"]
proposed_drivers: ["club-strength-gap", "home-field-advantage", "soccer-draw-risk"]
upstream_inputs: []
downstream_uses: ["market-implied-finding"]
tags: ["evidence-map", "sports", "market-implied"]
---

# Summary

The evidence supports Al Nassr as the deserved favorite, but the exact 91.5% market price looks somewhat rich relative to what was directly verified in this run.

## Question being evaluated

Will Al Nassr Saudi Club win on 2026-04-24 within 90 minutes plus stoppage time?

## Current lean

Lean Yes, with a high probability but below the market's implied level.

## Prior / starting view

Starting view was to respect the 91.5% price as a serious prior and test whether public evidence could justify an extreme favorite.

## Evidence supporting the claim

- Polymarket contract page shows the market is actively pricing Al Nassr as an overwhelming favorite.
  - direct for market baseline
  - moderate weight as information aggregation signal, not independent truth
- Sofascore snippet shows the exact 24 Apr 2026 fixture at Al-Awwal Park.
  - direct for fixture existence
  - moderate weight
- Sofascore snippet indicates Al Nassr is 1st and Al Ettifaq 7th.
  - contextual for relative strength
  - moderate weight
- Soccerway snippet independently matches the same fixture/date/competition.
  - contextual cross-check
  - moderate weight

## Evidence against the claim

- Soccer matches have meaningful draw variance; a 91.5% home-win price leaves very little room for the combined draw/away-win tail.
  - indirect but structurally important
  - high weight as disconfirming consideration
- No directly verified bookmaker odds, official standings page, or lineup/injury evidence was secured in this run.
  - indirect source-quality limitation
  - moderate weight
- Search noise included some date inconsistencies on third-party pages, reducing confidence in exact contextual parsing.
  - indirect reliability issue
  - low-to-moderate weight

## Ambiguous or mixed evidence

- The market may embed sharper private/public information than was accessible in this short run, which argues for respecting the price even without visible supporting detail.
- But absent stronger independent pricing or official data, the exact extremity of the price is not fully auditable from gathered evidence alone.

## Conflict between inputs

No major factual conflict. Main tension is between the market's extreme confidence and the thinner-than-ideal independent verification set.

## Key assumptions

- Al Nassr is genuinely much stronger than Al Ettifaq at this moment.
- Home advantage matters materially.
- No major squad/injury shock intervenes before match day.

## Key uncertainties

- True fair probability from bookmaker consensus.
- Matchday lineup availability.
- Whether the standings gap seen in snippets fully reflects current underlying strength.

## Disconfirming signals to watch

- Bookmaker prices materially below ~85%.
- Significant Al Nassr injury/rotation news.
- Sharp pre-match market selloff.

## What would increase confidence

- Official league table and fixture confirmation.
- Major bookmaker 1X2 consensus.
- Credible team-news confirmation near kickoff.

## Net update logic

The market baseline remained the strongest single signal. Independent public evidence supported the direction of a strong Al Nassr edge, but not enough to fully endorse a 91.5% win probability. That yields a high-Yes estimate below market rather than a contrarian No lean.

## Suggested downstream use

Use as synthesis input showing that the market likely has the direction right but may be modestly overextended on magnitude.