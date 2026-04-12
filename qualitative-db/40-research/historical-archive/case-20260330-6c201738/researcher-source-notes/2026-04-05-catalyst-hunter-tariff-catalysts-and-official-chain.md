---
type: source_note
case_key: case-20260330-6c201738
dispatch_id: dispatch-case-20260330-6c201738-20260405T212516Z
analysis_date: 2026-04-05
persona: catalyst-hunter
domain: trade-policy
subdomain: tariffs
entity: united-states-china-trade
topic: case-20260330-6c201738 | catalyst-hunter
question: Will the U.S. tariff rate on China be between 5% and 15% on March 31, 2026?
driver: official-order-timing
date_created: 2026-04-05
source_name: White House / USTR China tariff action chain plus contract timing logic
source_type: official executive actions + official trade-policy index + contract surface
source_url: https://ustr.gov/trade-topics/presidential-tariff-actions
source_date: 2025-03-03 to 2025-11-04
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [china, united-states, white-house, ustr]
related_drivers: [official-order-timing, paused-vs-in-effect-orders, tariff-stack-calculation, source-hierarchy]
upstream_inputs: []
downstream_uses: [orchestrator-synthesis]
tags: [official-source, catalysts, timing, tariffs, china]
---

# Summary

The key catalyst question is not the current headline tariff number but which later official event could still move the market into or out of the 5% to 15% band by March 31, 2026. The official action chain reviewed here implies that by late 2025 China still had at least two broad 10% layers in effect: a reciprocal-tariff layer and a synthetic-opioid-related PRC layer. That puts the operative stack above 15% unless later official action removes one layer, clarifies non-additivity, or legal/administrative implementation changes what is actually in effect at the checkpoint.

## Key facts extracted

- White House March 3, 2025 order raised the PRC synthetic-opioid-related duty from 10% to 20%.
- White House May 12, 2025 order made the PRC reciprocal layer 10% effective May 14, 2025 while suspending additional percentage points.
- White House August 11, 2025 order extended the reciprocal suspension through November 10, 2025.
- White House November 4, 2025 order extended the reciprocal suspension through November 10, 2026, leaving the 10% reciprocal layer in effect.
- White House November 4, 2025 order also reduced the synthetic-opioid-related PRC duty from 20% to 10% effective November 10, 2025.
- The Polymarket contract says to count only tariffs in effect, exclude paused or merely announced tariffs, exclude item-specific exceptions/increases, and use official Trump-administration information as the primary source of truth.

## Evidence directly stated by source

- Effective dates are explicit for both the reciprocal and synthetic-opioid tariff changes.
- The heightened reciprocal rates were suspended, but the residual 10% reciprocal layer remained in force.
- The synthetic-opioid PRC duty was reduced, not eliminated, to 10%.
- The contract’s additive example implies multiple general tariffs can be summed when simultaneously in effect.

## What is uncertain

- Whether any later White House / USTR action before March 31, 2026 removes one of the 10% China-wide layers.
- Whether a court or implementation change alters what is officially considered “in effect” by the checkpoint.
- Whether the resolver will aggregate both broad China-wide layers exactly as the contract’s example suggests.

## Why this source may matter

This source cluster identifies the actual repricing catalysts. The market is unlikely to move materially because of vague trade rhetoric alone. It should move if and when there is a concrete official action affecting one of the two broad China-wide layers, or an authoritative implementation clarification showing whether both layers count simultaneously.

## Possible impact on the question

As of the official chain reviewed, the live stack looks above the 5% to 15% band, favoring No. The main path to Yes is future catalyst-driven: an official rollback, legal displacement, or implementation clarification that leaves only one 10% general layer operative at noon ET on March 31, 2026.

## Reliability notes

High reliability on timing, source hierarchy, and what was formally in effect at the cited dates because the core materials are White House orders and an official USTR index. Remaining uncertainty is chiefly forward-looking and interpretive, not documentary.