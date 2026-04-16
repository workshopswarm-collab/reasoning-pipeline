---
type: evidence_map
case_key: case-20260414-26cfc91d
dispatch_id: dispatch-case-20260414-26cfc91d-20260414T181516Z
research_run_id: 6344b1c6-7139-4d75-858c-882c3fd80799
analysis_date: 2026-04-14
persona: risk-manager
domain: sports
subdomain: soccer
entity:
topic: inter-vs-cagliari-risk-netting
question: "Will FC Internazionale Milano win on 2026-04-17?"
driver: injuries-health
date_created: 2026-04-14
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: []
related_drivers: ["injuries-health"]
proposed_entities: ["internazionale", "cagliari", "lega-serie-a"]
proposed_drivers: ["lineup-rotation", "motivation-schedule-congestion"]
tags: ["sports", "soccer", "evidence-map", "risk-manager"]
---

# Summary

The net evidence favors Inter clearly, but the main risk-manager job here is to avoid over-reading an already-high price. The most realistic failure mode is not that Cagliari are secretly the better team; it is that soccer's draw/upset variance, plus possible lineup or motivation slippage, is larger than an 81.5% single-outcome price fully captures.

## Question being evaluated

Will FC Internazionale Milano win their Serie A match against Cagliari on 2026-04-17?

## Current lean

Inter should be favored strongly, but the pure win probability looks slightly below the Polymarket price once ordinary soccer variance and hidden lineup risk are respected.

## Prior / starting view

Starting view was that Inter were probably a deserved favorite because this is a simple home-match favorite case rather than a complex rules market.

## Evidence supporting the claim

- **ESPN fixture + records + form + odds payload** — direct for fixture existence and contextual for team quality; high weight. Confirms Inter home match, strong season record (24-3-5), positive recent form, and a large external odds edge.
- **Wikipedia 2025-26 Serie A context** — indirect/tertiary; low-to-medium weight. Corroborates that Inter have been one of the league's best sides while Cagliari have had poor runs.
- **Home venue at San Siro** — direct from ESPN event payload; medium weight. Home advantage matters, especially against a weaker away side.

## Evidence against the claim

- **Contract asks for a win, not merely avoiding defeat** — direct logic; high weight. Even strong favorites drop points via draws often enough that a win-only contract should not be treated like double chance.
- **No authoritative lineup/injury confirmation in hand yet** — direct research gap; medium weight. Late absences or rotation are a standard way heavy-favorite prices get punished.
- **Source-of-truth ambiguity on settlement page** — medium weight. The market description identifies the match, but the governing final score source is not fully explicit in the assignment prompt; this is manageable but should be noted.

## Ambiguous or mixed evidence

- External sportsbook odds support favoritism, but they also reflect bookmaker margin and may still leave true win probability below Polymarket's 81.5%.
- Recent-form strings are directionally useful but lossy and vulnerable to schedule-strength distortions.

## Conflict between inputs

No major source conflict found. The issue is more missing granularity than contradictory evidence.

## Key assumptions

- Inter field a sufficiently strong lineup.
- No major motivation distortion or scheduling congestion changes the intensity profile.
- Resolution is based on the official match result for regulation/full-time in the scheduled Serie A fixture.

## Key uncertainties

- Final lineup/injury availability.
- Whether any late market-moving team news emerges.
- Exact settlement authority Polymarket will lean on if there is a data discrepancy.

## Disconfirming signals to watch

- Credible reports of multiple Inter starters out or rested.
- Sharp adverse odds move against Inter.
- Any official fixture change, postponement, or venue issue.

## What would increase confidence

- Official Lega Serie A fixture page loaded cleanly with matching details.
- Trusted lineup/news confirmation within 24h of kickoff.
- Multiple independent books holding similar heavy-favorite pricing.

## Net update logic

The evidence justifies Inter as the favorite, but the risk-manager adjustment is to shave confidence versus a raw favorite narrative. The biggest reason is contract structure: a single-match win market leaves meaningful room for draws and variance even when one side is plainly superior.

## Suggested downstream use

Use as synthesis input and as a reminder not to let team-strength asymmetry erase ordinary soccer upset/draw variance.