---
type: causal_node
artifact_type: causal_node
schema_version: v1
node_key:
label:
node_type: market_state
status: draft
mechanism_family:
source_kind: manual
lifecycle_stage: draft
superseded_by_key:
description:
tags: []
---

# Node label

## What this node means

- Describe the reusable state / mechanism / condition the node captures.

## When it applies

- Describe the contract or case conditions where the node should become active.

## Boundaries

- Say when this node should **not** be activated.
- Distinguish similar but different nodes when needed.

## Lifecycle / family metadata

- `mechanism_family`: bounded family such as `threshold_touch`, `source_resolution`, `workflow_pricing`, or `publication_timing`.
- `source_kind`: usually `seed`, `manual`, `proposal_auto`, or `merged`.
- `lifecycle_stage`: one of `draft`, `trial`, `active`, `hold`, `retired`, or `archived`.
- `superseded_by_key`: optional replacement node key when this node is merged or retired.

## Linked evidence and artifacts

- List relevant reviewed cases, drivers, interventions, or canon paths when known.

<!-- Optional sidecar: <same-path>.json
{
  "artifact_type": "causal_node",
  "schema_version": "v1",
  "node_key": "example-node",
  "mechanism_family": "threshold_touch",
  "source_kind": "manual",
  "lifecycle_stage": "draft",
  "superseded_by_key": "",
  "contexts": {
    "platforms": [],
    "categories": [],
    "question_mechanics": []
  },
  "linked_paths": {
    "drivers": [],
    "domains": [],
    "entities": []
  }
}
-->
