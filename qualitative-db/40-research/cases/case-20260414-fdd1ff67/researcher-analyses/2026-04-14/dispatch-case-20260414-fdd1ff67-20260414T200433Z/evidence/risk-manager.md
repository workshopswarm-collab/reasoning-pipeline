---
type: evidence_map
case_key: case-20260414-fdd1ff67
dispatch_id: dispatch-case-20260414-fdd1ff67-20260414T200433Z
research_run_id: e01428c5-13b4-4067-937f-da1d2c5978b6
analysis_date: 2026-04-14
persona: risk-manager
domain: sports
subdomain: soccer
entity:
topic: will-al-qadisiyah-saudi-club-vs.-al-shabab-saudi-club-end-in-a-draw
question: "Will Al Qadisiyah Saudi Club vs. Al Shabab Saudi Club end in a draw?"
driver:
date_created: 2026-04-14
agent: orchestrator
status: draft
confidence: medium
conflict_status: "low-direct-conflict / moderate-source-clarity-risk"
action_relevance: high
related_entities: []
related_drivers: []
proposed_entities: ["al-qadisiyah-saudi-club", "al-shabab-saudi-club", "saudi-pro-league"]
proposed_drivers: ["soccer-match-draw-rate", "source-of-truth-ambiguity"]
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "draw-market", "risk-manager"]
---

# Summary

This evidence map nets the main issue in the case: the market price is extreme for a standard full-time draw proposition, while the available direct evidence mostly clarifies settlement rather than justifying that extreme probability.

## Question being evaluated

Will Al Qadisiyah Saudi Club vs. Al Shabab Saudi Club end in a draw, settled on 90 minutes plus stoppage time?

## Current lean

Lean against the market’s level of confidence. A draw is plausible, but the available evidence does not justify a 76% draw probability.

## Prior / starting view

Starting view: standard soccer full-time draw markets are usually much lower than 76%, so the burden of proof should be on evidence that this is a special case.

## Evidence supporting the claim

- OddsPortal contextual page embeds a 2:2 final-result style output for the scheduled fixture.
  - Source: 2026-04-14-risk-manager-oddsportal-context.md
  - Why it matters: at least one external contextual source points toward draw plausibility.
  - Direct vs indirect: indirect/contextual.
  - Weight: low-to-medium because semantics of the 2:2 display are unclear.

- The fixture is listed as a normal Saudi Pro League match at the named venue.
  - Source: OddsPortal contextual page.
  - Why it matters: reduces the chance that the market is about a misidentified or exotic event.
  - Direct vs indirect: indirect/contextual.
  - Weight: low.

## Evidence against the claim

- Polymarket current price is 0.76, implying a very high confidence level for a standard full-time draw proposition.
  - Source: assignment context / market price.
  - Why it matters: this is precisely the confidence object being stress-tested.
  - Direct vs indirect: direct market baseline, not factual sports evidence.
  - Weight: high as baseline, not as truth.

- The market contract text clarifies resolution mechanics but does not provide independent team-strength evidence that would justify such an extreme draw probability.
  - Source: 2026-04-14-risk-manager-polymarket-contract.md
  - Why it matters: high settlement clarity does not equal high outcome certainty.
  - Direct vs indirect: direct for mechanics, indirect for probability.
  - Weight: high.

- No strong independent pre-match source was found here showing broad consensus near a 76% draw chance.
  - Source: research pass result.
  - Why it matters: absence of corroborating odds/model evidence increases risk that confidence is overstated.
  - Direct vs indirect: indirect.
  - Weight: medium.

## Ambiguous or mixed evidence

- OddsPortal’s embedded 2:2 output is suggestive but not cleanly interpretable; it could be prediction, cache artifact, or generated preview data.
- The governing source of truth is specified only generically as official statistics recognized by governing body or event organizers, leaving some ambiguity about the exact post-match surface.

## Conflict between inputs

There is no hard factual conflict. The main issue is weighting conflict:
- Polymarket price implies near-certainty.
- Available external context supports draw plausibility but not near-certainty.
- The disagreement is mostly interpretive and confidence-based rather than factual.

## Key assumptions

- This is an ordinary full-time draw market with standard 90-minute settlement.
- There is no hidden special circumstance causing true draw probability to be extraordinarily high.
- Lack of corroborating independent extreme pricing is informative.

## Key uncertainties

- Whether the 0.76 price reflects some hidden context not visible in fetched sources.
- Whether other bookmakers are pricing the draw similarly.
- Exact official settlement surface if organizer/governing-body stats are delayed or inconsistent.

## Disconfirming signals to watch

- Independent bookmaker draw odds implying roughly 70%+ draw probability.
- Official pre-match sources indicating special conditions or already-determined state.
- Clarification that the market is mapped differently than a standard draw proposition.

## What would increase confidence

- Clean independent bookmaker 1X2 pricing for this exact fixture.
- Official Saudi Pro League fixture page plus post-match stats endpoint.
- A second independent contextual source supporting draw parity without relying on the same odds aggregator class.

## Net update logic

The starting skepticism toward a 76% draw price held up. What mattered most was the gap between settlement clarity and probability justification. The contextual external source was enough to keep draw plausibility live, but not enough to close the confidence gap.

## Suggested downstream use

Use as orchestrator synthesis input and as a caution against overweighting the market’s confidence level without stronger independent corroboration.