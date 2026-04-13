---
type: evidence_map
case_key: case-20260413-36f15d57
dispatch_id: dispatch-case-20260413-36f15d57-20260413T175211Z
research_run_id: 78a9d31d-0584-4646-9418-91e8d2d972ee
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: tech-ai
subdomain: ai-model-releases
entity:
topic: "DeepSeek V4 release timing and qualification audit"
question: "DeepSeek V4 released by April 30?"
driver: product-launches
date_created: 2026-04-13
agent: catalyst-hunter
status: draft
confidence: medium
conflict_status: moderate
action_relevance: high
related_entities: []
related_drivers: ["product-launches", "reliability", "operational-risk"]
proposed_entities: ["DeepSeek"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-36f15d57/researcher-analyses/2026-04-13/dispatch-case-20260413-36f15d57-20260413T175211Z/personas/catalyst-hunter.md"]
tags: ["evidence-netting", "timing", "resolution-audit"]
---

# Summary

Evidence points to a real near-term launch narrative around DeepSeek V4, but not to a completed qualifying public release yet. The most important distinction is between anticipation/preparation and an officially announced flagship successor that the general public can actually access.

## Question being evaluated

Will the next major DeepSeek V-series model be made publicly accessible in a qualifying way by the deadline under the market contract?

## Current lean

Lean No versus the market, though not remotely settled.

## Prior / starting view

Starting view: market at 70% implies investors believe a near-term official flagship release is more likely than not.

## Evidence supporting the claim

- SCMP reported that DeepSeek added instant/expert modes and framed them as arriving ahead of an anticipated V4 release this month.
  - Source: `2026-04-13-catalyst-hunter-scmp-ui-modes-ahead-of-v4.md`
  - Why it matters: suggests live launch preparation and public-facing product changes.
  - Direct/indirect: indirect for qualifying release.
  - Weight: medium.
- Google-search surfaced Reuters/The Information style reporting that DeepSeek V4 is expected in late April and tied to Huawei chips.
  - Why it matters: indicates broader market narrative and a plausible upcoming catalyst window.
  - Direct/indirect: indirect and partly second-hand.
  - Weight: low-medium.

## Evidence against the claim

- The contract is exclusion-heavy: previews, derivative variants, and private access do not count; the release must be clearly defined and publicly accessible.
  - Source: `2026-04-13-catalyst-hunter-polymarket-contract-and-resolution.md`
  - Why it matters causally: narrows the set of qualifying events materially.
  - Direct/indirect: direct.
  - Weight: high.
- Public release-surface checks on GitHub and Hugging Face did not show a visible V4 or successor flagship public release as of April 13.
  - Source: `2026-04-13-catalyst-hunter-open-release-surface-checks.md`
  - Why it matters causally: if launch were already effectively public, stronger traces would often exist.
  - Direct/indirect: direct for current absence on checked surfaces; indirect for final market outcome.
  - Weight: medium-high.
- SCMP itself described anticipation and interface changes, not actual qualifying flagship release/access.
  - Source: `2026-04-13-catalyst-hunter-scmp-ui-modes-ahead-of-v4.md`
  - Why it matters causally: strongest live catalyst evidence still stops short of contract satisfaction.
  - Direct/indirect: direct.
  - Weight: medium-high.

## Ambiguous or mixed evidence

- Rumors of a late-April launch cut both ways: they support eventual release potential, but also suggest the timeline may slip beyond the actual operative deadline if the contract text fetch is correct about April 15 rather than the assignment header's April 30.
- DeepSeek may launch first on its own app/site, so GitHub/Hugging Face silence is meaningful but not dispositive.

## Conflict between inputs

- There is a factual/process conflict between assignment metadata (April 30 title) and the fetched Polymarket contract text (April 15 deadline on the live page fetched here).
- There is also a timing conflict between public anticipation of V4 "this month" and the absence of a currently qualifying public release surface.
- Evidence needed to resolve: direct official DeepSeek announcement and confirmed public-access mechanism.

## Key assumptions

- A qualifying release would likely generate clearer official/public artifacts than are currently visible.
- The fetched market contract text is the governing deadline reference unless a newer official market page says otherwise.

## Key uncertainties

- Whether the operative deadline is actually April 15 or April 30.
- Whether DeepSeek may launch suddenly on first-party surfaces without advance GitHub/Hugging Face artifacts.
- Whether consensus reporting would treat a chatbot-mode rollout as the flagship successor release.

## Disconfirming signals to watch

- Official DeepSeek announcement explicitly naming V4 or successor flagship.
- Open public waitlist or public-access page tied to the flagship successor.
- Credible independent reporting converging on public availability rather than rumor/specs.

## What would increase confidence

- Direct official DeepSeek statement on release and access.
- Confirmed public model page or access flow from DeepSeek.
- Additional independent reporting verifying general-public availability.

## Net update logic

The strongest positive evidence is timing/narrative evidence, not settlement-grade evidence. The strongest negative evidence is the contract's narrow wording plus the lack of visible qualifying public release artifacts. That combination pulls the estimate below the market even while preserving a meaningful chance of a last-minute repricing catalyst.

## Suggested downstream use

Use as orchestrator synthesis input and for forecast update, with emphasis on deadline/source-of-truth ambiguity and on the difference between launch rumors and contract-qualifying public release.