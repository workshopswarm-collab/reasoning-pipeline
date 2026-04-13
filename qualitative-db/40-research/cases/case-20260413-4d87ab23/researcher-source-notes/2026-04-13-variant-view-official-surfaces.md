---
type: source_note
case_key: case-20260413-4d87ab23
dispatch_id: dispatch-case-20260413-4d87ab23-20260413T174302Z
analysis_date: 2026-04-13
persona: variant-view
domain: tech-ai
subdomain: foundation-model-releases
entity:
topic: official-release-surfaces
question: Did DeepSeek publicly release the next DeepSeek V model by the market deadline?
driver: product-launches
date_created: 2026-04-13
source_name: DeepSeek official website and API docs news index
source_type: primary
source_url: https://www.deepseek.com/ ; https://api-docs.deepseek.com/
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: [product-launches, reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [deepseek, official-source, release-audit, contract-interpretation]
---

# Summary

DeepSeek's own public surfaces as of 2026-04-13 still present the flagship/publicly accessible family as DeepSeek-V3.2, not V4. The API docs news menu shows a sequence of V-series releases through V3.2 and no V4 item. The homepage banner explicitly advertises "DeepSeek-V3.2 正式版发布" and says it is live on web, app, and API.

## Key facts extracted

- DeepSeek homepage banner says: "DeepSeek-V3.2 正式版发布... 在网页端、APP 和 API 全面上线".
- The homepage research/product links still enumerate DeepSeek V3, V2, R1, etc., with no visible DeepSeek V4 link.
- The API docs homepage identifies `deepseek-chat` and `deepseek-reasoner` as corresponding to model version DeepSeek-V3.2.
- The API docs news section lists V-series items including DeepSeek-V3, DeepSeek-V3-0324, DeepSeek-V3.1, DeepSeek-V3.1-Terminus, DeepSeek-V3.2-Exp, and DeepSeek-V3.2 Release; no V4 item appears in the visible index.

## Evidence directly stated by source

- Official homepage banner: DeepSeek-V3.2 formally released and live across public surfaces.
- Official API docs: current public API model aliases map to DeepSeek-V3.2.
- Official news chronology: public release naming progresses through V3.2; no official V4 release item is visible on the public docs index checked on 2026-04-13.

## What is uncertain

- This source set does not prove a V4 announcement could not appear before the market deadline.
- The market text provided in the assignment says "by May 15," but the embedded market description says resolves Yes only if public by March 31, 2026 at 11:59 PM ET, creating a material source-of-truth ambiguity that must be handled in the main finding.
- Public docs/index visibility is strong negative evidence but not absolute proof against a same-day or later release.

## Why this source may matter

These are the governing official surfaces most likely to satisfy the contract's primary source requirement. If V4 had been publicly released and made generally accessible, DeepSeek's own site or API docs would be the most natural place to verify it.

## Possible impact on the question

This materially lowers the chance that the contract should resolve Yes based on currently visible official evidence. It also shifts the main remaining risk from product-launch evidence to contract interpretation: whether some future or non-obvious announcement could count, and what deadline actually governs.

## Reliability notes

Primary-source quality is high for release existence and public accessibility. Evidence independence is low because the homepage and docs are both official DeepSeek surfaces, but that is acceptable for source-of-truth auditing. Absence evidence is weaker than explicit denial, so this should be combined with at least one additional verification surface.