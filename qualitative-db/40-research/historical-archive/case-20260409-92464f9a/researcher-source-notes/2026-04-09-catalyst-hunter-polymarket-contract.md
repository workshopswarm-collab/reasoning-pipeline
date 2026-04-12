---
type: source_note
case_key: case-20260409-92464f9a
dispatch_id: dispatch-case-20260409-92464f9a-20260409T201552Z
analysis_date: 2026-04-09
persona: catalyst-hunter
domain: climate
subdomain: global-temperature
entity: nasa
topic: march-2026-global-temperature-contract
question: Will global temperature increase by more than 1.29ºC in March 2026?
driver: reliability
date_created: 2026-04-09
source_name: Polymarket contract page for March 2026 Temperature Increase market
source_type: market-contract
source_url: https://polymarket.com/event/march-2026-temperature-increase-c
source_date: 2026-04-09
credibility: medium
recency: current
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [nasa]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-92464f9a/researcher-analyses/2026-04-09/dispatch-case-20260409-92464f9a-20260409T201552Z/personas/catalyst-hunter.md]
tags: [polymarket, contract, source-of-truth, resolution]
---

# Summary

The market contract states that resolution depends on the NASA GISS `GLB.Ts+dSST.txt` table, specifically the `Mar` column for row `2026`, and that later revisions do not matter once the figure is first available. It also states a fallback-to-lowest-bracket rule only if NASA does not provide the relevant information by May 1, 2026 11:59 PM ET.

## Key facts extracted

- Primary resolution source is NASA GISS `GLOBAL Land-Ocean Temperature Index in 0.01 degrees Celsius` table.
- Exact field is the `Mar` column in row `2026`.
- Initial release controls; later revisions do not change settlement.
- If NASA’s main index page is permanently unavailable, other NASA information may be used.
- If no information is provided by the stated deadline, market resolves to the lowest bracket.
- The public market page currently also displays `Outcome proposed: No` and `Final outcome: No`, though that display is platform-side reporting rather than the governing scientific source itself.

## Evidence directly stated by source

The contract text directly specifies what counts, what does not count, and the governing NASA table. It directly settles that NOAA or Copernicus numbers are contextual, not dispositive, for this contract.

## What is uncertain

- The fetched page is not the scientific source of truth itself.
- The page display showing `Final outcome: No` is useful context but should not substitute for the underlying NASA table when available.
- The fallback clause appears to contain a likely typo referring to February 2026 in one version of the contract text, even though the market concerns March 2026.

## Why this source may matter

This source defines the settlement mechanics and therefore determines which external evidence is direct versus merely contextual.

## Possible impact on the question

It sharply narrows the relevant catalyst set: the only truly decisive catalyst is NASA GISS publishing the March 2026 row/column value. Other climate reports matter mainly as previews for repricing, not for final settlement.

## Reliability notes

Useful and necessary for contract interpretation, but not sufficient alone for the terminal scientific answer. Reliability is medium because it is authoritative for market rules yet secondary to the underlying NASA publication for the actual number.