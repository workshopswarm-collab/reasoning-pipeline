---
type: source_note
case_key: case-20260413-49227e85
dispatch_id: dispatch-case-20260413-49227e85-20260413T180153Z
analysis_date: 2026-04-13
persona: base-rate
domain: technology
subdomain: ai-model-releases
entity:
topic: DeepSeek V-series cadence and comparable release behavior
question: What outside-view/base-rate evidence is relevant to whether DeepSeek publicly ships the next major V model by Apr 15, 2026?
driver: operational-risk
date_created: 2026-04-13
source_name: DeepSeek official GitHub commit/repo timestamps and Hugging Face model timestamps
source_type: official/public release cadence evidence
source_url: https://api.github.com/users/deepseek-ai/repos?per_page=100
source_date: 2026-04-13
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [deepseek, cadence, base-rate]
---

# Summary

The outside view from DeepSeek's own public release history suggests major V-line releases are infrequent and often followed by incremental V3.x variants rather than immediate new flagship-number jumps. That base rate argues against assuming a public V4 launch in a very short remaining window absent direct official evidence.

## Key facts extracted

- Official GitHub repo creation dates show DeepSeek-V2 on 2024-04-22 and DeepSeek-V3 on 2024-12-26, implying roughly an 8-month gap between major V-line public repo appearances.
- The latest official DeepSeek-V3 repository push seen via GitHub API was 2025-08-27, indicating continued maintenance of the V3 line rather than a visible handoff to a V4 repo by Apr 13, 2026.
- DeepSeek's Hugging Face org shows V3.2-Exp created 2025-09-29 and V3.2 created 2025-12-01, reinforcing that late-2025 public positioning stayed within the V3 family.
- Given that the contract requires the next major V release, intermediate labels such as V3.2 do not count even if they are public and significant.

## Evidence directly stated by source

- GitHub API directly states repository creation and push timestamps.
- Hugging Face API/page directly states model identifiers and creation timing.

## What is uncertain

- Public repo/model-card timing is not identical to corporate announcement timing.
- DeepSeek may intentionally avoid public pre-positioning until launch day.
- A one-off acceleration could still break the historical cadence.

## Why this source may matter

This source supports the outside-view anchor. Markets often overprice short-window launches from salient AI labs without enough adjustment for how rarely a lab jumps to a new flagship-numbered model on command.

## Possible impact on the question

This cadence evidence lowers the prior for a qualifying release within the remaining two-day window unless fresh official launch evidence appears.

## Reliability notes

- These are official/public timestamps, so they are strong for cadence and naming behavior.
- They are indirect rather than dispositive for the exact market outcome because the model could launch through another official channel or after a private development cycle.