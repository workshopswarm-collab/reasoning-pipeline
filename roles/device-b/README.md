# Device B scripts

This folder holds scripts intended to run on the data-pipeline mini (Device B).

Current intake / filtering scripts live in:
- `roles/device-b/intake + filtering/`

This README documents the current repo-local Device B intake path only.
It does not imply that execution, accounting, or all Device B infrastructure lives in this folder yet.

## Current scripts

### `1_intake_filter.py`
Fetches active Polymarket events from the Gamma API, applies filtering rules, and writes a `filtered_markets.json` file.

### `2_push_to_db.py`
Reads `filtered_markets.json` and pushes each selected market payload into Postgres by calling the ingest script.

### `3_db_ingest_script.py`
Reads one intake payload and:
1. upserts a row into `markets`
2. inserts one row into `market_snapshots`
3. updates selected pipeline-state fields on `markets`

## Required environment variable

Preferred configuration:

```bash
export PREDQUANT_INGEST_URL='postgresql://pq_deviceb_ingest:PASSWORD@HOST:5432/predquant'
```

## Example runs

From `roles/device-b/intake + filtering/`:

```bash
python3 1_intake_filter.py
python3 2_push_to_db.py
```

Direct single-payload ingest:

```bash
python3 3_db_ingest_script.py --file market_payload.json --pretty
```

## Expected payload shape for `3_db_ingest_script.py`

Top-level required fields:
- `platform`
- `external_market_id`
- `title`

Optional market fields:
- `slug`
- `description`
- `category`
- `status`
- `outcome_type`
- `closes_at`
- `resolves_at`
- `metadata`

Optional `snapshot` object fields:
- `observed_at`
- `last_price`
- `best_bid`
- `best_ask`
- `yes_price`
- `no_price`
- `volume`
- `open_interest`
- `raw_payload`
