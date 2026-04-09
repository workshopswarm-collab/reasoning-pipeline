---
type: proposed_driver_family_review
family_slug: resolution-mapping
review_model: qwen3.5:9b
generated_at: 2026-04-08T15:41:22Z
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
- reason: no existing canonical driver covers this family; heuristic summary marks it as novel

## Family quality
- coherent cluster: `True`
- needs split: `False`
- confidence: `low`

## Rationale
The family contains 2 candidates from 1 case. Evidence is sparse (4 total occurrences). The two candidates differ in persona (market-implied vs catalyst-hunter) and label, but there is no clear evidence of materially different mechanisms to justify a split. The family appears coherent but not yet robust enough for promotion. No existing canonical driver covers this, so merge_into_canon is not appropriate. Hold is the conservative choice pending more evidence.

## Raw candidate assignments
- `chart-label-resolution-mapping` -> family `resolution-mapping` | notes: primary candidate with 3 occurrences; persona market-implied
- `title-mapping-ambiguity` -> family `resolution-mapping` | notes: single occurrence; persona catalyst-hunter; unclear mechanistic distinction from chart-label-resolution-mapping

## Suggested follow-up
Gather additional occurrences or cases to determine if the two candidates represent distinct mechanisms or should remain grouped.

## Normalization notes
- `canon_overlap_status_defaulted_to_none`

## Source candidate notes
- `chart-label-resolution-mapping` -> `qualitative-db/40-research/review-queue/drivers-candidates/candidate-notes/generated-driver-candidate-chart-label-resolution-mapping.md`
- `title-mapping-ambiguity` -> `qualitative-db/40-research/review-queue/drivers-candidates/candidate-notes/generated-driver-candidate-title-mapping-ambiguity.md`

## Source input
- `qualitative-db/40-research/review-queue/drivers-candidates/surfaced-family-review/inputs/generated-family-review-input-resolution-mapping.json`
