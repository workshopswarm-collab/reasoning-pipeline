# Live Swarm Dispatch Procedure

Use this procedure when launching the real 5-agent swarm from the OpenClaw agent runtime.

## Goal

Launch the full case swarm using the generated prompt text from `roles/orchestrator/pipeline-launch-procedure/planner/scripts/build_researcher_prompt.py` rather than a hand-written task string.

This is a **two-phase** process:
- local Python/Postgres scripts prepare the dispatch plan
- the TUI/main OpenClaw runtime executes the actual `sessions_send` handoffs into fixed Discord persona channels

For headless launches from TUI, prefer the wrapper:
- `roles/orchestrator/pipeline-launch-procedure/runtime/scripts/prepare_headless_discord_dispatch.py`

That wrapper emits the manifest path plus one prepared `sessions_send` step per persona channel.

See also:
- `roles/orchestrator/pipeline-launch-procedure/OPENCLAW_RUNTIME_BRIDGE.md`

## Required order

### Phase 1 — prepare the dispatch plan

1. Load case + market context.
2. Set `markets.pipeline_status = researching`.
3. Create one `research_runs` row per persona.
4. For each persona, call `roles/orchestrator/pipeline-launch-procedure/planner/scripts/build_researcher_prompt.py` with:
   - `agent_label`
   - `case_id`
   - `case_key`
   - `market_id`
   - `external_market_id`
   - `slug`
   - `title`
   - `description`
   - `current_price`
   - `closes_at`
   - `resolves_at`
   - `metadata`
   - `workspace_note_path`
   - optional exact artifact-path overrides if needed
5. Emit one channel handoff payload plus one post-handoff DB patch template per persona.

Primary planner:
- `roles/orchestrator/pipeline-launch-procedure/planner/scripts/dispatch_case_research.py`

### Phase 2 — execute the dispatch plan in OpenClaw runtime

6. Hand the manifest to the runtime lane.
7. Run the thin runtime harness flow using:
   - `roles/orchestrator/pipeline-launch-procedure/runtime/scripts/run_dispatch_runtime.py`
8. Use each emitted launchable `handoff_payload` as the literal input to `sessions_send`.
9. Remember that this handoff is internal to the persona session and may not itself be visible in Discord.
10. After each successful handoff, build the filled post-handoff patch and patch the matching `research_runs` row through `update_research_run.py`, setting the run to `running`.
11. Fill `research_runs.notes` with delivery metadata from the handoff result, especially:
   - `delivery_target_session_key`
   - `delivery_target_channel_id`
   - optional `model`
   - optional `thinking`
12. Persona lanes should post visible lifecycle updates in-channel using the standardized STARTING/FINISHED format.
13. Persona lanes should post visible lifecycle updates in-channel using the standardized STARTING/FINISHED format when possible.
14. Completion handling should then reconcile each run back from its fixed persona lane.
15. Terminal `update_research_run.py` completion/failure updates now auto-attempt dispatch reconciliation and parent case/market finalization.
16. If that automatic path is missed or you need a manual repair, run:
   - `runtime/scripts/finalize_dispatch_after_swarm.py --file <manifest> --apply`
17. The manual finalizer reconciles any artifact-vs-DB lag and returns post-finalization counts.
18. Finalize launch/completion summaries for Orchestrator.

If only some personas receive handoff successfully:
- keep successful runs active
- patch successful runs to `status = running`
- return `delivered_partial`
- retry only the runs that are still `queued`

When persona lanes later complete:
- resolve them back to the corresponding `research_runs` row
- patch successful runs to `completed`
- patch errored runs to `failed`
- use runtime-side DB helpers as the completion-side mechanism

## Default artifact path rules

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

## Rule

Do not handwrite persona dispatch prompts when `roles/orchestrator/pipeline-launch-procedure/planner/scripts/build_researcher_prompt.py` is available. The generated prompt is the source of truth because it reflects the latest researcher contract and artifact path rules.

Do not try to make local subprocess Python call `sessions_send` directly. The correct pattern is:
- planner scripts prepare the dispatch manifest
- the OpenClaw runtime executes the handoff payloads
- runtime helpers patch DB state using the returned delivery metadata
