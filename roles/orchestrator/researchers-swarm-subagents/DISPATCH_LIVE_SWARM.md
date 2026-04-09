# Live Swarm Dispatch Procedure

Use this procedure when launching the real 5-agent swarm from the OpenClaw runtime.

## Goal

Launch the swarm from the canonical planner-generated prompts, not from hand-written task strings.

This is a two-phase process:
- local Python/Postgres scripts prepare the dispatch plan
- the OpenClaw runtime creates fresh Telegram topics, materializes the canonical topic sessions, and executes the actual `sessions.send` handoffs into those topic sessions

For headless launches from TUI, prefer:
- `roles/orchestrator/researchers-swarm-subagents/runtime/scripts/prepare_and_launch_headless_telegram_dispatch.py`

Use the older two-step prepare-then-launch path only when you intentionally want to inspect or repair the prepared manifest before launch:
- `roles/orchestrator/researchers-swarm-subagents/runtime/scripts/prepare_headless_telegram_dispatch.py`
- `roles/orchestrator/researchers-swarm-subagents/runtime/scripts/launch_dispatch_with_stateful_posts.py`

See also:
- `roles/orchestrator/researchers-swarm-subagents/OPENCLAW_RUNTIME_BRIDGE.md`

## Phase 1 — prepare the dispatch plan

1. load case + market context
2. set `markets.pipeline_status = researching`
3. create one `research_runs` row per persona
4. for each persona, call `planner/scripts/build_researcher_prompt.py` with the full market/case context
5. emit one logical Telegram topic target plus one post-handoff DB patch template per persona

Primary planner:
- `roles/orchestrator/researchers-swarm-subagents/planner/scripts/dispatch_case_research.py`

## Phase 2 — execute the dispatch plan in runtime

6. hand the manifest to the runtime lane
7. prefer the stateful runtime launcher:
   - `roles/orchestrator/researchers-swarm-subagents/runtime/scripts/launch_dispatch_with_stateful_posts.py`
8. create/reuse the controller topic and one fresh persona topic per queued run
9. materialize each created topic as a canonical OpenClaw session, then deliver the internal persona `handoff_payload` via the runtime `sessions.send` bridge
10. after each successful handoff, apply the matching `update_research_run.py` patch so the run becomes `running`
11. treat that `queued -> running` patch as the canonical start transition; `update_research_run.py` auto-posts the visible Telegram `STARTING RESEARCH` marker
12. write delivery metadata into `research_runs.notes`, especially:
   - `delivery_target_session_key`
   - `delivery_target_chat_id`
   - `delivery_target_topic_id`
   - optional `model`
   - optional `thinking`
13. once research begins, ensure the Telegram runtime loop is running so it can supervise active lanes
14. between start and finish, persona topics may post brief progress updates sparsely (milestone-based or roughly every 10 minutes while active) so humans can see movement without spamming the runtime surface
15. completion handling should reconcile each run back from its fixed `research_run_id`
16. successful completion should auto-post the visible Telegram finish marker through `update_research_run.py`
17. the runtime loop can auto-complete stale finished work, send nudges to stalled lanes, and optionally fail hard-stalled runs
18. terminal `update_research_run.py` completion/failure updates should auto-attempt dispatch reconciliation and parent case/market finalization
19. if the automatic path is missed or you need a repair/audit step, run:
   - `runtime/scripts/runrepairs/finalize_dispatch_after_swarm.py --file <manifest> --apply`
20. finalize launch/completion summaries for Orchestrator

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
`qualitative-db/40-research/cases/<case-key>/researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/personas/<persona>.md`

### Source notes
Directory:
`qualitative-db/40-research/cases/<case-key>/researcher-source-notes/`

### Assumption note
`qualitative-db/40-research/cases/<case-key>/researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/assumptions/<persona>.md`

### Evidence map
`qualitative-db/40-research/cases/<case-key>/researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/evidence/<persona>.md`

### Per-analysis summary
`qualitative-db/40-research/cases/<case-key>/researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/summary.md`

## Rules

### Use generated prompts
Do not handwrite persona dispatch prompts when `planner/scripts/build_researcher_prompt.py` is available.
The generated prompt is the source of truth because it reflects the current researcher contract and artifact path rules.

### Do not bypass the runtime bridge from planner code
Do not try to make planner/control-plane Python deliver topic handoffs directly.

Correct pattern:
- planner scripts prepare the dispatch manifest
- runtime launcher/bootstrap creates or reuses Telegram topics
- runtime bridge/helper materializes the target topic session and delivers via `sessions.send`
- runtime helpers patch DB state using the returned delivery metadata

## Preferred combined command

For the normal headless live path, prefer the combined wrapper:

```bash
python3 roles/orchestrator/researchers-swarm-subagents/runtime/scripts/prepare_and_launch_headless_telegram_dispatch.py   --case-id <CASE_UUID>   --model openai-codex/gpt-5.4   --thinking medium   --pretty
```

Use the older two-step prepare-then-launch path only when you intentionally want to inspect or edit the prepared manifest before launch.
