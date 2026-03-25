# Research Vault

This vault is the canonical human-readable research memory for the reasoning pipeline.

It is designed to be understandable by both:
- humans browsing in Obsidian or Git
- LLMs retrieving or summarizing with QMD

---

# What this vault is for

This vault is **not** the forecast ledger and **not** the final decision engine.

Its purpose is to store:
- durable domain knowledge
- reusable entity dossiers
- reusable driver notes
- time-stamped research artifacts
- source reliability guidance
- retrospective methodology improvements

The core objective is to help a multi-agent research swarm answer:
- what do we know?
- where did it come from?
- what objects matter?
- what mechanisms matter?
- what changed?
- which inputs should influence future evaluation?

Forecast tracking is expected to live in a separate system/agent.

---

# High-level mental model

Think of the vault as five interacting layers:

## 1. System layer
How the memory system works.

Contains:
- methodology
- templates
- source reliability notes
- canonical memory rules

## 2. Domain layer
Subject-area background knowledge.

Contains broad topic maps for:
- crypto
- culture
- economics
- geopolitics
- politics
- sports
- tech-ai

## 3. Entity layer
Reusable dossiers on recurring objects.

Examples:
- people
- countries
- companies
- protocols
- teams
- leagues
- parties
- agencies
- products

## 4. Driver layer
Reusable causal mechanisms that recur across many topics.

Examples:
- regulation
- media narratives
- injuries & health
- macro
- polling
- conflicts

## 5. Research layer
Time-stamped artifacts produced during research.

Examples:
- source notes
- agent findings
- syntheses
- investigations
- assumptions

## 6. Retrospective layer
Backward-looking analysis of what inputs, sources, and methods helped or hurt performance.

---

# Top-level structure

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

## `00-system/`
Use for system rules and meta-knowledge.

Includes:
- `methodology/`
- `templates/`
- `source-reliability/`
- `taxonomies/`
- `agent-protocols/`
- `evaluation-criteria/`

## `10-domains/`
Use for broad subject-area understanding.

Current major domain coverage includes:
- crypto
- culture
- economics
- geopolitics
- politics
- sports
- tech-ai

Each domain may contain subdomains with `00-overview.md` anchor notes.

## `20-entities/`
Use for canonical dossiers on recurring objects.

Current entity types include:
- agencies
- companies
- countries
- leagues
- organizations
- parties
- people
- players
- products
- protocols
- teams

## `30-drivers/`
Use for reusable cross-domain causal mechanisms.

Current strong examples:
- regulation
- media-narratives
- injuries-health

## `40-research/`
Use for time-stamped research artifacts.

Current intended structure includes:
- `source-notes/`
- `agent-findings/`
- `investigations/`
- `syntheses/`
- `evidence-maps/`
- `assumption-notes/`

## `50-retrospectives/`
Use for hindsight learning and pipeline improvement.

## `60-uncategorized/`
Temporary holding area for notes that are useful but not yet stably categorized.

---

# What the main note types mean

## `00-overview.md`
A high-level synthesis anchor for a domain or subdomain.

Purpose:
- orient quickly
- summarize what matters
- list important evidence clusters
- identify missing information

These are not raw source dumps.
They are the top-level "how to think about this area" notes.

## Entity dossiers
Usually found under `20-entities/`.

Purpose:
- preserve durable memory about important objects
- summarize current state, strengths, weaknesses, and open questions
- act as canonical anchors for retrieval

## Source notes
Usually found under `40-research/source-notes/`.

Purpose:
- preserve provenance
- record what a source said
- capture durable extracted facts and why the source matters

## Agent findings
Usually found under `40-research/agent-findings/`.

Purpose:
- hold time-stamped role-specific interpretation from scout / skeptic / quant / analyst / synthesizer style agents

## Syntheses
Usually found under `40-research/syntheses/` or as overview notes.

Purpose:
- combine multiple upstream inputs into a structured current interpretation

## Retrospective notes
Used after outcomes are known or methodology has been stress-tested.

Purpose:
- identify what inputs helped
- identify what inputs misled
- improve source selection and research process over time

---

# Canonical memory policy

This vault distinguishes between:
- **canonical memory**
- **research memory**

## Canonical memory
Canonical memory lives mainly in:
- `10-domains/`
- `20-entities/`
- `30-drivers/`

These notes are **slow-moving summaries**.
They should be updated rarely.

## Research memory
Research memory lives mainly in:
- `40-research/`

These notes are time-stamped, evidence-bearing, and can update frequently.

## Canonical update rule
Canonical dossiers should update only when there is:
1. an **extremely material change**, or
2. an **explicit and repeated conflict of information** that makes the current canonical summary misleading

If new information does **not** meet that threshold, it should remain in the research layer.

Detailed rules live in:
- `00-system/methodology/canonical-dossier-update-policy.md`
- `00-system/methodology/canonical-memory-workflow.md`

---

# How an LLM should use this vault

If you are an LLM reading this vault, use the following order of operations:

## Step 1: Orient from this README
Understand:
- the vault is layered
- canonical notes are slow-moving
- research notes are time-stamped
- this is a provenance-first memory system, not a forecast ledger

## Step 2: Start with canonical anchors
For broad understanding, read:
- relevant `10-domains/.../00-overview.md`
- relevant `20-entities/.../*.md`
- relevant `30-drivers/.../00-overview.md`

## Step 3: Pull recent evidence from research notes
If a question depends on recent developments, then read:
- `40-research/source-notes/`
- `40-research/syntheses/`
- `40-research/agent-findings/`

## Step 4: Respect update discipline
Do not casually rewrite canonical dossiers.
Prefer writing new information into research artifacts first.
Only promote into canonical memory when the materiality/conflict threshold is met.

---

# Current strengths of the vault

The vault already has meaningful starter coverage in:
- major cross-domain backgrounds
- crypto assets, institutions, and stablecoin/payment infrastructure
- AI labs, products, leaders, cloud/platform entities
- geopolitics leaders, countries, and strategic institutions
- basketball, baseball, football, and some league/team/player coverage
- source reliability guidance for several key domains
- QMD-compatible retrieval structure

---

# Current limitations

This is still an actively growing memory system.

Known limitations:
- some subdomains are broader than they are deep
- some entity coverage is uneven across domains
- live-input operational layers are stronger in some areas than others
- many notes are foundational starter dossiers, not yet full research-grade dossiers

This is expected. The design is intended to scale through:
- repeated research artifacts
- selective canonical promotion
- periodic retrospective cleanup

---

# Design rules

- keep folders coarse and stable
- push nuance into frontmatter metadata and QMD retrieval
- treat canonical dossiers as slow-moving memory
- route new information into research artifacts first
- preserve provenance whenever possible
- prefer durable summaries over noisy note churn

---

# One-line summary

**This vault is a layered research-memory system: canonical domain/entity/driver knowledge on top, time-stamped research artifacts underneath, and strict rules preventing casual rewrites of canonical memory.**
