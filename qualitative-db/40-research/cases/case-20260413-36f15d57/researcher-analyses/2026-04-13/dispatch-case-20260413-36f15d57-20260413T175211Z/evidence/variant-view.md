---
type: evidence_map
case_key: case-20260413-36f15d57
dispatch_id: dispatch-case-20260413-36f15d57-20260413T175211Z
research_run_id: 5208ab3c-9391-46f8-b31a-39b3ba810637
analysis_date: 2026-04-13
persona: variant-view
domain: technology
subdomain: ai-model-releases
entity:
topic: deepseek-next-v-model
question: "Will the next DeepSeek V model be made available to the general public by the contract deadline?"
driver: product-launches
date_created: 2026-04-13
agent: Orchestrator
status: draft
confidence: medium
conflict_status: medium
action_relevance: high
related_entities: []
related_drivers: ["product-launches", "operational-risk", "reliability"]
proposed_entities: ["deepseek"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["deepseek", "evidence-map", "release-risk"]
---

# Summary

The current lean is No / below-market because official public surfaces still center V3.2 and there is no checked first-party evidence of a contract-compliant V4 public release yet, while the market appears to be pricing expectation of imminence.

## Question being evaluated

Will the next DeepSeek V model be made available to the general public by the contract deadline under the market's specific wording?

## Current lean

Lean No relative to market pricing; public-release proof is weaker than the market level implies.

## Prior / starting view

Starting view: market at 70% suggests consensus expects an imminent DeepSeek successor launch.

## Evidence supporting the claim

- Contextual expectation that DeepSeek planned a newer model in spring 2026, reflected in secondary/contextual reporting summarized on Wikipedia. Weight: low-to-medium because not settlement-grade and partly derivative.
- DeepSeek has a prior pattern of public model iteration and open public model surfaces. Weight: medium as a general capability/tendency signal, not direct proof.

## Evidence against the claim

- Official homepage checked on 2026-04-13 prominently advertises DeepSeek-V3.2 across web/app/API surfaces, with no visible V4 labeling. Direct first-party negative indicator. Weight: high.
- Official API docs front page states `deepseek-chat` and `deepseek-reasoner` correspond to DeepSeek-V3.2; news list shows no V4 item on checked surface. Direct first-party negative indicator. Weight: high.
- DeepSeek public GitHub org listing and checked public model pages showed V2/V3-family artifacts but no V4 artifact on checked surfaces. Indirect but useful public-artifact check. Weight: medium.

## Ambiguous or mixed evidence

- DeepSeek could still announce and open a qualifying public release before the deadline with little advance warning.
- Lack of public V4 breadcrumbs is a negative indicator, not a definitive negative.

## Conflict between inputs

- Disagreement is mainly weighting-based and timing-based.
- Bull case: DeepSeek has incentive and history to ship quickly; expectation of a successor may be right.
- Bear/variant case: the contract requires a clearly defined public release, and that proof is absent on checked official surfaces despite the market pricing a high chance.
- Resolving evidence: a first-party DeepSeek announcement or public access surface explicitly naming the next major V model.

## Key assumptions

- A qualifying public launch would likely leave visible first-party traces by now.
- The next qualifying major V successor would be clearly named or positioned as successor to V3, not just another V3.x refresh.

## Key uncertainties

- Whether DeepSeek is holding a launch for very near term.
- Whether a non-website official channel could announce qualifying public access before the deadline.

## Disconfirming signals to watch

- Official announcement of DeepSeek V4 or another next-major V successor.
- Open public beta, open waitlist, or broad public API/app access labeled as the next major V model.

## What would increase confidence

- More direct secondary reporting independently confirming no public V4 release yet.
- Additional first-party surfaces checked with no V4 evidence.

## Net update logic

The market seems to price an imminent release based on expectation. The official surfaces checked here still show V3.2 as the public flagship. Because the contract is strict on naming and public accessibility, I downweight rumor/anticipation and overweight absence of first-party public-release evidence.

## Suggested downstream use

Use as orchestrator synthesis input and as a resolution-audit reminder: do not count mere successor rumors, private rollout, or unlabeled V3.x iteration as contract-compliant.