---
type: source_note
case_key: case-20260413-4d87ab23
dispatch_id: dispatch-case-20260413-4d87ab23-20260413T174302Z
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: technology
subdomain: ai-model-releases
entity:
topic: deepseek-public-model-distribution
question: Will the next DeepSeek V model be made available to the general public by April 15, 2026, 11:59 PM ET under the market rules?
driver: product-launches
date_created: 2026-04-13
source_name: Hugging Face DeepSeek organization page and model API
source_type: secondary but near-direct distribution evidence
source_url: https://huggingface.co/deepseek-ai ; https://huggingface.co/api/models?author=deepseek-ai&limit=100
source_date: 2026-04-13
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: [product-launches]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-4d87ab23/researcher-analyses/2026-04-13/dispatch-case-20260413-4d87ab23-20260413T174302Z/personas/catalyst-hunter.md]
tags: [deepseek, huggingface, public-availability, release-timing]
---

# Summary

Hugging Face is not the governing source of truth, but it is a strong public-distribution cross-check for whether DeepSeek has made a new V-series model broadly accessible. As of 2026-04-13, the visible DeepSeek models include DeepSeek-V3, DeepSeek-V3-0324, DeepSeek-R1, and later 2025 artifacts such as DeepSeek-V3.2; there is no visible DeepSeek-V4 entry in the checked output.

## Key facts extracted

- The organization page shows DeepSeek-V3.2 collection items later in 2025, which implies that even after April 2026 the lineage apparently continued through V3.x naming rather than an observed V4 jump in the checked surfaces.
- The model API output includes DeepSeek-V3, DeepSeek-V3-0324, and many R1 / OCR / other-model entries, but no DeepSeek-V4 entry in the returned sample.
- DeepSeek-V3 was created on Hugging Face on 2024-12-25 and DeepSeek-V3-0324 on 2025-03-24, reinforcing that public releases have so far stayed inside the V3 naming family in the checked evidence.

## Evidence directly stated by source

- API entries explicitly name `deepseek-ai/DeepSeek-V3` and `deepseek-ai/DeepSeek-V3-0324`.
- No `DeepSeek-V4` model appears in the checked API output.
- The organization page exposes later V3.2 artifacts rather than a V4 artifact in the visible collection output.

## What is uncertain

- DeepSeek could make a qualifying general-public release without using Hugging Face.
- Hugging Face API output may not include every possible artifact in the first returned page.
- Some visible items reference dates later than the current decision window; they are useful mainly as lineage/context rather than contemporaneous proof.

## Why this source may matter

The contract requires a release that is publicly accessible to the general public. Public model-hosting surfaces are a meaningful independent check on whether such accessibility exists or is imminent.

## Possible impact on the question

This source lowers the probability of a near-term yes because it shows no visible V4 public-distribution artifact and suggests continuation of the V3 naming line rather than an imminent major-version handoff.

## Reliability notes

This is not the official settlement source, but it is a practical cross-check with moderate-to-high relevance for public accessibility. It is meaningfully independent from the market page and partially independent from DeepSeek's own announcement language.