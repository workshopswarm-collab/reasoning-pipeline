---
# decision header

type: syndicated_finding
case_key:
dispatch_id:
question:
coverage_status:
market_implied_probability:
syndicated_probability_low:
syndicated_probability_high:
syndicated_probability_midpoint:
edge_vs_market_pct_points:
relation_to_market:
edge_quality:
edge_independent_verification_quality:
compressed_toward_market_due_to_verification:
disagreement_intensity:
synthesis_confidence_quality:
staleness_risk:
next_checkpoint:
follow_up_needed:
---

# Claim

State the single consolidated finding for this dispatch in plain language.

This is the primary synthesis artifact in the current `roles/orchestrator/synthesis-subagent/` pipeline.
A downstream `decision-handoff.md` may be derived from it for the decision-maker, but this syndicated finding remains the main authored synthesis surface.

This is a synthesis artifact, not a new research lane.
Use persona findings under `researcher-analyses/<YYYY-MM-DD>/<dispatch-id>/personas/` as the canonical primary inputs.
Use sibling assumption/evidence artifacts only when they materially clarify provenance, assumptions, or disagreement.
Do not claim independent primary research unless the synthesis run explicitly did so.

## Frontmatter rules

Keep frontmatter limited to the decision header above.

### Runtime-populated frontmatter

- `type`
- `case_key`
- `dispatch_id`
- `question`
- `market_implied_probability`

### Synthesizer-authored frontmatter

- `coverage_status` = `complete | partial`
- `syndicated_probability_low`
- `syndicated_probability_high`
- `edge_independent_verification_quality` = `low | medium | high`
- `compressed_toward_market_due_to_verification` = `yes | no`
- `disagreement_intensity` = `low | medium | high`
- `synthesis_confidence_quality` = `low | medium | high`
- `staleness_risk` = `low | medium | high`
- `next_checkpoint`
- `follow_up_needed` = `yes | no`

### Runtime-derived frontmatter

- `syndicated_probability_midpoint`
- `edge_vs_market_pct_points`
- `relation_to_market` = `above_market | below_market | roughly_agree | crosses_market | unclear`
- `edge_quality` = `unclear | weak | moderate | strong`

### Authoring rules

- Fill only synthesizer-authored frontmatter fields and the body sections below.
- Use decimal probabilities in `[0, 1]`.
- Do not hand-calculate midpoint, edge, relation-to-market, or edge-quality fields.
- Use enum values exactly as written.

## External runtime metadata

Keep these out of frontmatter and persist them in a JSON sidecar.

Filename convention:
- for a dispatch-scoped artifact `.../syndicated-finding.md`, use `.../syndicated-finding.runtime.json`
- for the canonical case-level artifact `.../synthesizer-agent/syndicated-finding.md`, use `.../synthesizer-agent/syndicated-finding.runtime.json`

Use `syndicated-finding-runtime-metadata-template.json` as the schema/template reference.

Preferred sidecar fields:
- `artifact_type`
- `artifact_path`
- `case_key`
- `dispatch_id`
- `question`
- `generated_by`
- `synthesis_method`
- `synthesis_status`
- `market_snapshot_time`
- `source_personas`
- `missing_personas`
- `source_finding_paths`
- `source_supporting_artifacts`
- `source_persona_count`
- `missing_persona_count`
- `supporting_artifact_count`
- `upstream_inputs`
- `downstream_uses`

Do not put `tags` in the sidecar for this artifact in V1.

## Runtime derivation rules

Use these exact rules for V1.

### Validation

Runtime must validate:
- `market_implied_probability`
- `syndicated_probability_low`
- `syndicated_probability_high`

Canonical stored probability fields must be decimal probabilities in `[0, 1]`.
If any required probability is missing, unparsable, outside `[0, 1]`, or if `syndicated_probability_low > syndicated_probability_high`, then:
- leave derived numeric fields blank
- set `relation_to_market = unclear`
- set `edge_quality = unclear`

### Derived frontmatter fields

Runtime computes:
- `syndicated_probability_midpoint = round((syndicated_probability_low + syndicated_probability_high) / 2, 4)`
- `edge_vs_market_pct_points = round((syndicated_probability_midpoint - market_implied_probability) * 100, 1)`

Store `edge_vs_market_pct_points` as percentage points, not a decimal probability.
Example: market `0.61`, midpoint `0.68` -> `+7.0`

### `relation_to_market`

Runtime computes in this order:
1. if probability validation failed -> `unclear`
2. else if `syndicated_probability_low <= market_implied_probability <= syndicated_probability_high` -> `crosses_market`
3. else if `abs(edge_vs_market_pct_points) < 3.0` -> `roughly_agree`
4. else if `syndicated_probability_midpoint > market_implied_probability` -> `above_market`
5. else if `syndicated_probability_midpoint < market_implied_probability` -> `below_market`
6. else -> `roughly_agree`

### `edge_quality`

Runtime computes in this order:
1. if probability validation failed -> `unclear`
2. else if `relation_to_market` is `crosses_market` or `unclear` -> `unclear`
3. else if `abs(edge_vs_market_pct_points) < 3.0` -> `weak`
4. else if `abs(edge_vs_market_pct_points) < 7.0` -> `moderate`
5. else -> `strong`

These thresholds are absolute edge thresholds in percentage points.

## Alpha summary

State briefly:
- market-implied probability
- syndicated probability range
- whether the edge appears actionable, marginal, or unclear
- the main reason the market may be mispriced

If the range is wide or the edge is fragile, say so explicitly.

## Input coverage

State briefly:
- which persona findings were available
- which personas were missing, thin, or unusable
- whether supporting assumption/evidence artifacts were used
- why coverage should be treated as `complete` or `partial`

## Market-implied baseline

