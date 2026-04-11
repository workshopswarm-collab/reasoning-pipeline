# Decision-Maker

This folder is the architecture and implementation home for the **Decision-Maker** stage of the prediction-market pipeline.

## Canonical status

This Orchestrator repo is the **canonical workspace** for the Decision-Maker pipeline stage.

Reason:
- Decision-Maker is not a standalone side project; it is a downstream stage in the live pipeline
- its canonical inputs are produced by Orchestrator synthesis
- its canonical outputs are consumed by downstream execution / accounting / evaluator layers that belong to the pipeline architecture
- keeping the stage contract in Orchestrator reduces drift between doctrine, file paths, runtime behavior, and execution-facing artifacts

The separate `~/.openclaw/decision-maker` workspace is the real OpenClaw agent home for the `decision-maker` agent. It owns persona, continuity, and sessions. This Orchestrator repo remains the source of truth for live pipeline architecture, contracts, prompts, runtime scripts, and case-artifact conventions.

## Purpose

Decision-Maker is the pipeline's **final judgment layer**.

Its job is not to repeat synthesis or produce another attractive memo.
Its job is to decide whether the synthesized edge is:
- real enough
- verified enough
- large enough
- clean enough
- actionable enough

for the pipeline to authorize action.

The Decision-Maker should optimize for:
- long-run prediction-market profit
- predictive accuracy
- calibration
- risk discipline
- execution usefulness
- auditability

It must be fully allowed to conclude:
- no trade
- watch only
- reduce only
- not decision ready
- price not good enough
- risk constraint binding

Those are successful outputs when they improve expected value.

## Runtime ownership split

Keep this split explicit:

- `~/.openclaw/orchestrator/roles/decision-maker` = canonical implementation surface
- `~/.openclaw/orchestrator/qualitative-db/...` = canonical pipeline artifacts
- `~/.openclaw/decision-maker` = separate OpenClaw agent workspace, persona, continuity, and session home

Operationally, Orchestrator should hand off decision work to the separate `decision-maker` agent after synthesis completes. The current runtime model is:
- Orchestrator-hosted runtime builds the decision context and prompt
- Orchestrator-hosted runtime bootstraps a dedicated Telegram decision lane
- the runtime posts visible stage markers (`SYNTHESIS RECEIVED`, `DECISION-MAKING ANALYSIS UNDERWAY`, `DECISION-MAKING COMPLETED, DECISION PACKAGE CREATED`)
- the separate `decision-maker` agent provides the actual judgment by returning the decision packet JSON
- in `targeted_escalation`, the agent may perform bounded independent search/fetch work itself rather than relying on a runtime-selected source list
- Orchestrator-hosted runtime performs deterministic validation, transcript-budget auditing, rendering, and status persistence against canonical case paths

The Decision-Maker agent should operate against the canonical Orchestrator paths rather than creating a parallel implementation tree in its own workspace.

## Stage position in the pipeline

Current pipeline shape:

1. market/case selection
2. researcher swarm
3. synthesis
4. decision-maker
5. isolated execution / accounting
6. evaluator / retrospectives

Canonical upstream synthesis outputs today:
- `qualitative-db/40-research/cases/<case-key>/synthesizer-agent/syndicated-finding.md`
- `qualitative-db/40-research/cases/<case-key>/synthesizer-agent/syndicated-finding.runtime.json`
- `qualitative-db/40-research/cases/<case-key>/synthesizer-agent/decision-handoff.md`

Canonical Decision-Maker outputs should become:
- `qualitative-db/40-research/cases/<case-key>/decision-maker/decision-maker-packet.md`
- `qualitative-db/40-research/cases/<case-key>/decision-maker/artifacts/decision-maker-packet.json` (optional but preferred when execution consumes structured output)

## What Decision-Maker is for

Decision-Maker exists to perform the last economically meaningful compression before execution.

It should:
- consume synthesis and researcher context as guidance without treating either as infallible or determinative
- critically evaluate upstream material rather than merely ratify it
- respect market baselines and base rates
- compress weak or poorly verified apparent edges back toward market when warranted
- decide whether the case is actually ready for action
- use bounded independent source search during `targeted_escalation` when the crux justifies it, while remaining inside runtime-enforced budgets
- convert fair value judgment into deterministic execution-facing thresholds
- make pass / wait / no-trade outcomes first-class
- provide a clean artifact for later evaluator scoring and postmortem review

## What Decision-Maker is not for

Decision-Maker should not become:
- a duplicate synthesis worker
- a long-form narrative vanity stage
- a pressure mechanism that converts internal effort into forced action
- a consensus worship layer
- a direct execution surface

Internal agreement is evidence, not authority.
Synthesis and researcher outputs are guidance, not verdicts.
Narrative elegance is not edge.
A high-effort swarm can still correctly end in `flat` or `watch_only`.

## Core doctrine

