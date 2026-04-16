---
type: evidence_map
case_key: case-20260413-1fcb4925
dispatch_id: dispatch-case-20260413-1fcb4925-20260413T212655Z
research_run_id: ad2462a8-2e50-428b-a45d-1c7f2d4df798
analysis_date: 2026-04-13
persona: risk-manager
domain: politics
subdomain: elections
entity:
topic: "Bulgaria 2026 parliamentary election"
question: "Will Progressive Bulgaria (PB) win the most seats in the 2026 Bulgarian parliamentary election?"
driver: elections
date_created: 2026-04-13
agent: Orchestrator
status: draft
confidence: medium
conflict_status: moderate_poll_dispersion
action_relevance: high
related_entities: []
related_drivers: ["elections", "polling"]
proposed_entities: ["progressive-bulgaria", "gerb-sds", "we-continue-the-change-democratic-bulgaria", "central-election-commission-of-bulgaria", "rumen-radev"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-1fcb4925/researcher-analyses/2026-04-13/dispatch-case-20260413T212655Z/personas/risk-manager.md"]
tags: ["bulgaria", "election", "evidence-map", "risk-manager"]
---

# Summary

PB looks like the front-runner, but the evidence supports “likely” more than “near-certain.” The main risk is not hidden evidence that PB is losing; it is that the market is pricing away normal election uncertainty despite poll dispersion, seat-conversion mechanics, and the novelty of the PB vehicle.

## Question being evaluated

Will Progressive Bulgaria (PB) win the most seats in the 2026 Bulgarian parliamentary election?

## Current lean

Lean yes, but at a materially lower probability than the market implies.

## Prior / starting view

Starting baseline was the market price of 0.9595, which implies roughly 95.95% confidence that PB wins the most seats.

## Evidence supporting the claim

- Multiple March contextual sources place PB first in the race.
  - Source/note: `researcher-source-notes/2026-04-13-risk-manager-polls-and-field.md`
  - Why it matters: the simplest path to winning the most seats is still being the top vote-getter entering the final week.
  - Direct or indirect: indirect/contextual.
  - Weight: high.
- Balkan Insight cites a Sova Harris poll with PB on 30.9% versus GERB on 19.3%.
  - Why it matters: a double-digit lead would normally be enough to survive ordinary polling error.
  - Direct or indirect: indirect/contextual.
  - Weight: medium-high.
- Google News snippets indicate Reuters, Alpha Research coverage, and TVP World also reported PB leading.
  - Why it matters: independent confirmation that PB-first is not a one-source artifact.
  - Direct or indirect: indirect/contextual.
  - Weight: medium.

## Evidence against the claim

- Market Links poll relayed by The Sofia Globe shows PB at only 21.1% versus GERB at 18.6%.
  - Why it matters: that smaller lead is still first place but much more vulnerable to late swing, house effects, or seat inefficiency.
  - Direct or indirect: indirect/contextual.
  - Weight: high.
- PB is a brand-new alliance built quickly around Radev.
  - Why it matters: new vehicles can underperform polls because organization, ballot discipline, district depth, and candidate quality may lag national enthusiasm.
  - Direct or indirect: indirect/contextual.
  - Weight: medium.
- The field is fragmented and multiple parties hover near the 4% threshold.
  - Why it matters: seat allocation can move sharply even on modest vote-share changes, so “wins the vote” and “wins the most seats” are close but not identical in risk terms.
  - Direct or indirect: indirect/contextual.
  - Weight: medium-high.
- Official results are not due immediately; the CEC seat-allocation window runs until April 23.
  - Why it matters: election-night consensus may still be revised, and the contract ultimately falls back to official CEC reporting if credible-reporting consensus is ambiguous.
  - Direct or indirect: direct on mechanics, indirect on outcome.
  - Weight: medium.

## Ambiguous or mixed evidence

- High turnout can help legitimacy of the result but can cut in different directions depending on whether it reflects mobilized Radev supporters or broader anti-incumbent consolidation.
- PB’s anti-establishment appeal may both expand its ceiling and increase volatility because late-cycle narratives can move softer supporters.

## Conflict between inputs

- Main disagreement is weighting-based and polling-based, not factual.
- Some sources imply PB has a comfortable lead in the low 30s; others imply only a narrow lead in the low 20s.
- Evidence that would resolve this: final-week high-quality polls from multiple houses, or district-level/election-night reporting tied to seat allocation.

## Key assumptions

- PB’s lead is not mostly a transient leader-popularity effect.
- No rival consolidates enough late support to overtake PB in seats.
- The contract’s named PB outcome maps cleanly to the coalition contesting the election.

## Key uncertainties

- Poll house effects and lack of raw polling detail.
- Seat conversion under fragmentation and threshold effects.
- How much confidence should be assigned to a newly created alliance one week before voting.

## Disconfirming signals to watch

- Late polling showing GERB tied with or ahead of PB.
- Credible reports of PB organizational weakness or district-level underperformance.
- Election-night returns showing GERB converting more efficiently into seats despite trailing or tying on vote share.

## What would increase confidence

- Final-week convergence of independent polls with PB holding a clear first-place margin.
- Early official or consensus reporting showing PB clearly ahead in both votes and projected seats.
- Clear evidence that threshold-exposed minor parties are not siphoning meaningful PB votes.

## Net update logic

The evidence supports PB as the favorite, but not at the market’s near-lock level. What mattered most was the combination of consistent PB-first polling and simultaneous signs of fragility: wide dispersion in lead size, a large undecided bloc, a very new alliance structure, and seat-allocation sensitivity to threshold crossings. Those features create enough tail risk that I downweight the market’s extreme confidence.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review