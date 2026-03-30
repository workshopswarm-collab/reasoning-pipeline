---
type: evidence_map
domain: culture
subdomain: film
entity: Project Hail Mary
topic: evidence map for Project Hail Mary > $54M second weekend
question: Will "Project Hail Mary" 2nd weekend domestic box office be greater than $54M?
driver: seasonality
date_created: 2026-03-30
agent: market-implied
status: active
confidence: medium-high
conflict_status: moderate-operational-conflict
action_relevance: high
related_entities: [amazon]
related_drivers: [seasonality, product-launches, media-narratives]
upstream_inputs:
  - qualitative-db/40-research/source-notes/by-market/case-20260330-0a94627e-market-implied-the-numbers-movie-page.md
  - qualitative-db/40-research/source-notes/by-market/case-20260330-0a94627e-market-implied-weekend-chart-confirmation.md
  - qualitative-db/40-research/source-notes/by-market/case-20260330-0a94627e-market-implied-box-office-mojo-link-anomaly.md
  - qualitative-db/40-research/assumption-notes/case-20260330-0a94627e-market-implied-assumptions.md
downstream_uses:
  - qualitative-db/40-research/agent-findings/market-implied/case-20260330-0a94627e-will-project-hail-mary-2nd-weekend-box-office-be-greater-than-54m.md
tags: [domain/culture, subdomain/film, market/project-hail-mary, evidence-map]
---

# Summary

The best current evidence favors **YES** and suggests the market's high YES stance is fundamentally right, but the remaining uncertainty is concentrated in **finalization/revision mechanics** rather than in the film's audience-demand trajectory.

## Question being evaluated

Will `Project Hail Mary` post a domestic second-weekend gross greater than **$54M** for Mar. 27-29, 2026 under the market's resolution rules?

## Current lean

Lean **YES**, with the main caution being that the reported margin above the threshold is narrow and the cited Box Office Mojo URL is anomalous.

## Prior / starting view

Starting from the market price of **79.25% YES**, the natural prior is that traders believed the movie had enough momentum to clear the bar, but not with enough certainty to price out reporting/revision risk.

## Evidence supporting the claim

1. **Direct The Numbers weekend figure is above threshold**  
   - Source: `...market-implied-the-numbers-movie-page.md`  
   - The page lists **$54,537,595** for the Mar. 27 weekend.  
   - This is direct evidence on the exact numeric proposition.  
   - Weight: **very high**.

2. **Separate weekend chart repeats the same number**  
   - Source: `...market-implied-weekend-chart-confirmation.md`  
   - The Mar. 27 weekend chart also lists **$54,537,595**, #1 rank, and **-32%** weekend drop.  
   - This reduces extraction-error risk and reinforces that the number was not a one-page artifact.  
   - Weight: **high**.

3. **Underlying trajectory is consistent with a strong hold**  
   - Source: `...market-implied-the-numbers-movie-page.md`  
   - Opening weekend was **$80.506M** and second weekend fell only **32%**, with theater count slightly increasing.  
   - That is the kind of hold profile the market would rationally price bullishly.  
   - Weight: **high**.

4. **Daily components support the weekend total**  
   - Source: `...market-implied-the-numbers-movie-page.md`  
   - Fri/Sat/Sun daily figures align with a weekend just above the bar.  
   - This makes the headline weekend figure feel mechanically grounded rather than arbitrary.  
   - Weight: **medium-high**.

## Evidence against the claim

1. **Margin above threshold is thin**  
   - Source: `...market-implied-the-numbers-movie-page.md`  
   - The current reported edge above $54M is only about **$0.538M**.  
   - Small downward revisions could flip the outcome.  
   - Weight: **high**.

2. **Named Box Office Mojo URL appears mismatched**  
   - Source: `...market-implied-box-office-mojo-link-anomaly.md`  
   - The market's cited Box Office Mojo title link currently resolves to a different movie page.  
   - This does not directly argue for NO on economics, but it does create operational resolution risk and may explain why the market is not closer to certainty.  
   - Weight: **medium-high**.

3. **The Numbers markup still appears estimate-like**  
   - Source: both The Numbers notes  
   - If numbers are not fully locked, some revision risk remains.  
   - Weight: **medium**.

## Ambiguous or mixed evidence

- The market price of **79.25%** itself is mixed evidence. It strongly favors YES, implying traders already respect the hold trajectory, but it is also much lower than one might expect if traders treated the currently reported The Numbers figure as effectively final.
- The Box Office Mojo anomaly may reflect a harmless link issue rather than a true resolution problem. If so, the market is too low; if not, the market's discount makes more sense.

## Conflict between inputs

- The conflict is not mainly factual about ticket demand. It is **operational and weighting-based**:
  - factual box-office evidence points to **YES**;
  - resolution mechanics and revision risk keep the probability below certainty.
- Evidence that would resolve this conflict:
  - correct final Box Office Mojo Domestic Daily posting for Project Hail Mary;
  - explicit finalization on The Numbers / industry trades with no material downward revision.

## Key assumptions

- The current $54.5376M figure will not revise below $54.0M.
- The Box Office Mojo URL problem will not create a materially different resolved value or invalidate the use of the already available box-office data.

## Key uncertainties

- Final versus estimate status of the current weekend number.
- Whether the exact Box Office Mojo page in the market description is a bad link or a deeper source-mapping issue.
- How much room there is for late downward revision.

## Disconfirming signals to watch

- Any revision that pushes weekend gross below **$54.0M**.
- Resolver communication treating the source anomaly as more than a clerical issue.
- Divergence between The Numbers and final Box Office Mojo domestic daily totals.

## What would increase confidence

- A correct Box Office Mojo daily table for Mar. 27-29 summing above **$54M**.
- Monday/Tuesday trade reporting confirming actuals near **$54.5M**.
- Confirmation that the market's cited Box Office Mojo link is simply wrong while the underlying film data is not contested.

## Net update logic

Starting from the market's **79.25% YES** prior, the live evidence pushes me upward because a major box-office source is already printing a figure above threshold and the trajectory behind it looks internally coherent. I do not go near 100% because the margin over the line is slim and the Box Office Mojo-side resolution path is currently messy. In other words: the market seems directionally right about audience demand, but still somewhat too conservative if the only major residual risks are modest revision and source plumbing.

## Suggested downstream use

Use this as direct input for forecast comparison and final orchestration. The key takeaway is that the market looks mostly right on direction, but likely underweights the now-published above-threshold weekend total relative to the remaining operational risks.