Decision-Maker should inherit these operating rules:
- prioritize predictive accuracy over elegance
- optimize for long-run market performance, not narrative satisfaction
- separate signal from story
- respect market baseline and base rates
- require stronger proof for larger claimed edges
- prefer deterministic computation over hand-wavy arithmetic
- make the decisive crux explicit
- preserve auditability
- do not distort outputs to justify action or justify the pipeline

## Canonical inputs

Decision-Maker should support three input classes.

### 1. Required upstream qualitative inputs

Required:
- `decision-handoff.md`

Strongly preferred:
- `syndicated-finding.runtime.json`
- `syndicated-finding.md`

Why:
- `decision-handoff.md` gives the direct synthesis-to-decision bridge
- `syndicated-finding.runtime.json` carries deterministic synthesis-side fields like edge and market relation in structured form
- `syndicated-finding.md` preserves the full authored synthesis rationale for audit and selective reread

### 2. Required market context inputs

Decision-Maker should read enough market state to ground actionability.
Minimum required market context:
- market id
- question / title
- current actionable reference price
- quote timestamp / staleness
- resolution horizon if relevant

Preferred market context:
- current order-book or executable quote summary
- liquidity / depth snapshot
- recent market movement summary
- contract-specific structural constraints

### 3. Portfolio / execution-context inputs

Portfolio-aware judgment is currently out of scope for Decision-Maker.

Risk management and execution-context handling are currently expected to happen off-pipeline on the other device, so the present Decision-Maker stage should not depend on portfolio inputs to choose its verification mode or form its market judgment.

If portfolio-aware execution constraints are reintroduced later, they should be added back explicitly rather than inferred from missing placeholder fields.

## Canonical outputs

### Human-auditable packet

Required canonical path:
- `decision-maker/decision-maker-packet.md`

Purpose:
- primary operator-facing recommendation artifact
- audit and retrospective surface
- plain-language statement of the action or no-action call

### Machine-readable packet

Optional but preferred canonical path:
- `decision-maker/artifacts/decision-maker-packet.json`

Purpose:
- structured downstream contract for isolated execution / monitoring logic
- deterministic validation against the JSON schema
- evaluator-friendly extraction of decision-state fields

Canonical schema/template surfaces already exist in:
- `qualitative-db/00-system/templates/decision-packet-template.md`
- `qualitative-db/00-system/templates/decision-packet.schema.json`

## Decision output classes

Decision-Maker must be able to produce all of the following classes of output.

### 1. Authorized action
Use when:
- edge is present
- edge is sufficiently verified
- market price is good enough
- risk constraints allow action
- packet is execution-ready

Representative settings:
- `trade_authorization = authorized`
- `position_policy = enter_or_add | hold_only | reduce_only | exit_only`
- `decision_readiness = ready`

### 2. Watch / passive state
Use when:
- thesis may be directionally right
- but price is not attractive enough
- or quote freshness/liquidity is inadequate
- or verification is too weak for autonomous action

Representative settings:
- `trade_authorization = watch_only`
- readiness may still be `ready` or may indicate a blocking context gap

### 3. Risk reduction only
Use when:
- current exposure is too large
- confidence has weakened
- invalidation is developing
- the right move is to shrink or exit, not add

Representative settings:
- `trade_authorization = risk_reduce_only`
- `position_policy = reduce_only | exit_only`

### 4. Forbidden / flat
Use when:
- no actionable edge exists
- edge is too weak after skepticism / compression
- the case is not ready
- the market/portfolio context is too incomplete
- risk constraints prohibit action

Representative settings:
- `trade_authorization = forbidden`
- `position_policy = flat`

## Canonical decision questions

Every Decision-Maker evaluation should answer these questions explicitly:

1. What is my actual fair-value range?
2. What is the current actionable market reference price?
3. Is the edge versus market large enough to matter after costs, liquidity, and risk?
4. How independently verified is that edge?
5. Should the apparent edge be compressed back toward market?
6. Is this case decision-ready?
7. What is the decisive crux carrying the action or no-action call?
8. What deterministic execution bands should downstream systems use?
9. What would invalidate the packet?
10. What should the evaluator later judge most harshly?

## Verification policy

Decision-Maker should use **bounded, escalation-based verification**.

Interpretation:
- Decision-Maker is important enough to do more than blindly trust synthesis
- but not so unconstrained that it routinely reruns synthesis in disguise

Default policy:
- start from synthesis as the upstream compression
- perform a bounded internal audit of only the most decision-relevant upstream artifacts
- escalate to a small number of targeted external or freshness checks only when the crux justifies it
- if responsible verification would require a broader new research pass, prefer `needs_more_research`, `watch_only`, `forbidden`, or other fail-closed outputs rather than pretending bounded verification was enough

