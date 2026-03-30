# Dispatch Manifest Retention

This directory is the **active handoff queue/history** for planner-emitted dispatch manifests.

## Purpose

Keep recent manifests in a stable workspace location so they are:
- reusable for retries
- easy to inspect during debugging
- available to the TUI/runtime handoff layer for fixed Discord persona channels

## Tiny cleanup/archive policy

### Keep in `dispatch-manifests/`
Keep manifests here when they are:
- newly created
- currently being launched
- still useful for immediate debugging/retry
- from the last **7 days**

### Prune old manifests from the active queue
Old test manifests should not remain in the active queue once they are no longer useful.

If you want to keep a copy temporarily, move them out of the active manifest directory first.
Otherwise, remove them with explicit human approval.

## Helper

Use:

- `runtime/scripts/archive_dispatch_manifests.py`

Default behavior:
- **dry-run only**
- proposes which manifests should leave the active queue
- when applied, moves them to a Trash-backed staging area instead of hard-deleting them

To actually move files, run it with `--apply`.
