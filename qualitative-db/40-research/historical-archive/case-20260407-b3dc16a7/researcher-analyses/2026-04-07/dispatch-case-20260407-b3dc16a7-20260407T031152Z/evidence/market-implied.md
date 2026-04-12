---
type: evidence_map
case_key: case-20260407-b3dc16a7
dispatch_id: dispatch-case-20260407-b3dc16a7-20260407T031152Z
research_run_id: f2425e82-bb01-41d5-b9b4-42d6a641e514
analysis_date: 2026-04-07
persona: market-implied
domain: politics
subdomain: trump
entity: donald-trump
topic: will-donald-trump-post-80-99-truth-social-posts-from-march-31-to-april-7-2026
question: "Will Donald Trump post 80-99 Truth Social posts from March 31 to April 7, 2026?"
driver: reliability
date_created: 2026-04-07
agent: market-implied
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["donald-trump"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260407-b3dc16a7/researcher-analyses/2026-04-07/dispatch-case-20260407-b3dc16a7-20260407T031152Z/personas/market-implied.md"]
tags: ["evidence-map", "tracker-audit", "truth-social"]
---

# Summary

The evidence leans to the market being directionally plausible but somewhat rich. The tracker count is close enough to the 80-99 band that a routine late burst can still get there, but the current count of 77 means the market is pricing a crossing that has not yet happened.

## Question being evaluated

Will Donald Trump finish the March 31, 12:00 PM ET to April 7, 12:00 PM ET window with 80-99 counted Truth Social posts under the market's counting rules?

## Current lean

Slight lean yes, but less confidently than the 71.5% market price implies.

## Prior / starting view

Starting from the market price, the sensible prior was that traders were probably incorporating both recent high posting activity and the fact that only three more qualifying posts were needed.

## Evidence supporting the claim

- XTracker, the named source of truth, already shows 77 counted posts in the target window. Only three more are needed to enter the band. This is direct evidence with heavy weight.
- Trump posted 17 counted items on April 6 ET within the window, showing recent activity is still elevated rather than fading to near zero. Direct evidence with medium weight.
- The prior weekly window returned 99 counted posts from the same account, which supports the idea that market participants may be using a high-activity prior rather than assuming a cold finish. Contextual evidence with medium weight.
- The exported/countable dataset contains a mix of text posts, link posts, quote-style items, and empty-body repost-like items, which matches the rule structure that multiple formats qualify. Direct rule-consistent evidence with medium weight.

## Evidence against the claim

- The target band has not yet been reached; the actual tracked total is still below 80 at 77. Direct evidence with heavy weight.
- There are only roughly eight hours remaining before noon ET resolution, so time-to-threshold is nontrivial even if only three more posts are needed. Direct timing evidence with medium-high weight.
- The market rules are exclusion-heavy. Replies generally do not count, deleted posts depend on tracker capture, and some tracker-classified items are opaque from the public schema. This raises interpretation and implementation risk. Direct rule/operational evidence with medium weight.
- The previous week finishing at 99 may be anchoring traders upward, but this week is currently 22 posts behind that pace. Contextual evidence with medium weight.

## Ambiguous or mixed evidence

- Empty-body posts in the tracker likely represent repost/media actions that count, but the schema does not label them perfectly.
- Some posts have notable `replies_count` metrics, but that does not mean the post itself is a reply; it only shows engagement and thus is not decisive for inclusion/exclusion.
- XTracker `percentComplete = 100` is not very informative before the window actually closes.

## Conflict between inputs

There is little factual conflict between the governing sources. The main uncertainty is interpretive: how much confidence to place in a market price that is above coin-flip when the live count still sits three posts short.

## Key assumptions

- XTracker is functioning correctly and remains the governing source through resolution.
- Trump will add at least a small number of qualifying posts before noon ET.
- No hidden tracker/reclassification issue materially changes the currently reported 77.

## Key uncertainties

- Overnight-to-morning posting intensity.
- Whether any marginal new activity falls into clearly countable formats.
- Whether tracker implementation edge cases affect the final few posts.

## Disconfirming signals to watch

- The xtracker total remains stuck at 77-79 deep into the morning.
- Late posts appear mainly as non-counting replies not surfaced on main feed.
- The tracker export or post counter begins lagging or diverging materially.

## What would increase confidence

- Observing the post counter tick to at least 80 before late morning ET.
- A cleaner public schema showing explicit per-post type classifications.
- Confirmation that no recent counted items are likely to be excluded on review.

## Net update logic

The market's core logic is understandable: only three more posts are needed, and Trump has recently posted at high enough volume to make that happen. But because the live tracked total is still below the bucket and the case has rule-sensitive counting criteria, the evidence supports a more tempered probability than the market price. The main downward adjustment is not from a contrarian thesis; it is from insisting on the live source-of-truth count and remaining time.

## Suggested downstream use

Use this as an orchestrator synthesis input and as an audit trail for why a mildly below-market probability was assigned despite the market remaining the directional prior.