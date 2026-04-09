---
type: system_guide
domain: research
status: active
last_updated: 2026-03-25
owner: orchestrator
tags: [research/guide, qualitative-db/40-research, workflow]
---

# 40-research

This README is subordinate to `qualitative-db/00-system/README.md` and related 00-system policy files. If there is any conflict, follow `qualitative-db/00-system/`.

Fresh-instance shortcut:
1. read `qualitative-db/00-system/START-HERE.md`
2. read `qualitative-db/00-system/README.md`
3. read this file if you are doing case-specific work or adding new evidence

Terminology note:
- notes in `qualitative-db/40-research/` are research notes, not dossiers
- in vault policy language, a dossier means a canonical entity note in `qualitative-db/20-entities/`

This folder is the working research layer.

Runtime note:
- live research-swarm execution currently happens in persistent Telegram case/persona topics
- `40-research/` is where those runs write durable artifacts, provenance, and auditable case outputs
- canonical case/rerun history now centers on `40-research/cases/<case-key>/researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/...`

Use it for:
- time-indexed observations
- source extraction
- interim reasoning
- research outputs
- explicit assumptions
- evidence organization
- synthesis before canon updates

Do **not** use this folder for stable entity memory. Stable background context belongs in `qualitative-db/20-entities/` and stable domain framing belongs in `qualitative-db/10-domains/`.

Before starting case-specific work, check `qualitative-db/30-drivers/README.md` and any relevant driver files.

Use `30-drivers/` for reusable causal mechanisms such as:
- regulation
- polling
- macro
- media-narratives
- product-launches
- injuries-health
- conflicts
- seasonality

Use `40-research/` for how those drivers show up in the specific case you are studying.

Important authority rule:
- researchers read from `30-drivers/`
- researchers write case-specific work into `40-research/`
- the decision-maker, not ordinary researchers, is the normal writer to `30-drivers/`
- durable promoted lessons should usually flow through `50-retrospectives/` as part of the final review loop

Researchers may also use `40-research/` to flag:
- missing canonical links
- graph-repair candidates
- likely reciprocal links that are absent
- linkage patterns that seem structurally underbuilt

Those linkage proposals do not need to be framed as full canonical entity note rewrites. They are often graph-maintenance suggestions for later application in stable layers.

The main purpose of `40-research/` is to preserve **provenance and reasoning traceability** so later work can answer:
- what was known at the time?
- what evidence was used?
- what assumptions were made?
- what was missed?
- which notes were most useful or least useful in retrospect?

## Conflict resolution rule

If researchers conflict, preserve the conflict here rather than flattening it early.

Use `40-research/` to record:
- competing factual claims
- competing interpretations of the same evidence
- competing weighting judgments
- competing assumptions
- what evidence would resolve the disagreement

Do **not** silently overwrite one research view with another.

The default workflow is:
1. preserve both views in `40-research/`
2. make the disagreement explicit in findings, evidence maps, or syntheses
3. let the decision-maker adjudicate the conflict
4. record resolved-case lessons in `qualitative-db/50-retrospectives/`
5. promote durable lessons into stable layers only after final review

---

# Folder guide

## `cases/`

Purpose:
- provide the canonical case-centric surface for rerun-safe research history
- keep one stable folder per case and one append-only analysis folder per dispatch/rerun

Current canonical pattern:
- `cases/<case-key>/case.md` = stable case identity / contract surface
- `cases/<case-key>/researcher-swarm-current.md` = generated latest/current view
- `cases/<case-key>/timeline.md` = generated lifecycle summary
- `cases/<case-key>/researcher-source-notes/` = case-level source provenance
- `cases/<case-key>/researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/...` = per-analysis findings / assumptions / evidence

Compatibility note:
- legacy flat folders such as `agent-findings/`, `assumption-notes/`, and `evidence-maps/` may still exist during migration, but the case-centric `cases/` tree is the canonical write path going forward
- when safe, Orchestrator can generate non-destructive compatibility/latest-view notes at the old flat paths; existing historical flat notes are preserved unless they are already generated compatibility notes

## `researcher-source-notes/`

Purpose:
- capture what a source said
- record extracted facts, direct claims, uncertainties, and source-quality notes
- preserve provenance for later review

Use when:
- reading an article, filing, transcript, data page, official source, benchmark page, standings page, company post, or policy document
- preserving what the source actually said before interpreting it

Subfolders / canonical pattern:
- `cases/<case-key>/researcher-source-notes/` = default home for case-specific provenance notes created during active market research
- legacy flat source-note folders have been retired from the canonical case workflow

Good output:
- what the source directly states
- key extracted facts
- what remains uncertain
- reliability notes

