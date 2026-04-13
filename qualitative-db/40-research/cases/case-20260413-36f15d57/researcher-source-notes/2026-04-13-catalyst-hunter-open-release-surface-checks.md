---
type: source_note
case_key: case-20260413-36f15d57
dispatch_id: dispatch-case-20260413-36f15d57-20260413T175211Z
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: tech-ai
subdomain: ai-model-releases
entity:
topic: Public release-surface checks across DeepSeek channels
question: Is there visible public evidence of a qualifying DeepSeek V4 or successor flagship release?
driver: product-launches
date_created: 2026-04-13
source_name: GitHub, Hugging Face, and public DeepSeek release surfaces
source_type: platform-check
source_url: https://github.com/deepseek-ai ; https://huggingface.co/deepseek-ai ; https://api.github.com/search/repositories?q=DeepSeek-V4+in:name+user:deepseek-ai ; https://api.github.com/search/repositories?q=V4+user:deepseek-ai ; https://huggingface.co/api/models?author=deepseek-ai&limit=100&full=false
source_date: 2026-04-13
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: []
related_drivers: [product-launches, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-36f15d57/researcher-analyses/2026-04-13/dispatch-case-20260413-36f15d57-20260413T175211Z/personas/catalyst-hunter.md]
tags: [verification, release-surface, github, huggingface]
---

# Summary

I checked major public release surfaces associated with DeepSeek. As of April 13, these checks did not show a publicly accessible flagship successor labeled V4 or otherwise clearly positioned as the next major V-series release.

## Key facts extracted

- GitHub repository search for DeepSeek-V4 under the deepseek-ai org returned zero results.
- GitHub repository search for V4 under the deepseek-ai org also returned zero relevant results.
- Hugging Face public organization page prominently showed DeepSeek-V3.2 family models, not a V4 flagship.
- Hugging Face API results included public DeepSeek-R1 and DeepSeek-V3.2 entries but no visible public V4 flagship in the returned set.
- GitHub search did show a DeepSeek-V3.2-Exp repo, reinforcing that DeepSeek has used public release surfaces for late-V3 family iterations, making the absence of a visible V4 surface somewhat informative.

## Evidence directly stated by source

The platform responses directly show what public repos/models are visible at check time.

## What is uncertain

- DeepSeek could release first on its own site/app without simultaneous GitHub or Hugging Face publication.
- API pagination or naming differences could hide a non-obvious successor if it uses unexpected branding.
- Absence on these surfaces is not proof of No by the deadline; it is only negative evidence at the time checked.

## Why this source may matter

For a market requiring a public, clearly defined, generally accessible flagship release, major public distribution surfaces are relevant verification points. Their silence this close to deadline is meaningful negative evidence.

## Possible impact on the question

This check pushes against an immediate-Yes thesis and supports the view that the strongest live catalyst is still a future official DeepSeek announcement rather than something already publicly shipped.

## Reliability notes

Moderate-high for what is publicly visible at the time of checking. Lower as proof of nonexistence, because DeepSeek might use private or first-party channels before mirroring elsewhere.