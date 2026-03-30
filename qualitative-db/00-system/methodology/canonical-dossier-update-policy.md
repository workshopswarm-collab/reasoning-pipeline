# Canonical Dossier Update Policy

## Purpose

Canonical dossiers in `qualitative-db/20-entities/` and major overview notes in `qualitative-db/10-domains/` are **slow-moving summaries**, not raw research logs.

They exist to preserve:
- durable understanding
- reusable object memory
- high-signal current state
- stable strengths / weaknesses / open questions

They should **not** be rewritten for routine news flow.

## Core rule

**Do not update a canonical dossier unless there is both:**
1. an **extremely material change**, and/or
2. an **explicit and repeated conflict of information** that forces the current canonical view to be revised.

If neither condition is met, new information belongs in the research layer, usually in:
- `qualitative-db/40-research/source-notes/`
- `qualitative-db/40-research/agent-findings/`
- `qualitative-db/40-research/evidence-maps/`
- `qualitative-db/40-research/product-notes/`
- `qualitative-db/40-research/review-queue/` when proposing a stable-layer change rather than applying it directly

## What counts as extremely material

Examples:
- leadership change at a major institution or team
- regulatory/legal change that alters market access or classification
- season-ending or structurally important injury to a key player
- war / ceasefire / sanctions shift that changes baseline geopolitical interpretation
- major product launch or platform change that alters competitive position
- capital-structure or treasury change that materially changes an entity's economic profile
- repeated evidence showing the entity's strengths/weaknesses are now mischaracterized

## What does NOT count as material enough on its own

Do not update canonical dossiers for:
- normal daily news flow
- one-off rumors
- single-source claims
- minor injuries or temporary absences unless strategically decisive
- transient sentiment shifts
- ordinary weekly performance variation
- a single article that merely adds color to an existing view

## Repeated conflict standard

A canonical dossier may be updated when the existing view is being contradicted by:
- multiple independent sources, and/or
- repeated agent findings across time, and/or
- new evidence that consistently invalidates a current canonical section

This is especially relevant when the current dossier's sections are no longer accurate in any of these areas:
- `Current state`
- `Key strengths`
- `Key weaknesses`
- `Important recent changes`
- `Open questions`

## Write discipline

### Default behavior

Researchers should write new information to the research layer, not directly to canonical dossiers.

### Canonical write authority

Canonical dossiers should normally be updated only by:
- orchestrator
- decision-maker
- a specifically designated canonical-memory maintainer

Researchers may surface update candidates through research notes or canonical entity update proposals, but should not directly amend stable layers during ordinary pipeline operation.

### Promotion threshold

New information should be promoted from research artifacts into a canonical dossier only if it is:
- durable enough to matter beyond one cycle
- high-confidence enough to survive re-reading later
- important enough to change future retrieval and downstream evaluation

## Required evidence before canonical update

Before updating a canonical dossier, confirm at least one of:
- multiple independent sources support the new view
- multiple agent artifacts converge on the same change
- the old canonical summary is now clearly misleading

## Preferred workflow

1. source note created
2. agent finding created
3. synthesis note decides whether conflict/materiality threshold is met
4. only then consider canonical dossier update
5. canonical update should reference upstream inputs

## Review metadata guidance

Canonical dossiers should carry these fields:
- `last_updated`
- `review_after`
- `freshness`

Recommended values:
- `freshness: current`
- `freshness: needs-review`
- `freshness: stale`

## Practical test

Before editing a dossier, ask:

- Is this change durable?
- Is it highly material?
- Is the current dossier now misleading if left unchanged?
- Do we have repeated or independent evidence?

If the answer is not clearly yes, do **not** update the dossier.

## One-line rule

**Research artifacts update often; canonical dossiers update rarely and only under strong evidentiary pressure.**
