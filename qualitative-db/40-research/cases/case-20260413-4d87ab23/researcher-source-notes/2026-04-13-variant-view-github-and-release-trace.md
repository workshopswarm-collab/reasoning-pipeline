---
type: source_note
case_key: case-20260413-4d87ab23
dispatch_id: dispatch-case-20260413-4d87ab23-20260413T174302Z
analysis_date: 2026-04-13
persona: variant-view
domain: tech-ai
subdomain: foundation-model-releases
entity:
topic: github-release-trace
question: Did DeepSeek publicly surface a new DeepSeek V-series successor consistent with V4 before deadline?
driver: product-launches
date_created: 2026-04-13
source_name: DeepSeek GitHub org and repo/API traces
source_type: primary_context
source_url: https://github.com/deepseek-ai ; https://api.github.com/orgs/deepseek-ai/repos?per_page=100
source_date: 2026-04-13
credibility: high
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
tags: [deepseek, github, release-trace, independent-check]
---

# Summary

DeepSeek's public GitHub organization on 2026-04-13 shows prominent/public V-series repos through DeepSeek-V3 and DeepSeek-V3.2-Exp, but no visible DeepSeek-V4 repository in the checked surfaces. This is not by itself decisive, but it is a meaningful independent-ish verification pass against the official website/docs.

## Key facts extracted

- GitHub org overview shows pinned/public repos including DeepSeek-V3 and DeepSeek-R1.
- API enumeration of org repos returned DeepSeek-V2, DeepSeek-VL2, DeepSeek-V3, DeepSeek-R1, and DeepSeek-V3.2-Exp among relevant names.
- No repository named DeepSeek-V4 appeared in the checked repo list.
- DeepSeek-V3 repo remained the main public V-series repo visible from the org, with V3.2-Exp also present later in the product line.

## Evidence directly stated by source

- Public repos on the org reflect actual public artifacts under DeepSeek's control.
- Relevant V-series repo names found: DeepSeek-V2, DeepSeek-V3, DeepSeek-V3.2-Exp.
- No DeepSeek-V4 repo surfaced in the queried organization repo list.

## What is uncertain

- A public release could in principle occur without a GitHub repo.
- Repo absence is weaker evidence than an explicit statement from DeepSeek.
- GitHub is contextual verification, not the governing source of truth for market resolution.

## Why this source may matter

It provides an additional verification pass outside the homepage/docs navigation path and helps show the negative evidence is not just an artifact of one web page.

## Possible impact on the question

This slightly strengthens the case that the market-implied Yes view may be overconfident if it assumes an already-public V4 launch. It does not eliminate the possibility of a non-GitHub release before deadline.

## Reliability notes

Strong for confirming publicly exposed artifacts under DeepSeek's organization; weaker for proving nonexistence of a release. Useful as corroborating rather than governing evidence.