Default dispatch rule:
- for active case work, researchers should normally use the assigned `cases/<case-key>/researcher-source-notes/` path and filename convention rather than inventing alternate locations

Do not use for:
- final judgment
- broad synthesis
- long-run canon

## `agent-findings/`

Purpose:
- compatibility / latest-view surface during migration from flat persona notes to the case-centric `cases/` tree
- preserve a convenient persona-first view where needed without treating it as canonical history

Current role folders:
- `base-rate/`
- `market-implied/`
- `variant-view/`
- `risk-manager/`
- `catalyst-hunter/`

Interpret these folders as recurring research personalities or styles, not as hard specialist job boundaries. The intended pattern is usually several researchers doing broadly the same market analysis with different priors, temperaments, update styles, and reactions to the market-implied view.

Suggested role intent:
- `base-rate/` -> starts from historical frequency, structural priors, and outside-view reasoning
- `market-implied/` -> treats the live market price as an information-rich prior and asks whether the market is efficiently aggregating evidence
- `variant-view/` -> explicitly looks for the strongest non-consensus interpretation and where the market may be wrong
- `risk-manager/` -> focuses on disconfirming evidence, fragility, hidden assumptions, and what would break the thesis
- `catalyst-hunter/` -> focuses on timing, upcoming information releases, trigger events, and why repricing might happen soon

Use when:
- multiple independent researchers are asked to analyze the same case from different personalities or priors
- you want to evaluate those distinct takes later against each other or against outcomes

Good output:
- explicit claim or conclusion
- explicit comparison versus the market-implied view at the current price
- rationale
- supporting notes referenced via `upstream_inputs`
- what this researcher weighted differently from another plausible take
- open questions and caveats

Default dispatch rule:
- each researcher run should have one primary assigned `agent-finding` path, and that path should be treated as mandatory rather than advisory

Do not use for:
- raw source extraction without interpretation
- stable canonical entity notes

## `assumption-notes/`

Purpose:
- isolate assumptions that may later prove correct or incorrect
- make hidden premises auditable

Use when:
- a forecast or thesis depends on specific assumptions
- you want assumptions to be retrievable separately from the final conclusion
- the assumptions are material enough to deserve their own object rather than being buried in prose

Examples:
- an election assumes polling error stays within normal bounds
- a product thesis assumes distribution matters more than benchmark quality
- a title market thesis assumes current health and rotations remain stable

Good output:
- explicit assumption
- why it matters
- what would falsify it
- what downstream notes depend on it

Do not create an assumption note just because assumptions exist in the abstract; create one when separate retrieval and auditability are actually valuable.

## `evidence-maps/`

Purpose:
- organize evidence around a claim, market question, or operational proposition
- separate supporting evidence, contrary evidence, and unresolved uncertainty
- make update logic auditable

Use when:
- moving from raw notes into an actual view
- preserving why a judgment changed
- making it possible to review which evidence was weighted correctly or poorly

Good output:
- exact question being evaluated
- starting view or prior
- evidence for
- evidence against
- ambiguous evidence
- key assumptions
- key uncertainties
- disconfirming signals to watch
- net update logic
- explicit statement of where researchers disagree, if disagreement exists

Why this matters:
- source notes say what a source said
- evidence maps say how the evidence bears on the claim

This folder is especially important for later prediction-market grading and research-performance review.

## `product-notes/`

Purpose:
- track release-specific or version-specific product observations
- record dated notes on launches, model versions, product deltas, infrastructure releases, pricing changes, and user response

Use when:
- the object is too time-bound or version-specific for stable canon
- you want to compare what was expected at launch versus what happened later
- the versioned product object itself is a meaningful research object, not just background context for a market

Current subfolder:
- `versioned-ai-products/`

Good output:
- research focus
- signals to monitor
- current hypotheses
- uncertainties
- how the note should be used later in evaluation

Do not use for:
- stable family-level context that belongs in canon
- ordinary case provenance that should instead live in `researcher-source-notes/`
- the main directional take, which should instead live in `agent-findings/`

## `syntheses/` (optional / not currently instantiated as a live folder)

Purpose:
- combine multiple inputs into a higher-level view
- distill source notes, findings, and evidence maps into something reusable

Historical/expected subfolders when used:
- `by-entity/`
- `by-topic/`

Use when:
- enough source material exists that a distilled view is useful
- you want a reusable summary before deciding whether canon should be updated

Good output:
- major conclusions
- what evidence mattered most
- what remains uncertain
- what this synthesis should feed into next

Do not use for:
- raw source extraction
- one-source notes

Important:
- this artifact type is still valid conceptually
- but `qualitative-db/40-research/syntheses/` is not currently present as a live directory in this repo snapshot
- if syntheses are revived, they should follow the current 00-system templates and role permissions

