---
type: source_note
case_key: case-20260415-894d4fca
dispatch_id: dispatch-case-20260415-894d4fca-20260415T021731Z
analysis_date: 2026-04-15
persona: variant-view
domain: politics
subdomain: legislative-power
entity:
topic: fisa-section-702-reauthorization-contract-logic
question: What exactly must happen for the market to resolve Yes?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market description and resolution criteria
source_type: market-contract
source_url: https://polymarket.com/event/fisa-section-702-reauthorized-before-it-expires
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-894d4fca/researcher-analyses/2026-04-15/dispatch-case-20260415-894d4fca-20260415T021731Z/personas/variant-view.md]
tags: [polymarket, market-rules, resolution, deadline, source-note]
---

# Summary

The market resolves Yes only if legislation reauthorizing FISA Title VII including Section 702 passes both chambers and is signed into law by April 19, 2026, 11:59 PM ET. The description also says qualifying legislation includes Public Law 118-49 and lists Congress.gov / Library of Congress / other official U.S. government information as primary resolution sources, with credible reporting as fallback.

## Key facts extracted

- Yes requires passage by both House and Senate plus enactment into law by Apr. 19, 2026 11:59 PM ET.
- Qualifying legislation includes Public Law 118-49.
- Joint resolutions can qualify.
- Law without signature while Congress remains in session and veto override can qualify; pocket veto expiration resolves No.
- Primary resolution sources are Congress.gov and other official U.S. government information, with credible reporting as fallback.

## Evidence directly stated by source

- The market uses a fixed deadline: Apr. 19, 2026 11:59 PM ET.
- The market explicitly contemplates official government sources and fallback consensus reporting.
- The market expressly includes Public Law 118-49 as qualifying legislation.

## What is uncertain

- The description does not itself explain why the operative legal deadline is framed as Apr. 19, 2026 rather than two years after Apr. 20, 2024 enactment.
- The relationship between the named Congress.gov bill page and the explicit Public Law 118-49 inclusion creates some source-of-truth ambiguity if they appear to point in different directions.

## Why this source may matter

The contract wording is itself outcome-determinative. Even if Section 702 legally expires later than Apr. 19, 2026, the market still asks whether qualifying legislation is enacted by Apr. 19, 2026, so the practical question becomes whether Congress acts by that fixed market deadline.

## Possible impact on the question

This source keeps the analysis from drifting into pure legal sunset interpretation. It forces a two-part logic check: actual statutory timing versus market-imposed deadline and source-of-truth hierarchy.

## Reliability notes

- This is the governing contract text for the market, so it is authoritative for resolution logic but not for underlying legal interpretation.
- It is direct evidence for market conditions, not for congressional likelihood by itself.
