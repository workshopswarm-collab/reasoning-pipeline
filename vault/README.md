# Research Vault

## TL;DR

This vault is a **layered research-memory system** for a multi-agent reasoning pipeline.

Use it to store:
- durable domain knowledge
- reusable entity dossiers
- reusable driver notes
- time-stamped research artifacts
- source reliability guidance
- retrospective lessons

Do **not** treat it as:
- the forecast ledger
- the final decision engine
- a place to dump every transient update into canonical notes

**Core rule:** canonical notes change rarely; research notes change often.

---

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
3. **Entities** — reusable dossiers on important objects
4. **Drivers** — reusable causal mechanisms
5. **Research** — time-stamped source notes, findings, syntheses
6. **Retrospectives** — what helped, what misled, what to improve

---

## Top-level map

```text
vault/
  00-system/
  10-domains/
  20-entities/
  30-drivers/
  40-research/
  50-retrospectives/
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
Canonical dossiers on recurring objects.

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
- source notes
- agent findings
- syntheses
- investigations
- evidence maps
- assumption notes

### `50-retrospectives/`
Hindsight and methodology-improvement layer.

### `60-uncategorized/`
Temporary holding area for useful notes that do not yet have a stable home.

---

## What the main note types mean

### `00-overview.md`
A fast orientation note for a domain or subdomain.

Purpose:
- summarize what matters
- identify main evidence clusters
- identify missing information
- provide a "how to think about this area" anchor

### Entity dossier
Usually under `20-entities/`.

Purpose:
- preserve durable memory about an object
- summarize current state
- list strengths, weaknesses, and open questions
- act as the canonical retrieval anchor

### Source note
Usually under `40-research/source-notes/`.

Purpose:
- preserve provenance
- record what a source said
- explain why that source matters

### Agent finding
Usually under `40-research/agent-findings/`.

Purpose:
- store role-specific interpretation from a research agent

### Synthesis
Usually under `40-research/syntheses/` or as an overview note.

Purpose:
- combine multiple upstream inputs into a current interpretation

### Retrospective note
Usually under `50-retrospectives/`.

Purpose:
- record what inputs helped or hurt
- improve future source selection and methodology

---

## Canonical vs research memory

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
2. relevant `10-domains/.../00-overview.md`
3. relevant `20-entities/.../*.md`
4. relevant `30-drivers/.../00-overview.md`

### If you need recent evidence
Then pull from:
- `40-research/source-notes/`
- `40-research/syntheses/`
- `40-research/agent-findings/`

### If you want to write new information
Default to the **research layer first**.
Do not casually rewrite canonical dossiers.

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
- many dossiers are foundation-level rather than final research-grade notes

This is expected.
The system is meant to improve through:
- more research artifacts
- selective canonical promotion
- periodic retrospective cleanup

---

## Design rules

- keep folders coarse and stable
- push nuance into metadata and QMD retrieval
- keep canonical dossiers slow-moving
- route new information into research artifacts first
- preserve provenance whenever possible
- prefer durable summaries over note churn

---

## One-line summary

**This vault is a provenance-first research memory: stable domain/entity/driver summaries on top, time-stamped research underneath, and strict rules against casual rewriting of canonical memory.**
