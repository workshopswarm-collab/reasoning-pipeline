---
type: evidence_map
case_key: case-20260416-683adab3
dispatch_id: dispatch-case-20260416-683adab3-20260416T160048Z
research_run_id: 7df07f2b-9dd6-42b5-aebc-688a89026d91
analysis_date: 2026-04-16
persona: market-implied
domain: culture
subdomain: film-box-office-and-ranking-surfaces
entity: the-numbers
topic: will-lee-cronin-s-the-mummy-opening-weekend-box-office-be-between-10m-and-15m
question: "Will \"Lee Cronin's The Mummy\" Opening Weekend Box Office be between 10m and 15m?"
driver:
date_created: 2026-04-16
agent: Orchestrator
status: draft
confidence: medium
conflict_status: "low-direct-conflict / high-data-sparseness"
action_relevance: high
related_entities: ["box-office-mojo", "the-numbers"]
related_drivers: []
proposed_entities: ["warner-bros", "lee-cronins-the-mummy"]
proposed_drivers: ["theater-count-scale", "horror-opening-demand"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-683adab3/researcher-analyses/2026-04-16/dispatch-case-20260416-683adab3-20260416T160048Z/personas/market-implied.md"]
tags: ["evidence-map", "market-implied", "box-office"]
---

# Summary

The net evidence supports a modestly market-aligned view: the 10–15m bracket looks plausible and probably modal, but the 70% market price is a bit rich given sparse independent pre-release gross evidence.

## Question being evaluated

Will the finalized The Numbers 3-day opening weekend figure for Lee Cronin’s The Mummy, covering April 17–19, 2026, fall between 10m and 15m inclusive of the higher bracket on exact boundaries?

## Current lean

Lean yes, but with less confidence than the market price implies.

## Prior / starting view

Starting from the market price, the default prior is that the market may already be aggregating film-tracking or crowd-information not fully visible in a quick public-source pass.

## Evidence supporting the claim

- **The Numbers title page confirms a wide Warner Bros. domestic launch on April 17.**
  - Source: source note on The Numbers title page.
  - Why it matters: a wide launch is structurally consistent with a non-negligible opening and makes the middle bracket plausible.
  - Direct vs indirect: direct.
  - Weight: high.

- **The Numbers contextual reporting projects a 3,200-theater launch.**
  - Source: source note on The Numbers homepage/news item dated April 9.
  - Why it matters: 10–15m on 3,200 theaters only requires a plausible mid-range per-theater average for an R-rated horror opening.
  - Direct vs indirect: contextual but close to direct.
  - Weight: high.

- **Settlement mechanics favor this same data ecosystem.**
  - Source: market rules plus The Numbers title page existence.
  - Why it matters: the same source family that frames release scale also determines resolution, reducing one kind of data mismatch risk.
  - Direct vs indirect: direct for mechanics.
  - Weight: medium.

## Evidence against the claim

- **No clean public gross forecast was directly retrieved in this run.**
  - Source: research process outcome.
  - Why it matters: a bracket market at 70% ideally would have stronger corroboration than release scale alone.
  - Direct vs indirect: direct limitation.
  - Weight: high.

- **Bracket risk is inherently two-sided.**
  - Why it matters: even if the title opens decently, it can miss by coming in below 10m or above 15m; a 70% yes price requires fairly concentrated distribution around the middle band.
  - Direct vs indirect: inferential.
  - Weight: medium.

- **Independent-source confirmation was weak.**
  - Source: Box Office Mojo page was not extractable in a useful way; web search was bot-blocked.
  - Why it matters: independence of evidence is lower than ideal.
  - Direct vs indirect: direct process limitation.
  - Weight: medium.

## Ambiguous or mixed evidence

- The film’s horror genre can support a decent opening, but without direct tracking it does not cleanly separate a 7–9m opener from a 12–14m opener or a 16m overshoot.
- International rollout beginning before domestic release may indicate broad studio support, but it does not directly resolve the domestic 3-day bracket.

## Conflict between inputs

There is little outright factual conflict. The main issue is not contradiction but **data sparsity**: strong settlement mechanics and release-scale evidence versus weak independent confirmation of the actual gross range.

## Key assumptions

- 3,200 theaters is approximately correct by opening weekend.
- Mid-range horror demand is the right analogue rather than either breakout demand or outright collapse.
- The Numbers final weekend figure will reflect the standard 3-day April 17–19 window with Thursday previews rolled into weekend performance as the market description states.

## Key uncertainties

- Actual preview strength and audience awareness.
- Whether the title is tracking under 10m or has enough interest to threaten >15m.
- Whether other contemporaneous wide releases dilute attention more than expected.

## Disconfirming signals to watch

- Opening-day trade commentary indicating low-single-digit Friday.
- Confirmed theater count materially below projected scale.
- Early weekend estimates clustering outside the 10–15m range.

## What would increase confidence

- A direct trade tracking estimate.
- A second usable independent box-office source confirming expected opening range.
- Opening-day/previews data consistent with a 10–15m full weekend extrapolation.

## Net update logic

The market prior survives first contact with evidence because the contract is clearly tied to The Numbers and the publicly inspected The Numbers context supports a substantial wide launch. But because direct forecast evidence remains thin and bracket markets are sensitive to both downside and upside misses, the market still looks a little overconfident rather than obviously wrong.

## Suggested downstream use

Use as an orchestrator synthesis input with moderate weight: likely yes / middle bracket plausible, but confidence should be discounted for source-independence weakness and lack of direct public tracking in this run.