State the baseline being synthesized against.
If it moved materially during the swarm run, note that briefly.

## Syndicated probability estimate

State the synthesizer's own final probability range clearly.
This range should reflect the synthesizer's post-synthesis judgment after reviewing the raw lane findings, critically evaluating the extracts, and doing any synthesis-stage truth-finding research.
Use the swarm's probability outputs broadly as a baseline prior, but do not merely restate, average, or mechanically median the lane probabilities.
Prefer a bounded range over a false single-point estimate when lanes disagree materially.

## Difference from swarm-implied center

State how your final probability range relates to the swarm-implied center or baseline probability view.
If your final view is materially different from that swarm-implied center, explain why.
Useful reasons may include:
- independent verification weakened or strengthened the apparent edge
- one or more lanes looked weak, stale, overconfident, or underweighted
- additional synthesis-stage truth-finding changed the evidence balance
- skepticism about a large implied edge caused compression back toward the market

If there is no meaningful difference, say so explicitly.

## Agreement or disagreement with market

Explain whether the synthesis roughly agrees with, exceeds, or falls below the market-implied view, and why.

## Independent verification of edge

State how well the final edge versus market was independently verified during the synthesis-stage truth-finding pass.
Be explicit about:
- what was independently checked
- how strong that verification was
- what remained unverified or weak
- why the final verification quality should be considered `low`, `medium`, or `high`

## Compression toward market due to verification

State whether the final synthesis compressed toward the market view because the apparent swarm edge could not be independently verified strongly enough.
If yes, say:
- what part of the swarm edge was treated skeptically
- what verification was missing or weak
- how that changed the final probability range

If no, say why the synthesis judged the edge sufficiently verified to avoid meaningful compression.

## Timing and catalyst posture

State briefly:
- the next catalyst or resolution checkpoint that matters most
- whether the edge is more likely to widen, compress, or decay before then
- whether waiting is more likely to improve or worsen the decision

## Decision blockers

State what still prevents a high-confidence downstream decision, if anything.
Examples:
- unresolved contract ambiguity
- thin or non-independent sourcing
- unresolved factual disagreement
- timing uncertainty
- no real edge after synthesis

If there are no meaningful blockers, say so.

## Implication for the question

State what this synthesis implies for the actual market question or operational interpretation.

## Consensus across personas

List the main points that multiple lanes converged on.
Focus on causal or decision-relevant agreement, not cosmetic overlap.

## Key disagreements across personas

State the most important disagreements.
For each one, identify the main type:
- factual
- interpretive
- weighting-based
- timing-based
- assumption-based
- source-of-truth / contract-based

Do not flatten away real disagreement just to make the synthesis feel cleaner.

## Best countercase

State the strongest minority or dissenting interpretation preserved across the swarm.
Name which persona(s) best represented it.
If there was no meaningful minority view, say so.

## Encapsulated assumptions

Consolidate the key assumptions from the lane findings.
If useful, separate them into:
- shared assumptions
- contested assumptions
- fragile assumptions

## Encapsulated evidence map

Net the evidence into one section.
If useful, organize it into:
- strongest supporting evidence
- strongest contradictory evidence
- authoritative / governing source-of-truth evidence
- ambiguous or mixed evidence

Prefer concise synthesis over repeating lane memos.

## Evidence weighting

State briefly:
- what evidence carried the most weight
- what evidence was downweighted
- what was ignored and why

## Counterpoints / strongest disconfirming evidence

State the strongest evidence or mechanism against the current syndicated view.
This should be the real best disconfirming case, not a token caveat.

## Resolution or source-of-truth interpretation

Use this section when contract wording, exclusions, timing, attribution, or source-of-truth rules materially affect the answer.
If lanes disagreed about what counts, make the synthesis position explicit and auditable here.

## Why this could create or destroy alpha

Explain why the synthesized view matters for downstream forecasting, review, or decision support.
Address, where possible:
- what may be mispriced
- why the market may be wrong
- why the signal may already be priced in

## What would falsify this interpretation / change the view

State what future observation, verification, or disconfirming evidence would most change the syndicated view.
If specific timing or resolution events matter, name them.

## Highest-value next research

State the single next check, source, or verification step most likely to move the syndicated estimate materially.
If none, say none.

## Source-quality assessment

State briefly:
- the primary or governing source class most relied on across the swarm
- the most important contextual or secondary source class
- whether evidence independence looked low / medium / high
- whether source-of-truth ambiguity looked low / medium / high
- whether the synthesis is bottlenecked by thin upstream sourcing from one or more lanes

## Verification impact

State briefly:
- whether any additional verification beyond the persona findings was used by the synthesis layer
- whether cross-lane comparison materially changed the apparent confidence or mechanism view
- whether the synthesis exposed any lane-level inconsistency or provenance weakness

If no extra verification was performed, say so explicitly.

## Persona contribution map

List what each persona contributed that mattered most.
Make provenance legible enough that a later reviewer can trace major claims back to the lane findings.

Suggested format:
- `base-rate` — ...
- `market-implied` — ...
- `variant-view` — ...
- `risk-manager` — ...
- `catalyst-hunter` — ...

## Reusable lesson signals

State briefly:
- possible durable lesson, if any
- possible missing or underbuilt driver, if any
- possible source-quality lesson, if any
- confidence that any lesson here is reusable: low / medium / high

## Orchestrator review suggestions

State briefly:
- review later for durable lesson: yes / no
- review later for driver candidate: yes / no
- review later for canon or linkage issue: yes / no
- review later for swarm-method issue: yes / no
- one-sentence reason

## Recommended follow-up

State what should happen next, if anything:
- no follow-up needed
- rerun one or more research lanes
- request decision-maker review
- collect missing source provenance
- investigate a specific disagreement
- wait for a catalyst or resolution checkpoint
