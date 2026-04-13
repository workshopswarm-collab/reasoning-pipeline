---
type: source_note
case_key: case-20260413-9c835dfe
dispatch_id: dispatch-case-20260413-9c835dfe-20260413T162509Z
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: corporate-treasury
entity: btc
topic: case-20260413-9c835dfe | risk-manager
question: Will MicroStrategy/Strategy announce a purchase of more than 1000 BTC between April 7 and April 13, 2026 ET?
driver: reliability
date_created: 2026-04-13
source_name: Strategy Bitcoin Purchases page
source_type: official company webpage
source_url: https://www.strategy.com/purchases
source_date: 2026-04-13
credibility: high
recency: current
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-9c835dfe/researcher-analyses/2026-04-13/dispatch-case-20260413-9c835dfe-20260413T162509Z/personas/risk-manager.md]
tags: [official-source, resolution-source, strategy, bitcoin-purchases]
---

# Summary

The official Strategy purchases page is explicitly referenced by the market description as a tracking surface for reported BTC holdings. In this run it verified that the company maintains a dedicated official BTC-purchases page on the current Strategy domain, which matters for source-of-truth and attribution, but the page extraction available here did not expose the live holdings table/body content.

## Key facts extracted

- `https://www.strategy.com/purchases` is a live official company page titled **"Bitcoin Purchases - Strategy"**.
- The legacy `microstrategy.com` domain redirects into the current `strategy.com` domain, confirming the corporate rename/domain mapping.
- The market description itself identifies official information from **MicroStrategy or Michael Saylor** as the governing resolution source, with the purchases page given as a reference tracking surface.

## Evidence directly stated by source

- The page title and metadata identify it as an official Strategy Bitcoin purchases page.
- The page is hosted on the company domain used by the renamed firm.

## What is uncertain

- The readable fetch available in this environment did not expose the dynamic page contents showing latest purchases/holdings.
- This note therefore confirms source legitimacy and accessibility more than the underlying purchase count for the specific week.

## Why this source may matter

- It is the cleanest official company source mentioned in the contract context.
- For a narrow date-window announcement market, confirming the correct official domain and purchase-announcement surface reduces attribution risk and settlement ambiguity.

## Possible impact on the question

- This source supports the view that any qualifying announcement should appear through official Strategy channels and/or Michael Saylor.
- It does not by itself prove a >1000 BTC announcement occurred during April 7-13, but it sharply narrows what should count as authoritative evidence.

## Reliability notes

- High credibility as an official company webpage.
- Evidence independence is limited if combined only with other company-controlled channels; independent verification is still useful for timing or announcement confirmation.
- The limitation in this run is technical readability of dynamic content, not source legitimacy.
