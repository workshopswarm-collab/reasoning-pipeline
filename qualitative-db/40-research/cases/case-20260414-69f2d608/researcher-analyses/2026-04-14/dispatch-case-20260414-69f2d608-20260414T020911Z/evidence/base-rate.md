---
type: evidence_map
case_key: case-20260414-69f2d608
dispatch_id: dispatch-case-20260414-69f2d608-20260414T020911Z
research_run_id: 6fb146c7-1562-45f8-b175-6ee5c286b3b5
analysis_date: 2026-04-14
persona: base-rate
domain: geopolitics
subdomain: middle-east-conflict
entity:
topic: us-iran-ceasefire-extension
question: "Will the US x Iran ceasefire be extended by April 21, 2026?"
driver:
date_created: 2026-04-13
agent: orchestrator
status: draft
confidence: medium
conflict_status: limited-conflict
action_relevance: high
related_entities: ["iran", "united-states"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["ceasefire-negotiation-friction", "contract-resolution-source-ambiguity"]
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "ceasefire", "diplomacy", "base-rate"]
---

# Summary

The outside-view lean is below market. The strongest live evidence says the ceasefire still exists but the main direct negotiation channel already failed to produce an extension, while the contract requires a narrower and more formal outcome than mere continued de-escalation.

## Question being evaluated

Will there be a publicly announced and mutually agreed extension of the April 7, 2026 two-week U.S.-Iran ceasefire, or an equivalent new agreement taking effect with no gap, by the market deadline?

## Current lean

Lean No / below-market Yes probability.

## Prior / starting view

Starting outside-view prior: extensions of fragile wartime ceasefires between adversarial states are materially less common than short-lived continuation, partial compliance, or resumed bargaining without clean formal rollover.

## Evidence supporting the claim

- Existing ceasefire appears to still be holding as of April 13.
  - source: AP market-context note
  - why it matters causally: if the ceasefire had already collapsed, extension odds would be much lower
  - direct or indirect: indirect for extension, direct for continued pause
  - weight: medium

- Continued U.S.-Iran engagement remained possible after failed weekend talks.
  - source: AP market-context note
  - why it matters causally: open channels preserve some chance of a last-minute diplomatic rollover
  - direct or indirect: indirect
  - weight: low-to-medium

- Market price around 70.5% implies many participants expect some form of extension path.
  - source: assignment market price
  - why it matters causally: market embeds aggregated expectations and may reflect additional monitoring not visible in my limited source set
  - direct or indirect: indirect
  - weight: low as evidence, medium as caution against overconfidence

## Evidence against the claim

- AP reported that a 21-hour direct negotiation round ended without agreement on April 11.
  - source: AP ceasefire-talks note
  - why it matters causally: this was the clearest near-term mechanism for a formal extension and it failed
  - direct or indirect: direct on failed talks, indirect on final resolution
  - weight: high

- Contract wording is narrower than "ceasefire still holding" and requires official mutual confirmation or overwhelming media consensus of an official extension.
  - source: Polymarket market description
  - why it matters causally: many real-world de-escalation outcomes would still resolve No
  - direct or indirect: direct on settlement mechanics
  - weight: high

- Ongoing coercive escalation, including blockade and port threats, signals the conflict remains unstable and makes formal extension harder.
  - source: AP market-context note
  - why it matters causally: escalation pressure increases odds of breakdown or ambiguous continuation instead of clean extension announcement
  - direct or indirect: indirect
  - weight: medium

## Ambiguous or mixed evidence

- The ceasefire seems to be holding "for now." This raises odds relative to outright collapse, but it is not equivalent to a qualifying extension.
- Continued dialogue can be read either as progress toward extension or as evidence the sides remain far apart.

## Conflict between inputs

There is no sharp factual conflict in the sources reviewed. The main disagreement is interpretive: whether continued holding plus ongoing talks should dominate, or whether failed high-level talks and formal-confirmation friction should dominate.

## Key assumptions

- The market will be resolved according to the stated narrow wording rather than looser narrative impressions.
- No hidden agreement already exists awaiting announcement.
- Formal extension remains meaningfully harder than informal continued de-escalation.

## Key uncertainties

- Whether official U.S. and Iranian statements emerge in the next several days.
- Whether credible independent media achieve overwhelming consensus even if one side is slow to publish.
- Whether a broader deal is close enough to bundle a qualifying extension.

## Disconfirming signals to watch

- Parallel official statements from both governments confirming the ceasefire is extended beyond the original term.
- Two or more independent top-tier outlets reporting finalized extension terms.
- Public scheduling of a new direct negotiation round with announced extension text or framework.

## What would increase confidence

- A direct U.S. government statement specifically denying any extension agreement.
- A direct Iranian government statement rejecting extension on public terms.
- Additional independent reporting that the Islamabad failure reflected substantive gaps unlikely to close before the deadline.

## Net update logic

The prior was already cautious because formal extensions of active-war ceasefires are rare and friction-heavy. The evidence did not supply the kind of official or overwhelming independent confirmation needed to move above 50%. Instead, it showed a still-active but fragile ceasefire, failed direct talks, and a contract structure that can easily produce a No even if hostilities remain partially paused. That keeps the lean below market.

## Suggested downstream use

- orchestrator synthesis input
- forecast update
- source collection gap