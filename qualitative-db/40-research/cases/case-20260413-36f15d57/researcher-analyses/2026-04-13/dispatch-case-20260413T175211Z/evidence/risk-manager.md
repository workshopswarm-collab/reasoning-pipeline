---
type: evidence_map
case_key: case-20260413-36f15d57
dispatch_id: dispatch-case-20260413-36f15d57-20260413T175211Z
research_run_id: d2545831-fee8-4734-a0b3-f30e7a461598
analysis_date: 2026-04-13
persona: risk-manager
domain: ai
subdomain: model-releases
entity:
topic: DeepSeek next major V-series release public availability
question: Will the next DeepSeek V model be publicly accessible by the contract deadline?
driver:
date_created: 2026-04-13
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: []
related_drivers: [reliability, operational-risk]
proposed_entities: [DeepSeek]
proposed_drivers: [public-access-qualification-risk]
upstream_inputs: []
downstream_uses: []
tags: [evidence-map, deepseek, release-risk]
---

# Summary

The evidence nets to a No lean because the contract requires a very specific kind of launch and the checked primary surfaces do not show one.

## Question being evaluated

Will the next major DeepSeek V-series model be made publicly accessible in a contract-qualifying way by the deadline?

## Current lean

Lean No.

## Prior / starting view

Starting baseline was the market-implied 70% Yes from current price 0.7.

## Evidence supporting the claim

- The contract allows open beta or open rolling waitlist signups rather than requiring full open weights release. This means the bar for Yes is not impossibly high. Weight: medium.
- DeepSeek has previously shipped major V-series models publicly, so a future successor launch is plausible in principle. Weight: low-to-medium contextual only.

## Evidence against the claim

- No official V4 or V5 repo found under DeepSeek GitHub org search. Direct official-surface negative evidence. Weight: medium-high.
- Hugging Face org page still foregrounds V3.2-era models rather than any V4/V5 flagship. Direct official-surface negative evidence. Weight: medium.
- Contract excludes previews, derivative variants, and private access, meaning many rumor-like or limited-access scenarios would still resolve No. Contractual negative filter. Weight: high.
- No qualifying official announcement surfaced in this run despite explicit verification pass across primary surfaces. Weight: medium-high.

## Ambiguous or mixed evidence

- DeepSeek website extraction was sparse, so website silence alone is weak.
- GitHub/Hugging Face are helpful but not guaranteed source-of-truth for access mechanisms like open waitlists.
- Assignment metadata and fetched market page used inconsistent date language, which raises operational ambiguity but does not create positive evidence for Yes.

## Conflict between inputs

There is little factual conflict in gathered sources; the main conflict is between a 70% market price and currently sparse qualifying evidence.

## Key assumptions

- A qualifying public flagship launch would leave visible evidence on official surfaces and/or broad credible reporting.
- No hidden official access page presently exists that meets the contract while evading checked sources.

## Key uncertainties

- Whether DeepSeek could use a minimally public but contract-qualifying open waitlist page not visible in the checked surfaces.
- Whether credible reporting exists behind search limitations not reached in this run.
- Which exact deadline text is currently operative on the live market surface.

## Disconfirming signals to watch

- Official DeepSeek statement naming V4 or V5 as successor to V3 and open to the general public.
- Official signup page for open beta or rolling public waitlist.
- Consensus reporting from multiple credible outlets pointing to such official access.

## What would increase confidence

- Successful retrieval of major independent reporting confirming absence of launch, or confirming launch.
- Direct capture of DeepSeek announcement/blog/API docs showing whether V4/V5 access exists.
- Live market screenshot or archived rules confirming exact deadline and wording.

## Net update logic

The market starts from a fairly confident Yes. The contract's strict qualification rules plus lack of visible official release evidence push the estimate down because the bullish case appears to assume not just imminent model progress but also a clearly documented public-access rollout that meets all conditions.

## Suggested downstream use

Use as an orchestrator synthesis input and resolution-audit reminder; especially confirm deadline wording and whether any official waitlist/access page exists before final decision.