---
type: source_note
case_key: case-20260413-9c835dfe
dispatch_id: dispatch-case-20260413-9c835dfe-20260413T162509Z
analysis_date: 2026-04-13
persona: variant-view
domain: crypto
subdomain: institutions
entity: strategy
topic: strategy bitcoin purchase disclosure page
question: Did Strategy announce a purchase of more than 1000 BTC during April 7-13, 2026?
driver: capital-markets
date_created: 2026-04-13
source_name: Strategy Bitcoin Purchases page
source_type: official company webpage / disclosure hub
source_url: https://www.strategy.com/purchases
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: variant-view
related_entities: [strategy, bitcoin, btc]
related_drivers: [capital-markets]
upstream_inputs: []
downstream_uses: []
tags: [official-source, resolution-source, company-disclosure]
---

# Summary

Strategy's official purchases page shows a new entry dated 2026-04-13 for 13,927 BTC acquired, with total holdings of 780,897 BTC as of 2026-04-12. This directly exceeds the market threshold of more than 1,000 BTC and falls within the April 7-13 window.

## Key facts extracted

- Latest entry date_of_purchase: `2026-04-13`
- BTC acquired (`count`): `13,927`
- Total purchase price: about `$1.001B`
- Holdings after purchase: `780,897 BTC`
- The page links a same-day SEC filing (`form-8-k_04-13-2026.pdf`)
- The same entry includes plain-text social copy: `@Strategy has acquired 13,927 BTC... As of 4/12/2026, we hodl 780,897 BTC...`

## Evidence directly stated by source

The official company page directly states that Strategy acquired 13,927 BTC and timestamps the entry to 2026-04-13. It also provides linked filing provenance for the announcement.

## What is uncertain

- The page is a company-maintained summary surface rather than the formal SEC filing text itself.
- The field name `date_of_purchase` appears to map to the announcement/filing date in this interface, but the market resolves on announcement timing anyway, so the main relevant fact is that Strategy publicly posted the announcement on 2026-04-13.

## Why this source may matter

This is one of the explicit governing sources of truth under the contract: official information from MicroStrategy/Strategy or Michael Saylor.

## Possible impact on the question

If this page is authentic and current, the market should resolve Yes because Strategy officially disclosed a >1,000 BTC purchase on 2026-04-13.

## Reliability notes

High reliability as an official company disclosure hub, but still worth cross-checking against the linked SEC filing or same-day company/social disclosure because the market is already at an extreme probability and the case checklist requires an extra verification pass.
