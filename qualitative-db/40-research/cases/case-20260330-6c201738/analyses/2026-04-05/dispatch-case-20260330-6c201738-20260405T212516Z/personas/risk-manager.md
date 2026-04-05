---
type: agent_finding
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
stance: no
certainty: medium
importance: high
novelty: medium
time_horizon: through-2026-03-31
related_entities: [china, united-states, white-house, federal-register, cbp]
related_drivers: [tariff-policy-implementation-timing, source-of-truth-hierarchy, tariff-stacking-logic]
upstream_inputs: []
downstream_uses: [controller-synthesis]
tags: [risk-manager, tariff, china, polymarket, resolution-risk, source-of-truth]
---

# Claim

The market should currently lean **NO**. The strongest official evidence indicates the U.S. general tariff rate on China was already above the 5%-15% band by April 2025, likely at least **30%** under the contract’s own stacking logic (20% China-wide additional duty plus 10% all-country baseline tariff). The main risk is not that the current level is near 10%; it is that later official changes before March 31, 2026 could alter the stack or create resolution ambiguity.

## Market-implied baseline

Current price is **0.959**, implying about **95.9%** probability for the market side currently favored by price. Since the market page fetched here shows final outcome “No” and the assignment asks me to compare against current_price, I treat the market as implying **roughly 95.9% NO / 4.1% YES**.

Embedded confidence is very high. That confidence looks directionally justified, but still somewhat fragile because it compresses real source-of-truth and timing risk into a near-certain price.

## Own probability estimate

**NO 90% / YES 10%**.

## Agreement or disagreement with market

I **roughly agree** with the market directionally, but I am a bit less confident than the market.

Why I am below the market:
- this is a high-resolution-risk contract with explicit timing and exclusion rules;
- tariff policy can be changed by later official action before March 31, 2026;
- there is some source-of-truth ambiguity around how overlapping tariff authorities are ultimately described for resolution.

Why I still agree on direction:
- the current official framework appears far above the 5%-15% band, not marginally above it;
- the contract itself explicitly instructs additive logic for a broad all-import tariff plus a China-on-top tariff;
- the China-specific duty alone reached 20% in March 2025, already above the band before adding the universal baseline announced for April 2025.

## Implication for the question

Absent a later explicit rollback or non-stacking clarification, this market should resolve **No** because the countable general tariff rate on China appears structurally above 15%, not inside the 5%-15% range.

## Key sources used

1. **Primary / authoritative / direct:** White House EO 14195 (Feb. 1, 2025) imposing an additional 10% tariff on PRC products effective Feb. 4, 2025.
2. **Primary / authoritative / direct:** White House EO 14228 (Mar. 3, 2025) raising that PRC-wide additional duty from 10% to 20%.
3. **Primary / authoritative / direct:** White House EO 14257 / Federal Register publication (Apr. 2 / Apr. 7, 2025) establishing a 10% tariff on all countries effective Apr. 5, 2025 and a higher individualized reciprocal structure beginning Apr. 9, 2025.
4. **Primary / authoritative / contextual boundary source:** White House / Federal Register EO 14256 concerning low-value PRC imports and de minimis treatment, mainly used to separate special-case treatment from the market’s “general tariff rate.”
5. **Context / market contract surface:** Polymarket market description specifying what counts, what does not count, the in-effect requirement, and the official-source hierarchy.
6. **Supporting provenance artifact:** `qualitative-db/40-research/cases/case-20260330-6c201738/source-notes/2026-04-05-risk-manager-white-house-and-federal-register-tariff-orders.md`

**Governing source of truth:** the market says primary resolution source is **official information from the Trump administration**, with consensus of credible information as fallback/support. So the governing source hierarchy here is: official White House / Federal Register / implementing executive materials first, then credible consensus reporting if official materials are incomplete or conflicting.

## Supporting evidence

- **China-specific broad tariff already at 20%:** EO 14195 created an additional 10% tariff on PRC goods; EO 14228 amended it to 20%. That alone is above the 5%-15% band.
- **General all-country tariff layer added in April 2025:** the White House fact sheet for EO 14257 states Trump will impose a 10% tariff on all countries effective Apr. 5, 2025.
- **Contract wording explicitly supports stacking:** the market description says a general tariff on all imports plus an extra tariff on Chinese imports should be added together.
- **In-effect timing appears satisfied for the checked orders:** the orders specify concrete effective timestamps rather than merely announcing future intent.

## Counterpoints / strongest disconfirming evidence

The strongest disconfirming consideration is **not evidence that the tariff is currently in the band**; it is that **later official modifications before March 31, 2026 could materially reduce or restructure the countable China tariff stack**. Federal Register listings show multiple later 2025 modifications touching reciprocal tariff rates and China, which means the April 2025 structure is not guaranteed to remain unchanged through resolution.

## Resolution or source-of-truth interpretation

### What counts

- Broad general tariffs in effect on imports into the U.S. from China.
- A universal all-country tariff plus an additional China-wide tariff, if both remain in effect.
- Official Trump administration source material takes priority.

### What does not count

