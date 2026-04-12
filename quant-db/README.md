# quant-db/

This directory holds **schema and migration artifacts** for the shared PostgreSQL database used by the prediction pipeline.

It does **not** hold the live PostgreSQL data directory.

The live database cluster is runtime infrastructure and should stay outside the repo.

## Structure

- `schema/` → canonical schema/bootstrap SQL snapshots
- `migrations/` → ordered SQL migrations applied to a running database

## Intended flow

1. Start a PostgreSQL instance outside the repo
2. Create local roles/database with `quant-db/scripts/bootstrap_local.sh`
3. Load connection variables from `.env.postgres.local`
4. Apply migrations with `quant-db/scripts/apply.sh`
5. Verify access with `quant-db/scripts/check.sh`

## Current scope

The initial schema is intentionally minimal. It is designed to validate the first end-to-end architecture loop:

Current forecast-ledger surfaces now also include:
- `forecast_decisions`
- `market_resolutions`
- view `forecast_decisions_with_resolution`
- view `latest_forecast_decisions`
- view `initial_forecast_decisions`

Manual resolution ingestion helper:
- `quant-db/scripts/upsert_market_resolution.py`
- intended for explicit operator/manual writes into `market_resolutions` while the automated resolution-ingest path is still being built
- defaults to `PREDQUANT_ORCHESTRATOR_URL` (or falls back to `PREDQUANT_ADMIN_URL`)

Automated Polymarket resolution sync helper:
- `quant-db/scripts/sync_polymarket_market_resolutions.py`
- scans unresolved Polymarket forecast rows, normalizes missing market identity from the dispatch manifest when needed, fetches the current market status from `gamma-api.polymarket.com/markets/slug/{slug}`, and upserts resolved rows into `market_resolutions`
- supports `--dry-run` for verification before writing

Brier scoring helper:
- `quant-db/scripts/score_brier.py`
- computes Brier metrics across resolved rows using:
  - `initial_forecast_decisions`
  - `latest_forecast_decisions`
  - `forecast_decisions_with_resolution`
- intended as the first evaluation surface for predictive-accuracy tracking

Safety note:
- `migrations/005_research_run_active_attempt_uniqueness.sql` introduces a partial unique index for active case/persona attempts, but it should only be applied after auditing/cleaning existing duplicate queued/running rows (see `quant-db/scripts/audit_active_research_run_conflicts.py`).

- Device B writes market metadata and market snapshots
- Device A opens cases and coordinates research runs
- research runs are handed off into Telegram forum topics and tracked in PostgreSQL
- research agents log predictions
- Device A writes decision packets
- Device B reads those packets and records paper executions
- resolved outcomes and retrospectives close the loop

The first migration set is meant to reduce time to deployment, not to fully model the final system on day one.
