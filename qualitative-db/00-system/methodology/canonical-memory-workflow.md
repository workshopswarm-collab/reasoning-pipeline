# Canonical Memory Workflow

## Memory layers

### Canonical layer

- `qualitative-db/10-domains/`
- `qualitative-db/20-entities/`
- `qualitative-db/30-drivers/`

Purpose:
- durable summaries
- reusable memory
- stable retrieval anchors
- domain overviews, entity overviews, and driver notes that should not be confused with research-layer syntheses

### Research layer

- `qualitative-db/40-research/`

Purpose:
- time-stamped inputs
- source captures
- agent findings
- evidence maps
- product notes
- review-queue proposals and candidates

Conceptually, additional artifact types such as syntheses or investigations may still be used later, but they are not required as live top-level folders in the current repo snapshot.

## Default rule

New research goes into the research layer first.

Do **not** edit a canonical dossier just because new information exists.

## Promotion rule

Promote research-layer information into a canonical dossier only when:
- the change is extremely material, or
- repeated evidence creates explicit conflict with the canonical summary

## Canonical update path

1. gather source notes
2. gather research findings
3. write synthesis and evidence map if needed
4. write canonical entity update proposal or equivalent promotion note in the research layer
5. let the decision-maker or orchestrator review the proposal
6. only then update the canonical dossier
7. if the case produces methodology or conflict lessons, capture them in `qualitative-db/50-retrospectives/`

## Canonical sections most likely to change

- `Current state`
- `Key strengths`
- `Key weaknesses`
- `Important recent changes`
- `Open questions`

## Canonical sections least likely to change frequently

- `What this entity is`
- `Why it matters`

## Strong recommendation

When in doubt:
- append to research
- do not rewrite canonical memory
