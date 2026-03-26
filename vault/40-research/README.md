---
type: system_guide
domain: research
status: active
last_updated: 2026-03-25
owner: orchestrator
tags: [research/guide, vault/40-research, workflow]
---

# 40-research

This README is subordinate to `vault/00-system/README.md` and related 00-system policy files. If there is any conflict, follow `vault/00-system/`.

Fresh-instance shortcut:
1. read `vault/00-system/START-HERE.md`
2. read `vault/00-system/README.md`
3. read this file if you are doing case-specific work or adding new evidence

Terminology note:
- notes in `vault/40-research/` are research notes, not dossiers
- in vault policy language, a dossier means a canonical entity note in `vault/20-entities/`

This folder is the working research layer.

Use it for:
- time-indexed observations
- source extraction
- interim reasoning
- research outputs
- explicit assumptions
- evidence organization
- investigation tracking
- synthesis before canon updates

Do **not** use this folder for stable entity memory. Stable background context belongs in `vault/20-entities/` and stable domain framing belongs in `vault/10-domains/`.

Before starting case-specific work, check `vault/30-drivers/README.md` and any relevant driver files.

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
2. make the disagreement explicit in findings, evidence maps, syntheses, or investigations
3. let the decision-maker adjudicate the conflict
4. record resolved-case lessons in `vault/50-retrospectives/`
5. promote durable lessons into stable layers only after final review

---

# Folder guide

## `source-notes/`

Purpose:
- capture what a source said
- record extracted facts, direct claims, uncertainties, and source-quality notes
- preserve provenance for later review

Use when:
- reading an article, filing, transcript, data page, official source, benchmark page, standings page, company post, or policy document
- preserving what the source actually said before interpreting it

Subfolders:
- `by-source/` = notes organized around a specific source or outlet
- `by-domain/` = reusable source-framework notes useful across a domain
- `by-entity/` = source notes centered on one recurring entity

Good output:
- what the source directly states
- key extracted facts
- what remains uncertain
- reliability notes

Do not use for:
- final judgment
- broad synthesis
- long-run canon

## `agent-findings/`

Purpose:
- store parallel research outputs so later review can compare multiple independent takes on the same case
- preserve differences in framing, reasoning quality, source selection, and weighting across researcher personalities

Current role folders:
- `analyst/`
- `quant/`
- `scout/`
- `skeptic/`
- `synthesizer/`

Interpret these folders as working labels for recurring research personalities or styles, not as hard specialist job boundaries. The intended pattern is usually several researchers doing broadly the same analysis with different priors, temperaments, or reasoning styles.

Use when:
- multiple independent researchers are asked to analyze the same case from different personalities or priors
- you want to evaluate those distinct takes later against each other or against outcomes

Good output:
- explicit claim or conclusion
- rationale
- supporting notes referenced via `upstream_inputs`
- what this researcher weighted differently from another plausible take
- open questions and caveats

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

Examples:
- an election assumes polling error stays within normal bounds
- a product thesis assumes distribution matters more than benchmark quality
- a title market thesis assumes current health and rotations remain stable

Good output:
- explicit assumption
- why it matters
- what would falsify it
- what downstream notes depend on it

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

## `investigations/`

Purpose:
- track active research threads over time
- maintain a living case file for a question that requires multiple passes

Subfolders:
- `open/` = active work
- `paused/` = waiting on more evidence or deprioritized
- `closed/` = finished or resolved investigations

Use when:
- a question cannot be answered well in one note
- multiple source notes, evidence maps, and findings need coordination
- the thread should survive across sessions

Good output:
- current question
- why it matters
- current status
- linked source notes / evidence maps / findings
- next steps
- closure condition

## `product-notes/`

Purpose:
- track release-specific or version-specific product observations
- record dated notes on launches, model versions, product deltas, infrastructure releases, pricing changes, and user response

Use when:
- the object is too time-bound or version-specific for stable canon
- you want to compare what was expected at launch versus what happened later

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

## `syntheses/`

Purpose:
- combine multiple inputs into a higher-level view
- distill source notes, findings, investigations, and evidence maps into something reusable

Subfolders:
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

2. **Collect source notes**
   - capture what sources actually said
   - preserve provenance and reliability judgments

3. **Write findings**
   - preserve different role-based or perspective-based interpretations when useful
   - avoid flattening disagreement too early

4. **Build evidence maps**
   - organize the strongest support, contradiction, and uncertainty around the exact claim or market question
   - make update logic explicit

5. **Track longer threads in investigations**
   - if the question stays open across time, convert it into an investigation file

6. **Write syntheses**
   - compress multiple notes into a reusable view for downstream forecasting or memory updates

7. **Hand off durable lesson candidates and conflict lessons to retrospectives and final review**
   - if a research pass suggests a durable lesson, make it explicit in `40-research/` and/or `50-retrospectives/`
   - if researchers conflicted, make the conflict type and strongest unresolved issue explicit before handoff
   - the decision-maker decides whether that lesson should update `30-drivers/`, `20-entities/`, or `10-domains/`

---

# Recommended behavior for future researchers

When researching:

- start by checking relevant driver files in `30-drivers/`
- write source notes when reading new material
- write findings when making a directional interpretation
- use evidence maps when a market question or claim needs explicit pro/con structure
- open or update an investigation when the topic will persist across turns
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
- `source-notes/` = what did the source say?
- `agent-findings/` = what does this research role think?
- `assumption-notes/` = what must be true for the view to hold?
- `evidence-maps/` = how does the evidence push the claim up or down?
- `investigations/` = what are we actively tracking over time?
- `product-notes/` = what changed in this specific release/version?
- `syntheses/` = what is the distilled take after reviewing many inputs?
- `50-retrospectives/` = what did the resolved case teach us?

If uncertain, preserve provenance first and canonize later.
