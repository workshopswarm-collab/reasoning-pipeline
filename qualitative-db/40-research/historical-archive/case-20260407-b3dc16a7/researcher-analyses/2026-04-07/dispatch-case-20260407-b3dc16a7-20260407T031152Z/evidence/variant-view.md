---
type: evidence_map
case_key: case-20260407-b3dc16a7
dispatch_id: dispatch-case-20260407-b3dc16a7-20260407T031152Z
research_run_id: 3b617d66-f2a7-4c1d-937a-85733d320825
analysis_date: 2026-04-07
persona: variant-view
domain: politics
subdomain: social-media
entity: donald-trump
topic: will-donald-trump-post-80-99-truth-social-posts-from-march-31-to-april-7-2026
question: "Will Donald Trump post 80-99 Truth Social posts from March 31 to April 7, 2026?"
driver: operational-risk
date_created: 2026-04-06T23:14:30-04:00
agent: Orchestrator
status: draft
confidence: medium
conflict_status: "low-direct-data / medium-resolution-ambiguity"
action_relevance: high
related_entities: ["donald-trump"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260407-b3dc16a7/researcher-analyses/2026-04-07/dispatch-case-20260407-b3dc16a7-20260407T031152Z/personas/variant-view.md"]
tags: ["evidence-map", "tracker-audit", "rule-sensitive"]
---

# Summary

The variant lean is not based on a strong claim that Trump definitely posted outside the 80-99 band. It is based on the market possibly being too confident in a narrow band whose official count depends on tracker-specific edge cases that were not independently auditable from lightweight public checks.

## Question being evaluated

Will Donald Trump post 80-99 Truth Social posts from March 31, 2026 12:00 PM ET to April 7, 2026 12:00 PM ET under the market's stated counting rules?

## Current lean

Slight lean against overconfidence in the 80-99 band; modest under on the contract as priced.

## Prior / starting view

Starting baseline was the market-implied probability of 71.5%, which suggests the band is already considered more likely than not.

## Evidence supporting the claim

- Market structure itself implies participants likely expect a high but not extreme Trump posting volume in the relevant week. This deserves some weight because similar social-post-count markets often attract informed flow, though it is indirect.
- The governing source of truth is a dedicated tracker designed for this purpose, which argues against assuming complete chaos in the count. Indirect but relevant.

## Evidence against the claim

- The market rules explicitly allow replies that appear on the main feed to be counted by the tracker despite saying replies do not count. This is direct rule-based evidence of potential counting ambiguity.
- The rules count deleted posts if the tracker captures them for about five minutes, which introduces operational capture risk rather than a purely observable platform total. Direct rule-based evidence.
- Truth Social public page access in this environment verifies identity but does not expose an auditable timeline. This makes independent verification of the precise band weak.
- XTracker static fetches returned a client-rendered shell rather than the actual live dataset or counter, so a lightweight independent audit could not verify the count path directly.

## Ambiguous or mixed evidence

- The fact that XTracker is the official source cuts both ways: it reduces settlement ambiguity formally, but increases practical audit ambiguity when the interface is not easily inspectable from simple fetches.
- If the final count lands comfortably inside 80-99, the edge cases may not matter. If it lands near the boundaries, they matter a lot.

## Conflict between inputs

There is no strong factual conflict between sources. The conflict is interpretive: whether to trust the market's apparent confidence in a narrow numerical band despite tracker-edge-case ambiguity and limited public auditability.

## Key assumptions

- The unresolved tracker-audit gap is material enough to justify a lower probability than market.
- The final total may be close enough to the band edges that reply/deletion capture rules matter.

## Key uncertainties

- The actual live XTracker post counter and export for the relevant window were not directly inspectable here.
- Unknown presence or absence of counted deleted posts.
- Unknown presence or absence of main-feed replies that the tracker would include.

## Disconfirming signals to watch

- A clean exported tracker ledger showing a stable count clearly inside the band.
- Independent audit showing no edge-case posts and a comfortable mid-band total.
- Final tracker total well away from 79 or 100.

## What would increase confidence

- Direct access to XTracker export data for @realDonaldTrump over the window.
- A second independent tracker or archived post log with classification by post type.
- Screenshots or records confirming whether any deleted posts were captured.

## Net update logic

The evidence did not create a strong directional call on Trump's raw behavior. It did create a credible variant case that the market may be overconfident because contract-specific counting mechanics are harder to independently validate than the price suggests. That shifts the estimate modestly below market rather than dramatically against it.

## Suggested downstream use

Use as an orchestrator synthesis input and as a caution flag on settlement-mechanics confidence rather than as a strong behavioral forecast.