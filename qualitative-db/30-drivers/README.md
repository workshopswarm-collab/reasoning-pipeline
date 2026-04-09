---
type: system_guide
domain: drivers
status: active
last_updated: 2026-03-25
owner: orchestrator
tags: [drivers/guide, qualitative-db/30-drivers, workflow]
---

# 30-drivers

This README is subordinate to `qualitative-db/00-system/README.md` and related 00-system policy files. If there is any conflict, follow `qualitative-db/00-system/`.

Fresh-instance shortcut:
1. read `qualitative-db/00-system/START-HERE.md`
2. read `qualitative-db/00-system/README.md`
3. read this file only if you are working in `30-drivers/` or using driver labels in research

This folder stores **reusable causal mechanisms**.

Use it to answer:
- what recurring force matters here?
- how does that force usually affect outcomes?
- what evidence normally shows it is active?
- how do researchers commonly misread it?

Examples:
- regulation
- polling
- macro
- product-launches
- media-narratives
- injuries-health
- conflicts
- seasonality
- leadership-changes

Driver notes may also carry an optional `aliases` field for high-confidence synonymous labels or obvious shorthand that should normalize to the same canonical driver.

## What this folder is for in the pipeline

`30-drivers/` is the causal layer between:
- `20-entities/` = what the objects are
- `40-research/` = what happened in this case
- `50-retrospectives/` = what was learned after the case resolved

Use `30-drivers/` to improve the pipeline in four ways:

1. **Scope the research quickly**
   - identify the likely causal forces before reading sources

2. **Standardize reasoning across researchers**
   - multiple researchers can use the same driver vocabulary instead of inventing new labels each time

3. **Improve retrieval and comparison**
   - notes linked to the same driver can be retrieved, compared, and reviewed together later

4. **Support retrospectives and quant review**
   - driver labels make it easier to analyze which recurring mechanisms were present in good or bad calls

## Authority rule

Researchers **read from** `30-drivers/`.

Researchers do **not** directly amend `30-drivers/` during ordinary case work.

The **decision-maker** is the normal writer to `30-drivers/`, and it should update driver files only when a durable lesson has survived case-specific research and retrospective review.

In practice:
- researchers write case-specific material into `40-research/`
- the decision-maker reviews completed research and retrospectives
- the decision-maker updates `30-drivers/` only when a lesson is generalizable across cases

## Core rule

`30-drivers/` is for **generalizable, durable causal guidance**.

`40-research/` is for **case-specific evidence, reasoning, updates, and judgments**.

`50-retrospectives/` is for **after-the-fact evaluation of what worked, what failed, and what should change**.

Rule of thumb:
- if it is about **how this mechanism usually works** -> `30-drivers/`
- if it is about **how this mechanism appears in this case right now** -> `40-research/`
- if it is about **what the resolved case taught us afterward** -> `50-retrospectives/`

## What belongs here

Write to `30-drivers/` only when the lesson is:
- **generalizable** across cases
- **durable** over time
- useful for future reasoning, retrieval, or retrospective evaluation

Good content:
- what the driver is
- why it matters
- where it tends to matter most
- what signals usually indicate it is active
- common failure modes
- common market misreads
- interactions with other drivers
- durable lessons promoted from repeated retrospective evidence

## What does NOT belong here

Do **not** put case-specific material here.

Keep these in `qualitative-db/40-research/` instead:
- one-off events
- source extracts
- market-specific updates
- dated observations
- temporary narratives
- specific forecast judgments
- investigation logs
- single-case conclusions that have not yet generalized

Keep these in `qualitative-db/50-retrospectives/` instead:
- postmortems of specific predictions or investigations
- agent-performance evaluations
- false-signal notes
- missed-signal notes
- source-performance reviews
- methodology adjustments tied to resolved outcomes

## Exact instructions for researchers

### Before research

1. Read `qualitative-db/30-drivers/README.md`.
2. Read any existing driver files that look relevant.
3. Choose the **2 to 5 most likely active drivers** for the case.
4. Use those drivers to guide source collection and evidence weighting.

### During research

When writing to `40-research/`:
- use `related_drivers` in frontmatter
- reference only the drivers that are actually active in the case
- prefer existing driver names over inventing new ones
- keep driver labels stable and simple
- use a canonical driver slug when you know it; if you only have a case-local phrase, record it as a proposed driver rather than pretending it is canonical
- if a new mechanism seems important, record it in the research note as a candidate driver, but do not create a new driver file directly

