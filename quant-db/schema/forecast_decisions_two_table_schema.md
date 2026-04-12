# Forecast Decisions Two-Table Schema

This document defines the initial **forecast decision ledger** schema for quant-db.

Goal:
- record what the pipeline forecasted
- preserve an append-only history of forecast decisions
- link each forecast to eventual market resolution
- keep forecast-time facts separate from ex-post outcome facts

This schema is intentionally limited to two tables:
- `forecast_decisions`
- `market_resolutions`

## Design principles

1. **Append-only forecast ledger**
   - Every materially distinct forecast decision gets its own row.
   - Do not overwrite prior forecast probabilities in place.

2. **Separate ex-ante and ex-post facts**
   - Forecast rows store what the system believed at decision time.
   - Resolution rows store what later happened in the market.

3. **Artifact-linked, not artifact-embedded**
   - Store paths/URIs to canonical qualitative artifacts.
   - Do not embed full transcripts or large reasoning blobs in the DB.

4. **One market can have many forecasts**
   - Multiple forecasts may be recorded against the same market over time.
   - A later forecast may supersede an earlier one.

5. **One canonical resolution per market/contract pair**
   - The `market_resolutions` table should normally contain at most one active final resolution per `(market_id, contract_id)` pair.
   - If a market is disputed or corrected, handle that as an explicit update policy later.

---

## Table 1: `forecast_decisions`

One row = one decision-maker forecast event.

### Purpose

This table is the canonical ledger of decision outputs.

It should answer:
- what was forecasted
- when it was forecasted
- for which market
- with what probability
- from which artifact packet
- whether the forecast was later superseded / resolved / voided

### Proposed columns

| Column | Type | Null | Notes |
|---|---|---:|---|
| `forecast_id` | `TEXT` | no | Stable unique ID for the forecast event |
| `decision_ts` | `TIMESTAMPTZ` | no | When the forecast decision was made |
| `case_id` | `TEXT` | yes | Qualitative case identifier |
| `dispatch_id` | `TEXT` | yes | Pipeline dispatch/run identifier |
| `market_id` | `TEXT` | no | Canonical market identifier |
| `contract_id` | `TEXT` | no | Contract/outcome identifier |
| `platform` | `TEXT` | no | e.g. `polymarket` |
| `market_slug` | `TEXT` | yes | Human-friendly slug captured at forecast time |
| `question` | `TEXT` | no | Human-readable market question at forecast time |
| `forecast_prob` | `NUMERIC(6,5)` | no | Probability in `[0,1]` |
| `forecast_direction` | `TEXT` | yes | e.g. `yes`, `no`, `lean_yes`, `lean_no` |
| `confidence_label` | `TEXT` | yes | e.g. `low`, `medium`, `high` |
| `confidence_score` | `NUMERIC(6,5)` | yes | Optional normalized confidence score |
| `time_horizon_label` | `TEXT` | yes | Optional horizon framing |
| `verification_mode` | `TEXT` | yes | e.g. `light`, `targeted`, `full` |
| `decision_status` | `TEXT` | no | Semantic state of this forecast row |
| `rationale_summary` | `TEXT` | yes | Short summary for operators/analysis |
| `decision_packet_path` | `TEXT` | no | Canonical structured decision packet path/URI |
| `decision_handoff_path` | `TEXT` | yes | Path/URI to handoff artifact |
| `syndicated_finding_path` | `TEXT` | yes | Path/URI to synthesis artifact |
| `supersedes_forecast_id` | `TEXT` | yes | Prior forecast row superseded by this one |
| `created_at` | `TIMESTAMPTZ` | no | Insert time |
| `updated_at` | `TIMESTAMPTZ` | no | Metadata update time |

### Recommended status values

Keep these narrow and semantic:
- `recorded`
- `superseded`
- `resolved`
- `void`
- `error`

Avoid using this table for orchestration runtime states like `queued`, `running`, `retrying`, etc.

### Invariants

- `forecast_prob` must be between `0` and `1`
- `platform` should be lowercase normalized
- `forecast_id` is unique
- multiple rows per `market_id` are allowed
- `supersedes_forecast_id`, when present, should point to an earlier row

