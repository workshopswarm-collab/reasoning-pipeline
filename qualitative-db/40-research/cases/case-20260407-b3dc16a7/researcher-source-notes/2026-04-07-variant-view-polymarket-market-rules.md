---
type: source_note
case_key: case-20260407-b3dc16a7
dispatch_id: dispatch-case-20260407-b3dc16a7-20260407T031152Z
analysis_date: 2026-04-07
persona: variant-view
domain: politics
subdomain: social-media
entity: donald-trump
topic: case-20260407-b3dc16a7 | variant-view
question: Will Donald Trump post 80-99 Truth Social posts from March 31 to April 7, 2026?
driver: operational-risk
date_created: 2026-04-06T23:13:00-04:00
source_name: Polymarket market page for Trump Truth Social post-count market
source_type: market rules / resolution text
source_url: https://polymarket.com/event/donald-trump-of-truth-social-posts-march-31-april-7
source_date: 2026-04-07
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [donald-trump]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260407-b3dc16a7/researcher-analyses/2026-04-07/dispatch-case-20260407-b3dc16a7-20260407T031152Z/personas/variant-view.md]
tags: [market-rules, resolution-criteria, truth-social, xtracker]
---

# Summary

The market rules are unusually important here because the contract is narrow, date-specific, and explicitly allows a tracker behavior that can diverge from a plain-language reading of "replies do not count."

## Key facts extracted

- The market resolves on the number of Donald Trump (@realDonaldTrump) Truth Social posts between March 31, 2026 12:00 PM ET and April 7, 2026 12:00 PM ET.
- Counted content includes main feed posts, quote posts, and reposts.
- Replies do not count, but replies that are recorded on the main feed will be counted by the tracker.
- Deleted posts count if they remain available long enough to be captured by the tracker, approximately five minutes.
- The governing source of truth is the XTracker "Post Counter" figure.
- Truth Social itself is only a secondary resolution source if the tracker fails to update correctly according to the rules.

## Evidence directly stated by source

The source directly states both the inclusion/exclusion rules and the settlement hierarchy: XTracker first, Truth Social second if tracker behavior is incorrect.

## What is uncertain

- The rules do not specify how often XTracker refreshes or whether users can independently inspect the exact counter history without the app rendering properly.
- The reply exclusion language is internally awkward because some replies can still count if surfaced on the main feed by the tracker.
- The deletion rule creates a capture-window dependency rather than a purely platform-native count.

## Why this source may matter

This is the governing contract. The market can resolve differently from a naive manual count on Truth Social if the tracker captures main-feed replies or captures posts later deleted.

## Possible impact on the question

This source makes tracker mechanics and auditability as important as Trump posting behavior itself. Any estimate near the 80-99 band has to account for operational counting edge cases, not just expected posting frequency.

## Reliability notes

High reliability for contract interpretation because this is the market's own resolution text. Lower reliability for actually reconstructing the live count, because the source delegates that to XTracker.