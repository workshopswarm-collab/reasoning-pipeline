---
type: source_note
case_key: case-20260410-1c62ba82
dispatch_id: dispatch-case-20260410-1c62ba82-20260410T002235Z
analysis_date: 2026-04-10
persona: catalyst-hunter
domain: politics
subdomain: social-media-monitoring
entity: donald-trump
topic: trump-truth-social-post-count-apr3-apr10
question: Will Donald Trump post 100-119 Truth Social posts from April 3 to April 10, 2026?
driver: reliability
date_created: 2026-04-10
source_name: Truth Social public profile and independent archive mirror
source_type: platform-and-archive
source_url: https://truthsocial.com/@realDonaldTrump
source_date: 2026-04-10
credibility: medium
recency: current
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: Orchestrator
related_entities: [donald-trump]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260410-1c62ba82/researcher-analyses/2026-04-10/dispatch-case-20260410-1c62ba82-20260410T002235Z/personas/catalyst-hunter.md]
tags: [truth-social, identity-check, archive-check]
---

# Summary

A secondary verification pass confirmed that the Truth Social profile page is for Donald J. Trump / @realDonaldTrump and that an independent archive mirror reproduces contemporaneous posts seen in the XTracker feed.

## Key facts extracted

- The public Truth Social profile page title resolves to `Donald J. Trump (@realDonaldTrump)`.
- XTracker’s user endpoint identifies the same handle as verified and gives the Truth Social platformId `107780257626128497`.
- An independent archive mirror, Trump's Truth, displayed the same late-window posts visible in the XTracker posts endpoint, including the April 9 posts on Hungary/Viktor Orbán, Elise Stefanik’s book, Benjamin Flowers, and several Iran-related posts.
- The archive mirror therefore supports that the tracked feed is the real Trump account and that at least a sample of the counted late-window posts existed outside the tracker itself.

## Evidence directly stated by source

- Truth Social directly identifies the profile as Donald J. Trump (@realDonaldTrump).
- The archive mirror displays contemporaneous post text matching the tracker feed.

## What is uncertain

- The public Truth Social page was JS-heavy, so this pass did not produce a convenient direct count from the platform itself.
- The archive mirror is not the governing source and may inherit data from scraping or delayed replication.
- This pass cannot independently audit whether replies are excluded in every edge case; it only confirms identity and cross-surface consistency for sampled posts.

## Why this source may matter

This secondary source is useful for the contract’s fallback logic and for the case-specific requirement to verify poster identity and cross-reference tracker versus platform/secondary archive.

## Possible impact on the question

It increases confidence that XTracker is following the correct Donald Trump account and that the late-window post activity is real rather than a tracker-only artifact.

## Reliability notes

- Truth Social identity check is high relevance but low extraction depth because of the JS shell.
- The archive mirror is independent enough to improve confidence modestly, but not strong enough to override XTracker if the two diverged.
