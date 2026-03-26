# Quant Research Swarm Workspace

This workspace is the control plane and memory substrate for a multi-agent prediction-market / quantitative research pipeline.

At a high level, the system is split into two kinds of state:

- **Vault / markdown memory** → qualitative reasoning, provenance, syntheses, retrospectives, and durable domain/entity/driver knowledge
- **PostgreSQL** → structured market state, portfolio state, execution state, outcomes, calibration, attribution, and agent-weight data

The vault is **not** the forecast ledger or execution engine.
The database is **not** the human-readable reasoning layer.

## Core architecture

```mermaid
%%{init: {"flowchart": {"nodesep": 80, "ranksep": 80}}}%%
flowchart TD
 %% Class Definitions
 classDef orchestrator fill:#EFF6FF,stroke:#3B82F6,stroke-width:2px,color:#1E3A8A;
 classDef swarm fill:#ECFDF5,stroke:#10B981,stroke-width:2px,color:#064E3B;
 classDef decision fill:#FAF5FF,stroke:#8B5CF6,stroke-width:2px,color:#4C1D95;
 classDef executor fill:#FFFBEB,stroke:#D97706,stroke-width:2px,color:#92400E;
 classDef evaluator fill:#F5F3FF,stroke:#7C3AED,stroke-width:2px,color:#4C1D95;
 classDef memory fill:#F8FAFC,stroke:#64748B,stroke-width:2px,stroke-dasharray: 5 5,color:#0F172A;
 classDef external fill:#FFF1F2,stroke:#F43F5E,stroke-width:2px,color:#881337;

 %% --- START ---
 Start([<b>Data Pipeline</b>:<br>New Market Event]):::external

 %% --- DEVICE A: INTELLIGENCE ---
 subgraph Device_A[<b>DEVICE A: OpenClaw Intelligence</b><br>Local M4 Mac Mini]
 direction TB
 
 subgraph P1[<b>Phase 1: Deep Research</b>]
 O_Dispatch[<b>Orchestrator</b>:<br>Spawns Swarm]:::orchestrator
 Researchers[<b>Research Swarm</b>:<br>Independent Analysts with<br>Diverse Personalities / Priors]:::swarm
 end

 subgraph P2[<b>Phase 2: Tactical Decision</b>]
 O_Synth[<b>Orchestrator</b>:<br>Synthesize & Weighted Ensembling]:::orchestrator
 DM[<b>Decision-Maker</b><br>Decision Packet:<br>Action Zones, Constraints,<br>Invalidation]:::decision
 end
 
 Vault[(<b>Obsidian Vault</b><br>Qualitative Knowledge<br>30-Drivers)]:::memory
 end

 %% --- THE HARDWARE BORDER ---
 PostgreSQL[(<b>Quantitative Prediction Data and Portfolio Data</b><br>SHARED POSTGRESQL Database)]:::memory

 %% --- DEVICE B: EXECUTION ---
 subgraph Device_B[<b>DEVICE B: Execution & Accounting</b><br>External M4 Mac Mini <br>Isolated Environment]
 direction TB
 
 subgraph P3[<b>Phase 3: Automated Execution</b>]
 Monitor[Execution Script:<br>Live Price vs. Decision Packet]:::executor
 Trade_Action[Order Manager:<br>Sign & Push Transactions]:::executor
 end

 subgraph P4_Acc[<b>Phase 4a: Accounting</b>]
 Accounting[Accounting Script:<br>Calculate PnL, Brier,<br>Lifecycle Metrics]:::executor
 end
 end

 %% --- EXTERNAL MARKET ---
 Market_API((Prediction Market APIs)):::external

 %% --- THE FEEDBACK LOOP ---
 subgraph P4_Retro[<b>Phase 4b: Learning</b>]
 Eval[<b>Evaluator</b>:<br>Calibration, Attribution,<br>Trust Weight Updates]:::evaluator
 O_Retro[<b>Orchestrator</b>:<br>Causal Retrospective &<br>Qualitative Learning]:::orchestrator
 end

 %% --- VERTICAL FLOW LOGIC ---
 Start -.->|Writes market metadata| PostgreSQL
 Start ===> O_Dispatch
 
 O_Dispatch ---> Researchers
 Researchers ===> O_Synth
 O_Synth ---> DM

 %% --- DEVICE A STATE INTERACTIONS ---
 O_Dispatch <-->|Reads market state &<br>performance context| PostgreSQL
 Researchers <==>|Read / write logic| Vault
 Researchers -.->|Append-only: log predictions,<br>conviction, timestamps| PostgreSQL
 O_Synth <==>|Reads findings / writes synthesis| Vault
 O_Synth <-->|Reads priors &<br>researcher logs| PostgreSQL
 DM <==>|Reads synthesis / targeted notes| Vault
 
 %% COMBINED DM EDGE: Eliminates double-crossing lines
 DM <-->|Reads market state & portfolio context<br>Writes decision packet| PostgreSQL

 %% --- DATABASE TO DEVICE B ---
 PostgreSQL -->|Reads decision packet| Monitor
 Monitor ---> Trade_Action
 Trade_Action <==>|Execute via API keys| Market_API
 Trade_Action ---> Accounting

 %% --- ACCOUNTING BACK TO DB ---
 Accounting -->|Writes fills, realized PnL,<br>Brier, lifecycle facts| PostgreSQL

 %% --- LEARNING LOOP ---
 %% COMBINED EVAL EDGE: Eliminates double-crossing lines
 Eval <-->|Reads realized stats<br>Writes updated trust weights & calibration| PostgreSQL
 PostgreSQL -->|Reads final stats| O_Retro
 O_Retro -.->|Updates drivers / qualitative knowledge| Vault
```

