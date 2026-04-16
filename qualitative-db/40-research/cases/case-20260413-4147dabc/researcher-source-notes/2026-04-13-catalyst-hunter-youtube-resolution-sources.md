---
type: source_note
case_key: case-20260413-4147dabc
dispatch_id: dispatch-case-20260413-4147dabc-20260413T183547Z
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: animals-and-nature
subdomain: wildlife-cams-and-date-resolution
entity: youtube
topic: great-lakes-bald-eagle-cam-resolution-sources
question: Will the first eaglet hatch on April 11, 2026?
driver: reliability
date_created: 2026-04-13
source_name: Great Lakes Bald Eagle Cam YouTube resolution source endpoints (Cam 1 and Cam 2)
source_type: primary-resolution-source
source_url: https://www.youtube.com/watch?v=vMW-S6ZoYgY ; https://www.youtube.com/live/rWQEKZGcius
source_date: 2026-04-13
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [youtube]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [source-note, youtube, livestream, source-of-truth, outage-risk]
---

# Summary

These two YouTube endpoints are the direct governing resolution sources named by the contract. The fetchable metadata confirms that both source URLs exist, are active YouTube video surfaces, and are branded as Great Lakes Bald Eagle Cam 1 and Cam 2 for Traverse City, Michigan.

## Key facts extracted

- Cam 1 title metadata: **"BALD EAGLE Live Cam 1 Traverse City, MI"**.
- Cam 2 title metadata: **"BALD EAGLE Live Cam 2 Traverse City, MI"**.
- Both are published under **Great Lakes Bald Eagle Cam** on YouTube.
- Both endpoints return active YouTube oEmbed metadata as of the verification pass on 2026-04-13.
- Because the contract explicitly keys to these livestream timestamps, stream availability and timestamp integrity are operationally material to resolution.

## Evidence directly stated by source

- The oEmbed metadata directly states the video titles and channel attribution.
- The source URLs resolve successfully at verification time, supporting that the named resolution surfaces exist and are reachable.

## What is uncertain

- This metadata does not itself provide hatch timing, egg chronology, or stream uptime history.
- The lightweight fetch path here does not expose full livestream status history or whether there were prior outages around potential hatch windows.
- The metadata alone does not confirm whether the stream timestamps display ET or localize in a way visible to end users; that still depends on YouTube/live interface behavior and the contract's ET wording.

## Why this source may matter

This confirms the source-of-truth surfaces are real and currently reachable, which matters because the contract contains a special rule for the case where **both** streams are unavailable. For a date-specific market, source availability is itself part of the causal chain to settlement.

## Possible impact on the question

The most important catalyst is not a soft narrative event but a concrete stream-visible change from incubation to **full emergence**. A secondary catalyst is an operational one: any period where both streams are down near the hatch window could alter how the qualifying date is recorded under the contract.

## Reliability notes

- Strong relevance because these are the named authoritative surfaces.
- Limited informational depth from oEmbed alone; this is a presence/identity verification pass rather than a full biological timing source.
- Best combined with contract text and independent contextual timing about bald eagle incubation.