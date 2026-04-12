---
type: source_note
case_key: case-20260410-1c62ba82
dispatch_id: dispatch-case-20260410-1c62ba82-20260410T002235Z
analysis_date: 2026-04-10
persona: risk-manager
domain: politics
subdomain: prediction-markets
entity: truth-social
topic: case-20260410-1c62ba82 | risk-manager
question: Will Donald Trump post 100-119 Truth Social posts from April 3 to April 10, 2026?
driver: operational-risk
date_created: 2026-04-10
source_name: Polymarket market rules page
source_type: market_contract_page
source_url: https://polymarket.com/event/donald-trump-of-truth-social-posts-april-3-april-10
source_date: 2026-04-10
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [truth-social, donald-trump]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260410-1c62ba82/researcher-analyses/2026-04-10/dispatch-case-20260410-1c62ba82-20260410T002235Z/personas/risk-manager.md]
tags: [polymarket, market-rules, resolution-source, source-note]
---

# Summary

The market rules sharply constrain what counts: only Donald Trump `@realDonaldTrump` Truth Social main-feed posts, quote posts, and reposts in the stated window count; replies do not count unless they are recorded on the main feed; deleted posts count only if the tracker captured them; and XTracker's Post Counter is the primary resolution source, with Truth Social itself as fallback only if the tracker fails.

## Key facts extracted

- Time window: Apr 3 2026 12:00 PM ET through Apr 10 2026 12:00 PM ET.
- Counted items: main feed posts, quote posts, reposts.
- Excluded by default: replies, except replies recorded on the main feed and therefore counted by the tracker.
- Deleted posts count if they remain up long enough to be captured by the tracker, roughly 5 minutes.
- Governing source of truth is the `Post Counter` at `https://xtracker.polymarket.com`.
- If the tracker does not update correctly in accordance with the rules, Truth Social itself may be used as a secondary resolution source.

## Evidence directly stated by source

The rules explicitly encode both the counting window and the hierarchy of evidence sources. They also make clear that the counted set is not just "all visible posts" but a rules-filtered subset.

## What is uncertain

- The rules do not define an easy public method for separating replies that are on the main feed from replies that are not, beyond trusting tracker behavior or manually auditing the platform.
- The rules permit deleted-post inclusion if tracker-captured, which creates a divergence risk between current platform visibility and eventual settlement count.
- The phrase "if the tracker does not update correctly" leaves some judgment room about when fallback to Truth Social becomes justified.

## Why this source may matter

This contract language governs both directional probability and risk analysis. In particular, it explains why a raw post scrape can differ from the official counted total and why late deletion or classification edge cases matter.

## Possible impact on the question

The rules make the current 103 tracker count highly relevant, but they also create tail risk around count interpretation, especially if additional posts appear close to the deadline or if borderline reply/main-feed cases emerge.

## Reliability notes

- Strong because it is the contract text for market settlement.
- Not independent from settlement mechanics because it delegates final counting to XTracker first.
- Main research use is as the governing interpretation layer rather than as numerical evidence by itself.