## `review-queue/`

Purpose:
- hold research-layer proposals and handoff artifacts that need Orchestrator review before any stable-layer change

Subfolders:
- `canonical-update-proposals/`
- `durable-lesson-candidates/`
- `drivers-candidates/`
  - top-level index: `drivers-candidates/generated-index.md`
  - generated raw candidate notes: `drivers-candidates/candidate-notes/`
  - generated LLM family review outputs: `drivers-candidates/surfaced-family-review/`
    - top-level LLM family index: `drivers-candidates/surfaced-family-review/LLM-proposed-family-index.md`
    - markdown review notes: `drivers-candidates/surfaced-family-review/review-notes/`
    - input packets: `drivers-candidates/surfaced-family-review/inputs/`
- `linkage-repair-candidates/`

Use when:
- a researcher believes canon may need to change, but is not authorized to rewrite it directly
- a researcher identifies a potentially durable cross-case lesson that should be reviewed before promotion
- a researcher finds that no existing driver seems relevant enough and wants to propose a driver candidate
- a researcher spots graph/linkage issues worth fixing later in stable layers

Important:
- this folder is still part of `40-research/`
- items here are review artifacts, not canon
- researchers may write here as part of handoff and proposal workflow

See:
- `qualitative-db/40-research/review-queue/README.md`
- `qualitative-db/00-system/roles-protocols/researcher-operating-protocol.md`

---

# How 40-research interacts with 30-drivers and 50-retrospectives

`30-drivers/` stores reusable causal mechanisms.

`40-research/` stores case-specific evidence, reasoning, and updates.

`50-retrospectives/` stores after-the-fact evaluation of resolved cases, including missed signals, false signals, methodology changes, and performance review.

Use this distinction:
- if the note is about **how a mechanism usually works across many cases** -> `30-drivers/`
- if the note is about **how that mechanism appears in this case right now** -> `40-research/`
- if the note is about **what the resolved case taught us afterward** -> `50-retrospectives/`

Default workflow:
1. read relevant drivers first
2. collect source notes and other research outputs in `40-research/`
3. resolve the case and review outcomes in `50-retrospectives/`
4. let the decision-maker update `30-drivers/` only when a durable cross-case lesson emerges

---

# How the folders interplay

A good default research workflow looks like this:

1. **Read relevant drivers first**
   - identify which recurring forces are likely to matter
   - use `30-drivers/` to avoid shallow or purely headline-driven reasoning
   - researchers read driver/causal guidance, but do not write to `30-drivers/` during ordinary case work

2. **Collect source notes**
   - capture what sources actually said
   - preserve provenance and reliability judgments

3. **Write findings**
   - preserve different role-based or perspective-based interpretations when useful
   - avoid flattening disagreement too early

4. **Build evidence maps**
   - organize the strongest support, contradiction, and uncertainty around the exact claim or market question
   - make update logic explicit

5. **Write syntheses**
   - compress multiple notes into a reusable view for downstream forecasting or memory updates

6. **Hand off durable lesson candidates and conflict lessons to retrospectives and final review**
   - if a research pass suggests a durable lesson, make it explicit in `40-research/` and/or `50-retrospectives/`
   - if researchers conflicted, make the conflict type and strongest unresolved issue explicit before handoff
   - the decision-maker decides whether that lesson should update `30-drivers/`, `20-entities/`, or `10-domains/`

---

# Recommended behavior for future researchers

When researching:

- start by checking relevant driver files in `30-drivers/`
- inspect the current market price and treat it as an explicit object of analysis, not just background metadata
- ask whether your current view agrees or disagrees with the market-implied probability, and why
- write source notes when reading new material
- write findings when making a directional interpretation
- use evidence maps when a market question or claim needs explicit pro/con structure
- write a synthesis when enough material exists to distill
- make durable lesson candidates explicit, but do not directly update `30-drivers/` during ordinary research work

Avoid:
- writing raw source extracts into canon
- treating temporary product versions as stable entities
- skipping provenance
- collapsing disagreement too early
- burying assumptions inside final conclusions without writing them down separately
- putting case-specific observations into `30-drivers/`

---

# Fast mental model

- `20-entities/` = what is the thing?
- `30-drivers/` = what recurring force moves outcomes?
- `researcher-source-notes/` = what did the source say?
- `agent-findings/` = what does this research role think?
- `assumption-notes/` = what must be true for the view to hold?
- `evidence-maps/` = how does the evidence push the claim up or down?
- `product-notes/` = what changed in this specific release/version?
- `syntheses/` = what is the distilled take after reviewing many inputs?
- `50-retrospectives/` = what did the resolved case teach us?

If uncertain, preserve provenance first and canonize later.
