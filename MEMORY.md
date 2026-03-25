# MEMORY.md

## Identity and role

- Assistant identity: **Orchestrator**.
- Role: executive arbiter and state manager for a 5-agent quantitative research swarm.
- Objective: manage hierarchical memory, prevent redundant research, optimize compute, and distill raw findings into high-conviction actionable parameters.
- Preferred communication style: succinct, accurate, to-the-point.

## Memory system direction

- The research memory stack should move toward **Obsidian as the canonical human-readable vault** plus **QMD as the retrieval/index layer**.
- QMD should be treated as the swarm's retrieval substrate, not the reasoning engine itself.
- The vault should optimize for **research provenance, input quality, auditability, and retrospective pipeline improvement** rather than forecast lifecycle tracking.
- Forecast tracking is expected to live in a separate agent/system with its own memory.

## Research-memory design principles

- Organize the vault by **knowledge role**, not only by domain.
- Recommended top-level structure is parallel, not nested:
  - `00-system/`
  - `10-domains/`
  - `20-entities/`
  - `30-drivers/`
  - `40-research/`
  - `50-retrospectives/`
  - `60-uncategorized/`
- `10-domains` = subject-area knowledge.
- `20-entities` = reusable dossiers on recurring actors/objects.
- `30-drivers` = reusable causal mechanisms.
- `40-research` = actual research artifacts (source notes, agent findings, syntheses, investigations, assumptions).
- `50-retrospectives` = analysis of input quality, agent performance, methodology adjustments, missed/false signals.
- `20/30/40` are **parallel to** `10`, not nested inside it.

## Domain coverage targets

- The system should support broad prediction-market domains including:
  - Crypto
  - Culture
  - Economics
  - Geopolitics
  - Politics
  - Sports
  - Tech & AI
- Cross-domain entity and driver categories are important for reusable retrieval and analogical reasoning.

## Operational guidance

- Keep folders coarse and stable; push detail into frontmatter metadata and QMD retrieval.
- Avoid overfitting the filesystem to forecast lifecycle or overly deep folder nesting.
- Treat research artifacts as the core memory object: source notes, entity briefs, driver briefs, agent findings, investigations, syntheses, assumption notes, retrospective notes.
- Preserve provenance fields so later retrospectives can determine what inputs contributed to good or bad downstream evaluations.
- Use the vault to answer: what did we know, where did it come from, why did it matter, and which inputs shaped the eventual evaluation?
