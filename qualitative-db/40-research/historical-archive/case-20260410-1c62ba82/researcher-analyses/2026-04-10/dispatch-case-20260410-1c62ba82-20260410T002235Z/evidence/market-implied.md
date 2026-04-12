---
type: evidence_map
case_key: case-20260410-1c62ba82
dispatch_id: dispatch-case-20260410-1c62ba82-20260410T002235Z
research_run_id: cab4a1b2-b066-4160-a364-4a3ec6921ac7
analysis_date: 2026-04-10
persona: market-implied
domain: politics
subdomain: social-media
entity: donald-trump
topic: trump-truth-social-post-count-april-3-to-april-10-2026
question: "Will Donald Trump post 100-119 Truth Social posts from April 3 to April 10, 2026?"
driver: reliability
date_created: 2026-04-10
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["donald-trump"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "tracker", "truth-social", "post-count"]
---

# Summary

The market looks directionally right to make 100-119 the favorite because the designated tracker already showed 103 in-window posts before the final overnight-to-noon stretch. The main risk is not undercount but overshoot above 119 if Trump keeps posting at a brisk pace into the deadline.

## Question being evaluated

Will Donald Trump post 100-119 Truth Social posts between April 3, 12:00 PM ET and April 10, 12:00 PM ET under the contract’s counting rules?

## Current lean

Lean yes / in-range, but with substantial overshoot risk; roughly agree with the market, slightly less bullish than price.

## Prior / starting view

The 0.81 market price implies the crowd thinks the running count is already near or inside range and that remaining time is more likely to preserve the band than to produce a large overshoot.

## Evidence supporting the claim

- XTracker is the contract’s primary resolution source and exposed the exact April 3-April 10 tracking window plus a live post list. Direct. High weight.
- The XTracker posts endpoint returned 103 posts already inside the target bucket by about 20:20 ET on April 9. Direct. Very high weight.
- Poster identity cross-check: XTracker user object, Truth Social profile metadata, and archive site all point to Donald J. Trump / `@realDonaldTrump`. Direct/contextual mix. Medium weight.
- Independent archive (`trumpstruth.org`) displayed the same latest posts seen in XTracker, reducing wrong-account / phantom-data risk. Contextual corroboration. Medium weight.

## Evidence against the claim

- There were still roughly 11.5 hours remaining after the 103-count snapshot, leaving ample time for Trump to overshoot 119. Direct timing consideration. High weight.
- The tracker/public docs do not fully expose how main-feed versus reply-only classification is handled at the per-record level in the public API, leaving some rule-audit ambiguity. Indirect but relevant. Medium weight.
- Deleted-post treatment depends on tracker capture lasting ~5 minutes; that introduces operational edge-case risk. Contractual / process risk. Low-to-medium weight.

## Ambiguous or mixed evidence

- Some returned posts have empty `<p></p>` content, which may still count if they are reposts or other main-feed objects, but are harder to classify manually from API text alone.
- The market may be pricing not only current count but also Trump’s typical late-cycle posting cadence; without a full intraday pace model, this remains a judgment call.

## Conflict between inputs

No major factual conflict. The main issue is weighting-based: whether to emphasize the already-in-range count or the remaining-time overshoot risk.

## Key assumptions

- The tracker’s 103 count is directionally reliable.
- Remaining uncertainty is dominated by future posting pace rather than a hidden recount.
- Fallback to Truth Social is unlikely to be needed.

## Key uncertainties

- Final overnight and morning posting volume before noon ET.
- Edge-case handling for replies recorded on main feed.
- Whether any very short-lived deleted posts were missed or any current items later disappear from the displayed tracker output.

## Disconfirming signals to watch

- A burst of 17+ additional countable posts before noon ET, pushing total above 119.
- Evidence of tracker misclassification or outage.
- A fallback-to-platform resolution path with a materially different total.

## What would increase confidence

- Another tracker check closer to noon ET showing total still within band.
- Cleaner public documentation or export labeling for replies/reposts/quotes.
- A direct platform-accessible feed view that matches tracker latest entries one-for-one.

## Net update logic

Starting from the market prior, the key update is that the publicly queryable tracker already had the count at 103, which strongly validates why the market is so confident. I still discount the price modestly because 0.81 leaves limited room for the very real overshoot mechanism with almost half a day remaining.

## Suggested downstream use

Use as orchestrator synthesis input and forecast update context, with emphasis on: market probably right to favor this bucket, but remaining edge mostly lives in modeling overshoot risk rather than disputing current count integrity.