---
type: source_note
case_key: case-20260413-49227e85
dispatch_id: dispatch-case-20260413-49227e85-20260413T180153Z
analysis_date: 2026-04-13
persona: risk-manager
domain: tech-ai
subdomain: ai-model-releases
entity:
topic: deepseek-v4-release-status
question: DeepSeek V4 released by April 15?
driver: product-launches
date_created: 2026-04-13
source_name: DeepSeek API Docs
source_type: official_docs
source_url: https://api-docs.deepseek.com/
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: risk-manager
related_entities: []
related_drivers: [product-launches]
upstream_inputs: []
downstream_uses: []
tags: [official-source, public-availability, model-version]
---

# Summary

DeepSeek's own public API documentation, fetched on 2026-04-13, identifies the currently exposed API models as `deepseek-chat` and `deepseek-reasoner`, and explicitly says these correspond to DeepSeek-V3.2. The page does not mention any publicly available DeepSeek-V4 endpoint, launch notice, or waitlist/open-beta access path.

## Key facts extracted

- DeepSeek API docs say `deepseek-chat` and `deepseek-reasoner` correspond to DeepSeek-V3.2.
- The docs emphasize that the `/v1` API path naming has no relationship to model version.
- The public docs include standard onboarding material for API access, but no V4 public release announcement.

## Evidence directly stated by source

- "the deepseek-chat and deepseek-reasoner correspond to the model version DeepSeek-V3.2 (128K context limit)"
- "the v1 here has NO relationship with the model's version"

## What is uncertain

- The docs alone do not prove DeepSeek V4 does not exist internally or in private testing.
- The docs do not settle whether DeepSeek might separately launch V4 to the public via app/web/waitlist after this snapshot.

## Why this source may matter

This is a primary official source for what DeepSeek is currently offering publicly via its API. For a rule-sensitive market that requires general-public availability and clear public announcement, the absence of a V4 public offer in official docs is meaningful negative evidence.

## Possible impact on the question

This source pushes against a YES resolution as of 2026-04-13 because it shows DeepSeek's official public API surface still presenting V3.2 rather than V4.

## Reliability notes

High credibility as a first-party public source. Its limitation is scope: it covers public API docs, not necessarily every possible release surface (web app, blog, open beta, public waitlist, or social announcements).