---
type: source_note
case_key: case-20260410-1c62ba82
dispatch_id: dispatch-case-20260410-1c62ba82-20260410T002235Z
analysis_date: 2026-04-10
persona: risk-manager
domain: politics
subdomain: social-media
entity: donald-trump
topic: case-20260410-1c62ba82 | risk-manager
question: Will Donald Trump post 100-119 Truth Social posts from April 3 to April 10, 2026?
driver: operational-risk
date_created: 2026-04-10
source_name: XTracker API docs and live user/stats endpoints
source_type: tracker_api_and_docs
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
downstream_uses: [qualitative-db/40-research/cases/case-20260410-1c62ba82/researcher-analyses/2026-04-10/dispatch-case-20260410-1c62ba82-20260410T002235Z/personas/risk-manager.md]
tags: [xtracker, truth-social, resolution-source, source-note]
---

# Summary

XTracker is the governing resolution source for this market, and its public docs plus live API endpoints allow a direct check of both the exact tracking window and the tracked user identity. The key risk-relevant result is that the documented stats endpoint returns `totalBetweenStartAndEnd: 103` for the exact market window tied to the market URL, which falls inside the 100-119 band.

## Key facts extracted

- XTracker docs say the API supports Truth Social and stores dates in UTC while tracking periods are defined in EST / America-New_York.
- The public `/api/users/realDonaldTrump?platform=TRUTH_SOCIAL` endpoint identifies the tracked user as `Donald J. Trump`, handle `realDonaldTrump`, verified true, platform `TRUTH_SOCIAL`.
- That same endpoint lists the exact tracking object for this market: `Donald Trump # Truth Social posts April 3 - April 10, 2026?` with market link `https://polymarket.com/event/donald-trump-of-truth-social-posts-april-3-april-10` and dates `2026-04-03T16:00:00.000Z` to `2026-04-10T15:59:59.000Z`.
- The legacy stats endpoint `/api/users?platform=TRUTH_SOCIAL&stats=true&includeInactive=true` returns for that exact market window `tweetData.totalBetweenStartAndEnd = 103`.
- The same stats payload gives daily counts of 6, 9, 11, 19, 37, 10, and 11 for Apr 3 through Apr 9, summing to 103.
- A direct posts endpoint for the same window returned 105 captured posts, not 103, indicating that raw captured posts can exceed the official counter used for settlement.
- The posts endpoint schema exposed only basic fields (`content`, `createdAt`, `metrics`, etc.) and did not clearly label which posts were excluded from the official counter, leaving some rule-application opacity.

## Evidence directly stated by source

- XTracker docs: base URL `https://xtracker.polymarket.com/api`; Truth Social supported; date filtering available; tracking periods defined in EST.
- Live stats endpoint: exact market-linked tracking period exists and official aggregate count is 103 so far.
- Live user endpoint: tracked poster identity matches `@realDonaldTrump` on Truth Social and is marked verified.

## What is uncertain

- Public endpoints do not make fully explicit which two of the 105 captured posts were excluded from the official 103 counter.
- The posts endpoint does not clearly expose reply vs main-feed vs repost flags in the returned schema sample I pulled, so rule application is only partially auditable from the public surface.
- Because the market remains open until noon ET Apr 10, the 103 count can still rise materially before resolution.

## Why this source may matter

This is the source of truth named in the market rules, so it dominates all secondary interpretation. It also directly informs the main risk question: whether the market is underpricing late-window count drift or tracker-rule ambiguity.

## Possible impact on the question

As of the check time, the governing source points to a Yes-zone total of 103, which strongly supports a current Yes lean. The risk signal is not directional support for No, but rather procedural fragility: raw captured posts and official counted posts are not identical, so late resolution can still hinge on tracker-rule treatment and any additional overnight/morning posting burst.

## Reliability notes

- Strongest feature: this is the explicit resolution source and it exposes public docs plus live machine-readable endpoints.
- Main weakness: public auditability of inclusion/exclusion logic is incomplete because raw post rows do not clearly annotate why the official counter differs from the raw fetch count.
- Independence is limited because both docs and live count come from the same tracker operator, so a platform-side check remains useful as a fallback sanity check rather than a fully independent source.