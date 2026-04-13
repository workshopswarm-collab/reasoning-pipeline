---
type: assumption_note
case_key: case-20260413-9c835dfe
dispatch_id: dispatch-case-20260413-9c835dfe-20260413T162509Z
research_run_id: 543bb9e8-4b94-4eba-a73c-6475f6455b18
analysis_date: 2026-04-13
persona: base-rate
domain: crypto
subdomain: corporate-bitcoin-treasury
entity:
topic: "resolution timing and official-source assumption"
question: "MicroStrategy announces >1000 BTC purchase April 7-13?"
driver:
date_created: 2026-04-13
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: immediate
related_entities: ["strategy", "bitcoin"]
related_drivers: ["reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["assumption", "resolution-interpretation", "official-source"]
---

# Assumption

The official Strategy purchases-page entry dated 2026-04-13 counts as an eligible company announcement within the market window, absent evidence that it was posted after 11:59 PM ET or otherwise excluded by market rules.

## Why this assumption matters

The case is mostly resolved by source-of-truth mechanics rather than by uncertain forecasting. If the purchases-page disclosure is in-window and eligible, the contract is overwhelmingly YES.

## What this assumption supports

- A near-certain YES estimate.
- Agreement with the extreme market pricing.
- Treating the market as effectively resolved in substance, though not necessarily yet formally settled.

## Evidence or logic behind the assumption

The market description explicitly says resolution is based on official information from MicroStrategy or Michael Saylor and separately references the Strategy purchases page as a tracking source. The purchases page shows a 2026-04-13 entry for 13,927 BTC with linked SEC filing metadata, which is exactly the sort of official disclosure the contract appears designed to capture.

## What would falsify it

- Evidence that the official posting occurred after the contract window ended.
- A clarified market rule saying the purchases page does not count unless mirrored in another specific channel.
- A correction/retraction by Strategy or Michael Saylor showing the entry was erroneous.

## Early warning signs

- Resolution admins flagging timing ambiguity.
- Official company clarification that the entry was backdated or posted outside the relevant window.
- A later filing materially revising the reported BTC count below the threshold.

## What changes if this assumption fails

The probability would fall sharply because the case would revert from an apparent official disclosure to a contract-interpretation dispute about what counts as an announcement.

## Notes that depend on this assumption

- Main base-rate finding for this dispatch.
- Any later synthesis that treats the market as substantively resolved YES.
