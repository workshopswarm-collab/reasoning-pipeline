---
type: source_note
case_key: case-20260414-4ed80a0a
dispatch_id: dispatch-case-20260414-4ed80a0a-20260414T174040Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: protocols
entity: ethereum
topic: market contract page and resolution framing
question: Will Ethereum reach $2,400 April 13-19?
driver:
date_created: 2026-04-14
source_name: Polymarket market page fetch
source_type: market_page
source_url: https://polymarket.com/event/what-price-will-ethereum-hit-april-13-19
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: low
importance: high
novelty: medium
agent: variant-view
related_entities: [ethereum]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/personas/variant-view.md]
tags: [source-note, polymarket, source-of-truth, contract-interpretation]
---

# Summary

The fetched Polymarket page confirms the market exists, shows extreme pricing behavior in the extracted FAQ text, and explicitly says the rules section governs settlement, but the readable fetch did not expose the actual rules text. That missing rule text is the main unresolved ambiguity in this run.

## Key facts extracted

- The fetched page title matches the relevant market: "What price will Ethereum hit April 13-19?"
- Extracted page text says the current leading outcome is `↑ 2,400` and tells users that the resolution criteria and official data sources are defined in the "Rules" section.
- The actual rules content was not included in the fetch output.

## Evidence directly stated by source

- "The resolution rules ... define exactly what needs to happen for each outcome to be declared a winner — including the official data sources used to determine the result."
- "We recommend reading the rules carefully before trading, as they specify the precise conditions, edge cases, and sources that govern how this market is settled."

## What is uncertain

- Which exchange, oracle, or index Polymarket will actually use.
- Whether "hit" means touched on one venue, touched on a designated reference source, or some other internal rule.
- Whether the extracted displayed percentages are reliable, since the FAQ-style fetch can reflect page-generation quirks.

## Why this source may matter

This source is the best available direct evidence about the contract surface itself and, importantly, it highlights that source-of-truth ambiguity is real rather than imagined.

## Possible impact on the question

The missing rules text prevents treating venue-specific highs as fully dispositive. That keeps a small but meaningful wedge between "ETH almost certainly traded above $2,400 somewhere" and "this specific contract is already safely settled."

## Reliability notes

Useful as direct market-surface context, but not fully sufficient because the extraction failed to capture the governing rules text.