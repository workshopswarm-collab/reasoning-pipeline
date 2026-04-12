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
driver: operational-risk
date_created: 2026-04-07
source_name: Polymarket market rules page
source_type: market-rules
source_url: https://polymarket.com/event/donald-trump-of-truth-social-posts-march-31-april-7
source_date: 2026-04-07
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: market-implied
related_entities: [donald-trump]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260407-b3dc16a7/researcher-analyses/2026-04-07/dispatch-case-20260407-b3dc16a7-20260407T031152Z/personas/market-implied.md]
tags: [polymarket, resolution-rules, truth-social, market-structure]
---

# Summary

The Polymarket market page provides the governing wording for what counts. It explicitly says the market resolves according to Donald Trump (`@realDonaldTrump`) Truth Social posts between March 31, 12:00 PM ET and April 7, 12:00 PM ET; only main feed posts, quote posts, and reposts count; replies do not count, except replies recorded on the main feed are counted by the tracker; deleted posts count if captured by the tracker for roughly five minutes; and the primary resolution source is the XTracker `Post Counter`, with Truth Social itself as a fallback if the tracker mis-updates.

## Key facts extracted

- Governing account: `Donald Trump (@realDonaldTrump)`.
- Governing window: March 31, 12:00 PM ET to April 7, 12:00 PM ET.
- Included post types: main feed posts, quote posts, reposts.
- Excluded post type: replies, except those recorded on the main feed and therefore counted by the tracker.
- Deleted-post treatment: count them if captured by the tracker long enough (~5 minutes).
- Primary resolution source: `Post Counter` at `https://xtracker.polymarket.com`.
- Secondary fallback source: Truth Social itself if tracker updates incorrectly relative to the stated rules.

## Evidence directly stated by source

The page directly defines the inclusion/exclusion rules and the hierarchy of settlement sources.

## What is uncertain

- The market rules do not explain exactly how the tracker operationally distinguishes a reply that appears on the main feed from a reply that should be excluded.
- The rules leave some implementation dependence on whether deleted posts remain captured long enough by the tracker.

## Why this source may matter

This source governs interpretation. For this case, the key edge is less about generic posting behavior and more about whether the live tracker count lines up with the contract's counting rules.

## Possible impact on the question

These rules make simple manual counting from the visible Truth Social profile insufficient on its own. The market should be expected to key primarily off xtracker's counted total rather than broad public impressions of how active Trump has been.

## Reliability notes

Highest relevance for rule interpretation because it is the market contract itself. It is not sufficient alone to answer the count question; it must be paired with the tracker or fallback source actually supplying the count.