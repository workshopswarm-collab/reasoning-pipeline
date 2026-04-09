---
type: proposed_driver_family_review
family_slug: resolution-mechanics
review_model: qwen3.5:9b
generated_at: 2026-04-09T07:49:49Z
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
- reason: family marked novel in heuristic summary; no canonical driver covers the specific resolution mechanics concept

## Family quality
- coherent cluster: `True`
- needs split: `False`
- confidence: `low`

## Rationale
The family contains four candidates with sparse evidence (7 total occurrences, 2 distinct cases). While the grouping appears coherent under the 'resolution mechanics' label, the evidence is too sparse to confidently split or promote. The intraday-volatility candidate has related_canonical_drivers (operational-risk, reliability) but is not substantially covered by them, so merge_into_canon is not appropriate. No clear material distinction exists between candidates to justify split_family. Hold is the conservative choice.

## Raw candidate assignments
- `crypto-price-threshold-resolution` -> family `resolution-mechanics` | notes: primary candidate for family; distinct cases and personas support inclusion
- `intraday-volatility` -> family `resolution-mechanics` | notes: related_canonical_drivers suggest operational-risk/reliability but grouped here; sparse evidence warrants hold rather than split
- `exchange-specific settlement mechanics` -> family `resolution-mechanics` | notes: shares case keys with crypto-price-threshold-resolution; sparse evidence
- `resolution mechanics` -> family `resolution-mechanics` | notes: generic label variant; sparse evidence

## Suggested follow-up
accumulate more occurrences or distinct cases before considering promotion or split

## Normalization notes
- `canon_overlap_status_defaulted_to_none`

## Source candidate notes
- `crypto-price-threshold-resolution` -> `qualitative-db/40-research/review-queue/drivers-candidates/candidate-notes/generated-driver-candidate-crypto-price-threshold-resolution.md`
- `intraday-volatility` -> `qualitative-db/40-research/review-queue/drivers-candidates/candidate-notes/generated-driver-candidate-intraday-volatility.md`
- `exchange-specific settlement mechanics` -> `qualitative-db/40-research/review-queue/drivers-candidates/candidate-notes/generated-driver-candidate-exchange-specific-settlement-mechanics.md`
- `resolution mechanics` -> `qualitative-db/40-research/review-queue/drivers-candidates/candidate-notes/generated-driver-candidate-resolution-mechanics.md`

## Source input
- `qualitative-db/40-research/review-queue/drivers-candidates/surfaced-family-review/inputs/generated-family-review-input-resolution-mechanics.json`
