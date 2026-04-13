# backups/

This directory is for local/operator backup snapshots such as automation reset exports.

These artifacts are operational breadcrumbs, not canonical source files.

Policy:
- keep durable code/docs/contracts in normal repo paths
- keep one-off reset/export snapshots under `backups/`
- do not rely on backup snapshots as part of the live runtime contract
- `backups/automation-reset-*` is gitignored so future reset bundles stay local unless intentionally handled another way

If a backup snapshot becomes important enough to preserve in version control, promote the durable information into docs, migrations, or structured test fixtures instead of keeping raw operator snapshots as ordinary tracked files.
