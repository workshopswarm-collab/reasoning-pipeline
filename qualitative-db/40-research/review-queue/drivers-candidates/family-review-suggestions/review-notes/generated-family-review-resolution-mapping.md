---
type: proposed_driver_family_review
family_slug: resolution-mapping
review_model: qwen3.5:9b
generated_at: 2026-04-07T02:37:38Z
prompt_version: v1
recommended_action: hold
recommended_family_slug: resolution-mapping
recommended_family_label: "resolution mapping"
merge_target_family_slug: 
merge_target_canonical_driver: 
canon_overlap_status: none
canon_overlap_driver: 
review_confidence: low
status: active
---

# Family review: resolution-mapping

## Recommendation
- action: `hold`
- recommended family slug: `resolution-mapping`
- recommended family label: `resolution mapping`
- merge target family: ``
- merge target canonical driver: ``

## Canon overlap
- status: `none`
- canonical driver: ``
- reason: no existing canonical drivers provided in input

## Family quality
- coherent cluster: `True`
- needs split: `False`
- confidence: `low`

## Rationale
The family contains 2 candidates from 1 case with 4 total occurrences. Evidence is sparse (1 distinct case). The two candidates differ in persona (market-implied vs catalyst-hunter) and label semantics (chart-label vs title-mapping-ambiguity), but without clear evidence of materially different mechanisms, splitting is premature. The family appears coherent but needs more data before promotion or split. No canonical drivers exist to merge into.

## Raw candidate assignments
- `chart-label-resolution-mapping` -> family `resolution-mapping` | notes: primary candidate, 3 occurrences, market-implied persona
- `title-mapping-ambiguity` -> family `resolution-mapping` | notes: secondary candidate, 1 occurrence, catalyst-hunter persona, same case

## Suggested follow-up
gather more occurrences across distinct cases to assess mechanism differentiation and persona consistency before considering split or promotion.

## Normalization notes
- `canon_overlap_status_defaulted_to_none`

## Source candidate notes
- none

## Source input
- `qualitative-db/40-research/review-queue/drivers-candidates/family-review-suggestions/inputs/generated-family-review-input-resolution-mapping.json`
