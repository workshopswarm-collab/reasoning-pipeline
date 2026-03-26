---
type: system_guide
domain: retrospectives
status: active
last_updated: 2026-03-25
owner: orchestrator
tags: [retrospectives/guide, vault/50-retrospectives, workflow]
---

# 50-retrospectives

This README is subordinate to `vault/00-system/README.md` and related 00-system policy files. If there is any conflict, follow `vault/00-system/`.

Fresh-instance shortcut:
1. read `vault/00-system/START-HERE.md`
2. read `vault/00-system/README.md`
3. read this file only if you are reviewing resolved cases or writing retrospective lessons

This folder stores **after-the-fact evaluation**.

Use it to answer:
- what turned out to matter?
- what misled the pipeline?
- which sources or signals were useful or harmful?
- how should future research, weighting, or driver guidance change?

## What belongs here

Use `50-retrospectives/` for:
- agent-performance review
- false-signal review
- missed-signal review
- input-quality review
- source-performance review
- methodology adjustments after resolved cases
- conflict-resolution lessons after disagreements are adjudicated

## Role rule

Researchers may read this folder, but ordinary researchers should not treat it as their main working layer.

The decision-maker and orchestrator are the normal writers here.

## Conflict-resolution role in the pipeline

When researchers disagree on facts, interpretation, weighting, or assumptions:
- preserve the disagreement in `40-research/`
- let the decision-maker adjudicate the case
- write the retrospective lesson here after the outcome is known or the disagreement is resolved well enough to evaluate

Good retrospective questions:
- was this a source conflict, interpretation conflict, weighting conflict, timing conflict, or assumption conflict?
- which side had better evidence?
- which side had better causal logic?
- was one side right on direction but wrong on magnitude?
- did the disagreement reveal a reusable lesson for `30-drivers/` or methodology?

## Relationship to 30-drivers

`30-drivers/` stores durable promoted causal lessons.

`50-retrospectives/` stores the resolved-case review that may justify those promotions.

Default rule:
- keep the case-specific disagreement and evaluation here
- promote only durable cross-case lessons into `30-drivers/`
