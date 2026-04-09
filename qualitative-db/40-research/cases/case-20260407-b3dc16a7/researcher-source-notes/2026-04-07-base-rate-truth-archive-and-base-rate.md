---
type: source_note
case_key: case-20260407-b3dc16a7
dispatch_id: dispatch-case-20260407-b3dc16a7-20260407T031152Z
analysis_date: 2026-04-07
persona: base-rate
domain: politics
subdomain: social-media
entity: donald-trump
topic: case-20260407-b3dc16a7 | base-rate
question: Will Donald Trump post 80-99 Truth Social posts from March 31 to April 7, 2026?
driver: reliability
date_created: 2026-04-07
source_name: CNN Truth Social archive plus 2025 posting-rate reporting
source_type: dataset+media-report
source_url: https://ix.cnn.io/data/truth-social/truth_archive.json
source_date: 2026-04-07
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [donald-trump]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260407-b3dc16a7/researcher-analyses/2026-04-07/dispatch-case-20260407-b3dc16a7-20260407T031152Z/personas/base-rate.md]
tags: [truth-social, post-count, base-rate, archive]
---

# Summary

Independent archive evidence suggests Trump posted 79 times in the market window from 2026-03-31 12:00 ET to 2026-04-07 12:00 ET, which is just below the 80-99 band. Broader posting-rate context suggests the 80-99 bucket is plausible but slightly low relative to his recent typical 7-day output.

## Key facts extracted

- The CNN-hosted Truth Social archive was reachable and current through 2026-04-07, with the latest entries at 2026-04-07T01:59:08Z.
- Counting all archived posts between 2026-03-31T16:00:00Z and 2026-04-07T16:00:00Z produced 79 posts.
- Day-level counts in that ET-adjusted window were: Mar 31 = 5, Apr 1 = 11, Apr 2 = 14, Apr 3 = 7, Apr 4 = 13, Apr 5 = 10, Apr 6 = 14, Apr 7 pre-noon ET = 5.
- Rough signature checks on the 79 rows found 5 entries beginning with "RT:" and 17 blank-content posts with media attached, indicating the archive includes repost-like and media-only items that are relevant to the market’s inclusion rules.
- A 2025 local-TV data analysis (KOCO / Hearst) reported 6,168 posts in calendar 2025, about 18 per day on average, with two days above 100 posts.
- My direct count from the CNN archive for calendar 2025 found 6,229 archived rows across 362 active days, about 17.1 per calendar day, which is directionally consistent with the KOCO/Hearst figure.
- Twelve non-overlapping 7-day windows immediately preceding the target window in 2026 ranged from 77 to 210 posts, averaging 132.25.

## Evidence directly stated by source

- The GitHub archive project states its old public repo stopped updating in late 2025 and points users to a CNN-hosted archive updated every five minutes.
- KOCO/Hearst states Trump averaged 18 Truth Social posts per day in 2025 and had multiple days over 100 posts.

## What is uncertain

- The CNN archive is an independent tracker, not the market’s governing xtracker counter.
- The archive does not expose a clean field telling original post vs quote post vs repost vs reply in the fetched rows I inspected.
- Because the market counts main-feed posts, quote posts, and reposts, but excludes replies unless they appear on the main feed, exact rule matching between archive rows and xtracker remains somewhat ambiguous.
- Deleted posts captured by xtracker for ~5 minutes could create small mismatches versus a downstream archive snapshot.

## Why this source may matter

It provides both a near-real-time independent count for the exact market window and a broader outside-view baseline for Trump’s posting frequency, which is useful for a base-rate persona and for auditing whether the xtracker-derived range is plausible.

## Possible impact on the question

The exact-window archive count of 79 is mildly bearish for the 80-99 bucket if the archive roughly matches market rules. But the broader posting baseline suggests the bucket is near the lower edge of Trump’s normal posting intensity rather than an implausibly high threshold.

## Reliability notes

- Strengths: current, machine-readable, directly tied to the account in question, and partially corroborated by independent media reporting on 2025 totals.
- Weaknesses: not the governing source of truth for settlement, imperfect visibility into inclusion/exclusion categories, and possible miss risk for short-lived deleted posts.