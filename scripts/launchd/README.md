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

## Recommended initial posture

Observe-only, one-pass, periodic launch agent:

- `watch_pipeline.py`
- `--control-managed`
- control file defaults still keep it observe-only
- no `--apply` required in the plist
- `RunAtLoad = true`
- `StartInterval = 60`

This means the watchdog can restart automatically on login/reboot **once bootstrapped into launchd**, while later behavior changes can come from the automation control file rather than reinstalling the plist.

## Current safety stance

This repo contains the rendered plists and management helpers, but **nothing here bootstraps either job automatically**.

Until someone explicitly runs a helper with `install --bootstrap` (or manually runs `launchctl bootstrap ...`), the watchdog and sequencer are **not active**.

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