### PostgreSQL DDL draft

```sql
CREATE TABLE forecast_decisions (
    forecast_id TEXT PRIMARY KEY,
    decision_ts TIMESTAMPTZ NOT NULL,
    case_id TEXT,
    dispatch_id TEXT,
    market_id TEXT NOT NULL,
    contract_id TEXT NOT NULL,
    platform TEXT NOT NULL,
    market_slug TEXT,
    question TEXT NOT NULL,
    forecast_prob NUMERIC(6,5) NOT NULL CHECK (forecast_prob >= 0 AND forecast_prob <= 1),
    forecast_direction TEXT,
    confidence_label TEXT,
    confidence_score NUMERIC(6,5) CHECK (
        confidence_score IS NULL OR (confidence_score >= 0 AND confidence_score <= 1)
    ),
    time_horizon_label TEXT,
    verification_mode TEXT,
    decision_status TEXT NOT NULL CHECK (
        decision_status IN ('recorded', 'superseded', 'resolved', 'void', 'error')
    ),
    rationale_summary TEXT,
    decision_packet_path TEXT NOT NULL,
    decision_handoff_path TEXT,
    syndicated_finding_path TEXT,
    supersedes_forecast_id TEXT REFERENCES forecast_decisions(forecast_id),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_forecast_decisions_market_id
    ON forecast_decisions (market_id);

CREATE INDEX idx_forecast_decisions_case_id
    ON forecast_decisions (case_id);

CREATE INDEX idx_forecast_decisions_decision_ts
    ON forecast_decisions (decision_ts);

CREATE INDEX idx_forecast_decisions_status
    ON forecast_decisions (decision_status);

CREATE INDEX idx_forecast_decisions_market_ts
    ON forecast_decisions (market_id, decision_ts DESC);
```

---

## Table 2: `market_resolutions`

One row = one resolved market outcome record.

### Purpose

This table stores ex-post outcome facts.

It should answer:
- how the market resolved
- when it resolved
- where the resolution was sourced from
- whether the market was unresolved / canceled / disputed / finalized

### Proposed columns

| Column | Type | Null | Notes |
|---|---|---:|---|
| `market_id` | `TEXT` | no | Canonical market identifier |
| `contract_id` | `TEXT` | no | Contract/outcome identifier |
| `platform` | `TEXT` | no | e.g. `polymarket` |
| `resolution_status` | `TEXT` | no | Resolution lifecycle status |
| `resolved_outcome` | `TEXT` | yes | e.g. `yes`, `no`, `invalid`, `canceled` |
| `resolved_value` | `NUMERIC(6,5)` | yes | Optional normalized outcome value, often `0` or `1` |
| `resolved_ts` | `TIMESTAMPTZ` | yes | When the market resolved |
| `resolution_source` | `TEXT` | yes | API/source of truth for resolution |
| `resolution_notes` | `TEXT` | yes | Optional notes/context |
| `created_at` | `TIMESTAMPTZ` | no | Insert time |
| `updated_at` | `TIMESTAMPTZ` | no | Update time |

### Recommended status values

- `unresolved`
- `resolved`
- `canceled`
- `disputed`
- `error`

### Invariants

- one row per `(market_id, contract_id)` pair in the initial design
- `resolved_value`, when present, should be in `[0,1]`
- if `resolution_status = 'resolved'`, we usually expect `resolved_outcome` and/or `resolved_value` to be present

### PostgreSQL DDL draft

```sql
CREATE TABLE market_resolutions (
    market_id TEXT NOT NULL,
    contract_id TEXT NOT NULL,
    platform TEXT NOT NULL,
    resolution_status TEXT NOT NULL CHECK (
        resolution_status IN ('unresolved', 'resolved', 'canceled', 'disputed', 'error')
    ),
    resolved_outcome TEXT,
    resolved_value NUMERIC(6,5) CHECK (
        resolved_value IS NULL OR (resolved_value >= 0 AND resolved_value <= 1)
    ),
    resolved_ts TIMESTAMPTZ,
    resolution_source TEXT,
    resolution_notes TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (market_id, contract_id)
);

CREATE INDEX idx_market_resolutions_status
    ON market_resolutions (resolution_status);

CREATE INDEX idx_market_resolutions_resolved_ts
    ON market_resolutions (resolved_ts);
```

