---
type: source_note
case_key: case-20260409-a8d8231d
dispatch_id: dispatch-case-20260409-a8d8231d-20260409T183257Z
analysis_date: 2026-04-09
persona: base-rate
domain: climate
subdomain: market-rules
entity:
topic: march-2026-temperature-market-rules
question: Will global temperature increase by between 1.25ºC and 1.29ºC in March 2026?
driver: operational-risk
date_created: 2026-04-09
source_name: Polymarket market description and settlement rules
source_type: market_rules
source_url: https://polymarket.com/event/march-2026-temperature-increase-c
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: []
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-a8d8231d/researcher-analyses/2026-04-09/dispatch-case-20260409-a8d8231d-20260409T183257Z/personas/base-rate.md]
tags: [source-note, market-rules, settlement, polymarket]
---

# Summary

This source defines what counts for settlement and what does not count.

## Key facts extracted

- The market resolves according to the value reported by the Global Land-Ocean Temperature Index for March 2026 when it is released.
- The exact primary resolution source is the NASA GISS table `GLB.Ts+dSST.txt`, specifically the `Mar` column in the `2026` row.
- A figure within the named bracket is necessary and sufficient to resolve the market immediately once data is available, even if later revised.
- If NASA’s Global Temperature Index is permanently unavailable, other NASA information may be used.
- If no information for the target monthly observation is provided by NASA by the specified deadline, the market resolves to the lowest range bracket. The displayed contract text contains an apparent typo referencing February 2026 in the fallback clause, which raises minor source-of-truth ambiguity but does not dominate because the primary March 2026 table cell is available.
- The page snapshot also displayed `Outcome proposed: No` and `Dispute window Final`, which is suggestive but not itself the governing evidence.

## Evidence directly stated by source

- The rules name the exact NASA table and cell needed for settlement.
- The rules explicitly prioritize first availability over later revisions.

## What is uncertain

- The fallback clause appears internally inconsistent because it references February 2026 in a March 2026 market. That likely reflects boilerplate or drafting error.
- The page snapshot included status text (`Outcome proposed: No`) that may be an exchange UI state rather than core rules text.

## Why this source may matter

The market is rule-sensitive. Correct interpretation depends on reading the contract literally rather than inferring from generic climate-data expectations.

## Possible impact on the question

Because the rules are cell-specific and revision-insensitive, once the named NASA table reports March 2026 as 1.34°C, the relevant question is effectively settled against the 1.25–1.29°C bracket.

## Reliability notes

High reliability as the market’s governing contract text. Residual risk comes from drafting ambiguity in the fallback clause, not from the primary source definition.