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
driver: reliability
date_created: 2026-04-06T23:13:30-04:00
source_name: Truth Social profile landing page for @realDonaldTrump
source_type: platform profile page
source_url: https://truthsocial.com/@realDonaldTrump
source_date: 2026-04-07
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: Orchestrator
related_entities: [donald-trump]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260407-b3dc16a7/researcher-analyses/2026-04-07/dispatch-case-20260407-b3dc16a7-20260407T031152Z/personas/variant-view.md]
tags: [identity-check, truth-social, profile, attribution]
---

# Summary

The Truth Social profile page resolves to a page titled "Donald J. Trump (@realDonaldTrump)," which supports the case-specific identity check, but the public HTML is mostly a shell and not a straightforward source for manual historical counting.

## Key facts extracted

- The public page at https://truthsocial.com/@realDonaldTrump resolves successfully.
- The page title and metadata identify the account as "Donald J. Trump (@realDonaldTrump)."
- The delivered HTML is app-shell heavy and does not expose an easy text-rendered timeline in the fetched response.

## Evidence directly stated by source

The account identity in page metadata is directly stated.

## What is uncertain

- The fetched page does not provide a reliable manual count of posts in the relevant window without client-side execution or authenticated scraping.
- The page alone does not reveal whether deleted posts occurred or how quote-post / repost distinctions are surfaced for counting.

## Why this source may matter

It helps verify poster identity, which is an explicit checklist item. It also confirms why the market relies on XTracker as the primary settlement source: Truth Social itself is not trivially auditable from lightweight fetches.

## Possible impact on the question

The identity check supports the entity attribution, but the limited observability of the raw platform increases dependence on tracker correctness and therefore increases operational ambiguity around a narrow numerical band market.

## Reliability notes

Moderately reliable for identity verification. Weak as a stand-alone counting source in this environment because the rendered timeline is not exposed in the fetched HTML.