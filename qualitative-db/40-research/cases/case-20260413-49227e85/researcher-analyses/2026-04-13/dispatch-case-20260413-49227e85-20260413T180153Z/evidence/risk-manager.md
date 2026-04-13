---
type: evidence_map
case_key: case-20260413-49227e85
dispatch_id: dispatch-case-20260413-49227e85-20260413T180153Z
research_run_id: fe620ff5-0f3f-4111-a396-f7d111a57171
analysis_date: 2026-04-13
persona: risk-manager
domain: tech-ai
subdomain: ai-model-releases
entity:
topic: deepseek-v4-release-status
question: "DeepSeek V4 released by April 15?"
driver: operational-risk
date_created: 2026-04-13
agent: risk-manager
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: []
related_drivers: ["operational-risk", "reliability", "product-launches"]
proposed_entities: ["DeepSeek"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["auditability", "timing-risk", "resolution-sensitive"]
---

# Summary

The evidence nets to a NO-lean because recent first-party-visible public surfaces still show V3.2, while independent reporting describes V4 as anticipated but not yet publicly launched. The main risk to this view is a very late official public release before the cutoff.

## Question being evaluated

Will the next major DeepSeek V model be made available to the general public by the contract deadline, in a way that satisfies the market's public-access and announcement requirements?

## Current lean

Lean NO.

## Prior / starting view

Starting point was that the market price of 0.755 implied strong confidence in a near-term public release.

## Evidence supporting the claim

- Reuters-visible reporting discussed DeepSeek V4 as the new model and described it in future-oriented terms (contextual, medium weight).
- Industry expectation and repeated rumors suggest a release is plausible in the near term (indirect, low-to-medium weight).
- The contract allows open beta or open rolling waitlist access, so the bar is lower than a full broad rollout (contractual, medium weight).

## Evidence against the claim

- Official DeepSeek API docs still identify public model access as DeepSeek-V3.2, with no V4 public endpoint or launch notice visible (direct / primary, high weight).
- AFP/Taipei Times on 2026-04-12 says that despite rumors of imminent release, V4 is "nowhere in sight" (contextual but recent and independent, high weight).
- Reuters-visible reporting also shows rumor contamination: one suspected V4 model was reportedly actually Xiaomi's, reducing confidence in leak-driven claims (contextual, medium weight).

## Ambiguous or mixed evidence

- Reporting around Huawei chips and training/inference stack says V4 may be close, but that same reporting also implies operational friction and re-engineering burden.
- The contract text in the assignment includes a March 31 wording, while the market title says April 15. This run treats the active market question and listed closes/resolves_at timing as the operative assignment context, but notes source-of-truth ambiguity.

## Conflict between inputs

There is little direct factual conflict. The main disagreement is between high market confidence / rumor-driven expectation and the absence of clear first-party public-release evidence.

## Key assumptions

- A qualifying public release would likely already leave a visible first-party artifact.
- No hidden public waitlist or open beta satisfying the contract exists yet.
- Rumor-based sightings without DeepSeek confirmation should be downweighted heavily.

## Key uncertainties

- Whether DeepSeek could still do a last-minute official public release before the deadline.
- Whether any public web/app release surface exists outside the API docs and escaped discovery in this run.
- Whether the final resolver will apply the April 15 framing or the March 31 wording embedded in the copied market description.

## Disconfirming signals to watch

- First-party DeepSeek announcement naming V4 or the next major V successor.
- Public signup or open waitlist available to any user before cutoff.
- Independent reporting with direct screenshots or links showing broad public accessibility.

## What would increase confidence

- A direct check of DeepSeek's official announcement/blog/social channels showing no release.
- Consensus reporting from multiple major outlets that V4 remains unreleased as deadline approaches.
- Resolver clarification on the exact operative deadline and wording.

## Net update logic

The market's high price appears to embed substantial confidence that an anticipated release will happen on time. The risk-manager update is that public-release evidence is still missing close to deadline, and the available independent reporting emphasizes waiting, friction, and rumor contamination rather than confirmed launch. That shifts the view below market mainly on timing and contract-compliance risk, not because V4 seems impossible in principle.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review
- source collection gap