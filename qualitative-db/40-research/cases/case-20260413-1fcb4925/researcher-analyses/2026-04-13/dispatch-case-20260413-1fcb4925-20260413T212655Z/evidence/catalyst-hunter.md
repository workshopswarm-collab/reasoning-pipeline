---
type: evidence_map
case_key: case-20260413-1fcb4925
dispatch_id: dispatch-case-20260413-1fcb4925-20260413T212655Z
research_run_id: bdd3a424-5b42-4c0d-b6f1-06f1f3241596
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: politics
subdomain: bulgaria-election
entity:
topic: "2026 Bulgarian parliamentary election"
question: "Will Progressive Bulgaria (PB) win the most seats in the 2026 Bulgarian parliamentary election?"
driver: elections
date_created: 2026-04-13
agent: catalyst-hunter
status: draft
confidence: medium
conflict_status: moderate
action_relevance: high
related_entities: []
related_drivers: ["elections", "polling"]
proposed_entities: ["progressive-bulgaria", "central-election-commission-of-bulgaria", "gerb-sds", "pp-db", "rumen-radev"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-1fcb4925/researcher-analyses/2026-04-13/dispatch-case-20260413-1fcb4925-20260413T212655Z/personas/catalyst-hunter.md"]
tags: ["auditability", "catalyst", "election", "polling"]
---

# Summary

The core issue is whether a real late-cycle catalyst around Rumen Radev and PB is strong enough to justify a near-certain seat-plurality claim before election day. Current evidence supports PB as a meaningful contender, but not yet as a 96% terminal favorite.

## Question being evaluated

Will Progressive Bulgaria (PB) win the most seats in the 2026 Bulgarian parliamentary election?

## Current lean

Lean no relative to the 95.95% market price; PB is live but not near-certain.

## Prior / starting view

Start from skepticism of any pre-election market priced above 95% in a multi-party parliamentary contest unless supported by authoritative late polling or direct result reporting.

## Evidence supporting the claim

- **PB is a real, measured electoral actor, not just a rumor**  
  Source: `researcher-source-notes/2026-04-13-catalyst-hunter-pb-election-landscape.md`  
  Why it matters: the election page includes PB in polling tables and as a listed coalition, so the market is tied to an actual competitive entrant.  
  Direct/indirect: indirect for winning most seats, direct for competitive relevance.  
  Weight: medium.

- **Radev's entry is itself the main repricing catalyst**  
  Source: same note.  
  Why it matters: a former president launching a coalition only weeks before the election can cause abrupt narrative and polling shifts.  
  Direct/indirect: indirect.  
  Weight: medium.

- **Contract simplicity after votes are counted**  
  Source: `researcher-source-notes/2026-04-13-catalyst-hunter-polymarket-contract.md`  
  Why it matters: if PB truly finishes first in seats, settlement ambiguity is low because the contract points to credible reporting with CIK fallback.  
  Direct/indirect: direct on resolution mechanics, indirect on current probability.  
  Weight: medium.

## Evidence against the claim

- **The market is asking about seat plurality before the vote, not long-run party growth**  
  Source: Polymarket contract note.  
  Why it matters causally: PB can be important, popular, or coalition-relevant without actually topping the seat table.  
  Direct/indirect: direct.  
  Weight: high.

- **PB is a late-created coalition with very little time left before 19 April 2026**  
  Source: election-landscape note.  
  Why it matters causally: late organizational entrants often face conversion and list-structure friction even when leader popularity is strong.  
  Direct/indirect: indirect.  
  Weight: high.

- **Available accessible evidence does not show decisive independent confirmation that PB is already first**  
  Source: this run's verification pass.  
  Why it matters causally: in a high-resolution-risk case with a 95%+ market price, absence of easy confirming evidence is itself meaningful.  
  Direct/indirect: indirect but important.  
  Weight: high.

## Ambiguous or mixed evidence

- Wikipedia poll references imply PB may have significant support, but the page is an aggregation layer rather than the pollster's own primary publication.
- CIK is explicitly the official fallback source of truth, but direct access was blocked from this environment, limiting independent confirmation of registration/result surfaces in-run.

## Conflict between inputs

- There is a weighting conflict between **narrative momentum** (Radev/PB as disruptive entrant) and **seat-conversion caution** (established blocs may still finish first).
- The disagreement is mainly timing-based and weighting-based, not rule-based.
- Best resolution evidence would be multiple independent final polls or election-day exit polls.

## Key assumptions

- PB momentum is real but not enough to justify near certainty.
- Established machine advantage still matters in a parliamentary seat-plurality contest.
- No hidden official or high-quality poll evidence exists that would instantly validate the 96% price.

## Key uncertainties

- Exact latest standings in independent polls.
- Whether PB support is geographically efficient enough for seats.
- Whether any final-week event consolidates anti-establishment votes behind PB.

## Disconfirming signals to watch

- Two or more late independent polls with PB clearly first.
- Credible exit polls with PB leading seat projections.
- Consensus reporting immediately after polls close showing PB won most seats.

## What would increase confidence

- Direct access to underlying MarketLinks / Sova / Gallup poll outputs in extractable form.
- Direct CIK access confirming official lists and later official tallies.
- A clear final-week poll average rather than a secondary compilation.

## Net update logic

The main update is from "PB is a serious catalyst" to "PB is serious, but the market price overstates certainty." What mattered most was the combination of extreme price, short time remaining, and lack of directly accessible authoritative confirmation that PB already leads the field. I downweighted pure popularity/narrative arguments because the contract counts seats only.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- follow-up investigation focused on final independent polls and election-day exit polls