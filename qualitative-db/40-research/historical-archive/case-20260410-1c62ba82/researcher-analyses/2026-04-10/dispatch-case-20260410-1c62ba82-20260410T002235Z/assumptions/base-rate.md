---
type: assumption_note
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
status: active
certainty: medium
importance: high
time_horizon: immediate
related_entities: ["donald-trump"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260410-1c62ba82/researcher-analyses/2026-04-10/dispatch-case-20260410-1c62ba82-20260410T002235Z/personas/base-rate.md"]
tags: ["assumption", "tracker-integrity", "resolution"]
---

# Assumption

The XTracker total of 103 for the specified window correctly implements the contract’s inclusion and exclusion rules closely enough that a separate full manual recount is unlikely to change the bucket outcome.

## Why this assumption matters

The final probability estimate is mostly a question of whether the named tracker should be trusted as the operative count surface. If that assumption fails, the market could still resolve differently despite the tracker currently sitting squarely in range.

## What this assumption supports

- A high probability that the 100-119 bucket resolves Yes.
- A view close to, but slightly below, the market because residual implementation risk still exists.
- Stopping research without a line-by-line manual recount of all posts.

## Evidence or logic behind the assumption

- The contract explicitly names XTracker Post Counter as the primary resolution source.
- XTracker public docs describe the relevant endpoints and date-handling.
- The tracking object, user identity, and posts endpoint all line up on `realDonaldTrump` / `TRUTH_SOCIAL` / the exact noon-to-noon ET window.
- The reported total of 103 is not near the edge of the bucket; modest recount noise would be unlikely to move it outside 100-119.

## What would falsify it

- Evidence that XTracker included a material number of non-counting replies.
- Evidence that XTracker missed enough valid main-feed posts, reposts, or quote posts to move the true count below 100.
- A tracker malfunction or later correction from Polymarket indicating the API total was wrong.

## Early warning signs

- Exported records showing many obvious reply-only objects not appearing on the main feed.
- A discrepancy between tracker records and Truth Social main-feed visibility large enough to exceed a few posts.
- API instability, sync error, or changed tracker count near resolution.

## What changes if this assumption fails

Confidence should drop sharply, and the case would require manual recounting from exported tracker data and/or a direct Truth Social main-feed audit with explicit contract-rule application.

## Notes that depend on this assumption

- Main finding for the base-rate persona.
- Evidence map for this dispatch.