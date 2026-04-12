---
type: source_note
case_key: case-20260410-1c62ba82
dispatch_id: dispatch-case-20260410-1c62ba82-20260410T002235Z
analysis_date: 2026-04-10
persona: market-implied
domain: politics
subdomain: social-media
entity: donald-trump
topic: trump-truth-social-post-count-april-3-to-april-10-2026
question: Will Donald Trump post 100-119 Truth Social posts from April 3 to April 10, 2026?
driver: operational-risk
date_created: 2026-04-10
source_name: Truth Social profile plus third-party archive cross-check
source_type: platform-and-archive
source_url: https://truthsocial.com/@realDonaldTrump
source_date: 2026-04-10
credibility: medium
recency: current
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: orchestrator
related_entities: [donald-trump]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [truth-social, cross-check, archive, poster-identity]
---

# Summary

Truth Social’s public profile page title and metadata identify the account as Donald J. Trump (`@realDonaldTrump`), and an independent archive site (`trumpstruth.org`) displayed the same latest April 9 posts that appeared in the XTracker pull, including the late-night Hungary, Florida, Stefanik, and judicial nomination posts.

## Key facts extracted

- The Truth Social profile page title renders as `Donald J. Trump (@realDonaldTrump)`.
- The public HTML metadata includes the same avatar image URL used by the tracker user object.
- `trumpstruth.org` displayed the same sequence of late April 9 posts that the XTracker API returned, including:
  - the Florida / Haiti crime post
  - the Viktor Orbán endorsement post
  - the Elise Stefanik book post
  - the Benjamin Flowers nomination post
  - the Strait of Hormuz / Iran-related posts
- This cross-check supports that the tracker is following the correct account and is capturing real posts visible to outside observers.

## Evidence directly stated by source

- Truth Social profile metadata identifies the account name/handle.
- The independent archive reproduces recent post content matching XTracker output.

## What is uncertain

- The publicly fetched Truth Social profile HTML was JS-heavy and did not expose a clean countable post list by itself.
- The archive page did not visibly separate main-feed posts from reply-only activity in the fetched text.
- The archive is not the resolution source and should be treated as contextual corroboration, not authoritative settlement evidence.

## Why this source may matter

It provides an independence check on poster identity and on whether the tracker is capturing actual public-facing posts from the correct account.

## Possible impact on the question

It increases confidence that the tracker’s count is not a wrong-account or phantom-data issue, but it does not settle the main-feed / reply / deleted-post edge cases on its own.

## Reliability notes

Moderate only. Useful as a corroborating platform/archive cross-check, not as the primary count source. The JS-heavy Truth Social page limits direct manual auditing from this environment.