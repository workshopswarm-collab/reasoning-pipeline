# Decision-Maker bounded verification policy

This document defines how the Decision-Maker stage should perform additional verification while staying aligned with the pipeline's objective:

- maximize predictive accuracy for prediction markets
- preserve calibration and decision quality
- spend additional verification budget when it plausibly improves expected value
- avoid collapsing Decision-Maker into a routine second synthesis pass

## Core principle

Decision-Maker is the most important judgment layer, but that does **not** imply unlimited rereading or open-ended re-research on every case.

A good Decision-Maker should be:
- more skeptical than synthesis
- more economically disciplined than synthesis
- selectively more verifying than synthesis when the crux justifies it
- willing to say `watch_only`, `forbidden`, or `needs_more_research` instead of pretending bounded verification was sufficient

The policy goal is:

> spend verification effort where the expected improvement in decision quality is plausibly high, and fail closed where it is not.

## Verification hierarchy

Decision-Maker should work through verification in layers.

### Layer 0 — consume synthesis as the starting compression
Always read:
- `decision-handoff.md`
- `syndicated-finding.runtime.json` when present
- `syndicated-finding.md` when materially useful

Default assumption:
- synthesis is the best upstream compression available
- it is not infallible
- Decision-Maker begins from synthesis but is not required to rubber-stamp it

### Layer 1 — bounded internal audit
Default Decision-Maker behavior should include a bounded internal audit.

Allowed work by default:
- reread the decisive synthesis handoff sections
- reread a small number of upstream research artifacts tied to the crux
- check whether the synthesis confidence seems too high, too low, or internally inconsistent
- reread the strongest countercase lane when the synthesis edge is meaningful

This is the default mode for most cases.

### Layer 2 — targeted external verification
Escalate to targeted source review only when the likely EV gain justifies it.

Allowed work in this mode:
- use bounded `web_search` / `web_fetch` to find and review decisive external sources independently
- resolve a narrow contract or source ambiguity
- check live market/quote/tracker or underlying-platform surfaces when the crux depends on freshness
- choose sources based on quality and diversity rather than only reusing links surfaced upstream

This mode should be used often enough to improve important decisions, but not so often that Decision-Maker becomes a general-purpose duplicate researcher.

### Layer 3 — bounded re-open / major escalation
Use only for high-value or high-risk cases when the current package is not sufficient for a responsible decision.

Examples:
- contract ambiguity that materially changes resolution semantics
- a large claimed edge with low independent verification
- unusually large size / exposure / correlation implications
- major disagreement between synthesis and market that could be real or could be artifact-driven
- stale or broken upstream package on a live-sensitive case

In this mode, Decision-Maker should still remain bounded and explicit.
If the case effectively requires another research pass, the correct output is often:
- `needs_more_research`
- `needs_market_update`
- `watch_only`

rather than performing unlimited ad hoc research inside Decision-Maker.

## Default verification budget

The default policy should assume a **bounded internal audit + optional targeted check**, not full reread.

### Default artifact budget
Without escalation, Decision-Maker may review at most:
- required synthesis handoff artifacts: always
- 2 persona findings
- 1 assumption artifact
- 1 evidence artifact
- 1 countercase artifact or supporting note bundle

Interpretation:
- prefer the most decision-relevant artifacts, not broad coverage
- if the case's decisive crux is narrow, the budget should remain narrow

### Default external-source budget
Without explicit escalation, Decision-Maker should review at most:
- 0 search queries
- 0 fetched external sources

In `targeted_escalation`, runtime computes a bounded search/fetch budget from uncertainty instead of using a one-size-fits-all fixed count.

### Default iterative budget
Without escalation, avoid multi-round exploratory loops.
Prefer:
- one pass of bounded reread
- one pass of targeted checking if needed
- then decide or fail closed

## Escalation triggers

Escalation above the default bounded audit is justified when one or more of the following are true.

### 1. Large apparent edge versus market
Examples:
- synthesis fair value materially differs from market
- the packet would authorize meaningful action against market consensus

Rule:
- the larger the claimed edge, the stronger the required verification
- large edge + weak verification should usually mean compression, smaller size, or no-trade

### 2. Source-of-truth or contract ambiguity
Examples:
- narrow resolution semantics
- ambiguous venue rules
- tracker/classification dependence
- timing-window mapping risk

Rule:
- Decision-Maker should spend verification effort resolving the contract mechanics before spending effort on broad narrative reread

### 3. Freshness-sensitive catalysts
Examples:
- near-close event
- live count threshold
- tracker updates
- fast-moving catalyst or liquidity changes

Rule:
- prefer one high-value freshness check over rereading many stale notes

### 4. Internal inconsistency in the package
Examples:
- synthesis rationale and confidence do not match
- handoff signals conflict with packet implication
- sidecar evidence strongly disagrees with synthesis conclusion

Rule:
- use bounded reread to resolve the inconsistency
- if unresolved, emit `needs_more_research` or a non-action outcome

## When not to escalate

Do **not** escalate just because:
- the pipeline spent many tokens upstream
- the research tree is large and tempting to reread
- there are many available notes
- the stage wants to justify its own importance
- a decision feels emotionally significant without strong economic consequence

Decision-Maker should remain willing to say:
- `edge_too_small`
- `price_not_good_enough`
- `needs_market_update`
- `watch_only`
- `forbidden`

## Decision-Maker verification modes

### Mode A — synthesis-trusting bounded audit
Use when:
- edge is small/moderate
- synthesis verification is not obviously weak
- no major contract ambiguity is present
- action consequences are ordinary

Target behavior:
- consume synthesis
- reread only the most decisive 2-4 upstream artifacts
- decide or fail closed

### Mode B — bounded skeptical escalation
Use when:
- edge is meaningful
- one narrow ambiguity is carrying the decision
- one or two targeted checks could materially improve accuracy

Target behavior:
- bounded internal audit
- bounded independent search/fetch within runtime-enforced budgets
- decide with explicit statement of what was verified, which sources were chosen, and what remained unresolved

### Mode C — not-ready / re-open recommended
Use when:
- the required verification is broader than a responsible bounded check
- the case effectively needs new research rather than final judgment
- market context gaps prevent safe autonomous action

Target behavior:
- do not hide the inadequacy
- return a non-action or not-ready packet
- state exactly what verification is still required

## Reporting requirements

Decision-Maker should make verification behavior legible.

Every packet should make clear, at least in `audit.notes`, `epistemic_status`, or related packet fields:
- whether only synthesis was used
- whether bounded internal audit occurred
- whether targeted source checks occurred
- which specific ambiguity or crux motivated escalation
- which search queries were used
- which external sources were consulted and why
- why verification remained bounded
- what remains unresolved

## Policy preference order

When choosing between two verification moves, prefer this order:

1. verify the exact crux
2. verify freshness / source-of-truth mechanics
3. verify the strongest countercase
4. only then expand into broader reread

## Implementation guidance

Runtime should pass a structured verification policy into Decision-Maker context, including:
- default mode
- default artifact budget
- default external-source budget
- escalation triggers
- hard instruction that full duplicate synthesis is not the default

Decision-Maker should treat this as a real budget and decision discipline, not decorative prose.
