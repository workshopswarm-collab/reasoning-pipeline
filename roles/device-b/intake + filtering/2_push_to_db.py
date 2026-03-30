#!/usr/bin/env python3
import subprocess
import os
import sys
import json

# --- HARDCODE THE TARGET DEVICE A URL HERE ---
# Replace 'PASSWORD' with the actual password for this database role
TARGET_DB_URL = "postgresql://pq_deviceb_ingest:DRJDdRpCXfo4EnS17QxJ0cpZDdsOPEYJ@100.68.192.21:5432/predquant"
os.environ["PREDQUANT_INGEST_URL"] = TARGET_DB_URL
# ---------------------------------------------

INTAKE_SCRIPT = "./3_db_ingest_script.py"
INPUT_JSON_FILE = "filtered_markets.json"

def push_data():
    if not os.path.exists(INPUT_JSON_FILE):
        print(f"Error: {INPUT_JSON_FILE} not found.")
        return 1

    success_count = 0
    error_count = 0

    with open(INPUT_JSON_FILE, "r", encoding="utf-8") as f:
        try:
            markets = json.load(f)
        except json.JSONDecodeError:
            print(f"Error: {INPUT_JSON_FILE} is not valid JSON.")
            return 1

    if not isinstance(markets, list):
        print(f"Error: {INPUT_JSON_FILE} must contain a JSON array.")
        return 1

    print(f"Loaded {len(markets)} markets. Pushing to database...")

    for item in markets:
        if not isinstance(item, dict):
            error_count += 1
            print("Skipping non-object item in JSON array.")
            continue

        # Script 1 already emits the correct nested intake payload shape.
        payload = {
            "platform": item.get("platform"),
            "external_market_id": item.get("external_market_id"),
            "slug": item.get("slug"),
            "title": item.get("title"),
            "description": item.get("description"),
            "category": item.get("category"),
            "status": item.get("status"),
            "outcome_type": item.get("outcome_type"),
            "closes_at": item.get("closes_at"),
            "resolves_at": item.get("resolves_at"),
            "metadata": item.get("metadata", {}),
            "snapshot": item.get("snapshot", {}),
        }

        payload_str = json.dumps(payload)

        proc = subprocess.run(
            [sys.executable, INTAKE_SCRIPT, "--file", "-"],
            input=payload_str,
            text=True,
            capture_output=True,
        )

        if proc.returncode == 0:
            success_count += 1
        else:
            error_count += 1
            market_ref = payload.get("external_market_id") or payload.get("slug") or "UNKNOWN"
            print(f"Failed to insert {market_ref}: {proc.stderr.strip()}")

    print(f"Finished pushing to Postgres! Success: {success_count}, Errors: {error_count}")
    return 0 if error_count == 0 else 1

if __name__ == "__main__":
    raise SystemExit(push_data())