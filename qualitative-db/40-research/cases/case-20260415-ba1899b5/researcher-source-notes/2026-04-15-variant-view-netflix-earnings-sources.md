---
type: source_note
case_key: case-20260415-ba1899b5
dispatch_id: dispatch-case-20260415-ba1899b5-20260415T121723Z
analysis_date: 2026-04-15
persona: variant-view
domain: culture
subdomain: streaming
entity: netflix
topic: Netflix Q1 2026 earnings beat market
action: research
question: Will Netflix Inc (NFLX) beat quarterly earnings?
driver: sentiment
date_created: 2026-04-15
source_name: Mixed primary and contextual source set for Netflix Q1 2026 earnings beat market
source_type: mixed
source_url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1065280&type=10-k&owner=exclude&count=10
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: variant-view
related_entities: [netflix]
related_drivers: [sentiment]
upstream_inputs: []
downstream_uses: []
tags: [source-note, netflix, earnings, sec, contextual-source]
---

# Summary

This note captures the main source set used to evaluate the Netflix Q1 2026 earnings beat market. The most important primary source was SEC EDGAR material confirming the company identity, filing recency, and recent reported diluted EPS history through FY2025. The most useful contextual source was AlphaQuery's earnings-history page, which explicitly listed the next expected announcement date as 2026-04-16 and the average estimated EPS as $0.76 for the quarter ending 2026-03-31, matching the market strike reference.

## Key facts extracted

- SEC EDGAR shows Netflix filed its 2025 10-K on 2026-01-23 under accession 0001065280-26-000034.
- The filing index links to `nflx-20251231.htm`, confirming a valid recent primary filing surface for Netflix.
- Macrotrends reports quarterly diluted EPS history for Netflix, including 2025-03-31 $0.66, 2025-06-30 $0.72, 2025-09-30 $0.59, and 2025-12-31 $0.56.
- AlphaQuery states that on 2026-01-20 Netflix announced EPS of $0.56 for the fiscal quarter ending 2025-12-31 and that the next expected earnings announcement date is 2026-04-16 with average estimated EPS of $0.76 for the fiscal quarter ending 2026-03-31.
- Nasdaq's earnings page was reachable but low quality for this run because most fields rendered as unavailable; it did not materially improve the estimate.

## Evidence directly stated by source

### SEC EDGAR filing index
- Netflix 10-K filing date: 2026-01-23.
- Filing accession: 0001065280-26-000034.
- Primary document: `nflx-20251231.htm`.

### AlphaQuery earnings history
- Next expected announcement date: 2026-04-16.
- Average estimated EPS for quarter ending 2026-03-31: $0.76.
- Last announced EPS for quarter ending 2025-12-31: $0.56.

### Macrotrends EPS history
- Quarterly diluted EPS history rose as high as $0.72 in Q2 2025 but fell to $0.56 in Q4 2025, showing recent volatility around the market strike neighborhood rather than a straight-line beat pattern.

## What is uncertain

- I was not able to retrieve Netflix investor-relations guidance or a current shareholder letter directly because some primary IR pages returned anti-bot/403 responses through the fetch layer.
- AlphaQuery is a contextual aggregator, not a settlement source; it is useful for date/consensus context but not authoritative for final resolution.
- The SEC 10-K is authoritative for historical company reporting quality and recent reported results, but it does not directly settle Q1 2026 EPS before the company releases earnings.

## Why this source may matter

These sources jointly establish three things needed for this case: the company and reporting surface are unambiguous; the relevant earnings window is plausibly 2026-04-16; and the strike of $0.76 sits only modestly above some recent quarterly diluted EPS prints rather than far below an obviously dominant run-rate.

## Possible impact on the question

This source set supports a cautious variant view against the market's 94.5% implied probability. The market may be overconfident because the contract is not yet directly settled, the earnings date still has timing dependency, and recent diluted EPS history does not show a persistent margin above the $0.76 strike.

## Reliability notes

- Primary-source quality: SEC EDGAR high for company identity and historical filings.
- Key contextual source quality: AlphaQuery medium; useful for expected date and consensus but not authoritative.
- Evidence independence: medium at best because contextual earnings pages often inherit consensus data from overlapping analyst-estimate ecosystems.
- Source-of-truth ambiguity: low for final settlement once Netflix releases official earnings documents, but medium pre-release because third-party consensus pages are not the governing source.
