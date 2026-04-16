# Research Vault

## TL;DR

This vault is a **layered research-memory system** for a multi-role reasoning pipeline.

Authority note:
- `qualitative-db/00-system/` is the highest-priority rule layer inside the vault
- start with `qualitative-db/00-system/START-HERE.md` if you are a fresh-instance LLM
- lower-level READMEs explain local usage but should not override 00-system rules
- role permissions are defined in `qualitative-db/00-system/README.md`

Use it to store:
- durable domain knowledge
- reusable canonical entity dossiers
- reusable driver notes
- time-stamped research artifacts
- source reliability guidance
- learning artifacts

Current runtime note:
- the live research swarm executes in Telegram forum topics, with one controller topic plus one persona topic per case while research is active
- once the researcher swarm is truly terminal, synthesis promotion creates one dedicated synthesis topic for that dispatch and runs the final synthesis there
- this vault is the durable output/provenance layer for that runtime, not the execution surface itself

Do **not** treat it as:
- the forecast ledger
- the final decision engine
- a place to dump every transient update into canonical notes

**Core rule:** canonical notes change rarely; research notes change often.

---

## Terminology note

In this vault:
- a **dossier** means a **canonical entity note** in `qualitative-db/20-entities/`
- a **canonical dossier** is acceptable shorthand for a canonical entity note
- notes in `qualitative-db/40-research/` are **research notes**, not dossiers

Use this distinction consistently so canonical memory and research memory do not blur together.

## What this vault is trying to answer

This vault should help a human or LLM quickly answer:
- What do we know?
- Where did it come from?
- What objects matter?
- What mechanisms matter?
- What changed recently?
- What should influence future evaluation?

Forecast tracking is expected to live in a separate system/agent.

---

## Fast mental model

Think of the vault as six layers:

1. **System** — how the memory system works
2. **Domains** — broad subject-area knowledge
3. **Entities** — reusable canonical entity dossiers on important objects
4. **Drivers** — reusable causal mechanisms
5. **Research** — time-stamped source notes, findings, syntheses
6. **Learnings** — resolved-case reviews, recurring patterns, and what to improve

---

## Top-level map

```text
qualitative-db/
  00-system/
  10-domains/
  20-entities/
  30-drivers/
  40-research/
  50-learnings/
  60-uncategorized/
```

### `00-system/`
Meta-knowledge about how the vault works.

Use for:
- methodology
- templates
- source-reliability notes
- canonical-memory rules
- taxonomies / agent protocols / evaluation criteria

### `10-domains/`
Broad background knowledge by subject area.

Current major domains:
- crypto
- culture
- economics
- geopolitics
- politics
- sports
- tech-ai

Most important files here are usually `00-overview.md` notes.

### `20-entities/`
Canonical entity dossiers on recurring objects.

Examples:
- people
- countries
- companies
- organizations
- agencies
- products
- protocols
- parties
- teams
- players
- leagues

### `30-drivers/`
Cross-domain causal mechanisms.

Examples:
- regulation
- media-narratives
- injuries-health
- macro
- polling
- conflicts

### `40-research/`
The active evidence layer.

Use for:
- case-centric analysis history under `cases/`
- source notes
- agent findings / latest views
- review-queue proposals
- evidence maps
- assumption notes
- product notes

Important: the canonical live `40-research/` structure is moving toward `cases/<case-key>/researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/...` for rerun-safe history, while legacy flat folders such as `agent-findings/`, `assumption-notes/`, and `evidence-maps/` may remain as compatibility or latest-view surfaces during migration. Existing historical flat notes should be preserved unless they are already generated compatibility notes.
Historical references to `syntheses/` or `investigations/` should be treated as conceptual artifact types or future/optional folders, not guaranteed live directories.

### `50-learnings/`
Resolved-case learning and recursive-improvement layer.

### `60-uncategorized/`
Temporary holding area for useful notes that do not yet have a stable home.

---

## What the main note types mean

### `00-overview.md`
A fast orientation note for a domain or subdomain.

In `10-domains/`, these are canonical **domain overviews**, not research-layer syntheses.

Purpose:
- summarize what matters
- identify main evidence clusters
- identify missing information
- provide a "how to think about this area" anchor

### Canonical entity dossier
Usually under `20-entities/`.

