---
type: source_note
case_key: case-20260413-9c835dfe
dispatch_id: dispatch-case-20260413-9c835dfe-20260413T162509Z
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: crypto
subdomain: corporate-bitcoin-treasury
entity: btc
topic: strategy bitcoin purchases page update
question: Did Strategy announce a purchase of more than 1000 BTC during April 7-13, 2026?
driver: reliability
date_created: 2026-04-13
source_name: Strategy purchases page
source_type: company website / investor relations tracker
source_url: https://www.strategy.com/purchases
source_date: 2026-04-13
credibility: high
recency: same-day
stance: supports-yes
certainty: high
importance: high
novelty: high
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-9c835dfe/researcher-analyses/2026-04-13/dispatch-case-20260413-9c835dfe-20260413T162509Z/personas/catalyst-hunter.md]
tags: [strategy, bitcoin-purchases, official-source, timing]
---

# Summary

Strategy's official purchases page updated on April 13, 2026 with a new row showing a purchase announcement above the market threshold.

## Key facts extracted

- The latest row on the official purchases page is dated `2026-04-13`.
- It reports `count: 13927` BTC and `btc_holdings: 780897`.
- The linked SEC filing is `form-8-k_04-13-2026.pdf`.
- The row includes official company social copy: `@Strategy has acquired 13,927 BTC for ~$1.00 billion ... As of 4/12/2026, we hodl 780,897 BTC ...`.
- The page metadata shows publish time around `2026-04-13T12:01:30Z`, consistent with an announcement inside the market window.

## Evidence directly stated by source

The source directly states that Strategy announced acquisition of 13,927 BTC on April 13, 2026, comfortably above the >1000 BTC threshold.

## What is uncertain

- The purchases page is an official company surface, but the exact market wording says the resolution source is official information from MicroStrategy or Michael Saylor; that means this page should be checked against an explicit company press/SEC-linked surface as an extra verification pass.
- The market resolves on announcement timing, not purchase timing; the page implies same-day announcement but does not itself reproduce the full resolution rule.

## Why this source may matter

This is the cleanest company-maintained tracker for Strategy/MicroStrategy bitcoin purchase announcements and directly addresses both size and timing.

## Possible impact on the question

Strongly supports YES because it shows an official company announcement on April 13, 2026 for a 13,927 BTC acquisition, which is well above the required threshold and inside the April 7-13 ET window.

## Reliability notes

High-quality primary source, but still worth pairing with the linked SEC filing or press archive because the market was trading at an extreme probability and the contract explicitly names official company information as source of truth.