# runrepairs/ - Repair and backstop tools

These scripts are **not** part of the normal happy-path runtime loop.
They exist for:
- reconciling drift between artifacts and DB state
- finalizing manifests after partial or missed automation
- queue/archive hygiene for dispatch manifests

## When to use these

Use `runrepairs/` when:
- a lane wrote artifacts but did not reconcile completion
- a dispatch finished awkwardly and needs a repair/finalization pass
- manifests need inspection or archive cleanup outside the normal runtime path

Do **not** treat these as the canonical launch/supervision path.
For normal execution, use the top-level runtime scripts instead.

## Current scripts

- `reconcile_dispatch_from_artifacts.py` — repair DB state from produced artifacts
- `finalize_dispatch_after_swarm.py` — manifest-level repair/finalization backstop
- `list_pending_dispatch_manifests.py` — inspect the pending manifest queue
- `archive_dispatch_manifests.py` — archive completed/old manifests

## Design note

If the happy-path runtime starts depending on a script in this folder during ordinary launches, that is usually a smell. It likely belongs either in top-level `scripts/` or in `internal/` instead.
