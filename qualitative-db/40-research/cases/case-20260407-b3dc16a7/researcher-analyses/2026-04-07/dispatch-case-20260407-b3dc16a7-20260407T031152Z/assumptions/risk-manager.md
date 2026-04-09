---
type: assumption_note
case_key: case-20260407-b3dc16a7
dispatch_id: dispatch-case-20260407-b3dc16a7-20260407T031152Z
research_run_id: bad9a67d-7650-43cf-b457-2a037e49c83e
analysis_date: 2026-04-07
persona: risk-manager
domain: politics
subdomain: social-media
entity: donald-trump
topic: will-donald-trump-post-80-99-truth-social-posts-from-march-31-to-april-7-2026
question: "Will Donald Trump post 80-99 Truth Social posts from March 31 to April 7, 2026?"
driver: operational-risk
date_created: 2026-04-07T03:12:00Z
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: intraday
related_entities: ["donald-trump"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260407-b3dc16a7/researcher-analyses/2026-04-07/dispatch-case-20260407-b3dc16a7-20260407T031152Z/personas/risk-manager.md"]
tags: ["assumption", "tracker", "truth-social"]
---

# Assumption

The XTracker count of 77 at audit time is directionally reliable enough that the remaining question is mainly whether Trump adds at least three more countable in-window posts before noon ET, not whether the tracker is already off by several countable posts.

## Why this assumption matters

The market is in a narrow band near the threshold. If the tracker is already undercounting by 3+ countable posts, the market could already be effectively in-range; if not, the probability depends on remaining intraday posting behavior.

## What this assumption supports

- A moderate-to-high probability on Yes rather than an almost certain Yes.
- Emphasis on late-window path risk and classification risk rather than assuming the threshold has already been safely cleared.
- Treating tracker integrity as important but not currently broken.

## Evidence or logic behind the assumption

- XTracker stats endpoint and raw posts endpoint both returned 77 for the same window.
- The tracked user identity matches verified `@realDonaldTrump` on Truth Social.
- Secondary archive review supports high activity and correct account identity, but did not reveal obvious missing clusters of countable in-window posts.
- Much of the archive-vs-tracker gap is explainable by pre-window posts and hard-to-classify repost/media items rather than a clear tracker miss.

## What would falsify it

- Evidence that several countable main-feed or quote/repost items from after Mar 31 noon ET are present on Truth Social/archive but absent from XTracker.
- A late tracker correction jumping the count by several posts without corresponding new posting activity.
- Resolver guidance or market history indicating XTracker routinely omits a meaningful class of countable Truth Social items in this exact market family.

## Early warning signs

- Archive/manual feed review shows multiple noon-to-noon items that cannot be matched to the XTracker export.
- XTracker sync lag widens materially near the close.
- Confusion appears around blank-content items, which may represent countable media posts or reposts.

## What changes if this assumption fails

If XTracker is undercounting materially, the probability on Yes should move sharply upward because the market may already be inside the 80-99 band even before the final morning activity.

## Notes that depend on this assumption

- Main risk-manager finding for this dispatch.
- Any synthesis that interprets the current sub-80 count as meaningfully below threshold rather than potentially stale.