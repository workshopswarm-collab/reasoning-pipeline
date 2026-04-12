---
type: assumption_note
case_key: case-20260407-b3dc16a7
dispatch_id: dispatch-case-20260407-b3dc16a7-20260407T031152Z
research_run_id: d17a6871-ef15-45ce-893c-472f2458eed0
analysis_date: 2026-04-07
persona: base-rate
domain: politics
subdomain: social-media
entity: donald-trump
topic: will-donald-trump-post-80-99-truth-social-posts-from-march-31-to-april-7-2026
question: "Will Donald Trump post 80-99 Truth Social posts from March 31 to April 7, 2026?"
driver: reliability
date_created: 2026-04-07
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: days
related_entities: ["donald-trump"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260407-b3dc16a7/researcher-analyses/2026-04-07/dispatch-case-20260407-b3dc16a7-20260407T031152Z/personas/base-rate.md"]
tags: ["assumption", "tracker-audit", "truth-social"]
---

# Assumption

The independent CNN Truth Social archive is close enough to xtracker’s included-post logic that an archive count of 79 implies the market bucket 80-99 is only slightly above the current independent baseline rather than wildly mis-specified.

## Why this assumption matters

The base-rate view relies on using an independent archive as an audit check on the governing tracker. If the archive materially undercounts reposts, quote posts, or short-lived deleted posts relative to xtracker, then the probability of landing in 80-99 rises.

## What this assumption supports

- A slightly-bearish-to-neutral stance on the 80-99 bucket despite a market price of 71.5%
- The interpretation that the market is leaning on tracker-specific inclusion logic and/or expectation of late additional posting, not just broad historical frequency

## Evidence or logic behind the assumption

- The archive is current through the target window and clearly tied to @realDonaldTrump.
- It includes rows suggestive of repost-like activity (for example rows beginning with "RT:") and media-only posts, so it is not obviously limited to text-only originals.
- Independent media summaries of Trump’s 2025 posting totals align closely with counts derived from the same archive, suggesting it is directionally representative of overall output.

## What would falsify it

- Exported xtracker data showing a materially higher included count in the same window, especially above 80 by several posts
- Evidence that the archive systematically excludes a category that xtracker includes, such as reposts or quote posts
- Evidence of many deleted posts captured by xtracker but absent from the archive

## Early warning signs

- Large mismatch between xtracker post counter and archive-derived counts
- Rule notes or product behavior indicating replies frequently surface on the main feed and are counted by xtracker in ways the archive misses
- Missing clusters of high-frequency repost bursts in the independent archive

## What changes if this assumption fails

If xtracker is materially more inclusive than the independent archive, my estimate should move upward toward or above market, because the 80-99 band could then be the modal outcome rather than just above current observed independent count.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260407-b3dc16a7/researcher-analyses/2026-04-07/dispatch-case-20260407-b3dc16a7-20260407T031152Z/personas/base-rate.md