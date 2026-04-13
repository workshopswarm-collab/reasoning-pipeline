---
type: source_note
case_key: case-20260413-4d87ab23
dispatch_id: dispatch-case-20260413-4d87ab23-20260413T174302Z
analysis_date: 2026-04-13
persona: risk-manager
domain: tech-ai
subdomain: model-releases
entity:
topic: deepseek-v4-release-status
question: Has DeepSeek publicly released the next DeepSeek V model by the market deadline?
driver: reliability
date_created: 2026-04-13
source_name: DeepSeek official web surfaces + official GitHub org inventory
source_type: primary
source_url: https://www.deepseek.com/
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
tags: [deepseek, official-source, release-audit]
---

# Summary

Primary-source audit of DeepSeek's official website access plus the public `deepseek-ai` GitHub organization. This does not directly prove non-release across all official channels, but it is strong evidence that no clear, general-public V4 flagship release is presently visible on major official surfaces.

## Key facts extracted

- `https://www.deepseek.com/` returned only the company landing/copyright/legal footer content in this fetch path, with no visible public announcement of a DeepSeek V4 flagship release.
- `https://chat.deepseek.com` returned HTTP 403 in direct unauthenticated fetch, so it could not be used to confirm a publicly accessible general-release state from this environment.
- `https://api.deepseek.com` returned HTTP 401, indicating access control rather than an obviously open public launch surface.
- Official GitHub org inventory shows public repos including `DeepSeek-V2`, `DeepSeek-V3`, and `DeepSeek-V3.2-Exp`, but no public `DeepSeek-V4` or `DeepSeek-V5` repo surfaced in the org listing at audit time.
- Presence of `DeepSeek-V3.2-Exp` is notable because the market rules explicitly exclude preview/experimental releases that are not the new V flagship model.

## Evidence directly stated by source

- DeepSeek official site fetch exposed no V4 public-release announcement in retrieved content.
- GitHub org inventory explicitly lists current public repos and names; the listing includes `DeepSeek-V3.2-Exp` and lacks `DeepSeek-V4`.

## What is uncertain

- DeepSeek could publicly announce/access-enable a qualifying model through an authenticated chat or app surface that is not fully inspectable from this environment.
- GitHub is not the governing source of truth for this market; a qualifying release could occur without an open repo.
- Absence of evidence on these surfaces is not absolute proof of non-release, only meaningful negative evidence.

## Why this source may matter

The contract names official information from DeepSeek as the primary resolution source. Official web surfaces and the official GitHub org are therefore high-priority audit targets for a release-status check.

## Possible impact on the question

As of 2026-04-13, the official-surface audit leans against a view that a qualifying public DeepSeek V4 release has already happened. It also strengthens the risk-manager case that the market may be overconfident if it is pricing near-certain release without a clear official public-access artifact.

## Reliability notes

- Strong for checking visible official naming and public availability signals.
- Incomplete for gated product surfaces because unauthenticated access can hide rollout status.
- Best used together with independent reporting on timing and expectations, not as a sole settlement source.