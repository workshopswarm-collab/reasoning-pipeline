# Pipeline watchdog launchd

This folder contains the repo-local `launchd` management surface for the pipeline watchdog.

## Goal

Run the watchdog in a **safe, non-fully-automated** posture:

- observe-only by default
- single-pass per invocation
- launched periodically by `launchd`
- **never claims new markets/cases**
- only touches existing cases if a future deployment explicitly enables `--apply` and allow-flags

## Files

- `manage_pipeline_watchdog_launch_agent.py`
  - renders a launch agent plist
  - can stage/install it into `~/Library/LaunchAgents`
  - can query launchd bootstrap status
  - can uninstall it later
- `ai.openclaw.orchestrator.pipeline-watchdog.plist`
  - rendered repo-local watchdog plist for the recommended initial deployment posture
- `manage_pipeline_sequencer_launch_agent.py`
  - renders/stages/queries a repo-local launch agent for `run_sequential_market_pipeline.py`
  - uses `--loop` + `--control-managed` so launchd supervision can be prepared before automation is actually enabled
- `ai.openclaw.orchestrator.pipeline-sequencer.plist`
  - rendered repo-local control-managed sequencer plist, intentionally not installed/bootstrapped by default
- `manage_pipeline_healthcheck_launch_agent.py`
  - renders/stages/queries a repo-local launch agent for `check_pipeline_health.py`
  - intended as an external stale/failure monitor for the sequencer heartbeat/runtime state
  - also runs a small canonical case-artifact contract audit so future `case_id`/`case_key` drift is surfaced automatically
- `ai.openclaw.orchestrator.pipeline-healthcheck.plist`
  - rendered repo-local periodic health-check plist for the sequencer heartbeat/quarantine/report surfaces
- `manage_decided_market_watcher_launch_agent.py`
  - renders/stages/queries a repo-local launch agent for `watch_decided_market_prices.py`
  - polls only already-decided open markets from shared Postgres, watches them for material price changes, and reopens them into `pending_research` for the existing refresh pipeline
- `ai.openclaw.orchestrator.decided-market-watcher.plist`
  - rendered repo-local periodic watcher plist for tracked already-decided markets

## Recommended initial posture

Observe-only, one-pass, periodic launch agent:

- `watch_pipeline.py`
- `--control-managed`
- control file defaults still keep it observe-only
- no `--apply` required in the plist
- `RunAtLoad = true`
- `StartInterval = 60`

This means the watchdog can restart automatically on login/reboot **once bootstrapped into launchd**, while later behavior changes can come from the automation control file rather than reinstalling the plist.

The watchdog/sequencer shared status layer only enumerates canonical `case-*` roots for active case pipeline state, while the health-check surface now separately audits for any non-canonical legacy status roots or case-root artifact drift.

## Current safety stance

This repo contains the rendered plists and management helpers, but **nothing here bootstraps any of these jobs automatically**.

Until someone explicitly runs a helper with `install --bootstrap` (or manually runs `launchctl bootstrap ...`), the watchdog, sequencer, health-check, and decided-market-watcher jobs are **not active**.

## Common commands

Render/update the repo-local plist:

```bash
python3 scripts/launchd/manage_pipeline_watchdog_launch_agent.py render
```

Check whether the user LaunchAgent is bootstrapped:

```bash
python3 scripts/launchd/manage_pipeline_watchdog_launch_agent.py status
```

Install into `~/Library/LaunchAgents` but do **not** start it yet:

```bash
python3 scripts/launchd/manage_pipeline_watchdog_launch_agent.py install
```

Install and bootstrap it into launchd:

```bash
python3 scripts/launchd/manage_pipeline_watchdog_launch_agent.py install --bootstrap
```

Render/update the repo-local sequencer plist:

```bash
python3 scripts/launchd/manage_pipeline_sequencer_launch_agent.py render
```

Check sequencer launchd status:

```bash
python3 scripts/launchd/manage_pipeline_sequencer_launch_agent.py status
```

Install the sequencer plist without starting it:

```bash
python3 scripts/launchd/manage_pipeline_sequencer_launch_agent.py install
```

Install and bootstrap the sequencer:

```bash
python3 scripts/launchd/manage_pipeline_sequencer_launch_agent.py install --bootstrap
```

Render/update the repo-local health-check plist:

```bash
python3 scripts/launchd/manage_pipeline_healthcheck_launch_agent.py render
```

Render/update the decided-market watcher plist:

```bash
python3 scripts/launchd/manage_decided_market_watcher_launch_agent.py render
```

Check health-check launchd status:

```bash
python3 scripts/launchd/manage_pipeline_healthcheck_launch_agent.py status
```

Install the health-check plist without starting it:

```bash
python3 scripts/launchd/manage_pipeline_healthcheck_launch_agent.py install
```

Install and bootstrap the health-check agent:

```bash
python3 scripts/launchd/manage_pipeline_healthcheck_launch_agent.py install --bootstrap
```

Install the decided-market watcher plist without starting it:

```bash
python3 scripts/launchd/manage_decided_market_watcher_launch_agent.py install
```

Install and bootstrap the decided-market watcher agent:

```bash
python3 scripts/launchd/manage_decided_market_watcher_launch_agent.py install --bootstrap
```

Uninstall the staged LaunchAgent file:

```bash
python3 scripts/launchd/manage_pipeline_watchdog_launch_agent.py uninstall
```

Boot it out of launchd and uninstall:

```bash
python3 scripts/launchd/manage_pipeline_watchdog_launch_agent.py uninstall --bootout
```

## Logs

By default the rendered plist writes to:

- `scripts/.runtime-state/launchd/pipeline-watchdog.stdout.log`
- `scripts/.runtime-state/launchd/pipeline-watchdog.stderr.log`

The sequencer/watch surfaces now also expose repo-local runtime state files under `scripts/.runtime-state/`, including:

- `pipeline-heartbeat.json`
  - current sequencer heartbeat / last-pass status / periodic-task timestamps
- `pipeline-quarantine.json`
  - temporarily quarantined case_keys / market_ids after soft-fail handling
- `pipeline-health-report.json`
  - machine-readable health-check report written by `scripts/check_pipeline_health.py`
- `pipeline-artifact-contract-report.json`
  - machine-readable audit report for canonical case-root artifact contract / `case_key` drift checks
- `decided-market-watcher-heartbeat.json`
  - machine-readable heartbeat/report written by `scripts/watch_decided_market_prices.py`

Health check command:

```bash
python3 scripts/check_pipeline_health.py --pretty
```

Standalone artifact-contract regression check:

```bash
python3 scripts/check_case_artifact_contract.py --pretty
```

One-shot decided-market watcher run:

```bash
python3 scripts/watch_decided_market_prices.py --apply --pretty
```

## If/when enabling repairs later

The helper can also render/install a more active watchdog, but that is **not** the recommended initial posture.

Example of a bounded future posture:

```bash
python3 scripts/launchd/manage_pipeline_watchdog_launch_agent.py install \
  --apply \
  --allow-finalize-pipeline \
  --allow-finalize-decision
```

That still would not claim new markets, but it would allow narrow repair/finalization on already-open cases.
