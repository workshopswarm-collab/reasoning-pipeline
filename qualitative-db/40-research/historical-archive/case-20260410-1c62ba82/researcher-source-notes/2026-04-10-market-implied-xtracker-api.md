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
driver: reliability
date_created: 2026-04-10
source_name: XTracker API
source_type: tracker-api
source_url: https://xtracker.polymarket.com/docs
source_date: 2026-04-10
credibility: medium-high
recency: current
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [donald-trump]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [xtracker, truth-social, resolution-source, post-count]
---

# Summary

XTracker is the governing primary resolution source for this market. Its public docs expose endpoints that identify the tracked Truth Social user, the relevant tracking window, and the post list within the date range. For this case, the API returned Donald J. Trump / `realDonaldTrump` on `TRUTH_SOCIAL`, verified, with platformId `107780257626128497`, and 103 posts captured in the April 3 12:00 ET to April 10 12:00 ET window as of shortly after 20:20 ET on April 9.

## Key facts extracted

- `GET /api/users/realDonaldTrump?platform=TRUTH_SOCIAL` returns the tracked user as Donald J. Trump, verified, handle `realDonaldTrump`, platformId `107780257626128497`.
- `GET /api/users/realDonaldTrump/trackings?platform=TRUTH_SOCIAL` returns the exact market tracking period `2026-04-03T16:00:00.000Z` to `2026-04-10T15:59:59.000Z`, matching the contract window.
- `GET /api/users/realDonaldTrump/posts?platform=TRUTH_SOCIAL&startDate=2026-04-03T16:00:00.000Z&endDate=2026-04-10T00:25:00.000Z` returned 103 posts in-window at query time.
- Returned records include timestamps, platform post IDs, content, and engagement metrics, showing the tracker has actually captured concrete posts rather than only publishing an aggregate count.
- The tracker docs state `/users/[handle]/posts` is the public route for retrieving posts in a date range and supports `platform`, `startDate`, `endDate`, and `timezone` parameters.

## Evidence directly stated by source

- XTracker docs describe the API as providing access to post tracking data for X and Truth Social users.
- The tracked user endpoint explicitly identifies the account as Donald J. Trump / `realDonaldTrump` on `TRUTH_SOCIAL` and marked verified.
- The trackings endpoint explicitly lists the exact April 3-April 10 market window.
- The posts endpoint directly returns 103 captured posts within the queried in-window range.

## What is uncertain

- The public API sample did not itself label each returned item as main-feed post vs reply vs repost vs quote post.
- The tracker docs did not explicitly document whether reply-only items are excluded at the API layer, though the contract says the market resolves to the tracker’s Post Counter figure and allows tracker-captured replies if they are recorded on the main feed.
- The query was done before market close, so the 103 count is not final.
- Deleted-post treatment is contract-level and tracker-process-level; this snapshot cannot prove absence of missed very short-lived deletions.

## Why this source may matter

It is the contract’s governing source of truth unless the tracker fails to update correctly. It is also the cleanest available source for poster identity and live in-window count.

## Possible impact on the question

This source strongly supports the market’s current high probability for the 100-119 bucket because the tracked count was already 103 with roughly half a day left before resolution. The same source also implies growing risk of overshooting 119 if posting pace remains elevated.

## Reliability notes

Strong for identity and live count because it is the designated primary resolution source and exposes structured endpoints. Less strong for nuanced rule auditing because the public docs do not fully explain reply/main-feed classification or deleted-post capture edge cases.