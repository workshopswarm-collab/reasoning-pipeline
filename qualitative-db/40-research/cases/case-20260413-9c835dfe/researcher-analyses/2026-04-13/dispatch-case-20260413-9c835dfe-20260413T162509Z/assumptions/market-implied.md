---
type: assumption_note
case_key: case-20260413-9c835dfe
research_run_id: 6edf651b-6373-44a6-838c-5444cf21da1d
analysis_date: 2026-04-13
persona: market-implied
domain: crypto
subdomain: institutions
entity: strategy
topic: microstrategy-announces-1000-btc-purchase-april-7-13
question: "MicroStrategy announces >1000 BTC purchase April 7-13?"
date_created: 2026-04-13
agent: market-implied
status: active
certainty: medium
importance: high
time_horizon: near-term
related_entities: ["strategy", "bitcoin"]
related_drivers: []
proposed_entities: ["michael-saylor"]
proposed_drivers: ["official-disclosure-timing"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-9c835dfe/researcher-analyses/2026-04-13/dispatch-case-20260413-9c835dfe-20260413T162509Z/personas/market-implied.md"]
tags: ["assumption", "resolution-logic", "timing"]
dispatch_id: dispatch-case-20260413-9c835dfe-20260413T162509Z
driver:
---

# Assumption

A refreshed official Strategy holdings/purchases surface dated 2026-04-13 is not automatically equivalent to a contract-qualifying announcement unless the purchase attribution and in-window announcement timing are clear from Strategy or Michael Saylor.

## Why this assumption matters

The entire gap between the market's 96% Yes price and my lower estimate comes from whether traders are correctly treating live official-site updates as sufficient announcement evidence.

## What this assumption supports

- A more cautious probability than the market.
- Emphasis on source-of-truth wording and timing rather than just inferred holdings changes.
- Explicit treatment of official-site metrics as strong but not fully dispositive evidence in this run.

## Evidence or logic behind the assumption

- The contract resolves on announcements made in the designated time frame, regardless of purchase date.
- The contract names official information from MicroStrategy/Strategy or Michael Saylor as the resolution source.
- In this run, I observed official current holdings data and a purchases surface, but not a clearly extracted dated announcement text stating a >1000 BTC purchase within Apr 7-13 ET.

## What would falsify it

- A dated row, post, press release, or official site statement from Strategy or Michael Saylor within Apr 7-13 ET clearly stating a purchase >1000 BTC.
- Clear resolution guidance that the official purchases page update itself counts as the required announcement even without separate prose.

## Early warning signs

- Discovery of an archived `/purchases` entry with an Apr 13 timestamp.
- A Michael Saylor X post linking to or restating the purchase.
- Any official SEC-linked disclosure or investor-relations note cited by the company during the window.

## What changes if this assumption fails

My estimate should move sharply upward toward the market, likely into the 90%+ range.

## Notes that depend on this assumption

- Main finding at the assigned persona path.