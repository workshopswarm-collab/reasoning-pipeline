---
type: evidence_map
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
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["donald-trump"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260407-b3dc16a7/researcher-analyses/2026-04-07/dispatch-case-20260407-b3dc16a7-20260407T031152Z/personas/risk-manager.md"]
tags: ["evidence-map", "truth-social", "tracker"]
---

# Summary

The current lean is modestly bullish on the 80-99 band, but not as bullish as the market, because the governing counter sat at 77 at audit time and the remaining path depends on a small number of additional countable posts plus clean classification.

## Question being evaluated

Will Donald Trump post 80-99 Truth Social posts, as counted by Polymarket's XTracker under the stated exclusions and deleted-post rule, between Mar 31 12:00 PM ET and Apr 7 12:00 PM ET?

## Current lean

Lean Yes, but with real tail risk from narrow threshold mechanics and classification uncertainty.

## Prior / starting view

Starting view was that a 0.715 market price likely reflected Trump being active enough to finish in-range, but that rule sensitivity could make the confidence look slightly too high.

## Evidence supporting the claim

- XTracker governing count already at 77 with roughly 10 hours left before resolution, so only 3 more countable posts are needed to reach the band.
  - Source: `2026-04-07-risk-manager-xtracker-audit.md`
  - Direct evidence.
  - High weight.
- Trump was actively posting late in the window, including three countable-looking text posts during the Apr 6 evening / Apr 7 early-morning period.
  - Source: XTracker raw posts endpoint and archive cross-check.
  - Direct evidence.
  - Medium-high weight.
- Secondary archive confirms substantial activity and correct account identity, reducing the chance that the tracker is attached to the wrong user.
  - Source: `2026-04-07-risk-manager-trumpstruth-crosscheck.md`
  - Contextual / audit evidence.
  - Medium weight.

## Evidence against the claim

- Governing count was still below threshold at 77; this is not a settled-in-range market yet.
  - Source: XTracker stats endpoint.
  - Direct evidence.
  - High weight.
- Market rules exclude replies, and tracker/archives contain blank-content and repost-like items whose countability is not perfectly transparent from quick API inspection.
  - Source: market rules + XTracker raw export pattern.
  - Direct plus interpretive.
  - High weight.
- Deleted posts count only if captured for about five minutes; that rule adds an operational tail where apparent feed activity may not resolve into countable tracker activity if short-lived.
  - Source: market rules.
  - Direct rule evidence.
  - Medium weight.
- The archive showed more raw result blocks than XTracker's 77 count, which is a warning that naive feed counts can overstate the market-valid total.
  - Source: archive cross-check.
  - Contextual audit evidence.
  - Medium weight.

## Ambiguous or mixed evidence

- Blank-content entries likely include media-only posts or repost shells. They probably count if they are main-feed posts/reposts captured by XTracker, but the exact subclassification is opaque in the quick audit.
- The archive's broader result set may imply missing items, but much of the difference is due to pre-window timestamps and search-mode inclusion behavior rather than obvious XTracker failure.

## Conflict between inputs

There is no hard factual conflict between sources. The main tension is methodological: the governing tracker says 77, while the independent archive shows a noisier/higher raw set that is not directly market-valid without careful filtering.

## Key assumptions

- XTracker is not materially undercounting countable in-window items.
- Trump remains likely to post at least a few more countable items before noon ET.
- No late clarifying guidance changes how blank/repost items are interpreted.

## Key uncertainties

- Morning posting pace before noon ET.
- Whether any late-window activity is replies/non-counting rather than main-feed posts.
- Whether any deleted items appear and are or are not captured long enough.

## Disconfirming signals to watch

- No new countable posts added by late morning.
- XTracker count stalls below 80 while Truth Social activity appears mostly replies.
- Evidence of tracker misclassification or missed captured posts.

## What would increase confidence

- One more verification pass closer to noon showing count at 80+.
- Export data showing the 77 current items are being classified in line with the market rules.
- Independent confirmation that blank-content items are valid main-feed/media posts rather than replies.

## Net update logic

The decisive fact is that the market only needs three more countable posts, which makes Yes the modal path. But because the current governing count remains below threshold and the rules are narrow, the market's 71.5% confidence looks a bit rich rather than obviously wrong.

## Suggested downstream use

Use this as synthesis input for a slightly cautious Yes-leaning view, with emphasis on threshold/path risk rather than on a clean settled edge.