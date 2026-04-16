---
type: source_note
case_key: case-20260415-ba1899b5
dispatch_id: dispatch-case-20260415-ba1899b5-20260415T121723Z
analysis_date: 2026-04-15
persona: risk-manager
domain: economics
subdomain: corporate-earnings
entity: netflix
topic: nflx-quarterly-earnings-gaap-eps-04-16-2026-0pt76
question: Will Netflix Inc (NFLX) beat quarterly earnings?
driver: reliability
date_created: 2026-04-15
source_name: SEC EDGAR company filings page for Netflix 8-Ks
source_type: primary-source-index
source_url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1065280&type=8-k&owner=exclude&count=20
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [netflix, sec]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [risk-manager-finding]
tags: [source-note, sec, earnings-timing, resolution]
---

# Summary

SEC EDGAR provides the authoritative filing trail for Netflix earnings releases and is the cleanest primary-source route for verifying whether Netflix actually reports the relevant quarter within the contract window.

## Key facts extracted

- The SEC EDGAR results page for Netflix shows regular earnings-related 8-K filings under item 2.02.
- The most recent listed earnings 8-K before this market window was filed on 2026-01-20.
- Prior earnings-related 8-Ks shown include 2025-10-21, 2025-07-17, 2025-04-17, 2025-01-21, 2024-10-17, 2024-07-18, and 2024-04-18.
- This cadence supports the expectation that Netflix normally reports quarterly earnings in mid-April, mid-July, mid-October, and mid-January.

## Evidence directly stated by source

- EDGAR explicitly lists filing dates and item classifications for Netflix 8-Ks.
- The January 20, 2026 filing is labeled as item 2.02 and 9.01, which is the standard earnings-release filing pattern.

## What is uncertain

- The EDGAR index page alone does not provide the Q1 2026 GAAP EPS figure because the relevant April 2026 filing has not yet occurred.
- The EDGAR page does not itself prove the exact April 2026 report date; it supports timing expectations from historical cadence.

## Why this source may matter

- The contract resolves from the company's official earnings documents if available, so SEC-filed earnings materials are central to the source-of-truth hierarchy.
- Historical cadence helps test whether the market may be underpricing timing/report-window failure risk.

## Possible impact on the question

This source reduces uncertainty around the reporting-window condition because Netflix appears to file earnings releases on a stable quarterly cadence, making a total miss of the reporting window look low probability.

## Reliability notes

- Primary and authoritative for filing existence and dates.
- Strong for timing verification and settlement-source hierarchy.
- Weak for the actual beat/no-beat outcome before the April 2026 earnings release is published.
