---
type: source_note
case_key: case-20260413-36f15d57
dispatch_id: dispatch-case-20260413-36f15d57-20260413T175211Z
analysis_date: 2026-04-13
persona: risk-manager
domain: ai
subdomain: prediction-market-resolution
entity: polymarket
topic: Contract wording and source-of-truth rules for DeepSeek V release market
question: What exactly counts for Yes vs No under the contract?
driver: reliability
date_created: 2026-04-13
source_name: Polymarket event page / contract text
source_type: market contract source
source_url: https://polymarket.com/event/deepseek-v4-released-by-march-31
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [polymarket]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [contract, resolution, source-of-truth, deepseek]
---

# Summary

The governing contract is stricter than a generic "did DeepSeek mention V4" question. For Yes, the next major DeepSeek V model must be publicly accessible by the deadline, clearly positioned as successor to V3, and officially announced by DeepSeek as accessible to the general public. Closed beta, private access, derivative variants, and preview/experimental releases not positioned as the new flagship do not count.

## Key facts extracted

- The market resolves Yes only if the next DeepSeek V model is made available to the general public by the stated deadline.
- Intermediate versions such as V3.5 do not count.
- Versions such as V4 or V5 could count if they are the next major V-series release.
- Derivative models such as V4-Lite, V4-Mini, task-specialized models, R-series models, and experimental/preview releases such as V4-Exp or V4-Preview do not count unless they are positioned as the new V flagship model.
- Open beta or open rolling waitlist signups can count; closed beta or private access does not.
- The release must be clearly defined and publicly announced by DeepSeek as accessible to the general public.
- Primary resolution source is official DeepSeek information, with additional verification from consensus credible reporting.

## Evidence directly stated by source

The contract text itself explicitly states the qualifying and disqualifying conditions above.

## What is uncertain

- The fetched event page text references an April 15 deadline while assignment metadata and prompt text mention April 30 / March 31 variants; this indicates market-surface drift or prompt inconsistency, increasing resolution-audit importance.
- The exact currently operative deadline on the live market should be treated carefully, but this run's directional view is not close to the deadline edge because the issue is absence of any qualifying public V4/V5 release signal at all.

## Why this source may matter

This is the governing rule set for what counts. It sharply narrows what evidence should matter and excludes many superficially bullish signals.

## Possible impact on the question

The stricter the contract interpretation, the more fragile a Yes case becomes. Evidence must show not just a new model rumor or preview, but an official, public, flagship successor release.

## Reliability notes

Highest relevance for resolution mechanics. Some ambiguity remains because the assignment metadata and fetched market text appear inconsistent on deadline naming, so later synthesis should confirm the live operative date.