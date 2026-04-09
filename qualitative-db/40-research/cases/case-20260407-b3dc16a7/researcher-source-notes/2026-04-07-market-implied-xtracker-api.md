---
type: source_note
case_key: case-20260407-b3dc16a7
dispatch_id: dispatch-case-20260407-b3dc16a7-20260407T031152Z
analysis_date: 2026-04-07
persona: market-implied
domain: politics
subdomain: trump
entity: donald-trump
topic: case-20260407-b3dc16a7 | market-implied
question: Will Donald Trump post 80-99 Truth Social posts from March 31 to April 7, 2026?
driver: reliability
date_created: 2026-04-07
source_name: XTracker API for @realDonaldTrump and assigned March 31-April 7 tracking window
source_type: tracker-api
source_url: https://xtracker.polymarket.com/user/realDonaldTrump
source_date: 2026-04-07
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: medium
agent: market-implied
related_entities: [donald-trump]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260407-b3dc16a7/researcher-analyses/2026-04-07/dispatch-case-20260407-b3dc16a7-20260407T031152Z/personas/market-implied.md]
tags: [xtracker, truth-social, post-count, resolution-source]
---

# Summary

XTracker is the governing resolution source named in the market rules. Its public API for `realDonaldTrump` exposes both the relevant tracking window and the counted posts inside that window. On the additional verification pass run during this research session, the specific March 31-April 7 tracking record reported `stats.total = 77` with `percentComplete = 100` but `isComplete = false`, consistent with the market window being underway but already substantially populated. A direct pull of posts for `startDate=2026-03-31T16:00:00.000Z` and `endDate=2026-04-07T15:59:59.000Z` also returned 77 posts, matching the tracker total.

## Key facts extracted

- `api/users/realDonaldTrump` identifies the tracked account as `Donald J. Trump`, platform `TRUTH_SOCIAL`, handle `realDonaldTrump`, verified `true`, with Truth Social platform ID `107780257626128497`.
- The relevant tracking object is titled `Donald Trump # Truth Social posts March 31 - April 7, 2026?`.
- That tracking object uses `startDate = 2026-03-31T16:00:00.000Z` and `endDate = 2026-04-07T15:59:59.000Z`, which corresponds to the noon ET to noon ET market window.
- `api/trackings/9f35cbad-4204-4aa3-9ea5-157a88b0b32c?includeStats=true` returned `stats.total = 77` as of the check.
- `api/users/realDonaldTrump/posts?startDate=...&endDate=...` returned 77 post objects, matching the tracker total exactly.
- Quick content audit of the returned objects shows a mix of ordinary text/link posts, empty-body items, and quote/repost-style items marked by `quote-inline` / `RT:` in content. That mix is directionally consistent with the rule that main feed posts, quote posts, and reposts count.
- In the same audit, some returned items appear to have substantial `replies_count` metrics, but the dataset itself is still being included by the tracker because they are present in the main feed export; this matches the rule nuance that replies generally do not count, yet replies recorded on the main feed are counted by the tracker.
- Previous-week contextual pull for March 24-March 31 returned 99 posts, showing the current 77 count is notably below the immediately prior week.

## Evidence directly stated by source

- The account being tracked is `@realDonaldTrump` on Truth Social and is marked verified.
- The tracker window for this market exists and is active.
- The current tracked total for the window is 77.
- The API exposes the underlying counted posts for the same window.

## What is uncertain

- The API response does not by itself label each item with a clean post-type enum such as `main post`, `quote`, `repost`, or `reply`; that had to be inferred from content structure and from the market-rule language.
- The source does not independently prove whether any qualifying deleted posts were captured earlier and later removed from Truth Social itself, though the tracker rules say such captured deleted posts should still count.
- `percentComplete = 100` appears to be a somewhat awkward field because the market window had not yet ended at the time of audit; the more decision-relevant field is the actual total plus time remaining.

## Why this source may matter

This is the market's explicit source of truth unless it fails to track correctly. Because this is a narrow, rule-sensitive counting market, the tracker itself matters more than generic commentary or price action.

## Possible impact on the question

At 77 counted posts with only the overnight-to-noon ET segment left, the market would need at least 3 more counted posts to enter the 80-99 band and at least 23 more to leave the band on the high side. That makes the path into the band plausible but not locked, while the path above 99 looks much less likely than it did in the prior 99-post week.

## Reliability notes

Strong on recency and direct relevance because it is the named settlement source and exposes the exact tracked objects. Moderate caveat: tracker implementation details are somewhat opaque, and some rule-sensitive classifications (reply vs repost vs main-feed inclusion) are only partially transparent from the returned schema.