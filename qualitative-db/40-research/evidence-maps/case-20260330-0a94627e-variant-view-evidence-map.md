---
type: evidence_map
domain: culture
subdomain: film
entity: project-hail-mary
topic: Second-weekend box office versus $54m threshold
question: Will "Project Hail Mary" 2nd weekend box office be greater than 54m?
driver: product-launches
date_created: 2026-03-30
agent: variant-view
status: draft
confidence: medium
conflict_status: low factual conflict, moderate weighting conflict
action_relevance: high
related_entities: [universal-pictures]
related_drivers: [product-launches, seasonality, media-narratives]
upstream_inputs:
  - qualitative-db/40-research/source-notes/by-market/case-20260330-0a94627e-variant-view-box-office-mojo-daily-weekend.md
  - qualitative-db/40-research/source-notes/by-market/case-20260330-0a94627e-variant-view-the-numbers-box-office-page.md
downstream_uses:
  - qualitative-db/40-research/agent-findings/variant-view/case-20260330-0a94627e-will-project-hail-mary-2nd-weekend-box-office-be-greater-than-54m.md
  - qualitative-db/40-research/assumption-notes/case-20260330-0a94627e-variant-view-assumptions.md
tags: [evidence-map, domain/culture, subdomain/film, market/case-20260330-0a94627e]
---

# Summary

Current observed data leans **Yes**, but the variant case is that the market may have been **too confident** because the estimated over-threshold cushion was only about **$0.54m**, small enough that ordinary finalization noise still mattered.

## Question being evaluated

Will **Project Hail Mary** finish with a domestic second weekend **greater than $54m** on finalized Box Office Mojo daily figures for **March 27-29, 2026**?

## Current lean

Lean **Yes**, but less confidently than the market.

## Prior / starting view

Starting from a market-implied probability of **79.25%**, the crowd’s baseline view is that the movie was likely to clear the line.

## Evidence supporting the claim

1. **Both core box-office sources currently show the weekend above $54m.**
   - BOM weekend chart: **$54,537,596**.
   - The Numbers movie page: **$54,537,595**.
   - Why it matters: the market only needs the final value to stay above the threshold, and both high-signal sources point there.
   - Weight: **high**.

2. **The daily BOM figures add up cleanly to an over-threshold weekend.**
   - Mar. 27: **$14,669,588**; Mar. 28: **$22,781,719**; Mar. 29: **$17,086,289**.
   - Sum: **$54,537,596**.
   - Why it matters: the market rules resolve off BOM’s daily tab, so the relevant arithmetic is already visible.
   - Weight: **high**.

3. **The film held very well for a large opener.**
   - Opening weekend: **$80,506,007**.
   - Second weekend drop: about **32%**.
   - Why it matters: a strong hold suggests genuine audience conversion and reduces the chance that the current gross is a pure one-day fluke.
   - Weight: **medium-high**.

4. **Theaters increased rather than collapsing.**
   - 4,007 opening theaters; 4,077 max theaters.
   - Why it matters: stable/increased footprint supports weekend resilience.
   - Weight: **medium**.

## Evidence against the claim

1. **The margin over the line is tiny relative to box-office estimate noise.**
   - Current cushion above $54m is only about **$537.6k**.
   - Why it matters: a downward revision of roughly **0.99%** would be enough to flip the market to **No**.
   - Weight: **high**.

2. **BOM still labels the data as estimated.**
   - Why it matters: until finalized, the apparent over cannot be treated as locked.
   - Weight: **high**.

3. **The market may be anchoring on direction, not distance from the line.**
   - The movie is above the threshold, but only barely.
   - Why it matters: prediction markets often overstate certainty when the leading scenario is just one modest revision away from failure.
   - Weight: **medium**.

## Ambiguous or mixed evidence

1. **A -32% second-weekend drop is strong, but not itself resolution-safe.**
   - It supports a robust run and a healthy audience story.
   - But the contract is not about “strong hold” in the abstract; it is about clearing a specific line.

2. **Cross-source agreement helps, but both sources may still be reflecting the same estimate regime.**
   - BOM and The Numbers align closely.
   - That is comforting for direction, but it does not eliminate common-estimate revision risk.

## Conflict between inputs

- No major factual conflict between the sources I found.
- The disagreement is mainly **weighting-based**:
  - consensus/market view: current estimate above line means high-probability Yes;
  - variant view: current estimate above line, but not by enough to justify nearly 80% confidence.
- Evidence that would resolve the disagreement: finalized BOM daily values, or a historical reference class showing how often a wide-release Sunday estimate ~1% above a market line revises below it.

## Key assumptions

- Finalized BOM daily figures will not revise downward by about **$538k** or more.
- There is no hidden reporting artifact that would materially change the Fri/Sat/Sun sum on finalization.

## Key uncertainties

- Typical size and direction of final Monday adjustments for comparable wide releases.
- Whether the current displayed BOM data is effectively final in practice despite the estimate labeling.

## Disconfirming signals to watch

- Finalized BOM daily entries that lower any of Mar. 27-29 enough to push the total below **$54.0m**.
- Any divergence between BOM finals and The Numbers confirmation large enough to imply late estimate error.

## What would increase confidence

- BOM removing the estimate status and leaving the current values intact.
- Independent trade reporting describing the weekend as finalized above **$54m** rather than merely estimated above it.

## Net update logic

The strongest raw evidence points to **Yes**: both key box-office sources currently place the weekend at roughly **$54.54m**. But the market-implied **79.25%** appears somewhat overconfident because the over-threshold cushion is only **~1%**. My net update is therefore: **Yes is the likeliest outcome, but the price seems to underweight finalization/revision fragility.**

## Suggested downstream use

Use this as an input to forecast calibration and role comparison. It is a good example of a case where the market likely had the right direction but may have overstated certainty because the resolution line sat very close to the current estimate.