---
type: source_note
case_key: case-20260413-36f15d57
dispatch_id: dispatch-case-20260413-36f15d57-20260413T175211Z
analysis_date: 2026-04-13
persona: risk-manager
domain: ai
subdomain: model-releases
entity:
topic: DeepSeek next major V-series release public availability
question: Will the next DeepSeek V model be made available to the general public by the deadline under the contract wording?
driver: product-launches
date_created: 2026-04-13
source_name: DeepSeek official public surfaces (website, Hugging Face org, GitHub org)
source_type: official primary sources
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
tags: [deepseek, official-source, public-release, model-release]
---

# Summary

DeepSeek's official public-facing surfaces checked in this run do not show a publicly accessible DeepSeek V4 or V5 flagship release. The website fetch yielded only corporate footer/legal information, the Hugging Face org page shows V3.2-era model collections rather than a V4/V5 flagship, and GitHub org searches for DeepSeek-V4 / DeepSeek-V5 returned zero repositories.

## Key facts extracted

- `www.deepseek.com` fetched successfully but exposed only company footer/legal information in extraction, with no visible V4/V5 public release announcement in the extracted content.
- Hugging Face org page for `deepseek-ai` showed collections including DeepSeek-OCR and DeepSeek-V3.2, including `DeepSeek-V3.2`, `DeepSeek-V3.2-Exp`, and related variants.
- GitHub search for `org:deepseek-ai DeepSeek-V4` returned `total_count: 0`.
- GitHub search for `org:deepseek-ai DeepSeek-V5` returned `total_count: 0`.
- The `deepseek-ai/DeepSeek-V3` repository exists, with active maintenance continuing into 2025 rather than obvious supersession by a new V4 repo.

## Evidence directly stated by source

- Hugging Face explicitly displayed V3.2 family model names on DeepSeek's org page.
- GitHub API explicitly returned no V4/V5 repositories under the DeepSeek org search queries used.
- DeepSeek-V3 GitHub repo metadata showed the repo is real, public, and materially updated after initial release.

## What is uncertain

- The DeepSeek website extraction is sparse; absence of evidence from readability output is weaker than absence from structured repositories/HF model cards.
- A qualifying release could exist on an official API or waitlist page not exposed in the surfaces checked here.
- The contract allows open beta or open rolling waitlist signups, so a non-download-based public access page could still qualify if officially announced and generally accessible.

## Why this source may matter

These are the most relevant primary surfaces for whether DeepSeek itself has made a new flagship V-series model publicly accessible. They directly bear on the contract's primary source-of-truth requirement.

## Possible impact on the question

The lack of a visible official V4/V5 public release signal on primary DeepSeek-controlled surfaces is meaningful negative evidence for a Yes resolution as of this run date, though not fully dispositive because contract-qualified access might still appear via another official DeepSeek channel.

## Reliability notes

Primary-source quality is high, but negative inference from absence is only medium strength. Stronger if combined with no credible independent reporting and no official announcement language.