- Item-specific exceptions or increases.
- “Effective tariff rate” concepts based on product mix.
- Paused tariffs.
- Announced but not yet effective tariffs.

### How the contract wording affects the view

This wording strongly favors a **stacked general-rate interpretation**, not a trade-weighted or item-specific one. That matters a lot: a 20% China-wide broad duty plus a 10% all-country baseline is enough by itself to push the market well outside the YES band.

### Case-specific check: verify in effect timing

Addressed. The official orders I relied on include explicit effective times:
- PRC tariff effective Feb. 4, 2025;
- amended to 20% on Mar. 3, 2025;
- 10% all-country tariff effective Apr. 5, 2025.

### Case-specific check: exclude paused announcements

Addressed. I did not rely on mere announcements. I relied on executive orders / Federal Register publications with effective dates. I also treated the de minimis history carefully because one earlier removal of duty-free treatment had been suspended before later re-implementation; I did **not** use that as core support for the main general-tariff calculation.

### Case-specific check: confirm source hierarchy

Addressed. Primary weight goes to official Trump administration materials and Federal Register publication of those orders. Market description itself confirms that official administration information is primary.

### Case-specific check: validate rate calculation logic

Addressed. The key logic is additive:
- China-wide broad tariff = 20%
- broad all-country baseline tariff = 10%
- implied general China tariff under the contract’s example = **30%**
This is the central mechanism behind the NO view.

## Key assumptions

- The market’s stacking example applies to these broad tariff layers.
- The 20% China-wide opioid-order tariff remains a countable general tariff rather than being superseded for resolution purposes.
- No later official rollback before March 31, 2026 moves the countable rate back into 5%-15%.

## Why this is decision-relevant

This market is priced near certainty. The risk-manager contribution is that the likely error is **overconfidence**, not direction. A trader or synthesizer should treat this as a high-probability NO with a nontrivial tail for later policy modification or settlement confusion rather than as a zero-risk lock.

## What would falsify this interpretation / change your mind

I would revise materially toward YES if I saw any of the following from the governing source class:
- a later official Trump administration order or implementation notice reducing China’s countable general tariff into the 5%-15% band by March 31, 2026;
- explicit official guidance that the broad all-country tariff does **not** stack with the China-wide tariff for this purpose;
- an official statement naming a lower general tariff rate for China that clearly overrides the additive reading.

## Source-quality assessment

- **Primary source used:** White House executive orders and their Federal Register publication.
- **Most important secondary/contextual source used:** the Polymarket market description itself, because this is a wording-sensitive contract.
- **Evidence independence:** **medium**. The core evidence comes from multiple official surfaces but largely from the same executive-policy chain.
- **Source-of-truth ambiguity:** **medium**. The contract names official administration info as primary, but overlapping tariff authorities and later modifications can create interpretation risk.

## Verification impact

- **Additional verification pass performed:** yes.
- **What I checked:** Federal Register publication status for the reciprocal order, the amended China opioid-order sequence, and whether I was accidentally relying on paused or merely announced tariffs.
- **Did it materially change the view?** No material directional change.
- **Impact:** it increased confidence that the core NO case rests on in-effect official measures, while preserving uncertainty around later modifications before the 2026 resolution date.

## Evidence floor / compliance notes

- **Difficulty / evidence floor:** high-complexity and rule-sensitive case.
- **Meaningful sources used:** at least three.
  1. EO 14195 (official primary)
  2. EO 14228 (official primary)
  3. EO 14257 / Federal Register publication + White House fact sheet (official primary)
  4. EO 14256 for boundary clarification (official contextual)
  5. Polymarket contract text for resolution mechanics
- **Provenance preserved via:** one substantive source note, one assumption note, one evidence map, and this finding with explicit source list.
- **Checklist compliance:** market-implied probability stated, own estimate stated, strongest disconfirming consideration stated, what could change my mind stated, governing source of truth stated, source-quality assessment included, verification impact included, reusable lesson signals included, Orchestrator review suggestions included, what counts/does not count explained, extra verification performed, and all four case-specific checks addressed explicitly.

## Reusable lesson signals

- Possible durable lesson: for tariff markets, the biggest mistake risk is often confusing **headline policy announcements** with **in-effect countable tariff layers**.
- Possible missing or underbuilt driver: a reusable driver around **tariff stacking vs. supersession mechanics** may be worth tracking if similar contracts recur.
- Possible source-quality lesson: Federal Register publication is useful as a confirmation layer when White House pages are truncated or hard to parse, but it is not independent from the underlying executive action.
- Confidence that any lesson here is reusable: **medium**.

## Orchestrator review suggestions

- review later for durable lesson: **yes**
- review later for driver candidate: **yes**
- review later for canon or linkage issue: **no**
- one-sentence reason: repeated tariff markets are likely to benefit from a reusable method note on in-effect timing, stacking, and official-source hierarchy.

## Recommended follow-up

- Before any final pre-resolution synthesis, re-check later 2025-2026 official orders or CBP/HTSUS implementation notices for any rollback, pause, or non-stacking clarification affecting China’s broad tariff layers.
