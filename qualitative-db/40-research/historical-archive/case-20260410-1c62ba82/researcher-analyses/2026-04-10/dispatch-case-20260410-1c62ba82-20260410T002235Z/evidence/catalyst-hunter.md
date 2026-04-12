---
type: evidence_map
case_key: case-20260410-1c62ba82
dispatch_id: dispatch-case-20260410-1c62ba82-20260410T002235Z
research_run_id: a166421a-4c1b-40a8-b891-0e042db28782
analysis_date: 2026-04-10
persona: catalyst-hunter
domain: politics
subdomain: social-media-monitoring
entity: donald-trump
topic: trump-truth-social-post-count-apr3-apr10
question: "Will Donald Trump post 100-119 Truth Social posts from April 3 to April 10, 2026?"
driver: operational-risk
date_created: 2026-04-10
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["donald-trump"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260410-1c62ba82/researcher-analyses/2026-04-10/dispatch-case-20260410-1c62ba82-20260410T002235Z/personas/catalyst-hunter.md"]
tags: ["evidence-map", "post-counter", "intraday-catalyst"]
---

# Summary

The evidence currently supports a Yes lean because the governing tracker already has Trump at 103 posts in the window, but the live remaining risk is an intraday overshoot above 119 before the noon ET deadline.

## Question being evaluated

Will Donald Trump post 100-119 Truth Social posts from April 3, 2026 12:00 PM ET to April 10, 2026 12:00 PM ET under the contract’s counting rules?

## Current lean

Lean Yes, because the count is already inside the target range and recent pace is high but not yet high enough to make an overshoot the base case.

## Prior / starting view

Starting view: if market price is 0.81, the market likely thinks the bucket is favored but not locked, implying meaningful upside-bust risk above 119.

## Evidence supporting the claim

- XTracker stats endpoint shows `totalBetweenStartAndEnd: 103` for the exact April 3-April 10 window. Direct, high weight.
- XTracker daily totals show the bucket was reached by April 9 with cumulative counts of 6, 15, 26, 45, 82, 92, and 103. Direct, high weight.
- Recent observed pace is 10 posts on April 8 and 11 on April 9 through the checked sync, which is elevated but below the 17+ additional posts needed to bust the bucket from 103 to 120. Direct, medium-high weight.
- The tracker’s user endpoint verifies that the tracked account is Donald J. Trump on Truth Social and the account is marked verified. Direct, medium weight.
- A secondary archive mirror reproduces sampled late-window posts, modestly reducing tracker-only artifact risk. Contextual/confirmatory, low-medium weight.

## Evidence against the claim

- There were still roughly 12 hours left in the resolution window after the last checked tracker sync, leaving real time for a late posting burst. Direct timing risk, high weight.
- April 7 produced 37 counted posts, proving Trump can generate very high-volume days that would easily push the total above 119 if repeated in compressed form. Direct historical-in-window evidence, high weight.
- The contract includes reposts and quote posts, which can increase count quickly during fast-moving news cycles. Contract/mechanism evidence, medium weight.

## Ambiguous or mixed evidence

- The posts endpoint quick pass did not explicitly label reply vs quote/repost status for each item, so exclusion auditing remains partly inferential.
- Deleted posts count if captured for about five minutes; this is tracker-favorable for inclusion but hard to independently verify from the platform.
- Truth Social itself is a fallback source, but the public page is less auditable in a quick browserless pass than XTracker’s API.

## Conflict between inputs

There is no major factual conflict between sources. The main tension is not factual but timing-based: the tracker says 103 now, while the live unresolved question is how many more counted posts arrive before noon ET.

## Key assumptions

- XTracker continues updating correctly through resolution.
- No large hidden classification error materially changes the current 103 count.
- Trump’s remaining posting pace stays below the threshold needed to add 17+ more counted items.

## Key uncertainties

- Overnight/morning posting burst risk.
- Edge handling of replies that appear on the main feed.
- Whether any captured deleted posts later disappear from visible secondary surfaces.

## Disconfirming signals to watch

- XTracker count moving into the high teens for April 10 early in the morning ET.
- A sudden cluster of reposts/quote posts tied to geopolitics, endorsements, or media fights.
- Signs the tracker is lagging or misclassifying the feed.

## What would increase confidence

- Another XTracker check closer to noon ET still showing total under 120.
- Better post-type labels from export data confirming that currently counted items are contract-eligible.
- Secondary archival confirmation of a stable sub-120 count near the deadline.

## Net update logic

The governing source already places the market in the target bucket, so the thesis is no longer about reaching 100. The live catalyst is simply whether Trump keeps posting fast enough overnight/morning to overshoot 119. Because that overshoot requires a meaningful additional burst from an already-observed 103 base, Yes remains more likely than No, but not by enough to call the contract effectively settled.

## Suggested downstream use

- Forecast update.
- Orchestrator synthesis input.
- Follow-up investigation only if a later intraday check shows acceleration toward 120+.
