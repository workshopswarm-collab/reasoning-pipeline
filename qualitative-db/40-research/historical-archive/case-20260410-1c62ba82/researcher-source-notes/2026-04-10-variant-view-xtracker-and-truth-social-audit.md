---
type: source_note
case_key: case-20260410-1c62ba82
dispatch_id: dispatch-case-20260410-1c62ba82-20260410T002235Z
research_run_id: bb69cc11-7243-4a63-98d1-08d27a36a2d1
analysis_date: 2026-04-10
persona: variant-view
source_type: mixed
source_name: XTracker frontend/API plus Truth Social public surfaces and archive references
source_url: https://xtracker.polymarket.com
confidence: medium
tags: [xtracker, truth-social, resolution-mechanics, provenance]
---

# Summary

This note audits the governing resolution surfaces rather than trying to finish an exact count from scratch. The key takeaway is that the market is governed first by XTracker's post counter, but XTracker currently exposes a public `/api/users` feed and frontend code that confirm broad mechanics while not trivially exposing the exact Trump counter through a simple unauthenticated endpoint. Truth Social public web pages confirm account identity (`Donald J. Trump (@realDonaldTrump)`), while independent archive/search results from Trump's Truth confirm that Trump had multiple April 3, 2026 posts visible in the relevant window and that removed posts may persist in third-party archives.

# What was checked

## XTracker

- `https://xtracker.polymarket.com` loaded successfully.
- Frontend JS chunk inspection showed the landing page uses `fetch('/api/users')` and computes top-level stats from returned user objects.
- Public unauthenticated `GET /api/users` returned real user tracking objects for other monitored accounts, confirming this is a live tracker API rather than a placeholder page.
- The same API output observed in this session did not immediately include `realDonaldTrump`, which raises an operational caveat: the public API surface is incomplete or paginated, so a reviewer should not infer absence of Trump tracking from that endpoint alone.

## Truth Social

- `https://truthsocial.com/@realDonaldTrump` loaded and exposed page title metadata `Donald J. Trump (@realDonaldTrump)`, supporting poster-identity verification for the target handle.
- Direct unauthenticated API lookup to Truth Social account endpoints returned `403 Forbidden`, so the platform is not easily queryable through a clean public JSON endpoint in this environment.

## Independent contextual archive

- DuckDuckGo surfaced Trump's Truth pages for April 3, 2026 entries, including snippets labeled `Original Post` and `ReTruthed Donald J. Trump @ realDonaldTrump`.
- This is useful as contextual corroboration that the account was actively posting/reposting in the target week and that third-party archives can preserve deleted or removed items.

# Why it matters

The contract is count-sensitive and exclusion-heavy. The main variant concern is not that Trump suddenly stopped posting, but that the market may be overconfident about a narrow 100-119 bucket when the governing tracker/platform surfaces have operational and interpretation ambiguity around:

- replies that appear on the main feed,
- deleted posts that only count if captured,
- repost/quote treatment,
- and the practical opacity of public Truth Social data access.

# Reliability / limitations

- Strong on resolution mechanics and identity verification.
- Weaker on exact total count because the exact Trump tracker export was not directly retrievable from a simple public endpoint during this run.
- Archive snippets are contextual, not authoritative settlement evidence by themselves.

# Bottom line

This source set supports a cautious variant stance: the market's high confidence in a narrow band should be discounted somewhat unless the exact XTracker export for Trump is checked directly near resolution.