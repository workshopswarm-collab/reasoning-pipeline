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
driver: reliability
date_created: 2026-04-07T03:12:00Z
source_name: Trump's Truth archive cross-check
source_type: secondary_archive
source_url: https://www.trumpstruth.org/search?start_date=2026-03-31&end_date=2026-04-07&removed=include&per_page=100&sort=date_desc
source_date: 2026-04-07
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [donald-trump]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260407-b3dc16a7/researcher-analyses/2026-04-07/dispatch-case-20260407-b3dc16a7-20260407T031152Z/personas/risk-manager.md]
tags: [archive, cross-check, source-note, truth-social]
---

# Summary

This note cross-checks XTracker against the third-party Trump’s Truth archive, which archives Donald Trump Truth Social posts and exposes a search view with `removed=include`.

## Key facts extracted

- The archive identifies the account as `Donald J. Trump` / `@realDonaldTrump` and uses the same Truth Social avatar/profile identity as the official page.
- Search with `start_date=2026-03-31`, `end_date=2026-04-07`, `removed=include`, `per_page=100`, `sort=date_desc` produced 90 rendered result blocks, 84 unique archive status pages.
- Several archive items before noon ET on March 31 appear in the result set (e.g. 7:11 AM, 7:19 AM, 9:15 AM, 9:21 AM, 10:53 AM, 11:45 AM local timestamps), so the raw archive result set is broader than the market window and cannot be used as a simple direct count without filtering.
- Many archive rows are blank-content entries or repost/RT-style entries, consistent with the market's warning that classification and exclusions matter.
- Archive samples match recent XTracker items closely for late-window posts on Apr 6-7, including the Georgia special election post and the two late Apr 7 text posts.
- The archive did not, in this quick scrape, display a simple explicit deleted-post count or a clean marker that would let me isolate captured-then-deleted items mechanically.

## Evidence directly stated by source

- Trump’s Truth describes itself as an archive of all Donald Trump Truth Social posts and exposes a search UI that can `Include removed` posts.
- Result rows are tied to `@realDonaldTrump` and individual archive status pages.

## What is uncertain

- The archive search result set includes posts outside the market window when only date filters are used, so it is not a precise settlement counter.
- I did not establish a one-to-one machine mapping from archive status IDs to Truth Social platform IDs.
- Because reposts, quote posts, and blank media posts appear in the archive, manual filtering would still be needed to convert the archive into a market-valid count.
- The archive is an independent contextual source, not the governing resolution source.

## Why this source may matter

It is useful as an independence check on tracker identity, broad activity level, and whether the tracker appears to be obviously missing large chunks of feed activity or deleted/captured items.

## Possible impact on the question

The archive supports the view that Trump was highly active in the period and that XTracker is following the correct account, but it also reinforces the main risk-manager point: raw feed/archive volume is not the same as countable resolution volume because replies/exclusions/window boundaries matter. It did not surface a clear reason to think XTracker was missing several countable in-window posts.

## Reliability notes

- Strength: independent from Polymarket and includes removed-post search mode.
- Weakness: search/date filtering is imperfect for exact settlement counting, and post-type classification is not clean enough for direct market resolution.
- Best use: cross-check provenance and spot obvious tracker failures, not replace the governing counter unless XTracker breaks.