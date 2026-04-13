---
type: source_note
case_key: case-20260413-49227e85
dispatch_id: dispatch-case-20260413-49227e85-20260413T180153Z
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: technology
subdomain: ai-model-releases
entity:
topic: DeepSeek official release surfaces before April 15, 2026
question: Will the next DeepSeek V model be made available to the general public by April 15, 2026?
driver: product-launches
date_created: 2026-04-13
source_name: DeepSeek API Docs news pages and current API docs
source_type: official_vendor_docs
source_url: https://api-docs.deepseek.com/
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
downstream_uses: [qualitative-db/40-research/cases/case-20260413-49227e85/researcher-analyses/2026-04-13/dispatch-case-20260413-49227e85-20260413T180153Z/personas/catalyst-hunter.md]
tags: [deepseek, official-source, release-timing, api-docs]
---

# Summary

DeepSeek's official API docs and news index show no publicly announced DeepSeek V4 release as of the research date. The visible official release chronology instead shows DeepSeek-R1 on 2025-01-20, DeepSeek-V3-0324 on 2025-03-25, DeepSeek-R1-0528 on 2025-05-28, DeepSeek V3.1 on 2025-08-21 and 2025-09-22, and DeepSeek-V3.2 on 2025-12-01. The live API docs home page also states that `deepseek-chat` and `deepseek-reasoner` correspond to DeepSeek-V3.2, not a V4 model.

## Key facts extracted

- The official docs home page currently says `deepseek-chat` and `deepseek-reasoner` correspond to model version DeepSeek-V3.2.
- The official news chronology includes multiple releases and updates through late 2025 but no listed DeepSeek V4 launch.
- The official 2025-03-25 news post is explicitly a DeepSeek-V3-0324 release, not V4.
- The official 2025-01-20 release page is for DeepSeek-R1, confirming DeepSeek publicly announces major launches on this surface.

## Evidence directly stated by source

- DeepSeek API Docs home: `deepseek-chat` and `deepseek-reasoner` correspond to DeepSeek-V3.2.
- DeepSeek news page chronology includes named releases and updates, with no V4 entry visible on 2026-04-13.
- DeepSeek-V3-0324 release page says API usage remains unchanged and links to open-source weights for V3-0324.

## What is uncertain

- DeepSeek could announce a V4 release between now and the April 15 deadline.
- The official website/app could expose a V4 launch on a surface other than the API docs before that date.
- Absence from the docs today does not prove non-release by the deadline; it only weighs against imminent public availability.

## Why this source may matter

The market's primary resolution source is official information from DeepSeek. This is therefore the best currently available source of truth on whether a qualifying major release has already happened and what model family is currently public.

## Possible impact on the question

This source materially lowers the probability that a qualifying DeepSeek V4 has already been launched or is already publicly accessible. It also suggests the current public flagship remains in the V3.x line, making a before-deadline V4 launch a short-fuse catalyst rather than an already underway rollout.

## Reliability notes

High reliability for what is officially announced and currently offered by DeepSeek. Lower reliability for proving a future non-event, because a launch could still occur after this snapshot.