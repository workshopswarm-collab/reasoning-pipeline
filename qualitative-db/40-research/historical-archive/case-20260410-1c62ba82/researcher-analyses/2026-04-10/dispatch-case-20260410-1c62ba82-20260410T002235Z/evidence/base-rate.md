---
type: evidence_map
case_key: case-20260410-1c62ba82
dispatch_id: dispatch-case-20260410-1c62ba82-20260410T002235Z
research_run_id: df6e1f0b-3e0c-46fd-aa3f-d095618d8c35
analysis_date: 2026-04-10
persona: base-rate
domain: politics
subdomain: social-media
entity: donald-trump
topic: trump-truth-social-post-count
question: "Will Donald Trump post 100-119 Truth Social posts from April 3 to April 10, 2026?"
driver: reliability
date_created: 2026-04-09
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["donald-trump"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260410-1c62ba82/researcher-analyses/2026-04-10/dispatch-case-20260410-1c62ba82-20260410T002235Z/personas/base-rate.md"]
tags: ["evidence-map", "truth-social", "xtracker", "post-count"]
---

# Summary

The evidence leans clearly toward Yes because the contract’s named tracker currently reports 103 posts in the exact window. The remaining issue is not directional uncertainty about Trump’s posting rate, but implementation risk around exclusion rules and tracker correctness.

## Question being evaluated

Will Donald Trump post 100-119 Truth Social posts from April 3, 2026 12:00 PM ET to April 10, 2026 12:00 PM ET under the contract’s counting rules?

## Current lean

Yes, with fairly high confidence but not full certainty.

## Prior / starting view

Outside-view prior: Trump often posts at high volume on Truth Social, so 100-119 in a 7-day noon-to-noon window is plausible on base rates alone. But rule-sensitive counting markets can resolve against narrative expectations if replies, deleted posts, or identity mismatches are mishandled.

## Evidence supporting the claim

- XTracker tracking stats for the exact market window show `total = 103`.
  - Source: source note `2026-04-10-base-rate-xtracker-trump-count-window.md`
  - Why it matters: direct resolution evidence from the named source of truth.
  - Direct vs indirect: direct.
  - Weight: very high.

- XTracker user endpoint confirms the tracked account is `realDonaldTrump`, `Donald J. Trump`, `TRUTH_SOCIAL`, verified, with the matching platform id.
  - Source: same source note.
  - Why it matters: addresses poster identity and reduces risk of counting a wrong or spoofed feed.
  - Direct vs indirect: direct.
  - Weight: high.

- XTracker posts endpoint returns post-level records from the relevant window, showing the tracker has underlying exported data and not just a synthetic headline statistic.
  - Source: same source note.
  - Why it matters: improves auditability and supports deleted-post capture logic.
  - Direct vs indirect: direct.
  - Weight: medium-high.

- Base-rate/context: weekly Trump Truth Social markets recur because his posting frequency is regularly high enough for these buckets to be live possibilities, so a 103 total is not an outlier requiring an exotic story.
  - Source: XTracker user tracking history and Polymarket market framing.
  - Why it matters: supports the outside-view plausibility of the bucket.
  - Direct vs indirect: contextual.
  - Weight: medium.

## Evidence against the claim

- The contract excludes replies unless they are recorded on the main feed; the public API output I saw did not expose an obvious field classifying each returned item as reply vs main-feed post.
  - Why it matters: a rule-implementation bug could contaminate the total.
  - Direct vs indirect: indirect challenge to source integrity.
  - Weight: medium.

- Deleted posts count only if captured by the tracker for long enough. That means Truth Social itself is not a perfect fallback for a later recount if some posts disappeared.
  - Why it matters: limits independent verification.
  - Direct vs indirect: direct contract caveat.
  - Weight: low-medium.

- I did not perform a full 103-item manual recount from exported data.
  - Why it matters: residual audit gap remains.
  - Direct vs indirect: process limitation.
  - Weight: low-medium.

## Ambiguous or mixed evidence

- Truth Social public web access is partially JS-rendered and its unauthenticated API access is constrained, which makes direct independent recounting cumbersome. That does not contradict the tracker, but it limits independence.

## Conflict between inputs

No material factual conflict found. The issue is mainly weighting and implementation risk, not source disagreement.

## Key assumptions

- The tracker implements the market rules correctly enough.
- Any residual counting error is smaller than the distance from the bucket edge.

## Key uncertainties

- Exact treatment of replies that appear on the main feed.
- Whether any late tracker correction occurs before resolution.
- Whether there are enough hidden or misclassified posts to move the total out of range.

## Disconfirming signals to watch

- Tracker count revision below 100 or above 119.
- Evidence of many reply-only objects being counted.
- Polymarket or tracker notice of sync/capture failure.

## What would increase confidence

- Full export-data pull for the exact tracking id.
- A direct independent recount from tracker-exported records with reply/main-feed labels.
- A clearer public API field identifying reposts, quote posts, and replies.

## Net update logic

Starting from a moderate outside-view expectation that a high-posting Trump week could plausibly land near this bucket, the exact tracker total of 103 moved the case strongly toward Yes. The main remaining deduction is not about the behavioral base rate but about narrow rule implementation and verification limits.

## Suggested downstream use

Use this as a synthesis input favoring a Yes lean, while keeping a modest discount for tracker-rule implementation risk rather than treating the count as perfectly audit-proof.