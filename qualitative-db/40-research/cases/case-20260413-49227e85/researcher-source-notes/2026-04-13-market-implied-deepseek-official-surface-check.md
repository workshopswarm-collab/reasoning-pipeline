---
type: source_note
case_key: case-20260413-49227e85
dispatch_id: dispatch-case-20260413-49227e85-20260413T180153Z
analysis_date: 2026-04-13
persona: market-implied
domain: tech-ai
subdomain: ai-model-releases
entity:
topic: DeepSeek official public release surface check
question: Will DeepSeek V4 be released to the general public by April 15, 2026?
driver: product-launches
date_created: 2026-04-13
source_name: DeepSeek official website and accessible endpoints
source_type: official primary source check
source_url: https://www.deepseek.com/
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: high
agent: Orchestrator
related_entities: []
related_drivers: [product-launches, reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-49227e85/researcher-analyses/2026-04-13/dispatch-case-20260413-49227e85-20260413T180153Z/personas/market-implied.md]
tags: [official-source, deepseek, website-check, release-surface]
---

# Summary

I checked DeepSeek’s official website and several obvious public endpoints for signs of a public V4 launch. I did not find an official announcement, blog/news page, or clearly accessible V4 product surface.

## Key facts extracted

- `https://www.deepseek.com/` was live on April 13, 2026 but the extracted readable content was effectively only the site footer/copyright, with no surfaced V4 launch announcement in the fetched readable output.
- Direct endpoint checks found:
  - `https://www.deepseek.com` responded 200.
  - `https://chat.deepseek.com` returned 403 Forbidden.
  - `https://api.deepseek.com` returned 401 Unauthorized.
  - `https://www.deepseek.com/api` returned 404 Not Found.
  - `https://www.deepseek.com/news` returned 404 Not Found.
  - `https://www.deepseek.com/blog` returned 404 Not Found.
- No obvious public-facing official release page for DeepSeek V4 was detected in this pass.

## Evidence directly stated by source

The website itself did not directly state that V4 had launched publicly.

## What is uncertain

- A dynamic or region-specific official announcement page could exist but not be surfaced in the fetch/readability pass.
- Some public-access mechanism may exist behind pages not discoverable from the checked endpoints.
- 403/401 responses do not by themselves rule out later general-public availability.

## Why this source may matter

The contract explicitly prioritizes official DeepSeek information. Absence of an official public V4 launch surface on April 13 is meaningful negative evidence for a deadline only about two days away.

## Possible impact on the question

This check weakens the case for a near-certain Yes. It suggests the market may be pricing expectation and rumors rather than already-visible qualifying public availability.

## Reliability notes

High value as a primary-source absence check, but still partial because absence-of-evidence on web surfaces is weaker than a direct official statement saying no launch has occurred.