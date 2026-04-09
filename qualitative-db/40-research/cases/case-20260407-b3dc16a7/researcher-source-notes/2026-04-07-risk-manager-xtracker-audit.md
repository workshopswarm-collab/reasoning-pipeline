---
type: source_note
case_key: case-20260407-b3dc16a7
dispatch_id: dispatch-case-20260407-b3dc16a7-20260407T031152Z
analysis_date: 2026-04-07
persona: risk-manager
domain: politics
subdomain: social-media
entity: donald-trump
topic: case-20260407-b3dc16a7 | risk-manager
question: Will Donald Trump post 80-99 Truth Social posts from March 31 to April 7, 2026?
driver: operational-risk
date_created: 2026-04-07T03:12:00Z
source_name: Polymarket XTracker API audit for @realDonaldTrump
source_type: tracker_api
source_url: https://xtracker.polymarket.com/user/realDonaldTrump
source_date: 2026-04-07
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: medium
agent: orchestrator
related_entities: [donald-trump]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260407-b3dc16a7/researcher-analyses/2026-04-07/dispatch-case-20260407-b3dc16a7-20260407T031152Z/personas/risk-manager.md]
tags: [xtracker, audit, source-note, truth-social]
---

# Summary

This note audits the stated governing resolution source for the market: Polymarket's XTracker for `@realDonaldTrump` on Truth Social.

## Key facts extracted

- `https://xtracker.polymarket.com/api/users/realDonaldTrump` identifies the tracked account as `Donald J. Trump`, platform `TRUTH_SOCIAL`, handle `realDonaldTrump`, platformId `107780257626128497`, verified `true`.
- The relevant tracking entry is `Donald Trump # Truth Social posts March 31 - April 7, 2026?` with tracking window `2026-03-31T16:00:00.000Z` to `2026-04-07T15:59:59.000Z`, which corresponds to Mar 31 12:00 PM ET to Apr 7 11:59:59 AM ET.
- `https://xtracker.polymarket.com/api/trackings/9f35cbad-4204-4aa3-9ea5-157a88b0b32c?includeStats=true` returned `total: 77`.
- `https://xtracker.polymarket.com/api/users/realDonaldTrump/posts?startDate=2026-03-31T16:00:00.000Z&endDate=2026-04-07T15:59:59.000Z` returned 77 posts, matching the tracker total exactly.
- The returned post list includes a mix of normal posts, quote/repost-style items, and blank-content items likely representing media-only or repost artifacts.
- Mechanical composition of the 77 captured items from the API sample audit:
  - 55 nonblank ordinary text/link posts
  - 5 quote-inline / repost-style items
  - 17 blank-content items
- The latest captured in-window post in the API sample was at `2026-04-07T01:59:08.390Z`; as of audit time the market window still had roughly 10 hours remaining before noon ET resolution.

## Evidence directly stated by source

- XTracker is actively syncing this user and reports `lastSync: 2026-04-07T03:11:04.388Z`.
- The specific market tracking object is active and tied to the exact Polymarket event URL for this case.
- XTracker's own stats endpoint says the count is 77, which is below the 80-99 band.

## What is uncertain

- The API output does not directly label each returned item as main-feed post vs reply vs repost; classification must be inferred from content structure and the market rules.
- Blank-content items could be media-only main-feed posts, repost shells, or other tracker representations; without per-item feed metadata they cannot be perfectly subclassified from the API alone.
- The tracker output at audit time is not final because the window had not yet closed.
- The API does not visibly expose whether any deleted posts were captured then later removed, only that captured items remain in the data returned now.

## Why this source may matter

It is the governing source of truth under market rules unless it fails to update correctly. It is therefore both direct evidence on current count and the most important object for resolution mechanics.

## Possible impact on the question

At audit time the governing source showed 77 in-window counted items, meaning the market needed at least 3 additional countable posts before noon ET to enter the 80-99 band. That keeps "Yes" alive but leaves limited margin if posting slows or if some apparent feed activity is non-counting.

## Reliability notes

- Strongest feature: this is the explicit resolution source named by the market.
- Main weakness: tracker classification logic is partly opaque, especially around replies, reposts, and deleted-post capture.
- The fact that stats total and raw post endpoint both independently returned 77 is a useful internal consistency check.
- Because the market wording has exclusions, the tracker should be treated as authoritative but still audited against a secondary archive for miss/overcount risk.