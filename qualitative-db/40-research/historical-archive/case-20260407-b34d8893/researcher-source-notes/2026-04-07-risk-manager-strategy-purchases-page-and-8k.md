---
type: source_note
case_key: case-20260407-b34d8893
dispatch_id: dispatch-case-20260407-b34d8893-20260407T004114Z
analysis_date: 2026-04-07
persona: risk-manager
domain: crypto
subdomain: institutions
entity: strategy
topic: strategy bitcoin purchase announcement cadence
question: Will Microstrategy announce a Bitcoin purchase March 31-April 6?
date_created: 2026-04-07
source_name: Strategy purchases page with linked April 6, 2026 8-K
source_type: official company website / linked SEC filing
source_url: https://www.strategy.com/purchases
source_date: 2026-04-06
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: high
agent: orchestrator
related_entities: [strategy, bitcoin]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260407-b34d8893/researcher-analyses/2026-04-07/dispatch-case-20260407-b34d8893-20260407T004114Z/personas/risk-manager.md]
tags: [official-source, company-announcement, website-verification, 8-k]
---

# Summary

Strategy's official purchases page contains structured page data for an entry labeled "April 2026" with `date_of_purchase` = `2026-04-06`, `count` = `4871`, `purchase_price` = `67718`, `btc_holdings` = `766970`, `total_purchase_price` = `330000000`, and a linked PDF titled `form-8-k_04-06-2026.pdf`. The same entry includes company-authored social copy: "@Strategy has acquired 4,871 BTC for ~$329.9 million at ~$67,718 per bitcoin. As of 4/5/2026, we hold 766,970 $BTC acquired for ~$58.02 billion at ~$75,644 per bitcoin. $MSTR $STRC".

## Key facts extracted

- Official page title: "Bitcoin Purchases - Strategy".
- Structured page payload includes an "April 2026" row.
- That row records a purchase announcement dated `2026-04-06`.
- Reported acquisition amount: 4,871 BTC.
- Reported total purchase price: about $330 million.
- Holdings after purchase: 766,970 BTC as of 4/5/2026.
- The row links to an official PDF asset titled `form-8-k_04-06-2026.pdf`.
- The company-authored text on the page explicitly says Strategy "has acquired 4,871 BTC".

## Evidence directly stated by source

Direct official-company evidence:
- The purchases page is an official Strategy-controlled source.
- It directly states the acquisition figures and date.
- It directly hosts/linkes the corresponding April 6, 2026 8-K PDF.
- It directly includes company-authored announcement text summarizing the purchase.

## What is uncertain

- I did not separately parse the PDF body within this note; I relied on the official purchases page metadata plus the linked-file presence.
- The market wording says resolution uses official information from MicroStrategy or Michael Saylor; this source clearly qualifies as official company information, but settlement mechanics are still controlled by the market operator.

## Why this source may matter

This is the governing evidence class for this market: official information from the company. It is both recent and directly on-point, and it addresses the exact timing window in the title.

## Possible impact on the question

This source strongly supports "Yes" because it shows an official company announcement on April 6, 2026 that Strategy acquired additional Bitcoin, which falls inside the March 31-April 6 market window.

## Reliability notes

- Primary source quality: high.
- Independence: low-to-medium if paired only with the linked 8-K, because both originate from the same issuer, but that is acceptable here because the rules explicitly make official company information the source of truth.
- Best use: direct settlement / confirmation, not broad contextual inference.
