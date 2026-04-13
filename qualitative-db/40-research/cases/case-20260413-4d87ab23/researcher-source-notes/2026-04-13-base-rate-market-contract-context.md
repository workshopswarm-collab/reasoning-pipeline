---
type: source_note
case_key: case-20260413-4d87ab23
dispatch_id: dispatch-case-20260413-4d87ab23-20260413T174302Z
analysis_date: 2026-04-13
persona: base-rate
domain: technology
subdomain: prediction-market-contracts
entity:
topic: Polymarket contract wording for DeepSeek V4/V5 release market
question: What exactly counts for resolution, and what is the effective timing pressure near the deadline?
driver:
date_created: 2026-04-13
source_name: Polymarket market page and contract description
source_type: market contract / resolution source
source_url: https://polymarket.com/event/deepseek-v4-released-by-march-31
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [polymarket, contract, resolution]
---

# Summary

The contract is narrow and rule-sensitive. A Yes requires not just an announcement, but a next major DeepSeek V-series model after V3 that is clearly positioned as the successor and made publicly accessible by the deadline. Closed beta, private access, derivative sub-models, and mere labeling errors do not count.

## Key facts extracted

- The fetched market page says Yes requires the next DeepSeek V model to be made available to the general public by April 15, 2026, at 11:59 PM ET.
- Intermediate versions like V3.5 do not count.
- Versions such as V4 or V5 could count, but only if they are the next major release in the DeepSeek V series and clearly positioned as successors to V3.
- Derivative or preview names such as V4-Lite, V4-Mini, V4-Exp, or V4-Preview do not count if they are not the new V flagship model.
- Public accessibility can include open beta or open rolling waitlist signups.
- Closed beta or private access does not count.
- Official DeepSeek information is the primary resolution source, with additional verification from consensus credible reporting.

## Evidence directly stated by source

The contract itself supplies the resolution mechanics and the source-of-truth hierarchy.

## What is uncertain

- The assignment metadata references a market title phrased as "by May 15," while the linked Polymarket page fetch describes an April 15 deadline. The runtime prompt itself also contains a stale March 31 description block. This creates nontrivial date ambiguity in the assignment materials.
- The safest interpretation for this run is to analyze the linked market page and the assignment context together, while explicitly flagging the timing inconsistency for review.

## Why this source may matter

This is the governing rule text for what counts and does not count. The narrow wording raises the evidence threshold and makes vague rumors or private testing much less relevant than a clear public successor launch.

## Possible impact on the question

The contract wording favors No unless there is clear official evidence of a publicly accessible successor. It also means that even genuine progress toward V4 would fail to resolve Yes if access remained closed or the branding stayed ambiguous.

## Reliability notes

High reliability for contract interpretation, but there is assignment-level deadline ambiguity that should be surfaced separately rather than silently ignored.