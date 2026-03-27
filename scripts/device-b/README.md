# Device B scripts

This folder holds scripts intended to run on the data-pipeline mini (Device B).

## `intake_market.py`

Minimal phase-0 intake script.

It:
1. reads one JSON payload
2. upserts a row into `markets`
3. inserts one row into `market_snapshots`

## Required environment variable

```bash
export PREDQUANT_INGEST_URL='postgresql://pq_deviceb_ingest:PASSWORD@100.68.192.21:5432/predquant'
```

## Example run

```bash
source ~/.predquant-db.env
python3 scripts/device-b/intake_market.py --file scripts/device-b/examples/market_payload.example.json --pretty
```

## Expected payload shape

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