Examples:
- election market -> `related_drivers: [polling, leadership-changes]`
- crypto policy market -> `related_drivers: [regulation, sentiment]`
- sports title market -> `related_drivers: [injuries-health, seasonality]`

### During evidence mapping and synthesis

Use drivers to structure the work:
- which driver is doing the most causal work?
- which evidence activates that driver?
- which driver is being over- or underweighted by the market?
- which assumptions are really driver assumptions?

A strong evidence map should make it clear not just **what happened**, but **which drivers mattered and why**.

### After the research pass

Researchers should:
- keep the durable lesson candidate inside `40-research/` or `50-retrospectives/`
- make the lesson explicit enough that the decision-maker can decide whether to promote it into `30-drivers/`

Researchers should **not** directly rewrite `30-drivers/` during ordinary pipeline operation.

## Exact instructions for the decision-maker

The decision-maker should use `30-drivers/` as the place to store **promoted causal lessons**.

Update `30-drivers/` only after reviewing:
- the completed `40-research/` record
- the resolved outcome where available
- the relevant `50-retrospectives/` notes

A `30-drivers/` update is justified when the lesson is:
- durable
- cross-case
- likely to improve future research or weighting
- supported by more than one case or by one very strong retrospective lesson

Good promoted updates:
- a repeated market misread
- a durable weighting rule
- a recurring timing trap
- a reliable warning about false signals
- a clear interaction between two drivers that repeatedly matters

## Exact instructions for quant / retrospective use

Treat driver names as **stable categorical identifiers**.

Use them to:
- group notes by recurring mechanism
- compare outcomes across cases sharing the same driver
- evaluate which drivers were associated with forecast error or edge
- identify where researchers systematically overweighted or underweighted a mechanism
- review whether certain driver combinations produce better or worse calls

Important:
- drivers are **not** raw numeric features by themselves
- they are stable labels for organizing reasoning, evidence, and later analysis
- if a quant workflow later derives features from them, keep the driver names stable so downstream analysis remains consistent

## Naming rule

Prefer simple stable names.

Good:
- `regulation`
- `polling`
- `macro`
- `media-narratives`

Avoid:
- temporary case labels
- overly narrow event names
- duplicate synonyms for the same mechanism

If a new mechanism is only relevant to one case so far, keep it in `40-research/` or `50-retrospectives/` first and promote it to `30-drivers/` only after durable retrospective value is clear.

## Structure rule

Keep `30-drivers/` lean.

Default structure:
- use **flat driver files** directly under `qualitative-db/30-drivers/`
- do **not** create folders or `00-overview.md` files by default

Create a driver folder and `00-overview.md` only in retrospect, after enough analysis shows a real need.

A folder is justified only when most of these are true:
- there are already **3+ distinct child drivers** that clearly belong together
- the parent concept is too broad for one file
- the grouping improves retrieval or navigation
- future work is likely to keep using both the parent and child levels

Do **not** create:
- empty driver folders
- folders with only `00-overview.md`
- speculative scaffolding for topics that do not yet have real child files

## Tagging standard

Each driver file should use tags to improve retrieval, but keep them sparse and consistent.

Default tagging rule:
- include **one driver tag**: `driver/<name>`
- include the **main domain tags** where the driver regularly applies: `domain/<name>`
- avoid large tag lists or speculative tags

Good target:
- 1 driver tag
- 2 to 5 domain tags
- optionally 0 to 2 extra tags only if they materially improve retrieval

## Recommended workflow

1. Researchers read relevant drivers first
2. Researchers collect source notes and produce case work in `40-research/`
3. Resolved cases and evaluation lessons are written into `50-retrospectives/`
4. The decision-maker promotes durable causal lessons into `30-drivers/`

## Fast mental model

- `20-entities/` = what is the thing?
- `30-drivers/` = what recurring force moves outcomes?
- `40-research/` = what happened in this case?
- `50-retrospectives/` = what did the resolved case teach us?

## Template

When creating or substantially rewriting a driver note, use:
- `qualitative-db/00-system/templates/driver-overview-template.md`

## Writing standard

Prefer concise, reusable guidance over long event histories.

A strong driver note should help future researchers:
- reason faster
- avoid repeated mistakes
- identify high-value evidence
- separate structural signal from temporary noise
- compare similar cases later using stable driver labels
