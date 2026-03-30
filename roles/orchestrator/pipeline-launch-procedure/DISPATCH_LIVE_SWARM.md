# Live Swarm Dispatch Procedure

Use this procedure when launching the real 5-agent swarm from the OpenClaw runtime.

## Goal

Launch the swarm from the canonical planner-generated prompts, not from hand-written task strings.

This is a two-phase process:
- local Python/Postgres scripts prepare the dispatch plan
- the OpenClaw runtime executes the actual `sessions_send` handoffs into fixed Discord persona channels

For headless launches from TUI, prefer:
- `roles/orchestrator/pipeline-launch-procedure/runtime/scripts/prepare_headless_discord_dispatch.py`

See also:
- `roles/orchestrator/pipeline-launch-procedure/OPENCLAW_RUNTIME_BRIDGE.md`

## Phase 1 — prepare the dispatch plan

1. load case + market context
2. set `markets.pipeline_status = researching`
3. create one `research_runs` row per persona
4. for each persona, call `planner/scripts/build_researcher_prompt.py` with the full market/case context
5. emit one channel handoff payload plus one post-handoff DB patch template per persona

Primary planner:
- `roles/orchestrator/pipeline-launch-procedure/planner/scripts/dispatch_case_research.py`

## Phase 2 — execute the dispatch plan in runtime

6. hand the manifest to the runtime lane
7. run the thin runtime harness flow using:
   - `roles/orchestrator/pipeline-launch-procedure/runtime/scripts/run_dispatch_runtime.py`
8. use each emitted `handoff_payload` as the literal input to `sessions_send`
9. remember that this handoff is internal to the persona session and may not itself be visible in Discord
10. after each successful handoff, apply the matching `update_research_run.py` patch so the run becomes `running`
11. write delivery metadata into `research_runs.notes`, especially:
   - `delivery_target_session_key`
   - `delivery_target_channel_id`
   - optional `model`
   - optional `thinking`
12. persona lanes should post visible lifecycle updates in-channel when possible using the standardized STARTING/FINISHED format
13. completion handling should reconcile each run back from its fixed persona lane
14. terminal `update_research_run.py` completion/failure updates should auto-attempt dispatch reconciliation and parent case/market finalization
15. if the automatic path is missed or you need a repair/audit step, run:
   - `runtime/scripts/finalize_dispatch_after_swarm.py --file <manifest> --apply`
16. finalize launch/completion summaries for Orchestrator

## Partial delivery rule

If only some personas receive handoff successfully:
- keep successful runs active
- patch successful runs to `status = running`
- return `delivered_partial`
- retry only the runs that are still `queued`

## Completion rule

When persona lanes later complete:
- resolve them back to the corresponding `research_runs` row
- patch successful runs to `completed`
- patch errored runs to `failed`
- use runtime-side DB helpers as the completion-side mechanism

## Default artifact paths

### Primary finding
`qualitative-db/40-research/agent-findings/<persona>/<case_key>-<slug>.md`

### Source notes
Directory:
`qualitative-db/40-research/source-notes/by-market/`

Filename prefix:
`<case_key>-<persona>-`

### Assumption note
`qualitative-db/40-research/assumption-notes/<case_key>-<persona>-assumptions.md`

### Evidence map
`qualitative-db/40-research/evidence-maps/<case_key>-<persona>-evidence-map.md`

## Rules

### Use generated prompts
Do not handwrite persona dispatch prompts when `planner/scripts/build_researcher_prompt.py` is available.
The generated prompt is the source of truth because it reflects the current researcher contract and artifact path rules.

### Do not call runtime tools from local Python
Do not try to make local subprocess Python call `sessions_send` directly.

Correct pattern:
- planner scripts prepare the dispatch manifest
- OpenClaw runtime executes the handoff payloads
- runtime helpers patch DB state using the returned delivery metadata
