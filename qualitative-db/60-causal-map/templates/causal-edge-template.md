---
type: causal_edge
artifact_type: causal_edge
schema_version: v1
edge_key:
edge_label:
source_node_key:
target_node_key:
effect_sign: increases
status: draft
mechanism_family:
source_kind: manual
lifecycle_stage: draft
superseded_by_key:
confidence_mode: reviewed
confidence_prior: 0.50
description:
linked_intervention_keys: []
---

# Edge label

## Claim

- Describe the directional causal or workflow claim this edge represents.

## When it should apply

- Describe the contexts where this edge is usually relevant.

## Boundaries or contest conditions

- Describe when the edge should be weakened, contested, or ignored.

## Lifecycle / family metadata

- `mechanism_family`: bounded family such as `threshold_touch`, `source_resolution`, `workflow_pricing`, or `publication_timing`.
- `source_kind`: usually `seed`, `manual`, `proposal_auto`, or `merged`.
- `lifecycle_stage`: one of `draft`, `trial`, `active`, `hold`, `retired`, or `archived`.
- `superseded_by_key`: optional replacement edge key when this edge is merged or retired.

## Linked evidence and artifacts

- Point to reviewed cases, interventions, or aggregate notes that support or challenge the edge.

<!-- Optional sidecar: <same-path>.json
{
  "artifact_type": "causal_edge",
  "schema_version": "v1",
  "edge_key": "source__increases__target",
  "mechanism_family": "threshold_touch",
  "source_kind": "manual",
  "lifecycle_stage": "draft",
  "superseded_by_key": "",
  "contexts": {
    "platforms": [],
    "categories": [],
    "question_mechanics": [],
    "source_of_truth_class": []
  },
  "linked_intervention_keys": [],
  "evidence_paths": [],
  "evidence_rows": [
    {
      "case_key": "case-...",
      "review_path": "qualitative-db/50-learnings/case-reviews/case-.../review.md",
      "support_direction": "supports",
      "confidence": 0.7,
      "notes": {}
    }
  ]
}
-->
