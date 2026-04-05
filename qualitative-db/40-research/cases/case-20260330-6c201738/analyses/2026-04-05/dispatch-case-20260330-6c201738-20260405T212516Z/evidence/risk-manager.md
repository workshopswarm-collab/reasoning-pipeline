---
type: evidence_map
case_key: case-20260330-6c201738
dispatch_id: dispatch-case-20260330-6c201738-20260405T212516Z
research_run_id: 25f730d5-986b-4c75-90e3-dbfdb5868416
analysis_date: 2026-04-05
persona: risk-manager
domain: geopolitics
subdomain: us-trade-policy
entity: united-states-china-trade
topic: case-20260330-6c201738 | risk-manager
question: Will the U.S. tariff rate on China be between 5% and 15% on March 31?
driver: tariff-policy-implementation-timing
date_created: 2026-04-05
agent: Orchestrator
status: draft
confidence: medium
conflict_status: limited-interpretive-conflict
action_relevance: high
related_entities: [china, united-states, white-house, federal-register]
related_drivers: [tariff-policy-implementation-timing, source-of-truth-hierarchy, tariff-stacking-logic]
upstream_inputs: []
downstream_uses: [risk-manager-finding]
tags: [evidence-map, tariff, china, timing, resolution-risk]
---

# Summary

The current lean is strongly NO because the official orders already establish countable tariff layers above the 5%-15% band. The main risk is not directional but interpretive: whether later official guidance changes stacking, timing, or source-of-truth treatment before the market’s March 31, 2026 timestamp.

## Question being evaluated

Will the U.S. tariff rate on China be between 5% and 15% on March 31, 2026, 12:00 PM ET, under the market’s definition of “general tariff rate” and exclusions?

## Current lean

Lean NO. The countable general rate appears well above 15%, likely at least 30% based on official orders already in effect in April 2025.

## Prior / starting view

Starting expectation: market likely correct directionally because price is 0.959, but needed stress-testing on timing, paused announcements, and stacking mechanics because contract wording is fragile.

## Evidence supporting the claim

1. **Market contract stacking example** — direct, high weight
   - The contract says a tariff on all imports plus a tariff on top of that on Chinese imports should be added.
   - Why it matters: directly supports stacked-rate interpretation.

2. **EO 14195 + EO 14228 set China-wide additional tariff at 20%** — direct official evidence, very high weight
   - Products of the PRC became subject to 10% effective Feb. 4, 2025, later raised to 20% on Mar. 3, 2025.
   - Why it matters: already puts general China tariff above the YES band unless that layer later disappears.

3. **EO 14257 / White House fact sheet imposes 10% tariff on all countries effective Apr. 5, 2025** — direct official evidence, high weight
   - Why it matters: if counted alongside China-specific 20%, total is at least 30%.

4. **Official language says these duties are in effect until modified/terminated** — direct official evidence, medium-high weight
   - Why it matters: reduces the chance that these were just announcements or temporary headlines.

## Evidence against the claim

1. **Later policy changes could materially revise China tariff treatment before Mar. 31, 2026** — indirect but important, medium weight
   - Tariff policy is politically adjustable and several later 2025 Federal Register entries indicate subsequent modifications to reciprocal tariffs involving China.
   - Why it matters: the question resolves far after the April 2025 launch point.

2. **Source-of-truth ambiguity around which official surface names the final ‘general tariff rate’** — interpretive, medium weight
   - The contract prefers official Trump administration information but also allows consensus of credible information.
   - Why it matters: overlapping authorities and special regimes can create settlement disputes.

3. **Special treatment paths (de minimis/postal) can confuse what counts as ‘general’** — indirect, low-medium weight
   - Why it matters: although likely excluded from the clean “general tariff” calculation, they create noise that could mislead analysts or settlers.

## Ambiguous or mixed evidence

- Federal Register 2025 listings show later reciprocal-tariff modifications involving China in April and May 2025, but without reading those full documents here, they are warning signals rather than estimate-moving facts.
- USTR’s legacy Section 301 page is not very informative for this case because the market definition excludes item-specific increases/effective tariff considerations.

## Conflict between inputs

- No hard factual conflict found in the sources checked.
- Main disagreement is interpretive: whether the market should count overlapping broad tariffs cumulatively.
- Evidence that would resolve it: later CBP/HTSUS implementation guidance or a direct official statement specifying China’s general tariff rate as of the target date.

## Key assumptions

- Stacking logic in the market description should be applied to the China-wide 20% layer plus the all-country 10% layer.
- No later rollback reduces the countable rate back into the 5%-15% band by March 31, 2026.
- Item-specific exceptions should not dominate settlement because the contract excludes them.

## Key uncertainties

- Whether later 2025-2026 modifications materially lower the China-wide countable general rate.
- Whether resolution administrators use a clean additive interpretation or some narrower official label.

## Disconfirming signals to watch

- Official rollback, pause, or termination of either broad tariff layer before March 31, 2026.
- Official clarification that one broad tariff supplants rather than adds to another for China.
- Official source explicitly stating a China general tariff rate inside the 5%-15% band.

## What would increase confidence

- A CBP or HTSUS implementation notice explicitly showing the stacked China-wide treatment.
- A later official Trump administration source affirming no rollback of the broad China layers through the target date.

## Net update logic

The main update was not discovering a hidden positive case for YES; it was confirming that the official mechanics already sit well above the target band and that the relevant downside is settlement/interpretation risk, not substantive evidence that the tariff is actually near 10%. That leaves a high-probability NO, but with residual caution because tariff policy can be revised and the market resolves at a much later date.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review focused on resolution mechanics and later-official-source monitoring
