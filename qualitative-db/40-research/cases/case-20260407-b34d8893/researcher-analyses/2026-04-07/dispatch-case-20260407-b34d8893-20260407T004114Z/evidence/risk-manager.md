---
type: evidence_map
case_key: case-20260407-b34d8893
dispatch_id: dispatch-case-20260407-b34d8893-20260407T004114Z
research_run_id: d761046a-6013-46f9-8f13-f0356f28481c
analysis_date: 2026-04-07
persona: risk-manager
domain: crypto
subdomain: institutions
entity: strategy
topic: "strategy april 6 purchase announcement"
question: "Will Microstrategy announce a Bitcoin purchase March 31-April 6?"
date_created: 2026-04-07
agent: orchestrator
status: draft
confidence: high
conflict_status: low
action_relevance: high
related_entities: ["strategy", "bitcoin"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["official-company-announcement-cadence"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260407-b34d8893/researcher-analyses/2026-04-07/dispatch-case-20260407-b34d8893-20260407T004114Z/personas/risk-manager.md"]
tags: ["evidence-netting", "official-source", "low-complexity"]
driver:
---

# Summary

The evidence nets strongly to "Yes" because the official Strategy purchases page directly shows an April 6, 2026 purchase announcement entry and links the supporting 8-K. The remaining risk is mostly mechanical: whether the market treats that official page/linked filing as qualifying and whether any timing edge case exists. Those risks look small.

## Question being evaluated

Will Microstrategy announce that it acquired additional Bitcoin between March 31 and April 6, 2026, inclusive?

## Current lean

Strong yes.

## Prior / starting view

Start from market price 0.9485 (~94.85% implied yes) and the known recurring Strategy Monday announcement cadence.

## Evidence supporting the claim

- Official Strategy purchases page shows an "April 2026" entry with `date_of_purchase` 2026-04-06 and 4,871 BTC acquired.
  - Direct official evidence.
  - High weight because it is company-controlled and directly on the resolution question.
- Same page links `form-8-k_04-06-2026.pdf`.
  - Direct official corroboration.
  - High weight because it supports that the company treated this as formal disclosure.
- Same page contains company-authored acquisition summary text for the April 6 purchase.
  - Direct official evidence.
  - Medium-to-high weight.
- Polymarket page indicates the market itself is trading at an extreme yes level and says official company information is the source of truth.
  - Contextual rather than dispositive.
  - Low-to-medium weight.

## Evidence against the claim

- Extracted page text via simple fetch was initially thin, meaning a shallow read could have missed the decisive data.
  - This is a tooling/auditability issue, not substantive counterevidence.
  - Low weight.
- A narrow timing objection could arise if someone argued the relevant announcement was posted outside the market window despite the row date.
  - This is the main residual risk.
  - Low weight absent contrary timestamp evidence.

## Ambiguous or mixed evidence

- The purchases page uses both a purchase date field and company summary text. In some markets, execution date vs announcement date matters. Here the rules say announcements made within the designated window govern resolution, regardless of when purchases were made.

## Conflict between inputs

No meaningful factual conflict found. The only issue was needing a deeper page inspection to expose the official structured data.

## Key assumptions

- Official Strategy website + linked 8-K counts as qualifying official company information.
- The April 6 entry reflects an announcement within the window relevant to resolution.

## Key uncertainties

- Whether a reviewer would insist on parsing the linked 8-K body for exact posting time, despite the official page already surfacing the entry on April 6.

## Disconfirming signals to watch

- Official correction or removal of the April 6 purchase entry.
- Market resolution discussion surfacing a timestamp problem.
- Official clarification that the page entry was posted after the window closed.

## What would increase confidence

- Direct parse of the linked 8-K body and/or filing timestamp.
- Confirmed official Michael Saylor/Strategy X post timestamp matching the page entry.

## Net update logic

The case moved from "highly likely yes because Strategy often announces weekly purchases" to "effectively settled yes" once the official purchases page revealed a dated April 6 purchase row with the linked 8-K.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- retrospective evaluation of how often official dynamic pages need structured-data extraction rather than plain readability fetches
