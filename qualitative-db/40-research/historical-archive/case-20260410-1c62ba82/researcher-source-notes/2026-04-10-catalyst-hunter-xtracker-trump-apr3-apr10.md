---
type: source_note
case_key: case-20260410-1c62ba82
dispatch_id: dispatch-case-20260410-1c62ba82-20260410T002235Z
analysis_date: 2026-04-10
persona: catalyst-hunter
domain: politics
subdomain: social-media-monitoring
entity: donald-trump
topic: trump-truth-social-post-count-apr3-apr10
question: Will Donald Trump post 100-119 Truth Social posts from April 3 to April 10, 2026?
driver: operational-risk
date_created: 2026-04-10
source_name: XTracker API docs and realDonaldTrump tracking endpoints
source_type: tracker-api
source_url: https://xtracker.polymarket.com/docs
source_date: 2026-04-10
credibility: medium-high
recency: current
stance: neutral
certainty: medium-high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [donald-trump]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260410-1c62ba82/researcher-analyses/2026-04-10/dispatch-case-20260410-1c62ba82-20260410T002235Z/personas/catalyst-hunter.md]
tags: [xtracker, truth-social, post-counter, resolution-source]
---

# Summary

XTracker is the governing source of truth for this market unless it fails to update correctly. Its public API exposes both the active Trump Truth Social tracking window and the counted posts inside that window.

## Key facts extracted

- XTracker docs state the base API URL is `https://xtracker.polymarket.com/api` and that it supports Truth Social with `platform=TRUTH_SOCIAL`.
- The docs describe endpoints for tracked users, user-specific trackings, user posts within a date range, and tracking statistics.
- `GET /api/users/realDonaldTrump?platform=TRUTH_SOCIAL` returns Donald J. Trump, verified, with platformId `107780257626128497` and the relevant tracking window titled `Donald Trump # Truth Social posts April 3 - April 10, 2026?`.
- That window runs from `2026-04-03T16:00:00.000Z` to `2026-04-10T15:59:59.000Z`, matching the contract’s noon ET to noon ET window.
- `GET /api/users?platform=TRUTH_SOCIAL&stats=true` for the relevant market link shows `totalBetweenStartAndEnd: 103` with daily counts of 6, 9, 11, 19, 37, 10, and 11 through April 9.
- `GET /api/users/realDonaldTrump/posts?...` returned timestamped individual posts for the window, including multiple posts late on April 9 UTC / April 9 ET, showing the feed was still active and syncing.
- XTracker reported `lastSync` around `2026-04-09T23:50:25.128Z` for the April 3-April 10 market at the time checked.

## Evidence directly stated by source

- The docs explicitly state that tracking periods are defined in EST / America-New_York while database dates are stored in UTC.
- The stats endpoint directly reports the running total between the start and end of the specified tracking window.
- The posts endpoint directly returns post-level records with timestamps and content for the selected user and date range.

## What is uncertain

- The public endpoints do not by themselves show a labeled field for whether an item is a repost, quote post, or reply; they mostly show counted posts and timestamped post objects.
- The API evidence alone does not prove whether any deleted posts were captured earlier and later removed from Truth Social, only that XTracker counts according to its own stored observations.
- There remains a live-window risk between the latest sync and the market close at noon ET.

## Why this source may matter

This is the contract-named resolution source. It is both the strongest direct evidence and the most important operational surface because the market settles to the XTracker post counter unless the tracker fails to update correctly.

## Possible impact on the question

A count of 103 already places the contract inside the 100-119 bucket with roughly 12 hours left. The remaining question is no longer whether Trump can reach the bucket, but whether he will post enough additional counted items before noon ET to move above 119.

## Reliability notes

- Strongest feature: contract-aligned and machine-readable.
- Main weakness: independent verification is limited because the public Truth Social page is JS-heavy and the API does not fully expose every classification detail in the quick pass.
- Still, for this market, XTracker is not merely contextual evidence; it is the named governing source unless operational failure is shown.
