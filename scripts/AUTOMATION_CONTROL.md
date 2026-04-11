# Pipeline automation control

This file documents the persisted control surface for the watchdog and sequencer.

## Control file

Default path:

- `scripts/.runtime-state/pipeline-automation-control.json`

Managed by:

- `python3 scripts/automation_control.py ...`

If the file does not exist, both services fall back to safe defaults:

- watchdog enabled but **observe-only**
- sequencer disabled
- new market claims disabled

## Key idea

There are now three separate concepts:

1. **watchdog process supervision** (`launchd`)
2. **sequencer process supervision** (`launchd`)
3. **automation state** (this control file)

That means services can be installed/bootstrapped once, while behavior is changed later by flipping the control file rather than editing plists.

## Common commands

Show current state:

```bash
python3 scripts/automation_control.py status
```

Force safe/off posture:

```bash
python3 scripts/automation_control.py disable-all
```

Enable only watchdog repairs:

```bash
python3 scripts/automation_control.py enable-watchdog-repairs --all-actions
```

Enable sequencer market-claim automation:

```bash
python3 scripts/automation_control.py enable-sequencer
```

Disable sequencer again:

```bash
python3 scripts/automation_control.py disable-sequencer
```

Patch individual fields directly:

```bash
python3 scripts/automation_control.py set \
  --automation-enabled on \
  --sequencer-enabled on \
  --allow-new-case-claims on
```

## Effective behavior

### Watchdog

The watchdog reads the control file when started with:

```bash
python3 scripts/watch_pipeline.py --control-managed
```

Current repair controls include:

- `allow_resume_swarm`
- `allow_launch_synthesis`
- `allow_launch_decision`
- `allow_finalize_decision`
- `allow_finalize_pipeline`

### Sequencer

The sequencer reads the control file when started with:

```bash
python3 scripts/run_sequential_market_pipeline.py --control-managed
```

Important distinction:

- `sequencer.enabled = true` means the sequencer service may run
- `automation_enabled = true` + `allow_new_case_claims = true` means it may claim **new** markets

This allows a useful intermediate posture:

- sequencer running
- resume existing cases allowed
- **new case claims still disabled**

## Current intended rollout

1. keep launch agents staged but not necessarily bootstrapped
2. keep control file in `disable-all` posture by default
3. enable watchdog repairs first
4. only later enable sequencer new-market claims