Programmatic enforcement now exists at the planner/runtime layer:
- `planner/scripts/decide_verification_mode.py` deterministically chooses the verification mode
- `planner/scripts/select_decision_inputs.py` deterministically selects the compact evidence bundle under a hard size budget
- `planner/scripts/build_decision_prompt.py` builds the Decision-Maker prompt from that compact bundle rather than from the whole case tree

Canonical policy reference:
- `roles/decision-maker/verification-policy.md`

## Relation to synthesis

Decision-Maker is downstream of synthesis, but not subordinate in a purely ceremonial sense.

Decision-Maker should:
- treat synthesis as the best current upstream compression
- not blindly rubber-stamp it
- usually begin from the synthesis baseline
- preserve explicit skepticism when apparent edge versus market is large
- not reopen the entire swarm unless the case is explicitly routed back for more research

Rule of thumb:
- synthesis answers: "what seems true after compressing the swarm and bounded truth-finding?"
- Decision-Maker answers: "given what seems true, the current price, and the current constraints, what should we do?"

## Relation to execution

Decision-Maker is the last reasoning layer before isolated execution.

It must therefore transform qualitative judgment into deterministic execution semantics.
That means:
- define bands on the canonical `market_implied_true_prob` axis
- define target exposure fractions
- define quote freshness rules
- define rebalancing thresholds
- define whether reversal is allowed
- define expiry / valid-until boundaries
- define portfolio and liquidity constraints

Execution should not need to reinterpret vague prose.

## Deterministic-vs-model split

### Model-authored responsibilities
The model may author:
- fair-value range
- primary crux and secondary cruxes
- reasons to act / pass
- invalidation logic
- key uncertainties
- rationale for compression toward market
- evaluator notes

### Deterministic responsibilities
Code should compute or validate:
- fair-value midpoint from low/high if that is the chosen policy
- edge versus market in percentage points
- band continuity over `[0,1]`
- no-gap / no-overlap constraints
- monotonic exposure-shape checks
- packet schema compliance
- path conventions
- timestamp validity / expiry sanity
- consistency constraints between authorization and policy

Principle:
if a field should be reproducible and checkable, prefer code.

## Packet generation flow

Recommended minimal flow:

1. locate case-level synthesis artifacts
2. load `decision-handoff.md`
3. load `syndicated-finding.runtime.json` when present
4. load current market context
5. load current portfolio context when available
6. load the bounded verification policy / budget for the run
7. ask Decision-Maker for the judgment layer only
8. validate / normalize deterministic fields in code
9. render `decision-maker-packet.md`
10. optionally emit JSON packet
11. fail closed if the packet is internally inconsistent or required context is missing

## Failure / not-ready rules

Decision-Maker should fail closed rather than manufacture action.

Representative not-ready reasons:
- missing synthesis handoff
- stale or missing market quote
- unresolved contract ambiguity
- invalid or inconsistent action bands
- strong edge claim with low verification and no compression justification

In those cases the system should prefer:
- `needs_more_research`
- `needs_market_update`
- `watch_only`
- `forbidden`

## Suggested folder shape

Recommended shape for this stage inside the repo:

- `roles/decision-maker/README.md` — this architecture/spec
- `roles/decision-maker/planner/` — input bundle construction if needed
- `roles/decision-maker/runtime/` — packet generation, validation, rendering, persistence
- `roles/decision-maker/planner/prompts/` — final judgment contracts/prompts

Initial likely scripts:
- `runtime/scripts/build_decision_context.py`
- `runtime/scripts/run_decision_maker.py`
- `runtime/scripts/validate_decision_packet.py`
- `runtime/scripts/render_decision_packet.py`

## Minimal v1 implementation target

A strong first implementation should do only a few things, but do them well:

1. consume the case-level synthesis outputs
2. consume a minimal market snapshot / reference price input
3. optionally consume minimal portfolio context
4. generate a validated decision packet
5. allow `authorized`, `watch_only`, `risk_reduce_only`, and `forbidden`
6. make no-trade and not-ready outputs fully first-class

This is preferable to prematurely building a large autonomous subsystem.

## Evaluation relevance

Decision-Maker packets should be written so the evaluator can later ask:
- was fair value wrong?
- was the edge too small after costs/risk?
- was skepticism insufficient or excessive?
- was the packet compressed toward market appropriately?
- were invalidation conditions good?
- was the no-trade call correct even if the market later moved?
- was sizing / band structure appropriate?

That means packets should preserve:
- decisive crux
- key uncertainties
- reasons to pass or stay small
- what would change the mind
- explicit evaluator notes

## Canonical implementation philosophy

Build Decision-Maker as a **thin, disciplined, economically useful** stage.

Prefer:
- explicit judgment
- deterministic validation
- first-class no-trade outcomes
- skeptical treatment of large internal-vs-market edges
- execution-ready outputs

Avoid:
- another broad synthesis pass
- verbose memo generation for its own sake
- architecture that rewards activity over expected value
