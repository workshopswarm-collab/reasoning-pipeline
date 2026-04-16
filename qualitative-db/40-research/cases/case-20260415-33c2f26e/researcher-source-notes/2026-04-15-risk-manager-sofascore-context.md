---
type: source_note
case_key: case-20260415-33c2f26e
dispatch_id: dispatch-case-20260415-33c2f26e-20260415T211658Z
analysis_date: 2026-04-15
persona: risk-manager
domain: sports
subdomain: soccer
entity:
topic: al-nassr-vs-al-ettifaq-2026-04-24
question: Will Al Nassr Saudi Club win on 2026-04-24?
driver: performance
date_created: 2026-04-15
source_name: Sofascore team page / schedule context
source_type: contextual sports data
source_url: https://www.sofascore.com/football/team/al-nassr/5547
source_date: 2026-04-15
credibility: medium
recency: medium
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: orchestrator
related_entities: []
related_drivers: [performance, team-dynamics]
upstream_inputs: []
downstream_uses: []
tags: [sofascore, source-note, sports-data, contextual]
---

# Summary

This source class was used as contextual sports-data verification for team identity, schedule/form context, and match framing. Retrieval quality was mixed: one fetched Sofascore URL returned a 404 and another candidate Al Ettifaq URL misresolved to an unrelated club page, so this source is useful mainly as a reminder that external sports-data pages can be noisy and require entity verification.

## Key facts extracted

- Sofascore was reachable as a mainstream sports-data source, but direct URL retrieval around these clubs was not fully clean in this run.
- The attempted Al Ettifaq team URL redirected to an unrelated team page, showing concrete entity-mapping risk.
- Because of that mapping issue, this source was not treated as authoritative for fine-grained estimates.

## Evidence directly stated by source

The cleanly fetched material did not provide trustworthy direct match evidence for this exact fixture because of the team-page mismatch.

## What is uncertain

- Exact fixture page and current form details were not reliably retrievable through the attempted URLs.
- Whether the mislabeled or redirected team identifiers reflect site changes, entity collisions, or extraction issues.

## Why this source may matter

It is still a meaningful contextual source because it shows the need for an extra verification pass and supports a lower-confidence, risk-managed stance rather than blind acceptance of an extreme favorite price.

## Possible impact on the question

This source does not materially move the directional view by itself. Its main impact is methodological: it reduces confidence in any estimate that would otherwise lean too heavily on a single consumer sports-data site without clean entity confirmation.

## Reliability notes

Medium-to-low reliability for this exact run because entity resolution was noisy. Useful as a contextual check and as evidence of source-independence limitations, not as the governing source of truth.