---
type: evidence_map
domain: culture
subdomain: film
entity: Project Hail Mary
topic: second weekend domestic box office versus 54M strike
question: Will "Project Hail Mary" 2nd Weekend Box Office be greater than 54m?
driver: seasonality
date_created: 2026-03-30
agent: catalyst-hunter
status: active
confidence: high
conflict_status: low
action_relevance: high
related_entities: []
related_drivers: [seasonality, performance, media-narratives, product-launches]
upstream_inputs:
  - qualitative-db/40-research/cases/case-20260330-0a94627e/researcher-source-notes/case-20260330-0a94627e-catalyst-hunter-box-office-mojo-weekend-chart.md
  - qualitative-db/40-research/cases/case-20260330-0a94627e/researcher-source-notes/case-20260330-0a94627e-catalyst-hunter-the-numbers-summary.md
downstream_uses:
  - qualitative-db/40-research/cases/case-20260330-0a94627e/researcher-analyses/2026-03-30/dispatch-case-20260330-0a94627e-20260330T142051Z/personas/catalyst-hunter.md
tags: [market/case-20260330-0a94627e, domain/culture, subdomain/film, evidence-map]
legacy_imported: true
legacy_original_path: qualitative-db/40-research/evidence-maps/case-20260330-0a94627e-catalyst-hunter-evidence-map.md
legacy_original_note_kind: evidence
imported_by: legacy_40_research_backfill
import_batch: 20260405T225345Z
case_key: case-20260330-0a94627e
dispatch_id: dispatch-case-20260330-0a94627e-20260330T142051Z
analysis_date: 2026-03-30
persona: catalyst-hunter
---

# Summary
The evidence now leans strongly to **YES**. The key catalyst is no longer moviegoing demand during the weekend; it is Monday confirmation/finalization of already-observed box-office totals that sit about $0.54M above the strike.

## Question being evaluated
Will **Project Hail Mary** gross **more than $54M** domestically in its second weekend (March 27-29, 2026)?

## Current lean
Strong **YES** lean.

## Prior / starting view
Before reviewing current data, a reasonable starting view would have been that a film opening to about $80.5M needed a hold of roughly 67% of opening weekend to clear $54M on weekend two. That is a demanding but very plausible hold for a well-received sci-fi event movie with stable theater count.

## Evidence supporting the claim
- **Box Office Mojo weekend chart:** lists Project Hail Mary at **$54,537,596** for Mar. 27-29 on 4,077 theaters. This is the highest-value evidence because BOM is the resolution-source family and the number is already above the strike.
- **The Numbers weekend total:** lists **$54,537,595** for the same second weekend. Independent confirmation reduces the chance of a feed or scrape anomaly.
- **The Numbers daily breakdown:** Friday + Saturday + Sunday totals sum to the same approximate weekend value, which makes a dramatic revision below $54M unlikely.
- **Second-weekend drop only ~32% from an $80.5M opening:** that hold is consistent with strong audience conversion and reduces the chance of a hidden collapse in Sunday actuals.

## Evidence against the claim
- **Finality ambiguity on Box Office Mojo extract:** the fetched BOM weekend chart includes the text "Key: New This Week Estimated," so the exact page extract does not explicitly prove the number is final on the title-page Domestic Daily tab.
- **Revision risk still exists until sources fully sync:** weekend estimates can move on Monday, and the formal market rule waits for final daily values.

## Ambiguous or mixed evidence
- **Market price at 79.25%:** this could mean traders are appropriately discounting finalization mechanics, or it could simply reflect stale pricing and limited liquidity after the main informational event has already happened.
- **Margin over strike is only ~$0.54M:** materially above the line, but not so enormous that one can say revision risk is literally zero.

## Conflict between inputs
There is no major factual conflict. The only live disagreement is about **mechanical certainty**, not directional sign:
- factual disagreement: minimal
- interpretive disagreement: low
- weighting/timing disagreement: moderate, centered on how much residual risk to assign to final Monday confirmation
- evidence that would resolve it: Box Office Mojo title-page Domestic Daily tab showing final Mar. 27-29 values, or clear confirmation that BOM and The Numbers have finalized matching numbers

## Key assumptions
- Normal Monday revisions will not shave more than roughly **$538k** off the weekend total.
- There will be no unusual source ambiguity or post-publication correction large enough to push the figure below $54M.
- The market is resolving on standard domestic weekend accounting rather than an unexpected methodological quirk.

## Key uncertainties
- Whether the exact Box Office Mojo title page used for settlement is already flagged final at the moment of review.
- Whether traders have already incorporated The Numbers confirmation, or are still anchoring to earlier estimate uncertainty.

## Disconfirming signals to watch
- Box Office Mojo title-page Domestic Daily tab revising the Mar. 27-29 combined weekend below $54M.
- A large downward correction on either Saturday or Sunday that breaks the current daily sum.
- An explicit source-finality dispute between Box Office Mojo and The Numbers.

## What would increase confidence
- A clean read of the Box Office Mojo title-page Domestic Daily tab showing final daily values for Mar. 27-29.
- Trade-report language describing the weekend result as final actuals rather than estimates.

## Net update logic
The crucial update is that this market is no longer mainly about whether the movie *can* hold well enough in weekend two; observable data say it **did** hold well enough. That shifts the case from demand uncertainty to settlement-mechanics uncertainty. Because both BOM-family data and The Numbers cluster tightly around **$54.54M**, the residual risk looks much smaller than a 20.75% chance of failure.

## Suggested downstream use
Use this as:
- forecast update
- orchestrator synthesis input
- decision-maker review
