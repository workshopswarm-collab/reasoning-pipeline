---
type: source_note
case_key: case-20260413-36f15d57
dispatch_id: dispatch-case-20260413-36f15d57-20260413T175211Z
analysis_date: 2026-04-13
persona: base-rate
domain: technology
subdomain: ai-model-releases
entity:
topic: DeepSeek official/public release surfaces
question: Does available official/public DeepSeek information show a publicly accessible next major DeepSeek V release by the contract deadline?
driver: product-launches
date_created: 2026-04-13
source_name: DeepSeek official/public web surfaces and official GitHub org
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
related_drivers: [product-launches, reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-36f15d57/researcher-analyses/2026-04-13/dispatch-case-20260413-36f15d57-20260413T175211Z/personas/base-rate.md]
tags: [primary-source, official-surface, deepseek, release-audit]
---

# Summary

I checked DeepSeek's official website plus clearly official public model surfaces tied to DeepSeek's GitHub/Hugging Face presence. As of 2026-04-13, these surfaces show no publicly accessible flagship model clearly announced as DeepSeek V4 or otherwise explicitly positioned as the next major DeepSeek V successor to V3. The strongest direct official/public evidence remains the existence of DeepSeek-V3 and other non-qualifying projects, which matters because the contract requires official information from DeepSeek plus public accessibility.

## Key facts extracted

- DeepSeek's official website fetch exposed only minimal corporate footer/public-company information and did not surface a public V4 launch announcement.
- DeepSeek's official GitHub organization exists and is clearly linked to DeepSeek.
- GitHub API results show an official `deepseek-ai/DeepSeek-V3` repository, created 2024-12-26 and still the salient V-series flagship-named repository visible in official public repos.
- The broader official GitHub repo list showed many auxiliary projects (e.g. 3FS, DeepEP, DeepGEMM) but no clearly named public `DeepSeek-V4` repository in the returned official repo inventory checked on 2026-04-13.
- Hugging Face organization material visible through fetch did not show a public `DeepSeek-V4` flagship release surface in the checked output; it referenced later V3.2-related collections, which is useful context that DeepSeek can use intermediate/experimental naming rather than jump directly to a qualifying V4 flagship.

## Evidence directly stated by source

- Official GitHub org metadata identifies `deepseek-ai` as organization name "DeepSeek" with blog `https://www.deepseek.com/`.
- Official repo metadata directly states `deepseek-ai/DeepSeek-V3` exists as a public repo and includes timestamps.
- Official repo inventory directly lists many public repos but, in the checked output, no public repo plainly named DeepSeek-V4.

## What is uncertain

- Absence of a GitHub repo or readable website announcement is not definitive proof that no qualifying public release exists; DeepSeek could release primarily through web/app/API access without matching GitHub publication.
- The official website fetch may miss JS-rendered content.
- Hugging Face output included cached/future-facing collection text and is better used as contextual rather than decisive evidence.

## Why this source may matter

The contract's primary source of truth is official information from DeepSeek. Checking official/public surfaces is therefore mandatory. These surfaces are also the most likely place a qualifying public launch would appear if it were clearly announced and generally accessible.

## Possible impact on the question

This source pushes against an immediate confident Yes. It does not rule out a later April launch, but it weakens the case that a qualifying public release had already effectively happened by 2026-04-13 or that strong official evidence already exists.

## Reliability notes

High reliability for what is directly observable on official/public surfaces; only medium completeness because website rendering and unpublished/private rollout channels could hide information.