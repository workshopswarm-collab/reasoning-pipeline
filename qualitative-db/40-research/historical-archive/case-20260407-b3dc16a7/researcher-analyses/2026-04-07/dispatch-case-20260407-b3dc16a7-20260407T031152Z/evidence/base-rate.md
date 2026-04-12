---
type: evidence_map
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
status: draft
confidence: medium
conflict_status: moderate
action_relevance: high
related_entities: ["donald-trump"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260407-b3dc16a7/researcher-analyses/2026-04-07/dispatch-case-20260407-b3dc16a7-20260407T031152Z/personas/base-rate.md"]
tags: ["evidence-map", "tracker-audit", "truth-social"]
---

# Summary

Netting the evidence yields a slightly-bearish view on the 80-99 bucket versus market. The exact-window independent archive count sits at 79, but settlement mechanics could still push the governing tracker into the band.

## Question being evaluated

Will Donald Trump post 80-99 Truth Social posts from March 31, 2026 12:00 PM ET to April 7, 2026 12:00 PM ET?

## Current lean

Slight lean against 80-99, but not by much.

## Prior / starting view

Starting outside-view prior was that 80-99 looked plausible but somewhat low given Trump’s 2025 average of about 17-18 posts per day and several recent 7-day windows above 100.

## Evidence supporting the claim

- Exact-window independent archive count of 79 is only one post below the target band if one or more additional included posts appear before noon ET cutoff or if xtracker is slightly more inclusive. Direct; high weight.
- Market rules count main-feed posts, quote posts, and reposts, not just original text posts. If xtracker captures a few repost/quote/deleted items the independent archive underrepresents, 80-99 becomes quite plausible. Direct-on-rules but indirect on realized count; medium weight.
- Trump’s broader posting behavior often clusters in bursts, so an 80-99 weekly total is not an extreme outlier. Contextual; medium weight.

## Evidence against the claim

- Independent archive count in the full stated market window is 79, which is outside the band as counted. Direct; high weight.
- Twelve prior 7-day windows before the target averaged 132.25 posts, suggesting the 80-99 bucket may actually be below his more recent typical pace rather than the center of it. Contextual; medium weight.
- Source-of-truth ambiguity adds downside risk: if the archive is already close to xtracker, then 71.5% market confidence looks too high for a bucket currently sitting just above observed independent count. Mixed direct/contextual; medium weight.

## Ambiguous or mixed evidence

- Deleted posts count only if captured for about five minutes by the tracker. This can add small count differences in either direction depending on what the archive catches.
- Replies do not count, but replies recorded on the main feed do count by tracker behavior. That creates a category-definition ambiguity that can matter by a few posts.
- Poster identity risk is low because both governing and backup sources target @realDonaldTrump, but operational posting by aides muddies authorship in a human sense even if not in account-identity terms.

## Conflict between inputs

- The main disagreement is not factual identity but source-definition mismatch: independent archive count says 79, while market pricing implies the governing tracker likely lands in 80-99.
- This is partly factual and partly rule-interpretive.
- The best resolving evidence would be the actual xtracker export data or post counter reading near settlement.

## Key assumptions

- The independent archive is directionally representative of xtracker’s included-post logic.
- No large late posting burst occurs before the noon ET cutoff.

## Key uncertainties

- Exact xtracker count near settlement
- Inclusion of reposts / quote posts / main-feed replies in tracker vs archive
- Whether any deleted posts were captured by xtracker but missed elsewhere

## Disconfirming signals to watch

- xtracker export clearly above 80 before noon ET
- Evidence of multiple included reposts/quote posts absent from the archive
- Morning posting burst on Apr 7 before cutoff

## What would increase confidence

- Direct xtracker export or post-counter snapshot
- Secondary independent dataset that explicitly labels reposts and replies
- Confirmation from Truth Social main feed for any disputed rows

## Net update logic

The outside view alone would not make 80-99 look crazy, but the direct independent count being 79 is the most decision-relevant evidence. That pulled the estimate below market. I downweighted vivid single-day posting spikes because the current realized window matters more than generic capacity for bursts.

## Suggested downstream use

Use as orchestrator synthesis input and as an audit note explaining why a base-rate persona stayed below market despite acknowledging tracker-rule upside.