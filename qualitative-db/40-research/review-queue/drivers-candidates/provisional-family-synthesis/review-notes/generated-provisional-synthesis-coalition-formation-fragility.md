---
type: proposed_driver_provisional_synthesis_review
family_slug: coalition-formation-fragility
review_model: qwen3.5:9b
generated_at: 2026-04-13T22:34:33Z
prompt_version: v1
recommended_action: merge_provisional_buckets
target_family_slug: coalition-fragmentation
target_family_label: "coalition-fragmentation"
target_canonical_driver: elections
review_confidence: low
status: active
---

# Provisional synthesis review: coalition-formation-fragility

## Recommendation
- action: `merge_provisional_buckets`
- target family slug: `coalition-fragmentation`
- target family label: `coalition-fragmentation`
- target canonical driver: `elections`
- confidence: `low`

## Rationale
The focal bucket 'coalition-formation-fragility' and neighbor 'coalition-fragmentation' share the same canonical driver 'elections' and both relate to coalition dynamics in an electoral context. The overlap score is high (1.75) and the mechanism token 'coalition' is shared. Merging them consolidates evidence around the broader mechanism of coalition instability driven by electoral mechanics. The third neighbor 'coalition-brand-decay' is less related as it focuses on brand decay rather than formation/fragmentation mechanics.

## Suggested follow-up
Review 'coalition-brand-decay' separately to determine if it should remain provisional or merge into a different family.

## Normalization notes
- `confidence_defaulted`

## Source input
- `qualitative-db/40-research/review-queue/drivers-candidates/provisional-family-synthesis/inputs/generated-provisional-synthesis-input-coalition-formation-fragility.json`