## How the pipeline works

## Phase 0: External trigger
A separate data pipeline identifies a new high-value market event and writes initial market metadata into PostgreSQL.

This is the entry point into the intelligence pipeline.

## Phase 1: Deep research
The **Orchestrator** decides that the market is worth work, scopes the case, and spawns a research swarm.

The research swarm is best thought of as **multiple independent analysts performing the same general research task under different personalities, priors, and temperaments**, rather than a rigid set of specialist functions.

Examples of useful diversity:
- more skeptical vs more constructive framing
- base-rate-heavy vs narrative-heavy interpretation
- more aggressive vs more conservative weighting
- faster exploratory vs slower careful synthesis style

Researchers primarily interact with:
- the **Vault** for qualitative note-taking and provenance
- **PostgreSQL** for append-only prediction logs, conviction, and timestamps

Researchers should normally write into `vault/40-research/`, not stable canonical layers.

## Phase 2: Tactical decision
The **Orchestrator** reviews the research outputs and produces a synthesized view.

Then the **Decision-Maker**:
- reviews the synthesis and selected underlying notes
- checks structured market / portfolio context in PostgreSQL
- produces a **decision packet**

A decision packet should include things like:
- action zones
- constraints
- invalidation logic
- other execution-relevant conditions

That decision packet is stored in PostgreSQL as structured state.

## Phase 3: Automated execution
In a separate isolated execution environment, a monitor script watches live prices against the decision packet.

If conditions are met:
- the **Order Manager** signs and pushes transactions through prediction-market APIs
- execution and fills are recorded
- the **Accounting** layer computes realized PnL, Brier, and other lifecycle metrics

Execution is intentionally separated from OpenClaw intelligence so the reasoning environment does not directly control private keys or execution infrastructure.

## Phase 4a: Quantitative learning
The **Evaluator** reads realized stats from PostgreSQL and updates:
- calibration metrics
- attribution metrics
- trust weights
- other quantitative performance measures

This is the structured evaluation loop.

## Phase 4b: Qualitative learning
The **Orchestrator** reads final stats and runs a retrospective.

The retrospective should answer:
- what actually mattered?
- what misled the pipeline?
- which sources or assumptions were useful or harmful?
- what should change in future research?
- which durable lessons should update `30-drivers` or other qualitative memory?

This is the qualitative learning loop.

## Responsibilities by component

### Orchestrator
Owns the control plane:
- selects cases
- spawns researchers
- synthesizes research
- triggers retrospectives
- maintains qualitative memory and promotes durable lessons carefully

### Research swarm
Owns parallel evidence generation:
- independent analysis of the same case
- divergent framing driven by different personalities / priors
- explicit disagreement and alternative weighting
- structured findings in `vault/40-research/`

### Decision-Maker
Owns the final suggested action:
- validates or challenges the orchestrator synthesis
- checks portfolio / market context
- emits the structured decision packet

### Evaluator
Owns quantitative performance review:
- calibration
- attribution
- trust-weight updates
- cross-lifecycle measurement

### Vault
Owns human-readable research memory:
- provenance
- source notes
- syntheses
- assumptions
- retrospectives
- stable domains / entities / drivers

Start at `vault/README.md` for the memory-system map.

### PostgreSQL
Owns structured quantitative state:
- market metadata
- researcher prediction logs
- decision packets
- fills and PnL
- lifecycle metrics
- calibration history
- trust weights
- portfolio state

### Execution environment
Owns action and accounting:
- reads the structured decision packet
- executes against market APIs
- records fills and realized metrics
- remains isolated from the OpenClaw reasoning environment

## Design principles

- **Qualitative and quantitative state stay separate**
  - Vault = reasoning and provenance
  - PostgreSQL = structured state and evaluation

- **Researchers write to research first**
  - new evidence belongs in `vault/40-research/`
  - stable layers update only under stronger review thresholds

- **Human remains in the loop**
  - the system is a decision-support and execution architecture, not an unbounded autonomous black box

- **Execution is isolated from reasoning**
  - private keys and trade execution should not live in the same environment as the research swarm

- **Retrospectives drive durable learning**
  - structured metrics update quantitative trust
  - qualitative retrospectives update drivers and other durable memory

## Repository orientation

Current key top-level areas:

- `vault/` → qualitative research memory system
- `memory/` → assistant continuity / daily memory
- `MEMORY.md` → compact long-term assistant memory
- `qmd.yml` → retrieval/index configuration for the vault
- `scripts/` → automation, ETL, reporting, and bridge logic

A likely future structured-data area would be something like:

```text
data/
  README.md
  schema/
  migrations/
  views/
```

The live PostgreSQL database itself is runtime infrastructure, not a file that belongs in git.

## Current status

This repository currently has a well-developed qualitative memory system in the vault.
The PostgreSQL-backed quantitative layer and isolated execution layer are the next major architectural expansion.

That means the vault is already serving as the reasoning substrate, while the structured state / execution system is the major next buildout.
