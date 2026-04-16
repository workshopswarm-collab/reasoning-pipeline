---
type: evidence_map
case_key: case-20260415-7f8f0d04
dispatch_id: dispatch-case-20260415-7f8f0d04-20260415T104754Z
research_run_id: 5a037c6c-1fb7-40fb-9968-b73728e7b211
analysis_date: 2026-04-15
persona: base-rate
domain: tech-ai
subdomain: model-rankings
entity:
topic: chatbot-arena-style-control-on-leaderboard
question: "Will claude-opus-4-6-thinking be the top AI model on April 17, 2026 (Style Control On)?"
driver: reliability
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["anthropic", "claude"]
related_drivers: ["reliability", "operational-risk", "product-launches"]
proposed_entities: ["chatbot-arena"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-7f8f0d04/researcher-analyses/2026-04-15/dispatch-case-20260415-7f8f0d04-20260415T104754Z/personas/base-rate.md"]
tags: ["evidence-map", "leaderboard", "ai-models"]
---

# Summary

This evidence map nets a high-but-not-extreme probability that `claude-opus-4-6-thinking` is first at the specified Chatbot Arena style-control-on check time.

## Question being evaluated

Will `claude-opus-4-6-thinking` be the top model on the Chatbot Arena `Text Arena | Overall` leaderboard with style control on when checked on April 17, 2026 at 12:00 PM ET?

## Current lean

Lean yes, but below market confidence.

## Prior / starting view

Outside-view prior for any named model remaining #1 over a two-day horizon is favorable if it already leads, but not near certainty because frontier leaderboard tops are crowded and release-sensitive.

## Evidence supporting the claim

- Polymarket contract text names Chatbot Arena style-control-on leaderboard as the governing source and the market currently prices YES at 87.4%.
  - source: `2026-04-15-base-rate-polymarket-contract.md`
  - why it matters: shows trader consensus and exact mechanics
  - direct or indirect: direct for contract mechanics, indirect for truth of outcome
  - weight: medium
- Direct leaderboard fetch shows Anthropic occupying the top two extracted rows with scores 1502 and 1496, ahead of Meta at 1495 and Google at 1493.
  - source: `2026-04-15-base-rate-lmarena-leaderboard.md`
  - why it matters: current leaderboard leadership is the strongest predictor over a short horizon
  - direct or indirect: direct
  - weight: high
- No concrete near-term catalyst was identified in this run that clearly implies an imminent dethroning before the check time.
  - source: synthesis from current source set
  - why it matters: absent a scheduled shock, incumbency on a short-horizon leaderboard matters
  - direct or indirect: indirect/contextual
  - weight: medium

## Evidence against the claim

- The leaderboard extraction did not preserve clean model names, so exact-model verification remains imperfect.
  - source: `2026-04-15-base-rate-lmarena-leaderboard.md`
  - why it matters: the contract resolves on exact model string, not just lab family
  - direct or indirect: direct limitation
  - weight: high
- The top-score gap appears modest, with the top four entries within about 9 points.
  - source: `2026-04-15-base-rate-lmarena-leaderboard.md`
  - why it matters: small gaps can flip on updates or additional votes
  - direct or indirect: direct
  - weight: medium-high
- Contract tie mechanics are unfavorable to the named model versus `claude-opus-4-6` if those two tie in score.
  - source: `2026-04-15-base-rate-polymarket-contract.md`
  - why it matters: even if Anthropic remains effectively tied at the top, the named option can still lose
  - direct or indirect: direct
  - weight: medium

## Ambiguous or mixed evidence

- Extreme market confidence can reflect genuine current lead, but it can also overcompress uncertainty in fast-moving leaderboard environments.
- Anthropic occupying the top two slots is supportive for the firm/family but not conclusive for the exact named contract.

## Conflict between inputs

No hard factual conflict. The main tension is between strong family-level current positioning and weaker exact-model-string verification.

## Key assumptions

- The current top Anthropic row corresponds to the named contract or a very close adjacent Anthropic variant.
- No major release or leaderboard-method shock occurs before the check time.

## Key uncertainties

- Exact current placement of `claude-opus-4-6-thinking` by name.
- Whether style-control-on ordering differs from the extracted visible ordering in ways not captured cleanly by the fetch.

## Disconfirming signals to watch

- Clean leaderboard check showing another model currently first.
- Evidence of a new major release from a rival lab before April 17 noon ET.
- Reported leaderboard update materially narrowing or reversing Anthropic’s lead.

## What would increase confidence

- A clean manual or API-level capture of the exact current top model name under style control on.
- Independent third-party screenshot or reporting that confirms `claude-opus-4-6-thinking` specifically is first.

## Net update logic

The outside-view starts from “current leader over a two-day horizon is favored, but not invulnerable.” Current evidence supports Anthropic leadership and therefore a high probability on the named contract, but exact-model identification and tie mechanics prevent endorsing the market’s 87.4% at face value.

## Suggested downstream use

- orchestrator synthesis input
- decision-maker review
- source collection gap