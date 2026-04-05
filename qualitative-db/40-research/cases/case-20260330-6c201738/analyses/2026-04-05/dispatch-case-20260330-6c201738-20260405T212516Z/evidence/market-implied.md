---
type: evidence_map
case_key: case-20260330-6c201738
dispatch_id: dispatch-case-20260330-6c201738-20260405T212516Z
research_run_id: dbdd6dfe-eebd-498f-a9e1-1f69619d2e74
analysis_date: 2026-04-05
persona: market-implied
topic: case-20260330-6c201738 | market-implied
question: Will the U.S. tariff rate on China be between 5% and 15% on March 31, 2026, 12:00 PM ET?
date_created: 2026-04-05
agent: Orchestrator
status: draft
confidence: medium-high
conflict_status: low-to-medium interpretive conflict
action_relevance: high
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [tariff, china, evidence-map, timing, source-hierarchy]
---

# Summary

The market price near 95.9% appears to be implicitly treating the relevant general tariff rate as 10%, not 20%. After tracing the official action chain, I think that interpretation is too narrow. The strongest evidence suggests two general China-wide tariffs were simultaneously in effect by the checkpoint: 10% reciprocal + 10% synthetic-opioid, for a combined 20%.

## Question being evaluated

Whether the U.S. general tariff rate on China at March 31, 2026 noon ET falls between 5% and 15%, under a contract that counts tariffs in effect, excludes paused or merely announced tariffs, and excludes item-specific exceptions or increases.

## Current lean

Lean No. The best reading is that the operative general tariff rate is 20%.

## Prior / starting view

Start from the market at 95.9% Yes, implying the market likely believes either (a) only one 10% China-wide tariff counts, or (b) one of the China-wide duties is not properly part of the contract’s “general tariff rate.”

## Evidence supporting the claim

- Market price itself at 0.959.
  - Why it matters: strong prior that traders may already have checked the resolution wording and official tariff chain.
  - Direct or indirect: indirect.
  - Weight: moderate as a prior, but not decisive against contradictory primary documents.

- May 12, 2025 White House / Geneva joint-statement chain keeps a 10% reciprocal PRC tariff in force while suspending the extra 24 points and removing retaliatory-modified higher rates.
  - Why it matters: supports the market’s likely assumption that the effective general reciprocal tariff was normalized back down to 10% rather than remaining at much higher April levels.
  - Direct or indirect: direct.
  - Weight: high.

## Evidence against the claim

- March 3, 2025 White House order raised the synthetic-opioid PRC duty from 10% to 20%; November 4, 2025 White House order reduced it to 10% effective November 10, 2025, not to zero.
  - Why it matters: this leaves a second general China-wide duty in effect by March 31, 2026.
  - Direct or indirect: direct.
  - Weight: very high.

- November 4, 2025 White House reciprocal-tariff order continued the suspension of heightened PRC reciprocal tariffs until November 10, 2026, leaving a 10% reciprocal tariff in place during the suspension.
  - Why it matters: confirms the reciprocal 10% was still live at the market checkpoint.
  - Direct or indirect: direct.
  - Weight: very high.

- Contract wording says the general tariff rate includes any general tariff on all imports plus any tariff on top of that on Chinese imports, and excludes item-specific exceptions rather than separate general China-wide duties.
  - Why it matters: additive logic is embedded in the contract itself.
  - Direct or indirect: direct as to contract interpretation.
  - Weight: high.

## Ambiguous or mixed evidence

- The phrase “general tariff rate” is not formal tariff-code terminology and could tempt some readers to collapse multiple general China-wide duties into a single headline number.
- The market may have anchored on the widely discussed 10% reciprocal figure and underweighted the separate opioid-linked China duty.

## Conflict between inputs

- Main disagreement is interpretive, not factual.
- Factual record from official executive actions is fairly clean: one 10% reciprocal China tariff remained in effect; one separate China duty fell to 10% effective November 10, 2025.
- Interpretive conflict is whether both count toward the contract’s “general tariff rate.”
- What would resolve it: an explicit Polymarket clarification, or a later official administration summary stating the aggregate general base rate on China as of the checkpoint.

## Key assumptions

- Both China-wide tariffs count because they are general rather than item-specific.
- No later executive action before March 31, 2026 reverses either 10% component.

## Key uncertainties

- Resolver interpretation could still favor the simpler 10% headline.
- Late policy change before the checkpoint remains possible.

## Disconfirming signals to watch

- A later White House/USTR order removing either the reciprocal 10% or the opioid 10% before March 31, 2026.
- A market-specific clarification that only one of the two China-wide duties counts.

## What would increase confidence

- Federal Register implementation notice explicitly showing both headings active through March 31, 2026 without contradiction.
- A trusted secondary explainer or CBP/USTR summary that states the combined general China tariff burden as 20%.

## Net update logic

The market prior deserved respect because it likely captured the May 2025 de-escalation from much higher China tariff headlines to a 10% reciprocal rate. But the official November 2025 action chain leaves another 10% China-wide duty alive. That additional component appears material and pushes the answer out of the 5-15% band. So I move from “market probably knows the 10% story” to “market likely underweights additive contract logic or the separate opioid-duty component.”

## Suggested downstream use

Use as orchestrator synthesis input and decision-maker review input, with special attention to contract interpretation risk rather than factual tariff-status risk.