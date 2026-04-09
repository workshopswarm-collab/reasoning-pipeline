# Synthesis Execution Architecture

## Intended execution model

The synthesis layer should not reuse arbitrary existing sessions.
It should run through dedicated subagents that Orchestrator wakes explicitly.

## Dedicated roles

### Persona reasoning extraction
- one dedicated extraction subagent per persona extraction run
- launched or resumed by Orchestrator for that extraction task
- responsible only for producing one reasoning-extract JSON payload

### Final synthesis
- one dedicated synthesis subagent per dispatch synthesis run
- launched or resumed by Orchestrator after the extracts-synthesis bundle is ready
- responsible only for producing one final synthesis JSON payload

## Separation of responsibility

Orchestrator owns:
- bundle building
- prompt building
- subagent wake/spawn orchestration
- validation
- rendering
- sidecar writing

Extraction/synthesis subagents own:
- semantic reasoning work only
- JSON output only

## Why

This keeps:
- Orchestrator deterministic and stateful
- reasoning workers fresh-context and task-bounded
- extraction and synthesis separate from one another
- execution closer to the researcher-swarm architecture
