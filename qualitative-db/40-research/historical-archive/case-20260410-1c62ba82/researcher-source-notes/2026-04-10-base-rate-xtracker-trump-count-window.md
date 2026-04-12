---
type: source_note
case_key: case-20260410-1c62ba82
dispatch_id: dispatch-case-20260410-1c62ba82-20260410T002235Z
analysis_date: 2026-04-10
persona: base-rate
domain: politics
subdomain: social-media
entity: donald-trump
topic: trump-truth-social-post-count
question: Will Donald Trump post 100-119 Truth Social posts from April 3 to April 10, 2026?
driver: reliability
date_created: 2026-04-09
source_name: XTracker Polymarket API tracking and posts endpoints
source_type: API / tracker
source_url: https://xtracker.polymarket.com/docs
source_date: 2026-04-10
credibility: medium-high
recency: current
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [donald-trump]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260410-1c62ba82/researcher-analyses/2026-04-10/dispatch-case-20260410-1c62ba82-20260410T002235Z/personas/base-rate.md]
tags: [xtracker, truth-social, post-count, resolution-source]
---

# Summary

XTracker is the governing resolution surface for this market, and its documented public API exposes enough detail to audit the relevant window. For the exact April 3 12:00 PM ET to April 10 12:00 PM ET tracking period tied to this market, the tracker returned `stats.total = 103`, which falls inside the 100-119 bucket.

## Key facts extracted

- XTracker docs state the API supports Truth Social and that `/trackings/{id}?includeStats=true` returns computed statistics including `stats.total`.
- The Donald Trump April 3-April 10 market tracking id is `5bbf11f3-3970-4fd1-8704-1be33e781109`.
- The tracking window in the API is `startDate: 2026-04-03T16:00:00.000Z` and `endDate: 2026-04-10T15:59:59.000Z`, matching noon ET to noon ET.
- The user attached to the tracking is `realDonaldTrump`, `name: Donald J. Trump`, `platform: TRUTH_SOCIAL`, `platformId: 107780257626128497`, `verified: true`.
- The tracking stats endpoint returned `total: 103`, `cumulative: 103`, `pace: 103`.
- The user posts endpoint for the same date window returned post objects from the exact period, with timestamps and content, showing the tracker is holding individual exported records rather than only a headline count.

## Evidence directly stated by source

- XTracker docs: public endpoint supports `GET /trackings/{id}?includeStats=true` and returns `stats.total`.
- Tracking detail for this market: Trump Truth Social April 3-April 10, 2026.
- Tracking stats value at time checked: `103`.
- Posts endpoint exists and returns post-level records within a date window for `realDonaldTrump` on `TRUTH_SOCIAL`.

## What is uncertain

- I did not recover a separate explicit API field labeling which returned posts are reposts, quote posts, or replies.
- I did not independently enumerate all 103 records from the posts endpoint to replicate the count one by one.
- Deleted-post handling remains dependent on tracker capture, as the market rules already specify.

## Why this source may matter

This is the market’s governing source of truth unless the tracker fails to reflect the contract correctly. It directly answers both identity and count, and it is the main evidence surface for resolution.

## Possible impact on the question

If the tracker remains functioning correctly, the current answer is Yes for the 100-119 bucket because 103 lies inside the target range.

## Reliability notes

- Strong relevance because the market explicitly names XTracker’s Post Counter as the resolution source.
- Medium-high credibility rather than absolute because tracker correctness still depends on implementation details around replies and deleted posts.
- Independence is limited: the same system provides both count and exported records. Truth Social therefore remains a useful fallback/contextual cross-check rather than a fully independent count source.