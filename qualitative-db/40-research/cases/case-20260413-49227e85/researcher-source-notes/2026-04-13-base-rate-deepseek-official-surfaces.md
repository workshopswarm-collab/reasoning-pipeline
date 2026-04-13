---
type: source_note
case_key: case-20260413-49227e85
dispatch_id: dispatch-case-20260413-49227e85-20260413T180153Z
analysis_date: 2026-04-13
persona: base-rate
domain: technology
subdomain: ai-model-releases
entity:
topic: official DeepSeek release surfaces before Apr 15, 2026
question: Is there official evidence that the next DeepSeek V model has been publicly released by Apr 15, 2026?
driver: reliability
date_created: 2026-04-13
source_name: Polymarket market rules + DeepSeek official GitHub organization + DeepSeek Hugging Face org
source_type: official market rules plus official distribution surfaces
source_url: https://polymarket.com/event/deepseek-v4-released-by-march-31
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [deepseek, official-surfaces, release-verification]
---

# Summary

The market resolves from official DeepSeek information plus consensus credible reporting. As of Apr 13, 2026, the official public release surfaces checked here do not show a clearly announced public DeepSeek V4/V5 flagship successor available to the general public. The most relevant official-family evidence instead shows continued V3-line naming and artifacts.

## Key facts extracted

- The current market wording says Yes requires the next major DeepSeek V model to be publicly accessible by Apr 15, 2026 11:59 PM ET, not just rumored or privately available.
- The contract explicitly excludes intermediate or derivative labels and requires the release to be clearly positioned as the successor to DeepSeek-V3.
- DeepSeek's public GitHub org, when enumerated through the GitHub API, shows named repos including DeepSeek-V2, DeepSeek-V3, DeepSeek-R1, and related tooling, but no DeepSeek-V4 or DeepSeek-V5 repo as of Apr 13, 2026.
- DeepSeek-V3 GitHub metadata shows repo creation on 2024-12-26 and release archival tag v1.0.0 published 2025-06-27; this is evidence of prior official V-series release behavior and naming.
- DeepSeek's Hugging Face org page shows official models including DeepSeek-V3.2 and DeepSeek-V3.2-Exp in late 2025, which suggests the public official line remained on V3-series branding rather than a clean V4 successor.

## Evidence directly stated by source

- Polymarket rules directly state what counts and what does not count.
- GitHub API directly lists DeepSeek official repositories and release metadata.
- Hugging Face official org page directly lists published official model names under the DeepSeek org.

## What is uncertain

- DeepSeek could choose a release surface outside GitHub/Hugging Face and still satisfy the market if officially announced and publicly accessible before the deadline.
- The absence of a V4 artifact on these surfaces is negative evidence, not dispositive proof of non-release.
- I did not obtain a same-day official DeepSeek website/newsroom page confirming either launch or non-launch.

## Why this source may matter

These are the closest available official-family public surfaces for whether a qualifying model has actually been launched and made available. They also show DeepSeek's prior public naming pattern, useful for canonical mapping and contract interpretation.

## Possible impact on the question

This evidence pushes against an immediate Yes resolution because the official public artifact trail still appears centered on V3-line products rather than an officially public V4/V5 flagship release.

## Reliability notes

- Polymarket rule text is authoritative for contract interpretation but not for the underlying event.
- GitHub/Hugging Face surfaces are strong direct evidence for public availability when a model is actually released there, but not exhaustive of every possible release channel.
- Combining these surfaces is useful because they are independent enough operationally to reduce single-surface false negatives, though both still depend on DeepSeek choosing to publish there.