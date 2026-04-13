---
type: source_note
case_key: case-20260413-36f15d57
dispatch_id: dispatch-case-20260413-36f15d57-20260413T175211Z
analysis_date: 2026-04-13
persona: variant-view
domain: technology
subdomain: ai-model-releases
entity:
topic: deepseek-version-sequencing
question: What does public release history imply about whether the next major DeepSeek V model is already publicly available?
driver: product-launches
date_created: 2026-04-13
source_name: DeepSeek public model history surfaces (GitHub API, Hugging Face model page, Wikipedia context)
source_type: mixed primary + contextual
source_url: https://api.github.com/orgs/deepseek-ai/repos?per_page=100 ; https://api.github.com/repos/deepseek-ai/DeepSeek-V3/releases ; https://huggingface.co/deepseek-ai/DeepSeek-V3-0324 ; https://en.wikipedia.org/wiki/DeepSeek
source_date: 2026-04-13
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: [product-launches, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [deepseek, github, huggingface, model-history]
---

# Summary

Public release history visible on GitHub/Hugging Face shows DeepSeek continuing to ship V3-line updates rather than a V4-branded successor on the checked surfaces. Contextual reporting/wikipedia-style summaries also point to anticipation of a successor but not clear evidence that a qualifying V4 public launch has already occurred.

## Key facts extracted

- DeepSeek GitHub org repo listing showed DeepSeek-V2 and DeepSeek-V3 repositories, but no V4-named repository on the checked list.
- The DeepSeek-V3 GitHub releases endpoint showed a single archival release tag `v1.0.0` published 2025-06-27, reinforcing that the public repo lineage remained V3-labeled on the checked surface.
- The Hugging Face `deepseek-ai/DeepSeek-V3-0324` page describes a March 2025 V3 refresh and says the model structure is exactly the same as DeepSeek-V3.
- Wikipedia context (non-authoritative) summarizes March 2025 V3-0324 and notes an announced expectation in February 2026 that a latest model could arrive as soon as March 2026, but this is expectation/context rather than official proof of a qualifying public launch.

## Evidence directly stated by source

- GitHub org results included DeepSeek-V2, DeepSeek-V3, DeepSeek-VL, and DeepSeek-VL2; no V4 repo was found in the checked first-party org listing.
- Hugging Face page: "DeepSeek-V3-0324 demonstrates notable improvements over its predecessor, DeepSeek-V3" and references local running via the DeepSeek-V3 repo.

## What is uncertain

- DeepSeek could launch V4 without a GitHub repo, or announce it first on website/app/API/news channels.
- Wikipedia is only contextual and should not be treated as settlement-grade evidence.
- Absence of a public V4 repo/model page is not conclusive proof of no launch, only a negative indicator.

## Why this source may matter

The market hinges on a major-version public launch. Public repo/model naming history gives a check on whether the company has already crossed from V3-line iteration into an explicitly named next major V release.

## Possible impact on the question

These sources support a lower-than-market probability by suggesting the public evidence still points to continued V3-family rollout rather than a clearly announced and generally accessible V4 launch.

## Reliability notes

GitHub API and Hugging Face are strong for visible public artifacts, but weaker than an explicit official announcement for final settlement. Wikipedia is low-authority contextual support only.