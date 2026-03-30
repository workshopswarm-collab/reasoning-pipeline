# Dispatch Manifest Retention

This directory is the **active handoff queue/history** for planner-emitted dispatch manifests.

## Purpose

Keep recent manifests in a stable workspace location so they are:
- reusable for retries
- easy to inspect during debugging
- available to the TUI/runtime handoff layer for fixed Discord persona channels

## Active-queue policy

Keep manifests here when they are:
- newly created
- currently being launched
- still useful for immediate debugging/retry
- from the last **7 days**

## What should leave the active queue

Do not keep stale experimental manifests in the active queue once they stop matching the current truth model.

Examples:
- old test manifests
- reverted workflow experiments
- old `awaiting_visible_start` manifests from the abandoned visible-start gating attempt

## Retention rule

If you want to keep a copy temporarily, move it out of the active manifest directory first.
Otherwise, retire it with explicit human approval.

## Helper

Use:
- `runtime/scripts/archive_dispatch_manifests.py`

Default behavior:
- dry-run only
- proposes which manifests should leave the active queue
- when applied, moves them to a Trash-backed staging area instead of hard-deleting them
