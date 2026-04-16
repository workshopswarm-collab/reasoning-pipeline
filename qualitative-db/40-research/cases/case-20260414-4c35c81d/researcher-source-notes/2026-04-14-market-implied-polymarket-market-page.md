---
type: source_note
case_key: case-20260414-4c35c81d
dispatch_id: dispatch-case-20260414-4c35c81d-20260414T204205Z
analysis_date: 2026-04-14
persona: market-implied
domain: sports
subdomain: soccer
entity:
topic: polymarket-spl-qad-sha-2026-04-23
question: Will Al Qadisiyah Saudi Club win on 2026-04-23?
driver:
date_created: 2026-04-14
source_name: Polymarket market page
source_type: market page / platform source
source_url: https://polymarket.com/event/spl-qad-sha-2026-04-23
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [polymarket, market-structure, resolution-source, pricing]
---

# Summary

The Polymarket page provides the contract wording, stated resolution mechanics, and current quoted prices embedded in page data for the Al Qadisiyah vs Al Shabab Saudi Pro League market.

## Key facts extracted

- The market question is whether Al Qadisiyah Saudi Club will win the scheduled April 23, 2026 match.
- Resolution is based only on the outcome in the first 90 minutes plus stoppage time.
- If the match is postponed, the market stays open until completed; if canceled entirely without a make-up game, it resolves No.
- The stated primary resolution source is the official statistics of the event as recognized by the governing body or event organizers; if no final statistics are published within 2 hours after the event, a consensus of credible reporting may be used.
- Embedded page data shows the binary moneyline market priced very strongly toward Al Qadisiyah winning, with outcomePrices including a 0.9995/0.0005 split for one of the moneyline slices, and the assignment context supplied the operative current price of 0.83 for the case.
- The page also embeds contextual match text stating that a prior Al Qadisiyah vs Al Shabab meeting ended 2-2 and that Al Qadisiyah sat 4th in the standings with an 18-7-3 record at the time of that generated page text.

## Evidence directly stated by source

- Contract wording and resolution source language are directly stated on the page.
- The page directly states that official statistics recognized by the governing body or event organizers are the primary source of truth.
- The page directly states that only regular time plus stoppage time counts.
- Page-embedded structured data directly exposes quoted market prices and related sports-market metadata.

## What is uncertain

- The public page includes templated/generated sports copy and multiple embedded markets; some embedded price snippets are not cleanly mapped without parsing the full app state.
- The assignment context's current_price field is more reliable for this run than hand-reading every embedded price object.
- The generated contextual text about standings and prior result is useful but still secondary to official league tables and fixture sources.

## Why this source may matter

This is the direct contract surface. It is the best source for what the market is actually asking, how it resolves, and what information the market itself is presenting to traders.

## Possible impact on the question

This source anchors the market-implied baseline and the source-of-truth interpretation. It also suggests that traders may be leaning heavily on team-strength and prior-results context already embedded or broadly known in the market.

## Reliability notes

Reliable for contract wording and platform-exposed pricing metadata. Less reliable as a standalone sports-information source because some page text is templated/generated and not clearly audited against official league records.