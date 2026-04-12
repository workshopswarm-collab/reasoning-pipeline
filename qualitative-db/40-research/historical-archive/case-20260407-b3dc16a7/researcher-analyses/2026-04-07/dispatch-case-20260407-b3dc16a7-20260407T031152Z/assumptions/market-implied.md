---
type: assumption_note
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
status: active
certainty: medium
importance: high
time_horizon: intraday
related_entities: ["donald-trump"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260407-b3dc16a7/researcher-analyses/2026-04-07/dispatch-case-20260407-b3dc16a7-20260407T031152Z/personas/market-implied.md"]
tags: ["assumption", "tracker", "post-count"]
---

# Assumption

The market's 71.5% price is implicitly assuming that the last stretch before noon ET will add at least three more counted xtracker posts but not enough to push the total above 99.

## Why this assumption matters

The market is not pricing whether Trump has been active in general; it is pricing whether the current tracked total of 77 will cross into the 80-99 bucket before the window closes. The path dependence over the final hours is therefore the main remaining uncertainty.

## What this assumption supports

- Treating 80-99 as the modal outcome despite the current count still sitting below 80.
- Interpreting the market as expecting an ordinary overnight-to-morning burst rather than a major acceleration or total stall.
- A probability estimate moderately below the market rather than a near-zero or near-certain view.

## Evidence or logic behind the assumption

- XTracker currently shows 77 counted posts for the target window.
- Trump has posted 17 counted items on April 6 ET so far within the window, showing he remains active late in the period.
- The previous week finished at 99, so traders likely have a recent high-activity prior and may be anchoring to his capacity to post in bunches.
- Only three additional qualifying posts are needed to get into range.

## What would falsify it

- No additional qualifying posts before noon ET, leaving the final total below 80.
- A tracker issue or exclusion-rule reinterpretation that removes currently assumed qualifying items.
- An unusually intense posting burst that pushes the count above 99, though that now looks less likely from 77 with limited time left.

## Early warning signs

- The xtracker count remains flat through the late evening and early morning.
- New activity appears mostly in formats that may not be counted cleanly.
- Evidence of tracker lag or visible mismatch between exported posts and reported post counter.

## What changes if this assumption fails

If Trump does not add at least three more counted posts, the 80-99 bucket is overpriced. If the count accelerates dramatically beyond a normal closing burst, the concern shifts from undercount risk to overshooting above 99.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260407-b3dc16a7/researcher-analyses/2026-04-07/dispatch-case-20260407-b3dc16a7-20260407T031152Z/personas/market-implied.md
- qualitative-db/40-research/cases/case-20260407-b3dc16a7/researcher-analyses/2026-04-07/dispatch-case-20260407-b3dc16a7-20260407T031152Z/evidence/market-implied.md