Purpose:
- preserve durable memory about an object
- summarize current state
- list strengths, weaknesses, and open questions
- act as the canonical retrieval anchor

### Source note
Usually under `40-research/cases/<case-key>/researcher-source-notes/`.

Purpose:
- preserve provenance
- record what a source said
- explain why that source matters

### Agent finding
Usually under `40-research/cases/<case-key>/researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/personas/`.

Purpose:
- store role-specific interpretation from a research agent

### Synthesis
Usually represented by a higher-level research artifact in `40-research/`.

Purpose:
- combine multiple upstream inputs into a current interpretation

### Learning note
Usually under `50-learnings/`.

Purpose:
- record what helped, what misled, and what was missing
- capture reusable lessons from resolved cases
- support concrete intervention and promotion decisions

---

## Canonical vs research memory

## Canonical body vs linkage metadata

Within canonical notes, treat these as two different maintenance surfaces:

### Canonical body content
- slow-moving
- durability-focused
- summary-oriented
- should update only when the long-run understanding of the entity materially changes

### Linkage metadata
- mainly `related_entities` and `related_drivers`
- curated graph/navigation infrastructure
- allowed to evolve more fluidly than canonical body prose
- should be updated whenever doing so materially improves retrieval, reciprocity, or structural navigation

Important: more fluid does **not** mean sloppy.

Linkages should still be compact, high-signal, and structurally justified.

Use this distinction so the vault can keep canon prose strict without freezing the graph in an underlinked state.

### Canonical memory
Lives mainly in:
- `10-domains/`
- `20-entities/`
- `30-drivers/`

These notes are:
- slow-moving
- durable
- summary-oriented
- retrieval anchors

### Research memory
Lives mainly in:
- `40-research/`

These notes are:
- time-stamped
- evidence-bearing
- frequently updated
- allowed to be noisy and incomplete

### Canonical update rule
Update canonical notes **only** when there is:
1. an **extremely material change**, or
2. an **explicit and repeated conflict of information** that makes the current canonical summary misleading

If the threshold is not met, write to the **research layer**, not the canonical layer.

Detailed rules:
- `00-system/methodology/canonical-dossier-update-policy.md`
- `00-system/methodology/canonical-memory-workflow.md`

---

## How an LLM should navigate this vault

### If you need fast orientation
Read in this order:
1. this `README.md`
2. `qualitative-db/00-system/START-HERE.md`
3. `qualitative-db/00-system/README.md`
4. relevant layer README (`20-entities/`, `30-drivers/`, `40-research/`, or `50-learnings/`)
5. relevant `10-domains/.../00-overview.md`, `20-entities/.../*.md`, and `30-drivers/*.md`

### If you need recent evidence
Then pull from current research artifacts such as:
- `40-research/cases/<case-key>/researcher-source-notes/`
- `40-research/cases/<case-key>/researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/personas/`
- `40-research/cases/<case-key>/researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/assumptions/`
- `40-research/cases/<case-key>/researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/evidence/`
- `40-research/product-notes/`
- `40-research/review-queue/` when relevant to handoff or promotion proposals

### If you want to write new information
Default to the **research layer first**.
Do not casually rewrite canonical entity notes.

---

## Current strengths

The vault already has meaningful starter coverage in:
- major cross-domain background notes
- crypto assets, exchanges, stablecoins, and institutions
- AI labs, products, leaders, cloud/platform entities
- geopolitics leaders, countries, and strategic institutions
- basketball, baseball, football, and key teams/players/leagues
- source-reliability guidance in several areas
- QMD-compatible retrieval structure

---

## Current limitations

This is still a growing system.

Known limitations:
- some areas are broad but not yet deep
- entity density is still uneven by domain
- live-input operational layers are incomplete in some areas
- many canonical entity notes are foundation-level rather than final research-grade notes

This is expected.
The system is meant to improve through:
- more research artifacts
- selective canonical promotion
- periodic learning-loop cleanup

---

## Design rules

- keep folders coarse and stable
- push nuance into metadata and QMD retrieval
- keep canonical entity notes slow-moving
- route new information into research artifacts first
- preserve provenance whenever possible
- prefer durable summaries over note churn

---

## One-line summary

**This vault is a provenance-first research memory: stable domain/entity/driver summaries on top, time-stamped research underneath, and strict rules against casual rewriting of canonical memory.**
