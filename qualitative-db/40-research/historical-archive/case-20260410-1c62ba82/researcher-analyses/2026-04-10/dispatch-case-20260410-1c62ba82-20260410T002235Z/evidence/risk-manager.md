---
type: evidence_map
case_key: case-20260410-1c62ba82
dispatch_id: dispatch-case-20260410-1c62ba82-20260410T002235Z
research_run_id: b83cd796-c912-417b-8f06-180333bca7de
analysis_date: 2026-04-10
persona: risk-manager
domain: politics
subdomain: social-media
entity: donald-trump
topic: will-donald-trump-post-100-119-truth-social-posts-from-april-3-to-april-10-2026
question: "Will Donald Trump post 100-119 Truth Social posts from April 3 to April 10, 2026?"
driver: operational-risk
date_created: 2026-04-10
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low-to-medium
action_relevance: high
related_entities: ["donald-trump", "truth-social"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260410-1c62ba82/researcher-analyses/2026-04-10/dispatch-case-20260410-1c62ba82-20260410T002235Z/personas/risk-manager.md"]
tags: ["evidence-map", "counting-market", "xtracker"]
---

# Summary

The net evidence favors a current Yes lean because the governing source already shows 103 counted posts in the exact window, but the edge is not clean enough for extreme confidence because the market remains open and raw captured-post totals do not perfectly match the official counter.

## Question being evaluated

Will Donald Trump post 100-119 Truth Social posts from Apr 3 2026 12:00 PM ET through Apr 10 2026 12:00 PM ET under the market's counting rules?

## Current lean

Lean Yes, with the main risk being overshoot above 119 before the window closes.

## Prior / starting view

Starting view was that a market at 0.81 likely reflected a count already near or inside the band, but rule ambiguity and late-window burst risk could still be underpriced.

## Evidence supporting the claim

- XTracker stats endpoint for the exact market-linked period returns `totalBetweenStartAndEnd = 103`.
  - Direct, authoritative-for-settlement evidence.
  - Very high weight.
- The XTracker user endpoint identifies the tracked account as verified `Donald J. Trump` / `realDonaldTrump` on Truth Social and links the exact market period.
  - Direct identity and mapping evidence.
  - High weight.
- The contract page explicitly says XTracker's post counter is the primary resolution source.
  - Direct rules evidence.
  - High weight.
- Daily tracker counts sum neatly to 103, which suggests an internally consistent counted total rather than an obviously stale or malformed snapshot.
  - Direct tracker-consistency evidence.
  - Medium weight.

## Evidence against the claim

- The market remains open until noon ET Apr 10, so 103 is not final and a moderate posting burst could still push the total above 119.
  - Direct timing risk.
  - High weight.
- The public posts endpoint returned 105 captured posts for the same window, versus 103 on the official counter.
  - Direct evidence of inclusion/exclusion ambiguity.
  - Medium-high weight.
- The rules allow deleted posts to count if captured and exclude replies unless they are recorded on the main feed, which means settlement can diverge from a simple visible-feed audit.
  - Direct contract-risk evidence.
  - Medium weight.

## Ambiguous or mixed evidence

- Truth Social profile fetch confirms the `@realDonaldTrump` account exists, but the public HTML fetch is too thin to independently audit the full counted set or classify posts cleanly.
- The raw posts endpoint includes many empty-content rows and no obvious classification field, which is consistent with repost/quote/deleted-post capture but not self-explanatory.

## Conflict between inputs

- Factual disagreement is small but real: raw captured posts endpoint yielded 105 rows, while the official counter is 103.
- This appears to be a rule-filtering or classification issue rather than a broad source conflict.
- The next evidence that would resolve it would be either an export-data surface with explicit counted/not-counted labels or a final tracker snapshot at resolution.

## Key assumptions

- The official counter remains the governing source because the tracker appears functional.
- Late-window posting volume is not large enough to overshoot 119.
- The current 103 figure is not about to be revised sharply downward by reclassification.

## Key uncertainties

- How many additional counted posts occur before noon ET.
- Which exact raw posts are excluded from the official count and why.
- Whether any deletions or borderline reply/main-feed items create a late settlement dispute.

## Disconfirming signals to watch

- Tracker total rises into the high teens above 103 before noon ET.
- Public evidence of a tracker malfunction or stale syncing.
- Platform-side review suggests many currently counted items are actually non-counting replies.

## What would increase confidence

- Another tracker update still keeping the total in the low 100s close to noon ET.
- Better export visibility showing why raw 105 maps to official 103.
- Independent platform audit confirming that the counted set is overwhelmingly main-feed posts, reposts, or quote posts.

## Net update logic

The main update is that the question is no longer about whether Trump is remotely close to the target band; he is already in it on the governing source. That pushes strongly toward Yes. The remaining risk-manager adjustment is to trim confidence because the market is still live and the counting mechanics are not fully transparent from public raw-post data.

## Suggested downstream use

- Forecast update.
- Orchestrator synthesis input.
- Final pre-resolution monitoring if another pass is run near noon ET.