---

## Join relationship

Primary join:
- `forecast_decisions.market_id = market_resolutions.market_id`
- `forecast_decisions.contract_id = market_resolutions.contract_id`

This supports:
- forecast scoring
- calibration analysis
- latest forecast vs final outcome views
- multi-forecast-per-market historical analysis

Example:

```sql
SELECT
    fd.forecast_id,
    fd.market_id,
    fd.contract_id,
    fd.decision_ts,
    fd.forecast_prob,
    mr.resolution_status,
    mr.resolved_outcome,
    mr.resolved_value,
    mr.resolved_ts
FROM forecast_decisions fd
LEFT JOIN market_resolutions mr
    ON fd.market_id = mr.market_id
   AND fd.contract_id = mr.contract_id;
```

---

## Evaluation-friendly views

Recommended convenience views:

```sql
CREATE VIEW forecast_decisions_with_resolution AS
SELECT
    fd.forecast_id,
    fd.decision_ts,
    fd.case_id,
    fd.dispatch_id,
    fd.market_id,
    fd.contract_id,
    fd.platform AS forecast_platform,
    fd.market_slug,
    fd.question,
    fd.forecast_prob,
    fd.forecast_direction,
    fd.confidence_label,
    fd.confidence_score,
    fd.time_horizon_label,
    fd.verification_mode,
    fd.decision_status,
    fd.rationale_summary,
    fd.decision_packet_path,
    fd.decision_handoff_path,
    fd.syndicated_finding_path,
    fd.supersedes_forecast_id,
    fd.created_at,
    fd.updated_at,
    mr.platform AS resolution_platform,
    mr.resolution_status,
    mr.resolved_outcome,
    mr.resolved_value,
    mr.resolved_ts,
    mr.resolution_source,
    mr.resolution_notes
FROM forecast_decisions fd
LEFT JOIN market_resolutions mr
    ON fd.market_id = mr.market_id
   AND fd.contract_id = mr.contract_id;

CREATE VIEW latest_forecast_decisions AS
SELECT DISTINCT ON (fdr.market_id, fdr.contract_id)
    fdr.*
FROM forecast_decisions_with_resolution fdr
ORDER BY
    fdr.market_id,
    fdr.contract_id,
    fdr.decision_ts DESC,
    fdr.created_at DESC,
    fdr.forecast_id DESC;

CREATE VIEW initial_forecast_decisions AS
SELECT DISTINCT ON (fdr.market_id, fdr.contract_id)
    fdr.*
FROM forecast_decisions_with_resolution fdr
ORDER BY
    fdr.market_id,
    fdr.contract_id,
    fdr.decision_ts ASC,
    fdr.created_at ASC,
    fdr.forecast_id ASC;
```

---

## Minimal insertion policy

### Decision-maker runtime should write `forecast_decisions` when:
- a decision packet has passed validation
- a concrete market + probability exists
- the forecast is semantically real enough to evaluate later

### Resolution writer should write/update `market_resolutions` when:
- market outcome is known from the trusted source
- cancellation/dispute state is detected
- resolution timing becomes available

---

## Open questions for next revision

1. `market_resolutions` is keyed by `(market_id, contract_id)` so contract-level settlement stays unambiguous.

2. Should `forecast_direction` be derived instead of stored?
   - it can be derived from `forecast_prob`
   - but storing it may preserve the original decision-maker semantics

3. Should `question` be duplicated on every forecast row?
   - convenient for snapshots/history
   - but eventually a separate market catalog table may be cleaner

4. Do we want `is_latest_for_market` as a derived view only, rather than a stored column?
   - recommended: derive it, do not store it initially

---

## Recommendation

Start with these exact two tables.

They are enough to support:
- append-only forecast capture
- resolution linkage
- later scoring and calibration work
- future extension into market catalog / execution / paper-trade layers without redesigning the core ontology
