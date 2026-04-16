---
type: source_note
case_key: case-20260416-969f7c01
dispatch_id: dispatch-case-20260416-969f7c01-20260416T013210Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: market-data-context
entity: ethereum
topic: ethereum-above-2200-on-april-17
question: Will the price of Ethereum be above $2,200 on April 17?
driver: reliability
date_created: 2026-04-15
source_name: Secondary ETH price references from CoinDesk and web search snippets
source_type: secondary market data context
source_url: https://www.coindesk.com/price/ethereum
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: market-implied
related_entities: [ethereum]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [market-implied-finding]
tags: [coindesk, secondary-source, cross-check]
---

# Summary

Secondary price references were used as a verification pass, not as the governing source of truth.

## Key facts extracted

- Web search surfaced a Binance snippet around `2317.93` and a CoinDesk snippet around `2317.18` earlier on Apr 15/16.
- CoinDesk page content itself was mostly descriptive, but the search snippet indicated ETH was trading in the low 2300s on the same date.
- These references are directionally consistent with the direct Binance check later showing ETH around `2352.6`.

## Evidence directly stated by source

- Secondary public references placed ETH well above 2200 on the relevant date.

## What is uncertain

- Search snippets are less auditable than direct page/API output.
- The exact timestamp of those snippets differs from the direct Binance pull and may lag.
- These sources do not settle the contract.

## Why this source may matter

They provide mild independence from the exchange API pull and help test whether the Binance reading looked anomalous.

## Possible impact on the question

They modestly reinforce that the market is not obviously mispricing by using a bad anchor; broader public pricing also had ETH safely above 2200.

## Reliability notes

Useful only as contextual corroboration. Lower weight than Binance and lower weight than the contract rules page for settlement mechanics.