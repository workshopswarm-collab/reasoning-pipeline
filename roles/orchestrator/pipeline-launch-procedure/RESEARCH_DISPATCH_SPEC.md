# Research Dispatch Spec

Compact operating contract for Orchestrator-driven case research.

## Purpose

Connect four things cleanly:
- market selection in Postgres
- case orchestration in Postgres
- independent OpenClaw subagent research runs
- qualitative artifacts in `qualitative-db/40-research/`

This is a control-plane contract, not a replacement for the vault READMEs.

---

## Core rules

1. **One market at a time through active research**
   - Device B may ingest many markets.
   - Orchestrator should normally advance only one selected market at a time into active case work.

2. **Researchers are independent takes, not rigid specialist microservices**
   - They analyze the same case with different priors, update styles, and independently informed reactions to the market-implied view.

3. **Researchers read broad context, but write only case-specific research**
   - Read from `10-domains/`, `20-entities/`, `30-drivers/`, and relevant existing research.
   - Normally write only into `qualitative-db/40-research/`.
   - Do not casually update canon during ordinary case work.

4. **Preserve disagreement**
   - Do not flatten conflicting views early.
   - Preserve competing interpretations in `40-research/` and structured predictions in Postgres.

5. **Market price is part of the object of analysis**
   - Every researcher must inspect the current market-implied probability and explicitly say whether they agree or disagree with it.

6. **Vault and Postgres are complementary**
   - Vault = provenance, reasoning, assumptions, evidence, synthesis.
   - Postgres = operational state, run records, structured predictions, decision state.

---

## Researcher personas

Preferred recurring personalities:

### `base-rate`
- outside view
- structural priors
- historical frequency
- skeptical of overfit narratives

Question: what should I believe before case-specific evidence impresses me?

### `market-implied`
- starts from live market price as an information-rich prior
- asks what would make the market reasonable
- guards against naive anti-market overconfidence

Question: what must be true for the current price to make sense?

### `variant-view`
- looks for the strongest credible anti-consensus take
- hunts underweighted mechanisms or neglected evidence

Question: what is the strongest reason the market may be wrong?

### `risk-manager`
- stress-tests the thesis
- focuses on hidden assumptions, fragility, and disconfirming evidence

Question: what could break this view badly?

### `catalyst-hunter`
- focuses on timing and near-term repricing triggers
- looks for events likely to move the market soon

Question: what changes the market before resolution, and when?

---

## Required researcher behavior

Each dispatched run should normally:

1. Read the case prompt and market metadata.
2. Inspect current market state, especially current price and timing.
3. Read relevant background context from:
   - `qualitative-db/10-domains/`
   - `qualitative-db/20-entities/`
   - `qualitative-db/30-drivers/`
4. Research independently using internet access and available tools.
5. Write case-specific artifacts into `qualitative-db/40-research/`.
6. Log a structured prediction in Postgres.
7. Explicitly state agreement/disagreement versus the market-implied probability.
8. Preserve uncertainty and disagreement rather than collapsing them too early.

Minimum expected outputs per run:
- one qualitative artifact in `40-research/`
- one structured prediction log in Postgres

---

## Default qualitative output location

Primary default output is an **agent finding** in one of:
- `qualitative-db/40-research/agent-findings/base-rate/`
- `qualitative-db/40-research/agent-findings/market-implied/`
- `qualitative-db/40-research/agent-findings/variant-view/`
- `qualitative-db/40-research/agent-findings/risk-manager/`
- `qualitative-db/40-research/agent-findings/catalyst-hunter/`

Researchers should also write in the course of researching:
- `source-notes/`
- `assumption-notes/`
- `evidence-maps/`
- `product-notes/` only when the research object is genuinely versioned or release-specific

Researchers should not normally write directly to:
- `10-domains/`
- `20-entities/`
- `30-drivers/`
- `50-retrospectives/`

---

## State model

### `markets.pipeline_status`
- `new`
- `pending_research`
- `researching`
- `ignored`
- `executed`
- `closed`

### `cases.status`
- `open`
- `closed`

### `research_runs.status`
- `queued`
- `running`
- `completed`
- `failed`
- `canceled`

---

## Dispatch flow

1. `roles/orchestrator/pipeline-launch-procedure/initialize/scripts/select_next_market.py` selects one eligible market.
2. `roles/orchestrator/pipeline-launch-procedure/initialize/scripts/open_case.py` creates or fetches the case.
3. When real dispatch begins, mark the market `researching`.
4. `roles/orchestrator/pipeline-launch-procedure/initialize/scripts/dispatch_case_research.py` prepares the dispatch plan:
   - create a `research_runs` row per persona
   - build the exact researcher prompt per persona
   - emit one `sessions_spawn` payload per persona
   - emit one post-spawn DB patch template per persona
5. The OpenClaw runtime executes the emitted `sessions_spawn` payloads.
6. The OpenClaw runtime patches the corresponding `research_runs` rows with runtime/session metadata.
7. Researchers write `40-research/` artifacts.
8. Researchers log structured predictions tied to run/case/market.
9. Orchestrator synthesizes vault outputs + structured predictions.
10. Decision-maker writes decision packet.
11. Case is later closed, deferred, or ignored.

---

See also:
- `roles/orchestrator/pipeline-launch-procedure/OPENCLAW_RUNTIME_BRIDGE.md`

## Why the DB run record exists

OpenClaw already provides worker execution.
The DB run record exists so the pipeline can answer:
- which personas were dispatched?
- when did each run start and finish?
- which subagent session corresponds to which run?
- which qualitative artifact came from which run?
- which prediction came from which run?
- how did each research style perform over time?

---

## DB metadata vs vault content

These are **not redundant** with the qualitative database.

### Strong keep
- `workspace_note_path`
- `notes.child_session_key`

### Good to keep
- `notes.spawn_run_id`
- `notes.model`

### Optional for MVP
- `notes.thinking`

Reason:
- the vault stores research content
- the DB stores runtime identity, structured linkage, and evaluation metadata

---

## MVP minimum contract

Per run, record at least:
- `case_id`
- `run_label`
- `agent_label`
- `runtime`
- `status`
- `started_at`
- `workspace_note_path`
- `notes.child_session_key`

Per researcher, require at least:
- one `40-research/` artifact
- one structured prediction log
- one explicit statement of agreement/disagreement versus market price

---

## Recommended first swarm

Default MVP swarm size: **3 researchers**

Recommended trio:
- `base-rate`
- `variant-view`
- `risk-manager`

Optional fourth:
- `catalyst-hunter`

Use `market-implied` either:
- as an additional researcher, or
- as a lightweight framing pass by Orchestrator before dispatch

---

## One-line operating model

Dispatch a small set of independent researcher personalities on one case at a time, require each to compare its view against the market-implied price, preserve qualitative reasoning in `40-research/`, preserve structured run/prediction state in Postgres, and delay durable canon updates until retrospective review.
