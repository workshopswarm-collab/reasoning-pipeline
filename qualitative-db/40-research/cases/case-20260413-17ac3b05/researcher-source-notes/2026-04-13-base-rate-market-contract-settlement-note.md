---
type: source_note
case_key: case-20260413-17ac3b05
dispatch_id: dispatch-case-20260413-17ac3b05-20260413T185719Z
analysis_date: 2026-04-13
persona: base-rate
domain: economics
subdomain: china-macro
entity: china
topic: china-q1-2026-gdp
question: Will China GDP growth in Q1 2026 be between 5.0% and 5.5%?
driver: reliability
date_created: 2026-04-13
source_name: Polymarket market page and embedded resolution description
source_type: market-contract
source_url: https://polymarket.com/event/china-gdp-growth-in-q1-2026
source_date: 2026-04-13
credibility: medium
recency: current
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [china]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [base-rate.md]
tags: [market-contract, settlement-mechanics, china-gdp]
---

# Summary

This source defines the market's governing settlement mechanics. It is not the authoritative economic source, but it is authoritative for how the market says it will map the statistic to resolution.

## Key facts extracted

- The market resolves to China's year-over-year GDP growth rate in the "Preliminary Accounting Results of GDP" release for Q1 2026.
- The release is scheduled for April 17, 2026.
- The referenced release location is the NBS English press release page.
- If the reported value falls exactly on a bracket boundary, the market resolves to the higher range bracket.
- If no data for the specified quarter is released by the date the next quarter's data is scheduled to be released, the market resolves using the last available quarter.
- Revisions after the initial release do not count.

## Evidence directly stated by source

Directly states the governing release family, the initial-release-only rule, and the bracket-boundary rule.

## What is uncertain

- The market text points to the NBS English press release page, but the exact Q1 2026 release document was not yet posted as of research time.
- The contract relies on the English-language release path, while the Chinese-language NBS release may appear first or differ in timing; the market text implies the English page is the practical reference surface.

## Why this source may matter

Settlement mechanics are material here because the contract is about a single official print, not a later revised estimate or a private forecast consensus.

## Possible impact on the question

It makes official NBS release timing and exact initial bracket placement more important than broader debates about true underlying growth quality.

## Reliability notes

Useful and necessary for contract interpretation, but it is a secondary wrapper around the actual governing data source, which is the NBS release itself.
