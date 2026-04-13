---
type: source_note
case_key: case-20260413-4d87ab23
dispatch_id: dispatch-case-20260413-4d87ab23-20260413T174302Z
analysis_date: 2026-04-13
persona: base-rate
domain: technology
subdomain: ai-model-releases
entity:
topic: DeepSeek next V-series release status
question: Has DeepSeek publicly released the next major V-series model after DeepSeek-V3 by the deadline?
driver: product-launches
date_created: 2026-04-13
source_name: DeepSeek official surfaces (website, GitHub repo, Hugging Face model card, platform)
source_type: official primary sources
source_url: https://www.deepseek.com/
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: []
related_drivers: [product-launches, reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [deepseek, official-source, release-status]
---

# Summary

As of 2026-04-13, the official DeepSeek surfaces I could verify still prominently expose DeepSeek-V3 rather than a clearly announced and generally accessible successor in the V-series. That does not strictly prove non-release, but it is meaningful negative evidence against an already-completed qualifying V4/V5 public launch.

## Key facts extracted

- DeepSeek official website fetch returned only sparse corporate footer content and did not expose a public V4/V5 announcement in readable extraction.
- DeepSeek's official GitHub repository `deepseek-ai/DeepSeek-V3` still presents DeepSeek-V3 as the flagship V-series model and links users to `chat.deepseek.com` and `platform.deepseek.com` for access.
- The Hugging Face model card for `deepseek-ai/DeepSeek-V3` likewise presents DeepSeek-V3 as the offered flagship V-series model and directs users to official DeepSeek chat and API surfaces.
- GitHub API data for the DeepSeek-V3 repository shows continued repo activity through 2025-08-28, indicating maintenance of V3 artifacts rather than an obvious superseding V4 release trail in that public repo.
- GitHub releases API for `deepseek-ai/DeepSeek-V3` showed an archival `v1.0.0` release published 2025-06-27, again tied to V3 rather than a new V-series successor.

## Evidence directly stated by source

- The GitHub README says: "We present DeepSeek-V3" and provides official chat/API access points for DeepSeek-V3.
- The Hugging Face model card says users can chat with DeepSeek-V3 on DeepSeek's official website and use the OpenAI-compatible API at DeepSeek Platform.
- No readable official source fetched in this pass explicitly announced "DeepSeek-V4" or another next major V-series successor as generally available.

## What is uncertain

- The official website fetch was extraction-poor, so absence of a visible V4 announcement there is not conclusive by itself.
- DeepSeek could theoretically announce a successor on another official channel or page that was not captured by these fetches.
- The market depends on contract interpretation around what counts as the "next DeepSeek V model" and whether open waitlist access qualifies.

## Why this source may matter

The contract names official DeepSeek information as the primary resolution source. For a Yes resolution, there should normally be a clear official public-access signal. Continued official emphasis on V3 close to the deadline is meaningful evidence that the next qualifying V release has not yet been publicly launched.

## Possible impact on the question

This source cluster pushes toward No by showing that the official surfaces still center on V3 and do not obviously present a publicly accessible successor. It is especially relevant because the market is already pricing a very high chance of release, so negative official evidence deserves weight.

## Reliability notes

These are primary sources, but the website/platform extraction quality was incomplete. Reliability is high for what was directly observed, but the inference from non-observation should be treated as moderate-weight rather than dispositive.