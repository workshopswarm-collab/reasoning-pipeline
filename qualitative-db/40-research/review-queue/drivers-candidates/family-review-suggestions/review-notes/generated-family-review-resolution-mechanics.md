---
type: proposed_driver_family_review
family_slug: resolution-mechanics
review_model: qwen3.5:9b
generated_at: 2026-04-07T02:37:38Z
prompt_version: v1
recommended_action: hold
recommended_family_slug: resolution-mechanics
recommended_family_label: "resolution mechanics"
merge_target_family_slug: 
merge_target_canonical_driver: 
canon_overlap_status: none
canon_overlap_driver: 
review_confidence: low
status: active
---

# Family review: resolution-mechanics

## Recommendation
- action: `hold`
- recommended family slug: `resolution-mechanics`
- recommended family label: `resolution mechanics`
- merge target family: ``
- merge target canonical driver: ``

## Canon overlap
- status: `none`
- canonical driver: ``
- reason: heuristic_summary indicates canon_coverage_status is novel with no canonical_driver provided

## Family quality
- coherent cluster: `True`
- needs split: `False`
- confidence: `low`

## Rationale
The family contains 4 candidates with 7 total occurrences across 2 distinct cases. While the candidates show some diversity (crypto price thresholds, intraday volatility, exchange settlement mechanics), the evidence is sparse (only 2 distinct cases). The heuristic summary marks it as novel with no canonical overlap. The grouping appears coherent but not yet robust enough for promotion or splitting. Sparse evidence suggests hold rather than split.

## Raw candidate assignments
- `crypto-price-threshold-resolution` -> family `resolution-mechanics` | notes: primary candidate within the family, distinct cases and personas
- `intraday-volatility` -> family `resolution-mechanics` | notes: related to catalyst-hunter persona, distinct mechanism but grouped under same family
- `exchange-specific settlement mechanics` -> family `resolution-mechanics` | notes: related to catalyst-hunter persona, distinct mechanism but grouped under same family
- `resolution mechanics` -> family `resolution-mechanics` | notes: generic label variant within the family

## Suggested follow-up
Gather more occurrences or distinct cases to assess if the diverse candidates represent materially different mechanisms or a single coherent family.

## Normalization notes
- `canon_overlap_status_defaulted_to_none`

## Source candidate notes
- none

## Source input
- `qualitative-db/40-research/review-queue/drivers-candidates/family-review-suggestions/inputs/generated-family-review-input-resolution-mechanics.json`
